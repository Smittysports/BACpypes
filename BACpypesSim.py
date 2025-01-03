#!/usr/bin/python
'''
Run an object server which may register as a foreign device with a BBMD.

This simulator is used to test AWS. It uses the property_defaults.default_property_values() function
to load default values for all usable properties of all objects that are created. A config file can
be passed in that modifies the desiredproperty values.

History:
1.3.3 - modified BACpypes BIPForeign to repeatedly register to BBMD with 10 second intervals
2.0.0 - Updated to work with Python 3.11.8 (3/6/2024)
'''

import argparse
import time

import importlib

from bacpypes.debugging import ModuleLogger
from bacpypes.consolelogging import ArgumentParser

from bacpypes.core import run, stop
from bacpypes.pdu import Address
from bacpypes.task import FunctionTask

from configuration import SimulatorConfig
from application import SimulatorDevice, SimulatorApplication, text_msg_handler

# debugging (change to 1 and Launch like this to enable the logging: python BACpypesSim.py --debug __main__)
_debug = 0
_log = ModuleLogger(globals())

__version__ = '2.0.3'
__svn_rev__ = 'se1'

argument_parser = ArgumentParser(description=__doc__)
argument_parser.add_argument('--version', action='version', version='%(prog)s {0}'.format(__version__))

argument_parser.add_argument('--ini', default="BACpypes.ini", type=argparse.FileType('r'), help="Simulator configuration file")
argument_parser.add_argument('-i', '--interactive', action="store_true", help="Run a prompt to enter commands")

argument_parser.add_argument('--localAddress', type=Address, help="The IP and port of the local address the simulator is running on")
argument_parser.add_argument('--bbmdAddress', type=Address, help="The IP and port of a BBMD to register with as foreign device")
argument_parser.add_argument('--foreignTTL', type=int, help="Time to Live for foreign device registration")

argument_parser.add_argument('--deviceName', help="The name to use for the device object")
argument_parser.add_argument('--deviceIdentifier', type=int, help="The ID to use for the device object")

argument_parser.add_argument('--objects', help="Path to initial object configuation")
argument_parser.add_argument('--timeout', type=int, help="Time in seconds before simulator should automatically terminate")
argument_parser.add_argument('--pluginDir', help="Directory to load test plugins from")

argument_parser.add_argument('--no-rpm', action='store_true', help="Disable read property multiple")
argument_parser.add_argument('--no-createDelete', action="store_true", help="Disable create and delete objects")
argument_parser.add_argument('--no-writablity', action="store_true", help="Disable optional writablity")

@text_msg_handler("shutdown")
def shutdownHandler(argument):
    if _debug: _log.debug("shutdown message received")
    stop()


@text_msg_handler("execute")
def executeHandler(plugin_spec):
    if _debug: _log.debug("execute message received")

    plugin = plugin_spec.split(None,1)
    name = plugin[0]
    args = plugin[1] if len(plugin) > 1 else ""

    try:
        plugin = importlib.import_module(name)
        plugin.execute(local_application, args)

    except Exception as e:
        _log.exception("execute error has occurred: %s", e)


@text_msg_handler("objects")
def objectsHandler(config_path):
    if _debug: _log.debug("objects message received")

    try:
        with open(config_path, 'r') as objects_file:
            local_application.reset_object_list()
            local_application.load_objects_from_file(objects_file)
            local_device.protocolObjectTypesSupported = local_application.get_supported_object_types()

    except Exception as e:
        _log.exception("objects: error has occurred: %s", e)

try:
    sim_config = SimulatorConfig(argument_parser.parse_args())

    print("Local address = ", sim_config.local_address)
    print("Device name = ", sim_config.device_name)
    print("Device ID = ", sim_config.device_id)
    print("Simulator timeout = ", sim_config.timeout)

    # Create the BACnet Device object that will hold all of the desired BACnet objects
    local_device = SimulatorDevice(
        objectIdentifier = sim_config.device_id,
        objectName = sim_config.device_name,
        firmwareRevision = __svn_rev__,
        applicationSoftwareVersion = __version__)

    SimulatorApplication.enable_create()
    SimulatorApplication.enable_delete()
    SimulatorApplication.enable_writability()
    SimulatorApplication.enable_reinitializedevice()
    SimulatorApplication.enable_readproperty()
    SimulatorApplication.enable_atomicreadfile()
    SimulatorApplication.enable_atomicwritefile()

    # create either a foreign device application
    if sim_config.foreign_device_enabled:
        local_application = SimulatorApplication.new_foreign(
            local_device,
            sim_config.local_address,
            sim_config.bbmd_address,
            sim_config.foriegn_TTL)
    # or a normal (local) application
    else:
        local_application = SimulatorApplication.new_local(
            local_device,
            sim_config.local_address)

    if sim_config.object_config:
        with open(sim_config.object_config, 'r') as cfg_file:
            local_application.load_objects_from_file(cfg_file)
    
    # initialize the device's objects and services bitstrings
    #local_device.protocolObjectTypesSupported = local_application.get_supported_object_types()
    #local_device.protocolServicesSupported = local_application.get_supported_services()

    # timeout the simulator after some time
    if sim_config.timeout:
        FunctionTask(stop).install_task(time.time() + sim_config.timeout)    

    run()

except Exception as e:
    _log.exception("an error has occurred: %s", e)

finally:
    if _debug: _log.debug("finishing")
