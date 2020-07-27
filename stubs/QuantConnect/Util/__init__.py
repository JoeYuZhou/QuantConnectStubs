# encoding: utf-8
# module QuantConnect.Util calls itself Util
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# functions

def Ref(*args, **kwargs): # real signature unknown
    """ Provides some helper methods that leverage C# type inference """
    pass

# classes

class BusyBlockingCollection(object, IBusyCollection[T], IDisposable):
    """
    BusyBlockingCollection[T]()
    BusyBlockingCollection[T](boundedCapacity: int)
    """
    def Add(self, item, cancellationToken=None):
        """
        Add(self: BusyBlockingCollection[T], item: T)
            Adds the items to this collection
        
            item: The item to be added
        Add(self: BusyBlockingCollection[T], item: T, cancellationToken: CancellationToken)
            Adds the items to this collection
        
            item: The item to be added
            cancellationToken: A cancellation token to observer
        """
        pass

    def CompleteAdding(self):
        """
        CompleteAdding(self: BusyBlockingCollection[T])
            Marks the 
             QuantConnect.Util.BusyBlockingCollection as not 
             accepting any more additions
        """
        pass

    def Dispose(self):
        """
        Dispose(self: BusyBlockingCollection[T])
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def GetConsumingEnumerable(self, cancellationToken=None):
        """
        GetConsumingEnumerable(self: BusyBlockingCollection[T]) -> IEnumerable[T]
        
            Provides a consuming enumerable for items in this 
             collection.
        
            Returns: An enumerable that removes and returns items from 
             the collection
        
        GetConsumingEnumerable(self: BusyBlockingCollection[T], cancellationToken: CancellationToken) -> IEnumerable[T]
        
            Provides a consuming enumerable for items in this 
             collection.
        
        
            cancellationToken: A cancellation token to observer
            Returns: An enumerable that removes and returns items from 
             the collection
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
    def __new__(self, boundedCapacity=None):
        """
        __new__(cls: type)
        __new__(cls: type, boundedCapacity: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items held within this collection

Get: Count(self: BusyBlockingCollection[T]) -> int

"""

    IsBusy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if processing, false otherwise

Get: IsBusy(self: BusyBlockingCollection[T]) -> bool

"""

    WaitHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a wait handle that can be used to wait until this instance is done
            processing all of it's item

Get: WaitHandle(self: BusyBlockingCollection[T]) -> WaitHandle

"""



class BusyCollection(object, IBusyCollection[T], IDisposable):
    """ BusyCollection[T]() """
    def Add(self, item, cancellationToken=None):
        """
        Add(self: BusyCollection[T], item: T)
            Adds the items to this collection
        
            item: The item to be added
        Add(self: BusyCollection[T], item: T, cancellationToken: CancellationToken)
            Adds the items to this collection
        
            item: The item to be added
            cancellationToken: A cancellation token to observer
        """
        pass

    def CompleteAdding(self):
        """
        CompleteAdding(self: BusyCollection[T])
            Marks the collection as not accepting any more 
             additions
        """
        pass

    def Dispose(self):
        """
        Dispose(self: BusyCollection[T])
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def GetConsumingEnumerable(self, cancellationToken=None):
        """
        GetConsumingEnumerable(self: BusyCollection[T]) -> IEnumerable[T]
        
            Provides a consuming enumerable for items in this 
             collection.
        
            Returns: An enumerable that removes and returns items from 
             the collection
        
        GetConsumingEnumerable(self: BusyCollection[T], cancellationToken: CancellationToken) -> IEnumerable[T]
        
            Provides a consuming enumerable for items in this 
             collection.
        
        
            cancellationToken: A cancellation token to observer
            Returns: An enumerable that removes and returns items from 
             the collection
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items held within this collection

Get: Count(self: BusyCollection[T]) -> int

"""

    IsBusy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if processing, false otherwise

Get: IsBusy(self: BusyCollection[T]) -> bool

"""

    WaitHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a wait handle that can be used to wait until this instance is done
            processing all of it's item

Get: WaitHandle(self: BusyCollection[T]) -> WaitHandle

"""



class CircularQueue(object):
    """
    CircularQueue[T](*items: Array[T])
    CircularQueue[T](items: IEnumerable[T])
    """
    def Dequeue(self):
        """
        Dequeue(self: CircularQueue[T]) -> T
        
            Dequeues the next item
            Returns: The next item
        """
        pass

    def OnCircleCompleted(self, *args): #cannot find CLR method
        """
        OnCircleCompleted(self: CircularQueue[T])
            Event invocator for the 
             QuantConnect.Util.CircularQueue evet
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, items):
        """
        __new__(cls: type, *items: Array[T])
        __new__(cls: type, items: IEnumerable[T])
        """
        pass

    CircleCompleted = None


class ColorJsonConverter(TypeChangeJsonConverter[Color, str]):
    """
    A Newtonsoft.Json.JsonConverter implementation that serializes a System.Drawing.Color as a string.
                If Color is empty, string is also empty and vice-versa. Meaning that color is autogen.
    
    ColorJsonConverter()
    """
    PopulateProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True will populate TResult object returned by QuantConnect.Util.TypeChangeJsonConverter with json properties

"""



class Composer(object):
    """
    Provides methods for obtaining exported MEF instances
    
    Composer()
    """
    def AddPart(self, instance):
        """ AddPart[T](self: Composer, instance: T) """
        pass

    def GetExportedValueByTypeName(self, typeName):
        """ GetExportedValueByTypeName[T](self: Composer, typeName: str) -> T """
        pass

    def GetExportedValues(self):
        """ GetExportedValues[T](self: Composer) -> IEnumerable[T] """
        pass

    def Reset(self):
        """
        Reset(self: Composer)
            Clears the cache of exported values, causing new 
             instances to be created.
        """
        pass

    def Single(self, predicate):
        """ Single[T](self: Composer, predicate: Func[T, bool]) -> T """
        pass

    Instance = None


class ConcurrentSet(object, ISet[T], ICollection[T], IEnumerable[T], IEnumerable):
    """ ConcurrentSet[T]() """
    def Add(self, item):
        """
        Add(self: ConcurrentSet[T], item: T)
            Adds an item to the 
             System.Collections.Generic.ICollection.
        
        
            item: The object to add to the 
             System.Collections.Generic.ICollection.
        """
        pass

    def Clear(self):
        """
        Clear(self: ConcurrentSet[T])
            Removes all items from the 
             System.Collections.Generic.ICollection.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: ConcurrentSet[T], item: T) -> bool
        
            Determines whether the 
             System.Collections.Generic.ICollection contains a 
             specific value.
        
        
            item: The object to locate in the 
             System.Collections.Generic.ICollection.
        
            Returns: true if item is found in the 
             System.Collections.Generic.ICollection; 
             otherwise, false.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: ConcurrentSet[T], array: Array[T], arrayIndex: int) """
        pass

    def ExceptWith(self, other):
        """
        ExceptWith(self: ConcurrentSet[T], other: IEnumerable[T])
            Removes all elements in the specified collection 
             from the current set.
        
        
            other: The collection of items to remove from the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ConcurrentSet[T]) -> IEnumerator[T]
        
            Returns an enumerator that iterates through the 
             collection.
        
            Returns: A System.Collections.Generic.IEnumerator that can 
             be used to iterate through the collection.
        """
        pass

    def IntersectWith(self, other):
        """
        IntersectWith(self: ConcurrentSet[T], other: IEnumerable[T])
            Modifies the current set so that it contains only 
             elements that are also in a specified collection.
        
        
            other: The collection to compare to the current set.
        """
        pass

    def IsProperSubsetOf(self, other):
        """
        IsProperSubsetOf(self: ConcurrentSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current set is a proper 
             (strict) subset of a specified collection.
        
        
            other: The collection to compare to the current set.
            Returns: true if the current set is a proper subset of 
             other; otherwise, false.
        """
        pass

    def IsProperSupersetOf(self, other):
        """
        IsProperSupersetOf(self: ConcurrentSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current set is a proper 
             (strict) superset of a specified collection.
        
        
            other: The collection to compare to the current set.
            Returns: true if the current set is a proper superset of 
             other; otherwise, false.
        """
        pass

    def IsSubsetOf(self, other):
        """
        IsSubsetOf(self: ConcurrentSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether a set is a subset of a 
             specified collection.
        
        
            other: The collection to compare to the current set.
            Returns: true if the current set is a subset of other; 
             otherwise, false.
        """
        pass

    def IsSupersetOf(self, other):
        """
        IsSupersetOf(self: ConcurrentSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current set is a superset 
             of a specified collection.
        
        
            other: The collection to compare to the current set.
            Returns: true if the current set is a superset of other; 
             otherwise, false.
        """
        pass

    def Overlaps(self, other):
        """
        Overlaps(self: ConcurrentSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current set overlaps with 
             the specified collection.
        
        
            other: The collection to compare to the current set.
            Returns: true if the current set and other share at least 
             one common element; otherwise, false.
        """
        pass

    def Remove(self, item):
        """
        Remove(self: ConcurrentSet[T], item: T) -> bool
        
            Removes the first occurrence of a specific object 
             from the System.Collections.Generic.ICollection.
        
        
            item: The object to remove from the 
             System.Collections.Generic.ICollection.
        
            Returns: true if item was successfully removed from the 
             System.Collections.Generic.ICollection; 
             otherwise, false. This method also returns false 
             if item is not found in the original 
             System.Collections.Generic.ICollection.
        """
        pass

    def SetEquals(self, other):
        """
        SetEquals(self: ConcurrentSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current set and the 
             specified collection contain the same elements.
        
        
            other: The collection to compare to the current set.
            Returns: true if the current set is equal to other; 
             otherwise, false.
        """
        pass

    def SymmetricExceptWith(self, other):
        """
        SymmetricExceptWith(self: ConcurrentSet[T], other: IEnumerable[T])
            Modifies the current set so that it contains only 
             elements that are present either in the current 
             set or in the specified collection, but not both.
        
        
            other: The collection to compare to the current set.
        """
        pass

    def UnionWith(self, other):
        """
        UnionWith(self: ConcurrentSet[T], other: IEnumerable[T])
            Modifies the current set so that it contains all 
             elements that are present in either the current 
             set or the specified collection.
        
        
            other: The collection to compare to the current set.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[T], item: T) -> bool
        
            Determines whether the 
             System.Collections.Generic.ICollection contains a 
             specific value.
        
        
            item: The object to locate in the 
             System.Collections.Generic.ICollection.
        
            Returns: true if item is found in the 
             System.Collections.Generic.ICollection; 
             otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained in the System.Collections.Generic.ICollection.

Get: Count(self: ConcurrentSet[T]) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Collections.Generic.ICollection is read-only.

Get: IsReadOnly(self: ConcurrentSet[T]) -> bool

"""



class DateTimeJsonConverter(IsoDateTimeConverter):
    """
    Provides a json converter that allows defining the date time format used
    
    DateTimeJsonConverter(format: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, format):
        """ __new__(cls: type, format: str) """
        pass


class DisposableExtensions(object):
    """ Provides extensions methods for System.IDisposable """
    @staticmethod
    def DisposeSafely(disposable, errorHandler=None):
        """
        DisposeSafely(disposable: IDisposable) -> bool
        
            Calls System.IDisposable.Dispose within a 
             try/catch and logs any errors.
        
        
            disposable: The System.IDisposable to be disposed
            Returns: True if the object was successfully disposed, 
             false if an error was thrown
        
        DisposeSafely(disposable: IDisposable, errorHandler: Action[Exception]) -> bool
        """
        pass

    __all__ = [
        'DisposeSafely',
    ]


class DoubleUnixSecondsDateTimeJsonConverter(TypeChangeJsonConverter[Nullable[DateTime], Nullable[float]]):
    """
    Defines a Newtonsoft.Json.JsonConverter that serializes System.DateTime use the number of whole and fractional seconds since unix epoch
    
    DoubleUnixSecondsDateTimeJsonConverter()
    """
    def CanConvert(self, objectType):
        """
        CanConvert(self: DoubleUnixSecondsDateTimeJsonConverter, objectType: Type) -> bool
        
            Determines whether this instance can convert the 
             specified object type.
        
        
            objectType: Type of the object.
            Returns: true if this instance can convert the specified 
             object type; otherwise, false.
        """
        pass

    PopulateProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True will populate TResult object returned by QuantConnect.Util.TypeChangeJsonConverter with json properties

"""



class EnumeratorExtensions(object):
    """ Provides convenience of linq extension methods for System.Collections.Generic.IEnumerator types """
    @staticmethod
    def Select(enumerator, selector):
        """ Select[(T, TResult)](enumerator: IEnumerator[T], selector: Func[T, TResult]) -> IEnumerator[TResult] """
        pass

    @staticmethod
    def SelectMany(enumerator, selector):
        """ SelectMany[(T, TResult)](enumerator: IEnumerator[T], selector: Func[T, IEnumerator[TResult]]) -> IEnumerator[TResult] """
        pass

    @staticmethod
    def Where(enumerator, predicate):
        """ Where[T](enumerator: IEnumerator[T], predicate: Func[T, bool]) -> IEnumerator[T] """
        pass

    __all__ = [
        'Select',
        'SelectMany',
        'Where',
    ]


class ExpressionBuilder(object):
    """ Provides methods for constructing expressions at runtime """
    @staticmethod
    def AsEnumerable(expression):
        """
        AsEnumerable(expression: Expression) -> IEnumerable[Expression]
        
            Converts the specified expression into an 
             enumerable of expressions by walking the 
             expression tree
        
        
            expression: The expression to enumerate
            Returns: An enumerable containing all expressions in the 
             input expression
        """
        pass

    @staticmethod
    def MakePropertyOrFieldSelector(*__args):
        """
        MakePropertyOrFieldSelector(type: Type, propertyOrField: str) -> LambdaExpression
        
            Constructs a selector of the form: x => 
             x.propertyOrField where x is an instance of 
             'type'
        
        
            type: The type of the parameter in the expression
            propertyOrField: The name of the property or field to bind to
            Returns: A new lambda expression that represents accessing 
             the property or field on 'type'
        
        MakePropertyOrFieldSelector[(T, TProperty)](propertyOrField: str) -> Expression[Func[T, TProperty]]
        """
        pass

    @staticmethod
    def OfType(expression):
        """ OfType[T](expression: Expression) -> IEnumerable[T] """
        pass

    __all__ = [
        'AsEnumerable',
        'MakePropertyOrFieldSelector',
        'OfType',
    ]


class FixedSizeHashQueue(object, IEnumerable[T], IEnumerable):
    """ FixedSizeHashQueue[T](size: int) """
    def Add(self, item):
        """
        Add(self: FixedSizeHashQueue[T], item: T) -> bool
        
            Returns true if the item was added and didn't 
             already exists
        """
        pass

    def Contains(self, item):
        """
        Contains(self: FixedSizeHashQueue[T], item: T) -> bool
        
            Returns true if the specified item exists in the 
             collection
        """
        pass

    def Dequeue(self):
        """
        Dequeue(self: FixedSizeHashQueue[T]) -> T
        
            Dequeues and returns the next item in the queue
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: FixedSizeHashQueue[T]) -> IEnumerator[T]
        
            Returns an enumerator that iterates through the 
             collection.
        
            Returns: A System.Collections.Generic.IEnumerator that can 
             be used to iterate through the collection.
        """
        pass

    def TryPeek(self, item):
        """ TryPeek(self: FixedSizeHashQueue[T]) -> (bool, T) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
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


class FixedSizeQueue(Queue[T], IEnumerable[T], IEnumerable, ICollection, IReadOnlyCollection[T]):
    """ FixedSizeQueue[T](limit: int) """
    def Enqueue(self, item):
        """
        Enqueue(self: FixedSizeQueue[T], item: T)
            Enqueue a new item int the generic fixed length 
             queue:
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, limit):
        """ __new__(cls: type, limit: int) """
        pass

    Limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Max Length

Get: Limit(self: FixedSizeQueue[T]) -> int

Set: Limit(self: FixedSizeQueue[T]) = value
"""



class FuncTextWriter(TextWriter, IDisposable):
    """
    Provides an implementation of System.IO.TextWriter that redirects Write(string) and WriteLine(string)
    
    FuncTextWriter(writer: Action[str])
    """
    def Dispose(self):
        """
        Dispose(self: TextWriter, disposing: bool)
            Releases the unmanaged resources used by the 
             System.IO.TextWriter and optionally releases the 
             managed resources.
        
        
            disposing: true to release both managed and unmanaged 
             resources; false to release only unmanaged 
             resources.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current 
             System.MarshalByRefObject object.
        
        
            cloneIdentity: false to delete the current 
             System.MarshalByRefObject object's identity, 
             which will cause the object to be assigned a new 
             identity when it is marshaled across a remoting 
             boundary. A value of false is usually 
             appropriate. true to copy the current 
             System.MarshalByRefObject object's identity to 
             its clone, which will cause remoting client calls 
             to be routed to the remote server object.
        
            Returns: A shallow copy of the current 
             System.MarshalByRefObject object.
        
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current 
             System.Object.
        
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: FuncTextWriter, value: str)
            Writes the string value using the delegate 
             provided at construction
        
        
            value: The string value to be written
        """
        pass

    def WriteLine(self, *__args):
        """
        WriteLine(self: FuncTextWriter, value: str)
            Writes the string value using the delegate 
             provided at construction
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
    def __new__(self, writer):
        """ __new__(cls: type, writer: Action[str]) """
        pass

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Encoding(self: FuncTextWriter) -> Encoding

"""


    CoreNewLine = None


class IReadOnlyRef:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current value this reference points to

Get: Value(self: IReadOnlyRef[T]) -> T

"""



class JsonRoundingConverter(JsonConverter):
    """
    Helper Newtonsoft.Json.JsonConverter that will round decimal and double types,
                to QuantConnect.Util.JsonRoundingConverter.FractionalDigits fractional digits
    
    JsonRoundingConverter()
    """
    def CanConvert(self, objectType):
        """
        CanConvert(self: JsonRoundingConverter, objectType: Type) -> bool
        
            Determines whether this instance can convert the 
             specified object type.
        
        
            objectType: Type of the object.
            Returns: True if this instance can convert the specified 
             object type
        """
        pass

    def ReadJson(self, reader, objectType, existingValue, serializer):
        """
        ReadJson(self: JsonRoundingConverter, reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object
        
            Not implemented, will throw 
             System.NotImplementedException
        
        
            reader: The Newtonsoft.Json.JsonReader to read from.
            objectType: Type of the object.
            existingValue: The existing value of object being read.
            serializer: The calling serializer.
        """
        pass

    def WriteJson(self, writer, value, serializer):
        """
        WriteJson(self: JsonRoundingConverter, writer: JsonWriter, value: object, serializer: JsonSerializer)
            Writes the JSON representation of the object.
        
            writer: The Newtonsoft.Json.JsonWriter to write to.
            value: The value.
            serializer: The calling serializer.
        """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Will always return false.
            Gets a value indicating whether this Newtonsoft.Json.JsonConverter can read JSON.

Get: CanRead(self: JsonRoundingConverter) -> bool

"""


    FractionalDigits = 4


class LeanData(object):
    """ Provides methods for generating lean data file content """
    @staticmethod
    def GenerateLine(data, *__args):
        """
        GenerateLine(data: IBaseData, resolution: Resolution, exchangeTimeZone: DateTimeZone, dataTimeZone: DateTimeZone) -> str
        
            Converts the specified base data instance into a 
             lean data file csv line.
                    This method 
             takes into account the fake that base data 
             instances typically
                    are time stamped 
             in the exchange time zone, but need to be written 
             to disk
                    in the data time zone.
        
        GenerateLine(data: IBaseData, securityType: SecurityType, resolution: Resolution) -> str
        
            Converts the specified base data instance into a 
             lean data file csv line
        """
        pass

    @staticmethod
    def GenerateRelativeFactorFilePath(symbol):
        """
        GenerateRelativeFactorFilePath(symbol: Symbol) -> str
        
            Generates relative factor file paths for equities
        """
        pass

    @staticmethod
    def GenerateRelativeZipFileDirectory(symbol, resolution):
        """
        GenerateRelativeZipFileDirectory(symbol: Symbol, resolution: Resolution) -> str
        
            Generates the relative zip directory for the 
             specified symbol/resolution
        """
        pass

    @staticmethod
    def GenerateRelativeZipFilePath(symbol, *__args):
        """
        GenerateRelativeZipFilePath(symbol: Symbol, date: DateTime, resolution: Resolution, tickType: TickType) -> str
        
            Generates the relative zip file path rooted in 
             the /Data directory
        
        GenerateRelativeZipFilePath(symbol: str, securityType: SecurityType, market: str, date: DateTime, resolution: Resolution) -> str
        
            Generates the relative zip file path rooted in 
             the /Data directory
        """
        pass

    @staticmethod
    def GenerateZipEntryName(symbol, date, resolution, tickType):
        """
        GenerateZipEntryName(symbol: Symbol, date: DateTime, resolution: Resolution, tickType: TickType) -> str
        
            Generate's the zip entry name to hold the 
             specified data.
        """
        pass

    @staticmethod
    def GenerateZipFileName(symbol, *__args):
        """
        GenerateZipFileName(symbol: Symbol, date: DateTime, resolution: Resolution, tickType: TickType) -> str
        
            Generates the zip file name for the specified 
             date of data.
        
        GenerateZipFileName(symbol: str, securityType: SecurityType, date: DateTime, resolution: Resolution, tickType: Nullable[TickType]) -> str
        """
        pass

    @staticmethod
    def GenerateZipFilePath(dataDirectory, symbol, *__args):
        """
        GenerateZipFilePath(dataDirectory: str, symbol: Symbol, date: DateTime, resolution: Resolution, tickType: TickType) -> str
        
            Generates the full zip file path rooted in the 
             dataDirectory
        
        GenerateZipFilePath(dataDirectory: str, symbol: str, securityType: SecurityType, market: str, date: DateTime, resolution: Resolution) -> str
        
            Generates the full zip file path rooted in the 
             dataDirectory
        """
        pass

    @staticmethod
    def GetCommonTickType(securityType):
        """
        GetCommonTickType(securityType: SecurityType) -> TickType
        
            Gets the tick type most commonly associated with 
             the specified security type
        
        
            securityType: The security type
            Returns: The most common tick type for the specified 
             security type
        """
        pass

    @staticmethod
    def GetCommonTickTypeForCommonDataTypes(type, securityType):
        """
        GetCommonTickTypeForCommonDataTypes(type: Type, securityType: SecurityType) -> TickType
        
            Get the QuantConnect.TickType for common Lean 
             data types.
                    If not a Lean common 
             data type, return a TickType of Trade.
        
        
            type: A Type used to determine the TickType
            securityType: The SecurityType used to determine the TickType
            Returns: A TickType corresponding to the type
        """
        pass

    @staticmethod
    def GetDataType(resolution, tickType):
        """
        GetDataType(resolution: Resolution, tickType: TickType) -> Type
        
            Gets the data type required for the specified 
             combination of resolution and tick type
        
        
            resolution: The resolution, if Tick, the Type returned is 
             always Tick
        
            tickType: The QuantConnect.TickType that primarily dictates 
             the type returned
        
            Returns: The Type used to create a subscription
        """
        pass

    @staticmethod
    def IsCommonLeanDataType(baseDataType):
        """
        IsCommonLeanDataType(baseDataType: Type) -> bool
        
            Determines if the Type is a 'common' type used 
             throughout lean
                    This method is 
             helpful in creating 
             QuantConnect.Data.SubscriptionDataConfig
        
        
            baseDataType: The Type to check
            Returns: A bool indicating whether the type is of type 
             QuantConnect.Data.Market.TradeBarQuantConnect.Data
             .Market.QuoteBar or 
             QuantConnect.Data.Market.OpenInterest
        """
        pass

    @staticmethod
    def ParseDataSecurityType(securityType):
        """
        ParseDataSecurityType(securityType: str) -> SecurityType
        
            Matches a data path security type with the 
             QuantConnect.SecurityType
        
        
            securityType: The data path security type
            Returns: The matching security type for the given data path
        """
        pass

    @staticmethod
    def ReadSymbolFromZipEntry(symbol, resolution, zipEntryName):
        """
        ReadSymbolFromZipEntry(symbol: Symbol, resolution: Resolution, zipEntryName: str) -> Symbol
        
            Creates a symbol from the specified zip entry name
        
            symbol: The root symbol of the output symbol
            resolution: The resolution of the data source producing the 
             zip entry name
        
            zipEntryName: The zip entry name to be parsed
            Returns: A new symbol representing the zip entry name
        """
        pass

    @staticmethod
    def TryParsePath(fileName, symbol, date, resolution):
        """
        TryParsePath(fileName: str) -> (bool, Symbol, DateTime, Resolution)
        
            Parses file name into a 
             QuantConnect.Securities.Security and DateTime
        
        
            fileName: File name to be parsed
        """
        pass

    SecurityTypeAsDataPath = None
    __all__ = [
        'GenerateLine',
        'GenerateRelativeFactorFilePath',
        'GenerateRelativeZipFileDirectory',
        'GenerateRelativeZipFilePath',
        'GenerateZipEntryName',
        'GenerateZipFileName',
        'GenerateZipFilePath',
        'GetCommonTickType',
        'GetCommonTickTypeForCommonDataTypes',
        'GetDataType',
        'IsCommonLeanDataType',
        'ParseDataSecurityType',
        'ReadSymbolFromZipEntry',
        'TryParsePath',
    ]


class LeanDataPathComponents(object):
    """
    Type representing the various pieces of information emebedded into a lean data file path
    
    LeanDataPathComponents(securityType: SecurityType, market: str, resolution: Resolution, symbol: Symbol, filename: str, date: DateTime, tickType: TickType)
    """
    @staticmethod
    def Parse(path):
        """
        Parse(path: str) -> LeanDataPathComponents
        
            Parses the specified path into a new instance of 
             the QuantConnect.Util.LeanDataPathComponents 
             class
        
        
            path: The path to be parsed
            Returns: A new instance of the 
             QuantConnect.Util.LeanDataPathComponents class 
             representing the specified path
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, securityType, market, resolution, symbol, filename, date, tickType):
        """ __new__(cls: type, securityType: SecurityType, market: str, resolution: Resolution, symbol: Symbol, filename: str, date: DateTime, tickType: TickType) """
        pass

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the date component from the file name

Get: Date(self: LeanDataPathComponents) -> DateTime

"""

    Filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file name, not inluding directory information

Get: Filename(self: LeanDataPathComponents) -> str

"""

    Market = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the market from the path

Get: Market(self: LeanDataPathComponents) -> str

"""

    Resolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the resolution from the path

Get: Resolution(self: LeanDataPathComponents) -> Resolution

"""

    SecurityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security type from the path

Get: SecurityType(self: LeanDataPathComponents) -> SecurityType

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the symbol object implied by the path. For options, or any
            multi-entry zip file, this should be the canonical symbol

Get: Symbol(self: LeanDataPathComponents) -> Symbol

"""

    TickType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the tick type from the file name

Get: TickType(self: LeanDataPathComponents) -> TickType

"""



class LinqExtensions(object):
    """ Provides more extension methods for the enumerable types """
    @staticmethod
    def AreDifferent(left, right):
        """ AreDifferent[T](left: ISet[T], right: ISet[T]) -> bool """
        pass

    @staticmethod
    def AsEnumerable(enumerator):
        """ AsEnumerable[T](enumerator: IEnumerator[T]) -> IEnumerable[T] """
        pass

    @staticmethod
    def BinarySearch(list, value, comparer=None):
        """
        BinarySearch[(TItem, TSearch)](list: IList[TItem], value: TSearch, comparer: Func[TSearch, TItem, int]) -> int
        BinarySearch[TItem](list: IList[TItem], value: TItem) -> int
        BinarySearch[TItem](list: IList[TItem], value: TItem, comparer: IComparer[TItem]) -> int
        """
        pass

    @staticmethod
    def DefaultIfEmpty(enumerable, selector, defaultValue):
        """ DefaultIfEmpty[(T, TResult)](enumerable: IEnumerable[T], selector: Func[T, TResult], defaultValue: TResult) -> IEnumerable[TResult] """
        pass

    @staticmethod
    def DistinctBy(enumerable, selector):
        """ DistinctBy[(T, TPropery)](enumerable: IEnumerable[T], selector: Func[T, TPropery]) -> IEnumerable[T] """
        pass

    @staticmethod
    def Except(enumerable, set):
        """ Except[T](enumerable: IEnumerable[T], set: ISet[T]) -> IEnumerable[T] """
        pass

    @staticmethod
    def GetValueOrDefault(dictionary, key, defaultValue):
        """ GetValueOrDefault[(K, V)](dictionary: IDictionary[K, V], key: K, defaultValue: V) -> V """
        pass

    @staticmethod
    def GroupAdjacentBy(enumerable, grouper):
        """ GroupAdjacentBy[T](enumerable: IEnumerable[T], grouper: Func[T, T, bool]) -> IEnumerable[IEnumerable[T]] """
        pass

    @staticmethod
    def IsNullOrEmpty(enumerable):
        """ IsNullOrEmpty[T](enumerable: IEnumerable[T]) -> bool """
        pass

    @staticmethod
    def Median(*__args):
        """
        Median[T](enumerable: IEnumerable[T]) -> T
        Median[(T, TProperty)](collection: IEnumerable[T], selector: Func[T, TProperty]) -> TProperty
        """
        pass

    @staticmethod
    def Memoize(enumerable):
        """ Memoize[T](enumerable: IEnumerable[T]) -> IEnumerable[T] """
        pass

    @staticmethod
    def Range(start, end, incrementer, includeEndPoint):
        """ Range[T](start: T, end: T, incrementer: Func[T, T], includeEndPoint: bool) -> IEnumerable[T] """
        pass

    @staticmethod
    def ToDictionary(*__args):
        """
        ToDictionary[(K, V)](lookup: ILookup[K, V]) -> Dictionary[K, List[V]]
        ToDictionary[(K, V)](enumerable: IEnumerable[KeyValuePair[K, V]]) -> Dictionary[K, V]
        """
        pass

    @staticmethod
    def ToHashSet(enumerable, selector=None):
        """
        ToHashSet[T](enumerable: IEnumerable[T]) -> HashSet[T]
        ToHashSet[(T, TResult)](enumerable: IEnumerable[T], selector: Func[T, TResult]) -> HashSet[TResult]
        """
        pass

    @staticmethod
    def ToList(enumerable, selector):
        """ ToList[(T, TResult)](enumerable: IEnumerable[T], selector: Func[T, TResult]) -> List[TResult] """
        pass

    @staticmethod
    def ToReadOnlyDictionary(enumerable):
        """ ToReadOnlyDictionary[(K, V)](enumerable: IEnumerable[KeyValuePair[K, V]]) -> IReadOnlyDictionary[K, V] """
        pass

    __all__ = [
        'AreDifferent',
        'AsEnumerable',
        'BinarySearch',
        'DefaultIfEmpty',
        'DistinctBy',
        'Except',
        'GetValueOrDefault',
        'GroupAdjacentBy',
        'IsNullOrEmpty',
        'Median',
        'Memoize',
        'Range',
        'ToDictionary',
        'ToHashSet',
        'ToList',
        'ToReadOnlyDictionary',
    ]


class ListComparer(object, IEqualityComparer[List[T]]):
    """ ListComparer[T]() """
    def Equals(self, *__args):
        """
        Equals(self: ListComparer[T], x: List[T], y: List[T]) -> bool
        
            Determines whether the specified objects are 
             equal.
        
            Returns: true if the specified objects are equal; 
             otherwise, false.
        """
        pass

    def GetHashCode(self, obj=None):
        """
        GetHashCode(self: ListComparer[T], obj: List[T]) -> int
        
            Returns a hash code for the specified object.
            Returns: A hash code for the specified object created from 
             combining the hash
                    code of all the 
             elements in the collection.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class MarketHoursDatabaseJsonConverter(TypeChangeJsonConverter[MarketHoursDatabase, MarketHoursDatabaseJson]):
    """
    Provides json conversion for the QuantConnect.Securities.MarketHoursDatabase class
    
    MarketHoursDatabaseJsonConverter()
    """
    PopulateProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True will populate TResult object returned by QuantConnect.Util.TypeChangeJsonConverter with json properties

"""


    MarketHoursDatabaseEntryJson = None
    MarketHoursDatabaseJson = None


class MemoizingEnumerable(object, IEnumerable[T], IEnumerable):
    """
    MemoizingEnumerable[T](enumerable: IEnumerable[T])
    MemoizingEnumerable[T](enumerator: IEnumerator[T])
    """
    def GetEnumerator(self):
        """
        GetEnumerator(self: MemoizingEnumerable[T]) -> IEnumerator[T]
        
            Returns an enumerator that iterates through the 
             collection.
        
            Returns: A System.Collections.Generic.IEnumerator that can 
             be used to iterate through the collection.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, enumerable: IEnumerable[T])
        __new__(cls: type, enumerator: IEnumerator[T])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class NullStringValueConverter(JsonConverter):
    """ NullStringValueConverter[T]() """
    def CanConvert(self, objectType):
        """
        CanConvert(self: NullStringValueConverter[T], objectType: Type) -> bool
        
            Determines whether this instance can convert the 
             specified object type.
        
        
            objectType: Type of the object.
            Returns: true if this instance can convert the specified 
             object type; otherwise, false.
        """
        pass

    def ReadJson(self, reader, objectType, existingValue, serializer):
        """
        ReadJson(self: NullStringValueConverter[T], reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object
        
            Reads the JSON representation of the object.
        
            reader: The Newtonsoft.Json.JsonReader to read from.
            objectType: Type of the object.
            existingValue: The existing value of object being read.
            serializer: The calling serializer.
            Returns: The object value.
        """
        pass

    def WriteJson(self, writer, value, serializer):
        """
        WriteJson(self: NullStringValueConverter[T], writer: JsonWriter, value: object, serializer: JsonSerializer)
            Writes the JSON representation of the object.
        
            writer: The Newtonsoft.Json.JsonWriter to write to.
            value: The value.
            serializer: The calling serializer.
        """
        pass


class ObjectActivator(object):
    """ Provides methods for creating new instances of objects """
    @staticmethod
    def AddActivator(key, value):
        """ AddActivator(key: Type, value: Func[Array[object], object]) """
        pass

    @staticmethod
    def Clone(instanceToClone):
        """
        Clone(instanceToClone: object) -> object
        
            Clones the specified instance using reflection
        
            instanceToClone: The instance to be cloned
            Returns: A field/property wise, non-recursive clone of the 
             instance
        
        Clone[T](instanceToClone: T) -> T
        """
        pass

    @staticmethod
    def GetActivator(dataType):
        """
        GetActivator(dataType: Type) -> Func[Array[object], object]
        
            Fast Object Creator from Generic Type:
                  
               Modified from 
             http://rogeralsing.com/2008/02/28/linq-expressions
             -creating-objects/
        
        
            dataType: Type of the object we wish to create
            Returns: Method to return an instance of object
        """
        pass

    @staticmethod
    def ResetActivators():
        """
        ResetActivators()
            Reset the object activators
        """
        pass

    __all__ = [
        'AddActivator',
        'Clone',
        'GetActivator',
        'ResetActivators',
    ]


class PythonUtil(object):
    """
    Collection of utils for python objects processing
    
    PythonUtil()
    """
    @staticmethod
    def PythonExceptionStackParser(value):
        """
        PythonExceptionStackParser(value: str) -> str
        
            Parsers Python.Runtime.PythonException.StackTrace 
             into a readable message
        
        
            value: String with the stacktrace information
            Returns: String with relevant part of the stacktrace
        """
        pass

    @staticmethod
    def ToAction(pyObject):
        """
        ToAction[T1](pyObject: PyObject) -> Action[T1]
        ToAction[(T1, T2)](pyObject: PyObject) -> Action[T1, T2]
        """
        pass

    @staticmethod
    def ToCoarseFundamentalSelector(pyObject):
        """
        ToCoarseFundamentalSelector(pyObject: PyObject) -> Func[IEnumerable[CoarseFundamental], IEnumerable[Symbol]]
        
            Encapsulates a python method in coarse 
             fundamental universe selector.
        
        
            pyObject: The python method
            Returns: A System.Func (parameter is 
             System.Collections.Generic.IEnumerable, return 
             value is System.Collections.Generic.IEnumerable) 
             that encapsulates the python method
        """
        pass

    @staticmethod
    def ToFineFundamentalSelector(pyObject):
        """
        ToFineFundamentalSelector(pyObject: PyObject) -> Func[IEnumerable[FineFundamental], IEnumerable[Symbol]]
        
            Encapsulates a python method in fine fundamental 
             universe selector.
        
        
            pyObject: The python method
            Returns: A System.Func (parameter is 
             System.Collections.Generic.IEnumerable, return 
             value is System.Collections.Generic.IEnumerable) 
             that encapsulates the python method
        """
        pass

    @staticmethod
    def ToFunc(pyObject):
        """ ToFunc[(T1, T2)](pyObject: PyObject) -> Func[T1, T2] """
        pass


class RateGate(object, IDisposable):
    """
    Used to control the rate of some occurrence per unit of time.
    
    RateGate(occurrences: int, timeUnit: TimeSpan)
    """
    def Dispose(self):
        """
        Dispose(self: RateGate)
            Releases unmanaged resources held by an instance 
             of this class.
        """
        pass

    def WaitToProceed(self, *__args):
        """
        WaitToProceed(self: RateGate, millisecondsTimeout: int) -> bool
        
            Blocks the current thread until allowed to 
             proceed or until the
                    specified 
             timeout elapses.
        
        
            millisecondsTimeout: Number of milliseconds to wait, or -1 to wait 
             indefinitely.
        
            Returns: true if the thread is allowed to proceed, or 
             false if timed out
        
        WaitToProceed(self: RateGate, timeout: TimeSpan) -> bool
        
            Blocks the current thread until allowed to 
             proceed or until the
                    specified 
             timeout elapses.
        
            Returns: true if the thread is allowed to proceed, or 
             false if timed out
        
        WaitToProceed(self: RateGate)
            Blocks the current thread indefinitely until 
             allowed to proceed.
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
    def __new__(self, occurrences, timeUnit):
        """ __new__(cls: type, occurrences: int, timeUnit: TimeSpan) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsRateLimited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flag indicating we are currently being rate limited

Get: IsRateLimited(self: RateGate) -> bool

"""

    Occurrences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of occurrences allowed per unit of time.

Get: Occurrences(self: RateGate) -> int

"""

    TimeUnitMilliseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of the time unit, in milliseconds.

Get: TimeUnitMilliseconds(self: RateGate) -> int

"""



class ReaderWriterLockSlimExtensions(object):
    """ Provides extension methods to make working with the System.Threading.ReaderWriterLockSlim class easier """
    @staticmethod
    def Read(readerWriterLockSlim):
        """
        Read(readerWriterLockSlim: ReaderWriterLockSlim) -> IDisposable
        
            Opens the read lock
        
            readerWriterLockSlim: The lock to open for read
            Returns: A disposable reference which will release the 
             lock upon disposal
        """
        pass

    @staticmethod
    def Write(readerWriterLockSlim):
        """
        Write(readerWriterLockSlim: ReaderWriterLockSlim) -> IDisposable
        
            Opens the write lock
        
            readerWriterLockSlim: The lock to open for write
            Returns: A disposale reference which will release thelock 
             upon disposal
        """
        pass

    __all__ = [
        'Read',
        'Write',
    ]


class ReferenceWrapper(object):
    """ ReferenceWrapper[T](value: T) """
    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: T) """
        pass

    Value = None


class SecurityExtensions(object):
    """
    Provides useful infrastructure methods to the QuantConnect.Securities.Security class.
                These are added in this way to avoid mudding the class's public API
    """
    @staticmethod
    def IsInternalFeed(security):
        """
        IsInternalFeed(security: Security) -> bool
        
            Determines if all subscriptions for the security 
             are internal feeds
        """
        pass

    __all__ = [
        'IsInternalFeed',
    ]


class SecurityIdentifierJsonConverter(TypeChangeJsonConverter[SecurityIdentifier, str]):
    """
    A Newtonsoft.Json.JsonConverter implementation that serializes a QuantConnect.SecurityIdentifier as a string
    
    SecurityIdentifierJsonConverter()
    """
    PopulateProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True will populate TResult object returned by QuantConnect.Util.TypeChangeJsonConverter with json properties

"""



class SeriesJsonConverter(JsonConverter):
    """
    Json Converter for Series which handles special Pie Series serialization case
    
    SeriesJsonConverter()
    """
    def CanConvert(self, objectType):
        """ CanConvert(self: SeriesJsonConverter, objectType: Type) -> bool """
        pass

    def ReadJson(self, reader, objectType, existingValue, serializer):
        """ ReadJson(self: SeriesJsonConverter, reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object """
        pass

    def WriteJson(self, writer, value, serializer):
        """ WriteJson(self: SeriesJsonConverter, writer: JsonWriter, value: object, serializer: JsonSerializer) """
        pass

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This converter wont be used to read JSON. Will throw exception if manually called.

Get: CanRead(self: SeriesJsonConverter) -> bool

"""



class SingleValueListConverter(JsonConverter):
    """ SingleValueListConverter[T]() """
    def CanConvert(self, objectType):
        """
        CanConvert(self: SingleValueListConverter[T], objectType: Type) -> bool
        
            Determines whether this instance can convert the 
             specified object type.
        
        
            objectType: Type of the object.
            Returns: true if this instance can convert the specified 
             object type; otherwise, false.
        """
        pass

    def ReadJson(self, reader, objectType, existingValue, serializer):
        """
        ReadJson(self: SingleValueListConverter[T], reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object
        
            Reads the JSON representation of the object. If 
             the JSON represents a singular instance, it will 
             be returned
                    in a list.
        
        
            reader: The Newtonsoft.Json.JsonReader to read from.
            objectType: Type of the object.
            existingValue: The existing value of object being read.
            serializer: The calling serializer.
            Returns: The object value
        """
        pass

    def WriteJson(self, writer, value, serializer):
        """
        WriteJson(self: SingleValueListConverter[T], writer: JsonWriter, value: object, serializer: JsonSerializer)
            Writes the JSON representation of the object. If 
             the instance is not a list then it will
                 
                be wrapped in a list
        
        
            writer: The Newtonsoft.Json.JsonWriter to write to.
            value: The value.
            serializer: The calling serializer.
        """
        pass


class StreamReaderEnumerable(object, IEnumerable[str], IEnumerable, IDisposable):
    """
    Converts a System.IO.StreamReader into an enumerable of string
    
    StreamReaderEnumerable(stream: Stream, *disposables: Array[IDisposable])
    StreamReaderEnumerable(reader: StreamReader, *disposables: Array[IDisposable])
    """
    def Dispose(self):
        """
        Dispose(self: StreamReaderEnumerable)
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: StreamReaderEnumerable) -> IEnumerator[str]
        
            Returns an enumerator that iterates through the 
             collection.
        
            Returns: A System.Collections.Generic.IEnumerator that can 
             be used to iterate through the collection.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[str](enumerable: IEnumerable[str], value: str) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, stream: Stream, *disposables: Array[IDisposable])
        __new__(cls: type, reader: StreamReader, *disposables: Array[IDisposable])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class StreamReaderExtensions(object):
    """ Extension methods to fetch data from a System.IO.StreamReader instance """
    @staticmethod
    def GetDateTime(stream, format, delimiter):
        """
        GetDateTime(stream: StreamReader, format: str, delimiter: Char) -> DateTime
        
            Gets a date time instance from a stream reader
        
            stream: The data stream
            format: The format in which the date time is
            delimiter: The data delimiter character to use, default is 
             ','
        
            Returns: The date time instance read
        """
        pass

    @staticmethod
    def GetDecimal(stream, *__args):
        """
        GetDecimal(stream: StreamReader, delimiter: Char) -> Decimal
        
            Gets a decimal from the provided stream reader
        
            stream: The data stream
            delimiter: The data delimiter character to use, default is 
             ','
        
            Returns: The decimal read from the stream
        GetDecimal(stream: StreamReader, delimiter: Char) -> (Decimal, bool)
        
            Gets a decimal from the provided stream reader
        
            stream: The data stream
            delimiter: The data delimiter character to use, default is 
             ','
        
            Returns: The decimal read from the stream
        """
        pass

    @staticmethod
    def GetInt32(stream, delimiter):
        """
        GetInt32(stream: StreamReader, delimiter: Char) -> int
        
            Gets an integer from a stream reader
        
            stream: The data stream
            delimiter: The data delimiter character to use, default is 
             ','
        
            Returns: The integer instance read
        """
        pass

    @staticmethod
    def GetString(stream, delimiter):
        """
        GetString(stream: StreamReader, delimiter: Char) -> str
        
            Gets a string from a stream reader
        
            stream: The data stream
            delimiter: The data delimiter character to use, default is 
             ','
        
            Returns: The string instance read
        """
        pass

    __all__ = [
        'GetDateTime',
        'GetDecimal',
        'GetInt32',
        'GetString',
    ]


class TypeChangeJsonConverter(JsonConverter):
    # no doc
    def CanConvert(self, objectType):
        """
        CanConvert(self: TypeChangeJsonConverter[T, TResult], objectType: Type) -> bool
        
            Determines whether this instance can convert the 
             specified object type.
        
        
            objectType: Type of the object.
            Returns: true if this instance can convert the specified 
             object type; otherwise, false.
        """
        pass

    def Convert(self, *args): #cannot find CLR method
        """
        Convert(self: TypeChangeJsonConverter[T, TResult], value: T) -> TResult
        
            Convert the input value to a value to be 
             serialzied
        
        
            value: The input value to be converted before 
             serialziation
        
            Returns: A new instance of TResult that is to be serialzied
        Convert(self: TypeChangeJsonConverter[T, TResult], value: TResult) -> T
        
            Converts the input value to be deserialized
        
            value: The deserialized value that needs to be converted 
             to T
        
            Returns: The converted value
        """
        pass

    def Create(self, *args): #cannot find CLR method
        """
        Create(self: TypeChangeJsonConverter[T, TResult], type: Type, token: JToken) -> T
        
            Creates an instance of the un-projected type to 
             be deserialized
        
        
            type: The input object type, this is the data held in 
             the token
        
            token: The input data to be converted into a T
            Returns: A new instance of T that is to be serialized 
             using default rules
        """
        pass

    def ReadJson(self, reader, objectType, existingValue, serializer):
        """
        ReadJson(self: TypeChangeJsonConverter[T, TResult], reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object
        
            Reads the JSON representation of the object.
        
            reader: The Newtonsoft.Json.JsonReader to read from.
            objectType: Type of the object.
            existingValue: The existing value of object being read.
            serializer: The calling serializer.
            Returns: The object value.
        """
        pass

    def WriteJson(self, writer, value, serializer):
        """
        WriteJson(self: TypeChangeJsonConverter[T, TResult], writer: JsonWriter, value: object, serializer: JsonSerializer)
            Writes the JSON representation of the object.
        
            writer: The Newtonsoft.Json.JsonWriter to write to.
            value: The value.
            serializer: The calling serializer.
        """
        pass

    PopulateProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True will populate TResult object returned by QuantConnect.Util.TypeChangeJsonConverter with json properties

"""



class Validate(object):
    """ Provides methods for validating strings following a certain format, such as an email address """
    @staticmethod
    def EmailAddress(emailAddress):
        """
        EmailAddress(emailAddress: str) -> bool
        
            Validates the provided email address
        
            emailAddress: The email address to be validated
            Returns: True if the provided email address is valid
        """
        pass

    RegularExpression = None
    __all__ = [
        'EmailAddress',
        'RegularExpression',
    ]


class VersionHelper(object):
    """ Provides methods for dealing with lean assembly versions """
    @staticmethod
    def CompareVersions(left, right):
        """
        CompareVersions(left: str, right: str) -> int
        
            Compares two versions
            Returns: 1 if the left version is after the right, 0 if 
             they're the same, -1 if the left is before the 
             right
        """
        pass

    @staticmethod
    def IsEqualVersion(version):
        """
        IsEqualVersion(version: str) -> bool
        
            Determines whether or not the specified version 
             is equal to this instance
        
        
            version: The version to compare
            Returns: True if the specified version is equal, false 
             otherwise
        """
        pass

    @staticmethod
    def IsNewerVersion(version):
        """
        IsNewerVersion(version: str) -> bool
        
            Determines whether or not the specified version 
             is newer than this instance
        
        
            version: The version to compare
            Returns: True if the specified version is newer, false 
             otherwise
        """
        pass

    @staticmethod
    def IsNotEqualVersion(version):
        """
        IsNotEqualVersion(version: str) -> bool
        
            Determines whether or not the specified version 
             is not equal to this instance
        
        
            version: The version to compare
            Returns: True if the specified version is not equal, false 
             otherwise
        """
        pass

    @staticmethod
    def IsOlderVersion(version):
        """
        IsOlderVersion(version: str) -> bool
        
            Determines whether or not the specified version 
             is older than this instance
        
        
            version: The version to compare
            Returns: True if the specified version is older, false 
             otherwise
        """
        pass

    __all__ = [
        'CompareVersions',
        'IsEqualVersion',
        'IsNewerVersion',
        'IsNotEqualVersion',
        'IsOlderVersion',
    ]


class WorkerThread(object, IDisposable):
    """
    This worker tread is required to guarantee all python operations are
                executed by the same thread, to enable complete debugging functionality.
                We don't use the main thread, to avoid any chance of blocking the process
    """
    def Add(self, action):
        """
        Add(self: WorkerThread, action: Action)
            Adds a new item of work
        
            action: The work item to add
        """
        pass

    def Dispose(self):
        """
        Dispose(self: WorkerThread)
            Disposes the worker thread.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    FinishedWorkItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Will be set when the worker thread finishes a work item

Get: FinishedWorkItem(self: WorkerThread) -> AutoResetEvent

"""


    Instance = None


class XElementExtensions(object):
    """ Provides extension methods for the XML to LINQ types """
    @staticmethod
    def Get(element, name):
# Error generating skeleton for function Get: Method must be called on a Type for which Type.IsGenericParameter is false.

    __all__ = [
        'Get',
    ]


# variables with complex values

