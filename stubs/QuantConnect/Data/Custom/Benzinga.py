# encoding: utf-8
# module QuantConnect.Data.Custom.Benzinga calls itself Benzinga
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BenzingaNews(IndexedBaseData, IBaseData):
    """
    News data powered by Benzinga - https://docs.benzinga.io/benzinga/newsfeed-v2.html
    
    BenzingaNews()
    """
    def Clone(self, fillForward=None):
        """
        Clone(self: BenzingaNews) -> BaseData
        
            Creates a clone of the instance
            Returns: A clone of the instance
        """
        pass

    def DataTimeZone(self):
        """
        DataTimeZone(self: BenzingaNews) -> DateTimeZone
        
            Set the data time zone to UTC
            Returns: Time zone as UTC
        """
        pass

    def DefaultResolution(self):
        """
        DefaultResolution(self: BenzingaNews) -> Resolution
        
            Sets the default resolution to Second
            Returns: Resolution.Second
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: BenzingaNews, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Gets the source of the index file
        
            config: Configuration object
            date: Date of this source file
            isLiveMode: Is live mode
            Returns: SubscriptionDataSource indicating where data is 
             located and how it's stored
        """
        pass

    def GetSourceForAnIndex(self, config, date, index, isLiveMode):
        """
        GetSourceForAnIndex(self: BenzingaNews, config: SubscriptionDataConfig, date: DateTime, index: str, isLiveMode: bool) -> SubscriptionDataSource
        
            Determines the actual source from an index 
             contained within a ticker folder
        
        
            config: Subscription configuration
            date: Date
            index: File to load data from
            isLiveMode: Is live mode
            Returns: SubscriptionDataSource pointing to the article
        """
        pass

    def IsSparseData(self):
        """
        IsSparseData(self: BenzingaNews) -> bool
        
            Indicates whether the data source is sparse.
            
                     If false, it will disable missing file 
             logging.
        
            Returns: true
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: BenzingaNews, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Creates an instance from a line of JSON 
             containing article information read from the 
             `content` directory
        
        
            config: Subscription configuration
            line: Line of data
            date: Date
            isLiveMode: Is live mode
            Returns: New instance of 
             QuantConnect.Data.Custom.Benzinga.BenzingaNews
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: BenzingaNews) -> bool
        
            Indicates whether the data source can undergo
           
                      rename events/is tied to equities.
        
            Returns: true
        """
        pass

    def SupportedResolutions(self):
        """
        SupportedResolutions(self: BenzingaNews) -> List[Resolution]
        
            Gets a list of all the supported Resolutions
            Returns: All resolutions
        """
        pass

    def ToString(self):
        """
        ToString(self: BenzingaNews) -> str
        
            Converts the instance to string
            Returns: Article title and contents
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Author of the article

Get: Author(self: BenzingaNews) -> str

Set: Author(self: BenzingaNews) = value
"""

    Categories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Categories that relate to the article

Get: Categories(self: BenzingaNews) -> List[str]

Set: Categories(self: BenzingaNews) = value
"""

    Contents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Contents of the article

Get: Contents(self: BenzingaNews) -> str

Set: Contents(self: BenzingaNews) = value
"""

    CreatedAt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Date the article was published

Get: CreatedAt(self: BenzingaNews) -> DateTime

Set: CreatedAt(self: BenzingaNews) = value
"""

    EndTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Date that the article was revised on

Get: EndTime(self: BenzingaNews) -> DateTime

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unique ID assigned to the article by Benzinga

Get: Id(self: BenzingaNews) -> int

Set: Id(self: BenzingaNews) = value
"""

    Symbols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbols that this news article mentions

Get: Symbols(self: BenzingaNews) -> List[Symbol]

Set: Symbols(self: BenzingaNews) = value
"""

    Tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Additional tags that are not channels/categories, but are reoccuring
            themes including, but not limited to; analyst names, bills being talked
            about in Congress (Dodd-Frank), specific products (iPhone), politicians,
            celebrities, stock movements (i.e. 'Mid-day Losers' & 'Mid-day Gainers').

Get: Tags(self: BenzingaNews) -> List[str]

Set: Tags(self: BenzingaNews) = value
"""

    Teaser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Summary of the article's contents

Get: Teaser(self: BenzingaNews) -> str

Set: Teaser(self: BenzingaNews) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Title of the article published

Get: Title(self: BenzingaNews) -> str

Set: Title(self: BenzingaNews) = value
"""

    UpdatedAt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Date that the article was revised on

Get: UpdatedAt(self: BenzingaNews) -> DateTime

Set: UpdatedAt(self: BenzingaNews) = value
"""



class BenzingaNewsJsonConverter(JsonConverter):
    """
    Helper json converter class used to convert Benzinga news data
                 into QuantConnect.Data.Custom.Benzinga.BenzingaNews
                
                 An example schema of the data in a serialized format is provided
                 to help you better understand this converter.
    
    BenzingaNewsJsonConverter(symbol: Symbol, liveMode: bool)
    """
    def CanConvert(self, objectType):
        """
        CanConvert(self: BenzingaNewsJsonConverter, objectType: Type) -> bool
        
            Determines whether this instance can convert the 
             specified object type.
        
        
            objectType: Type of the object.
            Returns: true if this instance can convert the specified 
             object type; otherwise, false.
        """
        pass

    @staticmethod
    def DeserializeNews(item, enableLogging):
        """
        DeserializeNews(item: JToken, enableLogging: bool) -> BenzingaNews
        
            Helper method to deserialize a single json 
             Benzinga news
        
        
            item: The json token containing the Benzinga news to 
             deserialize
        
            enableLogging: true to enable logging (for debug purposes)
            Returns: The deserialized 
             QuantConnect.Data.Custom.Benzinga.BenzingaNews 
             instance
        """
        pass

    def ReadJson(self, reader, objectType, existingValue, serializer):
        """
        ReadJson(self: BenzingaNewsJsonConverter, reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object
        
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
        WriteJson(self: BenzingaNewsJsonConverter, writer: JsonWriter, value: object, serializer: JsonSerializer)
            Writes the JSON representation of the object.
        
            writer: The Newtonsoft.Json.JsonWriter to write to.
            value: The value.
            serializer: The calling serializer.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol, liveMode):
        """ __new__(cls: type, symbol: Symbol, liveMode: bool) """
        pass

    ShareClassMappedTickers = None


