#!/usr/bin/env python
'''
Configuration options combined from command line arguments and config file
'''
from bacpypes.pdu import Address
import configparser
import time

_default_config_options = {
    'deviceName': 'BACPYPES_REFERENCE',
    'address': '0.0.0.0:47808',
    'deviceIdentifier': '4194302',

    # exclude: bbmdAddress from defaults!
    'foreignTTL': '300',

    'readPropertyMultiple': 'Yes',
    'createAndDelete': 'Yes',
    'writablity': 'Yes',

    'timeout' : '0',
    'objectConfig' : '',
    'pluginDir' : '',
}

class SimulatorConfig(object):

    def __init__(self, cmd_args):
        self.args = cmd_args

        self.config = configparser.ConfigParser(_default_config_options)
        self.config.read_file(cmd_args.ini)
   
        if not self.config.has_section('BACpypes'):
            print("INI file with BACpypes section required")

    def isConfigured(self):
        if not self.config.has_section('BACpypes'):
            return False
        else:
            return True
    @property
    def device_name(self):
        if self.args.deviceName:
            return self.args.deviceName
        else:
            return self.config.get('BACpypes', 'deviceName')

    @property
    def local_address(self):
        if self.args.localAddress:
            return self.args.localAddress
        else:
            addr = self.config.get('BACpypes', 'address')
            return Address(addr)

    @property
    def device_id(self):
        if self.args.deviceIdentifier:
            instance = self.args.deviceIdentifier
        else:
            instance = self.config.getint('BACpypes', 'deviceIdentifier')
        return ('device', instance)

    @property
    def foreign_device_enabled(self):
        return self.args.bbmdAddress or \
               self.config.has_option('BACpypes', 'bbmdAddress')

    @property
    def bbmd_address(self):
        if self.args.bbmdAddress:
            return self.args.bbmdAddress
        else:
            addr = self.config.get('BACpypes', 'bbmdAddress')
            return Address(addr)

    @property
    def foriegn_TTL(self):
        if self.args.foreignTTL:
            return self.args.foreignTTL
        else:
            return self.config.getint('BACpypes', 'foreignTTL')

    @property
    def rpm_enabled(self):
        if self.args.no_rpm:
            return False
        else:
            return self.config.getboolean('BACpypes', 'readPropertyMultiple')

    @property
    def create_delete_enabled(self):
        if self.args.no_createDelete:
            return False
        else:
            return self.config.getboolean('BACpypes', 'createAndDelete')

    @property
    def writablity_enabled(self):
        if self.args.no_writablity:
            return False
        else:
            return self.config.getboolean('BACpypes', 'writablity')

    @property
    def timeout(self):
        if self.args.timeout:
            return self.args.timeout
        else:
            return self.config.getint('BACpypes', 'timeout')

    @property
    def object_config(self):
        if self.args.objects:
            return self.args.objects
        else:
            return self.config.get('BACpypes', 'objectConfig')


    @property
    def plugin_dir(self):
        if self.args.objects:
            return self.args.pluginDir
        else:
            return self.config.get('BACpypes', 'pluginDir')

