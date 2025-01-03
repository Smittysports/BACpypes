#!/usr/bin/env python

"""
A module to provide a read property implementation.

The general implementation of ReadProperty is in bacpypes.service.object.py. This
version is used to customize it specific to our use.
ex... The BACnet backup and restore procedure uses a state machine and reads from a configuration
file. This is specific to our needs and the read will obtain the needed values from the correct
place.
"""

from bacpypes.debugging import bacpypes_debugging, ModuleLogger

from bacpypes.primitivedata import Atomic, Unsigned, ObjectIdentifier, Enumerated
from bacpypes.constructeddata import Array, Any, List, ArrayOf
from bacpypes.apdu import ReadPropertyACK, RejectPDU, RejectReason, AbortPDU, AbortReason, Error
from bacpypes.object import PropertyError
from bacpypes.errors import ExecutionError

# some debugging
_debug = 0
_log = ModuleLogger(globals())

def ReadProperty(self, apdu):

    # extract the object identifier
    objId = apdu.objectIdentifier

    # check for wildcard
    if (objId == ('device', 4194303)) and self.localDevice is not None:
        objId = self.localDevice.objectIdentifier

    # get the object
    obj = self.get_object_id(objId)

    if not obj:
        raise ExecutionError(errorClass='object', errorCode='unknownObject')

    try:
        # get the datatype
        datatype = obj.get_datatype(apdu.propertyIdentifier)

        # get the value
        value_from_datatype = value_read = obj.ReadProperty(apdu.propertyIdentifier, apdu.propertyArrayIndex)
        if value_read is None:
            raise PropertyError(apdu.propertyIdentifier)

        # change atomic values into something encodeable
        if issubclass(datatype, Atomic) or (issubclass(datatype, (Array, List)) and isinstance(value_read, list)):
            value_from_datatype = datatype(value_read)
        elif issubclass(datatype, Array) and (apdu.propertyArrayIndex is not None):
            # Array index 0 represents the size of the array
            if apdu.propertyArrayIndex == 0:
                value_from_datatype = Unsigned(value_read)
            elif issubclass(datatype.subtype, Atomic):
                value_from_datatype = datatype.subtype(value_read)
            elif not isinstance(value_read, datatype.subtype):
                raise TypeError("invalid result datatype, expecting {0} and got {1}" \
                    .format(datatype.subtype.__name__, type(value_read).__name__))
        elif issubclass(datatype, List):
            value_from_datatype = datatype(value_read)
        #elif not isinstance(value_read, datatype):
        #    raise TypeError("invalid result datatype, expecting {0} and got {1}" \
        #        .format(datatype.__name__, type(value_read).__name__))

        resp = ReadPropertyACK(context=apdu)
        resp.objectIdentifier = objId
        resp.propertyIdentifier = apdu.propertyIdentifier
        resp.propertyArrayIndex = apdu.propertyArrayIndex

        if (apdu.propertyIdentifier == 'backupAndRestoreState'):
            resp.propertyValue = Any(Enumerated(self.backup_restore.state))
            # Test only: The client should abort the restore if it receives one of these
            # BACnet-AbortPDU, BACnet-ErrorPDU, or BACnet-RejectPDU
            #resp = AbortPDU(srv = 1, reason = 'other', context=apdu)
            #resp = Error(errorClass='object', errorCode='unknownObject', context=apdu)
            #resp = RejectPDU(reason = 'other', context=apdu)
        elif (apdu.propertyIdentifier == 'configurationFiles'):
            resp.propertyValue = self.backup_restore.configFileAnyArray

            # Test only: The client should abort the restore if it receives one of these
            # BACnet-AbortPDU, BACnet-ErrorPDU, or BACnet-RejectPDU
            #resp = AbortPDU(srv = 1, reason = 'other', context=apdu)
            #resp = Error(errorClass='object', errorCode='unknownObject', context=apdu)
            #resp = RejectPDU(reason = 'other', context=apdu)
        else:
            resp.propertyValue = Any()
            resp.propertyValue.cast_in(value_from_datatype)

    except PropertyError:
        raise ExecutionError(errorClass='property', errorCode='unknownProperty')

    # return the result
    self.response(resp)
