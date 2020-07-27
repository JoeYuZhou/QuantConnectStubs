# encoding: utf-8
# module QuantConnect.Packets calls itself Packets
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Packet(object):
    """
    Base class for packet messaging system
    
    Packet(type: PacketType)
    """
    @staticmethod # known case of __new__
    def __new__(self, type):
        """ __new__(cls: type, type: PacketType) """
        pass

    Channel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """User unique specific channel endpoint to send the packets

Get: Channel(self: Packet) -> str

Set: Channel(self: Packet) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Packet type defined by a string enum

Get: Type(self: Packet) -> PacketType

Set: Type(self: Packet) = value
"""



class AlgorithmNodePacket(Packet):
    """
    Algorithm Node Packet is a work task for the Lean Engine
    
    AlgorithmNodePacket(type: PacketType)
    """
    def GetAlgorithmName(self):
        """
        GetAlgorithmName(self: AlgorithmNodePacket) -> str
        
            Gets a unique name for the algorithm defined by 
             this packet
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type):
        """ __new__(cls: type, type: PacketType) """
        pass

    AlgorithmId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Algorithm Id - BacktestId or DeployId - Common Id property between packets.

Get: AlgorithmId(self: AlgorithmNodePacket) -> str

"""

    RamAllocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum amount of RAM (in MB) this algorithm is allowed to utilize

Get: RamAllocation(self: AlgorithmNodePacket) -> int

"""


    Algorithm = None
    CompileId = None
    Controls = None
    HistoryProvider = None
    Language = None
    Parameters = None
    ProjectId = None
    Redelivered = None
    RequestSource = None
    ServerType = None
    SessionId = None
    UserId = None
    UserPlan = None
    UserToken = None
    Version = None


class AlgorithmStatusPacket(Packet):
    """
    Algorithm status update information packet
    
    AlgorithmStatusPacket()
    AlgorithmStatusPacket(algorithmId: str, projectId: int, status: AlgorithmStatus, message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, algorithmId=None, projectId=None, status=None, message=None):
        """
        __new__(cls: type)
        __new__(cls: type, algorithmId: str, projectId: int, status: AlgorithmStatus, message: str)
        """
        pass

    AlgorithmId = None
    ChannelStatus = None
    ChartSubscription = None
    Message = None
    ProjectId = None
    Status = None


class LiveNodePacket(AlgorithmNodePacket):
    """
    Live job task packet: container for any live specific job variables
    
    LiveNodePacket()
    """
    Brokerage = None
    BrokerageData = None
    DataChannelProvider = None
    DataQueueHandler = None
    DeployId = None
    DisableAcknowledgement = None


class AlphaNodePacket(LiveNodePacket):
    """
    Alpha job packet
    
    AlphaNodePacket()
    """
    AlphaId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the alpha id

Get: AlphaId(self: AlphaNodePacket) -> str

Set: AlphaId(self: AlphaNodePacket) = value
"""



class AlphaResultPacket(Packet):
    """
    Provides a packet type for transmitting alpha insights data
    
    AlphaResultPacket()
    AlphaResultPacket(algorithmId: str, userId: int, insights: List[Insight], orderEvents: List[OrderEvent], orders: List[Order])
    """
    @staticmethod # known case of __new__
    def __new__(self, algorithmId=None, userId=None, insights=None, orderEvents=None, orders=None):
        """
        __new__(cls: type)
        __new__(cls: type, algorithmId: str, userId: int, insights: List[Insight], orderEvents: List[OrderEvent], orders: List[Order])
        """
        pass

    AlgorithmId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The algorithm's unique identifier

Get: AlgorithmId(self: AlphaResultPacket) -> str

Set: AlgorithmId(self: AlphaResultPacket) = value
"""

    AlphaId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The deployed alpha id. This is the id generated upon submssion to the alpha marketplace.
            If this is a user backtest or live algo then this will not be specified

Get: AlphaId(self: AlphaResultPacket) -> str

Set: AlphaId(self: AlphaResultPacket) = value
"""

    Insights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The generated insights

Get: Insights(self: AlphaResultPacket) -> List[Insight]

Set: Insights(self: AlphaResultPacket) = value
"""

    OrderEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The generated OrderEvents

Get: OrderEvents(self: AlphaResultPacket) -> List[OrderEvent]

Set: OrderEvents(self: AlphaResultPacket) = value
"""

    Orders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The new or updated Orders

Get: Orders(self: AlphaResultPacket) -> List[Order]

Set: Orders(self: AlphaResultPacket) = value
"""

    UserId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The user's id that deployed the alpha stream

Get: UserId(self: AlphaResultPacket) -> int

Set: UserId(self: AlphaResultPacket) = value
"""



class BacktestNodePacket(AlgorithmNodePacket):
    """
    Algorithm backtest task information packet.
    
    BacktestNodePacket()
    BacktestNodePacket(userId: int, projectId: int, sessionId: str, algorithmData: Array[Byte], startingCapital: Decimal, name: str, userPlan: UserPlan)
    BacktestNodePacket(userId: int, projectId: int, sessionId: str, algorithmData: Array[Byte], name: str, userPlan: UserPlan, startingCapital: Nullable[CashAmount])
    """
    @staticmethod # known case of __new__
    def __new__(self, userId=None, projectId=None, sessionId=None, algorithmData=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, userId: int, projectId: int, sessionId: str, algorithmData: Array[Byte], startingCapital: Decimal, name: str, userPlan: UserPlan)
        __new__(cls: type, userId: int, projectId: int, sessionId: str, algorithmData: Array[Byte], name: str, userPlan: UserPlan, startingCapital: Nullable[CashAmount])
        """
        pass

    IsDebugging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True, if this is a debugging backtest

Get: IsDebugging(self: BacktestNodePacket) -> bool

"""


    BacktestId = None
    Breakpoints = None
    CashAmount = None
    Name = None
    PeriodFinish = None
    PeriodStart = None
    TradeableDates = None
    Watchlist = None


class BacktestResult(Result):
    """
    Backtest results object class - result specific items from the packet.
    
    BacktestResult()
    BacktestResult(parameters: BacktestResultParameters)
    """
    @staticmethod # known case of __new__
    def __new__(self, parameters=None):
        """
        __new__(cls: type)
        __new__(cls: type, parameters: BacktestResultParameters)
        """
        pass

    RollingWindow = None
    TotalPerformance = None


class BacktestResultPacket(Packet):
    """
    Backtest result packet: send backtest information to GUI for user consumption.
    
    BacktestResultPacket()
    BacktestResultPacket(json: str)
    BacktestResultPacket(job: BacktestNodePacket, results: BacktestResult, endDate: DateTime, startDate: DateTime, progress: Decimal)
    """
    @staticmethod
    def CreateEmpty(job):
        """
        CreateEmpty(job: BacktestNodePacket) -> BacktestResultPacket
        
            Creates an empty result packet, useful when the 
             algorithm fails to initialize
        
        
            job: The associated job packet
            Returns: An empty result packet
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, json: str)
        __new__(cls: type, job: BacktestNodePacket, results: BacktestResult, endDate: DateTime, startDate: DateTime, progress: Decimal)
        """
        pass

    BacktestId = None
    CompileId = None
    DateFinished = None
    DateRequested = None
    Name = None
    PeriodFinish = None
    PeriodStart = None
    ProcessingTime = None
    Progress = None
    ProjectId = None
    Results = None
    SessionId = None
    TradeableDates = None
    UserId = None


class BaseResultParameters(object):
    """
    Base parameters used by QuantConnect.Packets.LiveResultParameters and QuantConnect.Packets.BacktestResultParameters
    
    BaseResultParameters()
    """
    AlphaRuntimeStatistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Contains population averages scores over the life of the algorithm

Get: AlphaRuntimeStatistics(self: BaseResultParameters) -> AlphaRuntimeStatistics

Set: AlphaRuntimeStatistics(self: BaseResultParameters) = value
"""

    Charts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Charts updates for the live algorithm since the last result packet

Get: Charts(self: BaseResultParameters) -> IDictionary[str, Chart]

Set: Charts(self: BaseResultParameters) = value
"""

    OrderEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Order events updates since the last result packet

Get: OrderEvents(self: BaseResultParameters) -> List[OrderEvent]

Set: OrderEvents(self: BaseResultParameters) = value
"""

    Orders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Order updates since the last result packet

Get: Orders(self: BaseResultParameters) -> IDictionary[int, Order]

Set: Orders(self: BaseResultParameters) = value
"""

    ProfitLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Trade profit and loss information since the last algorithm result packet

Get: ProfitLoss(self: BaseResultParameters) -> IDictionary[DateTime, Decimal]

Set: ProfitLoss(self: BaseResultParameters) = value
"""

    RuntimeStatistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Runtime banner/updating statistics in the title banner of the live algorithm GUI.

Get: RuntimeStatistics(self: BaseResultParameters) -> IDictionary[str, str]

Set: RuntimeStatistics(self: BaseResultParameters) = value
"""

    Statistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Statistics information sent during the algorithm operations.

Get: Statistics(self: BaseResultParameters) -> IDictionary[str, str]

Set: Statistics(self: BaseResultParameters) = value
"""



class BacktestResultParameters(BaseResultParameters):
    """
    Defines the parameters for QuantConnect.Packets.BacktestResult
    
    BacktestResultParameters(charts: IDictionary[str, Chart], orders: IDictionary[int, Order], profitLoss: IDictionary[DateTime, Decimal], statistics: IDictionary[str, str], runtimeStatistics: IDictionary[str, str], rollingWindow: Dictionary[str, AlgorithmPerformance], orderEvents: List[OrderEvent], totalPerformance: AlgorithmPerformance, alphaRuntimeStatistics: AlphaRuntimeStatistics)
    """
    @staticmethod # known case of __new__
    def __new__(self, charts, orders, profitLoss, statistics, runtimeStatistics, rollingWindow, orderEvents, totalPerformance, alphaRuntimeStatistics):
        """ __new__(cls: type, charts: IDictionary[str, Chart], orders: IDictionary[int, Order], profitLoss: IDictionary[DateTime, Decimal], statistics: IDictionary[str, str], runtimeStatistics: IDictionary[str, str], rollingWindow: Dictionary[str, AlgorithmPerformance], orderEvents: List[OrderEvent], totalPerformance: AlgorithmPerformance, alphaRuntimeStatistics: AlphaRuntimeStatistics) """
        pass

    RollingWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rolling window detailed statistics.

Get: RollingWindow(self: BacktestResultParameters) -> Dictionary[str, AlgorithmPerformance]

Set: RollingWindow(self: BacktestResultParameters) = value
"""

    TotalPerformance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rolling window detailed statistics.

Get: TotalPerformance(self: BacktestResultParameters) -> AlgorithmPerformance

Set: TotalPerformance(self: BacktestResultParameters) = value
"""



class Breakpoint(object):
    """
    A debugging breakpoint
    
    Breakpoint()
    """
    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The file name

Get: FileName(self: Breakpoint) -> str

Set: FileName(self: Breakpoint) = value
"""

    LineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The line number

Get: LineNumber(self: Breakpoint) -> int

Set: LineNumber(self: Breakpoint) = value
"""



class HistoryResult(object):
    """
    Provides a container for results from history requests. This contains
                the file path relative to the /Data folder where the data can be written
    """
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, type: HistoryResultType) """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of history result

Get: Type(self: HistoryResult) -> HistoryResultType

"""



class CompletedHistoryResult(HistoryResult):
    """
    Specifies the completed message from a history result
    
    CompletedHistoryResult()
    """

class Controls(object):
    """
    Specifies values used to control algorithm limits
    
    Controls()
    """
    def GetLimit(self, resolution):
        """
        GetLimit(self: Controls, resolution: Resolution) -> int
        
            Gets the maximum number of subscriptions for the 
             specified resolution
        """
        pass

    BacktestingMaxOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximimum number of orders we'll allow in a backtest.

Get: BacktestingMaxOrders(self: Controls) -> int

Set: BacktestingMaxOrders(self: Controls) = value
"""


    BacktestingMaxInsights = None
    BacktestLogLimit = None
    CpuAllocation = None
    DailyLogLimit = None
    DataResolutionPermissions = None
    MaximumDataPointsPerChartSeries = None
    MinuteLimit = None
    PersistenceIntervalSeconds = None
    RamAllocation = None
    RemainingLogAllowance = None
    SecondLimit = None
    SecondTimeOut = None
    StorageFileCount = None
    StorageLimitMB = None
    StoragePermissions = None
    StreamingDataPermissions = None
    TickLimit = None
    TrainingLimits = None


class DebugPacket(Packet):
    """
    Send a simple debug message from the users algorithm to the console.
    
    DebugPacket()
    DebugPacket(projectId: int, algorithmId: str, compileId: str, message: str, toast: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, projectId=None, algorithmId=None, compileId=None, message=None, toast=None):
        """
        __new__(cls: type)
        __new__(cls: type, packetType: PacketType)
        __new__(cls: type, projectId: int, algorithmId: str, compileId: str, message: str, toast: bool)
        """
        pass

    AlgorithmId = None
    CompileId = None
    Message = None
    ProjectId = None
    Toast = None


class ErrorHistoryResult(HistoryResult):
    """
    Specfies an error message in a history result
    
    ErrorHistoryResult()
    ErrorHistoryResult(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, message=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        """
        pass

    Message = None


class FileHistoryResult(HistoryResult):
    """
    Defines requested file data for a history request
    
    FileHistoryResult()
    FileHistoryResult(filepath: str, file: Array[Byte])
    """
    @staticmethod # known case of __new__
    def __new__(self, filepath=None, file=None):
        """
        __new__(cls: type)
        __new__(cls: type, filepath: str, file: Array[Byte])
        """
        pass

    File = None
    Filepath = None


class HandledErrorPacket(Packet):
    """
    Algorithm runtime error packet from the lean engine. 
                This is a managed error which stops the algorithm execution.
    
    HandledErrorPacket()
    HandledErrorPacket(algorithmId: str, message: str, stacktrace: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, algorithmId=None, message=None, stacktrace=None):
        """
        __new__(cls: type)
        __new__(cls: type, algorithmId: str, message: str, stacktrace: str)
        """
        pass

    AlgorithmId = None
    Message = None
    StackTrace = None


class HistoryPacket(Packet):
    """
    Packet for history jobs
    
    HistoryPacket()
    """
    QueueName = None
    Requests = None


class HistoryRequest(object):
    """
    Specifies request parameters for a single historical request.
                A HistoryPacket is made of multiple requests for data. These
                are used to request data during live mode from a data server
    
    HistoryRequest()
    """
    EndTimeUtc = None
    Resolution = None
    StartTimeUtc = None
    Symbol = None
    TickType = None


class HistoryResultType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies various types of history results
    
    enum HistoryResultType, values: Completed (2), Error (3), File (0), Status (1)
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
    Error = None
    File = None
    Status = None
    value__ = None


class LeakyBucketControlParameters(object):
    """
    Provides parameters that control the behavior of a leaky bucket rate limiting algorithm. The
                parameter names below are phrased in the positive, such that the bucket is filled up over time
                vs leaking out over time.
    
    LeakyBucketControlParameters()
    LeakyBucketControlParameters(capacity: int, refillAmount: int, timeIntervalMinutes: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, capacity=None, refillAmount=None, timeIntervalMinutes=None):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int, refillAmount: int, timeIntervalMinutes: int)
        """
        pass

    Capacity = None
    DefaultCapacity = 120
    DefaultRefillAmount = 18
    DefaultTimeInterval = 1440
    RefillAmount = None
    TimeIntervalMinutes = None


class LiveResult(Result):
    """
    Live results object class for packaging live result data.
    
    LiveResult()
    LiveResult(parameters: LiveResultParameters)
    """
    @staticmethod # known case of __new__
    def __new__(self, parameters=None):
        """
        __new__(cls: type)
        __new__(cls: type, parameters: LiveResultParameters)
        """
        pass

    Cash = None
    Holdings = None


class LiveResultPacket(Packet):
    """
    Live result packet from a lean engine algorithm.
    
    LiveResultPacket()
    LiveResultPacket(json: str)
    LiveResultPacket(job: LiveNodePacket, results: LiveResult)
    """
    @staticmethod
    def CreateEmpty(job):
        """
        CreateEmpty(job: LiveNodePacket) -> LiveResultPacket
        
            Creates an empty result packet, useful when the 
             algorithm fails to initialize
        
        
            job: The associated job packet
            Returns: An empty result packet
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, json: str)
        __new__(cls: type, job: LiveNodePacket, results: LiveResult)
        """
        pass

    CompileId = None
    DeployId = None
    ProcessingTime = None
    ProjectId = None
    Results = None
    SessionId = None
    UserId = None


class LiveResultParameters(BaseResultParameters):
    """
    Defines the parameters for QuantConnect.Packets.LiveResult
    
    LiveResultParameters(charts: IDictionary[str, Chart], orders: IDictionary[int, Order], profitLoss: IDictionary[DateTime, Decimal], holdings: IDictionary[str, Holding], cashBook: CashBook, statistics: IDictionary[str, str], runtimeStatistics: IDictionary[str, str], orderEvents: List[OrderEvent], serverStatistics: IDictionary[str, str], alphaRuntimeStatistics: AlphaRuntimeStatistics)
    """
    @staticmethod # known case of __new__
    def __new__(self, charts, orders, profitLoss, holdings, cashBook, statistics, runtimeStatistics, orderEvents, serverStatistics, alphaRuntimeStatistics):
        """ __new__(cls: type, charts: IDictionary[str, Chart], orders: IDictionary[int, Order], profitLoss: IDictionary[DateTime, Decimal], holdings: IDictionary[str, Holding], cashBook: CashBook, statistics: IDictionary[str, str], runtimeStatistics: IDictionary[str, str], orderEvents: List[OrderEvent], serverStatistics: IDictionary[str, str], alphaRuntimeStatistics: AlphaRuntimeStatistics) """
        pass

    CashBook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Cashbook for the algorithm's live results.

Get: CashBook(self: LiveResultParameters) -> CashBook

Set: CashBook(self: LiveResultParameters) = value
"""

    Holdings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Holdings dictionary of algorithm holdings information

Get: Holdings(self: LiveResultParameters) -> IDictionary[str, Holding]

Set: Holdings(self: LiveResultParameters) = value
"""

    ServerStatistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Server status information, including CPU/RAM usage, ect...

Get: ServerStatistics(self: LiveResultParameters) -> IDictionary[str, str]

Set: ServerStatistics(self: LiveResultParameters) = value
"""



class LogPacket(Packet):
    """
    Simple log message instruction from the lean engine.
    
    LogPacket()
    LogPacket(algorithmId: str, message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, algorithmId=None, message=None):
        """
        __new__(cls: type)
        __new__(cls: type, algorithmId: str, message: str)
        """
        pass

    AlgorithmId = None
    Message = None


class MarketHours(object):
    """
    Market open hours model for pre, normal and post market hour definitions.
    
    MarketHours(referenceDate: DateTime, defaultStart: float, defaultEnd: float)
    """
    @staticmethod # known case of __new__
    def __new__(self, referenceDate, defaultStart, defaultEnd):
        """ __new__(cls: type, referenceDate: DateTime, defaultStart: float, defaultEnd: float) """
        pass

    End = None
    Start = None


class MarketToday(object):
    """
    Market today information class
    
    MarketToday()
    """
    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Date this packet was generated.

Get: Date(self: MarketToday) -> DateTime

Set: Date(self: MarketToday) = value
"""


    Open = None
    PostMarket = None
    PreMarket = None
    Status = None


class OrderEventPacket(Packet):
    """
    Order event packet for passing updates on the state of an order to the portfolio.
    
    OrderEventPacket()
    OrderEventPacket(algorithmId: str, eventOrder: OrderEvent)
    """
    @staticmethod # known case of __new__
    def __new__(self, algorithmId=None, eventOrder=None):
        """
        __new__(cls: type)
        __new__(cls: type, algorithmId: str, eventOrder: OrderEvent)
        """
        pass

    AlgorithmId = None
    Event = None


class PacketType(Enum, IComparable, IFormattable, IConvertible):
    """
    Classifications of internal packet system
    
    enum PacketType, values: AlgorithmNode (1), AlgorithmStatus (12), AlphaHeartbeat (32), AlphaNode (30), AlphaResult (28), AlphaWork (29), AutocompleteResult (3), AutocompleteWork (2), BacktestError (11), BacktestNode (4), BacktestResult (5), BacktestWork (6), BuildError (15), BuildSuccess (14), BuildWork (13), CommandResult (23), Debug (19), DebuggingStatus (33), Documentation (26), DocumentationResult (25), GitHubHook (24), HandledError (17), History (22), LiveNode (7), LiveResult (8), LiveWork (9), Log (18), None (0), OrderEvent (20), RegressionAlgorithm (31), RuntimeError (16), SecurityTypes (10), Success (21), SystemDebug (27)
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

    AlgorithmNode = None
    AlgorithmStatus = None
    AlphaHeartbeat = None
    AlphaNode = None
    AlphaResult = None
    AlphaWork = None
    AutocompleteResult = None
    AutocompleteWork = None
    BacktestError = None
    BacktestNode = None
    BacktestResult = None
    BacktestWork = None
    BuildError = None
    BuildSuccess = None
    BuildWork = None
    CommandResult = None
    Debug = None
    DebuggingStatus = None
    Documentation = None
    DocumentationResult = None
    GitHubHook = None
    HandledError = None
    History = None
    LiveNode = None
    LiveResult = None
    LiveWork = None
    Log = None
    None = None
    OrderEvent = None
    RegressionAlgorithm = None
    RuntimeError = None
    SecurityTypes = None
    Success = None
    SystemDebug = None
    value__ = None


class RuntimeErrorPacket(Packet):
    """
    Algorithm runtime error packet from the lean engine. 
                This is a managed error which stops the algorithm execution.
    
    RuntimeErrorPacket()
    RuntimeErrorPacket(userId: int, algorithmId: str, message: str, stacktrace: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, userId=None, algorithmId=None, message=None, stacktrace=None):
        """
        __new__(cls: type)
        __new__(cls: type, userId: int, algorithmId: str, message: str, stacktrace: str)
        """
        pass

    AlgorithmId = None
    Message = None
    StackTrace = None
    UserId = None


class SecurityTypesPacket(Packet):
    """
    Security types packet contains information on the markets the user data has requested.
    
    SecurityTypesPacket()
    """
    TypesCSV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """CSV formatted, lower case list of SecurityTypes for the web API.

Get: TypesCSV(self: SecurityTypesPacket) -> str

"""


    Types = None


class StatusHistoryResult(HistoryResult):
    """
    Specifies the progress of a request
    
    StatusHistoryResult()
    StatusHistoryResult(progress: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, progress=None):
        """
        __new__(cls: type)
        __new__(cls: type, progress: int)
        """
        pass

    Progress = None


class SystemDebugPacket(DebugPacket):
    """
    Debug packets generated by Lean
    
    SystemDebugPacket()
    SystemDebugPacket(projectId: int, algorithmId: str, compileId: str, message: str, toast: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, projectId=None, algorithmId=None, compileId=None, message=None, toast=None):
        """
        __new__(cls: type)
        __new__(cls: type, projectId: int, algorithmId: str, compileId: str, message: str, toast: bool)
        """
        pass


