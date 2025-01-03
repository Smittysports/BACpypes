#!/usr/bin/env python

'''
A module to provide a create and delete object implementation.
'''

from bacpypes.debugging import bacpypes_debugging, ModuleLogger

from bacpypes.apdu import Error, CreateObjectError, SimpleAckPDU, CreateObjectACK
from bacpypes.primitivedata import CharacterString
from bacpypes.basetypes import ErrorType
from bacpypes.object import get_object_class
from bacpypes.errors import ExecutionError

# some debugging
_debug = 0
_log = ModuleLogger(globals())


@bacpypes_debugging
def CreateObject(application, apdu):

    def make_object_id(objType):
        i = 1
        while (objType, i) in application.objectIdentifier: i += 1
        return (objType, i)

    def make_unique_name(new_object_id):
        i = 0
        new_name = "{0}.{1}".format(new_object_id[0], new_object_id[1])
        while new_name in application.objectName:
            i+=1
            new_name = "{0}.{1}.{2}".format(new_object_id[0], new_object_id[1], i)
        return new_name


    # tracking where a failure may occur
    first_failed_element = 0
    try:
        # create a new identifier
        if apdu.objectSpecifier.objectType:
            new_object_id = make_object_id(apdu.objectSpecifier.objectType)
        elif apdu.objectSpecifier.objectIdentifier in application.objectIdentifier:
            raise ExecutionError(errorClass='object', errorCode='objectIdentifierAlreadyExists')
        else:
            new_object_id = apdu.objectSpecifier.objectIdentifier

        # being a little restrictive here: only accept the object name.
        # this could be more generic,
        if apdu.listOfInitialValues:
            if len(apdu.listOfInitialValues) > 1:
                first_failed_element = 2
                raise ExecutionError(errorClass='property', errorCode='valueOutOfRange')

            elif apdu.listOfInitialValues[0].propertyIdentifier != 'objectName':
                first_failed_element = 1
                raise ExecutionError(errorClass='property', errorCode='valueOutOfRange')

            # extract the new name
            new_object_name = apdu.listOfInitialValues[0].value.cast_out(CharacterString)
            if new_object_name in application.objectName:
                first_failed_element = 1
                raise ExecutionError(errorClass='property', errorCode='valueOutOfRange')

        else:
            new_object_name = make_unique_name(new_object_id)

        # create the object, and add it to the application
        cls = get_object_class(new_object_id[0])

        new_object = application.create_object(cls, new_object_id[1], new_object_name)
        application.add_object(new_object)

        resp = CreateObjectACK(
            objectIdentifier = new_object.objectIdentifier,
            context=apdu
        )
    except ExecutionError as e:
        resp = CreateObjectError(
            errorType = ErrorType(errorClass=e.errorClass, errorCode=e.errorCode),
            firstFailedElementNumber = first_failed_element,
            context=apdu
        )
    except:
        resp = CreateObjectError(
            errorType = ErrorType(errorClass='device', errorCode='other'),
            firstFailedElementNumber = first_failed_element,
            context=apdu
        )

    # return the create object result
    return resp


@bacpypes_debugging
def DeleteObject(application, apdu):
    obj = application.get_object_id(apdu.objectIdentifier)

    if not obj:
        resp = Error(errorClass='object', errorCode='unknownObject', context=apdu)

    elif obj is application.localDevice:
        resp=Error(errorClass='object', errorCode='objectDeletionNotPermitted', context=apdu)

    else:
        application.delete_object(obj)
        resp = SimpleAckPDU(context=apdu)

    # return the delete object result
    return resp
