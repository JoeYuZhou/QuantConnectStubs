# encoding: utf-8
# module QuantConnect.Indicators calls itself Indicators
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# functions

def IIndicator(*args, **kwargs): # real signature unknown
    """
    Represents an indicator that can receive data updates and emit events when the value of
                the indicator has changed.
    """
    pass

# classes

class IIndicatorWarmUpPeriodProvider:
    """ Represents an indicator with a warm up period provider. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.

Get: WarmUpPeriod(self: IIndicatorWarmUpPeriodProvider) -> int

"""



class IndicatorDataPoint(BaseData, IBaseData, IEquatable[IndicatorDataPoint], IComparable[IndicatorDataPoint], IComparable):
    """
    Represents a piece of data at a specific time
    
    IndicatorDataPoint()
    IndicatorDataPoint(time: DateTime, value: Decimal)
    IndicatorDataPoint(symbol: Symbol, time: DateTime, value: Decimal)
    """
    def CompareTo(self, *__args):
        """
        CompareTo(self: IndicatorDataPoint, other: IndicatorDataPoint) -> int
        
            Compares the current object with another object 
             of the same type.
        
        
            other: An object to compare with this object.
            Returns: A value that indicates the relative order of the 
             objects being compared. The return value has the 
             following meanings: Value Meaning Less than zero 
             This object is less than the other parameter.Zero 
             This object is equal to other. Greater than zero 
             This object is greater than other.
        
        CompareTo(self: IndicatorDataPoint, obj: object) -> int
        
            Compares the current instance with another object 
             of the same type and returns an integer that 
             indicates whether the current instance precedes, 
             follows, or occurs in the same position in the 
             sort order as the other object.
        
        
            obj: An object to compare with this instance.
            Returns: A value that indicates the relative order of the 
             objects being compared. The return value has 
             these meanings: Value Meaning Less than zero This 
             instance precedes obj in the sort order. Zero 
             This instance occurs in the same position in the 
             sort order as obj. Greater than zero This 
             instance follows obj in the sort order.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: IndicatorDataPoint, other: IndicatorDataPoint) -> bool
        
            Indicates whether the current object is equal to 
             another object of the same type.
        
        
            other: An object to compare with this object.
            Returns: true if the current object is equal to the other 
             parameter; otherwise, false.
        
        Equals(self: IndicatorDataPoint, obj: object) -> bool
        
            Indicates whether this instance and a specified 
             object are equal.
        
        
            obj: Another object to compare to.
            Returns: true if obj and this instance are the same type 
             and represent the same value; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: IndicatorDataPoint) -> int
        
            Returns the hash code for this instance.
            Returns: A 32-bit signed integer that is the hash code for 
             this instance.
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: IndicatorDataPoint, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            This function is purposefully not implemented.
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: IndicatorDataPoint, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            This function is purposefully not implemented.
        """
        pass

    def ToString(self):
        """
        ToString(self: IndicatorDataPoint) -> str
        
            Returns a string representation of this DataPoint 
             instance using ISO8601 formatting for the date
        
            Returns: A System.String containing a fully qualified type 
             name.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, time: DateTime, value: Decimal)
        __new__(cls: type, symbol: Symbol, time: DateTime, value: Decimal)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class IndicatorUpdatedHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Event handler type for the IndicatorBase.Updated event
    
    IndicatorUpdatedHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, updated, callback, object):
        """ BeginInvoke(self: IndicatorUpdatedHandler, sender: object, updated: IndicatorDataPoint, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: IndicatorUpdatedHandler, result: IAsyncResult) """
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

    def Invoke(self, sender, updated):
        """ Invoke(self: IndicatorUpdatedHandler, sender: object, updated: IndicatorDataPoint) """
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


class IReadOnlyWindow(IEnumerable[T], IEnumerable):
    # no doc
    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current number of elements in this window

Get: Count(self: IReadOnlyWindow[T]) -> int

"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this window is ready, i.e,
                it has been filled to its capacity, this is when the Size==Count

Get: IsReady(self: IReadOnlyWindow[T]) -> bool

"""

    MostRecentlyRemoved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recently removed item from the window. This is the
                piece of data that just 'fell off' as a result of the most recent
                add. If no items have been removed, this will throw an exception.

Get: MostRecentlyRemoved(self: IReadOnlyWindow[T]) -> T

"""

    Samples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of samples that have been added to this window over its lifetime

Get: Samples(self: IReadOnlyWindow[T]) -> Decimal

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of this window

Get: Size(self: IReadOnlyWindow[T]) -> int

"""



class RollingWindow(object, IReadOnlyWindow[T], IEnumerable[T], IEnumerable):
    """ RollingWindow[T](size: int) """
    def Add(self, item):
        """
        Add(self: RollingWindow[T], item: T)
            Adds an item to this window and shifts all other 
             elements
        
        
            item: The item to be added
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: RollingWindow[T]) -> IEnumerator[T]
        
            Returns an enumerator that iterates through the 
             collection.
        
            Returns: A System.Collections.Generic.IEnumerator that can 
             be used to iterate through the collection.
        """
        pass

    def Reset(self):
        """
        Reset(self: RollingWindow[T])
            Clears this window of all data
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, size):
        """ __new__(cls: type, size: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current number of elements in this window

Get: Count(self: RollingWindow[T]) -> int

"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this window is ready, i.e,
                it has been filled to its capacity

Get: IsReady(self: RollingWindow[T]) -> bool

"""

    MostRecentlyRemoved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recently removed item from the window. This is the
                piece of data that just 'fell off' as a result of the most recent
                add. If no items have been removed, this will throw an exception.

Get: MostRecentlyRemoved(self: RollingWindow[T]) -> T

"""

    Samples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of samples that have been added to this window over its lifetime

Get: Samples(self: RollingWindow[T]) -> Decimal

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of this window

Get: Size(self: RollingWindow[T]) -> int

"""



