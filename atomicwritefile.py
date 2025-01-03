#!/usr/bin/env python

"""
A module to provide an atomic write file implementation.

This module currently only works for writing a configuration file.

TODO: Get this module to work with any file

"""

from bacpypes.primitivedata import Integer, Unsigned, OctetString
from bacpypes.apdu import AtomicWriteFileACK, \
                        RejectPDU, RejectReason, AbortPDU, AbortReason, Error

from bacpypes.errors import ExecutionError, MissingRequiredParameter

def AtomicWriteFile(self, apdu):

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
        if record_access.recordCount is None:
            raise MissingRequiredParameter("recordCount required")
        if record_access.fileRecordData is None:
            raise MissingRequiredParameter("fileRecordData required")

        # check for read-only
        if obj.readOnly:
            raise ExecutionError('services', 'fileAccessDenied')

        self.backup_restore.writeConfigurationFile(
            obj.objectName,
            'recordAccess',
            record_access.fileStartRecord,
            record_access.recordCount,
            record_access.fileRecordData
            )

        resp = AtomicWriteFileACK(context=apdu,
            fileStartRecord = record_access.fileStartRecord,
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
        if stream_access.fileData is None:
            raise MissingRequiredParameter("fileData required")

        # check for read-only
        if obj.readOnly:
            raise ExecutionError('services', 'fileAccessDenied')

        self.backup_restore.writeConfigurationFile(
            obj.objectName,
            'streamAccess',
            stream_access.fileStartPosition,
            0,
            stream_access.fileData
            )
        
        resp = AtomicWriteFileACK(context=apdu,
            fileStartPosition=stream_access.fileStartPosition,
            )

    # return the result
    self.response(resp)
