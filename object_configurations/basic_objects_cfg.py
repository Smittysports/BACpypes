#Table of objects - formated as a python list
[
    (AccumulatorObject, [(1, 'BACnet Accumulator (Generic)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            scale = Scale(floatScale = 1.0),
            units = 'noUnits',
            maxPresValue = 100,
        ))]
    ),
    
    (AnalogInputObject,  [(1, 'BACnet Analog Input (Generic)',
        dict(
            presentValue = 0.0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            units = 'noUnits',
            reliabilityEvaluationInhibit = False,
            updateInterval = 1000,
            covIncrement = 1.0,
            resolution = 0.1,
            minPresValue = -100.0,
            maxPresValue = 100.0,
            interfaceValue = OptionalReal(real = 1.0),
            highLimit = 80.0,
            lowLimit = -80.0,
            faultHighLimit = 90.0,
            faultLowLimit = -90.0,
            timeDelay = 1,
            notificationClass = 1,
            deadband = 0.2,
            limitEnable = [1,1],
            eventEnable = [1,1,1],
            ackedTransitions = [1,1,1],
            notifyType = 'alarm',
            eventMessageTexts = ArrayOf(CharacterString)
            (
                [
                    'OffNormal',
                    'Fault',
                    'Normal'
                ]
            ),
            eventMessageTextsConfig = ArrayOf(CharacterString)(['','','']),
            timeDelayNormal = 1,
            eventDetectionEnable = True,
            eventAlgorithmInhibit = False,
            eventAlgorithmInhibitRef = ObjectPropertyReference(
                objectIdentifier = ("binaryOutput", 1),
                propertyIdentifier = PropertyIdentifier('activeText'),
                propertyArrayIndex = 0
            ),
            eventTimeStamps = ArrayOf(TimeStamp)([TimeStamp(dateTime=DateTime(date=Date(), time=Time())) for i in range(3)]),
        ))]
    ),

    (AnalogOutputObject,  [(1, 'BACnet Analog Output (Generic)',
        dict(
            presentValue = 0.0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            units = 'noUnits',
            relinquishDefault = Real(0.0),
        ))]
    ),

    (AnalogValueObject,  [(1, 'BACnet Analog Value (Generic)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            units = 'noUnits',
        ))]
    ),

	(LargeAnalogValueObject,  [(1, 'BACnet Large Analog Value (Generic)',
        dict(
            presentValue = 3.07E306,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            units = 'noUnits',
        ))]
    ),
	
    (IntegerValueObject,  [(1, 'BACnet Integer Value (Generic)',
        dict(
            presentValue = -202,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            units = 'noUnits',
        ))]
    ),
	
    (PositiveIntegerValueObject,  [(1, 'BACnet Positive Integer Value (Generic)',
        dict(
            presentValue = 202,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            units = 'noUnits',
        ))]
    ),

    (BinaryInputObject,  [(1, 'BACnet Digital Input (Generic)',
        dict(
            presentValue = 'inactive',
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            polarity = 'normal',
        ))]
    ),

    (BinaryOutputObject,  [(1, 'BACnet Digital Output (Generic)',
        dict(
            presentValue = 'inactive',
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            polarity = 'normal',
            relinquishDefault = 'inactive',
        ))]
    ),

    (BinaryValueObject,  [(1, 'BACnet Digital Value (Generic)',
        dict(
            presentValue = 'inactive',
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
        ))]
    ),

    (MultiStateInputObject,  [(1, 'BACnet Multistate Input (Generic)',
        dict(
            presentValue = 1,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            numberOfStates = 3,
            stateText = ['State 1','State 2','State 3'],
        ))]
    ),

    (MultiStateOutputObject,  [(1, 'BACnet Multistate Output (Generic)',
        dict(
            presentValue = 1,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            relinquishDefault = 1,
            numberOfStates = 3,
            stateText = ['State 1','State 2','State 3'],
        ))]
    ),

    (MultiStateValueObject,  [(1, 'BACnet Multistate Value (Generic)',
        dict(
            presentValue = 1,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            numberOfStates = 3,
            stateText = ['State 1','State 2','State 3'],
        ))]
    ),

    (AveragingObject,  [(1, 'BACnet Averaging (Generic)',
        dict(
            minimumValue = float('inf'),
            averageValue = -float('nan'),
            maximumValue = float('-inf'),
            attemptedSamples = 0,
            validSamples = 0,
            objectPropertyReference = REF('analogInput', 1, 'presentValue',4194302),
            windowInterval = 60,
            windowSamples = 15,
        ))]
    ),
    
    (CalendarObject,  [(1, 'BACnet Calendar (Generic)',
        dict(
            presentValue = False,     
            dateList = [CE('3/21/2014'), CE('1/23/2014 - 3/19/2014'), CE('14.1.255')],
        ))]
    ),

    (CommandObject,  [(1, 'BACnet Command (Generic)',
        dict(
            presentValue = 0,
            inProcess = False,
            allWritesSuccessful = True,
            action = [],
        ))]
    ),

    (EventEnrollmentObject,  [(1, 'BACnet Alarm (Generic)',
        dict(
            eventType = 'outOfRange',
            eventParameters = EventParameter(
                outOfRange=EventParameterOutOfRange(timeDelay=3, lowLimit=-2.0, highLimit=40.0, deadband=2.0)),
            objectPropertyReference = REF('analogValue', 1, 'presentValue'),
            notificationClass = 1,
        ))]
    ),


    (FileObject,  [(1, 'BACnet File (Generic)',
        dict(
            description = "Sample file",
            fileType = "Empty File",
            fileSize = 0,
            modificationDate = DATETIME('3/20/2014', '17:00'),
            archive = False,
            readOnly = True,
            fileAccessMethod = 'streamAccess',
        ))]
    ),

    (LoadControlObject,  [(1, 'BACnet Load Control (Generic)',
        dict(
            presentValue = 'shedCompliant',
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            requestedShedLevel = ShedLevel(percent = 80),
            startTime = DATETIME('3/20/2014', '17:00'),
            shedDuration = 120,
            dutyWindow = 30,
            enable = True,
            expectedShedLevel = ShedLevel(percent = 80),
            actualShedLevel = ShedLevel(percent = 80),
            shedLevels = [1,3,6,9],
            shedLevelDescriptions = [
                "switch to alternate energy",
                "setback 2 degrees",
                "dim lights 20%",
                "setback 4 degrees"
            ],
        ))]
    ),

    (LoopObject,  [(1, 'BACnet Loop Control (Generic)',
        dict(
            presentValue = 0.0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            updateInterval = 100,
            outputUnits = 'noUnits',
            manipulatedVariableReference = LREF('analogOutput', 1, 'presentValue'),
            controlledVariableReference = LREF('analogInput', 1, 'presentValue'),
            controlledVariableValue = 0.0,
            controlledVariableUnits = 'noUnits',
            setpointReference = SetpointReference(),
            setpoint = 0.0,
            action = 'direct',
            priorityForWriting = 12,
        ))]
    ),
    (NotificationClassObject,  [(1, 'BACnet Notification (Generic)',
        dict(
            notificationClass = 1,
            priority = [255,255,255],
            ackRequired = [1,1,1],
            recipientList = [],
        ))]
    ),

    (ProgramObject,  [(1, 'BACnet Program (Generic)',
        dict(
            programState = 'running',
            programChange = 'ready',
            statusFlags = [0,0,0,0],
            outOfService = False,
        ))]
    ),

    (PulseConverterObject,  [(1, 'BACnet Pulse Converter (Generic)',
        dict(
            presentValue = 0.0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            units = 'noUnits',
            scaleFactor = 2.0,
            adjustValue = 1.0,
            count = 0,
            updateTime = DATETIME(),
            countChangeTime = DATETIME(),
            countBeforeChange = 0,
        ))]
    ),

    (ScheduleObject,  [(1, 'BACnet Schedule (Generic)',
        dict(
            presentValue = Real(72.0),
            weeklySchedule = [
                DS( TVP('8:00', Real(72.0)), TVP('17:00', Null()) ),
                DS( TVP('8:00', Real(72.0)), TVP('17:00', Null()) ),
                DS( TVP('8:00', Real(72.0)), TVP('17:00', Null()) ),
                DS( TVP('8:00', Real(72.0)), TVP('17:00', Null()) ),
                DS( TVP('8:00', Real(72.0)), TVP('17:00', Null()) ),
                DS( ),
                DS( ),
            ],
            exceptionSchedule = [
                SE( CE('4/1/2014'), 10, TVP('8:00', Real(84.0)), TVP('17:30:15', Null()) ),
                SE( CE('4/2/2014 - 7/19/2014'), 11, TVP('1:00', Real(54.0)), TVP('3:00', Null()) ),
                SE( CE('255.2.3'), 12, TVP('19:00', Real(72.0)), TVP('21:00', Null()) ),
                SE( ('calendar', 1), 16, TVP('8:00', Real(64.0)), TVP('17:00', Null()) ),
            ],
            listOfObjectPropertyReferences = [
                REF('analogOutput', 1, 'presentValue'),
                REF('analogOutput', 123, 'presentValue', 123),
            ],
            scheduleDefault = Real(64.0),
            priorityForWriting = 12,
        ))]
    ),

    (TrendLogObject,  [(1, 'BACnet Trend Log (Generic)',
        dict(
            logDeviceObjectProperty = REF('analogInput', 1, 'presentValue', 4194302)
        ))]
    ),

    (CharacterStringValueObject,  [(1, 'BACnet String Value (Generic)',
        dict(
            presentValue = "Simulation value",
            statusFlags = [0,0,0,0],
        ))]
    ),
	
	(DateTimeValueObject, [(1, 'BACnet DateTime (Generic)',
        dict(
			presentValue = DATETIME('3/20/2014', '17:00'),
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
			isUTC = False,
            relinquishDefault = DATETIME('3/20/2014', '13:00'),
        ))]
    ),

    (TimerObject, [(1, 'BACnet Timer Object (octetstring)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            updateTime = DateTime(date=Date(), time=Time()),
            lastStateChange = 'none',
            expirationTime = DateTime(date=Date(), time=Time()),
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(octetstring=b'0'), 
                    TimerStateChangeValue(octetstring=b'1'), 
                    TimerStateChangeValue(octetstring=b'2'), 
                    TimerStateChangeValue(octetstring=b'3'), 
                    TimerStateChangeValue(octetstring=b'4'), 
                    TimerStateChangeValue(octetstring=b'5'), 
                    TimerStateChangeValue(octetstring=b'6')])
        ))]
    ), 
   
    (LightingOutputObject,  [(1, 'BACnet Lighting Output (Generic)',
        dict(
            presentValue = 1.0,
            trackingValue = 1.0,
            covIncrement = 1.0,
            statusFlags = [0,0,0,0],
            outOfService = False,
            lightingCommand = LightingCommand(
                operation = 'none',
                targetLevel = 50.0,
                rampRate = 10.0,
                stepIncrement = 10.0,
                fadeTime = 5000,
                priority = 16
            ),
            power = 1.0,
            instantaneousPower = 1.0,
            feedbackValue = 1.0,
            minActualValue = 1.0,
            maxActualValue = 100.0,
            inProgress = 'idle',
            blinkWarnEnable = False,
            egressTime = 1,
            egressActive = False,
            defaultFadeTime = 5000,
            defaultRampRate = 10.0,
            defaultStepIncrement = 1.0,
            currentCommandPriority = 15,
            relinquishDefault = Real(5.0),
            lightingCommandDefaultPriority = 15,
        ))]
    ),
    (BinaryLightingOutputObject,  [(1, 'BACnet Binary Lighting Output (Generic)',
        dict(
            presentValue = 'off',
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            blinkWarnEnable = False,
            egressTime = 1,
            egressActive = False,
            feedbackValue = 'off',
            power = 1,
            polarity = 'normal',
            currentCommandPriority = 15,
            relinquishDefault = 'off',
            ackedTransitions = [1,1,1],
            eventEnable = [0,0,0],
            eventMessageTexts = ArrayOf(CharacterString)(['','','']),
            eventTimeStamps = ArrayOf(TimeStamp)([
                    TimeStamp(dateTime=DateTime(date=(95, 1, 25, 3), time=(7, 0, 0, 0))), 
                    TimeStamp(dateTime=DateTime(date=(95, 1, 25, 3), time=(8, 0, 0, 0))), 
                    TimeStamp(dateTime=DateTime(date=(95, 1, 25, 3), time=(9, 0, 0, 0)))]),      
            notificationClass = 1,
            notifyType = 'alarm',
        ))]
    ),
   
    (EventLogObject, [(1, 'BACnet Event Log Object (Generic)',
        dict(
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            recordCount = 17,
            totalRecordCount = 100,
            enable = False,
            stopWhenFull = False,
            bufferSize = 1000,
            logBuffer = event_log_records
        ))]
    ),
    (ChannelObject, [(1, 'BACnet Channel Object (Generic)',
        dict(
            presentValue = Real(5.0),
            lastPriority = 1,
            writeStatus = 'idle',
            statusFlags = [0,0,0,0],
            reliability = 'noFaultDetected',
            outOfService = False,
            listOfObjectPropertyReferences = [],
            executionDelay = [],
            allowGroupDelayInhibit = False,
            channelNumber = 1,
            controlGroups = [],
            eventDetectionEnable = True,
            notificationClass = 1,
            eventEnable = [1,1,1],
            ackedTransitions = [1,1,1],
            eventState = 'normal',
            notifyType = 'alarm',
            eventTimeStamps = ArrayOf(TimeStamp)([TimeStamp(dateTime=DateTime(date=Date(), time=Time())) for i in range(3)]),
            eventMessageTexts = ArrayOf(CharacterString)
            (
                [
                    'OffNormal',
                    'Fault',
                    'Normal'
                ]
            ),
            eventMessageTextsConfig = ArrayOf(CharacterString)(['','','']),
            reliabilityEvaluationInhibit = False,
            valueSource = Null(),
        ))]
    ),
  
    (DateTimePatternValueObject, [(1, 'BACnet DateTimePattern Value Object (Generic)',
        dict(
            presentValue = DateTime(date=Date(), time=Time()),
            statusFlags = [0,0,0,0],
            reliability = 'noFaultDetected',
            outOfService = False,
            eventState = 'normal',
            notificationClass = 1,
            notifyType = 'alarm',
            eventEnable = [1,1,1],
            ackedTransitions = [1,1,1],
            eventTimeStamps = ArrayOf(TimeStamp)([TimeStamp(dateTime=DateTime(date=Date(), time=Time())) for i in range(3)]),
            eventMessageTexts = ArrayOf(CharacterString)
            (
                [
                    'OffNormal',
                    'Fault',
                    'Normal'
                ]
            ),
            eventMessageTextsConfig = ArrayOf(CharacterString)(['','','']),
            currentCommandPriority = 1,
            valueSource = Null(),
        ))]
    ),
    
    (CharacterStringValueObject,  [(2, 'Long String Value',
        dict(
            presentValue = "A" * 1000,
            statusFlags = [0,0,0,0],
        ))]
    ),
    
    (OctetStringValueObject,  [(1, 'BACnet Octet String Value Object (Generic)',
        dict(
            presentValue = b'0',
            statusFlags = [0,0,0,0],
        ))]
    ),
   
]