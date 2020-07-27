# encoding: utf-8
# module QuantConnect.Data.Consolidators calls itself Consolidators
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# functions

def FilteredIdentityDataConsolidator(*args, **kwargs): # real signature unknown
    """ Provides factory methods for creating instances of QuantConnect.Data.Consolidators.FilteredIdentityDataConsolidator """
    pass

def RenkoConsolidator(barSize, type): # real signature unknown; restored from __doc__
    """
    This consolidator can transform a stream of QuantConnect.Data.BaseData instances into a stream of QuantConnect.Data.Market.RenkoBar
    
    RenkoConsolidator(barSize: Decimal, type: RenkoType)
    RenkoConsolidator(barSize: Decimal, evenBars: bool)
    RenkoConsolidator(barSize: Decimal, selector: Func[IBaseData, Decimal], volumeSelector: Func[IBaseData, Decimal], evenBars: bool)
    RenkoConsolidator(barSize: Decimal, selector: PyObject, volumeSelector: PyObject, evenBars: bool)
    """
    pass

# classes

class BaseDataConsolidator(TradeBarConsolidatorBase[BaseData], IDataConsolidator, IDisposable):
    """
    Type capable of consolidating trade bars from any base data instance
    
    BaseDataConsolidator(period: TimeSpan)
    BaseDataConsolidator(maxCount: int)
    BaseDataConsolidator(maxCount: int, period: TimeSpan)
    BaseDataConsolidator(func: Func[DateTime, CalendarInfo])
    BaseDataConsolidator(pyfuncobj: PyObject)
    """
    def AggregateBar(self, *args): #cannot find CLR method
        """
        AggregateBar(self: BaseDataConsolidator, workingBar: TradeBar, data: BaseData) -> TradeBar
        
            Aggregates the new 'data' into the 'workingBar'. 
             The 'workingBar' will be
                    null 
             following the event firing
        
        
            workingBar: The bar we're building, null if the event was 
             just fired and we're starting a new trade bar
        
            data: The new data
        """
        pass

    @staticmethod
    def FromResolution(resolution):
        """
        FromResolution(resolution: Resolution) -> BaseDataConsolidator
        
            Create a new TickConsolidator for the desired 
             resolution
        
        
            resolution: The resolution desired
            Returns: A consolidator that produces data on the 
             resolution interval
        """
        pass

    def GetRoundedBarTime(self, *args): #cannot find CLR method
        """
        GetRoundedBarTime(self: PeriodCountConsolidatorBase[BaseData, TradeBar], time: DateTime) -> DateTime
        
            Gets a rounded-down bar time. Called by 
             AggregateBar in derived classes.
        
        
            time: The bar time to be rounded down
            Returns: The rounded bar time
        """
        pass

    def OnDataConsolidated(self, *args): #cannot find CLR method
        """
        OnDataConsolidated(self: PeriodCountConsolidatorBase[BaseData, TradeBar], e: TradeBar)OnDataConsolidated(self: DataConsolidator[BaseData], consolidated: IBaseData)
            Event invocator for the DataConsolidated event. 
             This should be invoked
                    by derived 
             classes when they have consolidated a new piece 
             of data.
        
        
            consolidated: The newly consolidated data
        """
        pass

    def ShouldProcess(self, *args): #cannot find CLR method
        """ ShouldProcess(self: PeriodCountConsolidatorBase[BaseData, TradeBar], data: BaseData) -> bool """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, period: TimeSpan)
        __new__(cls: type, maxCount: int)
        __new__(cls: type, maxCount: int, period: TimeSpan)
        __new__(cls: type, func: Func[DateTime, CalendarInfo])
        __new__(cls: type, pyfuncobj: PyObject)
        """
        pass

    IsTimeBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this consolidator is time-based, false otherwise

"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time period for this consolidator

"""



class Calendar(object):
    """ Helper class that provides System.Func used to define consolidation calendar """
    def Monthly(self, *args): #cannot find CLR method
        """ Func[DateTime, CalendarInfo](object: object, method: IntPtr) """
        pass

    def Quarterly(self, *args): #cannot find CLR method
        """ Func[DateTime, CalendarInfo](object: object, method: IntPtr) """
        pass

    def Weekly(self, *args): #cannot find CLR method
        """ Func[DateTime, CalendarInfo](object: object, method: IntPtr) """
        pass

    def Yearly(self, *args): #cannot find CLR method
        """ Func[DateTime, CalendarInfo](object: object, method: IntPtr) """
        pass

    __all__ = []


class CalendarInfo(object):
    """ CalendarInfo(start: DateTime, period: TimeSpan) """
    @staticmethod # known case of __new__
    def __new__(self, start, period):
        """
        __new__(cls: type, start: DateTime, period: TimeSpan)
        __new__[CalendarInfo]() -> CalendarInfo
        """
        pass

    Period = None
    Start = None


class CalendarType(object):
    # no doc
    def Monthly(self, *args): #cannot find CLR method
        """ Func[DateTime, CalendarInfo](object: object, method: IntPtr) """
        pass

    def Weekly(self, *args): #cannot find CLR method
        """ Func[DateTime, CalendarInfo](object: object, method: IntPtr) """
        pass

    __all__ = []


class DataConsolidatedHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Event handler type for the IDataConsolidator.DataConsolidated event
    
    DataConsolidatedHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, consolidated, callback, object):
        """ BeginInvoke(self: DataConsolidatedHandler, sender: object, consolidated: IBaseData, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified 
             System.Delegate to form a new delegate.
        
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the 
             System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method 
             represented by the current delegate.
        
        
            args: An array of objects that are the arguments to 
             pass to the method represented by the current 
             delegate.-or- null, if the method represented by 
             the current delegate does not require arguments.
        
            Returns: The object returned by the method represented by 
             the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DataConsolidatedHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the 
             current System.MulticastDelegate.
        
            Returns: A static method represented by the current 
             System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, consolidated):
        """ Invoke(self: DataConsolidatedHandler, sender: object, consolidated: IBaseData) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of 
             this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this 
             instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this 
             instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class DataConsolidator(object, IDataConsolidator, IDisposable):
    # no doc
    def Dispose(self):
        """
        Dispose(self: DataConsolidator[TInput])
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def OnDataConsolidated(self, *args): #cannot find CLR method
        """
        OnDataConsolidated(self: DataConsolidator[TInput], consolidated: IBaseData)
            Event invocator for the DataConsolidated event. 
             This should be invoked
                    by derived 
             classes when they have consolidated a new piece 
             of data.
        
        
            consolidated: The newly consolidated data
        """
        pass

    def Scan(self, currentLocalTime):
        """
        Scan(self: DataConsolidator[TInput], currentLocalTime: DateTime)
            Scans this consolidator to see if it should emit 
             a bar due to time passing
        
        
            currentLocalTime: The current time in the local time zone (same as 
             QuantConnect.Data.BaseData.Time)
        """
        pass

    def Update(self, data):
        """
        Update(self: DataConsolidator[TInput], data: IBaseData)
            Updates this consolidator with the specified data
        
            data: The new data for the consolidator
        Update(self: DataConsolidator[TInput], data: TInput)
            Updates this consolidator with the specified 
             data. This method is
                    responsible for 
             raising the DataConsolidated event
        
        
            data: The new data for the consolidator
        """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Consolidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recently consolidated piece of data. This will be null if this consolidator
            has not produced any data yet.

Get: Consolidated(self: DataConsolidator[TInput]) -> IBaseData

"""

    InputType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type consumed by this consolidator

Get: InputType(self: DataConsolidator[TInput]) -> Type

"""

    OutputType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type produced by this consolidator

Get: OutputType(self: DataConsolidator[TInput]) -> Type

"""

    WorkingData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a clone of the data being currently consolidated

Get: WorkingData(self: DataConsolidator[TInput]) -> IBaseData

"""


    DataConsolidated = None


class DynamicDataConsolidator(TradeBarConsolidatorBase[DynamicData], IDataConsolidator, IDisposable):
    """
    A data csolidator that can make trade bars from DynamicData derived types. This is useful for
                aggregating Quandl and other highly flexible dynamic custom data types.
    
    DynamicDataConsolidator(period: TimeSpan)
    DynamicDataConsolidator(maxCount: int)
    DynamicDataConsolidator(maxCount: int, period: TimeSpan)
    DynamicDataConsolidator(func: Func[DateTime, CalendarInfo])
    """
    def AggregateBar(self, *args): #cannot find CLR method
        """
        AggregateBar(self: DynamicDataConsolidator, workingBar: TradeBar, data: DynamicData) -> TradeBar
        
            Aggregates the new 'data' into the 'workingBar'. 
             The 'workingBar' will be
                    null 
             following the event firing
        
        
            workingBar: The bar we're building, null if the event was 
             just fired and we're starting a new trade bar
        
            data: The new data
        """
        pass

    def GetRoundedBarTime(self, *args): #cannot find CLR method
        """
        GetRoundedBarTime(self: PeriodCountConsolidatorBase[DynamicData, TradeBar], time: DateTime) -> DateTime
        
            Gets a rounded-down bar time. Called by 
             AggregateBar in derived classes.
        
        
            time: The bar time to be rounded down
            Returns: The rounded bar time
        """
        pass

    def OnDataConsolidated(self, *args): #cannot find CLR method
        """
        OnDataConsolidated(self: PeriodCountConsolidatorBase[DynamicData, TradeBar], e: TradeBar)OnDataConsolidated(self: DataConsolidator[DynamicData], consolidated: IBaseData)
            Event invocator for the DataConsolidated event. 
             This should be invoked
                    by derived 
             classes when they have consolidated a new piece 
             of data.
        
        
            consolidated: The newly consolidated data
        """
        pass

    def ShouldProcess(self, *args): #cannot find CLR method
        """ ShouldProcess(self: PeriodCountConsolidatorBase[DynamicData, TradeBar], data: DynamicData) -> bool """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, period: TimeSpan)
        __new__(cls: type, maxCount: int)
        __new__(cls: type, maxCount: int, period: TimeSpan)
        __new__(cls: type, func: Func[DateTime, CalendarInfo])
        """
        pass

    IsTimeBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this consolidator is time-based, false otherwise

"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time period for this consolidator

"""



class IDataConsolidator(IDisposable):
    """
    Represents a type capable of taking BaseData updates and firing events containing new
                'consolidated' data. These types can be used to produce larger bars, or even be used to
                transform the data before being sent to another component. The most common usage of these
                types is with indicators.
    """
    def Scan(self, currentLocalTime):
        """
        Scan(self: IDataConsolidator, currentLocalTime: DateTime)
            Scans this consolidator to see if it should emit 
             a bar due to time passing
        
        
            currentLocalTime: The current time in the local time zone (same as 
             QuantConnect.Data.BaseData.Time)
        """
        pass

    def Update(self, data):
        """
        Update(self: IDataConsolidator, data: IBaseData)
            Updates this consolidator with the specified data
        
            data: The new data for the consolidator
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Consolidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recently consolidated piece of data. This will be null if this consolidator
            has not produced any data yet.

Get: Consolidated(self: IDataConsolidator) -> IBaseData

"""

    InputType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type consumed by this consolidator

Get: InputType(self: IDataConsolidator) -> Type

"""

    OutputType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type produced by this consolidator

Get: OutputType(self: IDataConsolidator) -> Type

"""

    WorkingData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a clone of the data being currently consolidated

Get: WorkingData(self: IDataConsolidator) -> IBaseData

"""


    DataConsolidated = None


class IdentityDataConsolidator(DataConsolidator[T], IDataConsolidator, IDisposable):
    """ IdentityDataConsolidator[T]() """
    def OnDataConsolidated(self, *args): #cannot find CLR method
        """
        OnDataConsolidated(self: DataConsolidator[T], consolidated: IBaseData)
            Event invocator for the DataConsolidated event. 
             This should be invoked
                    by derived 
             classes when they have consolidated a new piece 
             of data.
        
        
            consolidated: The newly consolidated data
        """
        pass

    def Scan(self, currentLocalTime):
        """
        Scan(self: IdentityDataConsolidator[T], currentLocalTime: DateTime)
            Scans this consolidator to see if it should emit 
             a bar due to time passing
        
        
            currentLocalTime: The current time in the local time zone (same as 
             QuantConnect.Data.BaseData.Time)
        """
        pass

    def Update(self, data):
        """
        Update(self: IdentityDataConsolidator[T], data: T)
            Updates this consolidator with the specified data
        
            data: The new data for the consolidator
        """
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

    OutputType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type produced by this consolidator

Get: OutputType(self: IdentityDataConsolidator[T]) -> Type

"""

    WorkingData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a clone of the data being currently consolidated

Get: WorkingData(self: IdentityDataConsolidator[T]) -> IBaseData

"""



class OpenInterestConsolidator(PeriodCountConsolidatorBase[Tick, OpenInterest], IDataConsolidator, IDisposable):
    """
    Type capable of consolidating open interest
    
    OpenInterestConsolidator(period: TimeSpan)
    OpenInterestConsolidator(maxCount: int)
    OpenInterestConsolidator(maxCount: int, period: TimeSpan)
    OpenInterestConsolidator(func: Func[DateTime, CalendarInfo])
    OpenInterestConsolidator(pyfuncobj: PyObject)
    """
    def AggregateBar(self, *args): #cannot find CLR method
        """
        AggregateBar(self: OpenInterestConsolidator, workingBar: OpenInterest, tick: Tick) -> OpenInterest
        
            Aggregates the new 'data' into the 'workingBar'. 
             The 'workingBar' will be
                    null 
             following the event firing
        
        
            workingBar: The bar we're building, null if the event was 
             just fired and we're starting a new OI bar
        
            tick: The new data
        """
        pass

    @staticmethod
    def FromResolution(resolution):
        """
        FromResolution(resolution: Resolution) -> OpenInterestConsolidator
        
            Create a new OpenInterestConsolidator for the 
             desired resolution
        
        
            resolution: The resolution desired
            Returns: A consolidator that produces data on the 
             resolution interval
        """
        pass

    def GetRoundedBarTime(self, *args): #cannot find CLR method
        """
        GetRoundedBarTime(self: PeriodCountConsolidatorBase[Tick, OpenInterest], time: DateTime) -> DateTime
        
            Gets a rounded-down bar time. Called by 
             AggregateBar in derived classes.
        
        
            time: The bar time to be rounded down
            Returns: The rounded bar time
        """
        pass

    def OnDataConsolidated(self, *args): #cannot find CLR method
        """
        OnDataConsolidated(self: PeriodCountConsolidatorBase[Tick, OpenInterest], e: OpenInterest)OnDataConsolidated(self: DataConsolidator[Tick], consolidated: IBaseData)
            Event invocator for the DataConsolidated event. 
             This should be invoked
                    by derived 
             classes when they have consolidated a new piece 
             of data.
        
        
            consolidated: The newly consolidated data
        """
        pass

    def ShouldProcess(self, *args): #cannot find CLR method
        """
        ShouldProcess(self: OpenInterestConsolidator, tick: Tick) -> bool
        
            Determines whether or not the specified data 
             should be processed
        
        
            tick: The data to check
            Returns: True if the consolidator should process this 
             data, false otherwise
        """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, period: TimeSpan)
        __new__(cls: type, maxCount: int)
        __new__(cls: type, maxCount: int, period: TimeSpan)
        __new__(cls: type, func: Func[DateTime, CalendarInfo])
        __new__(cls: type, pyfuncobj: PyObject)
        """
        pass

    IsTimeBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this consolidator is time-based, false otherwise

"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time period for this consolidator

"""



class PeriodCountConsolidatorBase(DataConsolidator[T], IDataConsolidator, IDisposable):
    # no doc
    def AggregateBar(self, *args): #cannot find CLR method
# Error generating skeleton for function AggregateBar: Method must be called on a Type for which Type.IsGenericParameter is false.

    def GetRoundedBarTime(self, *args): #cannot find CLR method
        """
        GetRoundedBarTime(self: PeriodCountConsolidatorBase[T, TConsolidated], time: DateTime) -> DateTime
        
            Gets a rounded-down bar time. Called by 
             AggregateBar in derived classes.
        
        
            time: The bar time to be rounded down
            Returns: The rounded bar time
        """
        pass

    def OnDataConsolidated(self, *args): #cannot find CLR method
        """
        OnDataConsolidated(self: PeriodCountConsolidatorBase[T, TConsolidated], e: TConsolidated)
            Event invocator for the 
             QuantConnect.Data.Consolidators.PeriodCountConsoli
             datorBase event
        
        
            e: The consolidated data
        OnDataConsolidated(self: DataConsolidator[T], consolidated: IBaseData)
            Event invocator for the DataConsolidated event. 
             This should be invoked
                    by derived 
             classes when they have consolidated a new piece 
             of data.
        
        
            consolidated: The newly consolidated data
        """
        pass

    def Scan(self, currentLocalTime):
        """
        Scan(self: PeriodCountConsolidatorBase[T, TConsolidated], currentLocalTime: DateTime)
            Scans this consolidator to see if it should emit 
             a bar due to time passing
        
        
            currentLocalTime: The current time in the local time zone (same as 
             QuantConnect.Data.BaseData.Time)
        """
        pass

    def ShouldProcess(self, *args): #cannot find CLR method
        """
        ShouldProcess(self: PeriodCountConsolidatorBase[T, TConsolidated], data: T) -> bool
        
            Determines whether or not the specified data 
             should be processed
        
        
            data: The data to check
            Returns: True if the consolidator should process this 
             data, false otherwise
        """
        pass

    def Update(self, data):
        """
        Update(self: PeriodCountConsolidatorBase[T, TConsolidated], data: T)
            Updates this consolidator with the specified 
             data. This method is
                    responsible for 
             raising the DataConsolidated event
                    
             In time span mode, the bar range is closed on the 
             left and open on the right: [T, T+TimeSpan).
            
                     For example, if time span is 1 minute, we 
             have [10:00, 10:01): so data at 10:01 is not 
           
                      included in the bar starting at 10:00.
        
        
            data: The new data for the consolidator
        """
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
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, period: TimeSpan)
        __new__(cls: type, maxCount: int)
        __new__(cls: type, maxCount: int, period: TimeSpan)
        __new__(cls: type, func: Func[DateTime, CalendarInfo])
        __new__(cls: type, pyObject: PyObject)
        """
        pass

    IsTimeBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this consolidator is time-based, false otherwise

"""

    OutputType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type produced by this consolidator

Get: OutputType(self: PeriodCountConsolidatorBase[T, TConsolidated]) -> Type

"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time period for this consolidator

"""

    WorkingData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a clone of the data being currently consolidated

Get: WorkingData(self: PeriodCountConsolidatorBase[T, TConsolidated]) -> IBaseData

"""


    DataConsolidated = None


class QuoteBarConsolidator(PeriodCountConsolidatorBase[QuoteBar, QuoteBar], IDataConsolidator, IDisposable):
    """
    Consolidates QuoteBars into larger QuoteBars
    
    QuoteBarConsolidator(period: TimeSpan)
    QuoteBarConsolidator(maxCount: int)
    QuoteBarConsolidator(maxCount: int, period: TimeSpan)
    QuoteBarConsolidator(func: Func[DateTime, CalendarInfo])
    QuoteBarConsolidator(pyfuncobj: PyObject)
    """
    def AggregateBar(self, *args): #cannot find CLR method
        """
        AggregateBar(self: QuoteBarConsolidator, workingBar: QuoteBar, data: QuoteBar) -> QuoteBar
        
            Aggregates the new 'data' into the 'workingBar'. 
             The 'workingBar' will be
                    null 
             following the event firing
        
        
            workingBar: The bar we're building, null if the event was 
             just fired and we're starting a new consolidated 
             bar
        
            data: The new data
        """
        pass

    def GetRoundedBarTime(self, *args): #cannot find CLR method
        """
        GetRoundedBarTime(self: PeriodCountConsolidatorBase[QuoteBar, QuoteBar], time: DateTime) -> DateTime
        
            Gets a rounded-down bar time. Called by 
             AggregateBar in derived classes.
        
        
            time: The bar time to be rounded down
            Returns: The rounded bar time
        """
        pass

    def OnDataConsolidated(self, *args): #cannot find CLR method
        """
        OnDataConsolidated(self: PeriodCountConsolidatorBase[QuoteBar, QuoteBar], e: QuoteBar)OnDataConsolidated(self: DataConsolidator[QuoteBar], consolidated: IBaseData)
            Event invocator for the DataConsolidated event. 
             This should be invoked
                    by derived 
             classes when they have consolidated a new piece 
             of data.
        
        
            consolidated: The newly consolidated data
        """
        pass

    def ShouldProcess(self, *args): #cannot find CLR method
        """ ShouldProcess(self: PeriodCountConsolidatorBase[QuoteBar, QuoteBar], data: QuoteBar) -> bool """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, period: TimeSpan)
        __new__(cls: type, maxCount: int)
        __new__(cls: type, maxCount: int, period: TimeSpan)
        __new__(cls: type, func: Func[DateTime, CalendarInfo])
        __new__(cls: type, pyfuncobj: PyObject)
        """
        pass

    IsTimeBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this consolidator is time-based, false otherwise

"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time period for this consolidator

"""



class SequentialConsolidator(object, IDataConsolidator, IDisposable):
    """
    This consolidator wires up the events on its First and Second consolidators
                such that data flows from the First to Second consolidator. It's output comes
                from the Second.
    
    SequentialConsolidator(first: IDataConsolidator, second: IDataConsolidator)
    """
    def Dispose(self):
        """
        Dispose(self: SequentialConsolidator)
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def OnDataConsolidated(self, *args): #cannot find CLR method
        """
        OnDataConsolidated(self: SequentialConsolidator, consolidated: IBaseData)
            Event invocator for the DataConsolidated event. 
             This should be invoked
                    by derived 
             classes when they have consolidated a new piece 
             of data.
        
        
            consolidated: The newly consolidated data
        """
        pass

    def Scan(self, currentLocalTime):
        """
        Scan(self: SequentialConsolidator, currentLocalTime: DateTime)
            Scans this consolidator to see if it should emit 
             a bar due to time passing
        
        
            currentLocalTime: The current time in the local time zone (same as 
             QuantConnect.Data.BaseData.Time)
        """
        pass

    def Update(self, data):
        """
        Update(self: SequentialConsolidator, data: IBaseData)
            Updates this consolidator with the specified data
        
            data: The new data for the consolidator
        """
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
    def __new__(self, first, second):
        """ __new__(cls: type, first: IDataConsolidator, second: IDataConsolidator) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Consolidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recently consolidated piece of data. This will be null if this consolidator
             has not produced any data yet.
            
             For a SequentialConsolidator, this is the output from the 'Second' consolidator.

Get: Consolidated(self: SequentialConsolidator) -> IBaseData

"""

    First = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the first consolidator to receive data

Get: First(self: SequentialConsolidator) -> IDataConsolidator

"""

    InputType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type consumed by this consolidator

Get: InputType(self: SequentialConsolidator) -> Type

"""

    OutputType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type produced by this consolidator

Get: OutputType(self: SequentialConsolidator) -> Type

"""

    Second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the second consolidator that ends up receiving data produced
            by the first

Get: Second(self: SequentialConsolidator) -> IDataConsolidator

"""

    WorkingData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a clone of the data being currently consolidated

Get: WorkingData(self: SequentialConsolidator) -> IBaseData

"""


    DataConsolidated = None


class TickConsolidator(TradeBarConsolidatorBase[Tick], IDataConsolidator, IDisposable):
    """
    A data consolidator that can make bigger bars from ticks over a given
                time span or a count of pieces of data.
    
    TickConsolidator(period: TimeSpan)
    TickConsolidator(maxCount: int)
    TickConsolidator(maxCount: int, period: TimeSpan)
    TickConsolidator(func: Func[DateTime, CalendarInfo])
    TickConsolidator(pyfuncobj: PyObject)
    """
    def AggregateBar(self, *args): #cannot find CLR method
        """
        AggregateBar(self: TickConsolidator, workingBar: TradeBar, data: Tick) -> TradeBar
        
            Aggregates the new 'data' into the 'workingBar'. 
             The 'workingBar' will be
                    null 
             following the event firing
        
        
            workingBar: The bar we're building
            data: The new data
        """
        pass

    def GetRoundedBarTime(self, *args): #cannot find CLR method
        """
        GetRoundedBarTime(self: PeriodCountConsolidatorBase[Tick, TradeBar], time: DateTime) -> DateTime
        
            Gets a rounded-down bar time. Called by 
             AggregateBar in derived classes.
        
        
            time: The bar time to be rounded down
            Returns: The rounded bar time
        """
        pass

    def OnDataConsolidated(self, *args): #cannot find CLR method
        """
        OnDataConsolidated(self: PeriodCountConsolidatorBase[Tick, TradeBar], e: TradeBar)OnDataConsolidated(self: DataConsolidator[Tick], consolidated: IBaseData)
            Event invocator for the DataConsolidated event. 
             This should be invoked
                    by derived 
             classes when they have consolidated a new piece 
             of data.
        
        
            consolidated: The newly consolidated data
        """
        pass

    def ShouldProcess(self, *args): #cannot find CLR method
        """
        ShouldProcess(self: TickConsolidator, data: Tick) -> bool
        
            Determines whether or not the specified data 
             should be processed
        
        
            data: The data to check
            Returns: True if the consolidator should process this 
             data, false otherwise
        """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, period: TimeSpan)
        __new__(cls: type, maxCount: int)
        __new__(cls: type, maxCount: int, period: TimeSpan)
        __new__(cls: type, func: Func[DateTime, CalendarInfo])
        __new__(cls: type, pyfuncobj: PyObject)
        """
        pass

    IsTimeBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this consolidator is time-based, false otherwise

"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time period for this consolidator

"""



class TickQuoteBarConsolidator(PeriodCountConsolidatorBase[Tick, QuoteBar], IDataConsolidator, IDisposable):
    """
    Consolidates ticks into quote bars. This consolidator ignores trade ticks
    
    TickQuoteBarConsolidator(period: TimeSpan)
    TickQuoteBarConsolidator(maxCount: int)
    TickQuoteBarConsolidator(maxCount: int, period: TimeSpan)
    TickQuoteBarConsolidator(func: Func[DateTime, CalendarInfo])
    TickQuoteBarConsolidator(pyfuncobj: PyObject)
    """
    def AggregateBar(self, *args): #cannot find CLR method
        """
        AggregateBar(self: TickQuoteBarConsolidator, workingBar: QuoteBar, data: Tick) -> QuoteBar
        
            Aggregates the new 'data' into the 'workingBar'. 
             The 'workingBar' will be
                    null 
             following the event firing
        
        
            workingBar: The bar we're building, null if the event was 
             just fired and we're starting a new consolidated 
             bar
        
            data: The new data
        """
        pass

    def GetRoundedBarTime(self, *args): #cannot find CLR method
        """
        GetRoundedBarTime(self: PeriodCountConsolidatorBase[Tick, QuoteBar], time: DateTime) -> DateTime
        
            Gets a rounded-down bar time. Called by 
             AggregateBar in derived classes.
        
        
            time: The bar time to be rounded down
            Returns: The rounded bar time
        """
        pass

    def OnDataConsolidated(self, *args): #cannot find CLR method
        """
        OnDataConsolidated(self: PeriodCountConsolidatorBase[Tick, QuoteBar], e: QuoteBar)OnDataConsolidated(self: DataConsolidator[Tick], consolidated: IBaseData)
            Event invocator for the DataConsolidated event. 
             This should be invoked
                    by derived 
             classes when they have consolidated a new piece 
             of data.
        
        
            consolidated: The newly consolidated data
        """
        pass

    def ShouldProcess(self, *args): #cannot find CLR method
        """
        ShouldProcess(self: TickQuoteBarConsolidator, data: Tick) -> bool
        
            Determines whether or not the specified data 
             should be processed
        
        
            data: The data to check
            Returns: True if the consolidator should process this 
             data, false otherwise
        """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, period: TimeSpan)
        __new__(cls: type, maxCount: int)
        __new__(cls: type, maxCount: int, period: TimeSpan)
        __new__(cls: type, func: Func[DateTime, CalendarInfo])
        __new__(cls: type, pyfuncobj: PyObject)
        """
        pass

    IsTimeBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this consolidator is time-based, false otherwise

"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time period for this consolidator

"""



class TradeBarConsolidator(TradeBarConsolidatorBase[TradeBar], IDataConsolidator, IDisposable):
    """
    A data consolidator that can make bigger bars from smaller ones over a given
                 time span or a count of pieces of data.
                
                 Use this consolidator to turn data of a lower resolution into data of a higher resolution,
                 for example, if you subscribe to minute data but want to have a 15 minute bar.
    
    TradeBarConsolidator(period: TimeSpan)
    TradeBarConsolidator(maxCount: int)
    TradeBarConsolidator(maxCount: int, period: TimeSpan)
    TradeBarConsolidator(func: Func[DateTime, CalendarInfo])
    TradeBarConsolidator(pyfuncobj: PyObject)
    """
    def AggregateBar(self, *args): #cannot find CLR method
        """
        AggregateBar(self: TradeBarConsolidator, workingBar: TradeBar, data: TradeBar) -> TradeBar
        
            Aggregates the new 'data' into the 'workingBar'. 
             The 'workingBar' will be
                    null 
             following the event firing
        
        
            workingBar: The bar we're building, null if the event was 
             just fired and we're starting a new trade bar
        
            data: The new data
        """
        pass

    @staticmethod
    def FromResolution(resolution):
        """
        FromResolution(resolution: Resolution) -> TradeBarConsolidator
        
            Create a new TradeBarConsolidator for the desired 
             resolution
        
        
            resolution: The resolution desired
            Returns: A consolidator that produces data on the 
             resolution interval
        """
        pass

    def GetRoundedBarTime(self, *args): #cannot find CLR method
        """
        GetRoundedBarTime(self: PeriodCountConsolidatorBase[TradeBar, TradeBar], time: DateTime) -> DateTime
        
            Gets a rounded-down bar time. Called by 
             AggregateBar in derived classes.
        
        
            time: The bar time to be rounded down
            Returns: The rounded bar time
        """
        pass

    def OnDataConsolidated(self, *args): #cannot find CLR method
        """
        OnDataConsolidated(self: PeriodCountConsolidatorBase[TradeBar, TradeBar], e: TradeBar)OnDataConsolidated(self: DataConsolidator[TradeBar], consolidated: IBaseData)
            Event invocator for the DataConsolidated event. 
             This should be invoked
                    by derived 
             classes when they have consolidated a new piece 
             of data.
        
        
            consolidated: The newly consolidated data
        """
        pass

    def ShouldProcess(self, *args): #cannot find CLR method
        """ ShouldProcess(self: PeriodCountConsolidatorBase[TradeBar, TradeBar], data: TradeBar) -> bool """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, period: TimeSpan)
        __new__(cls: type, maxCount: int)
        __new__(cls: type, maxCount: int, period: TimeSpan)
        __new__(cls: type, func: Func[DateTime, CalendarInfo])
        __new__(cls: type, pyfuncobj: PyObject)
        """
        pass

    IsTimeBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this consolidator is time-based, false otherwise

"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time period for this consolidator

"""



class TradeBarConsolidatorBase(PeriodCountConsolidatorBase[T, TradeBar], IDataConsolidator, IDisposable):
    # no doc
    def AggregateBar(self, *args): #cannot find CLR method
        """ AggregateBar(self: PeriodCountConsolidatorBase[T, TradeBar], workingBar: TradeBar, data: T) -> TradeBar """
        pass

    def GetRoundedBarTime(self, *args): #cannot find CLR method
        """
        GetRoundedBarTime(self: PeriodCountConsolidatorBase[T, TradeBar], time: DateTime) -> DateTime
        
            Gets a rounded-down bar time. Called by 
             AggregateBar in derived classes.
        
        
            time: The bar time to be rounded down
            Returns: The rounded bar time
        """
        pass

    def OnDataConsolidated(self, *args): #cannot find CLR method
        """
        OnDataConsolidated(self: PeriodCountConsolidatorBase[T, TradeBar], e: TradeBar)OnDataConsolidated(self: DataConsolidator[T], consolidated: IBaseData)
            Event invocator for the DataConsolidated event. 
             This should be invoked
                    by derived 
             classes when they have consolidated a new piece 
             of data.
        
        
            consolidated: The newly consolidated data
        """
        pass

    def ShouldProcess(self, *args): #cannot find CLR method
        """
        ShouldProcess(self: PeriodCountConsolidatorBase[T, TradeBar], data: T) -> bool
        
            Determines whether or not the specified data 
             should be processed
        
        
            data: The data to check
            Returns: True if the consolidator should process this 
             data, false otherwise
        """
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
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, period: TimeSpan)
        __new__(cls: type, maxCount: int)
        __new__(cls: type, maxCount: int, period: TimeSpan)
        __new__(cls: type, func: Func[DateTime, CalendarInfo])
        __new__(cls: type, pyfuncobj: PyObject)
        """
        pass

    IsTimeBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this consolidator is time-based, false otherwise

"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time period for this consolidator

"""

    WorkingBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a copy of the current 'workingBar'.

Get: WorkingBar(self: TradeBarConsolidatorBase[T]) -> TradeBar

"""



