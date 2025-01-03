#Table of objects - formated as a python list

[
    (NotificationClassObject,  [(1, 'All Alarms',
        dict(
            notificationClass = 1,
            priority = [255,255,255],
            ackRequired = [1,1,1],
            recipientList = [],
        ))]
    ),
    
    (AnalogValueObject,  [(i, 'AV_%d' % i) for i in range(1,101)]),
    
    (EventEnrollmentObject,  [(i, 'Alarm_%d' %i,
        dict(
            eventType = 'outOfRange',
            eventParameters = EventParameter(
                outOfRange=EventParameterOutOfRange(timeDelay=0, lowLimit=0.0, highLimit=10.0, deadband=0.0)
            ),
            objectPropertyReference = DeviceObjectPropertyReference(
                objectIdentifier=('analogValue', i), propertyIdentifier='presentValue'
            ),
            notificationClass = 1,
        ))
        for i in range(1,101)]
    ),

    
]
