#!/usr/bin/env python

'''
backuprestore.py
'''
from bacpypes.basetypes import Date, Time, DateTime, NameValue
from bacpypes.apdu import SimpleAckPDU, RejectPDU, RejectReason, AbortPDU, AbortReason, Error
from bacpypes.primitivedata import ObjectIdentifier
from bacpypes.constructeddata import Any, ArrayOf
from bacpypes.object import FileObject
from threading import Timer
from os import path

class ConfigFile():
    def __init__(self, name, id, access, isEmpty = False):
        self.name = name
        self.id = id
        self.access = access
        self.size = 0
        self.recordCount = 0
        self.isEmpty = isEmpty

class BackupRestore():
    """
    The BackupStates are defined as:
        class BackupState(Enumerated):
        enumerations = \
            { 'idle':0
            , 'preparingForBackup':1
            , 'preparingForRestore':2
            , 'performingABackup':3
            , 'performingARestore':4
            , 'backupFailure':5
            , 'restoreFailure':6
            }
    """

    def __init__(self):
        # Note: Currently, the backupPreparationTime, restorePreparationTimeSeconds, and restoreCompletionTimeSeconds
        # are configured in the initial_property_values dict in the SimulatorDevice in application.py
        # TODO: Find a good way to use this class to update the initial_property_values
        self.backupPreparationTimeSeconds = 30
        self.prepTimeTimer = 5 # Used with a timer to signal that the preparation is done
        self.restorePreparationTimeSeconds = 30
        self.restoreCompletionTimeSeconds = 180
        self.state = 0
        self.timer = None
        self.configFiles = []
        self.configFileAnyArray = Any()
        # Used to validate that protocol version < 10 works (it does not utilize preparation time)
        # To test this, make sure to set the protocolRevision in application.py
        self.revision = 16

    def preparationTimer(self, isBackup):
        """ This function is used as a way to artificially signal that preparation is done.
        It is used in conjunction with self.prepTimeTimer.

        Ex... The backupPreparationTimeSeconds is 30 seconds but we want to signal that the
              file is done being created in 5 so we do not have to wait the full 30. 
        """
        if (isBackup):
            self.state = 3
        else:
            self.state = 4

    def createConfigurationFiles(self):
        """ The BACnet standard requires that:
            - A file can be accessed via stream mode
            - A file can be accessed via record mode (and that the server can have a mix of both stream and record)
            - A configuration file of size 0 can be backed up and restored
        """
        for configFile in self.configFiles:
            fileHandle = open(configFile.name, "w")
            if (configFile.isEmpty == True):
                configFile.recordCount = 0
            else:
                if (configFile.access == 'streamAccess'):
                    fileHandle.write("Config file")
                else:
                    fileHandle.write("Record: 1 => Test 1\n")
                    fileHandle.write("Record: 2 => Test 2\n")
                    fileHandle.write("Record: 3 => Test 3\n")
                    configFile.recordCount = 3
            fileHandle.close()
        
    def updateFileSizes(self):
        for configFile in self.configFiles:
            configFile.size = path.getsize(configFile.name)
    
    def readConfigurationFile(self, fileName, access, start, count):
        """ Returns the data read from the file and True if eof, or False if there is more data to read
            
            @param fileName The name of the configuration file to read from
            @param access Can be streamAccess or recordAccess
            @param start The fileStartPosition for streamAccess or fileStartRecord for recordAccess
            @param count The requestedOctetCount for streamAccess or requestedRecordCount for recordAccess

            @return tuple containing the bytes read and whether the EOF was reached
        """
        eof = True
        fileHandle = open(fileName + ".txt", "rb")
        fileHandle.seek(start)

        if (access == 'streamAccess'):
            bytes = fileHandle.read(count)
        else:
            bytes = fileHandle.readline()
            for i in range(count - 1):
                bytes += fileHandle.readline()
        fileHandle.close()
        return bytes , eof
    
    def writeConfigurationFile(self, fileName, access, start, count, data):
        """ Writes the data passed in to the file

            @param fileName The name of the configuration file to write to
            @param access Can be streamAccess or recordAccess
            @param start The fileStartPosition for streamAccess or fileStartRecord for recordAccess
            @param count Not used for streamAccess and recordCount for recordAccess
            @param data The data to write to the file
        """
        eof = True
        fileHandle = open(fileName + ".txt", "w")
        fileHandle.seek(start)

        if (access == 'streamAccess'):
            # The data for a stream is 'fileData' which is a OctetString
            fileHandle.write(data.decode())
        else:
            # The data for a record is 'fileRecordData' which is a SequenceOf(OctetString)
            for octetstring in data:
                # The octetstring has extra crlf in it
                decodedline = octetstring.decode()
                decodedline = decodedline.splitlines()
                for decoded in decodedline:
                    fileHandle.write(decoded + "\n")
        fileHandle.close()

    
    def startBackup(self):
        self.state = 1
        self.createConfigurationFiles()

        if ((self.revision >= 10) and self.backupPreparationTimeSeconds > 0):
            self.timer = Timer(self.prepTimeTimer, self.preparationTimer, args = [True])
            self.timer.start()
        else:
            self.state = 3

    def startRestore(self):
        self.state = 2
        if ((self.revision >= 10) and self.restorePreparationTimeSeconds > 0):
            self.timer = Timer(self.prepTimeTimer, self.preparationTimer, args = [False])
            self.timer.start()
        else:
            self.state = 4

    def endBackupRestore(self):
        if (self.timer != None):
            self.timer.cancel()
            self.timer = None
        self.state = 0

    def createConfigurationFileObject(self, name, id, access, isEmpty = False):
        """ Create a configuration file with some default variables
            @param name The name of the file that this File object will reference
            @param id The ID of the File object
            @param access Can be streamAccess or recordAccess

            @return object The BACnet object file that can be added to the application with add_object()
        """
        object = FileObject(
            objectIdentifier = ("file", id),
            objectName = name,
            description ="Configuration file",
            profileName = "",
            profileLocation = "",
            fileType = "txt",
            fileSize = 0,
            modificationDate = DateTime(date=Date().now().value, time=Time().now().value),
            archive = False,
            readOnly = False,
            fileAccessMethod = access,
            recordCount = 0,
            tags = ArrayOf(NameValue)()
        )

        self.configFiles.append(ConfigFile(name + ".txt", id, access, isEmpty))
        return object

def ReinitializeDevice(application, apdu):
    """
    The ReinitializeDeviceRequest contains a sequence that contains the desired state and an
    optional password. It is defined as:

        class ReinitializeDeviceRequest(ConfirmedRequestSequence):
        serviceChoice = 20
        sequenceElements = \
            [ Element('reinitializedStateOfDevice', ReinitializeDeviceRequestReinitializedStateOfDevice, 0)
            , Element('password', CharacterString, 1, True)
            ]
    
    For reference, the ReadProperyMultiple uses this:

        class ReadPropertyMultipleRequest(ConfirmedRequestSequence):
        serviceChoice = 14
        sequenceElements = \
            [ Element('listOfReadAccessSpecs', SequenceOf(ReadAccessSpecification))
            ]
    """

    # Test only: The client should abort the restore if it receives one of these
    # BACnet-AbortPDU, BACnet-ErrorPDU, or BACnet-RejectPDU
    #resp = AbortPDU(srv = 1, reason = 'other', context=apdu)
    #resp = Error(errorClass='object', errorCode='unknownObject', context=apdu)
    #resp = RejectPDU(reason = 'other', context=apdu)

    if (apdu.reinitializedStateOfDevice == "startBackup"):
        # The BACnet File objects, that will link to the actual files, need to be created if they have not already
        application.initialize_configuration_files()
        application.backup_restore.startBackup()
        application.update_configuration_file_sizes()
    elif (apdu.reinitializedStateOfDevice == "endBackup"):
        application.backup_restore.endBackupRestore()
    elif (apdu.reinitializedStateOfDevice == "startRestore"):
        application.backup_restore.startRestore()
    elif (apdu.reinitializedStateOfDevice == "endRestore"):
        application.backup_restore.endBackupRestore()

    return(SimpleAckPDU(context=apdu))
