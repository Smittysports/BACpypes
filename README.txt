This is a simulated BACnet device intended for use as a reference device for testing.  It is based on the open-source BACpypes BACnet stack [1].

The simulator supports loading a set of objects at run time (from a command line switch).  Samples of the config files are in the object_configurations folder.  Also supported is runtime importing of modules - in order to execute various test senarios (test_plugins folder).  These can be copied to the TestData\BACnet folder in the SE.WorkStation.BACnet.AcceptanceTest project.

Nessisary tools for building:
Python 2.7 (on system PATH) [2]
cx_freeze [3]
7-zip (on system PATH) [4]

Note:
For errors or changes to the bacpypes stack, there is a folder for patches.  These should be applied to bacpypes before building.  Ideally, bug fixes should be submitted to bacpypes maintainer (Joel Bender).

[1] http://bacpypes.sourceforge.net/
[2] https://www.python.org/download/releases/2.7
[3] http://cx-freeze.sourceforge.net/
[4] http://www.7-zip.org/
