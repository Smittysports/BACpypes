#!/usr/bin/env python

"""
A module to provide an atomic read file implementation.

This module currently only works for reading a configuration file.

TODO: Get this module to work with any file

"""

from bacpypes.primitivedata import Integer, Unsigned, OctetString
from bacpypes.apdu import AtomicReadFileACK, AtomicReadFileACKAccessMethodChoice, AtomicReadFileACKAccessMethodRecordAccess, \
                        AtomicReadFileACKAccessMethodStreamAccess, \
                        RejectPDU, RejectReason, AbortPDU, AbortReason, Error

from bacpypes.errors import ExecutionError, MissingRequiredParameter

def AtomicReadFile(self, apdu):

    if (apdu.fileIdentifier[0] != 'file'):
        raise ExecutionError('services', 'inconsistentObjectType')

    # get the object
    obj = self.get_object_id(apdu.fileIdentifier)
    if not obj:
        raise ExecutionError('object', 'unknownObject')

    if apdu.accessMethod.recordAccess:
        # check against the object
        if obj.fileAccessMethod != 'recordAccess':
            raise ExecutionError('services', 'invalidFileAccessMethod')

        # simplify
        record_access = apdu.accessMethod.recordAccess

        # check for required parameters
        if record_access.fileStartRecord is None:
            raise MissingRequiredParameter("fileStartRecord required")
        if record_access.requestedRecordCount is None:
            raise MissingRequiredParameter("requestedRecordCount required")
      
        dataRead, isEOF = self.backup_restore.readConfigurationFile(
            obj.objectName,
            'recordAccess',
            record_access.fileStartRecord,
            record_access.requestedRecordCount,
            )        

        resp = AtomicReadFileACK(context=apdu,
            endOfFile = isEOF,
            accessMethod = AtomicReadFileACKAccessMethodChoice(
                recordAccess = AtomicReadFileACKAccessMethodRecordAccess(
                    fileStartRecord = Integer(record_access.fileStartRecord),
                    returnedRecordCount = Unsigned(1),
                    fileRecordData = [ OctetString(dataRead) ]
                )
            )
        )

    elif apdu.accessMethod.streamAccess:
        # check against the object
        if obj.fileAccessMethod != 'streamAccess':
            raise ExecutionError('services', 'invalidFileAccessMethod')

        # simplify
        stream_access = apdu.accessMethod.streamAccess

        # check for required parameters
        if stream_access.fileStartPosition is None:
            raise MissingRequiredParameter("fileStartPosition required")
        
        if stream_access.requestedOctetCount is None:
            raise MissingRequiredParameter("requestedOctetCount required")

        dataRead, isEOF = self.backup_restore.readConfigurationFile(
            obj.objectName,
            'streamAccess',
            stream_access.fileStartPosition,
            stream_access.requestedOctetCount,
            )

        resp = AtomicReadFileACK(context=apdu,
            endOfFile = isEOF,
            accessMethod = AtomicReadFileACKAccessMethodChoice(
                streamAccess = AtomicReadFileACKAccessMethodStreamAccess(
                    fileStartPosition = stream_access.fileStartPosition,
                    fileData = OctetString(dataRead),
                    ),
                ),
            )

    # Test only: The client should abort the restore if it receives one of these
    # BACnet-AbortPDU, BACnet-ErrorPDU, or BACnet-RejectPDU
    #resp = AbortPDU(srv = 1, reason = 'other', context=apdu)
    #resp = Error(errorClass='object', errorCode='unknownObject', context=apdu)
    #resp = RejectPDU(reason = 'other', context=apdu)

    self.response(resp)
