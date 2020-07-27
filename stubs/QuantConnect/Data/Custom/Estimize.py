# encoding: utf-8
# module QuantConnect.Data.Custom.Estimize calls itself Estimize
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class EstimizeConsensus(BaseData, IBaseData):
    """
    Consensus of the specified release
    
    EstimizeConsensus()
    EstimizeConsensus(csvLine: str)
    """
    def DataTimeZone(self):
        """
        DataTimeZone(self: EstimizeConsensus) -> DateTimeZone
        
            Specifies the data time zone for this data type. 
             This is useful for custom data types
        
            Returns: The NodaTime.DateTimeZone of this data type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: EstimizeConsensus, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
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
        Reader(self: EstimizeConsensus, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Reader converts each line of the data source into 
             BaseData objects.
        
        
            config: Subscription data config setup object
            line: Content of the source document
            date: Date of the requested data
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: Estimize consensus object
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: EstimizeConsensus) -> bool
        
            Indicates if there is support for mapping
            Returns: True indicates mapping should be used
        """
        pass

    def ToString(self):
        """
        ToString(self: EstimizeConsensus) -> str
        
            Formats a string with the Estimize Estimate 
             information.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, csvLine=None):
        """
        __new__(cls: type)
        __new__(cls: type, csvLine: str)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of estimates in the distribution

Get: Count(self: EstimizeConsensus) -> Nullable[int]

Set: Count(self: EstimizeConsensus) = value
"""

    EndTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The timestamp of this consensus (UTC)

Get: EndTime(self: EstimizeConsensus) -> DateTime

"""

    FiscalQuarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fiscal quarter for the release

Get: FiscalQuarter(self: EstimizeConsensus) -> Nullable[int]

Set: FiscalQuarter(self: EstimizeConsensus) = value
"""

    FiscalYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fiscal year for the release

Get: FiscalYear(self: EstimizeConsensus) -> Nullable[int]

Set: FiscalYear(self: EstimizeConsensus) = value
"""

    High = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The highest estimate in the distribution

Get: High(self: EstimizeConsensus) -> Nullable[Decimal]

Set: High(self: EstimizeConsensus) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique identifier for the estimate

Get: Id(self: EstimizeConsensus) -> str

Set: Id(self: EstimizeConsensus) = value
"""

    Low = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The lowest estimate in the distribution

Get: Low(self: EstimizeConsensus) -> Nullable[Decimal]

Set: Low(self: EstimizeConsensus) = value
"""

    Mean = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mean of the distribution of estimates (the "consensus")

Get: Mean(self: EstimizeConsensus) -> Nullable[Decimal]

Set: Mean(self: EstimizeConsensus) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Consensus source (Wall Street or Estimize)

Get: Source(self: EstimizeConsensus) -> Nullable[Source]

Set: Source(self: EstimizeConsensus) = value
"""

    StandardDeviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The standard deviation of the distribution

Get: StandardDeviation(self: EstimizeConsensus) -> Nullable[Decimal]

Set: StandardDeviation(self: EstimizeConsensus) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of Consensus (EPS or Revenue)

Get: Type(self: EstimizeConsensus) -> Nullable[Type]

Set: Type(self: EstimizeConsensus) = value
"""

    UpdatedAt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The timestamp of this consensus (UTC)

Get: UpdatedAt(self: EstimizeConsensus) -> DateTime

Set: UpdatedAt(self: EstimizeConsensus) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mean of the distribution of estimates (the "consensus")

Get: Value(self: EstimizeConsensus) -> Decimal

"""



class EstimizeEstimate(BaseData, IBaseData):
    """
    Financial estimates for the specified company
    
    EstimizeEstimate()
    EstimizeEstimate(csvLine: str)
    """
    def DataTimeZone(self):
        """
        DataTimeZone(self: EstimizeEstimate) -> DateTimeZone
        
            Specifies the data time zone for this data type. 
             This is useful for custom data types
        
            Returns: The NodaTime.DateTimeZone of this data type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: EstimizeEstimate, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
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
        Reader(self: EstimizeEstimate, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Reader converts each line of the data source into 
             BaseData objects.
        
        
            config: Subscription data config setup object
            line: Content of the source document
            date: Date of the requested data
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: Estimize Estimate object
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: EstimizeEstimate) -> bool
        
            Indicates if there is support for mapping
            Returns: True indicates mapping should be used
        """
        pass

    def ToString(self):
        """
        ToString(self: EstimizeEstimate) -> str
        
            Formats a string with the Estimize Estimate 
             information.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, csvLine=None):
        """
        __new__(cls: type)
        __new__(cls: type, csvLine: str)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AnalystId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The author of the estimate

Get: AnalystId(self: EstimizeEstimate) -> str

Set: AnalystId(self: EstimizeEstimate) = value
"""

    CreatedAt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The time that the estimate was created (UTC)

Get: CreatedAt(self: EstimizeEstimate) -> DateTime

Set: CreatedAt(self: EstimizeEstimate) = value
"""

    EndTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The time that the estimate was created (UTC)

Get: EndTime(self: EstimizeEstimate) -> DateTime

"""

    Eps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The estimated earnings per share for the company in the specified fiscal quarter

Get: Eps(self: EstimizeEstimate) -> Nullable[Decimal]

Set: Eps(self: EstimizeEstimate) = value
"""

    FiscalQuarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fiscal quarter of the quarter being estimated

Get: FiscalQuarter(self: EstimizeEstimate) -> int

Set: FiscalQuarter(self: EstimizeEstimate) = value
"""

    FiscalYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fiscal year of the quarter being estimated

Get: FiscalYear(self: EstimizeEstimate) -> int

Set: FiscalYear(self: EstimizeEstimate) = value
"""

    Flagged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A boolean value which indicates whether we have flagged this estimate internally as erroneous
            (spam, wrong accounting standard, etc)

Get: Flagged(self: EstimizeEstimate) -> bool

Set: Flagged(self: EstimizeEstimate) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique identifier for the estimate

Get: Id(self: EstimizeEstimate) -> str

Set: Id(self: EstimizeEstimate) = value
"""

    Revenue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The estimated revenue for the company in the specified fiscal quarter

Get: Revenue(self: EstimizeEstimate) -> Nullable[Decimal]

Set: Revenue(self: EstimizeEstimate) = value
"""

    Ticker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ticker of the company being estimated

Get: Ticker(self: EstimizeEstimate) -> str

Set: Ticker(self: EstimizeEstimate) = value
"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique identifier for the author of the estimate

Get: UserName(self: EstimizeEstimate) -> str

Set: UserName(self: EstimizeEstimate) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The estimated earnings per share for the company in the specified fiscal quarter

Get: Value(self: EstimizeEstimate) -> Decimal

"""



class EstimizeRelease(BaseData, IBaseData):
    """
    Financial releases for the specified company
    
    EstimizeRelease()
    EstimizeRelease(csvLine: str)
    """
    def DataTimeZone(self):
        """
        DataTimeZone(self: EstimizeRelease) -> DateTimeZone
        
            Specifies the data time zone for this data type. 
             This is useful for custom data types
        
            Returns: The NodaTime.DateTimeZone of this data type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: EstimizeRelease, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
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
        Reader(self: EstimizeRelease, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Reader converts each line of the data source into 
             BaseData objects.
        
        
            config: Subscription data config setup object
            line: Content of the source document
            date: Date of the requested data
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: Estimize Release object
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: EstimizeRelease) -> bool
        
            Indicates if there is support for mapping
            Returns: True indicates mapping should be used
        """
        pass

    def ToString(self):
        """
        ToString(self: EstimizeRelease) -> str
        
            Formats a string with the Estimize Release 
             information.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, csvLine=None):
        """
        __new__(cls: type)
        __new__(cls: type, csvLine: str)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ConsensusEpsEstimate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mean EPS consensus by the Estimize community

Get: ConsensusEpsEstimate(self: EstimizeRelease) -> Nullable[Decimal]

Set: ConsensusEpsEstimate(self: EstimizeRelease) = value
"""

    ConsensusRevenueEstimate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mean revenue consensus by the Estimize community

Get: ConsensusRevenueEstimate(self: EstimizeRelease) -> Nullable[Decimal]

Set: ConsensusRevenueEstimate(self: EstimizeRelease) = value
"""

    ConsensusWeightedEpsEstimate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The weighted EPS consensus by the Estimize community

Get: ConsensusWeightedEpsEstimate(self: EstimizeRelease) -> Nullable[Decimal]

Set: ConsensusWeightedEpsEstimate(self: EstimizeRelease) = value
"""

    ConsensusWeightedRevenueEstimate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The weighted revenue consensus by the Estimize community

Get: ConsensusWeightedRevenueEstimate(self: EstimizeRelease) -> Nullable[Decimal]

Set: ConsensusWeightedRevenueEstimate(self: EstimizeRelease) = value
"""

    EndTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The date of the release

Get: EndTime(self: EstimizeRelease) -> DateTime

"""

    Eps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The earnings per share for the specified fiscal quarter

Get: Eps(self: EstimizeRelease) -> Nullable[Decimal]

Set: Eps(self: EstimizeRelease) = value
"""

    FiscalQuarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fiscal quarter for the release

Get: FiscalQuarter(self: EstimizeRelease) -> int

Set: FiscalQuarter(self: EstimizeRelease) = value
"""

    FiscalYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fiscal year for the release

Get: FiscalYear(self: EstimizeRelease) -> int

Set: FiscalYear(self: EstimizeRelease) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique identifier for the release

Get: Id(self: EstimizeRelease) -> str

Set: Id(self: EstimizeRelease) = value
"""

    ReleaseDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The date of the release

Get: ReleaseDate(self: EstimizeRelease) -> DateTime

Set: ReleaseDate(self: EstimizeRelease) = value
"""

    Revenue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The revenue for the specified fiscal quarter

Get: Revenue(self: EstimizeRelease) -> Nullable[Decimal]

Set: Revenue(self: EstimizeRelease) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The earnings per share for the specified fiscal quarter

Get: Value(self: EstimizeRelease) -> Decimal

"""

    WallStreetEpsEstimate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The estimated EPS from Wall Street

Get: WallStreetEpsEstimate(self: EstimizeRelease) -> Nullable[Decimal]

Set: WallStreetEpsEstimate(self: EstimizeRelease) = value
"""

    WallStreetRevenueEstimate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The estimated revenue from Wall Street

Get: WallStreetRevenueEstimate(self: EstimizeRelease) -> Nullable[Decimal]

Set: WallStreetRevenueEstimate(self: EstimizeRelease) = value
"""



class Source(Enum, IComparable, IFormattable, IConvertible):
    """
    Source of the Consensus
    
    enum Source, values: Estimize (1), WallStreet (0)
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

    Estimize = None
    value__ = None
    WallStreet = None


class Type(Enum, IComparable, IFormattable, IConvertible):
    """
    Type of the consensus
    
    enum Type, values: Eps (0), Revenue (1)
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

    Eps = None
    Revenue = None
    value__ = None


