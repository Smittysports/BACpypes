#!/usr/bin/python
'''
Customize the application for the simulator
'''

from bacpypes.debugging import ModuleLogger
from bacpypes.app import BIPForeignApplication, BIPSimpleApplication
from bacpypes.local.device import LocalDeviceObject
from bacpypes.primitivedata import ObjectIdentifier, Date, Time
from bacpypes.basetypes import ObjectTypesSupported, TimeStamp, DateTime, PriorityArray
from bacpypes.constructeddata import ArrayOf, Any
from bacpypes.object import register_object_type
from object_utils import load_file
from property_defaults import default_property_values
from writeproperty import WriteProperty
from readproperty import ReadProperty
from readpropertymultiple import ReadPropertyMultiple
from createdeleteobject import CreateObject, DeleteObject
from backuprestore import BackupRestore, ReinitializeDevice
from atomicreadfile import AtomicReadFile
from atomicwritefile import AtomicWriteFile

# debugging
_debug = 0
_log = ModuleLogger(globals())

@register_object_type(vendor_id=10)
class SimulatorDevice(LocalDeviceObject):
    def __init__(self, **kwargs):

        initial_property_values = dict(
            profileName = "10-SIM-DEVICE",
            systemStatus = 'operational',
            vendorName = 'Schneider Electric',
            vendorIdentifier = 10,
            modelName = 'BACpypes',
            firmwareRevision = '???',
            applicationSoftwareVersion = '???',
            location = '',
            protocolVersion = 1,
            protocolRevision = 16,
            #protocolServicesSupported -- set by application,
            #protocolObjectTypesSupported -- set by application,
            #objectList -- built in,
            structuredObjectList = [],
            maxApduLengthAccepted = 1476,
            segmentationSupported = 'noSegmentation',
            vtClassesSupported = [],
            activeVtSessions = [],
            #localTime -- built in,
            #localDate -- built in,
            utcOffset = 0,
            daylightSavingsStatus = False,
            apduSegmentTimeout = 2000,
            apduTimeout = 3000,
            numberOfApduRetries = 3,
            timeSynchronizationRecipients = [],
            maxMaster = 0,
            maxInfoFrames = 0,
            deviceAddressBinding = [],
            databaseRevision = 1,
            configurationFiles = [],
            lastRestoreTime = TimeStamp(dateTime=DateTime(date=Date(), time=Time())),
            backupFailureTimeout = 0,
            backupPreparationTime = 30,
            restorePreparationTime = 30,
            restoreCompletionTime = 180,
            backupAndRestoreState = 'idle',
            activeCovSubscriptions = [],
            maxSegmentsAccepted = 0,
            slaveProxyEnable = [],
            autoSlaveDiscovery = [],
            slaveAddressBinding = [],
            manualSlaveAddressBinding = [],
            lastRestartReason = 'unknown',
            timeOfDeviceRestart = TimeStamp(dateTime=DateTime(date=Date(), time=Time())),
            restartNotificationRecipients = [],
            utcTimeSynchronizationRecipients = [],
            timeSynchronizationInterval = 0,
            alignIntervals = False,
            intervalOffset = 0,
        )

        # Update with supplied values
        initial_property_values.update(kwargs)

        # proceed to init the device...
        LocalDeviceObject.__init__(self, **initial_property_values)

class SimulatorApplication(object):
    backup_restore = BackupRestore()
    txt_msg_commands = {}
   
    @classmethod
    def new_local(cls, device, local_addr):
        class LocalSimuator(SimulatorApplication, BIPSimpleApplication):
            pass
        return LocalSimuator(device, local_addr)

    @classmethod
    def new_foreign(cls, device, local_addr, bbdm_add, ttl):
        class ForeignSimulator(SimulatorApplication, BIPForeignApplication):
            pass
        return ForeignSimulator(device, local_addr, bbdm_add, ttl)

    @classmethod
    def enable_readproperty(cls):
        def handler(self, apdu):
            resp = ReadProperty(self, apdu)
            self.response(resp)
        cls.do_ReadPropertyRequest = handler

    @classmethod
    def enable_rpm(cls):
        def handler(self, apdu):
            resp = ReadPropertyMultiple(self, apdu)
            self.response(resp)
        cls.do_ReadPropertyMultipleRequest = handler

    @classmethod
    def enable_create(cls):
        def handler(self, apdu):
            resp = CreateObject(self, apdu)
            self.response(resp)
        cls.do_CreateObjectRequest = handler

    @classmethod
    def enable_delete(cls):
        def handler(self, apdu):
            resp = DeleteObject(self, apdu)
            self.response(resp)
        cls.do_DeleteObjectRequest = handler

    @classmethod
    def enable_writability(cls):
        def handler(self, apdu):
            resp = WriteProperty(self, apdu)
            self.response(resp)
        cls.do_WritePropertyRequest = handler
   
    @classmethod
    def enable_reinitializedevice(cls):
        def handler(self, apdu):
            resp = ReinitializeDevice(self, apdu)
            self.response(resp)
            
        cls.do_ReinitializeDeviceRequest = handler

    @classmethod
    def enable_atomicreadfile(cls):
        def handler(self, apdu):
            resp = AtomicReadFile(self, apdu)
            self.response(resp)
            
        cls.do_AtomicReadFileRequest = handler

    @classmethod
    def enable_atomicwritefile(cls):
        def handler(self, apdu):
            resp = AtomicWriteFile(self, apdu)
            self.response(resp)
            
        cls.do_AtomicWriteFileRequest = handler

    def create_object(self, cls, instance, name, properties=None):
        if not properties:
            properties = {}

        properties['objectIdentifier'] = (cls.objectType, instance)
        properties['objectName'] = name

        for propid in cls._properties:
            # if already defined, skip it!
            if propid in properties:
                continue

            # fill in default values for remaining properties
            elif propid in default_property_values:
                default_value = default_property_values[propid]

                if cls.objectType in default_value:
                    properties[propid] = default_value[cls.objectType]

                elif 'default' in default_value:
                    # Do not use the 'default' for the priorityArray or it re-uses it across all objects
                    # It should still be created manually
                    if (propid == 'priorityArray'):
                        properties[propid] = PriorityArray()
                    else:
                        properties[propid] = default_value['default']
        return cls(**properties)


    def reset_object_list(self):
        self.objectName = {self.localDevice.objectName: self.localDevice}
        self.objectIdentifier = {self.localDevice.objectIdentifier: self.localDevice}
        self.localDevice.objectList = ArrayOf(ObjectIdentifier)([self.localDevice.objectIdentifier])


    def load_objects_from_file(self, theFile):
        object_table = load_file(theFile)
        for cls, config in object_table:
            for cfg in config:
                self.add_object(self.create_object(cls, *cfg))

    def initialize_configuration_files(self):
        """ The configuration files are created and configured internally so that
        they are not reliant on an external config file that can break it.
        """
        if (len(self.backup_restore.configFiles) == 0):
            newObjectIdentifiers = []
            self.add_object(self.backup_restore.createConfigurationFileObject('BACnet_Configuration_File_1', 100, 'streamAccess'))
            newObjectIdentifiers.append(ObjectIdentifier('file', 100))

            self.add_object(self.backup_restore.createConfigurationFileObject('BACnet_Configuration_File_2', 101, 'recordAccess'))
            newObjectIdentifiers.append(ObjectIdentifier('file', 101))
            
            self.add_object(self.backup_restore.createConfigurationFileObject('BACnet_Configuration_File_3', 102, 'streamAccess', True))
            newObjectIdentifiers.append(ObjectIdentifier('file', 102))
            
            self.add_object(self.backup_restore.createConfigurationFileObject('BACnet_Configuration_File_4', 103, 'recordAccess', True))
            newObjectIdentifiers.append(ObjectIdentifier('file', 103))

            self.backup_restore.configFileAnyArray = Any(ArrayOf(ObjectIdentifier)(newObjectIdentifiers))

    def update_configuration_file_sizes(self):
        # Change the filesize of the file object to reflect the configuration backup file
        self.backup_restore.updateFileSizes()

        for configFile in self.backup_restore.configFiles:
            fileobj = self.get_object_id(ObjectIdentifier('file', configFile.id))
            fileobj.WriteProperty('fileSize', configFile.size, direct = True)
            if (configFile.access == 'recordAccess'):
                fileobj.WriteProperty('recordCount', configFile.recordCount, direct = True)

    def get_supported_object_types(self):
        # claim to support everything...
        return list(ObjectTypesSupported.bitNames.keys())


    def get_supported_services(self):
        # Base set of services
        services = ['readProperty', 'writeProperty', 'iAm', 'whoIs', 'unconfirmedTextMessage']

        if getattr(self, 'do_ReadPropertyMultipleRequest', None):
            services.append('readPropertyMultiple')

        if getattr(self, 'do_CreateObjectRequest', None):
            services.append('createObject')

        if getattr(self, 'do_DeleteObjectRequest', None):
            services.append('deleteObject')

        return services


    def do_UnconfirmedTextMessageRequest(self, apdu):
        try:
            instruction = apdu.message.split(None, 1)
            cmd = instruction[0]
            arg = instruction[1] if len(instruction) > 1 else ""

            self.txt_msg_commands[cmd](arg)

        except KeyError as key:
            _log.exception("unknown text message command: %s", key)



# a decorator to add text message handlers to the Application
def text_msg_handler(command):
    def register(function):
        SimulatorApplication.txt_msg_commands[command] = function
        return function
    return register

