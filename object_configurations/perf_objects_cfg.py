#Table of objects - formated as a python list

[
    (AnalogInputObject,  [(i, 'AI_%d' % i) for i in range(1,21)]),
    (AnalogOutputObject, [(i, 'AO_%d' % i) for i in range(1,21)]),
    (AnalogValueObject,  [(i, 'AV_%d' % i) for i in range(1,21)]),
    
    (BinaryInputObject,  [(i, 'BI_%d' % i) for i in range(1,21)]),
    (BinaryOutputObject, [(i, 'BO_%d' % i) for i in range(1,21)]),
    (BinaryValueObject,  [(i, 'BV_%d' % i) for i in range(1,21)]),
    
    (MultiStateInputObject,  [(i, 'MSI_%d' % i) for i in range(1,21)]),
    (MultiStateOutputObject, [(i, 'MSO_%d' % i) for i in range(1,21)]),
    (MultiStateValueObject,  [(i, 'MSV_%d' % i) for i in range(1,21)]),
]