# encoding: utf-8
# module QuantConnect
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AccountType(Enum, IComparable, IFormattable, IConvertible):
    """
    Account type: margin or cash
    
    enum AccountType, values: Cash (1), Margin (0)
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

    Cash = None
    Margin = None
    value__ = None


class AlgorithmControl(object):
    """
    Wrapper for algorithm status enum to include the charting subscription.
    
    AlgorithmControl()
    """
    ChartSubscription = None
    HasSubscribers = None
    Initialized = None
    Status = None


class AlgorithmSettings(object, IAlgorithmSettings):
    """
    This class includes user settings for the algorithm which can be changed in the QuantConnect.Interfaces.IAlgorithm.Initialize method
    
    AlgorithmSettings()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DataSubscriptionLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets the maximum number of concurrent market data subscriptions available

Get: DataSubscriptionLimit(self: AlgorithmSettings) -> int

Set: DataSubscriptionLimit(self: AlgorithmSettings) = value
"""

    FreePortfolioValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets the SetHoldings buffers value.
            The buffer is used for orders not to be rejected due to volatility when using SetHoldings and CalculateOrderQuantity

Get: FreePortfolioValue(self: AlgorithmSettings) -> Decimal

Set: FreePortfolioValue(self: AlgorithmSettings) = value
"""

    FreePortfolioValuePercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets the SetHoldings buffers value percentage.
            This percentage will be used to set the QuantConnect.AlgorithmSettings.FreePortfolioValue
            based on the QuantConnect.Securities.SecurityPortfolioManager.TotalPortfolioValue

Get: FreePortfolioValuePercentage(self: AlgorithmSettings) -> Decimal

Set: FreePortfolioValuePercentage(self: AlgorithmSettings) = value
"""

    LiquidateEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets if Liquidate() is enabled

Get: LiquidateEnabled(self: AlgorithmSettings) -> bool

Set: LiquidateEnabled(self: AlgorithmSettings) = value
"""

    MaxAbsolutePortfolioTargetPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The absolute maximum valid total portfolio value target percentage

Get: MaxAbsolutePortfolioTargetPercentage(self: AlgorithmSettings) -> Decimal

Set: MaxAbsolutePortfolioTargetPercentage(self: AlgorithmSettings) = value
"""

    MinAbsolutePortfolioTargetPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The absolute minimum valid total portfolio value target percentage

Get: MinAbsolutePortfolioTargetPercentage(self: AlgorithmSettings) -> Decimal

Set: MinAbsolutePortfolioTargetPercentage(self: AlgorithmSettings) = value
"""

    RebalancePortfolioOnInsightChanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if should rebalance portfolio on new insights or expiration of insights. True by default

Get: RebalancePortfolioOnInsightChanges(self: AlgorithmSettings) -> Nullable[bool]

Set: RebalancePortfolioOnInsightChanges(self: AlgorithmSettings) = value
"""

    RebalancePortfolioOnSecurityChanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if should rebalance portfolio on security changes. True by default

Get: RebalancePortfolioOnSecurityChanges(self: AlgorithmSettings) -> Nullable[bool]

Set: RebalancePortfolioOnSecurityChanges(self: AlgorithmSettings) = value
"""

    StalePriceTimeSpan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets the minimum time span elapsed to consider a market fill price as stale (defaults to one hour)

Get: StalePriceTimeSpan(self: AlgorithmSettings) -> TimeSpan

Set: StalePriceTimeSpan(self: AlgorithmSettings) = value
"""



class AlgorithmStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    States of a live deployment.
    
    enum AlgorithmStatus, values: Completed (6), Deleted (5), DeployError (0), History (11), Initializing (10), InQueue (1), Invalid (8), Liquidated (4), LoggingIn (9), Running (2), RuntimeError (7), Stopped (3)
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

    Completed = None
    Deleted = None
    DeployError = None
    History = None
    Initializing = None
    InQueue = None
    Invalid = None
    Liquidated = None
    LoggingIn = None
    Running = None
    RuntimeError = None
    Stopped = None
    value__ = None


class AlphaRuntimeStatistics(object):
    """
    Contains insight population run time statistics
    
    AlphaRuntimeStatistics(accountCurrencyProvider: IAccountCurrencyProvider)
    AlphaRuntimeStatistics()
    """
    def SetDate(self, now):
        """
        SetDate(self: AlphaRuntimeStatistics, now: DateTime)
            Set the current date of the backtest
        """
        pass

    def SetStartDate(self, algorithmStartDate):
        """
        SetStartDate(self: AlphaRuntimeStatistics, algorithmStartDate: DateTime)
            Set the date range of the statistics
        """
        pass

    def ToDictionary(self):
        """
        ToDictionary(self: AlphaRuntimeStatistics) -> Dictionary[str, str]
        
            Creates a dictionary containing the statistics
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountCurrencyProvider=None):
        """
        __new__(cls: type, accountCurrencyProvider: IAccountCurrencyProvider)
        __new__(cls: type)
        """
        pass

    EstimatedMonthlyAlphaValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Suggested Value of the Alpha On A Monthly Basis For Licensing

Get: EstimatedMonthlyAlphaValue(self: AlphaRuntimeStatistics) -> Decimal

"""

    FitnessScore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Score of the strategy's performance, and suitability for the Alpha Stream Market

Get: FitnessScore(self: AlphaRuntimeStatistics) -> Decimal

Set: FitnessScore(self: AlphaRuntimeStatistics) = value
"""

    KellyCriterionEstimate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Score of the strategy's insights predictive power

Get: KellyCriterionEstimate(self: AlphaRuntimeStatistics) -> Decimal

Set: KellyCriterionEstimate(self: AlphaRuntimeStatistics) = value
"""

    KellyCriterionProbabilityValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The p-value or probability value of the QuantConnect.AlphaRuntimeStatistics.KellyCriterionEstimate

Get: KellyCriterionProbabilityValue(self: AlphaRuntimeStatistics) -> Decimal

Set: KellyCriterionProbabilityValue(self: AlphaRuntimeStatistics) = value
"""

    LongCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total number of insights with an up direction

Get: LongCount(self: AlphaRuntimeStatistics) -> Int64

Set: LongCount(self: AlphaRuntimeStatistics) = value
"""

    LongShortRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ratio of QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Up over QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Down

Get: LongShortRatio(self: AlphaRuntimeStatistics) -> Decimal

"""

    MeanPopulationEstimatedInsightValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the mean estimated insight value

Get: MeanPopulationEstimatedInsightValue(self: AlphaRuntimeStatistics) -> Decimal

"""

    MeanPopulationScore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the mean scores for the entire population of insights

Get: MeanPopulationScore(self: AlphaRuntimeStatistics) -> InsightScore

"""

    PortfolioTurnover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Measurement of the strategies trading activity with respect to the portfolio value.
            Calculated as the sales volume with respect to the average total portfolio value.

Get: PortfolioTurnover(self: AlphaRuntimeStatistics) -> Decimal

Set: PortfolioTurnover(self: AlphaRuntimeStatistics) = value
"""

    ReturnOverMaxDrawdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides a risk adjusted way to factor in the returns and drawdown of the strategy.
            It is calculated by dividing the Portfolio Annualized Return by the Maximum Drawdown seen during the backtest.

Get: ReturnOverMaxDrawdown(self: AlphaRuntimeStatistics) -> Decimal

Set: ReturnOverMaxDrawdown(self: AlphaRuntimeStatistics) = value
"""

    RollingAveragedPopulationScore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the 100 insight ema of insight scores

Get: RollingAveragedPopulationScore(self: AlphaRuntimeStatistics) -> InsightScore

"""

    ShortCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total number of insights with a down direction

Get: ShortCount(self: AlphaRuntimeStatistics) -> Int64

Set: ShortCount(self: AlphaRuntimeStatistics) = value
"""

    SortinoRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gives a relative picture of the strategy volatility.
            It is calculated by taking a portfolio's annualized rate of return and subtracting the risk free rate of return.

Get: SortinoRatio(self: AlphaRuntimeStatistics) -> Decimal

Set: SortinoRatio(self: AlphaRuntimeStatistics) = value
"""

    TotalAccumulatedEstimatedAlphaValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total accumulated estimated value of trading all insights

Get: TotalAccumulatedEstimatedAlphaValue(self: AlphaRuntimeStatistics) -> Decimal

Set: TotalAccumulatedEstimatedAlphaValue(self: AlphaRuntimeStatistics) = value
"""

    TotalInsightsAnalysisCompleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total number of insight signals generated by the algorithm

Get: TotalInsightsAnalysisCompleted(self: AlphaRuntimeStatistics) -> Int64

Set: TotalInsightsAnalysisCompleted(self: AlphaRuntimeStatistics) = value
"""

    TotalInsightsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total number of insight signals generated by the algorithm

Get: TotalInsightsClosed(self: AlphaRuntimeStatistics) -> Int64

Set: TotalInsightsClosed(self: AlphaRuntimeStatistics) = value
"""

    TotalInsightsGenerated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total number of insight signals generated by the algorithm

Get: TotalInsightsGenerated(self: AlphaRuntimeStatistics) -> Int64

Set: TotalInsightsGenerated(self: AlphaRuntimeStatistics) = value
"""



class BrokerageEnvironment(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the types of environments supported by brokerages for trading
    
    enum BrokerageEnvironment, values: Live (0), Paper (1)
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

    Live = None
    Paper = None
    value__ = None


class ChannelStatus(object):
    """ Defines the different channel status values """
    Occupied = 'channel_occupied'
    Vacated = 'channel_vacated'
    __all__ = [
        'Occupied',
        'Vacated',
    ]


class Chart(object):
    """
    Single Parent Chart Object for Custom Charting
    
    Chart()
    Chart(name: str, type: ChartType)
    Chart(name: str)
    """
    def AddSeries(self, series):
        """
        AddSeries(self: Chart, series: Series)
            Add a reference to this chart series:
        
            series: Chart series class object
        """
        pass

    def Clone(self):
        """
        Clone(self: Chart) -> Chart
        
            Return a new instance clone of this object
        """
        pass

    def GetUpdates(self):
        """
        GetUpdates(self: Chart) -> Chart
        
            Fetch the updates of the chart, and save the 
             index position.
        """
        pass

    def TryAddAndGetSeries(self, name, type, index, unit, color, symbol, forceAddNew):
        """
        TryAddAndGetSeries(self: Chart, name: str, type: SeriesType, index: int, unit: str, color: Color, symbol: ScatterMarkerSymbol, forceAddNew: bool) -> Series
        
            Gets Series if already present in chart, else 
             will add a new series and return it
        
        
            name: Name of the series
            type: Type of the series
            index: Index position on the chart of the series
            unit: Unit for the series axis
            color: Color of the series
            symbol: Symbol for the marker in a scatter plot series
            forceAddNew: True will always add a new Series instance, 
             stepping on existing if any
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None, type=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str, type: ChartType)
        __new__(cls: type, name: str)
        """
        pass

    ChartType = None
    Name = None
    Series = None


class ChartPoint(object):
    """
    Single Chart Point Value Type for QCAlgorithm.Plot();
    
    ChartPoint()
    ChartPoint(xValue: Int64, yValue: Decimal)
    ChartPoint(time: DateTime, value: Decimal)
    ChartPoint(point: ChartPoint)
    """
    def ToString(self):
        """
        ToString(self: ChartPoint) -> str
        
            Provides a readable string representation of this 
             instance.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, xValue: Int64, yValue: Decimal)
        __new__(cls: type, time: DateTime, value: Decimal)
        __new__(cls: type, point: ChartPoint)
        """
        pass

    x = None
    y = None


class ChartType(Enum, IComparable, IFormattable, IConvertible):
    """
    Type of chart - should we draw the series as overlayed or stacked
    
    enum ChartType, values: Overlay (0), Stacked (1)
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

    Overlay = None
    Stacked = None
    value__ = None


class Currencies(object):
    """ Provides commonly used currency pairs and symbols """
    @staticmethod
    def GetCurrencySymbol(currency):
        """
        GetCurrencySymbol(currency: str) -> str
        
            Gets the currency symbol for the specified 
             currency code
        
        
            currency: The currency code
            Returns: The currency symbol
        """
        pass

    CfdCurrencyPairs = None
    CryptoCurrencyPairs = None
    CurrencyPairs = None
    CurrencySymbols = None
    NullCurrency = 'QCC'
    USD = 'USD'
    __all__ = [
        'CfdCurrencyPairs',
        'CryptoCurrencyPairs',
        'CurrencyPairs',
        'CurrencySymbols',
        'GetCurrencySymbol',
        'NullCurrency',
    ]


class DataFeedEndpoint(Enum, IComparable, IFormattable, IConvertible):
    """
    Datafeed enum options for selecting the source of the datafeed.
    
    enum DataFeedEndpoint, values: Backtesting (0), Database (3), FileSystem (1), LiveTrading (2)
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

    Backtesting = None
    Database = None
    FileSystem = None
    LiveTrading = None
    value__ = None


class DataNormalizationMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how data is normalized before being sent into an algorithm
    
    enum DataNormalizationMode, values: Adjusted (1), Raw (0), SplitAdjusted (2), TotalReturn (3)
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

    Adjusted = None
    Raw = None
    SplitAdjusted = None
    TotalReturn = None
    value__ = None


class DateFormat(object):
    """ Shortcut date format strings """
    DB = 'yyyy-MM-dd HH:mm:ss'
    EightCharacter = 'yyyyMMdd'
    Forex = 'yyyyMMdd HH:mm:ss.ffff'
    JsonFormat = 'yyyy-MM-ddTHH:mm:ss'
    SixCharacter = 'yyMMdd'
    TwelveCharacter = 'yyyyMMdd HH:mm'
    UI = 'yyyy-MM-dd HH:mm:ss'
    US = 'M/d/yyyy h:mm:ss tt'
    YearMonth = 'yyyyMM'
    __all__ = [
        'DB',
        'EightCharacter',
        'Forex',
        'SixCharacter',
        'TwelveCharacter',
        'UI',
        'US',
        'YearMonth',
    ]


class DelistingType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of QuantConnect.Data.Market.Delisting data
    
    enum DelistingType, values: Delisted (1), Warning (0)
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

    Delisted = None
    value__ = None
    Warning = None


class DownloadFailedEventArgs(EventArgs):
    """
    Event arguments for the QuantConnect.Interfaces.IDataProviderEvents.DownloadFailed event
    
    DownloadFailedEventArgs(message: str, stackTrace: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, message, stackTrace):
        """ __new__(cls: type, message: str, stackTrace: str) """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error message

Get: Message(self: DownloadFailedEventArgs) -> str

"""

    StackTrace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error stack trace

Get: StackTrace(self: DownloadFailedEventArgs) -> str

"""



class Expiry(object):
    """ Provides static functions that can be used to compute a future System.DateTime (expiry) given a System.DateTime. """
    def EndOfDay(self, *args): #cannot find CLR method
        """ Func[DateTime, DateTime](object: object, method: IntPtr) """
        pass

    def EndOfMonth(self, *args): #cannot find CLR method
        """ Func[DateTime, DateTime](object: object, method: IntPtr) """
        pass

    def EndOfQuarter(self, *args): #cannot find CLR method
        """ Func[DateTime, DateTime](object: object, method: IntPtr) """
        pass

    def EndOfWeek(self, *args): #cannot find CLR method
        """ Func[DateTime, DateTime](object: object, method: IntPtr) """
        pass

    def EndOfYear(self, *args): #cannot find CLR method
        """ Func[DateTime, DateTime](object: object, method: IntPtr) """
        pass

    def OneMonth(self, *args): #cannot find CLR method
        """ Func[DateTime, DateTime](object: object, method: IntPtr) """
        pass

    def OneQuarter(self, *args): #cannot find CLR method
        """ Func[DateTime, DateTime](object: object, method: IntPtr) """
        pass

    def OneYear(self, *args): #cannot find CLR method
        """ Func[DateTime, DateTime](object: object, method: IntPtr) """
        pass

    __all__ = []


class ExtendedDictionary(object, IExtendedDictionary[Symbol, T]):
    # no doc
    def clear(self):
        """
        clear(self: ExtendedDictionary[T])
            Removes all keys and values from the 
             QuantConnect.Interfaces.IExtendedDictionary.
        """
        pass

    def Clear(self):
        """
        Clear(self: ExtendedDictionary[T])
            Removes all items from the 
             System.Collections.Generic.ICollection.
        """
        pass

    def copy(self):
        """
        copy(self: ExtendedDictionary[T]) -> PyDict
        
            Creates a shallow copy of the 
             QuantConnect.Interfaces.IExtendedDictionary.
        
            Returns: Returns a shallow copy of the dictionary. It 
             doesn't modify the original dictionary.
        """
        pass

    def fromkeys(self, sequence, value=None):
        """
        fromkeys(self: ExtendedDictionary[T], sequence: Array[Symbol]) -> PyDict
        
            Creates a new dictionary from the given sequence 
             of elements.
        
        
            sequence: Sequence of elements which is to be used as keys 
             for the new dictionary
        
            Returns: Returns a new dictionary with the given sequence 
             of elements as the keys of the dictionary.
        
        fromkeys(self: ExtendedDictionary[T], sequence: Array[Symbol], value: T) -> PyDict
        
            Creates a new dictionary from the given sequence 
             of elements with a value provided by the user.
        
        
            sequence: Sequence of elements which is to be used as keys 
             for the new dictionary
        
            value: Value which is set to each each element of the 
             dictionary
        
            Returns: Returns a new dictionary with the given sequence 
             of elements as the keys of the dictionary.
              
                   Each element of the newly created 
             dictionary is set to the provided value.
        """
        pass

    def get(self, symbol, value=None):
        """
        get(self: ExtendedDictionary[T], symbol: Symbol) -> T
        
            Returns the value for the specified Symbol if 
             Symbol is in dictionary.
        
        
            symbol: Symbol to be searched in the dictionary
            Returns: The value for the specified Symbol if Symbol is 
             in dictionary.
                    None if the Symbol is 
             not found and value is not specified.
        
        get(self: ExtendedDictionary[T], symbol: Symbol, value: T) -> T
        
            Returns the value for the specified Symbol if 
             Symbol is in dictionary.
        
        
            symbol: Symbol to be searched in the dictionary
            value: Value to be returned if the Symbol is not found. 
             The default value is null.
        
            Returns: The value for the specified Symbol if Symbol is 
             in dictionary.
                    value if the Symbol 
             is not found and value is specified.
        """
        pass

    def items(self):
        """
        items(self: ExtendedDictionary[T]) -> PyList
        
            Returns a view object that displays a list of 
             dictionary's (Symbol, value) tuple pairs.
        
            Returns: Returns a view object that displays a list of a 
             given dictionary's (Symbol, value) tuple pair.
        """
        pass

    def keys(self):
        """
        keys(self: ExtendedDictionary[T]) -> PyList
        
            Returns a view object that displays a list of all 
             the Symbol objects in the dictionary
        
            Returns: Returns a view object that displays a list of all 
             the Symbol objects.
                    When the 
             dictionary is changed, the view object also 
             reflect these changes.
        """
        pass

    def pop(self, symbol, default_value=None):
        """
        pop(self: ExtendedDictionary[T], symbol: Symbol) -> T
        
            Removes and returns an element from a dictionary 
             having the given Symbol.
        
        
            symbol: Key which is to be searched for removal
            Returns: If Symbol is found - removed/popped element from 
             the dictionary
                    If Symbol is not 
             found - KeyError exception is raised
        
        pop(self: ExtendedDictionary[T], symbol: Symbol, default_value: T) -> T
        
            Removes and returns an element from a dictionary 
             having the given Symbol.
        
        
            symbol: Key which is to be searched for removal
            default_value: Value which is to be returned when the Symbol is 
             not in the dictionary
        
            Returns: If Symbol is found - removed/popped element from 
             the dictionary
                    If Symbol is not 
             found - value specified as the second 
             argument(default)
        """
        pass

    def popitem(self):
        """
        popitem(self: ExtendedDictionary[T]) -> PyTuple
        
            Returns and removes an arbitrary element (Symbol, 
             value) pair from the dictionary.
        
            Returns: Returns an arbitrary element (Symbol, value) pair 
             from the dictionary
                    removes an 
             arbitrary element(the same element which is 
             returned) from the dictionary.
                    Note: 
             Arbitrary elements and random elements are not 
             same.The popitem() doesn't return a random 
             element.
        """
        pass

    def Remove(self, symbol):
        """
        Remove(self: ExtendedDictionary[T], symbol: Symbol) -> bool
        
            Removes the value with the specified Symbol
        
            symbol: The Symbol object of the element to remove.
            Returns: true if the element is successfully found and 
             removed; otherwise, false.
        """
        pass

    def setdefault(self, symbol, default_value=None):
        """
        setdefault(self: ExtendedDictionary[T], symbol: Symbol) -> T
        
            Returns the value of a Symbol (if the Symbol is 
             in dictionary). If not, it inserts Symbol with a 
             value to the dictionary.
        
        
            symbol: Key with null/None value is inserted to the 
             dictionary if Symbol is not in the dictionary.
        
            Returns: The value of the Symbol if it is in the 
             dictionary
                    None if Symbol is not in 
             the dictionary
        
        setdefault(self: ExtendedDictionary[T], symbol: Symbol, default_value: T) -> T
        
            Returns the value of a Symbol (if the Symbol is 
             in dictionary). If not, it inserts Symbol with a 
             value to the dictionary.
        
        
            symbol: Key with a value default_value is inserted to the 
             dictionary if Symbol is not in the dictionary.
        
            default_value: Default value
            Returns: The value of the Symbol if it is in the 
             dictionary
                    default_value if Symbol 
             is not in the dictionary and default_value is 
             specified
        """
        pass

    def TryGetValue(self, symbol, value):
        """ TryGetValue(self: ExtendedDictionary[T], symbol: Symbol) -> (bool, T) """
        pass

    def update(self, other):
        """
        update(self: ExtendedDictionary[T], other: PyObject)
            Updates the dictionary with the elements from the 
             another dictionary object or from an iterable of 
             Symbol/value pairs.
                    The update() 
             method adds element(s) to the dictionary if the 
             Symbol is not in the dictionary.If the Symbol is 
             in the dictionary, it updates the Symbol with the 
             new value.
        
        
            other: Takes either a dictionary or an iterable object 
             of Symbol/value pairs (generally tuples).
        """
        pass

    def values(self):
        """
        values(self: ExtendedDictionary[T]) -> PyList
        
            Returns a view object that displays a list of all 
             the values in the dictionary.
        
            Returns: Returns a view object that displays a list of all 
             values in a given dictionary.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        pass

    GetKeys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.Generic.ICollection containing the Symbol objects of the System.Collections.Generic.IDictionary.

"""

    GetValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.Generic.ICollection containing the values in the System.Collections.Generic.IDictionary.

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Collections.IDictionary object is read-only.

Get: IsReadOnly(self: ExtendedDictionary[T]) -> bool

"""



class Extensions(object):
    """ Extensions function collections - group all static extensions functions here. """
    @staticmethod
    def Add(dictionary, key, *__args):
        """
        Add[(TKey, TElement, TCollection)](dictionary: IDictionary[TKey, TCollection], key: TKey, element: TElement)Add(dictionary: Ticks, key: Symbol, tick: Tick)
            Adds the specified Tick to the Ticks collection. 
             If an entry does not exist for the specified key 
             then one will be created.
        
        
            dictionary: The ticks dictionary
            key: The symbol
            tick: The tick to add
        """
        pass

    @staticmethod
    def AddOrUpdate(dictionary, key, *__args):
        """ AddOrUpdate[(K, V)](dictionary: ConcurrentDictionary[K, V], key: K, value: V)AddOrUpdate[(TKey, TValue)](dictionary: ConcurrentDictionary[TKey, Lazy[TValue]], key: TKey, addValueFactory: Func[TKey, TValue], updateValueFactory: Func[TKey, TValue, TValue]) -> TValue """
        pass

    @staticmethod
    def Batch(resultPackets):
        """ Batch(resultPackets: List[AlphaResultPacket]) -> AlphaResultPacket """
        pass

    @staticmethod
    def BatchBy(enumerable, batchSize):
        """ BatchBy[T](enumerable: IEnumerable[T], batchSize: int) -> IEnumerable[List[T]] """
        pass

    @staticmethod
    def Clear(queue):
        """ Clear[T](queue: ConcurrentQueue[T]) """
        pass

    @staticmethod
    def ConvertFromUtc(time, to, strict):
        """
        ConvertFromUtc(time: DateTime, to: DateTimeZone, strict: bool) -> DateTime
        
            Converts the specified time from UTC to the to 
             time zone
        
        
            time: The time to be converted expressed in UTC
            to: The destinatio time zone
            strict: True for strict conversion, this will throw 
             during ambiguitities, false for lenient 
             conversion
        
            Returns: The time in terms of the to time zone
        """
        pass

    @staticmethod
    def ConvertTo(*__args):
        """
        ConvertTo(time: DateTime, from: DateTimeZone, to: DateTimeZone, strict: bool) -> DateTime
        
            Converts the specified time from the from time 
             zone to the to time zone
        
        
            time: The time to be converted in terms of the from 
             time zone
        
            from: The time zone the specified time is in
            to: The time zone to be converted to
            strict: True for strict conversion, this will throw 
             during ambiguitities, false for lenient 
             conversion
        
            Returns: The time in terms of the to time zone
        ConvertTo[T](value: str) -> T
        ConvertTo(value: str, type: Type) -> object
        
            Converts the specified string value into the 
             specified type
        
        
            value: The string value to be converted
            type: The output type
            Returns: The converted value
        """
        pass

    @staticmethod
    def ConvertToDelegate(pyObject):
        """ ConvertToDelegate[T](pyObject: PyObject) -> T """
        pass

    @staticmethod
    def ConvertToDictionary(pyObject):
        """ ConvertToDictionary[(TKey, TValue)](pyObject: PyObject) -> Dictionary[TKey, TValue] """
        pass

    @staticmethod
    def ConvertToSymbolEnumerable(pyObject):
        """
        ConvertToSymbolEnumerable(pyObject: PyObject) -> IEnumerable[Symbol]
        
            Gets Enumerable of QuantConnect.Symbol from a 
             PyObject
        
        
            pyObject: PyObject containing Symbol or Array of Symbol
            Returns: Enumerable of Symbol
        """
        pass

    @staticmethod
    def ConvertToUniverseSelectionStringDelegate(selector):
        """ ConvertToUniverseSelectionStringDelegate[T](selector: Func[T, object]) -> Func[T, IEnumerable[str]] """
        pass

    @staticmethod
    def ConvertToUniverseSelectionSymbolDelegate(selector):
        """ ConvertToUniverseSelectionSymbolDelegate[T](selector: Func[T, object]) -> Func[T, IEnumerable[Symbol]] """
        pass

    @staticmethod
    def ConvertToUtc(time, from, strict):
        """
        ConvertToUtc(time: DateTime, from: DateTimeZone, strict: bool) -> DateTime
        
            Converts the specified time from the from time 
             zone to QuantConnect.TimeZones.Utc
        
        
            time: The time to be converted in terms of the from 
             time zone
        
            from: The time zone the specified time is in
            strict: True for strict conversion, this will throw 
             during ambiguitities, false for lenient 
             conversion
        
            Returns: The time in terms of the to time zone
        """
        pass

    @staticmethod
    def CreateType(pyObject):
        """
        CreateType(pyObject: PyObject) -> Type
        
            Creates a type with a given name, if PyObject is 
             not a CLR type. Otherwise, convert it.
        
        
            pyObject: Python object representing a type.
            Returns: Type object
        """
        pass

    @staticmethod
    def ExchangeRoundDown(dateTime, interval, exchangeHours, extendedMarket):
        """
        ExchangeRoundDown(dateTime: DateTime, interval: TimeSpan, exchangeHours: SecurityExchangeHours, extendedMarket: bool) -> DateTime
        
            Extension method to round a datetime down by a 
             timespan interval until it's
                    within 
             the specified exchange's open hours. This works 
             by first rounding down
                    the specified 
             time using the interval, then producing a bar 
             between that
                    rounded time and the 
             interval plus the rounded time and incrementally 
             walking
                    backwards until the exchange 
             is open
        
        
            dateTime: Time to be rounded down
            interval: Timespan interval to round to.
            exchangeHours: The exchange hours to determine open times
            extendedMarket: True for extended market hours, otherwise false
            Returns: Rounded datetime
        """
        pass

    @staticmethod
    def ExchangeRoundDownInTimeZone(dateTime, interval, exchangeHours, roundingTimeZone, extendedMarket):
        """
        ExchangeRoundDownInTimeZone(dateTime: DateTime, interval: TimeSpan, exchangeHours: SecurityExchangeHours, roundingTimeZone: DateTimeZone, extendedMarket: bool) -> DateTime
        
            Extension method to round a datetime down by a 
             timespan interval until it's
                    within 
             the specified exchange's open hours. The rounding 
             is performed in the
                    specified time 
             zone
        
        
            dateTime: Time to be rounded down
            interval: Timespan interval to round to.
            exchangeHours: The exchange hours to determine open times
            roundingTimeZone: The time zone to perform the rounding in
            extendedMarket: True for extended market hours, otherwise false
            Returns: Rounded datetime
        """
        pass

    @staticmethod
    def GetAndDispose(instance):
        """ GetAndDispose[T](instance: PyObject) -> T """
        pass

    @staticmethod
    def GetBaseDataInstance(type):
        """
        GetBaseDataInstance(type: Type) -> BaseData
        
            Given a type will create a new instance using the 
             parameterless constructor
                    and assert 
             the type implements QuantConnect.Data.BaseData
        """
        pass

    @staticmethod
    def GetBetterTypeName(type):
        """
        GetBetterTypeName(type: Type) -> str
        
            Gets a type's name with the generic parameters 
             filled in the way they would look when
                  
               defined in code, such as converting 
             Dictionary<`1,`2> to Dictionary<string,int>
        
        
            type: The type who's name we seek
            Returns: A better type name
        """
        pass

    @staticmethod
    def GetBytes(str):
        """
        GetBytes(str: str) -> Array[Byte]
        
            Extension method to convert a string into a byte 
             array
        
        
            str: String to convert to bytes.
            Returns: Byte array
        """
        pass

    @staticmethod
    def GetDecimalEpsilon():
        """
        GetDecimalEpsilon() -> Decimal
        
            Gets the smallest positive number that can be 
             added to a decimal instance and return
                  
               a new value that does not == the old value
        """
        pass

    @staticmethod
    def GetEnumString(value, pyObject):
        """
        GetEnumString(value: int, pyObject: PyObject) -> str
        
            Converts the numeric value of one or more 
             enumerated constants to an equivalent enumerated 
             string.
        
        
            value: Numeric value
            pyObject: Python object that encapsulated a Enum Type
            Returns: String that represents the enumerated object
        """
        pass

    @staticmethod
    def GetExtension(str):
        """
        GetExtension(str: str) -> str
        
            Extension method to extract the extension part of 
             this file name if it matches a safe list, or 
             return a ".custom" extension for ones which do 
             not match.
        
        
            str: String we're looking for the extension for.
            Returns: Last 4 character string of string.
        """
        pass

    @staticmethod
    def GetHash(orders):
        """ GetHash(orders: IDictionary[int, Order]) -> int """
        pass

    @staticmethod
    def GetMD5Hash(stream):
        """
        GetMD5Hash(stream: Stream) -> Array[Byte]
        
            Gets the MD5 hash from a stream
        
            stream: The stream to compute a hash for
            Returns: The MD5 hash
        """
        pass

    @staticmethod
    def GetPythonMethod(instance, name):
        """
        GetPythonMethod(instance: PyObject, name: str) -> object
        
            Gets a python method by name
        
            instance: The object instance to search the method in
            name: The name of the method
            Returns: The python method or null if not defined or 
             CSharp implemented
        """
        pass

    @staticmethod
    def GetString(bytes, encoding):
        """
        GetString(bytes: Array[Byte], encoding: Encoding) -> str
        
            Extension method to convert a byte array into a 
             string.
        
        
            bytes: Byte array to convert.
            encoding: The encoding to use for the conversion. Defaults 
             to Encoding.ASCII
        
            Returns: String from bytes.
        """
        pass

    @staticmethod
    def GetStringBetweenChars(value, left, right):
        """
        GetStringBetweenChars(value: str, left: Char, right: Char) -> str
        
            Get the first occurence of a string between two 
             characters from another string
        
        
            value: The original string
            left: Left bound of the substring
            right: Right bound of the substring
            Returns: Substring from original string bounded by the two 
             characters
        """
        pass

    @staticmethod
    def GetZeroPriceMessage(symbol):
        """
        GetZeroPriceMessage(symbol: Symbol) -> str
        
            Extension method to get security price is 0 
             messages for users
        """
        pass

    @staticmethod
    def IsCommonBusinessDay(date):
        """
        IsCommonBusinessDay(date: DateTime) -> bool
        
            Business day here is defined as any day of the 
             week that is not saturday or sunday
        
        
            date: The date to be examined
            Returns: A bool indicating wether the datetime is a 
             weekday or not
        """
        pass

    @staticmethod
    def IsEmpty(*__args):
        """
        IsEmpty(series: Series) -> bool
        
            Returns true if the specified QuantConnect.Series 
             instance holds no QuantConnect.ChartPoint
        
        IsEmpty(chart: Chart) -> bool
        
            Returns if the specified QuantConnect.Chart 
             instance  holds no QuantConnect.Series
                  
               or they are all empty 
             QuantConnect.Extensions.IsEmpty(QuantConnect.Serie
             s)
        """
        pass

    @staticmethod
    def IsNaNOrZero(value):
        """
        IsNaNOrZero(value: float) -> bool
        
            Check if a number is NaN or equal to zero
        
            value: The double value to check
        """
        pass

    @staticmethod
    def IsSubclassOfGeneric(type, possibleSuperType):
        """
        IsSubclassOfGeneric(type: Type, possibleSuperType: Type) -> bool
        
            Checks the specified type to see if it is a 
             subclass of the possibleSuperType. This method 
             will
                    crawl up the inheritance 
             heirarchy to check for equality using generic 
             type definitions (if exists)
        
        
            type: The type to be checked as a subclass of 
             possibleSuperType
        
            possibleSuperType: The possible superclass of type
            Returns: True if type is a subclass of the generic type 
             definition possibleSuperType
        """
        pass

    @staticmethod
    def IsValid(securityType):
        """
        IsValid(securityType: SecurityType) -> bool
        
            Asserts the specified securityType value is valid
        
            securityType: The SecurityType value
            Returns: True if valid security type value
        """
        pass

    @staticmethod
    def LazyToUpper(data):
        """
        LazyToUpper(data: str) -> str
        
            Lazy string to upper implementation.
                    
             Will first verify the string is not already upper 
             and avoid
                    the call to 
             System.String.ToUpper if possible.
        
        
            data: The string to upper
            Returns: The upper string
        """
        pass

    @staticmethod
    def MatchesTypeName(type, typeName):
        """
        MatchesTypeName(type: Type, typeName: str) -> bool
        
            Function used to match a type against a string 
             type name. This function compares on the 
             AssemblyQualfiedName,
                    the FullName, 
             and then just the Name of the type.
        
        
            type: The type to test for a match
            typeName: The name of the type to match
            Returns: True if the specified type matches the type name, 
             false otherwise
        """
        pass

    @staticmethod
    def Move(list, oldIndex, newIndex):
        """ Move[T](list: List[T], oldIndex: int, newIndex: int) """
        pass

    @staticmethod
    def Normalize(input):
        """
        Normalize(input: Decimal) -> Decimal
        
            Will remove any trailing zeros for the provided 
             decimal input
        
        
            input: The System.Decimal to remove trailing zeros from
            Returns: Provided input with no trailing zeros
        """
        pass

    @staticmethod
    def NormalizeToStr(input):
        """
        NormalizeToStr(input: Decimal) -> str
        
            Will remove any trailing zeros for the provided 
             decimal and convert to string.
                    Uses 
             QuantConnect.Extensions.Normalize(System.Decimal).
        
        
            input: The System.Decimal to convert to System.String
            Returns: Input converted to System.String with no trailing 
             zeros
        """
        pass

    @staticmethod
    def OrderTargetsByMarginImpact(targets, algorithm, targetIsDelta):
        """ OrderTargetsByMarginImpact(targets: IEnumerable[IPortfolioTarget], algorithm: IAlgorithm, targetIsDelta: bool) -> IEnumerable[IPortfolioTarget] """
        pass

    @staticmethod
    def ProcessUntilEmpty(collection, handler):
        """ ProcessUntilEmpty[T](collection: IProducerConsumerCollection[T], handler: Action[T]) """
        pass

    @staticmethod
    def RemoveFromEnd(s, ending):
        """
        RemoveFromEnd(s: str, ending: str) -> str
        
            Returns a new string in which specified ending in 
             the current instance is removed.
        
        
            s: original string value
            ending: the string to be removed
        """
        pass

    @staticmethod
    def Reset(timer):
        """
        Reset(timer: Timer)
            Add the reset method to the System.Timer class.
        
            timer: System.timer object
        """
        pass

    @staticmethod
    def ResolutionToLower(resolution):
        """
        ResolutionToLower(resolution: Resolution) -> str
        
            Converts the specified resolution value to its 
             corresponding lower-case string representation
        
        
            resolution: The resolution value
            Returns: A lower-case string representation of the 
             specified resolution value
        """
        pass

    @staticmethod
    def Round(*__args):
        """
        Round(time: TimeSpan, roundingInterval: TimeSpan, roundingType: MidpointRounding) -> TimeSpan
        
            Extension method to round a timeSpan to nearest 
             timespan period.
        
        
            time: TimeSpan To Round
            roundingInterval: Rounding Unit
            roundingType: Rounding method
            Returns: Rounded timespan
        Round(time: TimeSpan, roundingInterval: TimeSpan) -> TimeSpan
        
            Extension method to round timespan to nearest 
             timespan period.
        
        
            time: Base timespan we're looking to round.
            roundingInterval: Timespan period we're rounding.
            Returns: Rounded timespan period
        Round(datetime: DateTime, roundingInterval: TimeSpan) -> DateTime
        
            Extension method to round a datetime to the 
             nearest unit timespan.
        
        
            datetime: Datetime object we're rounding.
            roundingInterval: Timespan rounding period.
            Returns: Rounded datetime
        """
        pass

    @staticmethod
    def RoundDown(dateTime, interval):
        """
        RoundDown(dateTime: DateTime, interval: TimeSpan) -> DateTime
        
            Extension method to round a datetime down by a 
             timespan interval.
        
        
            dateTime: Base DateTime object we're rounding down.
            interval: Timespan interval to round to.
            Returns: Rounded datetime
        """
        pass

    @staticmethod
    def RoundDownInTimeZone(dateTime, roundingInterval, sourceTimeZone, roundingTimeZone):
        """
        RoundDownInTimeZone(dateTime: DateTime, roundingInterval: TimeSpan, sourceTimeZone: DateTimeZone, roundingTimeZone: DateTimeZone) -> DateTime
        
            Rounds the specified date time in the specified 
             time zone. Careful with calling this method in a 
             loop while modifying dateTime, check unit tests.
        
        
            dateTime: Date time to be rounded
            roundingInterval: Timespan rounding period
            sourceTimeZone: Time zone of the date time
            roundingTimeZone: Time zone in which the rounding is performed
            Returns: The rounded date time in the source time zone
        """
        pass

    @staticmethod
    def RoundToSignificantDigits(d, digits):
        """
        RoundToSignificantDigits(d: float, digits: int) -> float
        
            Extension method to round a double value to a 
             fixed number of significant figures instead of a 
             fixed decimal places.
        
        
            d: Double we're rounding
            digits: Number of significant figures
            Returns: New double rounded to digits-significant figures
        RoundToSignificantDigits(d: Decimal, digits: int) -> Decimal
        
            Extension method to round a double value to a 
             fixed number of significant figures instead of a 
             fixed decimal places.
        
        
            d: Double we're rounding
            digits: Number of significant figures
            Returns: New double rounded to digits-significant figures
        """
        pass

    @staticmethod
    def RoundUp(time, d):
        """
        RoundUp(time: DateTime, d: TimeSpan) -> DateTime
        
            Extension method to explicitly round up to the 
             nearest timespan interval.
        
        
            time: Base datetime object to round up.
            d: Timespan interval for rounding
            Returns: Rounded datetime
        """
        pass

    @staticmethod
    def SafeDecimalCast(input):
        """
        SafeDecimalCast(input: float) -> Decimal
        
            Casts the specified input value to a decimal 
             while acknowledging the overflow conditions
        
        
            input: The value to be cast
            Returns: The input value as a decimal, if the value is too 
             large or to small to be represented
                    
             as a decimal, then the closest decimal value will 
             be returned
        """
        pass

    @staticmethod
    def SecurityTypeToLower(securityType):
        """
        SecurityTypeToLower(securityType: SecurityType) -> str
        
            Converts the specified securityType value to its 
             corresponding lower-case string representation
        
        
            securityType: The SecurityType value
            Returns: A lower-case string representation of the 
             specified SecurityType value
        """
        pass

    @staticmethod
    def SingleOrAlgorithmTypeName(names, algorithmTypeName):
        """ SingleOrAlgorithmTypeName(names: List[str], algorithmTypeName: str) -> str """
        pass

    @staticmethod
    def SmartRounding(input):
        """
        SmartRounding(input: Decimal) -> Decimal
        
            Provides global smart rounding, numbers larger 
             than 1000 will round to 4 decimal places,
               
                  while numbers smaller will round to 7 
             significant digits
        """
        pass

    @staticmethod
    def StopSafely(thread, timeout, token):
        """
        StopSafely(thread: Thread, timeout: TimeSpan, token: CancellationTokenSource)
            Helper method to safely stop a running thread
        
            thread: The thread to stop
            timeout: The timeout to wait till the thread ends after 
             which abort will be called
        
            token: Cancellation token source to use if any
        """
        pass

    @staticmethod
    def SynchronouslyAwaitTask(task):
        """
        SynchronouslyAwaitTask(task: Task)
            Safely blocks until the specified task has 
             completed executing
        
        
            task: The task to be awaited
            Returns: The result of the task
        """
        pass

    @staticmethod
    def SynchronouslyAwaitTaskResult(task):
        """ SynchronouslyAwaitTaskResult[TResult](task: Task[TResult]) -> TResult """
        pass

    @staticmethod
    def TickTypeToLower(tickType):
        """
        TickTypeToLower(tickType: TickType) -> str
        
            Converts the specified tickType value to its 
             corresponding lower-case string representation
        
        
            tickType: The tickType value
            Returns: A lower-case string representation of the 
             specified tickType value
        """
        pass

    @staticmethod
    def ToCamelCase(value):
        """
        ToCamelCase(value: str) -> str
        
            Converts the provided string into camel case 
             notation
        """
        pass

    @staticmethod
    def ToCsv(str, size):
        """
        ToCsv(str: str, size: int) -> List[str]
        
            Breaks the specified string into csv components, 
             all commas are considered separators
        
        
            str: The string to be broken into csv
            size: The expected size of the output list
            Returns: A list of the csv pieces
        """
        pass

    @staticmethod
    def ToCsvData(str, size, delimiter):
        """
        ToCsvData(str: str, size: int, delimiter: Char) -> List[str]
        
            Breaks the specified string into csv components, 
             works correctly with commas in data fields
        
        
            str: The string to be broken into csv
            size: The expected size of the output list
            delimiter: The delimiter used to separate entries in the line
            Returns: A list of the csv pieces
        """
        pass

    @staticmethod
    def ToDecimal(str):
        """
        ToDecimal(str: str) -> Decimal
        
            Extension method for faster string to decimal 
             conversion.
        
        
            str: String to be converted to positive decimal value
            Returns: Decimal value of the string
        """
        pass

    @staticmethod
    def ToDecimalAllowExponent(str):
        """
        ToDecimalAllowExponent(str: str) -> Decimal
        
            Extension method for string to decimal conversion 
             where string can represent a number with exponent 
             xe-y
        
        
            str: String to be converted to decimal value
            Returns: Decimal value of the string
        """
        pass

    @staticmethod
    def ToFunc(dateRule):
        """
        ToFunc(dateRule: IDateRule) -> Func[DateTime, Nullable[DateTime]]
        
            Converts a date rule into a function that 
             receives current time
                    and returns 
             the next date.
        
        
            dateRule: The date rule to convert
            Returns: A function that will enumerate the provided date 
             rules
        """
        pass

    @staticmethod
    def ToHigherResolutionEquivalent(timeSpan, requireExactMatch):
        """
        ToHigherResolutionEquivalent(timeSpan: TimeSpan, requireExactMatch: bool) -> Resolution
        
            Converts the specified time span into a 
             resolution enum value. If an exact match
                
                 is not found and `requireExactMatch` is 
             false, then the higher resoluion will be
                
                 returned. For example, timeSpan=5min will 
             return Minute resolution.
        
        
            timeSpan: The time span to convert to resolution
            requireExactMatch: True to throw an exception if an exact match is 
             not found
        
            Returns: The resolution
        """
        pass

    @staticmethod
    def ToInt32(str):
        """
        ToInt32(str: str) -> int
        
            Extension method for faster string to Int32 
             conversion.
        
        
            str: String to be converted to positive Int32 value
            Returns: Int32 value of the string
        """
        pass

    @staticmethod
    def ToInt64(str):
        """
        ToInt64(str: str) -> Int64
        
            Extension method for faster string to Int64 
             conversion.
        
        
            str: String to be converted to positive Int64 value
            Returns: Int32 value of the string
        """
        pass

    @staticmethod
    def ToLower(enum):
        """
        ToLower(enum: Enum) -> str
        
            Converts the specified enum value to its 
             corresponding lower-case string representation
        
        
            enum: The enumeration value
            Returns: A lower-case string representation of the 
             specified enumeration value
        """
        pass

    @staticmethod
    def ToMD5(str):
        """
        ToMD5(str: str) -> str
        
            Extension method to convert a string to a MD5 
             hash.
        
        
            str: String we want to MD5 encode.
            Returns: MD5 hash of a string
        """
        pass

    @staticmethod
    def ToOrderTicket(order, transactionManager):
        """
        ToOrderTicket(order: Order, transactionManager: SecurityTransactionManager) -> OrderTicket
        
            Turn order into an order ticket
        
            order: The QuantConnect.Orders.Order being converted
            transactionManager: The transaction manager, 
             QuantConnect.Securities.SecurityTransactionManager
        """
        pass

    @staticmethod
    def ToPyList(enumerable):
        """
        ToPyList(enumerable: IEnumerable) -> PyList
        
            Converts an IEnumerable to a PyList
        
            enumerable: IEnumerable object to convert
            Returns: PyList
        """
        pass

    @staticmethod
    def ToSafeString(pyObject):
        """
        ToSafeString(pyObject: PyObject) -> str
        
            Returns a System.String that represents the 
             current Python.Runtime.PyObject
        
        
            pyObject: The Python.Runtime.PyObject being converted
            Returns: string that represents the current PyObject
        """
        pass

    @staticmethod
    def ToSHA256(data):
        """
        ToSHA256(data: str) -> str
        
            Encrypt the token:time data to make our API hash.
        
            data: Data to be hashed by SHA256
            Returns: Hashed string.
        """
        pass

    @staticmethod
    def ToStream(str):
        """
        ToStream(str: str) -> Stream
        
            Extension method to convert strings to stream to 
             be read.
        
        
            str: String to convert to stream
            Returns: Stream instance
        """
        pass

    @staticmethod
    def ToStringPerformance(optionRight):
        """
        ToStringPerformance(optionRight: OptionRight) -> str
        
            Converts the specified optionRight value to its 
             corresponding string representation
        
        
            optionRight: The optionRight value
            Returns: A string representation of the specified 
             OptionRight value
        """
        pass

    @staticmethod
    def ToTimeSpan(resolution):
        """
        ToTimeSpan(resolution: Resolution) -> TimeSpan
        
            Converts the Resolution instance into a TimeSpan 
             instance
        
        
            resolution: The resolution to be converted
            Returns: A TimeSpan instance that represents the 
             resolution specified
        """
        pass

    @staticmethod
    def TruncateTo3DecimalPlaces(value):
        """
        TruncateTo3DecimalPlaces(value: Decimal) -> Decimal
        
            Will truncate the provided decimal, without 
             rounding, to 3 decimal places
        
        
            value: The value to truncate
            Returns: New instance with just 3 decimal places
        """
        pass

    @staticmethod
    def TryConvert(pyObject, result, allowPythonDerivative):
        """ TryConvert[T](pyObject: PyObject, allowPythonDerivative: bool) -> (bool, T) """
        pass

    @staticmethod
    def TryConvertToDelegate(pyObject, result):
        """ TryConvertToDelegate[T](pyObject: PyObject) -> (bool, T) """
        pass

    @staticmethod
    def WaitOne(waitHandle, *__args):
        """
        WaitOne(waitHandle: WaitHandle, cancellationToken: CancellationToken) -> bool
        
            Blocks the current thread until the current 
             System.Threading.WaitHandle receives a signal, 
             while observing a 
             System.Threading.CancellationToken.
        
        
            waitHandle: The wait handle to wait on
            cancellationToken: The System.Threading.CancellationToken to observe.
        WaitOne(waitHandle: WaitHandle, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool
        
            Blocks the current thread until the current 
             System.Threading.WaitHandle is set, using a 
             System.TimeSpan to measure the time interval, 
             while observing a 
             System.Threading.CancellationToken.
        
        
            waitHandle: The wait handle to wait on
            timeout: A System.TimeSpan that represents the number of 
             milliseconds to wait, or a System.TimeSpan that 
             represents -1 milliseconds to wait indefinitely.
        
            cancellationToken: The System.Threading.CancellationToken to observe.
            Returns: true if the System.Threading.WaitHandle was set; 
             otherwise, false.
        
        WaitOne(waitHandle: WaitHandle, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
        
            Blocks the current thread until the current 
             System.Threading.WaitHandle is set, using a 
             32-bit signed integer to measure the time 
             interval, while observing a 
             System.Threading.CancellationToken.
        
        
            waitHandle: The wait handle to wait on
            millisecondsTimeout: The number of milliseconds to wait, or 
             System.Threading.Timeout.Infinite(-1) to wait 
             indefinitely.
        
            cancellationToken: The System.Threading.CancellationToken to observe.
            Returns: true if the System.Threading.WaitHandle was set; 
             otherwise, false.
        """
        pass

    @staticmethod
    def WithEmbeddedHtmlAnchors(source):
        """
        WithEmbeddedHtmlAnchors(source: str) -> str
        
            Convert a string into the same string with a URL! 
             :)
        
        
            source: The source string to be converted
            Returns: The same source string but with anchor tags 
             around substrings matching a link regex
        """
        pass

    __all__ = [
        'Add',
        'AddOrUpdate',
        'Batch',
        'BatchBy',
        'Clear',
        'ConvertFromUtc',
        'ConvertTo',
        'ConvertToDelegate',
        'ConvertToDictionary',
        'ConvertToSymbolEnumerable',
        'ConvertToUniverseSelectionStringDelegate',
        'ConvertToUniverseSelectionSymbolDelegate',
        'ConvertToUtc',
        'CreateType',
        'ExchangeRoundDown',
        'ExchangeRoundDownInTimeZone',
        'GetAndDispose',
        'GetBaseDataInstance',
        'GetBetterTypeName',
        'GetBytes',
        'GetDecimalEpsilon',
        'GetEnumString',
        'GetExtension',
        'GetHash',
        'GetMD5Hash',
        'GetPythonMethod',
        'GetString',
        'GetStringBetweenChars',
        'GetZeroPriceMessage',
        'IsCommonBusinessDay',
        'IsEmpty',
        'IsNaNOrZero',
        'IsSubclassOfGeneric',
        'IsValid',
        'LazyToUpper',
        'MatchesTypeName',
        'Move',
        'Normalize',
        'NormalizeToStr',
        'OrderTargetsByMarginImpact',
        'ProcessUntilEmpty',
        'RemoveFromEnd',
        'Reset',
        'ResolutionToLower',
        'Round',
        'RoundDown',
        'RoundDownInTimeZone',
        'RoundToSignificantDigits',
        'RoundUp',
        'SafeDecimalCast',
        'SecurityTypeToLower',
        'SingleOrAlgorithmTypeName',
        'SmartRounding',
        'StopSafely',
        'SynchronouslyAwaitTask',
        'SynchronouslyAwaitTaskResult',
        'TickTypeToLower',
        'ToCamelCase',
        'ToCsv',
        'ToCsvData',
        'ToDecimal',
        'ToDecimalAllowExponent',
        'ToFunc',
        'ToHigherResolutionEquivalent',
        'ToInt32',
        'ToInt64',
        'ToLower',
        'ToMD5',
        'ToOrderTicket',
        'ToPyList',
        'ToSafeString',
        'ToSHA256',
        'ToStream',
        'ToStringPerformance',
        'ToTimeSpan',
        'TruncateTo3DecimalPlaces',
        'TryConvert',
        'TryConvertToDelegate',
        'WaitOne',
        'WithEmbeddedHtmlAnchors',
    ]


class Field(object):
    """ Provides static properties to be used as selectors with the indicator system """
    def Average(self, *args): #cannot find CLR method
        """ Func[IBaseData, Decimal](object: object, method: IntPtr) """
        pass

    def Close(self, *args): #cannot find CLR method
        """ Func[IBaseData, Decimal](object: object, method: IntPtr) """
        pass

    def High(self, *args): #cannot find CLR method
        """ Func[IBaseData, Decimal](object: object, method: IntPtr) """
        pass

    def Low(self, *args): #cannot find CLR method
        """ Func[IBaseData, Decimal](object: object, method: IntPtr) """
        pass

    def Median(self, *args): #cannot find CLR method
        """ Func[IBaseData, Decimal](object: object, method: IntPtr) """
        pass

    def Open(self, *args): #cannot find CLR method
        """ Func[IBaseData, Decimal](object: object, method: IntPtr) """
        pass

    def SevenBar(self, *args): #cannot find CLR method
        """ Func[IBaseData, Decimal](object: object, method: IntPtr) """
        pass

    def Typical(self, *args): #cannot find CLR method
        """ Func[IBaseData, Decimal](object: object, method: IntPtr) """
        pass

    def Volume(self, *args): #cannot find CLR method
        """ Func[IBaseData, Decimal](object: object, method: IntPtr) """
        pass

    def Weighted(self, *args): #cannot find CLR method
        """ Func[IBaseData, Decimal](object: object, method: IntPtr) """
        pass

    __all__ = []


class Globals(object):
    """ Provides application level constant values """
    @staticmethod
    def Reset():
        """
        Reset()
            Resets global values with the Config data.
        """
        pass

    Cache = './cache/data'
    CacheDataFolder = '../../../Data/'
    DataFolder = '../../../Data/'
    Version = '2.4.0.0'
    __all__ = [
        'Cache',
        'Reset',
    ]


class Holding(object):
    """
    Singular holding of assets from backend live nodes:
    
    Holding()
    Holding(security: Security)
    """
    def Clone(self):
        """
        Clone(self: Holding) -> Holding
        
            Clones this instance
            Returns: A new Holding object with the same values as this 
             one
        """
        pass

    def ToString(self):
        """
        ToString(self: Holding) -> str
        
            Writes out the properties of this instance to 
             string
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, security=None):
        """
        __new__(cls: type)
        __new__(cls: type, security: Security)
        """
        pass

    AveragePrice = None
    ConversionRate = None
    CurrencySymbol = None
    MarketPrice = None
    MarketValue = None
    Quantity = None
    Symbol = None
    Type = None
    UnrealizedPnL = None


class IIsolatorLimitResultProvider:
    """
    Provides an abstraction for managing isolator limit results.
                This is originally intended to be used by the training feature to permit a single
                algorithm time loop to extend past the default of ten minutes
    """
    def IsWithinLimit(self):
        """
        IsWithinLimit(self: IIsolatorLimitResultProvider) -> IsolatorLimitResult
        
            Determines whether or not a custom isolator limit 
             has be reached.
        """
        pass

    def RequestAdditionalTime(self, minutes):
        """
        RequestAdditionalTime(self: IIsolatorLimitResultProvider, minutes: int)
            Requests additional time from the isolator result 
             provider. This is intended
                    to 
             prevent 
             QuantConnect.IIsolatorLimitResultProvider.IsWithin
             Limit from returning an error result.
                   
              This method will throw a System.TimeoutException 
             if there is insufficient
                    resources 
             available to fulfill the specified number of 
             minutes.
        
        
            minutes: The number of additional minutes to request
        """
        pass

    def TryRequestAdditionalTime(self, minutes):
        """
        TryRequestAdditionalTime(self: IIsolatorLimitResultProvider, minutes: int) -> bool
        
            Attempts to request additional time from the 
             isolator result provider. This is intended
              
                   to prevent 
             QuantConnect.IIsolatorLimitResultProvider.IsWithin
             Limit from returning an error result.
                   
              This method will only return false if there is 
             insufficient resources available to fulfill
             
                    the specified number of minutes.
        
        
            minutes: The number of additional minutes to request
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InvalidConfigurationDetectedEventArgs(EventArgs):
    """
    Event arguments for the QuantConnect.Interfaces.IDataProviderEvents.InvalidConfigurationDetected event
    
    InvalidConfigurationDetectedEventArgs(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, message):
        """ __new__(cls: type, message: str) """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error message

Get: Message(self: InvalidConfigurationDetectedEventArgs) -> str

"""



class Isolator(object):
    """
    Isolator class - create a new instance of the algorithm and ensure it doesn't
                exceed memory or time execution limits.
    
    Isolator()
    """
    def ExecuteWithTimeLimit(self, timeSpan, *__args):
        """
        ExecuteWithTimeLimit(self: Isolator, timeSpan: TimeSpan, withinCustomLimits: Func[IsolatorLimitResult], codeBlock: Action, memoryCap: Int64, sleepIntervalMillis: int, workerThread: WorkerThread) -> bool
        ExecuteWithTimeLimit(self: Isolator, timeSpan: TimeSpan, codeBlock: Action, memoryCap: Int64, sleepIntervalMillis: int, workerThread: WorkerThread) -> bool
        
            Execute a code block with a maximum limit on time 
             and memory.
        
        
            timeSpan: Timeout in timespan
            codeBlock: Action codeblock to execute
            memoryCap: Maximum memory allocation, default 1024Mb
            sleepIntervalMillis: Sleep interval between each check in ms
            workerThread: The worker thread instance that will execute the 
             provided action, if null
                    will use a 
             System.Threading.Tasks.Task
        
            Returns: True if algorithm exited successfully, false if 
             cancelled because it exceeded limits.
        """
        pass

    CancellationToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Algo cancellation controls - cancellation token for algorithm thread.

Get: CancellationToken(self: Isolator) -> CancellationToken

"""

    CancellationTokenSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Algo cancellation controls - cancel source.

Get: CancellationTokenSource(self: Isolator) -> CancellationTokenSource

"""

    IsCancellationRequested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check if this task isolator is cancelled, and exit the analysis

Get: IsCancellationRequested(self: Isolator) -> bool

"""



class IsolatorLimitResult(object):
    """
    Represents the result of the QuantConnect.Isolator limiter callback
    
    IsolatorLimitResult(currentTimeStepElapsed: TimeSpan, errorMessage: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, currentTimeStepElapsed, errorMessage):
        """ __new__(cls: type, currentTimeStepElapsed: TimeSpan, errorMessage: str) """
        pass

    CurrentTimeStepElapsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of time spent on the current time step

Get: CurrentTimeStepElapsed(self: IsolatorLimitResult) -> TimeSpan

"""

    ErrorMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error message or an empty string if no error on the current time step

Get: ErrorMessage(self: IsolatorLimitResult) -> str

"""

    IsWithinCustomLimits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if there are no errors in the current time step

Get: IsWithinCustomLimits(self: IsolatorLimitResult) -> bool

"""



class IsolatorLimitResultProvider(object):
    """ Provides access to the QuantConnect.IsolatorLimitResultProvider.NullIsolatorLimitResultProvider and extension methods supporting QuantConnect.Scheduling.ScheduledEvent """
    @staticmethod
    def Consume(isolatorLimitProvider, *__args):
        """
        Consume(isolatorLimitProvider: IIsolatorLimitResultProvider, scheduledEvent: ScheduledEvent, scanTimeUtc: DateTime, timeMonitor: TimeMonitor)
            Convenience method for invoking a scheduled 
             event's Scan method inside the 
             QuantConnect.IsolatorLimitResultProvider
        
        Consume(isolatorLimitProvider: IIsolatorLimitResultProvider, timeProvider: ITimeProvider, code: Action, timeMonitor: TimeMonitor)
            Executes the provided code block and while the 
             code block is running, continually consume from
         
                        the limit result provided one token 
             each minute. This function allows the code to run 
             for the
                    first full minute without 
             requesting additional time from the provider. 
             Following that, every
                    minute an 
             additional one minute will be requested from the 
             provider.
        """
        pass

    Null = None
    __all__ = [
        'Consume',
        'Null',
    ]


class ITimeProvider:
    """
    Provides access to the current time in UTC. This doesn't necessarily
                need to be wall-clock time, but rather the current time in some system
    """
    def GetUtcNow(self):
        """
        GetUtcNow(self: ITimeProvider) -> DateTime
        
            Gets the current time in UTC
            Returns: The current time in UTC
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Language(Enum, IComparable, IFormattable, IConvertible):
    """
    Multilanguage support enum: which language is this project for the interop bridge converter.
    
    enum Language, values: CSharp (0), FSharp (1), Java (3), Python (4), VisualBasic (2)
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

    CSharp = None
    FSharp = None
    Java = None
    Python = None
    value__ = None
    VisualBasic = None


class LocalTimeKeeper(object):
    """
    Represents the current local time. This object is created via the QuantConnect.TimeKeeper to
                manage conversions to local time.
    """
    LocalTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current time in terms of the QuantConnect.LocalTimeKeeper.TimeZone

Get: LocalTime(self: LocalTimeKeeper) -> DateTime

"""

    TimeZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time zone of this QuantConnect.LocalTimeKeeper

Get: TimeZone(self: LocalTimeKeeper) -> DateTimeZone

"""


    TimeUpdated = None


class Market(object):
    """ Markets Collection: Soon to be expanded to a collection of items specifying the market hour, timezones and country codes. """
    @staticmethod
    def Add(market, identifier):
        """
        Add(market: str, identifier: int)
            Adds the specified market to the map of available 
             markets with the specified identifier.
        
        
            market: The market string to add
            identifier: The identifier for the market, this value must be 
             positive and less than 1000
        """
        pass

    @staticmethod
    def Decode(code):
        """
        Decode(code: int) -> str
        
            Gets the market string for the specified market 
             code.
        
        
            code: The market code to be decoded
            Returns: The string representation of the market, or null 
             if not found
        """
        pass

    @staticmethod
    def Encode(market):
        """
        Encode(market: str) -> Nullable[int]
        
            Gets the market code for the specified market. 
             Returns null if the market is not found
        
        
            market: The market to check for (case sensitive)
            Returns: The internal code used for the market. 
             Corresponds to the value used when calling 
             QuantConnect.Market.Add(System.String,System.Int32
             )
        """
        pass

    Binance = 'binance'
    Bitfinex = 'bitfinex'
    Bithumb = 'bithumb'
    Bitstamp = 'bitstamp'
    Bittrex = 'bittrex'
    CBOE = 'cboe'
    CBOT = 'cbot'
    CME = 'cme'
    Coinone = 'coinone'
    COMEX = 'comex'
    Dukascopy = 'dukascopy'
    FXCM = 'fxcm'
    GDAX = 'gdax'
    Globex = 'cmeglobex'
    HitBTC = 'hitbtc'
    HKFE = 'hkfe'
    ICE = 'ice'
    Kraken = 'kraken'
    NSE = 'nse'
    NYMEX = 'nymex'
    Oanda = 'oanda'
    OkCoin = 'okcoin'
    Poloniex = 'poloniex'
    SGX = 'sgx'
    USA = 'usa'
    __all__ = [
        'Add',
        'Binance',
        'Bitfinex',
        'Bithumb',
        'Bitstamp',
        'Bittrex',
        'CBOE',
        'CBOT',
        'CME',
        'Coinone',
        'COMEX',
        'Decode',
        'Dukascopy',
        'Encode',
        'FXCM',
        'GDAX',
        'Globex',
        'HitBTC',
        'HKFE',
        'ICE',
        'Kraken',
        'NSE',
        'NYMEX',
        'Oanda',
        'OkCoin',
        'Poloniex',
        'SGX',
        'USA',
    ]


class MarketCodes(object):
    """ Global Market Short Codes and their full versions: (used in tick objects) """
    Canada = None
    US = None
    __all__ = []


class MarketDataType(Enum, IComparable, IFormattable, IConvertible):
    """
    Market data style: is the market data a summary (OHLC style) bar, or is it a time-price value.
    
    enum MarketDataType, values: Auxiliary (3), Base (0), FuturesChain (6), OptionChain (5), QuoteBar (4), Tick (2), TradeBar (1)
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

    Auxiliary = None
    Base = None
    FuturesChain = None
    OptionChain = None
    QuoteBar = None
    Tick = None
    TradeBar = None
    value__ = None


class NewTradableDateEventArgs(EventArgs):
    """
    Event arguments for the NewTradableDate event
    
    NewTradableDateEventArgs(date: DateTime, lastBaseData: BaseData, symbol: Symbol)
    """
    @staticmethod # known case of __new__
    def __new__(self, date, lastBaseData, symbol):
        """ __new__(cls: type, date: DateTime, lastBaseData: BaseData, symbol: Symbol) """
        pass

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The new tradable date

Get: Date(self: NewTradableDateEventArgs) -> DateTime

"""

    LastBaseData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The last QuantConnect.Data.BaseData of the QuantConnect.Securities.Security
            for which we are enumerating

Get: LastBaseData(self: NewTradableDateEventArgs) -> BaseData

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The QuantConnect.NewTradableDateEventArgs.Symbol of the new tradable date

Get: Symbol(self: NewTradableDateEventArgs) -> Symbol

"""



class NumericalPrecisionLimitedEventArgs(EventArgs):
    """
    Event arguments for the QuantConnect.Interfaces.IDataProviderEvents.NumericalPrecisionLimited event
    
    NumericalPrecisionLimitedEventArgs(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, message):
        """ __new__(cls: type, message: str) """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error message

Get: Message(self: NumericalPrecisionLimitedEventArgs) -> str

"""



class OptionRight(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the different types of options
    
    enum OptionRight, values: Call (0), Put (1)
    """
    def Call(self, *args): #cannot find CLR method
        """
        Specifies the different types of options
        
        enum OptionRight, values: Call (0), Put (1)
        """
        pass

    def Put(self, *args): #cannot find CLR method
        """
        Specifies the different types of options
        
        enum OptionRight, values: Call (0), Put (1)
        """
        pass

    def __call__(self, *args): #cannot find CLR method
        """
        Specifies the different types of options
        
        enum OptionRight, values: Call (0), Put (1)
        """
        pass

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

    value__ = None


class OptionStyle(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the style of an option
    
    enum OptionStyle, values: American (0), European (1)
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

    American = None
    European = None
    value__ = None


class OS(object):
    """ Operating systems class for managing anything that is operation system specific. """
    @staticmethod
    def GetServerStatistics():
        """
        GetServerStatistics() -> Dictionary[str, str]
        
            Gets the statistics of the machine, including 
             CPU% and RAM
        """
        pass

    ApplicationMemoryUsed = None
    CpuUsage = None
    DriveSpaceRemaining = None
    DriveSpaceUsed = None
    DriveTotalSpace = None
    IsLinux = False
    IsWindows = True
    PathSeparation = '\\'
    TotalPhysicalMemoryUsed = None
    __all__ = [
        'GetServerStatistics',
    ]


class Parse(object):
    """ Provides methods for parsing strings using System.Globalization.CultureInfo.InvariantCulture """
    @staticmethod
    def DateTime(value):
        """
        DateTime(value: str) -> DateTime
        
            Parses the provided value as a System.DateTime 
             using 
             System.DateTime.Parse(System.String,System.IFormat
             Provider)
                    with 
             System.Globalization.CultureInfo.InvariantCulture
        """
        pass

    @staticmethod
    def DateTimeExact(value, format, dateTimeStyles=None):
        """
        DateTimeExact(value: str, format: str) -> DateTime
        
            Parses the provided value as a System.DateTime 
             using 
             System.DateTime.ParseExact(System.String,System.St
             ring,System.IFormatProvider)
                    with 
             the specified format and 
             System.Globalization.CultureInfo.InvariantCulture
        
        DateTimeExact(value: str, format: str, dateTimeStyles: DateTimeStyles) -> DateTime
        
            Parses the provided value as a System.DateTime 
             using 
             System.DateTime.ParseExact(System.String,System.St
             ring,System.IFormatProvider)
                    with 
             the specified format, dateTimeStyles and 
             System.Globalization.CultureInfo.InvariantCulture
        """
        pass

    @staticmethod
    def Decimal(value, numberStyles=None):
        """
        Decimal(value: str) -> Decimal
        
            Parses the provided value as a System.Decimal 
             using 
             System.Globalization.CultureInfo.InvariantCulture
        
        Decimal(value: str, numberStyles: NumberStyles) -> Decimal
        
            Parses the provided value as a System.Decimal 
             using the specified numberStyles
                    and 
             System.Globalization.CultureInfo.InvariantCulture
        """
        pass

    @staticmethod
    def Double(value):
        """
        Double(value: str) -> float
        
            Parses the provided value as a System.Double 
             using 
             System.Globalization.CultureInfo.InvariantCulture
        """
        pass

    @staticmethod
    def Int(value):
        """
        Int(value: str) -> int
        
            Parses the provided value as a System.Int32 using 
             System.Globalization.CultureInfo.InvariantCulture
        """
        pass

    @staticmethod
    def Long(value, numberStyles=None):
        """
        Long(value: str) -> Int64
        
            Parses the provided value as a System.Int64 using 
             System.Globalization.CultureInfo.InvariantCulture
        
        Long(value: str, numberStyles: NumberStyles) -> Int64
        
            Parses the provided value as a System.Int64 using 
             System.Globalization.CultureInfo.InvariantCulture
             
                    and the specified numberStyles
        """
        pass

    @staticmethod
    def TimeSpan(value):
        """
        TimeSpan(value: str) -> TimeSpan
        
            Parses the provided value as a System.TimeSpan 
             using 
             System.TimeSpan.Parse(System.String,System.IFormat
             Provider)
                    with 
             System.Globalization.CultureInfo.InvariantCulture
        """
        pass

    @staticmethod
    def TryParse(input, *__args):
        """
        TryParse(input: str) -> (bool, TimeSpan)
        
            Tries to parse the provided value with TryParse 
             as a System.TimeSpan using 
             System.Globalization.CultureInfo.InvariantCulture.
        
        TryParse(input: str, dateTimeStyle: DateTimeStyles) -> (bool, DateTime)
        
            Tries to parse the provided value with TryParse 
             as a System.DateTime using the specified 
             dateTimeStyle
                    and 
             System.Globalization.CultureInfo.InvariantCulture.
        
        TryParse(input: str, numberStyle: NumberStyles) -> (bool, float)
        
            Tries to parse the provided value with TryParse 
             as a System.Double using the specified 
             numberStyle
                    and 
             System.Globalization.CultureInfo.InvariantCulture.
        
        TryParse(input: str, numberStyle: NumberStyles) -> (bool, Decimal)
        
            Tries to parse the provided value with TryParse 
             as a System.Decimal using the specified 
             numberStyle
                    and 
             System.Globalization.CultureInfo.InvariantCulture.
        
        TryParse(input: str, numberStyle: NumberStyles) -> (bool, int)
        
            Tries to parse the provided value with TryParse 
             as a System.Int32 using the specified numberStyle
             
                    and 
             System.Globalization.CultureInfo.InvariantCulture.
        
        TryParse(input: str, numberStyle: NumberStyles) -> (bool, Int64)
        
            Tries to parse the provided value with TryParse 
             as a System.Int64 using the specified numberStyle
             
                    and 
             System.Globalization.CultureInfo.InvariantCulture.
        """
        pass

    @staticmethod
    def TryParseExact(input, format, *__args):
        """
        TryParseExact(input: str, format: str, timeSpanStyle: TimeSpanStyles) -> (bool, TimeSpan)
        
            Tries to parse the provided value with TryParse 
             as a System.TimeSpan, format
                    string, 
             System.Globalization.TimeSpanStyles, and using 
             System.Globalization.CultureInfo.InvariantCulture
        
        TryParseExact(input: str, format: str, dateTimeStyle: DateTimeStyles) -> (bool, DateTime)
        
            Tries to parse the provided value with TryParse 
             as a System.DateTime using the
                    
             specified dateTimeStyle, the format format, and
         
                        
             System.Globalization.CultureInfo.InvariantCulture.
        """
        pass

    __all__ = [
        'DateTime',
        'DateTimeExact',
        'Decimal',
        'Double',
        'Int',
        'Long',
        'TimeSpan',
        'TryParse',
        'TryParseExact',
    ]


class Period(Enum, IComparable, IFormattable, IConvertible):
    """
    enum Period - Enum of all the analysis periods, AS integers. Reference "Period" Array to access the values
    
    enum Period, values: FifteenMinutes (900), FiveMinutes (300), FourHours (14400), OneHour (3600), OneMinute (60), SixHours (21600), TenMinutes (600), TenSeconds (10), ThirtyMinutes (1800), ThirtySeconds (30), ThreeMinutes (180), TwentyMinutes (1200), TwoHours (7200), TwoMinutes (120)
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

    FifteenMinutes = None
    FiveMinutes = None
    FourHours = None
    OneHour = None
    OneMinute = None
    SixHours = None
    TenMinutes = None
    TenSeconds = None
    ThirtyMinutes = None
    ThirtySeconds = None
    ThreeMinutes = None
    TwentyMinutes = None
    TwoHours = None
    TwoMinutes = None
    value__ = None


class ReaderErrorDetectedEventArgs(EventArgs):
    """
    Event arguments for the QuantConnect.Interfaces.IDataProviderEvents.ReaderErrorDetected event
    
    ReaderErrorDetectedEventArgs(message: str, stackTrace: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, message, stackTrace):
        """ __new__(cls: type, message: str, stackTrace: str) """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error message

Get: Message(self: ReaderErrorDetectedEventArgs) -> str

"""

    StackTrace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error stack trace

Get: StackTrace(self: ReaderErrorDetectedEventArgs) -> str

"""



class RealTimeProvider(object, ITimeProvider):
    """
    Provides an implementation of QuantConnect.ITimeProvider that
                uses System.DateTime.UtcNow to provide the current time
    
    RealTimeProvider()
    """
    def GetUtcNow(self):
        """
        GetUtcNow(self: RealTimeProvider) -> DateTime
        
            Gets the current time in UTC
            Returns: The current time in UTC
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Instance = None


class RealTimeSynchronizedTimer(object):
    """
    Real time timer class for precise callbacks on a millisecond resolution in a self managed thread.
    
    RealTimeSynchronizedTimer()
    RealTimeSynchronizedTimer(period: TimeSpan, callback: Action[DateTime])
    """
    def Pause(self):
        """
        Pause(self: RealTimeSynchronizedTimer)
            Hang the real time event:
        """
        pass

    def Resume(self):
        """
        Resume(self: RealTimeSynchronizedTimer)
            Resume clock
        """
        pass

    def Scanner(self):
        """
        Scanner(self: RealTimeSynchronizedTimer)
            Scan the stopwatch for the desired millisecond 
             delay:
        """
        pass

    def Start(self):
        """
        Start(self: RealTimeSynchronizedTimer)
            Start the synchronized real time timer - fire 
             events at start of each second or minute
        """
        pass

    def Stop(self):
        """
        Stop(self: RealTimeSynchronizedTimer)
            Stop the real time timer:
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, period=None, callback=None):
        """
        __new__(cls: type)
        __new__(cls: type, period: TimeSpan, callback: Action[DateTime])
        """
        pass


class Resolution(Enum, IComparable, IFormattable, IConvertible):
    """
    Resolution of data requested.
    
    enum Resolution, values: Daily (4), Hour (3), Minute (2), Second (1), Tick (0)
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

    Daily = None
    Hour = None
    Minute = None
    Second = None
    Tick = None
    value__ = None


class Result(object):
    """
    Base class for backtesting and live results that packages result data.
                QuantConnect.Packets.LiveResultQuantConnect.Packets.BacktestResult
    
    Result()
    """
    AlphaRuntimeStatistics = None
    Charts = None
    OrderEvents = None
    Orders = None
    ProfitLoss = None
    RuntimeStatistics = None
    ServerStatistics = None
    Statistics = None


class ScatterMarkerSymbol(Enum, IComparable, IFormattable, IConvertible):
    """
    Shape or symbol for the marker in a scatter plot
    
    enum ScatterMarkerSymbol, values: Circle (1), Diamond (3), None (0), Square (2), Triangle (4), TriangleDown (5)
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

    Circle = None
    Diamond = None
    None = None
    Square = None
    Triangle = None
    TriangleDown = None
    value__ = None


class SecurityIdentifier(object, IEquatable[SecurityIdentifier]):
    """
    Defines a unique identifier for securities
    
    SecurityIdentifier(symbol: str, properties: UInt64)
    SecurityIdentifier(symbol: str, properties: UInt64, underlying: SecurityIdentifier)
    """
    def Equals(self, *__args):
        """
        Equals(self: SecurityIdentifier, other: SecurityIdentifier) -> bool
        
            Indicates whether the current object is equal to 
             another object of the same type.
        
        
            other: An object to compare with this object.
            Returns: true if the current object is equal to the other 
             parameter; otherwise, false.
        
        Equals(self: SecurityIdentifier, obj: object) -> bool
        
            Determines whether the specified System.Object is 
             equal to the current System.Object.
        
        
            obj: The object to compare with the current object.
            Returns: true if the specified object  is equal to the 
             current object; otherwise, false.
        """
        pass

    @staticmethod
    def GenerateBase(dataType, symbol, market, mapSymbol, date):
        """ GenerateBase(dataType: Type, symbol: str, market: str, mapSymbol: bool, date: Nullable[DateTime]) -> SecurityIdentifier """
        pass

    @staticmethod
    def GenerateBaseSymbol(dataType, symbol):
        """
        GenerateBaseSymbol(dataType: Type, symbol: str) -> str
        
            Generates the 
             QuantConnect.SecurityIdentifier.Symbol property 
             for QuantConnect.SecurityType.Base security 
             identifiers
        
        
            dataType: The base data custom data type if namespacing is 
             required, null otherwise
        
            symbol: The ticker symbol
            Returns: The value used for the security identifier's 
             QuantConnect.SecurityIdentifier.Symbol
        """
        pass

    @staticmethod
    def GenerateCfd(symbol, market):
        """
        GenerateCfd(symbol: str, market: str) -> SecurityIdentifier
        
            Generates a new QuantConnect.SecurityIdentifier 
             for a CFD security
        
        
            symbol: The CFD contract symbol
            market: The security's market
            Returns: A new QuantConnect.SecurityIdentifier 
             representing the specified CFD security
        """
        pass

    @staticmethod
    def GenerateConstituentIdentifier(symbol, securityType, market):
        """
        GenerateConstituentIdentifier(symbol: str, securityType: SecurityType, market: str) -> SecurityIdentifier
        
            Generates a new QuantConnect.SecurityIdentifier 
             for a 
             QuantConnect.Data.UniverseSelection.ConstituentsUn
             iverseData.
                    Note that the symbol 
             ticker is case sensitive here.
        
        
            symbol: The ticker to use for this constituent identifier
            securityType: The security type of this constituent universe
            market: The security's market
            Returns: A new QuantConnect.SecurityIdentifier 
             representing the specified constituent universe
        """
        pass

    @staticmethod
    def GenerateCrypto(symbol, market):
        """
        GenerateCrypto(symbol: str, market: str) -> SecurityIdentifier
        
            Generates a new QuantConnect.SecurityIdentifier 
             for a Crypto pair
        
        
            symbol: The currency pair in the format similar to: 
             'EURUSD'
        
            market: The security's market
            Returns: A new QuantConnect.SecurityIdentifier 
             representing the specified Crypto pair
        """
        pass

    @staticmethod
    def GenerateEquity(*__args):
        """
        GenerateEquity(symbol: str, market: str, mapSymbol: bool, mapFileProvider: IMapFileProvider, mappingResolveDate: Nullable[DateTime]) -> SecurityIdentifier
        GenerateEquity(date: DateTime, symbol: str, market: str) -> SecurityIdentifier
        
            Generates a new QuantConnect.SecurityIdentifier 
             for an equity
        
        
            date: The first date this security traded (in LEAN this 
             is the first date in the map_file
        
            symbol: The ticker symbol this security traded under on 
             the date
        
            market: The security's market
            Returns: A new QuantConnect.SecurityIdentifier 
             representing the specified equity security
        """
        pass

    @staticmethod
    def GenerateForex(symbol, market):
        """
        GenerateForex(symbol: str, market: str) -> SecurityIdentifier
        
            Generates a new QuantConnect.SecurityIdentifier 
             for a forex pair
        
        
            symbol: The currency pair in the format similar to: 
             'EURUSD'
        
            market: The security's market
            Returns: A new QuantConnect.SecurityIdentifier 
             representing the specified forex pair
        """
        pass

    @staticmethod
    def GenerateFuture(expiry, symbol, market):
        """
        GenerateFuture(expiry: DateTime, symbol: str, market: str) -> SecurityIdentifier
        
            Generates a new QuantConnect.SecurityIdentifier 
             for a future
        
        
            expiry: The date the future expires
            symbol: The security's symbol
            market: The market
            Returns: A new QuantConnect.SecurityIdentifier 
             representing the specified futures security
        """
        pass

    @staticmethod
    def GenerateOption(expiry, underlying, market, strike, optionRight, optionStyle):
        """
        GenerateOption(expiry: DateTime, underlying: SecurityIdentifier, market: str, strike: Decimal, optionRight: OptionRight, optionStyle: OptionStyle) -> SecurityIdentifier
        
            Generates a new QuantConnect.SecurityIdentifier 
             for an option
        
        
            expiry: The date the option expires
            underlying: The underlying security's symbol
            market: The market
            strike: The strike price
            optionRight: The option type, call or put
            optionStyle: The option style, American or European
            Returns: A new QuantConnect.SecurityIdentifier 
             representing the specified option security
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: SecurityIdentifier) -> int
        
            Serves as a hash function for a particular type.
            Returns: A hash code for the current System.Object.
        """
        pass

    @staticmethod
    def Parse(value):
        """
        Parse(value: str) -> SecurityIdentifier
        
            Parses the specified string into a 
             QuantConnect.SecurityIdentifier
                    The 
             string must be a 40 digit number. The first 20 
             digits must be parseable
                    to a 64 bit 
             unsigned integer and contain ancillary data about 
             the security.
                    The second 20 digits 
             must also be parseable as a 64 bit unsigned 
             integer and
                    contain the symbol 
             encoded from base36, this provides for 12 alpha 
             numeric case
                    insensitive characters.
        
        
            value: The string value to be parsed
            Returns: A new QuantConnect.SecurityIdentifier instance if 
             the value is able to be parsed.
        """
        pass

    def ToString(self):
        """
        ToString(self: SecurityIdentifier) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod
    def TryParse(value, identifier):
        """
        TryParse(value: str) -> (bool, SecurityIdentifier)
        
            Attempts to parse the specified lue as a 
             QuantConnect.SecurityIdentifier.
        
        
            value: The string value to be parsed
            Returns: True on success, otherwise false
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol, properties, underlying=None):
        """
        __new__(cls: type, symbol: str, properties: UInt64)
        __new__(cls: type, symbol: str, properties: UInt64, underlying: SecurityIdentifier)
        __new__[SecurityIdentifier]() -> SecurityIdentifier
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the date component of this identifier. For equities this
            is the first date the security traded. Technically speaking,
            in LEAN, this is the first date mentioned in the map_files.
            For options this is the expiry date. For futures this is the
            settlement date. For forex and cfds this property will throw an
            exception as the field is not specified.

Get: Date(self: SecurityIdentifier) -> DateTime

"""

    HasUnderlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether or not this QuantConnect.SecurityIdentifier is a derivative,
            that is, it has a valid QuantConnect.SecurityIdentifier.Underlying property

Get: HasUnderlying(self: SecurityIdentifier) -> bool

"""

    Market = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the market component of this security identifier. If located in the
            internal mappings, the full string is returned. If the value is unknown,
            the integer value is returned as a string.

Get: Market(self: SecurityIdentifier) -> str

"""

    OptionRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the option type component of this security identifier. This
            only applies to SecurityType.Open and will throw an exception if
            accessed otherwise.

Get: OptionRight(self: SecurityIdentifier) -> OptionRight

"""

    OptionStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the option style component of this security identifier. This
            only applies to SecurityType.Open and will throw an exception if
            accessed otherwise.

Get: OptionStyle(self: SecurityIdentifier) -> OptionStyle

"""

    SecurityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security type component of this security identifier.

Get: SecurityType(self: SecurityIdentifier) -> SecurityType

"""

    StrikePrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the option strike price. This only applies to SecurityType.Option
            and will thrown anexception if accessed otherwse.

Get: StrikePrice(self: SecurityIdentifier) -> Decimal

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the original symbol used to generate this security identifier.
            For equities, by convention this is the first ticker symbol for which
            the security traded

Get: Symbol(self: SecurityIdentifier) -> str

"""

    Underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the underlying security identifier for this security identifier. When there is
            no underlying, this property will return a value of QuantConnect.SecurityIdentifier.Empty.

Get: Underlying(self: SecurityIdentifier) -> SecurityIdentifier

"""


    DefaultDate = None
    Empty = None
    InvalidSymbolCharacters = None
    None = None


class SecurityType(Enum, IComparable, IFormattable, IConvertible):
    """
    Type of tradable security / underlying asset
    
    enum SecurityType, values: Base (0), Cfd (6), Commodity (3), Crypto (7), Equity (1), Forex (4), Future (5), Option (2)
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

    Base = None
    Cfd = None
    Commodity = None
    Crypto = None
    Equity = None
    Forex = None
    Future = None
    Option = None
    value__ = None


class Series(object):
    """
    Chart Series Object - Series data and properties for a chart:
    
    Series()
    Series(name: str)
    Series(name: str, type: SeriesType)
    Series(name: str, type: SeriesType, index: int)
    Series(name: str, type: SeriesType, index: int, unit: str)
    Series(name: str, type: SeriesType, unit: str)
    Series(name: str, type: SeriesType, unit: str, color: Color)
    Series(name: str, type: SeriesType, unit: str, color: Color, symbol: ScatterMarkerSymbol)
    """
    def AddPoint(self, *__args):
        """
        AddPoint(self: Series, time: DateTime, value: Decimal)
            Add a new point to this series
        
            time: Time of the chart point
            value: Value of the chart point
        AddPoint(self: Series, chartPoint: ChartPoint)
            Add a new point to this series
        
            chartPoint: The data point to add
        """
        pass

    def Clone(self):
        """
        Clone(self: Series) -> Series
        
            Return a new instance clone of this object
        """
        pass

    def ConsolidateChartPoints(self):
        """
        ConsolidateChartPoints(self: Series) -> ChartPoint
        
            Will sum up all chart points into a new single 
             value, using the time of lastest point
        
            Returns: The new chart point
        """
        pass

    def GetUpdates(self):
        """
        GetUpdates(self: Series) -> Series
        
            Get the updates since the last call to this 
             function.
        
            Returns: List of the updates from the series
        """
        pass

    def Purge(self):
        """
        Purge(self: Series)
            Removes the data from this series and resets the 
             update position to 0
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None, type=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, type: SeriesType)
        __new__(cls: type, name: str, type: SeriesType, index: int)
        __new__(cls: type, name: str, type: SeriesType, index: int, unit: str)
        __new__(cls: type, name: str, type: SeriesType, unit: str)
        __new__(cls: type, name: str, type: SeriesType, unit: str, color: Color)
        __new__(cls: type, name: str, type: SeriesType, unit: str, color: Color, symbol: ScatterMarkerSymbol)
        """
        pass

    Color = None
    Index = None
    Name = None
    ScatterMarkerSymbol = None
    SeriesType = None
    Unit = None
    Values = None


class SeriesSampler(object):
    """
    A type capable of taking a chart and resampling using a linear interpolation strategy
    
    SeriesSampler(resolution: TimeSpan)
    """
    def Sample(self, series, start, stop):
        """
        Sample(self: SeriesSampler, series: Series, start: DateTime, stop: DateTime) -> Series
        
            Samples the given series
        
            series: The series to be sampled
            start: The date to start sampling, if before start of 
             data then start of data will be used
        
            stop: The date to stop sampling, if after stop of data, 
             then stop of data will be used
        
            Returns: The sampled series
        """
        pass

    def SampleCharts(self, charts, start, stop):
        """ SampleCharts(self: SeriesSampler, charts: IDictionary[str, Chart], start: DateTime, stop: DateTime) -> Dictionary[str, Chart] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, resolution):
        """ __new__(cls: type, resolution: TimeSpan) """
        pass


class SeriesType(Enum, IComparable, IFormattable, IConvertible):
    """
    Available types of charts
    
    enum SeriesType, values: Bar (3), Candle (2), Flag (4), Line (0), Pie (6), Scatter (1), StackedArea (5), Treemap (7)
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

    Bar = None
    Candle = None
    Flag = None
    Line = None
    Pie = None
    Scatter = None
    StackedArea = None
    Treemap = None
    value__ = None


class ServerType(Enum, IComparable, IFormattable, IConvertible):
    """
    Live server types available through the web IDE. / QC deployment.
    
    enum ServerType, values: Server1024 (1), Server2048 (2), Server512 (0)
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

    Server1024 = None
    Server2048 = None
    Server512 = None
    value__ = None


class SettlementType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of settlement in derivative deals
    
    enum SettlementType, values: Cash (1), PhysicalDelivery (0)
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

    Cash = None
    PhysicalDelivery = None
    value__ = None


class SplitType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of QuantConnect.Data.Market.Split data
    
    enum SplitType, values: SplitOccurred (1), Warning (0)
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

    SplitOccurred = None
    value__ = None
    Warning = None


class StartDateLimitedEventArgs(EventArgs):
    """
    Event arguments for the QuantConnect.Interfaces.IDataProviderEvents.StartDateLimited event
    
    StartDateLimitedEventArgs(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, message):
        """ __new__(cls: type, message: str) """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error message

Get: Message(self: StartDateLimitedEventArgs) -> str

"""



class StoragePermissions(Enum, IComparable, IFormattable, IConvertible):
    """
    Cloud storage permission options.
    
    enum StoragePermissions, values: Authenticated (1), Public (0)
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

    Authenticated = None
    Public = None
    value__ = None


class StringExtensions(object):
    """
    Provides extension methods for properly parsing and serializing values while properly using
                an IFormatProvider/CultureInfo when applicable
    """
    @staticmethod
    def ConvertInvariant(value, conversionType=None):
        """
        ConvertInvariant[T](value: object) -> T
        ConvertInvariant(value: object, conversionType: Type) -> object
        
            Converts the provided value as conversionType
           
                      using 
             QuantConnect.StringExtensions.CultureInfo
        """
        pass

    @staticmethod
    def EndsWithInvariant(value, ending, ignoreCase):
        """
        EndsWithInvariant(value: str, ending: str, ignoreCase: bool) -> bool
        
            Checks if the string ends with the provided 
             ending using 
             QuantConnect.StringExtensions.CultureInfo
               
                  while optionally ignoring case.
        """
        pass

    @staticmethod
    def IfNotNullOrEmpty(value, *__args):
        """
        IfNotNullOrEmpty[T](value: str, defaultValue: T, func: Func[str, T]) -> T
        IfNotNullOrEmpty[T](value: str, func: Func[str, T]) -> T
        """
        pass

    @staticmethod
    def IndexOfInvariant(value, *__args):
        """
        IndexOfInvariant(value: str, character: Char) -> int
        
            Gets the index of the specified character using 
             QuantConnect.StringExtensions.StringComparison
        
        IndexOfInvariant(value: str, substring: str, ignoreCase: bool) -> int
        
            Gets the index of the specified substring using 
             QuantConnect.StringExtensions.StringComparison
          
                       or 
             System.StringComparison.InvariantCultureIgnoreCase
              when ignoreCase is true
        """
        pass

    @staticmethod
    def Invariant(formattable):
        """
        Invariant(formattable: FormattableString) -> str
        
            Non-extension method alias for 
             System.FormattableString.Invariant(System.Formatta
             bleString)
                    This supports the using 
             static QuantConnect.StringExtensions syntax
             
                    and is aimed at ensuring all formatting is 
             piped through this class instead of
                    
             alternatively piping through directly to 
             System.FormattableString.Invariant(System.Formatta
             bleString)
        """
        pass

    @staticmethod
    def LastIndexOfInvariant(value, substring, ignoreCase):
        """
        LastIndexOfInvariant(value: str, substring: str, ignoreCase: bool) -> int
        
            Gets the index of the specified substring using 
             QuantConnect.StringExtensions.StringComparison
          
                       or 
             System.StringComparison.InvariantCultureIgnoreCase
              when ignoreCase is true
        """
        pass

    @staticmethod
    def StartsWithInvariant(value, beginning, ignoreCase):
        """
        StartsWithInvariant(value: str, beginning: str, ignoreCase: bool) -> bool
        
            Checks if the string starts with the provided 
             beginning using 
             QuantConnect.StringExtensions.CultureInfo
               
                  while optionally ignoring case.
        """
        pass

    @staticmethod
    def ToIso8601Invariant(dateTime):
        """
        ToIso8601Invariant(dateTime: DateTime) -> str
        
            Provides a convenience methods for converting a 
             System.DateTime to an invariant ISO-8601 string
        """
        pass

    @staticmethod
    def ToStringInvariant(*__args):
        """
        ToStringInvariant(convertible: IConvertible) -> str
        
            Converts the provided value to a string using 
             QuantConnect.StringExtensions.CultureInfo
        
        ToStringInvariant(formattable: IFormattable, format: str) -> str
        
            Formats the provided value using the specified 
             format and
                    
             QuantConnect.StringExtensions.CultureInfo
        """
        pass

    __all__ = [
        'ConvertInvariant',
        'EndsWithInvariant',
        'IfNotNullOrEmpty',
        'IndexOfInvariant',
        'Invariant',
        'LastIndexOfInvariant',
        'StartsWithInvariant',
        'ToIso8601Invariant',
        'ToStringInvariant',
    ]


class SubscriptionTransportMedium(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies where a subscription's data comes from
    
    enum SubscriptionTransportMedium, values: LocalFile (0), RemoteFile (1), Rest (2), Streaming (3)
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

    LocalFile = None
    RemoteFile = None
    Rest = None
    Streaming = None
    value__ = None


class Symbol(object, IEquatable[Symbol], IComparable):
    """
    Represents a unique security identifier. This is made of two components,
                the unique SID and the Value. The value is the current ticker symbol while
                the SID is constant over the life of a security
    
    Symbol(sid: SecurityIdentifier, value: str)
    """
    def CompareTo(self, obj):
        """
        CompareTo(self: Symbol, obj: object) -> int
        
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

    def Contains(self, value):
        """ Contains(self: Symbol, value: str) -> bool """
        pass

    @staticmethod
    def Create(ticker, securityType, market, alias, baseDataType):
        """
        Create(ticker: str, securityType: SecurityType, market: str, alias: str, baseDataType: Type) -> Symbol
        
            Provides a convenience method for creating a 
             Symbol for most security types.
                    This 
             method currently does not support Commodities
        
        
            ticker: The string ticker symbol
            securityType: The security type of the ticker. If securityType 
             == Option, then a canonical symbol is created
        
            market: The market the ticker resides in
            alias: An alias to be used for the symbol cache. 
             Required when
                    adding the same 
             security from different markets
        
            baseDataType: Optional for QuantConnect.SecurityType.Base and 
             used for generating the base data SID
        
            Returns: A new Symbol object for the specified ticker
        """
        pass

    @staticmethod
    def CreateBase(baseType, underlying, market):
        """
        CreateBase(baseType: Type, underlying: Symbol, market: str) -> Symbol
        
            Creates a new Symbol for custom data. This method 
             allows for the creation of a new Base Symbol
            
                     using the first ticker and the first 
             traded date from the provided underlying Symbol. 
             This avoids
                    the issue for mappable 
             types, where the ticker is remapped supposing the 
             provided ticker value is from today.
                    
             See method 
             SecurityIdentifier.GetFirstTickerAndDate(Interface
             s.IMapFileProvider, string, string)
                    
             The provided symbol is also set to 
             QuantConnect.Symbol.Underlying so that it can be 
             accessed using the custom data Symbol.
                  
               This is useful for associating custom data 
             Symbols to other asset classes so that it is 
             possible to filter using custom data
                    
             and place trades on the underlying asset based on 
             the filtered custom data.
        
        
            baseType: Type of BaseData instance
            underlying: Underlying symbol to set for the Base Symbol
            market: Market
            Returns: New non-mapped Base Symbol that contains an 
             Underlying Symbol
        """
        pass

    @staticmethod
    def CreateFuture(ticker, market, expiry, alias):
        """
        CreateFuture(ticker: str, market: str, expiry: DateTime, alias: str) -> Symbol
        
            Provides a convenience method for creating a 
             future Symbol.
        
        
            ticker: The ticker
            market: The market the future resides in
            expiry: The future expiry date
            alias: An alias to be used for the symbol cache. 
             Required when
                    adding the same 
             security from different markets
        
            Returns: A new Symbol object for the specified future 
             contract
        """
        pass

    @staticmethod
    def CreateOption(*__args):
        """
        CreateOption(underlying: str, market: str, style: OptionStyle, right: OptionRight, strike: Decimal, expiry: DateTime, alias: str, mapSymbol: bool) -> Symbol
        
            Provides a convenience method for creating an 
             option Symbol.
        
        
            underlying: The underlying ticker
            market: The market the underlying resides in
            style: The option style (American, European, ect..)
            right: The option right (Put/Call)
            strike: The option strike price
            expiry: The option expiry date
            alias: An alias to be used for the symbol cache. 
             Required when
                    adding the same 
             security from different markets
        
            mapSymbol: Specifies if symbol should be mapped using map 
             file provider
        
            Returns: A new Symbol object for the specified option 
             contract
        
        CreateOption(underlyingSymbol: Symbol, market: str, style: OptionStyle, right: OptionRight, strike: Decimal, expiry: DateTime, alias: str) -> Symbol
        
            Provides a convenience method for creating an 
             option Symbol using SecurityIdentifier.
        
        
            underlyingSymbol: The underlying security symbol
            market: The market the underlying resides in
            style: The option style (American, European, ect..)
            right: The option right (Put/Call)
            strike: The option strike price
            expiry: The option expiry date
            alias: An alias to be used for the symbol cache. 
             Required when
                    adding the same 
             security from diferent markets
        
            Returns: A new Symbol object for the specified option 
             contract
        """
        pass

    def EndsWith(self, value):
        """ EndsWith(self: Symbol, value: str) -> bool """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Symbol, obj: object) -> bool
        
            Determines whether the specified System.Object is 
             equal to the current System.Object.
        
        
            obj: The object to compare with the current object.
            Returns: true if the specified object  is equal to the 
             current object; otherwise, false.
        
        Equals(self: Symbol, other: Symbol) -> bool
        
            Indicates whether the current object is equal to 
             another object of the same type.
        
        
            other: An object to compare with this object.
            Returns: true if the current object is equal to the other 
             parameter; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Symbol) -> int
        
            Serves as a hash function for a particular type.
            Returns: A hash code for the current System.Object.
        """
        pass

    def HasUnderlyingSymbol(self, symbol):
        """
        HasUnderlyingSymbol(self: Symbol, symbol: Symbol) -> bool
        
            Determines if the specified symbol is an 
             underlying of this symbol instance
        
        
            symbol: The underlying to check for
            Returns: True if the specified symbol is an underlying of 
             this symbol instance
        """
        pass

    def IsCanonical(self):
        """
        IsCanonical(self: Symbol) -> bool
        
            Method returns true, if symbol is a derivative 
             canonical symbol
        
            Returns: true, if symbol is a derivative canonical symbol
        """
        pass

    def StartsWith(self, value):
        """ StartsWith(self: Symbol, value: str) -> bool """
        pass

    def ToLower(self):
        """ ToLower(self: Symbol) -> str """
        pass

    def ToString(self):
        """
        ToString(self: Symbol) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    def ToUpper(self):
        """ ToUpper(self: Symbol) -> str """
        pass

    def UpdateMappedSymbol(self, mappedSymbol):
        """
        UpdateMappedSymbol(self: Symbol, mappedSymbol: str) -> Symbol
        
            Creates new symbol with updated mapped symbol. 
             Symbol Mapping: When symbols change over time 
             (e.g. CHASE-> JPM) need to update the symbol 
             requested.
                    Method returns newly 
             created symbol
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
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
    def __new__(self, sid, value):
        """ __new__(cls: type, sid: SecurityIdentifier, value: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HasUnderlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether or not this QuantConnect.Symbol is a derivative,
            that is, it has a valid QuantConnect.Symbol.Underlying property

Get: HasUnderlying(self: Symbol) -> bool

"""

    ID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security identifier for this symbol

Get: ID(self: Symbol) -> SecurityIdentifier

"""

    SecurityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security type of the symbol

Get: SecurityType(self: Symbol) -> SecurityType

"""

    Underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security underlying symbol, if any

Get: Underlying(self: Symbol) -> Symbol

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current symbol for this ticker

Get: Value(self: Symbol) -> str

"""


    Empty = None
    None = None


class SymbolCache(object):
    """
    Provides a string->Symbol mapping to allow for user defined strings to be lifted into a Symbol
                This is mainly used via the Symbol implicit operator, but also functions that create securities
                should also call Set to add new mappings
    """
    @staticmethod
    def Clear():
        """
        Clear()
            Clears the current caches
        """
        pass

    @staticmethod
    def GetSymbol(ticker):
        """
        GetSymbol(ticker: str) -> Symbol
        
            Gets the Symbol object that is mapped to the 
             specified string ticker symbol
        
        
            ticker: The string ticker symbol
            Returns: The symbol object that maps to the specified 
             string ticker symbol
        """
        pass

    @staticmethod
    def GetTicker(symbol):
        """
        GetTicker(symbol: Symbol) -> str
        
            Gets the string ticker symbol that is mapped to 
             the specified Symbol
        
        
            symbol: The symbol object
            Returns: The string ticker symbol that maps to the 
             specified symbol object
        """
        pass

    @staticmethod
    def Set(ticker, symbol):
        """
        Set(ticker: str, symbol: Symbol)
            Adds a mapping for the specified ticker
        
            ticker: The string ticker symbol
            symbol: The symbol object that maps to the string ticker 
             symbol
        """
        pass

    @staticmethod
    def TryGetSymbol(ticker, symbol):
        """
        TryGetSymbol(ticker: str) -> (bool, Symbol)
        
            Gets the Symbol object that is mapped to the 
             specified string ticker symbol
        
        
            ticker: The string ticker symbol
            Returns: The symbol object that maps to the specified 
             string ticker symbol
        """
        pass

    @staticmethod
    def TryGetTicker(symbol, ticker):
        """
        TryGetTicker(symbol: Symbol) -> (bool, str)
        
            Gets the string ticker symbol that is mapped to 
             the specified Symbol
        
        
            symbol: The symbol object
            Returns: The string ticker symbol that maps to the 
             specified symbol object
        """
        pass

    @staticmethod
    def TryRemove(*__args):
        """
        TryRemove(symbol: Symbol) -> bool
        
            Removes the mapping for the specified symbol from 
             the cache
        
        
            symbol: The symbol whose mappings are to be removed
            Returns: True if the symbol mapping were removed from the 
             cache
        
        TryRemove(ticker: str) -> bool
        
            Removes the mapping for the specified symbol from 
             the cache
        
        
            ticker: The ticker whose mappings are to be removed
            Returns: True if the symbol mapping were removed from the 
             cache
        """
        pass

    __all__ = [
        'Clear',
        'GetSymbol',
        'GetTicker',
        'Set',
        'TryGetSymbol',
        'TryGetTicker',
        'TryRemove',
    ]


class SymbolJsonConverter(JsonConverter):
    """
    Defines a Newtonsoft.Json.JsonConverter to be used when deserializing to
                the QuantConnect.Symbol class.
    
    SymbolJsonConverter()
    """
    def CanConvert(self, objectType):
        """
        CanConvert(self: SymbolJsonConverter, objectType: Type) -> bool
        
            Determines whether this instance can convert the 
             specified object type.
        
        
            objectType: Type of the object.
            Returns: true if this instance can convert the specified 
             object type; otherwise, false.
        """
        pass

    def ReadJson(self, reader, objectType, existingValue, serializer):
        """
        ReadJson(self: SymbolJsonConverter, reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object
        
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
        WriteJson(self: SymbolJsonConverter, writer: JsonWriter, value: object, serializer: JsonSerializer)
            Writes the JSON representation of the object.
        
            writer: The Newtonsoft.Json.JsonWriter to write to.
            value: The value.
            serializer: The calling serializer.
        """
        pass


class SymbolRepresentation(object):
    """ Public static helper class that does parsing/generation of symbol representations (options, futures) """
    @staticmethod
    def GenerateFutureTicker(underlying, expiration, doubleDigitsYear):
        """
        GenerateFutureTicker(underlying: str, expiration: DateTime, doubleDigitsYear: bool) -> str
        
            Returns future symbol ticker from underlying and 
             expiration date. Function can generate tickers of 
             two formats: one and two digits year.
                   
              Format [Ticker][2 digit day code][1 char month 
             code][2/1 digit year code], more information at 
             http://help.tradestation.com/09_01/tradestationhel
             p/symbology/futures_symbology.htm
        
        
            underlying: String underlying
            expiration: Expiration date
            doubleDigitsYear: True if year should represented by two digits; 
             False - one digit
        """
        pass

    @staticmethod
    def GenerateOptionTickerOSI(*__args):
        """
        GenerateOptionTickerOSI(symbol: Symbol) -> str
        
            Returns option symbol ticker in accordance with 
             OSI symbology
                    More information can 
             be found at 
             http://www.optionsclearing.com/components/docs/ini
             tiatives/symbology/symbology_initiative_v1_8.pdf
        
        
            symbol: Symbol object to create OSI ticker from
            Returns: The OSI ticker representation
        GenerateOptionTickerOSI(underlying: str, right: OptionRight, strikePrice: Decimal, expiration: DateTime) -> str
        
            Returns option symbol ticker in accordance with 
             OSI symbology
                    More information can 
             be found at 
             http://www.optionsclearing.com/components/docs/ini
             tiatives/symbology/symbology_initiative_v1_8.pdf
        
        
            underlying: Underlying string
            right: Option right
            strikePrice: Option strike
            expiration: Option expiration date
            Returns: The OSI ticker representation
        """
        pass

    @staticmethod
    def ParseFutureTicker(ticker):
        """
        ParseFutureTicker(ticker: str) -> FutureTickerProperties
        
            Function returns underlying name, expiration 
             year, expiration month, expiration day for the 
             future contract ticker. Function detects if
             
                    the format used is either 1 or 2 digits 
             year, and if day code is present (will default to 
             1rst day of month). Returns null, if parsing 
             failed.
                    Format [Ticker][2 digit day 
             code OPTIONAL][1 char month code][2/1 digit year 
             code]
        
            Returns: Results containing 1) underlying name, 2) short 
             expiration year, 3) expiration month
        """
        pass

    @staticmethod
    def ParseOptionTickerIQFeed(ticker):
        """
        ParseOptionTickerIQFeed(ticker: str) -> OptionTickerProperties
        
            Function returns option contract parameters 
             (underlying name, expiration date, strike, right) 
             from IQFeed option ticker
                    Symbology 
             details: 
             http://www.iqfeed.net/symbolguide/index.cfm?symbol
             guide=guide&displayaction=support%C2%A7ion=guide&w
             eb=iqfeed&guide=options&web=IQFeed&type=stock
        
        
            ticker: IQFeed option ticker
            Returns: Results containing 1) underlying name, 2) option 
             right, 3) option strike 4) expiration date
        """
        pass

    @staticmethod
    def ParseOptionTickerOSI(ticker):
        """
        ParseOptionTickerOSI(ticker: str) -> Symbol
        
            Parses the specified OSI options ticker into a 
             Symbol object
        
        
            ticker: The OSI compliant option ticker string
            Returns: Symbol object for the specified OSI option ticker 
             string
        """
        pass

    FutureTickerProperties = None
    OptionTickerProperties = None
    __all__ = [
        'FutureTickerProperties',
        'GenerateFutureTicker',
        'GenerateOptionTickerOSI',
        'OptionTickerProperties',
        'ParseFutureTicker',
        'ParseOptionTickerIQFeed',
        'ParseOptionTickerOSI',
    ]


class SymbolValueJsonConverter(JsonConverter):
    """
    Defines a Newtonsoft.Json.JsonConverter to be used when you only want to serialize
                the QuantConnect.Symbol.Value property instead of the full QuantConnect.Symbol
                instance
    
    SymbolValueJsonConverter()
    """
    def CanConvert(self, objectType):
        """
        CanConvert(self: SymbolValueJsonConverter, objectType: Type) -> bool
        
            Determines whether this instance can convert the 
             specified object type.
        
        
            objectType: Type of the object.
            Returns: true if this instance can convert the specified 
             object type; otherwise, false.
        """
        pass

    def ReadJson(self, reader, objectType, existingValue, serializer):
        """
        ReadJson(self: SymbolValueJsonConverter, reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object
        
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
        WriteJson(self: SymbolValueJsonConverter, writer: JsonWriter, value: object, serializer: JsonSerializer)
            Writes the JSON representation of the object.
        
            writer: The Newtonsoft.Json.JsonWriter to write to.
            value: The value.
            serializer: The calling serializer.
        """
        pass


class TickType(Enum, IComparable, IFormattable, IConvertible):
    """
    Types of tick data
    
    enum TickType, values: OpenInterest (2), Quote (1), Trade (0)
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

    OpenInterest = None
    Quote = None
    Trade = None
    value__ = None


class Time(object):
    """ Time helper class collection for working with trading dates """
    @staticmethod
    def Abs(timeSpan):
        """
        Abs(timeSpan: TimeSpan) -> TimeSpan
        
            Gets the absolute value of the specified time span
        
            timeSpan: Time span whose absolute value we seek
            Returns: The absolute value of the specified time span
        """
        pass

    @staticmethod
    def DateTimeToUnixTimeStamp(time):
        """
        DateTimeToUnixTimeStamp(time: DateTime) -> float
        
            Convert a Datetime to Unix Timestamp
        
            time: C# datetime object
            Returns: Double unix timestamp
        """
        pass

    @staticmethod
    def EachDay(from, thru):
        """
        EachDay(from: DateTime, thru: DateTime) -> IEnumerable[DateTime]
        
            Define an enumerable date range and return each 
             date as a datetime object in the date range
        
        
            from: DateTime start date
            thru: DateTime end date
            Returns: Enumerable date range
        """
        pass

    @staticmethod
    def EachTradeableDay(*__args):
        """
        EachTradeableDay(securities: ICollection[Security], from: DateTime, thru: DateTime) -> IEnumerable[DateTime]
        EachTradeableDay(security: Security, from: DateTime, thru: DateTime) -> IEnumerable[DateTime]
        
            Define an enumerable date range of tradeable 
             dates - skip the holidays and weekends when 
             securities in this algorithm don't trade.
        
        
            security: The security to get tradeable dates for
            from: Start date
            thru: End date
            Returns: Enumerable date range
        EachTradeableDay(exchange: SecurityExchangeHours, from: DateTime, thru: DateTime) -> IEnumerable[DateTime]
        
            Define an enumerable date range of tradeable 
             dates - skip the holidays and weekends when 
             securities in this algorithm don't trade.
        
        
            exchange: The security to get tradeable dates for
            from: Start date
            thru: End date
            Returns: Enumerable date range
        """
        pass

    @staticmethod
    def EachTradeableDayInTimeZone(exchange, from, thru, timeZone, includeExtendedMarketHours):
        """
        EachTradeableDayInTimeZone(exchange: SecurityExchangeHours, from: DateTime, thru: DateTime, timeZone: DateTimeZone, includeExtendedMarketHours: bool) -> IEnumerable[DateTime]
        
            Define an enumerable date range of tradeable 
             dates but expressed in a different time zone.
        
        
            exchange: The exchange hours
            from: The start time in the exchange time zone
            thru: The end time in the exchange time zone (inclusive 
             of the final day)
        
            timeZone: The timezone to project the dates into (inclusive 
             of the final day)
        
            includeExtendedMarketHours: True to include extended market hours trading in 
             the search, false otherwise
        """
        pass

    @staticmethod
    def GetEndTimeForTradeBars(exchangeHours, start, barSize, barCount, extendedMarketHours):
        """
        GetEndTimeForTradeBars(exchangeHours: SecurityExchangeHours, start: DateTime, barSize: TimeSpan, barCount: int, extendedMarketHours: bool) -> DateTime
        
            Determines the end time at which the requested 
             number of bars of the given  will have elapsed.
         
                        NOTE: The start time is not 
             discretized by barSize units like is done in 
             QuantConnect.Time.GetStartTimeForTradeBars(QuantCo
             nnect.Securities.SecurityExchangeHours,System.Date
             Time,System.TimeSpan,System.Int32,System.Boolean)
        
        
            exchangeHours: The exchange hours used to test for market open 
             hours
        
            start: The end time of the last bar over the requested 
             period
        
            barSize: The length of each bar
            barCount: The number of bars requested
            extendedMarketHours: True to allow extended market hours bars, 
             otherwise false for only normal market hours
        
            Returns: The start time that would provide the specified 
             number of bars ending at the specified end time, 
             rounded down by the requested bar size
        """
        pass

    @staticmethod
    def GetNumberOfTradeBarsInInterval(exchangeHours, start, end, barSize):
        """
        GetNumberOfTradeBarsInInterval(exchangeHours: SecurityExchangeHours, start: DateTime, end: DateTime, barSize: TimeSpan) -> int
        
            Gets the number of trade bars of the specified 
             barSize that fit between the start and end
        
        
            exchangeHours: The exchange used to test for market open hours
            start: The start time of the interval in the exchange 
             time zone
        
            end: The end time of the interval in the exchange time 
             zone
        
            barSize: The step size used to count number of bars 
             between start and end
        
            Returns: The number of bars of the specified size between 
             start and end times
        """
        pass

    @staticmethod
    def GetStartTimeForTradeBars(exchangeHours, end, barSize, barCount, extendedMarketHours):
        """
        GetStartTimeForTradeBars(exchangeHours: SecurityExchangeHours, end: DateTime, barSize: TimeSpan, barCount: int, extendedMarketHours: bool) -> DateTime
        
            Determines the start time required to produce the 
             requested number of bars and the given size
        
        
            exchangeHours: The exchange hours used to test for market open 
             hours
        
            end: The end time of the last bar over the requested 
             period
        
            barSize: The length of each bar
            barCount: The number of bars requested
            extendedMarketHours: True to allow extended market hours bars, 
             otherwise false for only normal market hours
        
            Returns: The start time that would provide the specified 
             number of bars ending at the specified end time, 
             rounded down by the requested bar size
        """
        pass

    @staticmethod
    def Max(one, two):
        """
        Max(one: TimeSpan, two: TimeSpan) -> TimeSpan
        
            Returns the timespan with the larger value
        Max(one: DateTime, two: DateTime) -> DateTime
        
            Returns the larger of two date times
        """
        pass

    @staticmethod
    def Min(one, two):
        """
        Min(one: TimeSpan, two: TimeSpan) -> TimeSpan
        
            Returns the timespan with the smaller value
        Min(one: DateTime, two: DateTime) -> DateTime
        
            Returns the smaller of two date times
        """
        pass

    @staticmethod
    def Multiply(interval, multiplier):
        """
        Multiply(interval: TimeSpan, multiplier: float) -> TimeSpan
        
            Multiplies the specified interval by the 
             multiplier
        
        
            interval: The interval to be multiplied, such as 
             TimeSpan.FromSeconds(1)
        
            multiplier: The number of times to multiply the interval
            Returns: The multiplied interval, such as 1s*5 = 5s
        """
        pass

    @staticmethod
    def NormalizeInstantWithinRange(start, current, period):
        """
        NormalizeInstantWithinRange(start: DateTime, current: DateTime, period: TimeSpan) -> float
        
            Normalizes the current time within the specified 
             period
                    time = start => 0
                   
              time = start + period => 1
        
        
            start: The start time of the range
            current: The current time we seek to normalize
            period: The time span of the range
            Returns: The normalized time
        """
        pass

    @staticmethod
    def NormalizeTimeStep(period, stepSize):
        """
        NormalizeTimeStep(period: TimeSpan, stepSize: TimeSpan) -> float
        
            Normalizes the step size as a percentage of the 
             period.
        
        
            period: The period to normalize against
            stepSize: The step size to be normaized
            Returns: The normalized step size as a percentage of the 
             period
        """
        pass

    @staticmethod
    def ParseDate(dateToParse):
        """
        ParseDate(dateToParse: str) -> DateTime
        
            Parse a standard YY MM DD date into a DateTime. 
             Attempt common date formats
        
        
            dateToParse: String date time to parse
            Returns: Date time
        """
        pass

    @staticmethod
    def TimeStamp():
        """
        TimeStamp() -> float
        
            Get the current time as a unix timestamp
            Returns: Double value of the unix as UTC timestamp
        """
        pass

    @staticmethod
    def TradableDate(securities, day):
        """ TradableDate(securities: IEnumerable[Security], day: DateTime) -> bool """
        pass

    @staticmethod
    def TradeableDates(securities, start, finish):
        """ TradeableDates(securities: ICollection[Security], start: DateTime, finish: DateTime) -> int """
        pass

    @staticmethod
    def UnixMillisecondTimeStampToDateTime(unixTimeStamp):
        """
        UnixMillisecondTimeStampToDateTime(unixTimeStamp: float) -> DateTime
        
            Create a C# DateTime from a UnixTimestamp
        
            unixTimeStamp: Double unix timestamp (Time since Midnight Jan 1 
             1970) in milliseconds
        
            Returns: C# date timeobject
        """
        pass

    @staticmethod
    def UnixTimeStampToDateTime(unixTimeStamp):
        """
        UnixTimeStampToDateTime(unixTimeStamp: float) -> DateTime
        
            Create a C# DateTime from a UnixTimestamp
        
            unixTimeStamp: Double unix timestamp (Time since Midnight Jan 1 
             1970)
        
            Returns: C# date timeobject
        """
        pass

    BeginningOfTime = None
    DateTimeWithZone = None
    EndOfTime = None
    EndOfTimeTimeSpan = None
    MaxTimeSpan = None
    OneDay = None
    OneHour = None
    OneMillisecond = None
    OneMinute = None
    OneSecond = None
    OneYear = None
    __all__ = [
        'Abs',
        'BeginningOfTime',
        'DateTimeToUnixTimeStamp',
        'DateTimeWithZone',
        'EachDay',
        'EachTradeableDay',
        'EachTradeableDayInTimeZone',
        'EndOfTime',
        'GetEndTimeForTradeBars',
        'GetNumberOfTradeBarsInInterval',
        'GetStartTimeForTradeBars',
        'Max',
        'MaxTimeSpan',
        'Min',
        'Multiply',
        'NormalizeInstantWithinRange',
        'NormalizeTimeStep',
        'OneDay',
        'OneHour',
        'OneMillisecond',
        'OneMinute',
        'OneSecond',
        'OneYear',
        'ParseDate',
        'TimeStamp',
        'TradableDate',
        'TradeableDates',
        'UnixMillisecondTimeStampToDateTime',
        'UnixTimeStampToDateTime',
    ]


class TimeKeeper(object, ITimeKeeper):
    """
    Provides a means of centralizing time for various time zones.
    
    TimeKeeper(utcDateTime: DateTime, *timeZones: Array[DateTimeZone])
    TimeKeeper(utcDateTime: DateTime, timeZones: IEnumerable[DateTimeZone])
    """
    def AddTimeZone(self, timeZone):
        """
        AddTimeZone(self: TimeKeeper, timeZone: DateTimeZone)
            Adds the specified time zone to this time keeper
        """
        pass

    def GetLocalTimeKeeper(self, timeZone):
        """
        GetLocalTimeKeeper(self: TimeKeeper, timeZone: DateTimeZone) -> LocalTimeKeeper
        
            Gets the QuantConnect.LocalTimeKeeper instance 
             for the specified time zone
        
        
            timeZone: The time zone whose QuantConnect.LocalTimeKeeper 
             we seek
        
            Returns: The QuantConnect.LocalTimeKeeper instance for the 
             specified time zone
        """
        pass

    def GetTimeIn(self, timeZone):
        """
        GetTimeIn(self: TimeKeeper, timeZone: DateTimeZone) -> DateTime
        
            Gets the local time in the specified time zone. 
             If the specified NodaTime.DateTimeZone
                  
               has not already been added, this will throw a 
             System.Collections.Generic.KeyNotFoundException.
        
        
            timeZone: The time zone to get local time for
            Returns: The local time in the specifed time zone
        """
        pass

    def SetUtcDateTime(self, utcDateTime):
        """
        SetUtcDateTime(self: TimeKeeper, utcDateTime: DateTime)
            Sets the current UTC time for this time keeper 
             and the attached child 
             QuantConnect.LocalTimeKeeper instances.
        
        
            utcDateTime: The current time in UTC
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, utcDateTime, timeZones):
        """
        __new__(cls: type, utcDateTime: DateTime, *timeZones: Array[DateTimeZone])
        __new__(cls: type, utcDateTime: DateTime, timeZones: IEnumerable[DateTimeZone])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    UtcTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current time in UTC

Get: UtcTime(self: TimeKeeper) -> DateTime

"""



class TimeUpdatedEventArgs(EventArgs):
    """
    Event arguments class for the QuantConnect.LocalTimeKeeper.TimeUpdated event
    
    TimeUpdatedEventArgs(time: DateTime, timeZone: DateTimeZone)
    """
    @staticmethod # known case of __new__
    def __new__(self, time, timeZone):
        """ __new__(cls: type, time: DateTime, timeZone: DateTimeZone) """
        pass

    Time = None
    TimeZone = None


class TimeZoneOffsetProvider(object):
    """
    Represents the discontinuties in a single time zone and provides offsets to UTC.
                This type assumes that times will be asked in a forward marching manner.
                This type is not thread safe.
    
    TimeZoneOffsetProvider(timeZone: DateTimeZone, utcStartTime: DateTime, utcEndTime: DateTime)
    """
    def ConvertFromUtc(self, utcTime):
        """
        ConvertFromUtc(self: TimeZoneOffsetProvider, utcTime: DateTime) -> DateTime
        
            Converts the specified utcTime using the offset 
             resolved from
                    a call to 
             QuantConnect.TimeZoneOffsetProvider.GetOffsetTicks
             (System.DateTime)
        
        
            utcTime: The time to convert from utc
            Returns: The same instant in time represented in the 
             QuantConnect.TimeZoneOffsetProvider.TimeZone
        """
        pass

    def ConvertToUtc(self, localTime):
        """
        ConvertToUtc(self: TimeZoneOffsetProvider, localTime: DateTime) -> DateTime
        
            Converts the specified local time to UTC. This 
             function will advance this offset provider
        
        
            localTime: The local time to be converted to UTC
            Returns: The specified time in UTC
        """
        pass

    def GetNextDiscontinuity(self):
        """
        GetNextDiscontinuity(self: TimeZoneOffsetProvider) -> Int64
        
            Gets this offset provider's next discontinuity
            Returns: The next discontinuity in UTC ticks
        """
        pass

    def GetOffsetTicks(self, utcTime):
        """
        GetOffsetTicks(self: TimeZoneOffsetProvider, utcTime: DateTime) -> Int64
        
            Gets the offset in ticks from this time zone to 
             UTC, such that UTC time + offset = local time
        
        
            utcTime: The time in UTC to get an offset to local
            Returns: The offset in ticks between UTC and the local 
             time zone
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, timeZone, utcStartTime, utcEndTime):
        """ __new__(cls: type, timeZone: DateTimeZone, utcStartTime: DateTime, utcEndTime: DateTime) """
        pass

    TimeZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time zone this instances provides offsets for

Get: TimeZone(self: TimeZoneOffsetProvider) -> DateTimeZone

"""



class TimeZones(object):
    """ Provides access to common time zones """
    Amsterdam = None
    Anchorage = None
    Athens = None
    Auckland = None
    Berlin = None
    Brisbane = None
    Bucharest = None
    BuenosAires = None
    Cairo = None
    Chicago = None
    Denver = None
    Detroit = None
    Dublin = None
    EasternStandard = None
    Helsinki = None
    HongKong = None
    Honolulu = None
    Istanbul = None
    Jerusalem = None
    Johannesburg = None
    London = None
    LosAngeles = None
    Madrid = None
    Melbourne = None
    MexicoCity = None
    Minsk = None
    Moscow = None
    NewYork = None
    Paris = None
    Phoenix = None
    Rome = None
    SaoPaulo = None
    Shanghai = None
    Sydney = None
    Tokyo = None
    Toronto = None
    Utc = None
    Vancouver = None
    Zurich = None
    __all__ = [
        'Amsterdam',
        'Anchorage',
        'Athens',
        'Auckland',
        'Berlin',
        'Brisbane',
        'Bucharest',
        'BuenosAires',
        'Cairo',
        'Chicago',
        'Denver',
        'Detroit',
        'Dublin',
        'EasternStandard',
        'Helsinki',
        'HongKong',
        'Honolulu',
        'Istanbul',
        'Jerusalem',
        'Johannesburg',
        'London',
        'LosAngeles',
        'Madrid',
        'Melbourne',
        'MexicoCity',
        'Minsk',
        'Moscow',
        'NewYork',
        'Paris',
        'Phoenix',
        'Rome',
        'SaoPaulo',
        'Shanghai',
        'Sydney',
        'Tokyo',
        'Toronto',
        'Utc',
        'Vancouver',
        'Zurich',
    ]


class TradingCalendar(object):
    """
    Class represents trading calendar, populated with variety of events relevant to currently trading instruments
    
    TradingCalendar(securityManager: SecurityManager, marketHoursDatabase: MarketHoursDatabase)
    """
    def GetDaysByType(self, type, start, end):
        """
        GetDaysByType(self: TradingCalendar, type: TradingDayType, start: DateTime, end: DateTime) -> IEnumerable[TradingDay]
        
            Method returns QuantConnect.TradingDay of the 
             specified type (QuantConnect.TradingDayType) that 
             contains trading events associated with the range 
             of dates
        
        
            type: Type of the events
            start: Start date of the range (inclusive)
            end: End date of the range (inclusive)
            Returns: >Populated list of QuantConnect.TradingDay
        """
        pass

    def GetTradingDay(self, day=None):
        """
        GetTradingDay(self: TradingCalendar) -> TradingDay
        
            Method returns QuantConnect.TradingDay that 
             contains trading events associated with today's 
             date
        
            Returns: Populated instance of QuantConnect.TradingDay
        GetTradingDay(self: TradingCalendar, day: DateTime) -> TradingDay
        
            Method returns QuantConnect.TradingDay that 
             contains trading events associated with the given 
             date
        
            Returns: Populated instance of QuantConnect.TradingDay
        """
        pass

    def GetTradingDays(self, start, end):
        """
        GetTradingDays(self: TradingCalendar, start: DateTime, end: DateTime) -> IEnumerable[TradingDay]
        
            Method returns QuantConnect.TradingDay that 
             contains trading events associated with the range 
             of dates
        
        
            start: Start date of the range (inclusive)
            end: End date of the range (inclusive)
            Returns: >Populated list of QuantConnect.TradingDay
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, securityManager, marketHoursDatabase):
        """ __new__(cls: type, securityManager: SecurityManager, marketHoursDatabase: MarketHoursDatabase) """
        pass


class TradingDay(object):
    """
    Class contains trading events associated with particular day in QuantConnect.TradingCalendar
    
    TradingDay()
    """
    BusinessDay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property returns true, if the day is a business day

Get: BusinessDay(self: TradingDay) -> bool

"""

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The date that this instance is associated with

Get: Date(self: TradingDay) -> DateTime

"""

    EquityDividends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property returns the list of symbols (among currently traded) that have ex-dividend date on this day

Get: EquityDividends(self: TradingDay) -> IEnumerable[Symbol]

"""

    FutureExpirations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property returns the list of futures (among currently traded) that expire on this day

Get: FutureExpirations(self: TradingDay) -> IEnumerable[Symbol]

"""

    FutureRolls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property returns the list of futures (among currently traded) that roll forward on this day

Get: FutureRolls(self: TradingDay) -> IEnumerable[Symbol]

"""

    OptionExpirations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property returns the list of options (among currently traded) that expire on this day

Get: OptionExpirations(self: TradingDay) -> IEnumerable[Symbol]

"""

    PublicHoliday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property returns true, if the day is a public holiday

Get: PublicHoliday(self: TradingDay) -> bool

"""

    SymbolDelistings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property returns the list of symbols (among currently traded) that are delisted on this day

Get: SymbolDelistings(self: TradingDay) -> IEnumerable[Symbol]

"""

    Weekend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property returns true, if the day is a weekend

Get: Weekend(self: TradingDay) -> bool

"""



class TradingDayType(Enum, IComparable, IFormattable, IConvertible):
    """
    Enum lists available trading events
    
    enum TradingDayType, values: BusinessDay (0), EconomicEvent (8), EquityDividends (7), FutureExpiration (4), FutureRoll (5), OptionExpiration (3), PublicHoliday (1), SymbolDelisting (6), Weekend (2)
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

    BusinessDay = None
    EconomicEvent = None
    EquityDividends = None
    FutureExpiration = None
    FutureRoll = None
    OptionExpiration = None
    PublicHoliday = None
    SymbolDelisting = None
    value__ = None
    Weekend = None


class UserPlan(Enum, IComparable, IFormattable, IConvertible):
    """
    User / Algorithm Job Subscription Level
    
    enum UserPlan, values: Free (0), Hobbyist (1), Professional (2)
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

    Free = None
    Hobbyist = None
    Professional = None
    value__ = None


class USHoliday(object):
    """ US Public Holidays - Not Tradeable: """
    Dates = None
    __all__ = [
        'Dates',
    ]


# variables with complex values

