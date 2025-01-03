#!/usr/bin/env python

"""
AWS_EventLogVariables.py
Re-usable variables that are useful for Event Log Object Properties
"""

from bacpypes.basetypes import DateTime, LogRecordLogDatum, StatusFlags, LogRecord, \
    TimeStamp, Date, Time, CharacterString, PriorityValue, PriorityArray, DeviceObjectPropertyReference, \
    NotificationParametersChangeOfBitstring, NotificationParametersChangeOfState, NotificationParameters, \
    PropertyStates, NotificationParametersChangeOfValue, NotificationParametersChangeOfValueNewValue, \
    EventType, NotificationParametersCommandFailure, NotificationParametersFloatingLimit, NotificationParametersOutOfRange, \
    NotificationParametersComplexEventType, PropertyValue, PropertyIdentifier, NotificationParametersChangeOfLifeSafety, \
    LifeSafetyState, LifeSafetyMode, LifeSafetyOperation, NotificationParametersExtended, NotificationParametersBufferReady, \
    NotificationParametersUnsignedRange, NotificationParametersAccessEventType, NotificationParametersDoubleOutOfRangeType, \
    NotificationParametersSignedOutOfRangeType, NotificationParametersUnsignedOutOfRangeType, NotificationParametersChangeOfCharacterStringType, \
    NotificationParameterschangeOfStatusflagsType, NotificationParametersChangeOfReliabilityType, NotificationParametersExtendedParametersType, \
    EventParameterUnsignedRange, EventParameterAccessEvent, EventParameterAccessEventAccessEvent, EventParameterAccessEventAccessEvent, \
    AccessEvent, DeviceObjectReference, AuthenticationFactorType, Reliability, NotificationParametersChangeOfDiscreteValue, \
    NotificationParametersChangeOfTimer, NotificationParametersChangeOfDiscreteValueNewValue, TimerTransition, TimerState
from bacpypes.object import EventLogRecord, EventLogRecordLogDatum
from bacpypes.constructeddata import ArrayOf, ListOf, Any
from bacpypes.primitivedata import Null, Integer, BitString, ObjectIdentifier, Enumerated, Real
from bacpypes.apdu import EventNotificationParameters

time_stamp1 = TimeStamp(dateTime=DateTime(date=(95, 1, 25, 3), time=(7, 0, 0, 0)))
current_date_time = DateTime(date=Date().now().value, time=Time().now().value)

"""
    EventLogRecordLogDatum
    choiceElements =
        Element('logStatus', LogStatus, 0)
        Element('notification', EventNotificationParameters, 1)
        Element('timeChange', Real, 2)
"""
log_status_datum = EventLogRecordLogDatum(logStatus=BitString([1,1,1]))
time_change_datum = EventLogRecordLogDatum(timeChange=0)

"""
    - notification is an EventNotificationParameters type in BACpypes
    - EventNotificationParameters represents the BACnet ConfirmedEventNotification-Request
        ConfirmedEventNotification-Request ::= SEQUENCE 
        {
            process-identifier 		        [0] Unsigned32,
            initiating-device-identifier 	[1] BACnetObjectIdentifier,
            event-object-identifier 		[2] BACnetObjectIdentifier,
            timestamp 			            [3] BACnetTimeStamp,
            notification-class 		        [4] Unsigned,
            priority 			            [5] Unsigned8,
            event-type			            [6] BACnetEventType,
            message-text 			        [7] CharacterString OPTIONAL,
            notify-type 			        [8] BACnetNotifyType,
            ack-required 			        [9] BOOLEAN OPTIONAL,
            from-state 			            [10] BACnetEventState OPTIONAL,
            to-state 			            [11] BACnetEventState,
            event-values 			        [12] BACnetNotificationParameters OPTIONAL
        }
    - The EventNotificationParameters BACpypes type can contain a NotificationParameters type, BACnetNotificationParameters in the BACnet standard
"""

device_object_id = 4194302

######### timeChange
event_log_record = EventLogRecord(
    timestamp=current_date_time, 
    logDatum=time_change_datum
)

######### notification: Change of bitstring
notification_params_change_of_bitstring = NotificationParametersChangeOfBitstring(
    referencedBitstring = BitString([1,1,1]),
    statusFlags = StatusFlags([1,1,1,1])
)
notification_parameters_1 = NotificationParameters(changeOfBitstring = notification_params_change_of_bitstring)

notification_change_datum_1 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 1,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('changeOfBitstring'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_1
        )
    )

######### notification: Change of state
notification_params_change_of_state = NotificationParametersChangeOfState(
    newState = PropertyStates(booleanValue=False),
    statusFlags = StatusFlags([1,1,1,1])
)
notification_parameters_2 = NotificationParameters(changeOfState = notification_params_change_of_state)

notification_change_datum_2 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 2,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('binaryInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('changeOfState'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_2
        )
    )

######### notification: Change of value
notification_params_change_of_value = NotificationParametersChangeOfValue(
    newValue = NotificationParametersChangeOfValueNewValue(changedValue = 1.5),
    statusFlags = StatusFlags([1,1,1,1])
)
notification_parameters_3 = NotificationParameters(changeOfValue = notification_params_change_of_value)

notification_change_datum_3 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 3,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('multiStateInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('changeOfValue'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_3
        )
    )

######### notification: Command failure
notification_params_command_failure = NotificationParametersCommandFailure(
    commandValue = Any(Real(0)),
    statusFlags = StatusFlags([1,1,1,1]),
    feedbackValue = Any(Real(0))
)
notification_parameters_4 = NotificationParameters(commandFailure = notification_params_command_failure)

notification_change_datum_4 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 4,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogOutput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('commandFailure'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_4
        )
    )

######### notification: Floating limit
notification_params_floating_limit = NotificationParametersFloatingLimit(
    referenceValue = Real(0),
    statusFlags = StatusFlags([1,1,1,1]),
    setpointValue = Real(0),
    errorLimit = Real(0)
)
notification_parameters_5 = NotificationParameters(floatingLimit = notification_params_floating_limit)

notification_change_datum_5 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 5,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('binaryOutput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('floatingLimit'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_5
        )
    )

######### notification: Out of range
notification_params_out_of_range = NotificationParametersOutOfRange(
    exceedingValue = Real(0),
    statusFlags = StatusFlags([1,1,1,1]),
    deadband = Real(0),
    exceededLimit = Real(0)
)
notification_parameters_6 = NotificationParameters(outOfRange = notification_params_out_of_range)

notification_change_datum_6 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 6,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('multiStateOutput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('outOfRange'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_6
        )
    )

"""
######### notification: Complex event type
notification_params_complex_event_type = NotificationParametersComplexEventType(
    complexEventType = PropertyValue(
        propertyIdentifier = PropertyIdentifier('action'),
        propertyArrayIndex = 0,
        value = Any(Real(0)),
        priority = 0
        )
)
notification_parameters_7 = NotificationParameters(complexEventType = notification_params_complex_event_type)

notification_change_datum_7 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 7,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogValue', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('None'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_7
        )
    )
"""

######### notification: Change of life safety
notification_params_change_of_life_safety = NotificationParametersChangeOfLifeSafety(
    newState = LifeSafetyState('quiet'),
    newMode = LifeSafetyMode('off'),
    statusFlags = StatusFlags([1,1,1,1]),
    operationExpected = LifeSafetyOperation('silence')
)
notification_parameters_8 = NotificationParameters(changeOfLifeSafety = notification_params_change_of_life_safety)

notification_change_datum_8 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 8,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogValue', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('changeOfLifeSafety'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_8
        )
    )

######### notification: Extended
notification_params_extended = NotificationParametersExtended(
    vendorId = 10,
    extendedEventType = 0,
    parameters = NotificationParametersExtendedParametersType(real = 2.2)
)
notification_parameters_9 = NotificationParameters(extended = notification_params_extended)

notification_change_datum_9 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 9,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('binaryValue', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('extended'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_9
        )
    )

######### notification: Buffer ready
notification_params_buffer_ready = NotificationParametersBufferReady(
    bufferProperty = DeviceObjectPropertyReference(
        objectIdentifier = ("multiStateValue", 1),
        propertyIdentifier = PropertyIdentifier('activeText'),
        propertyArrayIndex = 0,
        deviceIdentifier = ("device", 1)
    ),
    previousNotification = 1,
    currentNotification = 2
)
notification_parameters_10 = NotificationParameters(bufferReady = notification_params_buffer_ready)

notification_change_datum_10 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 10,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('multiStateValue', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('bufferReady'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_10
        )
    )

######### notification: Unsigned range

notification_params_unsigned_range = NotificationParametersUnsignedRange(
    exceedingValue = 0,
    statusFlags = StatusFlags([1,1,1,1]),
    exceedingLimit = 10
)

notification_parameters_11 = NotificationParameters(unsignedRange = notification_params_unsigned_range)

notification_change_datum_11 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 11,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('unsignedRange'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_11
        )
    )

######### notification: Access event
# TODO: This is malformed when sent over the wire
notification_params_access_event = NotificationParametersAccessEventType(
    accessEvent = AccessEvent('granted'),
    statusFlags = StatusFlags([1,1,1,1]),
    accessEventTag = 0,
    accessEventTime = time_stamp1,
    accessCredential = DeviceObjectReference(
        deviceIdentifier = ("multiStateValue", 1),
        objectIdentifier = ("analogValue", 1)
    ),
    authenicationFactor = AuthenticationFactorType('simpleNumber16')
)
notification_parameters_13 = NotificationParameters(accessEvent = notification_params_access_event)

notification_change_datum_13 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 11,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('binaryInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('accessEvent'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_13
        )
    )

######### notification: Double out of range

notification_params_double_out_of_range = NotificationParametersDoubleOutOfRangeType(
    exceedingValue = 5,
    statusFlags = StatusFlags([1,1,1,1]),
    deadband = 1,
    exceededLimit = 2
)

notification_parameters_14 = NotificationParameters(doubleOutOfRange = notification_params_double_out_of_range)

notification_change_datum_14 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 14,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('doubleOutOfRange'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_14
        )
    )

######### notification: Signed out of range

notification_params_signed_out_of_range = NotificationParametersSignedOutOfRangeType(
    exceedingValue = 6,
    statusFlags = StatusFlags([1,1,1,1]),
    deadband = 0,
    exceededLimit = 1
)

notification_parameters_15 = NotificationParameters(signedOutOfRange = notification_params_signed_out_of_range)

notification_change_datum_15 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 15,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('signedOutOfRange'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_15
        )
    )

######### notification: Unsigned out of range

notification_params_unsigned_out_of_range = NotificationParametersUnsignedOutOfRangeType(
    exceedingValue = 7,
    statusFlags = StatusFlags([1,1,1,1]),
    deadband = 3,
    exceededLimit = 10
)

notification_parameters_16 = NotificationParameters(unsignedOutOfRange = notification_params_unsigned_out_of_range)

notification_change_datum_16 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 16,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('unsignedOutOfRange'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_16
        )
    )

######### notification: Change of character string

notification_params_change_of_character_string = NotificationParametersChangeOfCharacterStringType(
    changedValue = "The changed value",
    statusFlags = StatusFlags([1,1,1,1]),
    alarmValue = "The alarm value",
)

notification_parameters_17 = NotificationParameters(changeOfCharacterString = notification_params_change_of_character_string)

notification_change_datum_17 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 17,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('changeOfCharacterstring'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_17
        )
    )

######### notification: Change of status flags
# TODO: The wire is sending a malformed packet

notification_params_change_of_status_flags = NotificationParameterschangeOfStatusflagsType(
    presentValue = "The present value",
    referencedFlags = StatusFlags([1,1,1,1])
)

notification_parameters_18 = NotificationParameters(changeOfStatusflags = notification_params_change_of_status_flags)

notification_change_datum_18 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 18,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('changeOfStatusflags'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_18
        )
    )

######### notification: Change of reliability

notification_params_change_of_reliability = NotificationParametersChangeOfReliabilityType(
    reliability = Reliability('openLoop'),
    statusFlags = StatusFlags([1,1,1,1]),
    propertyValues = [
            PropertyValue(
                propertyIdentifier="presentValue",
                propertyArrayIndex = 0,
                value = Any(Real(1.0)),
                priority = 1
            ),
            PropertyValue(
                propertyIdentifier="presentValue",
                propertyArrayIndex = 0,
                value = Any(Real(2.0)),
                priority = 2
            )]
)

notification_parameters_19 = NotificationParameters(changeOfReliability = notification_params_change_of_reliability)

notification_change_datum_19 = EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 19,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('changeOfReliability'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_19
        )
    )

######### notification: Change of discrete value
# TODO: This works over the wire, but is not decoded in the EBO BACnet library
notification_params_change_of_discrete_value = NotificationParametersChangeOfDiscreteValue(
    newValue = NotificationParametersChangeOfDiscreteValueNewValue(unsigned = 5),
    statusFlags = StatusFlags([1,1,1,1])
)

notification_parameters_21 = NotificationParameters(changeOfDiscreteValue = notification_params_change_of_discrete_value)

notification_change_datum_21= EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 21,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('changeOfDiscreteValue'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_21
        )
    )

######### notification: Change of timer
# TODO: This works over the wire, but is not decoded in the EBO BACnet library
notification_params_change_of_timer = NotificationParametersChangeOfTimer(
    newState = TimerState('running'),
    statusFlags = StatusFlags([1,1,1,1]),
    updateTime = current_date_time,
    lastStateChange = TimerTransition('runningToIdle'),
    initialTimeout = 0,
    expirationTime = current_date_time
)

notification_parameters_22 = NotificationParameters(changeOfTimer = notification_params_change_of_timer)

notification_change_datum_22= EventLogRecordLogDatum(
        notification = EventNotificationParameters(
            processIdentifier = 22,
            initiatingDeviceIdentifier = ObjectIdentifier(('device', device_object_id)),
            eventObjectIdentifier = ObjectIdentifier(('analogInput', 1)),
            timeStamp = time_stamp1,
            notificationClass = 0,
            priority = 0,
            eventType = EventType('changeOfTimer'),
            messageText = "",
            notifyType = Enumerated(0),
            ackRequired = False,
            fromState = Enumerated(0),
            toState = Enumerated(0),
            eventValues = notification_parameters_22
        )
    )

######### All of the Event Log records, to be sent in a single response (it can be segmented)
event_log_records = ListOf(EventLogRecord)([
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=log_status_datum,
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=time_change_datum,
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_1,
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_2,
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_3,
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_4,
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_5,
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_6,
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_8
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_9
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_10
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_11
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_14
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_15
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_16
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_17
    ),
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=notification_change_datum_19
    )
]
)

event_log_records_small = [
    EventLogRecord(
        timestamp=current_date_time, 
        logDatum=log_status_datum,
    )
]

trend_log_records = [
    LogRecord(
        timestamp=current_date_time, 
        logDatum=log_status_datum,
        statusFlags = [0,0,0,0],
    ),
]
