#!/usr/bin/python
'''
Utilties for creating simulator objects
'''
import re
import time

from bacpypes.object import *
from AWS_EventLogVariables import *
from bacpypes.primitivedata import Null
from bacpypes.basetypes import *
from bacpypes.debugging import xtob

# macros to simplify the config files

def TIME(theTime):
    m = re.match(r'^(\d{1,2}):(\d{2})(?::(\d{2})(?:\.(\d{2}))?)?$', theTime)
    if not m:
        raise ValueError(theTime)

    tup = tuple(int(g) for g in m.groups(0))
    return Time(tup)


def DATE(theDate):
    tup = time.strptime(theDate, "%m/%d/%Y")
    return Date((tup.tm_year - 1900, tup.tm_mon, tup.tm_mday, tup.tm_wday + 1))


def DATETIME(theDate=None, theTime=None):
    d = DATE(theDate) if theDate else Date()
    t = TIME(theTime) if theTime else Time()

    return DateTime(date=d, time=t)


def CE(calendarEntry):
    """
    re stands for Python's regular expression module.

    re.group(0) will return the entire string matched by the regular expression
    re.group(1) will return the first parenthesized subgroup
    re.group(2) will return the second parenthesized subgroup
    re.group(3) will return the third parenthesized subgroup
    """
    m = re.match(r'(?:^(\d{1,2}/\d{1,2}/\d{4})(?:\s*-\s*(\d{1,2}/\d{1,2}/\d{4}))?$)|(?:^(\d{1,3}\.\d{1,3}\.\d{1,3})$)', calendarEntry)
    if not m:
        raise ValueError(calendarEntry)

    if m.group(1) and m.group(2):
        return CalendarEntry(dateRange=DateRange(startDate=DATE(m.group(1)), endDate=DATE(m.group(2))))

    elif m.group(1):
        return CalendarEntry(date=DATE(m.group(1)))

    elif m.group(3):
        parts = m.group(3).split('.')

        octetByteArray = bytearray()
        for p in parts:
            intConv = int(p)
            # chr will get the character that represent the unicode of the integer passed in
            octetByteArray += intConv.to_bytes(1, 'little')
          
        return CalendarEntry(weekNDay=WeekNDay(octetByteArray))

    else:
        raise ValueError(calendarEntry)


def TVP(theTime, theValue):
    return TimeValue(time=TIME(theTime), value=theValue)


def DS(*time_value_pairs):
    return DailySchedule(daySchedule=list(time_value_pairs))


def SE(period, priority, *time_value_pairs):
    if isinstance(period, CalendarEntry):
        return SpecialEvent(
            period=SpecialEventPeriod(calendarEntry=period),
            listOfTimeValues=list(time_value_pairs),
            eventPriority=priority)

    elif isinstance(period, tuple):
        return SpecialEvent(
            period=SpecialEventPeriod(calendarReference=period),
            listOfTimeValues=list(time_value_pairs),
            eventPriority=priority)

    else:
        raise ValueError(period)


def REF(type, instance, property, device=None):
    if device is not None:
        return DeviceObjectPropertyReference(objectIdentifier=(type, instance), propertyIdentifier=property, deviceIdentifier=('device', device))
    else:
        return DeviceObjectPropertyReference(objectIdentifier=(type, instance), propertyIdentifier=property)


def LREF(type, instance, property):
    return ObjectPropertyReference(objectIdentifier=(type, instance), propertyIdentifier=property)


# functions for application to read and process the config files
def load_file(theFile):
    """ The eval() function evaluates the specified expression, if the expression is a legal Python
        statement, it will be executed.
    """
    return eval(theFile.read())
