#Table of objects - formated as a python list
[ 
    (TimerObject, [(1, 'BACnet Timer Object (null)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(null=Null()), 
                    TimerStateChangeValue(null=Null()),
                    TimerStateChangeValue(null=Null()), 
                    TimerStateChangeValue(null=Null()), 
                    TimerStateChangeValue(null=Null()), 
                    TimerStateChangeValue(null=Null()), 
                    TimerStateChangeValue(null=Null())])
        ))]
    ),
    (TimerObject, [(2, 'BACnet Timer Object (boolean)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(boolean=True), 
                    TimerStateChangeValue(boolean=False), 
                    TimerStateChangeValue(boolean=False), 
                    TimerStateChangeValue(boolean=False), 
                    TimerStateChangeValue(boolean=True), 
                    TimerStateChangeValue(boolean=False), 
                    TimerStateChangeValue(boolean=False)])
        ))]
    ), 
    (TimerObject, [(3, 'BACnet Timer Object (unsigned)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(unsigned=0), 
                    TimerStateChangeValue(unsigned=1), 
                    TimerStateChangeValue(unsigned=2), 
                    TimerStateChangeValue(unsigned=3), 
                    TimerStateChangeValue(unsigned=4), 
                    TimerStateChangeValue(unsigned=5), 
                    TimerStateChangeValue(unsigned=6)]),
            alarmValues = [
                'idle',
                'running',
                'expired'
            ]
        ))]
    ), 
    (TimerObject, [(4, 'BACnet Timer Object (integer)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(integer=-3), 
                    TimerStateChangeValue(integer=-2), 
                    TimerStateChangeValue(integer=-1), 
                    TimerStateChangeValue(integer=0), 
                    TimerStateChangeValue(integer=1), 
                    TimerStateChangeValue(integer=2), 
                    TimerStateChangeValue(integer=3)]),
            alarmValues = [
                'idle'
            ]
        ))]
    ), 
    (TimerObject, [(5, 'BACnet Timer Object (real)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(real=1.1), 
                    TimerStateChangeValue(real=2.2), 
                    TimerStateChangeValue(real=3.3), 
                    TimerStateChangeValue(real=4.4), 
                    TimerStateChangeValue(real=5.5), 
                    TimerStateChangeValue(real=6.6), 
                    TimerStateChangeValue(real=7.7)]),
            alarmValues = [
                'idle',
                'running',
                'expired',
                'idle',
                'idle',
                'expired',
                'running',
                'running'
            ]
        ))]
    ),
    (TimerObject, [(6, 'BACnet Timer Object (double)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(double=1.1), 
                    TimerStateChangeValue(double=2.2), 
                    TimerStateChangeValue(double=3.3), 
                    TimerStateChangeValue(double=4.4), 
                    TimerStateChangeValue(double=5.5), 
                    TimerStateChangeValue(double=6.6), 
                    TimerStateChangeValue(double=7.7)])
        ))]
    ),
    (TimerObject, [(7, 'BACnet Timer Object (octetstring)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
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
    (TimerObject, [(8, 'BACnet Timer Object (characterstring)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(characterstring="Test 1"), 
                    TimerStateChangeValue(characterstring="Test 2"), 
                    TimerStateChangeValue(characterstring="Test 3"), 
                    TimerStateChangeValue(characterstring="Test 4"), 
                    TimerStateChangeValue(characterstring="Test 5"), 
                    TimerStateChangeValue(characterstring="Test 6"), 
                    TimerStateChangeValue(characterstring="Test 7")])
        ))]
    ),
    (TimerObject, [(9, 'BACnet Timer Object (bitstring)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(bitstring=BitString([0,0,0,0])), 
                    TimerStateChangeValue(bitstring=BitString([0,0,0,1])), 
                    TimerStateChangeValue(bitstring=BitString([0,0,1,0])), 
                    TimerStateChangeValue(bitstring=BitString([0,1,0,0])), 
                    TimerStateChangeValue(bitstring=BitString([1,0,0,0])), 
                    TimerStateChangeValue(bitstring=BitString([1,1,0,0])), 
                    TimerStateChangeValue(bitstring=BitString([1,1,1,1]))])
        ))]
    ),    
    (TimerObject, [(10, 'BACnet Timer Object (enumerated)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(enumerated=0), 
                    TimerStateChangeValue(enumerated=1), 
                    TimerStateChangeValue(enumerated=2), 
                    TimerStateChangeValue(enumerated=3), 
                    TimerStateChangeValue(enumerated=4), 
                    TimerStateChangeValue(enumerated=5), 
                    TimerStateChangeValue(enumerated=6)])
        ))]
    ),    
    (TimerObject, [(11, 'BACnet Timer Object (date)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(date=Date((0x7C,0x04,0x01,0x01))), 
                    TimerStateChangeValue(date=Date((0x7C,0x04,0x02,0x02))), 
                    TimerStateChangeValue(date=Date((0x7C,0x04,0x03,0x03))), 
                    TimerStateChangeValue(date=Date((0x7C,0x04,0x04,0x04))), 
                    TimerStateChangeValue(date=Date((0x7C,0x04,0x05,0x05))), 
                    TimerStateChangeValue(date=Date((0x7C,0x04,0x06,0x06))), 
                    TimerStateChangeValue(date=Date((0x7C,0x04,0x07,0x07)))])
        ))]
    ),
    (TimerObject, [(12, 'BACnet Timer Object (time)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(time=Time((0x00,0x00,0x00,0x00))), 
                    TimerStateChangeValue(time=Time((0x01,0x01,0x01,0x01))), 
                    TimerStateChangeValue(time=Time((0x02,0x02,0x02,0x02))), 
                    TimerStateChangeValue(time=Time((0x03,0x03,0x03,0x03))), 
                    TimerStateChangeValue(time=Time((0x04,0x04,0x04,0x04))), 
                    TimerStateChangeValue(time=Time((0x05,0x05,0x05,0x05))), 
                    TimerStateChangeValue(time=Time((0x06,0x06,0x06,0x06)))])
        ))]
    ),    
    (TimerObject, [(13, 'BACnet Timer Object (objectidentifier)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(objectidentifier=("analogInput", 1)), 
                    TimerStateChangeValue(objectidentifier=("binaryInput", 1)), 
                    TimerStateChangeValue(objectidentifier=("analogOutput", 1)), 
                    TimerStateChangeValue(objectidentifier=("binaryOutput", 1)), 
                    TimerStateChangeValue(objectidentifier=("analogValue", 1)), 
                    TimerStateChangeValue(objectidentifier=("binaryValue", 1)), 
                    TimerStateChangeValue(objectidentifier=("analogInput", 2))])
        ))]
    ),      
    (TimerObject, [(14, 'BACnet Timer Object (noValue)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(noValue=Null()), 
                    TimerStateChangeValue(noValue=Null()),
                    TimerStateChangeValue(noValue=Null()),
                    TimerStateChangeValue(noValue=Null()),
                    TimerStateChangeValue(noValue=Null()),
                    TimerStateChangeValue(noValue=Null()),
                    TimerStateChangeValue(noValue=Null())])
        ))]
    ),     
    (TimerObject, [(15, 'BACnet Timer Object (constructedValue integer)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(constructedValue=Any(Integer(0))), 
                    TimerStateChangeValue(constructedValue=Any(Integer(1))),
                    TimerStateChangeValue(constructedValue=Any(Integer(2))),
                    TimerStateChangeValue(constructedValue=Any(Integer(3))),
                    TimerStateChangeValue(constructedValue=Any(Integer(4))),
                    TimerStateChangeValue(constructedValue=Any(Integer(5))),
                    TimerStateChangeValue(constructedValue=Any(Integer(6)))])
        ))]
    ),
        (TimerObject, [(16, 'BACnet Timer Object (constructedValue daterange)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(constructedValue=Any(DateRange(startDate=Date((0x7C,0x04,0x01,0x01)), endDate=Date((0x7C,0x04,0x02,0x01))))), 
                    TimerStateChangeValue(constructedValue=Any(DateRange(startDate=Date(), endDate=Date()))),
                    TimerStateChangeValue(constructedValue=Any(DateRange(startDate=Date(), endDate=Date()))),
                    TimerStateChangeValue(constructedValue=Any(DateRange(startDate=Date(), endDate=Date()))),
                    TimerStateChangeValue(constructedValue=Any(DateRange(startDate=Date(), endDate=Date()))),
                    TimerStateChangeValue(constructedValue=Any(DateRange(startDate=Date(), endDate=Date()))),
                    TimerStateChangeValue(constructedValue=Any(DateRange(startDate=Date((0x7C,0x04,0x02,0x01)), endDate=Date((0x7C,0x04,0x03,0x02)))))])
        ))]
    ),  
    (TimerObject, [(17, 'BACnet Timer Object (datetime)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(datetime=DateTime(date=Date((0x7C,0x04,0x01,0x01)), time=Time((0x00,0x00,0x00,0x00)))), 
                    TimerStateChangeValue(datetime=DateTime(date=Date((0x7C,0x04,0x02,0x02)), time=Time((0x01,0x01,0x01,0x01)))), 
                    TimerStateChangeValue(datetime=DateTime(date=Date((0x7C,0x04,0x03,0x03)), time=Time((0x02,0x02,0x02,0x02)))), 
                    TimerStateChangeValue(datetime=DateTime(date=Date((0x7C,0x04,0x04,0x04)), time=Time((0x03,0x03,0x03,0x03)))), 
                    TimerStateChangeValue(datetime=DateTime(date=Date((0x7C,0x04,0x05,0x05)), time=Time((0x04,0x04,0x04,0x04)))), 
                    TimerStateChangeValue(datetime=DateTime(date=Date((0x7C,0x04,0x06,0x06)), time=Time((0x05,0x05,0x05,0x05)))), 
                    TimerStateChangeValue(datetime=DateTime(date=Date((0x7C,0x04,0x07,0x07)), time=Time((0x06,0x06,0x06,0x06))))])
        ))]
    ),    
    (TimerObject, [(18, 'BACnet Timer Object (lightingCommand)',
        dict(
            presentValue = 0,
            statusFlags = [0,0,0,0],
            eventState = 'normal',
            outOfService = False,
            timerState = 'idle',
            timerRunning = False,
            stateChangeValues = ArrayOf(TimerStateChangeValue)([
                    TimerStateChangeValue(lightingCommand=LightingCommand(
                                            operation = 'none',
                                            targetLevel = 50.0,
                                            rampRate = 10.0,
                                            stepIncrement = 10.0,
                                            fadeTime = 5000,
                                            priority = 10
                                          )), 
                    TimerStateChangeValue(lightingCommand=LightingCommand(
                                            operation = 'none',
                                            targetLevel = 51.0,
                                            rampRate = 11.0,
                                            stepIncrement = 11.0,
                                            fadeTime = 5001,
                                            priority = 11
                                          )), 
                    TimerStateChangeValue(lightingCommand=LightingCommand(
                                            operation = 'none',
                                            targetLevel = 52.0,
                                            rampRate = 12.0,
                                            stepIncrement = 12.0,
                                            fadeTime = 5002,
                                            priority = 12
                                          )), 
                    TimerStateChangeValue(lightingCommand=LightingCommand(
                                            operation = 'none',
                                            targetLevel = 53.0,
                                            rampRate = 13.0,
                                            stepIncrement = 13.0,
                                            fadeTime = 5003,
                                            priority = 13
                                          )), 
                    TimerStateChangeValue(lightingCommand=LightingCommand(
                                            operation = 'none',
                                            targetLevel = 54.0,
                                            rampRate = 14.0,
                                            stepIncrement = 14.0,
                                            fadeTime = 5004,
                                            priority = 14
                                          )), 
                    TimerStateChangeValue(lightingCommand=LightingCommand(
                                            operation = 'none',
                                            targetLevel = 55.0,
                                            rampRate = 15.0,
                                            stepIncrement = 15.0,
                                            fadeTime = 5005,
                                            priority = 15
                                          )), 
                    TimerStateChangeValue(lightingCommand=LightingCommand(
                                            operation = 'none'
                                          ))])
        ))]
    ),            
]
