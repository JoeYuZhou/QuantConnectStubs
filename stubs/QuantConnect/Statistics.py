# encoding: utf-8
# module QuantConnect.Statistics calls itself Statistics
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AlgorithmPerformance(object):
    """
    The QuantConnect.Statistics.AlgorithmPerformance class is a wrapper for QuantConnect.Statistics.AlgorithmPerformance.TradeStatistics and QuantConnect.Statistics.AlgorithmPerformance.PortfolioStatistics
    
    AlgorithmPerformance(trades: List[Trade], profitLoss: SortedDictionary[DateTime, Decimal], equity: SortedDictionary[DateTime, Decimal], listPerformance: List[float], listBenchmark: List[float], startingCapital: Decimal)
    AlgorithmPerformance()
    """
    @staticmethod # known case of __new__
    def __new__(self, trades=None, profitLoss=None, equity=None, listPerformance=None, listBenchmark=None, startingCapital=None):
        """
        __new__(cls: type, trades: List[Trade], profitLoss: SortedDictionary[DateTime, Decimal], equity: SortedDictionary[DateTime, Decimal], listPerformance: List[float], listBenchmark: List[float], startingCapital: Decimal)
        __new__(cls: type)
        """
        pass

    ClosedTrades = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of closed trades

Get: ClosedTrades(self: AlgorithmPerformance) -> List[Trade]

Set: ClosedTrades(self: AlgorithmPerformance) = value
"""

    PortfolioStatistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The algorithm statistics on portfolio

Get: PortfolioStatistics(self: AlgorithmPerformance) -> PortfolioStatistics

Set: PortfolioStatistics(self: AlgorithmPerformance) = value
"""

    TradeStatistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The algorithm statistics on closed trades

Get: TradeStatistics(self: AlgorithmPerformance) -> TradeStatistics

Set: TradeStatistics(self: AlgorithmPerformance) = value
"""



class FillGroupingMethod(Enum, IComparable, IFormattable, IConvertible):
    """
    The method used to group order fills into trades
    
    enum FillGroupingMethod, values: FillToFill (0), FlatToFlat (1), FlatToReduced (2)
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

    FillToFill = None
    FlatToFlat = None
    FlatToReduced = None
    value__ = None


class FillMatchingMethod(Enum, IComparable, IFormattable, IConvertible):
    """
    The method used to match offsetting order fills
    
    enum FillMatchingMethod, values: FIFO (0), LIFO (1)
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

    FIFO = None
    LIFO = None
    value__ = None


class FitnessScoreManager(object):
    """
    Implements a fitness score calculator needed to account for strategy volatility,
                returns, drawdown, and factor in the turnover to ensure the algorithm engagement
                is statistically significant
    
    FitnessScoreManager()
    """
    def Initialize(self, algorithm):
        """
        Initialize(self: FitnessScoreManager, algorithm: IAlgorithm)
            Initializes the fitness score instance and sets 
             the initial portfolio value
        """
        pass

    @staticmethod
    def SigmoidalScale(valueToScale):
        """
        SigmoidalScale(valueToScale: Decimal) -> Decimal
        
            Adjusts the input value to a range of 0 to 10 
             based on a sigmoidal scale
        """
        pass

    def UpdateScores(self):
        """
        UpdateScores(self: FitnessScoreManager)
            Gets the fitness score value for the algorithms 
             current state
        """
        pass

    FitnessScore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Score of the strategy's performance, and suitability for the Alpha Stream Market

Get: FitnessScore(self: FitnessScoreManager) -> Decimal

"""

    PortfolioTurnover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Measurement of the strategies trading activity with respect to the portfolio value.
            Calculated as the sales volume with respect to the average total portfolio value.

Get: PortfolioTurnover(self: FitnessScoreManager) -> Decimal

"""

    ReturnOverMaxDrawdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides a risk adjusted way to factor in the returns and drawdown of the strategy.
            It is calculated by dividing the Portfolio Annualized Return by the Maximum Drawdown seen during the backtest.

Get: ReturnOverMaxDrawdown(self: FitnessScoreManager) -> Decimal

"""

    SortinoRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gives a relative picture of the strategy volatility.
            It is calculated by taking a portfolio's annualized rate of return and subtracting the risk free rate of return.

Get: SortinoRatio(self: FitnessScoreManager) -> Decimal

"""



class KellyCriterionManager(object):
    """
    Class in charge of calculating the Kelly Criterion values.
                Will use the sample values of the last year.
    
    KellyCriterionManager()
    """
    def AddNewValue(self, newValue, time):
        """
        AddNewValue(self: KellyCriterionManager, newValue: Decimal, time: DateTime)
            Adds a new value to the population.
                    
             Will remove values older than an year compared 
             with the provided time.
                    For 
             performance, will update the continuous average 
             calculation
        
        
            newValue: The new value to add
            time: The new values time
        """
        pass

    def UpdateScores(self):
        """
        UpdateScores(self: KellyCriterionManager)
            Updates the Kelly Criterion values
        """
        pass

    KellyCriterionEstimate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Score of the strategy's insights predictive power

Get: KellyCriterionEstimate(self: KellyCriterionManager) -> Decimal

Set: KellyCriterionEstimate(self: KellyCriterionManager) = value
"""

    KellyCriterionProbabilityValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The p-value or probability value of the QuantConnect.Statistics.KellyCriterionManager.KellyCriterionEstimate

Get: KellyCriterionProbabilityValue(self: KellyCriterionManager) -> Decimal

Set: KellyCriterionProbabilityValue(self: KellyCriterionManager) = value
"""



class PortfolioStatistics(object):
    """
    The QuantConnect.Statistics.PortfolioStatistics class represents a set of statistics calculated from equity and benchmark samples
    
    PortfolioStatistics(profitLoss: SortedDictionary[DateTime, Decimal], equity: SortedDictionary[DateTime, Decimal], listPerformance: List[float], listBenchmark: List[float], startingCapital: Decimal, tradingDaysPerYear: int)
    PortfolioStatistics()
    """
    @staticmethod
    def GetRiskFreeRate():
        """
        GetRiskFreeRate() -> Decimal
        
            Gets the current defined risk free annual return 
             rate
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, profitLoss=None, equity=None, listPerformance=None, listBenchmark=None, startingCapital=None, tradingDaysPerYear=None):
        """
        __new__(cls: type, profitLoss: SortedDictionary[DateTime, Decimal], equity: SortedDictionary[DateTime, Decimal], listPerformance: List[float], listBenchmark: List[float], startingCapital: Decimal, tradingDaysPerYear: int)
        __new__(cls: type)
        """
        pass

    Alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Algorithm "Alpha" statistic - abnormal returns over the risk free rate and the relationshio (beta) with the benchmark returns.

Get: Alpha(self: PortfolioStatistics) -> Decimal

Set: Alpha(self: PortfolioStatistics) = value
"""

    AnnualStandardDeviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Annualized standard deviation

Get: AnnualStandardDeviation(self: PortfolioStatistics) -> Decimal

Set: AnnualStandardDeviation(self: PortfolioStatistics) = value
"""

    AnnualVariance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Annualized variance statistic calculation using the daily performance variance and trading days per year.

Get: AnnualVariance(self: PortfolioStatistics) -> Decimal

Set: AnnualVariance(self: PortfolioStatistics) = value
"""

    AverageLossRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The average rate of return for losing trades

Get: AverageLossRate(self: PortfolioStatistics) -> Decimal

Set: AverageLossRate(self: PortfolioStatistics) = value
"""

    AverageWinRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The average rate of return for winning trades

Get: AverageWinRate(self: PortfolioStatistics) -> Decimal

Set: AverageWinRate(self: PortfolioStatistics) = value
"""

    Beta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Algorithm "beta" statistic - the covariance between the algorithm and benchmark performance, divided by benchmark's variance

Get: Beta(self: PortfolioStatistics) -> Decimal

Set: Beta(self: PortfolioStatistics) = value
"""

    CompoundingAnnualReturn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Annual compounded returns statistic based on the final-starting capital and years.

Get: CompoundingAnnualReturn(self: PortfolioStatistics) -> Decimal

Set: CompoundingAnnualReturn(self: PortfolioStatistics) = value
"""

    Drawdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Drawdown maximum percentage.

Get: Drawdown(self: PortfolioStatistics) -> Decimal

Set: Drawdown(self: PortfolioStatistics) = value
"""

    Expectancy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The expected value of the rate of return

Get: Expectancy(self: PortfolioStatistics) -> Decimal

Set: Expectancy(self: PortfolioStatistics) = value
"""

    InformationRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Information ratio - risk adjusted return

Get: InformationRatio(self: PortfolioStatistics) -> Decimal

Set: InformationRatio(self: PortfolioStatistics) = value
"""

    LossRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ratio of the number of losing trades to the total number of trades

Get: LossRate(self: PortfolioStatistics) -> Decimal

Set: LossRate(self: PortfolioStatistics) = value
"""

    ProbabilisticSharpeRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Probabilistic Sharpe Ratio is a probability measure associated with the Sharpe ratio.
            It informs us of the probability that the estimated Sharpe ratio is greater than a chosen benchmark

Get: ProbabilisticSharpeRatio(self: PortfolioStatistics) -> Decimal

Set: ProbabilisticSharpeRatio(self: PortfolioStatistics) = value
"""

    ProfitLossRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ratio of the average win rate to the average loss rate

Get: ProfitLossRatio(self: PortfolioStatistics) -> Decimal

Set: ProfitLossRatio(self: PortfolioStatistics) = value
"""

    SharpeRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sharpe ratio with respect to risk free rate: measures excess of return per unit of risk.

Get: SharpeRatio(self: PortfolioStatistics) -> Decimal

Set: SharpeRatio(self: PortfolioStatistics) = value
"""

    TotalNetProfit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total net profit percentage.

Get: TotalNetProfit(self: PortfolioStatistics) -> Decimal

Set: TotalNetProfit(self: PortfolioStatistics) = value
"""

    TrackingError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tracking error volatility (TEV) statistic - a measure of how closely a portfolio follows the index to which it is benchmarked

Get: TrackingError(self: PortfolioStatistics) -> Decimal

Set: TrackingError(self: PortfolioStatistics) = value
"""

    TreynorRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Treynor ratio statistic is a measurement of the returns earned in excess of that which could have been earned on an investment that has no diversifiable risk

Get: TreynorRatio(self: PortfolioStatistics) -> Decimal

Set: TreynorRatio(self: PortfolioStatistics) = value
"""

    WinRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ratio of the number of winning trades to the total number of trades

Get: WinRate(self: PortfolioStatistics) -> Decimal

Set: WinRate(self: PortfolioStatistics) = value
"""



class Statistics(object):
    """
    Calculate all the statistics required from the backtest, based on the equity curve and the profit loss statement.
    
    Statistics()
    """
    @staticmethod
    def Alpha(algoPerformance, benchmarkPerformance, riskFreeRate):
        """ Alpha(algoPerformance: List[float], benchmarkPerformance: List[float], riskFreeRate: float) -> float """
        pass

    @staticmethod
    def AnnualPerformance(performance, tradingDaysPerYear):
        """ AnnualPerformance(performance: List[float], tradingDaysPerYear: float) -> float """
        pass

    @staticmethod
    def AnnualStandardDeviation(performance, tradingDaysPerYear):
        """ AnnualStandardDeviation(performance: List[float], tradingDaysPerYear: float) -> float """
        pass

    @staticmethod
    def AnnualVariance(performance, tradingDaysPerYear):
        """ AnnualVariance(performance: List[float], tradingDaysPerYear: float) -> float """
        pass

    @staticmethod
    def Beta(algoPerformance, benchmarkPerformance):
        """ Beta(algoPerformance: List[float], benchmarkPerformance: List[float]) -> float """
        pass

    @staticmethod
    def CompoundingAnnualPerformance(startingCapital, finalCapital, years):
        """
        CompoundingAnnualPerformance(startingCapital: Decimal, finalCapital: Decimal, years: Decimal) -> Decimal
        
            Annual compounded returns statistic based on the 
             final-starting capital and years.
        
        
            startingCapital: Algorithm starting capital
            finalCapital: Algorithm final capital
            years: Years trading
            Returns: Decimal fraction for annual compounding 
             performance
        """
        pass

    @staticmethod
    def DrawdownPercent(equityOverTime, rounding):
        """ DrawdownPercent(equityOverTime: SortedDictionary[DateTime, Decimal], rounding: int) -> Decimal """
        pass

    @staticmethod
    def DrawdownValue(equityOverTime, rounding):
        """ DrawdownValue(equityOverTime: SortedDictionary[DateTime, Decimal], rounding: int) -> Decimal """
        pass

    @staticmethod
    def Generate(pointsEquity, profitLoss, pointsPerformance, unsortedBenchmark, startingCash, totalFees, totalTrades, tradingDaysPerYear):
        """ Generate(pointsEquity: IEnumerable[ChartPoint], profitLoss: SortedDictionary[DateTime, Decimal], pointsPerformance: IEnumerable[ChartPoint], unsortedBenchmark: Dictionary[DateTime, Decimal], startingCash: Decimal, totalFees: Decimal, totalTrades: Decimal, tradingDaysPerYear: float) -> Dictionary[str, str] """
        pass

    @staticmethod
    def InformationRatio(algoPerformance, benchmarkPerformance):
        """ InformationRatio(algoPerformance: List[float], benchmarkPerformance: List[float]) -> float """
        pass

    @staticmethod
    def ObservedSharpeRatio(listPerformance):
        """ ObservedSharpeRatio(listPerformance: List[float]) -> float """
        pass

    @staticmethod
    def ProbabilisticSharpeRatio(listPerformance, benchmarkSharpeRatio):
        """ ProbabilisticSharpeRatio(listPerformance: List[float], benchmarkSharpeRatio: float) -> float """
        pass

    @staticmethod
    def ProfitLossRatio(averageWin, averageLoss):
        """
        ProfitLossRatio(averageWin: Decimal, averageLoss: Decimal) -> Decimal
        
            Return profit loss ratio safely avoiding divide 
             by zero errors.
        """
        pass

    @staticmethod
    def SharpeRatio(algoPerformance, riskFreeRate):
        """ SharpeRatio(algoPerformance: List[float], riskFreeRate: float) -> float """
        pass

    @staticmethod
    def TrackingError(algoPerformance, benchmarkPerformance, tradingDaysPerYear):
        """ TrackingError(algoPerformance: List[float], benchmarkPerformance: List[float], tradingDaysPerYear: float) -> float """
        pass

    @staticmethod
    def TreynorRatio(algoPerformance, benchmarkPerformance, riskFreeRate):
        """ TreynorRatio(algoPerformance: List[float], benchmarkPerformance: List[float], riskFreeRate: float) -> float """
        pass


class StatisticsBuilder(object):
    """ The QuantConnect.Statistics.StatisticsBuilder class creates summary and rolling statistics from trades, equity and benchmark points """
    @staticmethod
    def Generate(trades, profitLoss, pointsEquity, pointsPerformance, pointsBenchmark, startingCapital, totalFees, totalTransactions):
        """ Generate(trades: List[Trade], profitLoss: SortedDictionary[DateTime, Decimal], pointsEquity: List[ChartPoint], pointsPerformance: List[ChartPoint], pointsBenchmark: List[ChartPoint], startingCapital: Decimal, totalFees: Decimal, totalTransactions: int) -> StatisticsResults """
        pass

    __all__ = [
        'Generate',
    ]


class StatisticsResults(object):
    """
    The QuantConnect.Statistics.StatisticsResults class represents total and rolling statistics for an algorithm
    
    StatisticsResults(totalPerformance: AlgorithmPerformance, rollingPerformances: Dictionary[str, AlgorithmPerformance], summary: Dictionary[str, str])
    StatisticsResults()
    """
    @staticmethod # known case of __new__
    def __new__(self, totalPerformance=None, rollingPerformances=None, summary=None):
        """
        __new__(cls: type, totalPerformance: AlgorithmPerformance, rollingPerformances: Dictionary[str, AlgorithmPerformance], summary: Dictionary[str, str])
        __new__(cls: type)
        """
        pass

    RollingPerformances = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The rolling performance of the algorithm over 1, 3, 6, 12 month periods

Get: RollingPerformances(self: StatisticsResults) -> Dictionary[str, AlgorithmPerformance]

"""

    Summary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a summary of the algorithm performance as a dictionary

Get: Summary(self: StatisticsResults) -> Dictionary[str, str]

"""

    TotalPerformance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The performance of the algorithm over the whole period

Get: TotalPerformance(self: StatisticsResults) -> AlgorithmPerformance

"""



class Trade(object):
    """
    Represents a closed trade
    
    Trade()
    """
    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The direction of the trade (Long or Short)

Get: Direction(self: Trade) -> TradeDirection

Set: Direction(self: Trade) = value
"""

    Duration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the duration of the trade

Get: Duration(self: Trade) -> TimeSpan

"""

    EndTradeDrawdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the amount of profit given back before the trade was closed

Get: EndTradeDrawdown(self: Trade) -> Decimal

"""

    EntryPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The price at which the trade was opened (or the average price if multiple entries)

Get: EntryPrice(self: Trade) -> Decimal

Set: EntryPrice(self: Trade) = value
"""

    EntryTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The date and time the trade was opened

Get: EntryTime(self: Trade) -> DateTime

Set: EntryTime(self: Trade) = value
"""

    ExitPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The price at which the trade was closed (or the average price if multiple exits)

Get: ExitPrice(self: Trade) -> Decimal

Set: ExitPrice(self: Trade) = value
"""

    ExitTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The date and time the trade was closed

Get: ExitTime(self: Trade) -> DateTime

Set: ExitTime(self: Trade) = value
"""

    MAE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Maximum Adverse Excursion (as account currency)

Get: MAE(self: Trade) -> Decimal

Set: MAE(self: Trade) = value
"""

    MFE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Maximum Favorable Excursion (as account currency)

Get: MFE(self: Trade) -> Decimal

Set: MFE(self: Trade) = value
"""

    ProfitLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The gross profit/loss of the trade (as account currency)

Get: ProfitLoss(self: Trade) -> Decimal

Set: ProfitLoss(self: Trade) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total unsigned quantity of the trade

Get: Quantity(self: Trade) -> Decimal

Set: Quantity(self: Trade) = value
"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The symbol of the traded instrument

Get: Symbol(self: Trade) -> Symbol

Set: Symbol(self: Trade) = value
"""

    TotalFees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total fees associated with the trade (always positive value) (as account currency)

Get: TotalFees(self: Trade) -> Decimal

Set: TotalFees(self: Trade) = value
"""



class TradeBuilder(object, ITradeBuilder):
    """
    The QuantConnect.Statistics.TradeBuilder class generates trades from executions and market price updates
    
    TradeBuilder(groupingMethod: FillGroupingMethod, matchingMethod: FillMatchingMethod)
    """
    def HasOpenPosition(self, symbol):
        """
        HasOpenPosition(self: TradeBuilder, symbol: Symbol) -> bool
        
            Returns true if there is an open position for the 
             symbol
        
        
            symbol: The symbol
            Returns: true if there is an open position for the symbol
        """
        pass

    def ProcessFill(self, fill, conversionRate, feeInAccountCurrency, multiplier):
        """
        ProcessFill(self: TradeBuilder, fill: OrderEvent, conversionRate: Decimal, feeInAccountCurrency: Decimal, multiplier: Decimal)
            Processes a new fill, eventually creating new 
             trades
        
        
            fill: The new fill order event
            conversionRate: The current security market conversion rate into 
             the account currency
        
            feeInAccountCurrency: The current order fee in the account currency
            multiplier: The contract multiplier
        """
        pass

    def SetLiveMode(self, live):
        """
        SetLiveMode(self: TradeBuilder, live: bool)
            Sets the live mode flag
        
            live: The live mode flag
        """
        pass

    def SetMarketPrice(self, symbol, price):
        """
        SetMarketPrice(self: TradeBuilder, symbol: Symbol, price: Decimal)
            Sets the current market price for the symbol
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, groupingMethod, matchingMethod):
        """ __new__(cls: type, groupingMethod: FillGroupingMethod, matchingMethod: FillMatchingMethod) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ClosedTrades = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of closed trades

Get: ClosedTrades(self: TradeBuilder) -> List[Trade]

"""



class TradeDirection(Enum, IComparable, IFormattable, IConvertible):
    """
    Direction of a trade
    
    enum TradeDirection, values: Long (0), Short (1)
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

    Long = None
    Short = None
    value__ = None


class TradeStatistics(object):
    """
    The QuantConnect.Statistics.TradeStatistics class represents a set of statistics calculated from a list of closed trades
    
    TradeStatistics(trades: IEnumerable[Trade])
    TradeStatistics()
    """
    @staticmethod # known case of __new__
    def __new__(self, trades=None):
        """
        __new__(cls: type, trades: IEnumerable[Trade])
        __new__(cls: type)
        """
        pass

    AverageEndTradeDrawdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The average amount of profit given back by all trades before exit (as symbol currency)

Get: AverageEndTradeDrawdown(self: TradeStatistics) -> Decimal

Set: AverageEndTradeDrawdown(self: TradeStatistics) = value
"""

    AverageLosingTradeDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The average duration for all losing trades

Get: AverageLosingTradeDuration(self: TradeStatistics) -> TimeSpan

Set: AverageLosingTradeDuration(self: TradeStatistics) = value
"""

    AverageLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The average loss for all winning trades (as symbol currency)

Get: AverageLoss(self: TradeStatistics) -> Decimal

Set: AverageLoss(self: TradeStatistics) = value
"""

    AverageMAE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The average Maximum Adverse Excursion for all trades

Get: AverageMAE(self: TradeStatistics) -> Decimal

Set: AverageMAE(self: TradeStatistics) = value
"""

    AverageMFE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The average Maximum Favorable Excursion for all trades

Get: AverageMFE(self: TradeStatistics) -> Decimal

Set: AverageMFE(self: TradeStatistics) = value
"""

    AverageProfit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The average profit for all winning trades (as symbol currency)

Get: AverageProfit(self: TradeStatistics) -> Decimal

Set: AverageProfit(self: TradeStatistics) = value
"""

    AverageProfitLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The average profit/loss (a.k.a. Expectancy or Average Trade) for all trades (as symbol currency)

Get: AverageProfitLoss(self: TradeStatistics) -> Decimal

Set: AverageProfitLoss(self: TradeStatistics) = value
"""

    AverageTradeDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The average duration for all trades

Get: AverageTradeDuration(self: TradeStatistics) -> TimeSpan

Set: AverageTradeDuration(self: TradeStatistics) = value
"""

    AverageWinningTradeDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The average duration for all winning trades

Get: AverageWinningTradeDuration(self: TradeStatistics) -> TimeSpan

Set: AverageWinningTradeDuration(self: TradeStatistics) = value
"""

    EndDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The exit date/time of the last trade

Get: EndDateTime(self: TradeStatistics) -> Nullable[DateTime]

Set: EndDateTime(self: TradeStatistics) = value
"""

    LargestLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The largest loss in a single trade (as symbol currency)

Get: LargestLoss(self: TradeStatistics) -> Decimal

Set: LargestLoss(self: TradeStatistics) = value
"""

    LargestMAE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The largest Maximum Adverse Excursion in a single trade (as symbol currency)

Get: LargestMAE(self: TradeStatistics) -> Decimal

Set: LargestMAE(self: TradeStatistics) = value
"""

    LargestMFE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The largest Maximum Favorable Excursion in a single trade (as symbol currency)

Get: LargestMFE(self: TradeStatistics) -> Decimal

Set: LargestMFE(self: TradeStatistics) = value
"""

    LargestProfit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The largest profit in a single trade (as symbol currency)

Get: LargestProfit(self: TradeStatistics) -> Decimal

Set: LargestProfit(self: TradeStatistics) = value
"""

    LossRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ratio of the number of losing trades to the total number of trades

Get: LossRate(self: TradeStatistics) -> Decimal

Set: LossRate(self: TradeStatistics) = value
"""

    MaxConsecutiveLosingTrades = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum number of consecutive losing trades

Get: MaxConsecutiveLosingTrades(self: TradeStatistics) -> int

Set: MaxConsecutiveLosingTrades(self: TradeStatistics) = value
"""

    MaxConsecutiveWinningTrades = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum number of consecutive winning trades

Get: MaxConsecutiveWinningTrades(self: TradeStatistics) -> int

Set: MaxConsecutiveWinningTrades(self: TradeStatistics) = value
"""

    MaximumClosedTradeDrawdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum closed-trade drawdown for all trades (as symbol currency)

Get: MaximumClosedTradeDrawdown(self: TradeStatistics) -> Decimal

Set: MaximumClosedTradeDrawdown(self: TradeStatistics) = value
"""

    MaximumDrawdownDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum amount of time to recover from a drawdown (longest time between new equity highs or peaks)

Get: MaximumDrawdownDuration(self: TradeStatistics) -> TimeSpan

Set: MaximumDrawdownDuration(self: TradeStatistics) = value
"""

    MaximumEndTradeDrawdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum amount of profit given back by a single trade before exit (as symbol currency)

Get: MaximumEndTradeDrawdown(self: TradeStatistics) -> Decimal

Set: MaximumEndTradeDrawdown(self: TradeStatistics) = value
"""

    MaximumIntraTradeDrawdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum intra-trade drawdown for all trades (as symbol currency)

Get: MaximumIntraTradeDrawdown(self: TradeStatistics) -> Decimal

Set: MaximumIntraTradeDrawdown(self: TradeStatistics) = value
"""

    MedianLosingTradeDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The median duration for all losing trades

Get: MedianLosingTradeDuration(self: TradeStatistics) -> TimeSpan

Set: MedianLosingTradeDuration(self: TradeStatistics) = value
"""

    MedianTradeDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The median duration for all trades

Get: MedianTradeDuration(self: TradeStatistics) -> TimeSpan

Set: MedianTradeDuration(self: TradeStatistics) = value
"""

    MedianWinningTradeDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The median duration for all winning trades

Get: MedianWinningTradeDuration(self: TradeStatistics) -> TimeSpan

Set: MedianWinningTradeDuration(self: TradeStatistics) = value
"""

    NumberOfLosingTrades = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total number of losing trades

Get: NumberOfLosingTrades(self: TradeStatistics) -> int

Set: NumberOfLosingTrades(self: TradeStatistics) = value
"""

    NumberOfWinningTrades = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total number of winning trades

Get: NumberOfWinningTrades(self: TradeStatistics) -> int

Set: NumberOfWinningTrades(self: TradeStatistics) = value
"""

    ProfitFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ratio of the total profit to the total loss

Get: ProfitFactor(self: TradeStatistics) -> Decimal

Set: ProfitFactor(self: TradeStatistics) = value
"""

    ProfitLossDownsideDeviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The downside deviation of the profits/losses for all trades (as symbol currency)

Get: ProfitLossDownsideDeviation(self: TradeStatistics) -> Decimal

Set: ProfitLossDownsideDeviation(self: TradeStatistics) = value
"""

    ProfitLossRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ratio of the average profit per trade to the average loss per trade

Get: ProfitLossRatio(self: TradeStatistics) -> Decimal

Set: ProfitLossRatio(self: TradeStatistics) = value
"""

    ProfitLossStandardDeviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The standard deviation of the profits/losses for all trades (as symbol currency)

Get: ProfitLossStandardDeviation(self: TradeStatistics) -> Decimal

Set: ProfitLossStandardDeviation(self: TradeStatistics) = value
"""

    ProfitToMaxDrawdownRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ratio of the total profit/loss to the maximum closed trade drawdown

Get: ProfitToMaxDrawdownRatio(self: TradeStatistics) -> Decimal

Set: ProfitToMaxDrawdownRatio(self: TradeStatistics) = value
"""

    SharpeRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ratio of the average profit/loss to the standard deviation

Get: SharpeRatio(self: TradeStatistics) -> Decimal

Set: SharpeRatio(self: TradeStatistics) = value
"""

    SortinoRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ratio of the average profit/loss to the downside deviation

Get: SortinoRatio(self: TradeStatistics) -> Decimal

Set: SortinoRatio(self: TradeStatistics) = value
"""

    StartDateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The entry date/time of the first trade

Get: StartDateTime(self: TradeStatistics) -> Nullable[DateTime]

Set: StartDateTime(self: TradeStatistics) = value
"""

    TotalFees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sum of fees for all trades

Get: TotalFees(self: TradeStatistics) -> Decimal

Set: TotalFees(self: TradeStatistics) = value
"""

    TotalLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total loss for all losing trades (as symbol currency)

Get: TotalLoss(self: TradeStatistics) -> Decimal

Set: TotalLoss(self: TradeStatistics) = value
"""

    TotalNumberOfTrades = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total number of trades

Get: TotalNumberOfTrades(self: TradeStatistics) -> int

Set: TotalNumberOfTrades(self: TradeStatistics) = value
"""

    TotalProfit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total profit for all winning trades (as symbol currency)

Get: TotalProfit(self: TradeStatistics) -> Decimal

Set: TotalProfit(self: TradeStatistics) = value
"""

    TotalProfitLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total profit/loss for all trades (as symbol currency)

Get: TotalProfitLoss(self: TradeStatistics) -> Decimal

Set: TotalProfitLoss(self: TradeStatistics) = value
"""

    WinLossRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ratio of the number of winning trades to the number of losing trades

Get: WinLossRatio(self: TradeStatistics) -> Decimal

Set: WinLossRatio(self: TradeStatistics) = value
"""

    WinRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ratio of the number of winning trades to the total number of trades

Get: WinRate(self: TradeStatistics) -> Decimal

Set: WinRate(self: TradeStatistics) = value
"""



