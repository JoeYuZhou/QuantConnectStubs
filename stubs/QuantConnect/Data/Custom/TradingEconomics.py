# encoding: utf-8
# module QuantConnect.Data.Custom.TradingEconomics calls itself TradingEconomics
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class EarningsType(Enum, IComparable, IFormattable, IConvertible):
    """
    Earnings type: earnings, ipo, dividends
    
    enum EarningsType, values: Dividends (2), Earnings (0), IPO (1), Split (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
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

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Dividends = None
    Earnings = None
    IPO = None
    Split = None
    value__ = None


class TradingEconomics(object):
    """ TradingEconomics static class contains shortcut definitions of major Trading Economics Indicators available """
    Calendar = None
    Event = None
    Indicator = None
    __all__ = [
        'Calendar',
        'Event',
        'Indicator',
    ]


class TradingEconomicsCalendar(BaseData, IBaseData):
    """
    Represents the Trading Economics Calendar information:
                The economic calendar covers around 1600 events for more than 150 countries a month.
                https://docs.tradingeconomics.com/#events
    
    TradingEconomicsCalendar()
    """
    def Clone(self, fillForward=None):
        """
        Clone(self: TradingEconomicsCalendar) -> BaseData
        
            Clones the data. This is required for some custom 
             data
        
            Returns: A new cloned instance
        """
        pass

    @staticmethod
    def CountryToCurrencyCode(country):
        """
        CountryToCurrencyCode(country: str) -> str
        
            Converts country name to currency code (ISO 4217)
        
            country: Country name
            Returns: ISO 4217 currency code
        """
        pass

    def DataTimeZone(self):
        """
        DataTimeZone(self: TradingEconomicsCalendar) -> DateTimeZone
        
            Specifies the data time zone for this data type. 
             This is useful for custom data types
        
            Returns: The NodaTime.DateTimeZone of this data type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: TradingEconomicsCalendar, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Return the Subscription Data Source gained from 
             the URL
        
        
            config: Configuration object
            date: Date of this source file
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: Subscription Data Source.
        """
        pass

    @staticmethod
    def ParseDecimal(value, inPercent):
        """
        ParseDecimal(value: str, inPercent: bool) -> Nullable[Decimal]
        
            Parse decimal from calendar data
        
            value: Value to parse
            inPercent: Is the value a percentage
            Returns: Nullable decimal
        """
        pass

    @staticmethod
    def ProcessAPIResponse(content):
        """
        ProcessAPIResponse(content: str) -> List[TradingEconomicsCalendar]
        
            Parses the raw Trading Economics calendar API 
             result
        
        
            content: Contents of returned data
            Returns: List of instances of the current class
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: TradingEconomicsCalendar, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Reader converts each line of the data source into 
             BaseData objects.
        
        
            config: Subscription data config setup object
            line: Line from the data source
            date: Date of the requested data
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: TradingEconomicsCalendar or BaseDataCollection 
             object containing TradingEconomicsCalendar as its 
             Data.
        """
        pass

    @staticmethod
    def SetAuthCode(authCode):
        """
        SetAuthCode(authCode: str)
            Sets the Trading Economics API key.
        
            authCode: The Trading Economics API key
        """
        pass

    def ToCsv(self):
        """
        ToCsv(self: TradingEconomicsCalendar) -> str
        
            Convert this instance to a CSV file
            Returns: string as CSV
        """
        pass

    def ToString(self):
        """
        ToString(self: TradingEconomicsCalendar) -> str
        
            Formats a string with the Trading Economics 
             Calendar information.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Actual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Latest released value

Get: Actual(self: TradingEconomicsCalendar) -> Nullable[Decimal]

Set: Actual(self: TradingEconomicsCalendar) = value
"""

    CalendarId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unique calendar ID used by Trading Economics

Get: CalendarId(self: TradingEconomicsCalendar) -> str

Set: CalendarId(self: TradingEconomicsCalendar) = value
"""

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicator category name

Get: Category(self: TradingEconomicsCalendar) -> str

Set: Category(self: TradingEconomicsCalendar) = value
"""

    Country = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Country name

Get: Country(self: TradingEconomicsCalendar) -> str

Set: Country(self: TradingEconomicsCalendar) = value
"""

    DateSpan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """0 indicates that the time of the event is known,
            1 indicates that we only know the date of event, the exact time of event is unknown

Get: DateSpan(self: TradingEconomicsCalendar) -> str

Set: DateSpan(self: TradingEconomicsCalendar) = value
"""

    EndTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Release time and date in UTC

Get: EndTime(self: TradingEconomicsCalendar) -> DateTime

Set: EndTime(self: TradingEconomicsCalendar) = value
"""

    Event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specific event name in the calendar

Get: Event(self: TradingEconomicsCalendar) -> str

Set: Event(self: TradingEconomicsCalendar) = value
"""

    EventRaw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Raw event name as provided by Trading Economics

Get: EventRaw(self: TradingEconomicsCalendar) -> str

Set: EventRaw(self: TradingEconomicsCalendar) = value
"""

    Forecast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Average forecast among a representative group of economists

Get: Forecast(self: TradingEconomicsCalendar) -> Nullable[Decimal]

Set: Forecast(self: TradingEconomicsCalendar) = value
"""

    Importance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Importance of a TradingEconomics information

Get: Importance(self: TradingEconomicsCalendar) -> TradingEconomicsImportance

Set: Importance(self: TradingEconomicsCalendar) = value
"""

    IsPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the Actual, Previous, Forecast, TradingEconomicsForecast fields are reported as percent values

Get: IsPercentage(self: TradingEconomicsCalendar) -> bool

Set: IsPercentage(self: TradingEconomicsCalendar) = value
"""

    LastUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Time when new data was inserted or changed

Get: LastUpdate(self: TradingEconomicsCalendar) -> DateTime

Set: LastUpdate(self: TradingEconomicsCalendar) = value
"""

    OCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Category's original name

Get: OCategory(self: TradingEconomicsCalendar) -> str

Set: OCategory(self: TradingEconomicsCalendar) = value
"""

    OCountry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Country's original name

Get: OCountry(self: TradingEconomicsCalendar) -> str

Set: OCountry(self: TradingEconomicsCalendar) = value
"""

    Previous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value for the previous period after the revision (if revision is applicable)

Get: Previous(self: TradingEconomicsCalendar) -> Nullable[Decimal]

Set: Previous(self: TradingEconomicsCalendar) = value
"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The period for which released data refers to

Get: Reference(self: TradingEconomicsCalendar) -> str

Set: Reference(self: TradingEconomicsCalendar) = value
"""

    Revised = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value reported in the previous period after revision

Get: Revised(self: TradingEconomicsCalendar) -> Nullable[Decimal]

Set: Revised(self: TradingEconomicsCalendar) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Source of data

Get: Source(self: TradingEconomicsCalendar) -> str

Set: Source(self: TradingEconomicsCalendar) = value
"""

    Ticker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unique ticker used by Trading Economics

Get: Ticker(self: TradingEconomicsCalendar) -> str

Set: Ticker(self: TradingEconomicsCalendar) = value
"""

    TradingEconomicsForecast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """TradingEconomics own projections

Get: TradingEconomicsForecast(self: TradingEconomicsCalendar) -> Nullable[Decimal]

Set: TradingEconomicsForecast(self: TradingEconomicsCalendar) = value
"""


    AuthCode = ''
    IsAuthCodeSet = False


class TradingEconomicsDateTimeConverter(JsonConverter):
    """
    DateTime JSON Converter that handles null value
    
    TradingEconomicsDateTimeConverter()
    """
    def CanConvert(self, objectType):
        """
        CanConvert(self: TradingEconomicsDateTimeConverter, objectType: Type) -> bool
        
            Indicate if we can convert this object.
        """
        pass

    def ReadJson(self, reader, objectType, existingValue, serializer):
        """
        ReadJson(self: TradingEconomicsDateTimeConverter, reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object
        
            Parse Trading Economics DateTime to C# DateTime
        """
        pass

    def WriteJson(self, writer, value, serializer):
        """
        WriteJson(self: TradingEconomicsDateTimeConverter, writer: JsonWriter, value: object, serializer: JsonSerializer)
            Write DateTime objects to JSON
        """
        pass


class TradingEconomicsEarnings(BaseData, IBaseData):
    """
    Represents the Trading Economics Earnings information.
                https://docs.tradingeconomics.com/#earnings
    
    TradingEconomicsEarnings()
    """
    def DataTimeZone(self):
        """
        DataTimeZone(self: TradingEconomicsEarnings) -> DateTimeZone
        
            Specifies the data time zone for this data type. 
             This is useful for custom data types
        
            Returns: The NodaTime.DateTimeZone of this data type
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Actual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Earnings per share

Get: Actual(self: TradingEconomicsEarnings) -> Nullable[Decimal]

Set: Actual(self: TradingEconomicsEarnings) = value
"""

    CalendarReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Calendar quarter for the release

Get: CalendarReference(self: TradingEconomicsEarnings) -> str

Set: CalendarReference(self: TradingEconomicsEarnings) = value
"""

    Country = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Country name

Get: Country(self: TradingEconomicsEarnings) -> str

Set: Country(self: TradingEconomicsEarnings) = value
"""

    Currency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Currency

Get: Currency(self: TradingEconomicsEarnings) -> str

Set: Currency(self: TradingEconomicsEarnings) = value
"""

    EarningsType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Earnings type: earnings, ipo, dividends

Get: EarningsType(self: TradingEconomicsEarnings) -> EarningsType

Set: EarningsType(self: TradingEconomicsEarnings) = value
"""

    EndTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Release time and date in UTC

Get: EndTime(self: TradingEconomicsEarnings) -> DateTime

Set: EndTime(self: TradingEconomicsEarnings) = value
"""

    FiscalReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fiscal year and quarter in different format

Get: FiscalReference(self: TradingEconomicsEarnings) -> str

Set: FiscalReference(self: TradingEconomicsEarnings) = value
"""

    FiscalTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fiscal year and quarter

Get: FiscalTag(self: TradingEconomicsEarnings) -> str

Set: FiscalTag(self: TradingEconomicsEarnings) = value
"""

    Forecast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Average forecast among a representative group of analysts

Get: Forecast(self: TradingEconomicsEarnings) -> Nullable[Decimal]

Set: Forecast(self: TradingEconomicsEarnings) = value
"""

    LastUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Time when new data was inserted or changed

Get: LastUpdate(self: TradingEconomicsEarnings) -> DateTime

Set: LastUpdate(self: TradingEconomicsEarnings) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Company name

Get: Name(self: TradingEconomicsEarnings) -> str

Set: Name(self: TradingEconomicsEarnings) = value
"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unique symbol used by Trading Economics

Get: Symbol(self: TradingEconomicsEarnings) -> str

Set: Symbol(self: TradingEconomicsEarnings) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Earnings per share

Get: Value(self: TradingEconomicsEarnings) -> Decimal

"""



class TradingEconomicsEventFilter(object):
    """ Provides methods to filter and standardize Trading Economics calendar event names. """
    @staticmethod
    def FilterEvent(eventName):
        """
        FilterEvent(eventName: str) -> str
        
            Convert and normalizes the Trading Economics 
             calendar "Event" field.
        
        
            eventName: Raw event name
            Returns: Event name normalized
        """
        pass

    __all__ = [
        'FilterEvent',
    ]


class TradingEconomicsImportance(Enum, IComparable, IFormattable, IConvertible):
    """
    Importance of a TradingEconomics information
    
    enum TradingEconomicsImportance, values: High (2), Low (0), Medium (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
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

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    High = None
    Low = None
    Medium = None
    value__ = None


class TradingEconomicsIndicator(BaseData, IBaseData):
    """
    Represents the Trading Economics Indicator information.
                https://docs.tradingeconomics.com/#indicators
    
    TradingEconomicsIndicator()
    """
    def Clone(self, fillForward=None):
        """
        Clone(self: TradingEconomicsIndicator) -> BaseData
        
            Clones the data. This is required for some custom 
             data
        
            Returns: A new cloned instance
        """
        pass

    def DataTimeZone(self):
        """
        DataTimeZone(self: TradingEconomicsIndicator) -> DateTimeZone
        
            Specifies the data time zone for this data type. 
             This is useful for custom data types
        
            Returns: The NodaTime.DateTimeZone of this data type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: TradingEconomicsIndicator, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Return the Subscription Data Source gained from 
             the URL
        
        
            config: Configuration object
            date: Date of this source file
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: Subscription Data Source.
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: TradingEconomicsIndicator, config: SubscriptionDataConfig, content: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Reader converts each line of the data source into 
             BaseData objects.
        
        
            config: Subscription data config setup object
            content: Content of the source document
            date: Date of the requested data
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: Collection of TradingEconomicsIndicator objects
        """
        pass

    def ToString(self):
        """
        ToString(self: TradingEconomicsIndicator) -> str
        
            Formats a string with the Trading Economics 
             Indicator information.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicator category name

Get: Category(self: TradingEconomicsIndicator) -> str

Set: Category(self: TradingEconomicsIndicator) = value
"""

    Country = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Country name

Get: Country(self: TradingEconomicsIndicator) -> str

Set: Country(self: TradingEconomicsIndicator) = value
"""

    EndTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Release time and date in UTC

Get: EndTime(self: TradingEconomicsIndicator) -> DateTime

Set: EndTime(self: TradingEconomicsIndicator) = value
"""

    Frequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Frequency of the indicator

Get: Frequency(self: TradingEconomicsIndicator) -> str

Set: Frequency(self: TradingEconomicsIndicator) = value
"""

    HistoricalDataSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unique symbol used by Trading Economics

Get: HistoricalDataSymbol(self: TradingEconomicsIndicator) -> str

Set: HistoricalDataSymbol(self: TradingEconomicsIndicator) = value
"""

    LastUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Time when new data was inserted or changed

Get: LastUpdate(self: TradingEconomicsIndicator) -> DateTime

Set: LastUpdate(self: TradingEconomicsIndicator) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value

Get: Value(self: TradingEconomicsIndicator) -> Decimal

Set: Value(self: TradingEconomicsIndicator) = value
"""



