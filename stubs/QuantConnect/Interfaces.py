# encoding: utf-8
# module QuantConnect.Interfaces calls itself Interfaces
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AlgorithmEvent(MulticastDelegate, ICloneable, ISerializable):
    """ AlgorithmEvent[T](object: object, method: IntPtr) """
    def BeginInvoke(self, algorithm, eventData, callback, object):
        """ BeginInvoke(self: AlgorithmEvent[T], algorithm: IAlgorithm, eventData: T, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: AlgorithmEvent[T], result: IAsyncResult) """
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

    def Invoke(self, algorithm, eventData):
        """ Invoke(self: AlgorithmEvent[T], algorithm: IAlgorithm, eventData: T) """
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


class IAccountCurrencyProvider:
    """ A reduced interface for an account currency provider """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AccountCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the account currency

Get: AccountCurrency(self: IAccountCurrencyProvider) -> str

"""



class ISecurityInitializerProvider:
    """ Reduced interface which provides an instance which implements QuantConnect.Securities.ISecurityInitializer """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    SecurityInitializer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an instance that is to be used to initialize newly created securities.

Get: SecurityInitializer(self: ISecurityInitializerProvider) -> ISecurityInitializer

"""



class IAlgorithm(ISecurityInitializerProvider, IAccountCurrencyProvider):
    """
    Interface for QuantConnect algorithm implementations. All algorithms must implement these
                basic members to allow interaction with the Lean Backtesting Engine.
    """
    def AddChart(self, chart):
        """
        AddChart(self: IAlgorithm, chart: Chart)
            Add a Chart object to algorithm collection
        
            chart: Chart object to add to collection.
        """
        pass

    def AddFutureContract(self, symbol, resolution, fillDataForward, leverage):
        """ AddFutureContract(self: IAlgorithm, symbol: Symbol, resolution: Nullable[Resolution], fillDataForward: bool, leverage: Decimal) -> Future """
        pass

    def AddOptionContract(self, symbol, resolution, fillDataForward, leverage):
        """ AddOptionContract(self: IAlgorithm, symbol: Symbol, resolution: Nullable[Resolution], fillDataForward: bool, leverage: Decimal) -> Option """
        pass

    def AddSecurity(self, securityType, symbol, resolution, market, fillDataForward, leverage, extendedMarketHours):
        """ AddSecurity(self: IAlgorithm, securityType: SecurityType, symbol: str, resolution: Nullable[Resolution], market: str, fillDataForward: bool, leverage: Decimal, extendedMarketHours: bool) -> Security """
        pass

    def Debug(self, message):
        """
        Debug(self: IAlgorithm, message: str)
            Send debug message
        """
        pass

    def Error(self, message):
        """
        Error(self: IAlgorithm, message: str)
            Send an error message for the algorithm
        
            message: String message
        """
        pass

    def GetChartUpdates(self, clearChartData):
        """
        GetChartUpdates(self: IAlgorithm, clearChartData: bool) -> List[Chart]
        
            Get the chart updates since the last request:
            Returns: List of Chart Updates
        """
        pass

    def GetLocked(self):
        """
        GetLocked(self: IAlgorithm) -> bool
        
            Gets whether or not this algorithm has been 
             locked and fully initialized
        """
        pass

    def GetParameter(self, name):
        """
        GetParameter(self: IAlgorithm, name: str) -> str
        
            Gets the parameter with the specified name. If a 
             parameter
                    with the specified name 
             does not exist, null is returned
        
        
            name: The name of the parameter to get
            Returns: The value of the specified parameter, or null if 
             not found
        """
        pass

    def GetWarmupHistoryRequests(self):
        """
        GetWarmupHistoryRequests(self: IAlgorithm) -> IEnumerable[HistoryRequest]
        
            Gets the date/time warmup should begin
        """
        pass

    def Initialize(self):
        """
        Initialize(self: IAlgorithm)
            Initialise the Algorithm and Prepare Required 
             Data:
        """
        pass

    def Liquidate(self, symbolToLiquidate, tag):
        """
        Liquidate(self: IAlgorithm, symbolToLiquidate: Symbol, tag: str) -> List[int]
        
            Liquidate your portfolio holdings:
        
            symbolToLiquidate: Specific asset to liquidate, defaults to all.
            tag: Custom tag to know who is calling this.
            Returns: list of order ids
        """
        pass

    def Log(self, message):
        """
        Log(self: IAlgorithm, message: str)
            Save entry to the Log
        
            message: String message
        """
        pass

    def OnAssignmentOrderEvent(self, assignmentEvent):
        """
        OnAssignmentOrderEvent(self: IAlgorithm, assignmentEvent: OrderEvent)
            Option assignment event handler. On an option 
             assignment event for short legs the resulting 
             information is passed to this method.
        
        
            assignmentEvent: Option exercise event details containing details 
             of the assignment
        """
        pass

    def OnBrokerageDisconnect(self):
        """
        OnBrokerageDisconnect(self: IAlgorithm)
            Brokerage disconnected event handler. This method 
             is called when the brokerage connection is lost.
        """
        pass

    def OnBrokerageMessage(self, messageEvent):
        """
        OnBrokerageMessage(self: IAlgorithm, messageEvent: BrokerageMessageEvent)
            Brokerage message event handler. This method is 
             called for all types of brokerage messages.
        """
        pass

    def OnBrokerageReconnect(self):
        """
        OnBrokerageReconnect(self: IAlgorithm)
            Brokerage reconnected event handler. This method 
             is called when the brokerage connection is 
             restored after a disconnection.
        """
        pass

    def OnData(self, slice):
        """
        OnData(self: IAlgorithm, slice: Slice)
            v3.0 Handler for all data types
        
            slice: The current slice of data
        """
        pass

    def OnEndOfAlgorithm(self):
        """
        OnEndOfAlgorithm(self: IAlgorithm)
            Call this event at the end of the algorithm 
             running.
        """
        pass

    def OnEndOfDay(self, symbol=None):
        """
        OnEndOfDay(self: IAlgorithm)
            Call this method at the end of each day of data.
        OnEndOfDay(self: IAlgorithm, symbol: Symbol)
            Call this method at the end of each day of data.
        """
        pass

    def OnEndOfTimeStep(self):
        """
        OnEndOfTimeStep(self: IAlgorithm)
            Invoked at the end of every time step. This 
             allows the algorithm
                    to process 
             events before advancing to the next time step.
        """
        pass

    def OnFrameworkData(self, slice):
        """
        OnFrameworkData(self: IAlgorithm, slice: Slice)
            Used to send data updates to algorithm framework 
             models
        
        
            slice: The current data slice
        """
        pass

    def OnFrameworkSecuritiesChanged(self, changes):
        """
        OnFrameworkSecuritiesChanged(self: IAlgorithm, changes: SecurityChanges)
            Used to send security changes to algorithm 
             framework models
        
        
            changes: Security additions/removals for this time step
        """
        pass

    def OnMarginCall(self, requests):
        """ OnMarginCall(self: IAlgorithm, requests: List[SubmitOrderRequest]) """
        pass

    def OnMarginCallWarning(self):
        """
        OnMarginCallWarning(self: IAlgorithm)
            Margin call warning event handler. This method is 
             called when Portfolio.MarginRemaining is under 5% 
             of your Portfolio.TotalPortfolioValue
        """
        pass

    def OnOrderEvent(self, newEvent):
        """
        OnOrderEvent(self: IAlgorithm, newEvent: OrderEvent)
            EXPERTS ONLY:: [-!-Async Code-!-]
                    
             New order event handler: on order status changes 
             (filled, partially filled, cancelled etc).
        
        
            newEvent: Event information
        """
        pass

    def OnSecuritiesChanged(self, changes):
        """
        OnSecuritiesChanged(self: IAlgorithm, changes: SecurityChanges)
            Event fired each time that we add/remove 
             securities from the data feed
        
        
            changes: Security additions/removals for this time step
        """
        pass

    def OnWarmupFinished(self):
        """
        OnWarmupFinished(self: IAlgorithm)
            Called when the algorithm has completed 
             initialization and warm up.
        """
        pass

    def PostInitialize(self):
        """
        PostInitialize(self: IAlgorithm)
            Called by setup handlers after Initialize and 
             allows the algorithm a chance to organize
               
                  the data gather in the Initialize method
        """
        pass

    def RemoveSecurity(self, symbol):
        """
        RemoveSecurity(self: IAlgorithm, symbol: Symbol) -> bool
        
            Removes the security with the specified symbol. 
             This will cancel all
                    open orders and 
             then liquidate any existing holdings
        
        
            symbol: The symbol of the security to be removed
        """
        pass

    def SetAccountCurrency(self, accountCurrency):
        """
        SetAccountCurrency(self: IAlgorithm, accountCurrency: str)
            Sets the account currency cash symbol this 
             algorithm is to manage.
        
        
            accountCurrency: The account currency cash symbol to set
        """
        pass

    def SetAlgorithmId(self, algorithmId):
        """
        SetAlgorithmId(self: IAlgorithm, algorithmId: str)
            Set the algorithm Id for this backtest or live 
             run. This can be used to identify the order and 
             equity records.
        
        
            algorithmId: unique 32 character identifier for backtest or 
             live server
        """
        pass

    def SetApi(self, api):
        """
        SetApi(self: IAlgorithm, api: IApi)
            Provide the API for the algorithm.
        
            api: Initiated API
        """
        pass

    def SetAvailableDataTypes(self, availableDataTypes):
        """ SetAvailableDataTypes(self: IAlgorithm, availableDataTypes: Dictionary[SecurityType, List[TickType]]) """
        pass

    def SetBrokerageMessageHandler(self, handler):
        """
        SetBrokerageMessageHandler(self: IAlgorithm, handler: IBrokerageMessageHandler)
            Sets the implementation used to handle messages 
             from the brokerage.
                    The default 
             implementation will forward messages to debug or 
             error
                    and when a 
             QuantConnect.Brokerages.BrokerageMessageType.Error
              occurs, the algorithm
                    is stopped.
        
        
            handler: The message handler to use
        """
        pass

    def SetBrokerageModel(self, brokerageModel):
        """
        SetBrokerageModel(self: IAlgorithm, brokerageModel: IBrokerageModel)
            Sets the brokerage model used to resolve 
             transaction models, settlement models,
                  
               and brokerage specified ordering behaviors.
        
        
            brokerageModel: The brokerage model used to emulate the real
            
                     brokerage
        """
        pass

    def SetCash(self, *__args):
        """
        SetCash(self: IAlgorithm, startingCash: Decimal)
            Set the starting capital for the strategy
        
            startingCash: decimal starting capital, default $100,000
        SetCash(self: IAlgorithm, symbol: str, startingCash: Decimal, conversionRate: Decimal)
            Set the cash for the specified symbol
        
            symbol: The cash symbol to set
            startingCash: Decimal cash value of portfolio
            conversionRate: The current conversion rate for the
        """
        pass

    def SetCurrentSlice(self, slice):
        """
        SetCurrentSlice(self: IAlgorithm, slice: Slice)
            Sets the current slice
        
            slice: The Slice object
        """
        pass

    def SetDateTime(self, time):
        """
        SetDateTime(self: IAlgorithm, time: DateTime)
            Set the DateTime Frontier: This is the master 
             time and is
        """
        pass

    def SetEndDate(self, end):
        """
        SetEndDate(self: IAlgorithm, end: DateTime)
            Set the end date for a backtest.
        
            end: Datetime value for end date
        """
        pass

    def SetFinishedWarmingUp(self):
        """
        SetFinishedWarmingUp(self: IAlgorithm)
            Sets 
             QuantConnect.Interfaces.IAlgorithm.IsWarmingUp to 
             false to indicate this algorithm has finished its 
             warm up
        """
        pass

    def SetFutureChainProvider(self, futureChainProvider):
        """
        SetFutureChainProvider(self: IAlgorithm, futureChainProvider: IFutureChainProvider)
            Sets the future chain provider, used to get the 
             list of future contracts for an underlying symbol
        
        
            futureChainProvider: The future chain provider
        """
        pass

    def SetHistoryProvider(self, historyProvider):
        """
        SetHistoryProvider(self: IAlgorithm, historyProvider: IHistoryProvider)
            Set the historical data provider
        
            historyProvider: Historical data provider
        """
        pass

    def SetLiveMode(self, live):
        """
        SetLiveMode(self: IAlgorithm, live: bool)
            Set live mode state of the algorithm run: Public 
             setter for the algorithm property LiveMode.
        
        
            live: Bool live mode flag
        """
        pass

    def SetLocked(self):
        """
        SetLocked(self: IAlgorithm)
            Set the algorithm as initialized and locked. No 
             more cash or security changes.
        """
        pass

    def SetMaximumOrders(self, max):
        """
        SetMaximumOrders(self: IAlgorithm, max: int)
            Set the maximum number of orders the algortihm is 
             allowed to process.
        
        
            max: Maximum order count int
        """
        pass

    def SetObjectStore(self, objectStore):
        """
        SetObjectStore(self: IAlgorithm, objectStore: IObjectStore)
            Sets the object store
        
            objectStore: The object store
        """
        pass

    def SetOptionChainProvider(self, optionChainProvider):
        """
        SetOptionChainProvider(self: IAlgorithm, optionChainProvider: IOptionChainProvider)
            Sets the option chain provider, used to get the 
             list of option contracts for an underlying symbol
        
        
            optionChainProvider: The option chain provider
        """
        pass

    def SetParameters(self, parameters):
        """ SetParameters(self: IAlgorithm, parameters: Dictionary[str, str]) """
        pass

    def SetRunTimeError(self, exception):
        """
        SetRunTimeError(self: IAlgorithm, exception: Exception)
            Set the runtime error
        
            exception: Represents error that occur during execution
        """
        pass

    def SetStartDate(self, start):
        """
        SetStartDate(self: IAlgorithm, start: DateTime)
            Set the start date for the backtest
        
            start: Datetime Start date for backtest
        """
        pass

    def SetStatus(self, status):
        """
        SetStatus(self: IAlgorithm, status: AlgorithmStatus)
            Set the state of a live deployment
        
            status: Live deployment status
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AlgorithmId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """AlgorithmId for the backtest

Get: AlgorithmId(self: IAlgorithm) -> str

"""

    Benchmark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the function used to define the benchmark. This function will return
            the value of the benchmark at a requested date/time

Get: Benchmark(self: IAlgorithm) -> IBenchmark

"""

    BrokerageMessageHandler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brokerage message handler used to decide what to do
            with each message sent from the brokerage

Get: BrokerageMessageHandler(self: IAlgorithm) -> IBrokerageMessageHandler

Set: BrokerageMessageHandler(self: IAlgorithm) = value
"""

    BrokerageModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brokerage model used to emulate a real brokerage

Get: BrokerageModel(self: IAlgorithm) -> IBrokerageModel

"""

    CurrentSlice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the current Slice object

Get: CurrentSlice(self: IAlgorithm) -> Slice

"""

    DebugMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Debug messages from the strategy:

Get: DebugMessages(self: IAlgorithm) -> ConcurrentQueue[str]

"""

    EndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get Requested Backtest End Date

Get: EndDate(self: IAlgorithm) -> DateTime

"""

    ErrorMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Error messages from the strategy:

Get: ErrorMessages(self: IAlgorithm) -> ConcurrentQueue[str]

"""

    FutureChainProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the future chain provider, used to get the list of future contracts for an underlying symbol

Get: FutureChainProvider(self: IAlgorithm) -> IFutureChainProvider

"""

    HistoryProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the history provider for the algorithm

Get: HistoryProvider(self: IAlgorithm) -> IHistoryProvider

Set: HistoryProvider(self: IAlgorithm) = value
"""

    IsWarmingUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether or not this algorithm is still warming up

Get: IsWarmingUp(self: IAlgorithm) -> bool

"""

    LiveMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Algorithm is running on a live server.

Get: LiveMode(self: IAlgorithm) -> bool

"""

    LogMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Log messages from the strategy:

Get: LogMessages(self: IAlgorithm) -> ConcurrentQueue[str]

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Public name for the algorithm.

Get: Name(self: IAlgorithm) -> str

Set: Name(self: IAlgorithm) = value
"""

    Notify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Notification manager for storing and processing live event messages

Get: Notify(self: IAlgorithm) -> NotificationManager

"""

    ObjectStore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object store, used for persistence

Get: ObjectStore(self: IAlgorithm) -> ObjectStore

"""

    OptionChainProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the option chain provider, used to get the list of option contracts for an underlying symbol

Get: OptionChainProvider(self: IAlgorithm) -> IOptionChainProvider

"""

    Portfolio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Security portfolio management class provides wrapper and helper methods for the Security.Holdings class such as
            IsLong, IsShort, TotalProfit

Get: Portfolio(self: IAlgorithm) -> SecurityPortfolioManager

"""

    RunTimeError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the run time error from the algorithm, or null if none was encountered.

Get: RunTimeError(self: IAlgorithm) -> Exception

Set: RunTimeError(self: IAlgorithm) = value
"""

    RuntimeStatistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Customizable dynamic statistics displayed during live trading:

Get: RuntimeStatistics(self: IAlgorithm) -> ConcurrentDictionary[str, str]

"""

    Schedule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets schedule manager for adding/removing scheduled events

Get: Schedule(self: IAlgorithm) -> ScheduleManager

"""

    Securities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Security object collection class stores an array of objects representing representing each security/asset
            we have a subscription for.

Get: Securities(self: IAlgorithm) -> SecurityManager

"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the user settings for the algorithm

Get: Settings(self: IAlgorithm) -> IAlgorithmSettings

"""

    StartDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Algorithm start date for backtesting, set by the SetStartDate methods.

Get: StartDate(self: IAlgorithm) -> DateTime

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current status of the algorithm

Get: Status(self: IAlgorithm) -> AlgorithmStatus

Set: Status(self: IAlgorithm) = value
"""

    SubscriptionManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Data subscription manager controls the information and subscriptions the algorithms recieves.
            Subscription configurations can be added through the Subscription Manager.

Get: SubscriptionManager(self: IAlgorithm) -> SubscriptionManager

"""

    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Current date/time in the algorithm's local time zone

Get: Time(self: IAlgorithm) -> DateTime

"""

    TimeKeeper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time keeper instance

Get: TimeKeeper(self: IAlgorithm) -> ITimeKeeper

"""

    TimeZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time zone of the algorithm

Get: TimeZone(self: IAlgorithm) -> DateTimeZone

"""

    TradeBuilder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Trade Builder to generate trades from executions

Get: TradeBuilder(self: IAlgorithm) -> ITradeBuilder

"""

    Transactions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Security transaction manager class controls the store and processing of orders.

Get: Transactions(self: IAlgorithm) -> SecurityTransactionManager

"""

    UniverseManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of universes for the algorithm

Get: UniverseManager(self: IAlgorithm) -> UniverseManager

"""

    UniverseSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the subscription settings to be used when adding securities via universe selection

Get: UniverseSettings(self: IAlgorithm) -> UniverseSettings

"""

    UtcTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Current date/time in UTC.

Get: UtcTime(self: IAlgorithm) -> DateTime

"""


    InsightsGenerated = None


class IAlgorithmSettings:
    """ User settings for the algorithm which can be changed in the QuantConnect.Interfaces.IAlgorithm.Initialize method """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataSubscriptionLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets the maximum number of concurrent market data subscriptions available

Get: DataSubscriptionLimit(self: IAlgorithmSettings) -> int

Set: DataSubscriptionLimit(self: IAlgorithmSettings) = value
"""

    FreePortfolioValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets the SetHoldings buffers value.
            The buffer is used for orders not to be rejected due to volatility when using SetHoldings and CalculateOrderQuantity

Get: FreePortfolioValue(self: IAlgorithmSettings) -> Decimal

Set: FreePortfolioValue(self: IAlgorithmSettings) = value
"""

    FreePortfolioValuePercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets the SetHoldings buffers value percentage.
            This percentage will be used to set the QuantConnect.Interfaces.IAlgorithmSettings.FreePortfolioValue
            based on the QuantConnect.Securities.SecurityPortfolioManager.TotalPortfolioValue

Get: FreePortfolioValuePercentage(self: IAlgorithmSettings) -> Decimal

Set: FreePortfolioValuePercentage(self: IAlgorithmSettings) = value
"""

    LiquidateEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets/sets if Liquidate() is enabled

Get: LiquidateEnabled(self: IAlgorithmSettings) -> bool

Set: LiquidateEnabled(self: IAlgorithmSettings) = value
"""

    MaxAbsolutePortfolioTargetPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The absolute maximum valid total portfolio value target percentage

Get: MaxAbsolutePortfolioTargetPercentage(self: IAlgorithmSettings) -> Decimal

Set: MaxAbsolutePortfolioTargetPercentage(self: IAlgorithmSettings) = value
"""

    MinAbsolutePortfolioTargetPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The absolute minimum valid total portfolio value target percentage

Get: MinAbsolutePortfolioTargetPercentage(self: IAlgorithmSettings) -> Decimal

Set: MinAbsolutePortfolioTargetPercentage(self: IAlgorithmSettings) = value
"""

    RebalancePortfolioOnInsightChanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if should rebalance portfolio on new insights or expiration of insights. True by default

Get: RebalancePortfolioOnInsightChanges(self: IAlgorithmSettings) -> Nullable[bool]

Set: RebalancePortfolioOnInsightChanges(self: IAlgorithmSettings) = value
"""

    RebalancePortfolioOnSecurityChanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if should rebalance portfolio on security changes. True by default

Get: RebalancePortfolioOnSecurityChanges(self: IAlgorithmSettings) -> Nullable[bool]

Set: RebalancePortfolioOnSecurityChanges(self: IAlgorithmSettings) = value
"""

    StalePriceTimeSpan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minimum time span elapsed to consider a market fill price as stale (defaults to one hour)

Get: StalePriceTimeSpan(self: IAlgorithmSettings) -> TimeSpan

Set: StalePriceTimeSpan(self: IAlgorithmSettings) = value
"""



class ISubscriptionDataConfigProvider:
    """ Reduced interface which provides access to registered QuantConnect.Data.SubscriptionDataConfig """
    def GetSubscriptionDataConfigs(self, symbol, includeInternalConfigs):
        """
        GetSubscriptionDataConfigs(self: ISubscriptionDataConfigProvider, symbol: Symbol, includeInternalConfigs: bool) -> List[SubscriptionDataConfig]
        
            Gets a list of all registered 
             QuantConnect.Data.SubscriptionDataConfig for a 
             given QuantConnect.Symbol
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISubscriptionDataConfigService(ISubscriptionDataConfigProvider):
    """
    This interface exposes methods for creating a list of QuantConnect.Data.SubscriptionDataConfig for a given
                configuration
    """
    def Add(self, *__args):
        """
        Add(self: ISubscriptionDataConfigService, dataType: Type, symbol: Symbol, resolution: Nullable[Resolution], fillForward: bool, extendedMarketHours: bool, isFilteredSubscription: bool, isInternalFeed: bool, isCustomData: bool, dataNormalizationMode: DataNormalizationMode) -> SubscriptionDataConfig
        Add(self: ISubscriptionDataConfigService, symbol: Symbol, resolution: Nullable[Resolution], fillForward: bool, extendedMarketHours: bool, isFilteredSubscription: bool, isInternalFeed: bool, isCustomData: bool, subscriptionDataTypes: List[Tuple[Type, TickType]], dataNormalizationMode: DataNormalizationMode) -> List[SubscriptionDataConfig]
        """
        pass

    def LookupSubscriptionConfigDataTypes(self, symbolSecurityType, resolution, isCanonical):
        """
        LookupSubscriptionConfigDataTypes(self: ISubscriptionDataConfigService, symbolSecurityType: SecurityType, resolution: Resolution, isCanonical: bool) -> List[Tuple[Type, TickType]]
        
            Get the data feed types for a given 
             QuantConnect.SecurityTypeQuantConnect.Resolution
        
        
            symbolSecurityType: The QuantConnect.SecurityType used to determine 
             the types
        
            resolution: The resolution of the data requested
            isCanonical: Indicates whether the security is Canonical 
             (future and options)
        
            Returns: Types that should be added to the 
             QuantConnect.Data.SubscriptionDataConfig
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AvailableDataTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the available data types

Get: AvailableDataTypes(self: ISubscriptionDataConfigService) -> Dictionary[SecurityType, List[TickType]]

"""



class IAlgorithmSubscriptionManager(ISubscriptionDataConfigService, ISubscriptionDataConfigProvider):
    """ AlgorithmSubscriptionManager interface will manage the subscriptions for the SubscriptionManager """
    def SubscriptionManagerCount(self):
        """
        SubscriptionManagerCount(self: IAlgorithmSubscriptionManager) -> int
        
            Returns the amount of data config subscriptions 
             processed for the SubscriptionManager
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    SubscriptionManagerSubscriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all the current data config subscriptions that are being processed for the SubscriptionManager

Get: SubscriptionManagerSubscriptions(self: IAlgorithmSubscriptionManager) -> IEnumerable[SubscriptionDataConfig]

"""



class IApi(IDisposable):
    """ API for QuantConnect.com """
    def AddProjectFile(self, projectId, name, content):
        """
        AddProjectFile(self: IApi, projectId: int, name: str, content: str) -> ProjectFilesResponse
        
            Add a file to a project
        
            projectId: The project to which the file should be added
            name: The name of the new file
            content: The content of the new file
            Returns: QuantConnect.Api.ProjectFilesResponse that 
             includes information about the newly created file
        """
        pass

    def CreateBacktest(self, projectId, compileId, backtestName):
        """
        CreateBacktest(self: IApi, projectId: int, compileId: str, backtestName: str) -> Backtest
        
            Create a new backtest from a specified projectId 
             and compileId
        """
        pass

    def CreateCompile(self, projectId):
        """
        CreateCompile(self: IApi, projectId: int) -> Compile
        
            Create a new compile job request for this project 
             id.
        
        
            projectId: Project id we wish to compile.
            Returns: Compile object result
        """
        pass

    def CreateLiveAlgorithm(self, projectId, compileId, serverType, baseLiveAlgorithmSettings, versionId):
        """
        CreateLiveAlgorithm(self: IApi, projectId: int, compileId: str, serverType: str, baseLiveAlgorithmSettings: BaseLiveAlgorithmSettings, versionId: str) -> LiveAlgorithm
        
            Create a new live algorithm for a logged in user.
        
            projectId: Id of the project on QuantConnect
            compileId: Id of the compilation on QuantConnect
            serverType: Type of server instance that will run the 
             algorithm
        
            baseLiveAlgorithmSettings: Brokerage specific 
             QuantConnect.API.BaseLiveAlgorithmSettingsBaseLive
             AlgorithmSettings.
        
            versionId: The version identifier
            Returns: Information regarding the new algorithm 
             QuantConnect.API.LiveAlgorithm
        """
        pass

    def CreateProject(self, name, language):
        """
        CreateProject(self: IApi, name: str, language: Language) -> ProjectResponse
        
            Create a project with the specified name and 
             language via QuantConnect.com API
        
        
            name: Project name
            language: Programming language to use
            Returns: QuantConnect.Api.ProjectResponse that includes 
             information about the newly created project
        """
        pass

    def DeleteBacktest(self, projectId, backtestId):
        """
        DeleteBacktest(self: IApi, projectId: int, backtestId: str) -> RestResponse
        
            Delete a backtest from the specified project and 
             backtestId.
        
        
            projectId: Project for the backtest we want to delete
            backtestId: Backtest id we want to delete
            Returns: RestResponse on success
        """
        pass

    def DeleteProject(self, projectId):
        """
        DeleteProject(self: IApi, projectId: int) -> RestResponse
        
            Delete a specific project owned by the user from 
             QuantConnect.com
        
        
            projectId: Project id we own and wish to delete
            Returns: RestResponse indicating success
        """
        pass

    def DeleteProjectFile(self, projectId, name):
        """
        DeleteProjectFile(self: IApi, projectId: int, name: str) -> RestResponse
        
            Delete a file in a project
        
            projectId: Project id to which the file belongs
            name: The name of the file that should be deleted
            Returns: QuantConnect.Api.ProjectFilesResponse that 
             includes the information about all files in the 
             project
        """
        pass

    def Download(self, address, headers, userName, password):
        """ Download(self: IApi, address: str, headers: IEnumerable[KeyValuePair[str, str]], userName: str, password: str) -> str """
        pass

    def DownloadData(self, symbol, resolution, date):
        """
        DownloadData(self: IApi, symbol: Symbol, resolution: Resolution, date: DateTime) -> bool
        
            Method to download and save the data purchased 
             through QuantConnect
        
        
            symbol: Symbol of security of which data will be 
             requested.
        
            resolution: Resolution of data requested.
            date: Date of the data requested.
            Returns: A bool indicating whether the data was 
             successfully downloaded or not.
        """
        pass

    def GetAlgorithmStatus(self, algorithmId):
        """
        GetAlgorithmStatus(self: IApi, algorithmId: str) -> AlgorithmControl
        
            Get the algorithm current status, active or 
             cancelled from the user
        """
        pass

    def GetDividends(self, from, to):
        """
        GetDividends(self: IApi, from: DateTime, to: DateTime) -> List[Dividend]
        
            Gets all dividend events between the specified 
             times. From and to are inclusive.
        
        
            from: The first date to get dividend for
            to: The last date to get dividend for
            Returns: A list of all dividend in the specified range
        """
        pass

    def GetSplits(self, from, to):
        """
        GetSplits(self: IApi, from: DateTime, to: DateTime) -> List[Split]
        
            Gets all split events between the specified 
             times. From and to are inclusive.
        
        
            from: The first date to get splits for
            to: The last date to get splits for
            Returns: A list of all splits in the specified range
        """
        pass

    def Initialize(self, userId, token, dataFolder):
        """
        Initialize(self: IApi, userId: int, token: str, dataFolder: str)
            Initialize the control system
        """
        pass

    def LiquidateLiveAlgorithm(self, projectId):
        """
        LiquidateLiveAlgorithm(self: IApi, projectId: int) -> RestResponse
        
            Liquidate a live algorithm from the specified 
             project.
        
        
            projectId: Project for the live instance we want to stop
        """
        pass

    def ListBacktests(self, projectId):
        """
        ListBacktests(self: IApi, projectId: int) -> BacktestList
        
            Get a list of backtests for a specific project id
        
            projectId: Project id to search
            Returns: BacktestList container for list of backtests
        """
        pass

    def ListLiveAlgorithms(self, status, startTime, endTime):
        """ ListLiveAlgorithms(self: IApi, status: Nullable[AlgorithmStatus], startTime: Nullable[DateTime], endTime: Nullable[DateTime]) -> LiveList """
        pass

    def ListProjects(self):
        """
        ListProjects(self: IApi) -> ProjectResponse
        
            Read back a list of all projects on the account 
             for a user.
        
            Returns: Container for list of projects
        """
        pass

    def ReadBacktest(self, projectId, backtestId):
        """
        ReadBacktest(self: IApi, projectId: int, backtestId: str) -> Backtest
        
            Read out the full result of a specific backtest
        
            projectId: Project id for the backtest we'd like to read
            backtestId: Backtest id for the backtest we'd like to read
            Returns: Backtest result object
        """
        pass

    def ReadCompile(self, projectId, compileId):
        """
        ReadCompile(self: IApi, projectId: int, compileId: str) -> Compile
        
            Read a compile packet job result.
        
            projectId: Project id we sent for compile
            compileId: Compile id return from the creation request
            Returns: Compile object result
        """
        pass

    def ReadDataLink(self, symbol, resolution, date):
        """
        ReadDataLink(self: IApi, symbol: Symbol, resolution: Resolution, date: DateTime) -> Link
        
            Gets the link to the downloadable data.
        
            symbol: Symbol of security of which data will be 
             requested.
        
            resolution: Resolution of data requested.
            date: Date of the data requested.
            Returns: Link to the downloadable data.
        """
        pass

    def ReadLiveAlgorithm(self, projectId, deployId):
        """
        ReadLiveAlgorithm(self: IApi, projectId: int, deployId: str) -> LiveAlgorithmResults
        
            Read out a live algorithm in the project id 
             specified.
        
        
            projectId: Project id to read
            deployId: Specific instance id to read
            Returns: Live object with the results
        """
        pass

    def ReadLiveLogs(self, projectId, algorithmId, startTime, endTime):
        """ ReadLiveLogs(self: IApi, projectId: int, algorithmId: str, startTime: Nullable[DateTime], endTime: Nullable[DateTime]) -> LiveLog """
        pass

    def ReadPrices(self, symbols):
        """ ReadPrices(self: IApi, symbols: IEnumerable[Symbol]) -> PricesList """
        pass

    def ReadProject(self, projectId):
        """
        ReadProject(self: IApi, projectId: int) -> ProjectResponse
        
            Read in a project from the QuantConnect.com API.
        
            projectId: Project id you own
            Returns: QuantConnect.Api.ProjectResponse about a specific 
             project
        """
        pass

    def ReadProjectFile(self, projectId, fileName):
        """
        ReadProjectFile(self: IApi, projectId: int, fileName: str) -> ProjectFilesResponse
        
            Read a file in a project
        
            projectId: Project id to which the file belongs
            fileName: The name of the file
            Returns: QuantConnect.Api.ProjectFilesResponse that 
             includes the file information
        """
        pass

    def ReadProjectFiles(self, projectId):
        """
        ReadProjectFiles(self: IApi, projectId: int) -> ProjectFilesResponse
        
            Read all files in a project
        
            projectId: Project id to which the file belongs
            Returns: QuantConnect.Api.ProjectFilesResponse that 
             includes the information about all files in the 
             project
        """
        pass

    def SendStatistics(self, algorithmId, unrealized, fees, netProfit, holdings, equity, netReturn, volume, trades, sharpe):
        """
        SendStatistics(self: IApi, algorithmId: str, unrealized: Decimal, fees: Decimal, netProfit: Decimal, holdings: Decimal, equity: Decimal, netReturn: Decimal, volume: Decimal, trades: int, sharpe: float)
            Send the statistics to storage for performance 
             tracking.
        
        
            algorithmId: Identifier for algorithm
            unrealized: Unrealized gainloss
            fees: Total fees
            netProfit: Net profi
            holdings: Algorithm holdings
            equity: Total equity
            netReturn: Algorithm return
            volume: Volume traded
            trades: Total trades since inception
            sharpe: Sharpe ratio since inception
        """
        pass

    def SendUserEmail(self, algorithmId, subject, body):
        """
        SendUserEmail(self: IApi, algorithmId: str, subject: str, body: str)
            Send an email to the user associated with the 
             specified algorithm id
        
        
            algorithmId: The algorithm id
            subject: The email subject
            body: The email message body
        """
        pass

    def SetAlgorithmStatus(self, algorithmId, status, message):
        """
        SetAlgorithmStatus(self: IApi, algorithmId: str, status: AlgorithmStatus, message: str)
            Set the algorithm status from the worker to 
             update the UX e.g. if there was an error.
        
        
            algorithmId: Algorithm id we're setting.
            status: Status enum of the current worker
            message: Message for the algorithm status event
        """
        pass

    def StopLiveAlgorithm(self, projectId):
        """
        StopLiveAlgorithm(self: IApi, projectId: int) -> RestResponse
        
            Stop a live algorithm from the specified project.
        
            projectId: Project for the live algo we want to delete
        """
        pass

    def UpdateBacktest(self, projectId, backtestId, backtestName, backtestNote):
        """
        UpdateBacktest(self: IApi, projectId: int, backtestId: str, backtestName: str, backtestNote: str) -> RestResponse
        
            Update the backtest name
        
            projectId: Project id to update
            backtestId: Backtest id to update
            backtestName: New backtest name to set
            backtestNote: Note attached to the backtest
            Returns: Rest response on success
        """
        pass

    def UpdateProjectFileContent(self, projectId, fileName, newFileContents):
        """
        UpdateProjectFileContent(self: IApi, projectId: int, fileName: str, newFileContents: str) -> RestResponse
        
            Update the contents of a file
        
            projectId: Project id to which the file belongs
            fileName: The name of the file that should be updated
            newFileContents: The new contents of the file
            Returns: QuantConnect.Api.RestResponse indicating success
        """
        pass

    def UpdateProjectFileName(self, projectId, oldFileName, newFileName):
        """
        UpdateProjectFileName(self: IApi, projectId: int, oldFileName: str, newFileName: str) -> RestResponse
        
            Update the name of a file
        
            projectId: Project id to which the file belongs
            oldFileName: The current name of the file
            newFileName: The new name for the file
            Returns: QuantConnect.Api.RestResponse indicating success
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IBrokerageCashSynchronizer:
    """ Defines live brokerage cash synchronization operations. """
    def PerformCashSync(self, algorithm, currentTimeUtc, getTimeSinceLastFill):
        """ PerformCashSync(self: IBrokerageCashSynchronizer, algorithm: IAlgorithm, currentTimeUtc: DateTime, getTimeSinceLastFill: Func[TimeSpan]) -> bool """
        pass

    def ShouldPerformCashSync(self, currentTimeUtc):
        """
        ShouldPerformCashSync(self: IBrokerageCashSynchronizer, currentTimeUtc: DateTime) -> bool
        
            Returns whether the brokerage should perform the 
             cash synchronization
        
        
            currentTimeUtc: The current time (UTC)
            Returns: True if the cash sync should be performed
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    LastSyncDateTimeUtc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the datetime of the last sync (UTC)

Get: LastSyncDateTimeUtc(self: IBrokerageCashSynchronizer) -> DateTime

"""



class IBrokerage(IBrokerageCashSynchronizer, IDisposable):
    """
    Brokerage interface that defines the operations all brokerages must implement. The IBrokerage implementation
                must have a matching IBrokerageFactory implementation.
    """
    def CancelOrder(self, order):
        """
        CancelOrder(self: IBrokerage, order: Order) -> bool
        
            Cancels the order with the specified ID
        
            order: The order to cancel
            Returns: True if the request was made for the order to be 
             canceled, false otherwise
        """
        pass

    def Connect(self):
        """
        Connect(self: IBrokerage)
            Connects the client to the broker's remote servers
        """
        pass

    def Disconnect(self):
        """
        Disconnect(self: IBrokerage)
            Disconnects the client from the broker's remote 
             servers
        """
        pass

    def GetAccountHoldings(self):
        """
        GetAccountHoldings(self: IBrokerage) -> List[Holding]
        
            Gets all holdings for the account
            Returns: The current holdings from the account
        """
        pass

    def GetCashBalance(self):
        """
        GetCashBalance(self: IBrokerage) -> List[CashAmount]
        
            Gets the current cash balance for each currency 
             held in the brokerage account
        
            Returns: The current cash balance for each currency 
             available for trading
        """
        pass

    def GetHistory(self, request):
        """
        GetHistory(self: IBrokerage, request: HistoryRequest) -> IEnumerable[BaseData]
        
            Gets the history for the requested security
        
            request: The historical data request
            Returns: An enumerable of bars covering the span specified 
             in the request
        """
        pass

    def GetOpenOrders(self):
        """
        GetOpenOrders(self: IBrokerage) -> List[Order]
        
            Gets all open orders on the account
            Returns: The open orders returned from IB
        """
        pass

    def PlaceOrder(self, order):
        """
        PlaceOrder(self: IBrokerage, order: Order) -> bool
        
            Places a new order and assigns a new broker ID to 
             the order
        
        
            order: The order to be placed
            Returns: True if the request for a new order has been 
             placed, false otherwise
        """
        pass

    def UpdateOrder(self, order):
        """
        UpdateOrder(self: IBrokerage, order: Order) -> bool
        
            Updates the order with the same id
        
            order: The new order information
            Returns: True if the request was made for the order to be 
             updated, false otherwise
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AccountInstantlyUpdated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the brokerage will instantly update account balances

Get: AccountInstantlyUpdated(self: IBrokerage) -> bool

"""

    IsConnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if we're currently connected to the broker

Get: IsConnected(self: IBrokerage) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the brokerage

Get: Name(self: IBrokerage) -> str

"""


    AccountChanged = None
    Message = None
    OptionPositionAssigned = None
    OrderStatusChanged = None


class IBrokerageFactory(IDisposable):
    """ Defines factory types for brokerages. Every IBrokerage is expected to also implement an IBrokerageFactory. """
    def CreateBrokerage(self, job, algorithm):
        """
        CreateBrokerage(self: IBrokerageFactory, job: LiveNodePacket, algorithm: IAlgorithm) -> IBrokerage
        
            Creates a new IBrokerage instance
        
            job: The job packet to create the brokerage for
            algorithm: The algorithm instance
            Returns: A new brokerage instance
        """
        pass

    def CreateBrokerageMessageHandler(self, algorithm, job, api):
        """
        CreateBrokerageMessageHandler(self: IBrokerageFactory, algorithm: IAlgorithm, job: AlgorithmNodePacket, api: IApi) -> IBrokerageMessageHandler
        
            Gets a brokerage message handler
        """
        pass

    def GetBrokerageModel(self, orderProvider):
        """
        GetBrokerageModel(self: IBrokerageFactory, orderProvider: IOrderProvider) -> IBrokerageModel
        
            Gets a brokerage model that can be used to model 
             this brokerage's unique behaviors
        
        
            orderProvider: The order provider
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BrokerageData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brokerage data required to run the brokerage from configuration/disk

Get: BrokerageData(self: IBrokerageFactory) -> Dictionary[str, str]

"""

    BrokerageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of brokerage produced by this factory

Get: BrokerageType(self: IBrokerageFactory) -> Type

"""



class IBusyCollection(IDisposable):
    # no doc
    def Add(self, item, cancellationToken=None):
        """
        Add(self: IBusyCollection[T], item: T)
            Adds the items to this collection
        
            item: The item to be added
        Add(self: IBusyCollection[T], item: T, cancellationToken: CancellationToken)
            Adds the items to this collection
        
            item: The item to be added
            cancellationToken: A cancellation token to observer
        """
        pass

    def CompleteAdding(self):
        """
        CompleteAdding(self: IBusyCollection[T])
            Marks the collection as not accepting any more 
             additions
        """
        pass

    def GetConsumingEnumerable(self, cancellationToken=None):
        """
        GetConsumingEnumerable(self: IBusyCollection[T]) -> IEnumerable[T]
        
            Provides a consuming enumerable for items in this 
             collection.
        
            Returns: An enumerable that removes and returns items from 
             the collection
        
        GetConsumingEnumerable(self: IBusyCollection[T], cancellationToken: CancellationToken) -> IEnumerable[T]
        
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items held within this collection

Get: Count(self: IBusyCollection[T]) -> int

"""

    IsBusy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if processing, false otherwise

Get: IsBusy(self: IBusyCollection[T]) -> bool

"""

    WaitHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a wait handle that can be used to wait until this instance is done
            processing all of it's item

Get: WaitHandle(self: IBusyCollection[T]) -> WaitHandle

"""



class IDataCacheProvider(IDisposable):
    """ Defines a cache for data """
    def Fetch(self, key):
        """
        Fetch(self: IDataCacheProvider, key: str) -> Stream
        
            Fetch data from the cache
        
            key: A string representing the key of the cached data
            Returns: An System.IO.Stream of the cached data
        """
        pass

    def Store(self, key, data):
        """
        Store(self: IDataCacheProvider, key: str, data: Array[Byte])
            Store the data in the cache
        
            key: The source of the data, used as a key to retrieve 
             data in the cache
        
            data: The data to cache as a byte array
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsDataEphemeral = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property indicating the data is temporary in nature and should not be cached

Get: IsDataEphemeral(self: IDataCacheProvider) -> bool

"""



class IDataChannelProvider:
    """ Specifies data channel settings """
    def ShouldStreamSubscription(self, job, config):
        """
        ShouldStreamSubscription(self: IDataChannelProvider, job: LiveNodePacket, config: SubscriptionDataConfig) -> bool
        
            True if this subscription configuration should be 
             streamed
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDataPermissionManager:
    """ Entity in charge of handling data permissions """
    def AssertConfiguration(self, subscriptionDataConfig):
        """
        AssertConfiguration(self: IDataPermissionManager, subscriptionDataConfig: SubscriptionDataConfig)
            Will assert the requested configuration is valid 
             for the current job
        
        
            subscriptionDataConfig: The data subscription configuration to assert
        """
        pass

    def GetResolution(self, preferredResolution):
        """
        GetResolution(self: IDataPermissionManager, preferredResolution: Resolution) -> Resolution
        
            Gets a valid resolution to use for internal 
             subscriptions
        
            Returns: A permitted resolution for internal subscriptions
        """
        pass

    def Initialize(self, job):
        """
        Initialize(self: IDataPermissionManager, job: AlgorithmNodePacket)
            Initialize the data permission manager
        
            job: The job packet
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataChannelProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The data channel provider instance

Get: DataChannelProvider(self: IDataPermissionManager) -> IDataChannelProvider

"""



class IDataProvider:
    """
    Fetches a remote file for a security.
                Must save the file to Globals.DataFolder.
    """
    def Fetch(self, key):
        """
        Fetch(self: IDataProvider, key: str) -> Stream
        
            Retrieves data to be used in an algorithm
        
            key: A string representing where the data is stored
            Returns: A System.IO.Stream of the data requested
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDataProviderEvents:
    """ Events related to data providers """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DownloadFailed = None
    InvalidConfigurationDetected = None
    NumericalPrecisionLimited = None
    ReaderErrorDetected = None
    StartDateLimited = None


class IDataQueueHandler(IDisposable):
    """ Task requestor interface with cloud system """
    def GetNextTicks(self):
        """
        GetNextTicks(self: IDataQueueHandler) -> IEnumerable[BaseData]
        
            Get the next ticks from the live trading data 
             queue
        
            Returns: IEnumerable list of ticks since the last update.
        """
        pass

    def Subscribe(self, job, symbols):
        """ Subscribe(self: IDataQueueHandler, job: LiveNodePacket, symbols: IEnumerable[Symbol]) """
        pass

    def Unsubscribe(self, job, symbols):
        """ Unsubscribe(self: IDataQueueHandler, job: LiveNodePacket, symbols: IEnumerable[Symbol]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsConnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns whether the data provider is connected

Get: IsConnected(self: IDataQueueHandler) -> bool

"""



class IDataQueueUniverseProvider:
    """
    This interface allows interested parties to lookup or enumerate the available symbols. Data source exposes it if this feature is available.
                Availability of a symbol doesn't imply that it is possible to trade it. This is a data source specific interface, not broker specific.
    """
    def CanAdvanceTime(self, securityType):
        """
        CanAdvanceTime(self: IDataQueueUniverseProvider, securityType: SecurityType) -> bool
        
            Returns whether the time can be advanced or not.
        
            securityType: The security type
            Returns: true if the time can be advanced
        """
        pass

    def LookupSymbols(self, lookupName, securityType, includeExpired, securityCurrency, securityExchange):
        """
        LookupSymbols(self: IDataQueueUniverseProvider, lookupName: str, securityType: SecurityType, includeExpired: bool, securityCurrency: str, securityExchange: str) -> IEnumerable[Symbol]
        
            Method returns a collection of Symbols that are 
             available at the data source.
        
        
            lookupName: String representing the name to lookup
            securityType: Expected security type of the returned symbols 
             (if any)
        
            includeExpired: Include expired contracts
            securityCurrency: Expected security currency(if any)
            securityExchange: Expected security exchange name(if any)
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDownloadProvider:
    """ Wrapper on the API for downloading data for an algorithm. """
    def Download(self, address, headers, userName, password):
        """ Download(self: IDownloadProvider, address: str, headers: IEnumerable[KeyValuePair[str, str]], userName: str, password: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IExtendedDictionary:
    # no doc
    def clear(self):
        """
        clear(self: IExtendedDictionary[TKey, TValue])
            Removes all keys and values from the 
             QuantConnect.Interfaces.IExtendedDictionary.
        """
        pass

    def copy(self):
        """
        copy(self: IExtendedDictionary[TKey, TValue]) -> PyDict
        
            Creates a shallow copy of the 
             QuantConnect.Interfaces.IExtendedDictionary.
        
            Returns: Returns a shallow copy of the dictionary. It 
             doesn't modify the original dictionary.
        """
        pass

    def fromkeys(self, sequence, value=None):
        """
        fromkeys(self: IExtendedDictionary[TKey, TValue], sequence: Array[TKey]) -> PyDict
        fromkeys(self: IExtendedDictionary[TKey, TValue], sequence: Array[TKey], value: TValue) -> PyDict
        """
        pass

    def get(self, key, value=None):
        """
        get(self: IExtendedDictionary[TKey, TValue], key: TKey) -> TValue
        
            Returns the value for the specified key if key is 
             in dictionary.
        
        
            key: Key to be searched in the dictionary
            Returns: The value for the specified key if key is in 
             dictionary.
                    None if the key is not 
             found and value is not specified.
        
        get(self: IExtendedDictionary[TKey, TValue], key: TKey, value: TValue) -> TValue
        
            Returns the value for the specified key if key is 
             in dictionary.
        
        
            key: Key to be searched in the dictionary
            value: Value to be returned if the key is not found. The 
             default value is null.
        
            Returns: The value for the specified key if key is in 
             dictionary.
                    value if the key is not 
             found and value is specified.
        """
        pass

    def items(self):
        """
        items(self: IExtendedDictionary[TKey, TValue]) -> PyList
        
            Returns a view object that displays a list of 
             dictionary's (key, value) tuple pairs.
        
            Returns: Returns a view object that displays a list of a 
             given dictionary's (key, value) tuple pair.
        """
        pass

    def keys(self):
        """
        keys(self: IExtendedDictionary[TKey, TValue]) -> PyList
        
            Returns a view object that displays a list of all 
             the keys in the dictionary
        
            Returns: Returns a view object that displays a list of all 
             the keys.
                    When the dictionary is 
             changed, the view object also reflect these 
             changes.
        """
        pass

    def pop(self, key, default_value=None):
        """
        pop(self: IExtendedDictionary[TKey, TValue], key: TKey) -> TValue
        
            Removes and returns an element from a dictionary 
             having the given key.
        
        
            key: Key which is to be searched for removal
            Returns: If key is found - removed/popped element from the 
             dictionary
                    If key is not found - 
             KeyError exception is raised
        
        pop(self: IExtendedDictionary[TKey, TValue], key: TKey, default_value: TValue) -> TValue
        
            Removes and returns an element from a dictionary 
             having the given key.
        
        
            key: Key which is to be searched for removal
            default_value: Value which is to be returned when the key is not 
             in the dictionary
        
            Returns: If key is found - removed/popped element from the 
             dictionary
                    If key is not found - 
             value specified as the second argument(default)
        """
        pass

    def popitem(self):
        """
        popitem(self: IExtendedDictionary[TKey, TValue]) -> PyTuple
        
            Returns and removes an arbitrary element (key, 
             value) pair from the dictionary.
        
            Returns: Returns an arbitrary element (key, value) pair 
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

    def setdefault(self, key, default_value=None):
        """
        setdefault(self: IExtendedDictionary[TKey, TValue], key: TKey) -> TValue
        
            Returns the value of a key (if the key is in 
             dictionary). If not, it inserts key with a value 
             to the dictionary.
        
        
            key: Key with null/None value is inserted to the 
             dictionary if key is not in the dictionary.
        
            Returns: The value of the key if it is in the dictionary
         
                        None if key is not in the dictionary
        
        setdefault(self: IExtendedDictionary[TKey, TValue], key: TKey, default_value: TValue) -> TValue
        
            Returns the value of a key (if the key is in 
             dictionary). If not, it inserts key with a value 
             to the dictionary.
        
        
            key: Key with a value default_value is inserted to the 
             dictionary if key is not in the dictionary.
        
            default_value: Default value
            Returns: The value of the key if it is in the dictionary
         
                        default_value if key is not in the 
             dictionary and default_value is specified
        """
        pass

    def update(self, other):
        """
        update(self: IExtendedDictionary[TKey, TValue], other: PyObject)
            Updates the dictionary with the elements from the 
             another dictionary object or from an iterable of 
             key/value pairs.
                    The update() method 
             adds element(s) to the dictionary if the key is 
             not in the dictionary.If the key is in the 
             dictionary, it updates the key with the new 
             value.
        
        
            other: Takes either a dictionary or an iterable object 
             of key/value pairs (generally tuples).
        """
        pass

    def values(self):
        """
        values(self: IExtendedDictionary[TKey, TValue]) -> PyList
        
            Returns a view object that displays a list of all 
             the values in the dictionary.
        
            Returns: Returns a view object that displays a list of all 
             values in a given dictionary.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IFactorFileProvider:
    """ Provides instances of QuantConnect.Data.Auxiliary.FactorFile at run time """
    def Get(self, symbol):
        """
        Get(self: IFactorFileProvider, symbol: Symbol) -> FactorFile
        
            Gets a QuantConnect.Data.Auxiliary.FactorFile 
             instance for the specified symbol, or null if not 
             found
        
        
            symbol: The security's symbol whose factor file we seek
            Returns: The resolved factor file, or null if not found
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IFutureChainProvider:
    """ Provides the full future chain for a given underlying. """
    def GetFutureContractList(self, symbol, date):
        """
        GetFutureContractList(self: IFutureChainProvider, symbol: Symbol, date: DateTime) -> IEnumerable[Symbol]
        
            Gets the list of future contracts for a given 
             underlying symbol
        
        
            symbol: The underlying symbol
            date: The date for which to request the future chain 
             (only used in backtesting)
        
            Returns: The list of future contracts
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IHistoryProvider(IDataProviderEvents):
    """ Provides historical data to an algorithm at runtime """
    def GetHistory(self, requests, sliceTimeZone):
        """ GetHistory(self: IHistoryProvider, requests: IEnumerable[HistoryRequest], sliceTimeZone: DateTimeZone) -> IEnumerable[Slice] """
        pass

    def Initialize(self, parameters):
        """
        Initialize(self: IHistoryProvider, parameters: HistoryProviderInitializeParameters)
            Initializes this history provider to work for the 
             specified job
        
        
            parameters: The initialization parameters
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataPointCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total number of data points emitted by this history provider

Get: DataPointCount(self: IHistoryProvider) -> int

"""



class IJobQueueHandler:
    """ Task requestor interface with cloud system """
    def AcknowledgeJob(self, job):
        """
        AcknowledgeJob(self: IJobQueueHandler, job: AlgorithmNodePacket)
            Signal task complete
        
            job: Work to do.
        """
        pass

    def Initialize(self, api):
        """
        Initialize(self: IJobQueueHandler, api: IApi)
            Initialize the internal state
        """
        pass

    def NextJob(self, algorithmPath):
        """
        NextJob(self: IJobQueueHandler) -> (AlgorithmNodePacket, str)
        
            Request the next task to run through the engine:
            Returns: Algorithm job to process
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IMapFileProvider:
    """ Provides instances of QuantConnect.Data.Auxiliary.MapFileResolver at run time """
    def Get(self, market):
        """
        Get(self: IMapFileProvider, market: str) -> MapFileResolver
        
            Gets a 
             QuantConnect.Data.Auxiliary.MapFileResolver 
             representing all the map
                    files for 
             the specified market
        
        
            market: The equity market, for example, 'usa'
            Returns: A QuantConnect.Data.Auxiliary.MapFileResolver 
             containing all map files for the specified market
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IMessagingHandler(IDisposable):
    """
    Messaging System Plugin Interface. 
                Provides a common messaging pattern between desktop and cloud implementations of QuantConnect.
    """
    def Initialize(self):
        """
        Initialize(self: IMessagingHandler)
            Initialize the Messaging System Plugin.
        """
        pass

    def Send(self, packet):
        """
        Send(self: IMessagingHandler, packet: Packet)
            Send any message with a base type of Packet.
        
            packet: Packet of data to send via the messaging system 
             plugin
        """
        pass

    def SendNotification(self, notification):
        """
        SendNotification(self: IMessagingHandler, notification: Notification)
            Send any notification with a base type of 
             Notification.
        
        
            notification: The notification to be sent.
        """
        pass

    def SetAuthentication(self, job):
        """
        SetAuthentication(self: IMessagingHandler, job: AlgorithmNodePacket)
            Set the user communication channel
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    HasSubscribers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether this messaging handler has any current subscribers.
            When set to false, messages won't be sent.

Get: HasSubscribers(self: IMessagingHandler) -> bool

Set: HasSubscribers(self: IMessagingHandler) = value
"""



class IObjectStore(IDisposable, IEnumerable[KeyValuePair[str, Array[Byte]]], IEnumerable):
    """ Provides object storage for data persistence. """
    def ContainsKey(self, key):
        """
        ContainsKey(self: IObjectStore, key: str) -> bool
        
            Determines whether the store contains data for 
             the specified key
        
        
            key: The object key
            Returns: True if the key was found
        """
        pass

    def Delete(self, key):
        """
        Delete(self: IObjectStore, key: str) -> bool
        
            Deletes the object data for the specified key
        
            key: The object key
            Returns: True if the delete operation was successful
        """
        pass

    def GetFilePath(self, key):
        """
        GetFilePath(self: IObjectStore, key: str) -> str
        
            Returns the file path for the specified key
        
            key: The object key
            Returns: The path for the file
        """
        pass

    def Initialize(self, algorithmName, userId, projectId, userToken, controls):
        """
        Initialize(self: IObjectStore, algorithmName: str, userId: int, projectId: int, userToken: str, controls: Controls)
            Initializes the object store
        
            algorithmName: The algorithm name
            userId: The user id
            projectId: The project id
            userToken: The user token
            controls: The job controls instance
        """
        pass

    def ReadBytes(self, key):
        """
        ReadBytes(self: IObjectStore, key: str) -> Array[Byte]
        
            Returns the object data for the specified key
        
            key: The object key
            Returns: A byte array containing the data
        """
        pass

    def SaveBytes(self, key, contents):
        """
        SaveBytes(self: IObjectStore, key: str, contents: Array[Byte]) -> bool
        
            Saves the object data for the specified key
        
            key: The object key
            contents: The object data
            Returns: True if the save operation was successful
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[str, Array[Byte]]](enumerable: IEnumerable[KeyValuePair[str, Array[Byte]]], value: KeyValuePair[str, Array[Byte]]) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    ErrorRaised = None


class IOptionChainProvider:
    """ Provides the full option chain for a given underlying. """
    def GetOptionContractList(self, symbol, date):
        """
        GetOptionContractList(self: IOptionChainProvider, symbol: Symbol, date: DateTime) -> IEnumerable[Symbol]
        
            Gets the list of option contracts for a given 
             underlying symbol
        
        
            symbol: The underlying symbol
            date: The date for which to request the option chain 
             (only used in backtesting)
        
            Returns: The list of option contracts
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISecurityPrice:
    """
    Reduced interface which allows setting and accessing
                price properties for a QuantConnect.Securities.Security
    """
    def GetLastData(self):
        """
        GetLastData(self: ISecurityPrice) -> BaseData
        
            Get the last price update set to the security.
            Returns: BaseData object for this security
        """
        pass

    def SetMarketPrice(self, data):
        """
        SetMarketPrice(self: ISecurityPrice, data: BaseData)
            Update any security properties based on the 
             latest market data and time
        
        
            data: New data packet from LEAN
        """
        pass

    def Update(self, data, dataType, containsFillForwardData):
        """ Update(self: ISecurityPrice, data: IReadOnlyList[BaseData], dataType: Type, containsFillForwardData: Nullable[bool]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AskPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent ask price if available

Get: AskPrice(self: ISecurityPrice) -> Decimal

"""

    AskSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent ask size if available

Get: AskSize(self: ISecurityPrice) -> Decimal

"""

    BidPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent bid price if available

Get: BidPrice(self: ISecurityPrice) -> Decimal

"""

    BidSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent bid size if available

Get: BidSize(self: ISecurityPrice) -> Decimal

"""

    Close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this uses trade bar data, return the most recent close.

Get: Close(self: ISecurityPrice) -> Decimal

"""

    OpenInterest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Access to the open interest of the security today

Get: OpenInterest(self: ISecurityPrice) -> Int64

"""

    Price = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the current value of the security.

Get: Price(self: ISecurityPrice) -> Decimal

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """QuantConnect.Interfaces.ISecurityPrice.Symbol for the asset.

Get: Symbol(self: ISecurityPrice) -> Symbol

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Access to the volume of the equity today

Get: Volume(self: ISecurityPrice) -> Decimal

"""



class IOptionPrice(ISecurityPrice):
    """
    Reduced interface for accessing QuantConnect.Securities.Option.Option
                specific price properties and methods
    """
    def EvaluatePriceModel(self, slice, contract):
        """
        EvaluatePriceModel(self: IOptionPrice, slice: Slice, contract: OptionContract) -> OptionPriceModelResult
        
            Evaluates the specified option contract to 
             compute a theoretical price, IV and greeks
        
        
            slice: The current data slice. This can be used to 
             access other information
                    available 
             to the algorithm
        
            contract: The option contract to evaluate
            Returns: An instance of 
             QuantConnect.Securities.Option.OptionPriceModelRes
             ult containing the theoretical
                    price 
             of the specified option contract
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a reduced interface of the underlying security object.

Get: Underlying(self: IOptionPrice) -> ISecurityPrice

"""



class IOrderProperties:
    """ Contains additional properties and settings for an order """
    def Clone(self):
        """
        Clone(self: IOrderProperties) -> IOrderProperties
        
            Returns a new instance clone of this object
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    TimeInForce = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the length of time over which an order will continue working before it is cancelled

Get: TimeInForce(self: IOrderProperties) -> TimeInForce

Set: TimeInForce(self: IOrderProperties) = value
"""



class IPriceProvider:
    """ Provides access to price data for a given asset """
    def GetLastPrice(self, symbol):
        """
        GetLastPrice(self: IPriceProvider, symbol: Symbol) -> Decimal
        
            Gets the latest price for a given asset
        
            symbol: The symbol
            Returns: The latest price
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IRegressionAlgorithmDefinition:
    """
    Defines a C# algorithm as a regression algorithm to be run as part of the test suite.
                This interface also allows the algorithm to declare that it has versions in other languages
                that should yield identical results.
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CanRunLocally = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This is used by the regression test system to indicate if the open source Lean repository has the required data to run this algorithm.

Get: CanRunLocally(self: IRegressionAlgorithmDefinition) -> bool

"""

    ExpectedStatistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This is used by the regression test system to indicate what the expected statistics are from running the algorithm

Get: ExpectedStatistics(self: IRegressionAlgorithmDefinition) -> Dictionary[str, str]

"""

    Languages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This is used by the regression test system to indicate which languages this algorithm is written in.

Get: Languages(self: IRegressionAlgorithmDefinition) -> Array[Language]

"""



class ISecurityService:
    """ This interface exposes methods for creating a new QuantConnect.Securities.Security """
    def CreateSecurity(self, symbol, *__args):
        """
        CreateSecurity(self: ISecurityService, symbol: Symbol, subscriptionDataConfigList: List[SubscriptionDataConfig], leverage: Decimal, addToSymbolCache: bool) -> Security
        CreateSecurity(self: ISecurityService, symbol: Symbol, subscriptionDataConfig: SubscriptionDataConfig, leverage: Decimal, addToSymbolCache: bool) -> Security
        
            Creates a new security
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IStreamReader(IDisposable):
    """ Defines a transport mechanism for data from its source into various reader methods """
    def ReadLine(self):
        """
        ReadLine(self: IStreamReader) -> str
        
            Gets the next line/batch of content from the 
             stream
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    EndOfStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether or not there's more data to be read in the stream

Get: EndOfStream(self: IStreamReader) -> bool

"""

    ShouldBeRateLimited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether or not this stream reader should be rate limited

Get: ShouldBeRateLimited(self: IStreamReader) -> bool

"""

    StreamReader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Direct access to the StreamReader instance

Get: StreamReader(self: IStreamReader) -> StreamReader

"""

    TransportMedium = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the transport medium of this stream reader

Get: TransportMedium(self: IStreamReader) -> SubscriptionTransportMedium

"""



class ITimeInForceHandler:
    """ Handles the time in force for an order """
    def IsFillValid(self, security, order, fill):
        """
        IsFillValid(self: ITimeInForceHandler, security: Security, order: Order, fill: OrderEvent) -> bool
        
            Checks if an order fill is valid
        
            security: The security matching the order
            order: The order to be checked
            fill: The order fill to be checked
            Returns: Returns true if the order fill can be emitted, 
             false otherwise
        """
        pass

    def IsOrderExpired(self, security, order):
        """
        IsOrderExpired(self: ITimeInForceHandler, security: Security, order: Order) -> bool
        
            Checks if an order is expired
        
            security: The security matching the order
            order: The order to be checked
            Returns: Returns true if the order has expired, false 
             otherwise
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITimeKeeper:
    """ Interface implemented by QuantConnect.TimeKeeper """
    def AddTimeZone(self, timeZone):
        """
        AddTimeZone(self: ITimeKeeper, timeZone: DateTimeZone)
            Adds the specified time zone to this time keeper
        """
        pass

    def GetLocalTimeKeeper(self, timeZone):
        """
        GetLocalTimeKeeper(self: ITimeKeeper, timeZone: DateTimeZone) -> LocalTimeKeeper
        
            Gets the QuantConnect.LocalTimeKeeper instance 
             for the specified time zone
        
        
            timeZone: The time zone whose QuantConnect.LocalTimeKeeper 
             we seek
        
            Returns: The QuantConnect.LocalTimeKeeper instance for the 
             specified time zone
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    UtcTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current time in UTC

Get: UtcTime(self: ITimeKeeper) -> DateTime

"""



class ITradeBuilder:
    """ Generates trades from executions and market price updates """
    def HasOpenPosition(self, symbol):
        """
        HasOpenPosition(self: ITradeBuilder, symbol: Symbol) -> bool
        
            Returns true if there is an open position for the 
             symbol
        
        
            symbol: The symbol
            Returns: true if there is an open position for the symbol
        """
        pass

    def ProcessFill(self, fill, securityConversionRate, feeInAccountCurrency, multiplier):
        """
        ProcessFill(self: ITradeBuilder, fill: OrderEvent, securityConversionRate: Decimal, feeInAccountCurrency: Decimal, multiplier: Decimal)
            Processes a new fill, eventually creating new 
             trades
        
        
            fill: The new fill order event
            securityConversionRate: The current security market conversion rate into 
             the account currency
        
            feeInAccountCurrency: The current order fee in the account currency
            multiplier: The contract multiplier
        """
        pass

    def SetLiveMode(self, live):
        """
        SetLiveMode(self: ITradeBuilder, live: bool)
            Sets the live mode flag
        
            live: The live mode flag
        """
        pass

    def SetMarketPrice(self, symbol, price):
        """
        SetMarketPrice(self: ITradeBuilder, symbol: Symbol, price: Decimal)
            Sets the current market price for the symbol
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClosedTrades = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of closed trades

Get: ClosedTrades(self: ITradeBuilder) -> List[Trade]

"""



class ObjectStoreErrorRaisedEventArgs(EventArgs):
    """
    Event arguments for the QuantConnect.Interfaces.IObjectStore.ErrorRaised event
    
    ObjectStoreErrorRaisedEventArgs(error: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, error):
        """ __new__(cls: type, error: Exception) """
        pass

    Error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Exception that was raised

Get: Error(self: ObjectStoreErrorRaisedEventArgs) -> Exception

"""



