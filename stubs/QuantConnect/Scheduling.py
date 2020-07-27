# encoding: utf-8
# module QuantConnect.Scheduling calls itself Scheduling
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CompositeTimeRule(object, ITimeRule):
    """
    Combines multiple time rules into a single rule that emits for each rule
    
    CompositeTimeRule(*timeRules: Array[ITimeRule])
    CompositeTimeRule(timeRules: IEnumerable[ITimeRule])
    """
    def CreateUtcEventTimes(self, dates):
        """ CreateUtcEventTimes(self: CompositeTimeRule, dates: IEnumerable[DateTime]) -> IEnumerable[DateTime] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, timeRules):
        """
        __new__(cls: type, *timeRules: Array[ITimeRule])
        __new__(cls: type, timeRules: IEnumerable[ITimeRule])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a name for this rule

Get: Name(self: CompositeTimeRule) -> str

"""


    Rules = None


class DateRules(object):
    """
    Helper class used to provide better syntax when defining date rules
    
    DateRules(securities: SecurityManager, timeZone: DateTimeZone)
    """
    def Every(self, *__args):
        """
        Every(self: DateRules, day: DayOfWeek) -> IDateRule
        
            Specifies an event should fire on each of the 
             specified days of week
        
        
            day: The day the event shouls fire
            Returns: A date rule that fires on every specified day of 
             week
        
        Every(self: DateRules, *days: Array[DayOfWeek]) -> IDateRule
        
            Specifies an event should fire on each of the 
             specified days of week
        
        
            days: The days the event shouls fire
            Returns: A date rule that fires on every specified day of 
             week
        """
        pass

    def EveryDay(self, symbol=None):
        """
        EveryDay(self: DateRules) -> IDateRule
        
            Specifies an event should fire every day
            Returns: A date rule that fires every day
        EveryDay(self: DateRules, symbol: Symbol) -> IDateRule
        
            Specifies an event should fire every day the 
             symbol is trading
        
        
            symbol: The symbol whose exchange is used to determine 
             tradeable dates
        
            Returns: A date rule that fires every day the specified 
             symbol trades
        """
        pass

    def MonthEnd(self, symbol=None):
        """
        MonthEnd(self: DateRules) -> IDateRule
        
            Specifies an event should fire on the last of 
             each month
        
            Returns: A date rule that fires on the last of each month
        MonthEnd(self: DateRules, symbol: Symbol) -> IDateRule
        
            Specifies an event should fire on the last 
             tradeable date for the specified
                    
             symbol of each month
        
        
            symbol: The symbol whose exchange is used to determine 
             the last
                    tradeable date of the month
        
            Returns: A date rule that fires on the last tradeable date 
             for the specified security each month
        """
        pass

    def MonthStart(self, symbol=None):
        """
        MonthStart(self: DateRules) -> IDateRule
        
            Specifies an event should fire on the first of 
             each month
        
            Returns: A date rule that fires on the first of each month
        MonthStart(self: DateRules, symbol: Symbol) -> IDateRule
        
            Specifies an event should fire on the first 
             tradeable date for the specified
                    
             symbol of each month
        
        
            symbol: The symbol whose exchange is used to determine 
             the first
                    tradeable date of the 
             month
        
            Returns: A date rule that fires on the first tradeable 
             date for the specified security each month
        """
        pass

    def On(self, *__args):
        """
        On(self: DateRules, year: int, month: int, day: int) -> IDateRule
        
            Specifies an event should fire only on the 
             specified day
        
        
            year: The year
            month: The month
            day: The day
        On(self: DateRules, *dates: Array[DateTime]) -> IDateRule
        
            Specifies an event should fire only on the 
             specified days
        
        
            dates: The dates the event should fire
        """
        pass

    def WeekEnd(self, symbol=None):
        """
        WeekEnd(self: DateRules) -> IDateRule
        
            Specifies an event should fire on Friday each week
            Returns: A date rule that fires on Friday each week
        WeekEnd(self: DateRules, symbol: Symbol) -> IDateRule
        
            Specifies an event should fire on the last 
             tradeable date for the specified
                    
             symbol of each week
        
        
            symbol: The symbol whose exchange is used to determine 
             the last
                    tradeable date of the week
        
            Returns: A date rule that fires on the last tradeable date 
             for the specified security each week
        """
        pass

    def WeekStart(self, symbol=None):
        """
        WeekStart(self: DateRules) -> IDateRule
        
            Specifies an event should fire on Monday each week
            Returns: A date rule that fires on Monday each week
        WeekStart(self: DateRules, symbol: Symbol) -> IDateRule
        
            Specifies an event should fire on the first 
             tradeable date for the specified
                    
             symbol of each week
        
        
            symbol: The symbol whose exchange is used to determine 
             the first
                    tradeable date of the week
        
            Returns: A date rule that fires on the first tradeable 
             date for the specified security each week
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, securities, timeZone):
        """ __new__(cls: type, securities: SecurityManager, timeZone: DateTimeZone) """
        pass

    Today = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies an event should only fire today in the algorithm's time zone
            using _securities.UtcTime instead of 'start' since ScheduleManager backs it up a day

Get: Today(self: DateRules) -> IDateRule

"""

    Tomorrow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies an event should only fire tomorrow in the algorithm's time zone
            using _securities.UtcTime instead of 'start' since ScheduleManager backs it up a day

Get: Tomorrow(self: DateRules) -> IDateRule

"""



class FluentScheduledEventBuilder(object, IFluentSchedulingDateSpecifier, IFluentSchedulingRunnable, IFluentSchedulingTimeSpecifier):
    """
    Provides a builder class to allow for fluent syntax when constructing new events
    
    FluentScheduledEventBuilder(schedule: ScheduleManager, securities: SecurityManager, name: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, schedule, securities, name):
        """ __new__(cls: type, schedule: ScheduleManager, securities: SecurityManager, name: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class FuncDateRule(object, IDateRule):
    """
    Uses a function to define an enumerable of dates over a requested start/end period
    
    FuncDateRule(name: str, getDatesFunction: Func[DateTime, DateTime, IEnumerable[DateTime]])
    """
    def GetDates(self, start, end):
        """
        GetDates(self: FuncDateRule, start: DateTime, end: DateTime) -> IEnumerable[DateTime]
        
            Gets the dates produced by this date rule between 
             the specified times
        
        
            start: The start of the interval to produce dates for
            end: The end of the interval to produce dates for
            Returns: All dates in the interval matching this date rule
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, getDatesFunction):
        """ __new__(cls: type, name: str, getDatesFunction: Func[DateTime, DateTime, IEnumerable[DateTime]]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a name for this rule

Get: Name(self: FuncDateRule) -> str

"""



class FuncTimeRule(object, ITimeRule):
    """
    Uses a function to define a time rule as a projection of date times to date times
    
    FuncTimeRule(name: str, createUtcEventTimesFunction: Func[IEnumerable[DateTime], IEnumerable[DateTime]])
    """
    def CreateUtcEventTimes(self, dates):
        """ CreateUtcEventTimes(self: FuncTimeRule, dates: IEnumerable[DateTime]) -> IEnumerable[DateTime] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, createUtcEventTimesFunction):
        """ __new__(cls: type, name: str, createUtcEventTimesFunction: Func[IEnumerable[DateTime], IEnumerable[DateTime]]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a name for this rule

Get: Name(self: FuncTimeRule) -> str

"""



class IDateRule:
    """ Specifies dates that events should be fired, used in conjunction with the QuantConnect.Scheduling.ITimeRule """
    def GetDates(self, start, end):
        """
        GetDates(self: IDateRule, start: DateTime, end: DateTime) -> IEnumerable[DateTime]
        
            Gets the dates produced by this date rule between 
             the specified times
        
        
            start: The start of the interval to produce dates for
            end: The end of the interval to produce dates for
            Returns: All dates in the interval matching this date rule
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a name for this rule

Get: Name(self: IDateRule) -> str

"""



class IEventSchedule:
    """ Provides the ability to add/remove scheduled events from the real time handler """
    def Add(self, scheduledEvent):
        """
        Add(self: IEventSchedule, scheduledEvent: ScheduledEvent)
            Adds the specified event to the schedule
        
            scheduledEvent: The event to be scheduled, including the 
             date/times the event fires and the callback
        """
        pass

    def Remove(self, scheduledEvent):
        """
        Remove(self: IEventSchedule, scheduledEvent: ScheduledEvent)
            Removes the specified event from the schedule
        
            scheduledEvent: The event to be removed
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IFluentSchedulingDateSpecifier:
    """ Specifies the date rule component of a scheduled event """
    def Every(self, days):
        """
        Every(self: IFluentSchedulingDateSpecifier, *days: Array[DayOfWeek]) -> IFluentSchedulingTimeSpecifier
        
            Creates events on each of the specified day of 
             week
        """
        pass

    def EveryDay(self, symbol=None):
        """
        EveryDay(self: IFluentSchedulingDateSpecifier) -> IFluentSchedulingTimeSpecifier
        
            Creates events on every day of the year
        EveryDay(self: IFluentSchedulingDateSpecifier, symbol: Symbol) -> IFluentSchedulingTimeSpecifier
        
            Creates events on every trading day of the year 
             for the symbol
        """
        pass

    def MonthStart(self, symbol=None):
        """
        MonthStart(self: IFluentSchedulingDateSpecifier) -> IFluentSchedulingTimeSpecifier
        
            Creates events on the first day of the month
        MonthStart(self: IFluentSchedulingDateSpecifier, symbol: Symbol) -> IFluentSchedulingTimeSpecifier
        
            Creates events on the first trading day of the 
             month
        """
        pass

    def On(self, *__args):
        """
        On(self: IFluentSchedulingDateSpecifier, year: int, month: int, day: int) -> IFluentSchedulingTimeSpecifier
        
            Creates events only on the specified date
        On(self: IFluentSchedulingDateSpecifier, *dates: Array[DateTime]) -> IFluentSchedulingTimeSpecifier
        
            Creates events only on the specified dates
        """
        pass

    def Where(self, predicate):
        """ Where(self: IFluentSchedulingDateSpecifier, predicate: Func[DateTime, bool]) -> IFluentSchedulingTimeSpecifier """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IFluentSchedulingTimeSpecifier:
    """ Specifies the time rule component of a scheduled event """
    def AfterMarketOpen(self, symbol, minutesAfterOpen, extendedMarketOpen):
        """
        AfterMarketOpen(self: IFluentSchedulingTimeSpecifier, symbol: Symbol, minutesAfterOpen: float, extendedMarketOpen: bool) -> IFluentSchedulingRunnable
        
            Creates events that fire a specified number of 
             minutes after market open
        """
        pass

    def At(self, *__args):
        """
        At(self: IFluentSchedulingTimeSpecifier, hour: int, minute: int, second: int) -> IFluentSchedulingRunnable
        
            Creates events that fire at the specified time of 
             day in the specified time zone
        
        At(self: IFluentSchedulingTimeSpecifier, hour: int, minute: int, timeZone: DateTimeZone) -> IFluentSchedulingRunnable
        
            Creates events that fire at the specified time of 
             day in the specified time zone
        
        At(self: IFluentSchedulingTimeSpecifier, hour: int, minute: int, second: int, timeZone: DateTimeZone) -> IFluentSchedulingRunnable
        
            Creates events that fire at the specified time of 
             day in the specified time zone
        
        At(self: IFluentSchedulingTimeSpecifier, timeOfDay: TimeSpan, timeZone: DateTimeZone) -> IFluentSchedulingRunnable
        
            Creates events that fire at the specified time of 
             day in the specified time zone
        
        At(self: IFluentSchedulingTimeSpecifier, timeOfDay: TimeSpan) -> IFluentSchedulingRunnable
        
            Creates events that fire at the specific time of 
             day in the algorithm's time zone
        """
        pass

    def BeforeMarketClose(self, symbol, minuteBeforeClose, extendedMarketClose):
        """
        BeforeMarketClose(self: IFluentSchedulingTimeSpecifier, symbol: Symbol, minuteBeforeClose: float, extendedMarketClose: bool) -> IFluentSchedulingRunnable
        
            Creates events that fire a specified numer of 
             minutes before market close
        """
        pass

    def Every(self, interval):
        """
        Every(self: IFluentSchedulingTimeSpecifier, interval: TimeSpan) -> IFluentSchedulingRunnable
        
            Creates events that fire on a period define by 
             the specified interval
        """
        pass

    def Where(self, predicate):
        """ Where(self: IFluentSchedulingTimeSpecifier, predicate: Func[DateTime, bool]) -> IFluentSchedulingTimeSpecifier """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IFluentSchedulingRunnable(IFluentSchedulingTimeSpecifier):
    """ Specifies the callback component of a scheduled event, as well as final filters """
    def DuringMarketHours(self, symbol, extendedMarket):
        """
        DuringMarketHours(self: IFluentSchedulingRunnable, symbol: Symbol, extendedMarket: bool) -> IFluentSchedulingRunnable
        
            Filters the event times to only include times 
             where the symbol's market is considered open
        """
        pass

    def Run(self, callback):
        """
        Run(self: IFluentSchedulingRunnable, callback: Action) -> ScheduledEvent
        
            Register the defined event with the callback
        Run(self: IFluentSchedulingRunnable, callback: Action[DateTime]) -> ScheduledEvent
        Run(self: IFluentSchedulingRunnable, callback: Action[str, DateTime]) -> ScheduledEvent
        """
        pass

    def Where(self, predicate):
        """ Where(self: IFluentSchedulingRunnable, predicate: Func[DateTime, bool]) -> IFluentSchedulingRunnable """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITimeRule:
    """ Specifies times times on dates for events, used in conjunction with QuantConnect.Scheduling.IDateRule """
    def CreateUtcEventTimes(self, dates):
        """ CreateUtcEventTimes(self: ITimeRule, dates: IEnumerable[DateTime]) -> IEnumerable[DateTime] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a name for this rule

Get: Name(self: ITimeRule) -> str

"""



class ScheduledEvent(object, IDisposable):
    """
    Real time self scheduling event
    
    ScheduledEvent(name: str, eventUtcTime: DateTime, callback: Action[str, DateTime])
    ScheduledEvent(name: str, orderedEventUtcTimes: IEnumerable[DateTime], callback: Action[str, DateTime])
    ScheduledEvent(name: str, orderedEventUtcTimes: IEnumerator[DateTime], callback: Action[str, DateTime])
    """
    def Equals(self, obj):
        """
        Equals(self: ScheduledEvent, obj: object) -> bool
        
            Determines whether the specified object is equal 
             to the current object.
        
        
            obj: The object to compare with the current object.
            Returns: true if the specified object  is equal to the 
             current object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScheduledEvent) -> int
        
            Serves as the default hash function.
            Returns: A hash code for the current object.
        """
        pass

    def OnEventFired(self, *args): #cannot find CLR method
        """
        OnEventFired(self: ScheduledEvent, triggerTime: DateTime)
            Event invocator for the 
             QuantConnect.Scheduling.ScheduledEvent.EventFired 
             event
        
        
            triggerTime: The event's time in UTC
        """
        pass

    def ToString(self):
        """
        ToString(self: ScheduledEvent) -> str
        
            Will return the ScheduledEvents name
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, *__args):
        """
        __new__(cls: type, name: str, eventUtcTime: DateTime, callback: Action[str, DateTime])
        __new__(cls: type, name: str, orderedEventUtcTimes: IEnumerable[DateTime], callback: Action[str, DateTime])
        __new__(cls: type, name: str, orderedEventUtcTimes: IEnumerator[DateTime], callback: Action[str, DateTime])
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether this event is enabled

Get: Enabled(self: ScheduledEvent) -> bool

Set: Enabled(self: ScheduledEvent) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an identifier for this event

Get: Name(self: ScheduledEvent) -> str

"""

    NextEventUtcTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the next time this scheduled event will fire in UTC

Get: NextEventUtcTime(self: ScheduledEvent) -> DateTime

"""


    AlgorithmEndOfDayDelta = None
    EventFired = None
    SecurityEndOfDayDelta = None


class ScheduledEventException(Exception, ISerializable, _Exception):
    """
    Throw this if there is an exception in the callback function of the scheduled event
    
    ScheduledEventException(name: str, message: str, innerException: Exception)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, message, innerException):
        """ __new__(cls: type, name: str, message: str, innerException: Exception) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ScheduledEventName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the scheduled event

Get: ScheduledEventName(self: ScheduledEventException) -> str

"""


    SerializeObjectState = None


class ScheduleManager(object, IEventSchedule):
    """
    Provides access to the real time handler's event scheduling feature
    
    ScheduleManager(securities: SecurityManager, timeZone: DateTimeZone)
    """
    def Add(self, scheduledEvent):
        """
        Add(self: ScheduleManager, scheduledEvent: ScheduledEvent)
            Adds the specified event to the schedule
        
            scheduledEvent: The event to be scheduled, including the 
             date/times the event fires and the callback
        """
        pass

    def Event(self, name=None):
        """
        Event(self: ScheduleManager) -> IFluentSchedulingDateSpecifier
        
            Entry point for the fluent scheduled event builder
        Event(self: ScheduleManager, name: str) -> IFluentSchedulingDateSpecifier
        
            Entry point for the fluent scheduled event builder
        """
        pass

    def On(self, *__args):
        """
        On(self: ScheduleManager, dateRule: IDateRule, timeRule: ITimeRule, callback: Action) -> ScheduledEvent
        
            Schedules the callback to run using the specified 
             date and time rules
        
        
            dateRule: Specifies what dates the event should run
            timeRule: Specifies the times on those dates the event 
             should run
        
            callback: The callback to be invoked
        On(self: ScheduleManager, dateRule: IDateRule, timeRule: ITimeRule, callback: PyObject) -> ScheduledEvent
        
            Schedules the callback to run using the specified 
             date and time rules
        
        
            dateRule: Specifies what dates the event should run
            timeRule: Specifies the times on those dates the event 
             should run
        
            callback: The callback to be invoked
        On(self: ScheduleManager, dateRule: IDateRule, timeRule: ITimeRule, callback: Action[str, DateTime]) -> ScheduledEvent
        On(self: ScheduleManager, name: str, dateRule: IDateRule, timeRule: ITimeRule, callback: Action) -> ScheduledEvent
        
            Schedules the callback to run using the specified 
             date and time rules
        
        
            name: The event's unique name
            dateRule: Specifies what dates the event should run
            timeRule: Specifies the times on those dates the event 
             should run
        
            callback: The callback to be invoked
        On(self: ScheduleManager, name: str, dateRule: IDateRule, timeRule: ITimeRule, callback: PyObject) -> ScheduledEvent
        
            Schedules the callback to run using the specified 
             date and time rules
        
        
            name: The event's unique name
            dateRule: Specifies what dates the event should run
            timeRule: Specifies the times on those dates the event 
             should run
        
            callback: The callback to be invoked
        On(self: ScheduleManager, name: str, dateRule: IDateRule, timeRule: ITimeRule, callback: Action[str, DateTime]) -> ScheduledEvent
        """
        pass

    def Remove(self, scheduledEvent):
        """
        Remove(self: ScheduleManager, scheduledEvent: ScheduledEvent)
            Removes the specified event from the schedule
        
            scheduledEvent: The event to be removed
        """
        pass

    def Training(self, dateRule, timeRule, trainingCode):
        """
        Training(self: ScheduleManager, dateRule: IDateRule, timeRule: ITimeRule, trainingCode: Action) -> ScheduledEvent
        
            Schedules the training code to run using the 
             specified date and time rules
        
        
            dateRule: Specifies what dates the event should run
            timeRule: Specifies the times on those dates the event 
             should run
        
            trainingCode: The training code to be invoked
        Training(self: ScheduleManager, dateRule: IDateRule, timeRule: ITimeRule, trainingCode: PyObject) -> ScheduledEvent
        
            Schedules the training code to run using the 
             specified date and time rules
        
        
            dateRule: Specifies what dates the event should run
            timeRule: Specifies the times on those dates the event 
             should run
        
            trainingCode: The training code to be invoked
        Training(self: ScheduleManager, dateRule: IDateRule, timeRule: ITimeRule, trainingCode: Action[DateTime]) -> ScheduledEvent
        """
        pass

    def TrainingNow(self, trainingCode):
        """
        TrainingNow(self: ScheduleManager, trainingCode: Action) -> ScheduledEvent
        
            Schedules the provided training code to execute 
             immediately
        
        TrainingNow(self: ScheduleManager, trainingCode: PyObject) -> ScheduledEvent
        
            Schedules the provided training code to execute 
             immediately
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, securities, timeZone):
        """ __new__(cls: type, securities: SecurityManager, timeZone: DateTimeZone) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DateRules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the date rules helper object to make specifying dates for events easier

Get: DateRules(self: ScheduleManager) -> DateRules

"""

    TimeRules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time rules helper object to make specifying times for events easier

Get: TimeRules(self: ScheduleManager) -> TimeRules

"""



class TimeConsumer(object):
    """
    Represents a timer consumer instance
    
    TimeConsumer()
    """
    Finished = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the consumer already finished it's work and no longer consumes time

Get: Finished(self: TimeConsumer) -> bool

Set: Finished(self: TimeConsumer) = value
"""

    IsolatorLimitProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The isolator limit provider to be used with this consumer

Get: IsolatorLimitProvider(self: TimeConsumer) -> IIsolatorLimitResultProvider

Set: IsolatorLimitProvider(self: TimeConsumer) = value
"""

    NextTimeRequest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The next time, base on the QuantConnect.Scheduling.TimeConsumer.TimeProvider, that time should be requested
            to be QuantConnect.Scheduling.TimeConsumer.IsolatorLimitProvider

Get: NextTimeRequest(self: TimeConsumer) -> Nullable[DateTime]

Set: NextTimeRequest(self: TimeConsumer) = value
"""

    TimeProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The time provider associated with this consumer

Get: TimeProvider(self: TimeConsumer) -> ITimeProvider

Set: TimeProvider(self: TimeConsumer) = value
"""



class TimeMonitor(object, IDisposable):
    """
    Helper class that will monitor timer consumers and request more time if required.
                Used by QuantConnect.IsolatorLimitResultProvider
    
    TimeMonitor(monitorIntervalMs: int)
    """
    def Add(self, consumer):
        """
        Add(self: TimeMonitor, consumer: TimeConsumer)
            Adds a new time consumer element to be monitored
        
            consumer: Time consumer instance
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TimeMonitor)
            Disposes of the inner timer
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, monitorIntervalMs):
        """ __new__(cls: type, monitorIntervalMs: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of time consumers currently being monitored

Get: Count(self: TimeMonitor) -> int

"""



class TimeRules(object):
    """
    Helper class used to provide better syntax when defining time rules
    
    TimeRules(securities: SecurityManager, timeZone: DateTimeZone)
    """
    def AfterMarketOpen(self, symbol, minutesAfterOpen, extendedMarketOpen):
        """
        AfterMarketOpen(self: TimeRules, symbol: Symbol, minutesAfterOpen: float, extendedMarketOpen: bool) -> ITimeRule
        
            Specifies an event should fire at market open +- 
             minutesAfterOpen
        
        
            symbol: The symbol whose market open we want an event for
            minutesAfterOpen: The minutes after market open that the event 
             should fire
        
            extendedMarketOpen: True to use extended market open, false to use 
             regular market open
        
            Returns: A time rule that fires the specified number of 
             minutes after the symbol's market open
        """
        pass

    def At(self, *__args):
        """
        At(self: TimeRules, timeOfDay: TimeSpan) -> ITimeRule
        
            Specifies an event should fire at the specified 
             time of day in the algorithm's time zone
        
        
            timeOfDay: The time of day in the algorithm's time zone the 
             event should fire
        
            Returns: A time rule that fires at the specified time in 
             the algorithm's time zone
        
        At(self: TimeRules, hour: int, minute: int, second: int) -> ITimeRule
        
            Specifies an event should fire at the specified 
             time of day in the algorithm's time zone
        
        
            hour: The hour
            minute: The minute
            second: The second
            Returns: A time rule that fires at the specified time in 
             the algorithm's time zone
        
        At(self: TimeRules, hour: int, minute: int, timeZone: DateTimeZone) -> ITimeRule
        
            Specifies an event should fire at the specified 
             time of day in the specified time zone
        
        
            hour: The hour
            minute: The minute
            timeZone: The time zone the event time is represented in
            Returns: A time rule that fires at the specified time in 
             the algorithm's time zone
        
        At(self: TimeRules, hour: int, minute: int, second: int, timeZone: DateTimeZone) -> ITimeRule
        
            Specifies an event should fire at the specified 
             time of day in the specified time zone
        
        
            hour: The hour
            minute: The minute
            second: The second
            timeZone: The time zone the event time is represented in
            Returns: A time rule that fires at the specified time in 
             the algorithm's time zone
        
        At(self: TimeRules, timeOfDay: TimeSpan, timeZone: DateTimeZone) -> ITimeRule
        
            Specifies an event should fire at the specified 
             time of day in the specified time zone
        
        
            timeOfDay: The time of day in the algorithm's time zone the 
             event should fire
        
            timeZone: The time zone the date time is expressed in
            Returns: A time rule that fires at the specified time in 
             the algorithm's time zone
        """
        pass

    def BeforeMarketClose(self, symbol, minutesBeforeClose, extendedMarketClose):
        """
        BeforeMarketClose(self: TimeRules, symbol: Symbol, minutesBeforeClose: float, extendedMarketClose: bool) -> ITimeRule
        
            Specifies an event should fire at the market 
             close +- minutesBeforeClose
        
        
            symbol: The symbol whose market close we want an event for
            minutesBeforeClose: The time before market close that the event 
             should fire
        
            extendedMarketClose: True to use extended market close, false to use 
             regular market close
        
            Returns: A time rule that fires the specified number of 
             minutes before the symbol's market close
        """
        pass

    def Every(self, interval):
        """
        Every(self: TimeRules, interval: TimeSpan) -> ITimeRule
        
            Specifies an event should fire periodically on 
             the requested interval
        
        
            interval: The frequency with which the event should fire, 
             can not be zero or less
        
            Returns: A time rule that fires after each interval passes
        """
        pass

    def SetDefaultTimeZone(self, timeZone):
        """
        SetDefaultTimeZone(self: TimeRules, timeZone: DateTimeZone)
            Sets the default time zone
        
            timeZone: The time zone to use for helper methods that 
             can't resolve a time zone
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, securities, timeZone):
        """ __new__(cls: type, securities: SecurityManager, timeZone: DateTimeZone) """
        pass

    Midnight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Convenience property for running a scheduled event at midnight in the algorithm time zone

Get: Midnight(self: TimeRules) -> ITimeRule

"""

    Noon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Convenience property for running a scheduled event at noon in the algorithm time zone

Get: Noon(self: TimeRules) -> ITimeRule

"""

    Now = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies an event should fire at the current time

Get: Now(self: TimeRules) -> ITimeRule

"""



