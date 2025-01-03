#!/usr/bin/env python

'''
A module to provide a write property implementation which supports writing anything
'''

from bacpypes.debugging import bacpypes_debugging, ModuleLogger

from bacpypes.apdu import Error, SimpleAckPDU
from bacpypes.primitivedata import CharacterString, Unsigned, Null
from bacpypes.basetypes import PriorityValue
from bacpypes.constructeddata import Array
from bacpypes.object import get_object_class, PropertyError
from bacpypes.errors import ExecutionError

from object_utils import load_file

# some debugging
_debug = 0
_log = ModuleLogger(globals())


# some utilities
def is_commandable(obj):
    return obj.objectType in (
        'analogOutput',
        'analogValue',
        'binaryOutput',
        'binaryValue',
        'bitstringValue',
        'characterstringValue',
        'datePatternValue',
        'dateValue',
        'datetimePatternValue',
        'datetimeValue',
        'integerValue',
        'largeAnalogValue',
        'multiStateOutput',
        'multiStateValue',
        'octetstringValue',
        'positiveIntegerValue',
        'timePatternValue',
        'timeValue',
    )

    
def priority_value_choice(obj):
    # Find the priority value choice name, and choice datatype
    # for an object.  Enumerations are specific in object (BinaryPV)
    # but must be returned as the generic Enumeration class.
    pv_datatype = obj.get_datatype('presentValue')

    for element in PriorityValue.choiceElements:
        if issubclass(pv_datatype, element.klass):
            return element.name, element.klass
    else:
        raise ExecutionError('device', 'other')


def change_object_name(application, obj, propertyValue):
    value = propertyValue.cast_out(CharacterString)

    if value != obj.objectName:
        if value in application.objectName:
            raise ExecutionError(errorClass='property', errorCode='valueOutOfRange')
        else:
            del application.objectName[obj.objectName]
            application.objectName[value] = obj

    obj.WriteProperty('objectName', value, direct=True)


def command_present_value(obj, propertyValue, priority):
    if not priority:
        priority = 16

    choicekey, datatype = priority_value_choice(obj)

    if propertyValue.is_application_class_null():
        obj.WriteProperty('priorityArray', PriorityValue(null=Null()), arrayIndex=priority, direct=True)

    else:
        value = propertyValue.cast_out(datatype)
        obj.WriteProperty('priorityArray', PriorityValue(**{choicekey: value}), arrayIndex=priority, direct=True)

    # update present value from priority array
    prio_array = obj.priorityArray
    for i in range(1,17):
        prio_value = prio_array[i]
        value = getattr(prio_value, choicekey, None)
        if value is not None:
            break
    else:
        value = obj.relinquishDefault

    obj.WriteProperty('presentValue', value, direct=True)


def write_relinquish_default(obj, propertyValue):
    datatype = obj.get_datatype('relinquishDefault')
    value = propertyValue.cast_out(datatype)
    obj.WriteProperty('relinquishDefault', value, direct=True)

    # update present value from priority array
    prio_array = obj.priorityArray
    for i in range(1,17):
        if prio_array[i].null is None:
            break
    else:
        obj.WriteProperty('presentValue', value, direct=True)


@bacpypes_debugging
def WriteProperty(application, apdu):
    """Override the default write property, to making all properties writable..."""
    if _debug: SimulatorMixin._debug("do_WritePropertyRequest %r", apdu)

    # get the object
    obj = application.get_object_id(apdu.objectIdentifier)
    if _debug: SimulatorMixin._debug("    - object: %r", obj)

    if not obj:
        resp = Error(errorClass='object', errorCode='unknownObject', context=apdu)
    else:
        try:
            # check if the property exists
            if obj.ReadProperty(apdu.propertyIdentifier, apdu.propertyArrayIndex) is None:
                raise PropertyError(apdu.propertyIdentifier)

            # special cases
            if apdu.propertyIdentifier == 'objectName':
                change_object_name(application, obj, apdu.propertyValue)

            elif apdu.propertyIdentifier == 'presentValue' and is_commandable(obj):
                command_present_value(obj, apdu.propertyValue, apdu.priority)

            elif apdu.propertyIdentifier == 'relinquishDefault':
                write_relinquish_default(obj, apdu.propertyValue)

            else:
                # get the datatype
                datatype = obj.get_datatype(apdu.propertyIdentifier)
                if _debug: SimulatorMixin._debug("    - datatype: %r", datatype)

                # special case for array parts, others are managed by cast_out
                if issubclass(datatype, Array) and (apdu.propertyArrayIndex is not None):
                    if apdu.propertyArrayIndex == 0:
                        value = apdu.propertyValue.cast_out(Unsigned)
                    else:
                        value = apdu.propertyValue.cast_out(datatype.subtype)
                else:
                    value = apdu.propertyValue.cast_out(datatype)
                if _debug: SimulatorMixin._debug("    - value: %r", value)

                # change the value -- direct=True makes all properties writable
                obj.WriteProperty(apdu.propertyIdentifier, value, apdu.propertyArrayIndex, apdu.priority, direct=True)

            # success
            resp = SimpleAckPDU(context=apdu)

        except PropertyError:
            resp = Error(errorClass='object', errorCode='unknownProperty', context=apdu)
    if _debug: SimulatorMixin._debug("    - resp: %r", resp)

    # return the result
    return resp
