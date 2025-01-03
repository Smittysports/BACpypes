#!/usr/bin/env python

"""
A module to provide an read property multiple implementation.
"""

from bacpypes.debugging import bacpypes_debugging, ModuleLogger

from bacpypes.primitivedata import Atomic, Unsigned
from bacpypes.constructeddata import Array, Any
from bacpypes.basetypes import ErrorType
from bacpypes.apdu import ReadPropertyMultipleACK, ReadAccessResult, ReadAccessResultElement, ReadAccessResultElementChoice
from bacpypes.object import PropertyError
from bacpypes.errors import ExecutionError

# some debugging
_debug = 0
_log = ModuleLogger(globals())

#
#   ReadPropertyToAny
#

@bacpypes_debugging
def ReadPropertyToAny(obj, propertyIdentifier, propertyArrayIndex=None):
    """Read the specified property of the object, with the optional array index,
    and cast the result into an Any object."""
    if _debug: ReadPropertyToAny._debug("ReadPropertyToAny %s %r %r", obj, propertyIdentifier, propertyArrayIndex)

    # get the datatype
    datatype = obj.get_datatype(propertyIdentifier)
    if _debug: ReadPropertyToAny._debug("    - datatype: %r", datatype)

    # get the value
    value = obj.ReadProperty(propertyIdentifier, propertyArrayIndex)
    if _debug: ReadPropertyToAny._debug("    - value: %r", value)
    if value is None:
        raise ExecutionError(errorClass='property', errorCode='unknownProperty')

    # change atomic values into something encodeable
    if issubclass(datatype, Atomic):
        value = datatype(value)
    elif issubclass(datatype, Array) and (propertyArrayIndex is not None):
        if propertyArrayIndex == 0:
            value = Unsigned(value)
        elif issubclass(datatype.subtype, Atomic):
            value = datatype.subtype(value)
        elif not isinstance(value, datatype.subtype):
            typeErrorStr = "invalid result datatype, expecting %s and got %s" \
                % (datatype.subtype.__name__, type(value).__name__)
            raise TypeError(typeErrorStr)

    # TODO Encode the Event Log log_buffer, start_time, and stop_time correctly
    elif not isinstance(value, datatype):
        typeErrorStr = "invalid result datatype, expecting %s and got %s" \
            % (datatype.__name__, type(value).__name__)
        raise TypeError(typeErrorStr)
    if _debug: ReadPropertyToAny._debug("    - encodeable value: %r", value)

    # encode the value
    result = Any()
    result.cast_in(value)
    if _debug: ReadPropertyToAny._debug("    - result: %r", result)

    # return the object
    return result

#
#   ReadPropertyToResultElement
#

@bacpypes_debugging
def ReadPropertyToResultElement(obj, propertyIdentifier, propertyArrayIndex=None):
    """Read the specified property of the object, with the optional array index,
    and cast the result into an Any object."""
    if _debug: ReadPropertyToResultElement._debug("ReadPropertyToResultElement %s %r %r", obj, propertyIdentifier, propertyArrayIndex)

    # save the result in the property value
    read_result = ReadAccessResultElementChoice()

    try:
        read_result.propertyValue = ReadPropertyToAny(obj, propertyIdentifier, propertyArrayIndex)
        if _debug: ReadPropertyToResultElement._debug("    - success")
    except PropertyError as error:
        if _debug: ReadPropertyToResultElement._debug("    - error: %r", error)
        read_result.propertyAccessError = ErrorType(errorClass='property', errorCode='unknownProperty')
    except ExecutionError as error:
        if _debug: ReadPropertyToResultElement._debug("    - error: %r", error)
        read_result.propertyAccessError = ErrorType(errorClass=error.errorClass, errorCode=error.errorCode)

    # make an element for this value
    read_access_result_element = ReadAccessResultElement(
        propertyIdentifier=propertyIdentifier,
        propertyArrayIndex=propertyArrayIndex,
        readResult=read_result,
        )
    if _debug: ReadPropertyToResultElement._debug("    - read_access_result_element: %r", read_access_result_element)

    # finish
    return read_access_result_element

#
#   ReadPropertyMultipleHandler
#

@bacpypes_debugging
def ReadPropertyMultiple(application, apdu):
    """Respond to a ReadPropertyMultiple Request."""
    if _debug: ReadPropertyMultiple._debug("ReadPropertyMultiple %r", apdu)

    # response is a list of read access results
    read_access_result_list = []

    # loop through the request
    for read_access_spec in apdu.listOfReadAccessSpecs:
        # get the object identifier
        objectIdentifier = read_access_spec.objectIdentifier
        if _debug: ReadPropertyMultiple._debug("    - objectIdentifier: %r", objectIdentifier)

        # check for wildcard
        if (objectIdentifier == ('device', 4194303)):
            if _debug: ReadPropertyMultiple._debug("    - wildcard device identifier")
            objectIdentifier = application.localDevice.objectIdentifier

        # get the object
        obj = application.get_object_id(objectIdentifier)
        if _debug: ReadPropertyMultiple._debug("    - object: %r", obj)

        # make sure it exists
        if not obj:
            resp = Error(errorClass='object', errorCode='unknownObject', context=apdu)
            break

        # build a list of result elements
        read_access_result_element_list = []

        # loop through the property references
        for prop_reference in read_access_spec.listOfPropertyReferences:
            # get the property identifier
            propertyIdentifier = prop_reference.propertyIdentifier
            if _debug: ReadPropertyMultiple._debug("    - propertyIdentifier: %r", propertyIdentifier)

            # get the array index (optional)
            propertyArrayIndex = prop_reference.propertyArrayIndex
            if _debug: ReadPropertyMultiple._debug("    - propertyArrayIndex: %r", propertyArrayIndex)

            # check for special property identifiers
            if propertyIdentifier in ('all', 'required', 'optional'):
                for propId, prop in obj._properties.items():
                    if _debug: ReadPropertyMultiple._debug("    - checking: %r %r", propId, prop.optional)

                    # property list is not include in these requests
                    if propId == 'propertyList':
                        continue

                    # filter the list of results
                    if (propertyIdentifier == 'all'):
                        pass
                    elif (propertyIdentifier == 'required') and (prop.optional):
                        if _debug: ReadPropertyMultiple._debug("    - not a required property")
                        continue
                    elif (propertyIdentifier == 'optional') and (not prop.optional):
                        if _debug: ReadPropertyMultiple._debug("    - not an optional property")
                        continue

                    # read the specific property
                    read_access_result_element = ReadPropertyToResultElement(obj, propId, propertyArrayIndex)

                    # check for undefined property
                    if read_access_result_element.readResult.propertyAccessError \
                        and read_access_result_element.readResult.propertyAccessError.errorCode == 'unknownProperty':
                        continue

                    # add it to the list
                    read_access_result_element_list.append(read_access_result_element)

            else:
                # read the specific property
                read_access_result_element = ReadPropertyToResultElement(obj, propertyIdentifier, propertyArrayIndex)

                # add it to the list
                read_access_result_element_list.append(read_access_result_element)

        # build a read access result
        read_access_result = ReadAccessResult(
            objectIdentifier=objectIdentifier,
            listOfResults=read_access_result_element_list
            )
        if _debug: ReadPropertyMultiple._debug("    - read_access_result: %r", read_access_result)

        # add it to the list
        read_access_result_list.append(read_access_result)

    # this is a ReadPropertyMultiple ack
    resp = ReadPropertyMultipleACK(context=apdu)
    resp.listOfReadAccessResults = read_access_result_list
    if _debug: ReadPropertyMultiple._debug("    - resp: %r", resp)

    # return the result
    return resp
