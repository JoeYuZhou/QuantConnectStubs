# encoding: utf-8
# module QuantConnect.Python calls itself Python
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BrokerageMessageHandlerPythonWrapper(object, IBrokerageMessageHandler):
    """
    Provides a wrapper for QuantConnect.Brokerages.IBrokerageMessageHandler implementations written in python
    
    BrokerageMessageHandlerPythonWrapper(model: PyObject)
    """
    def Handle(self, message):
        """
        Handle(self: BrokerageMessageHandlerPythonWrapper, message: BrokerageMessageEvent)
            Handles the message
        
            message: The message to be handled
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, model):
        """ __new__(cls: type, model: PyObject) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class BrokerageModelPythonWrapper(object, IBrokerageModel):
    """
    Provides an implementation of QuantConnect.Brokerages.IBrokerageModel that wraps a Python.Runtime.PyObject object
    
    BrokerageModelPythonWrapper(model: PyObject)
    """
    def ApplySplit(self, tickets, split):
        """ ApplySplit(self: BrokerageModelPythonWrapper, tickets: List[OrderTicket], split: Split) """
        pass

    def CanExecuteOrder(self, security, order):
        """
        CanExecuteOrder(self: BrokerageModelPythonWrapper, security: Security, order: Order) -> bool
        
            Returns true if the brokerage would be able to 
             execute this order at this time assuming
                
                 market prices are sufficient for the fill to 
             take place. This is used to emulate the
                 
                brokerage fills in backtesting and paper 
             trading. For example some brokerages may not 
             perform
                    executions during extended 
             market hours. This is not intended to be checking 
             whether or not
                    the exchange is open, 
             that is handled in the Security.Exchange 
             property.
        
        
            security: The security being ordered
            order: The order to test for execution
            Returns: True if the brokerage would be able to perform 
             the execution, false otherwise
        """
        pass

    def CanSubmitOrder(self, security, order, message):
        """
        CanSubmitOrder(self: BrokerageModelPythonWrapper, security: Security, order: Order) -> (bool, BrokerageMessageEvent)
        
            Returns true if the brokerage could accept this 
             order. This takes into account
                    order 
             type, security type, and order size limits.
        
        
            security: The security being ordered
            order: The order to be processed
            Returns: True if the brokerage could process the order, 
             false otherwise
        """
        pass

    def CanUpdateOrder(self, security, order, request, message):
        """
        CanUpdateOrder(self: BrokerageModelPythonWrapper, security: Security, order: Order, request: UpdateOrderRequest) -> (bool, BrokerageMessageEvent)
        
            Returns true if the brokerage would allow 
             updating the order as specified by the request
        
        
            security: The security of the order
            order: The order to be updated
            request: The requested updated to be made to the order
            Returns: True if the brokerage would allow updating the 
             order, false otherwise
        """
        pass

    def GetBuyingPowerModel(self, security, accountType=None):
        """
        GetBuyingPowerModel(self: BrokerageModelPythonWrapper, security: Security) -> IBuyingPowerModel
        
            Gets a new buying power model for the security, 
             returning the default model with the security's 
             configured leverage.
                    For cash 
             accounts, leverage = 1 is used.
        
        
            security: The security to get a buying power model for
            Returns: The buying power model for this brokerage/security
        GetBuyingPowerModel(self: BrokerageModelPythonWrapper, security: Security, accountType: AccountType) -> IBuyingPowerModel
        
            Gets a new buying power model for the security
        
            security: The security to get a buying power model for
            accountType: The account type
            Returns: The buying power model for this brokerage/security
        """
        pass

    def GetFeeModel(self, security):
        """
        GetFeeModel(self: BrokerageModelPythonWrapper, security: Security) -> IFeeModel
        
            Gets a new fee model that represents this 
             brokerage's fee structure
        
        
            security: The security to get a fee model for
            Returns: The new fee model for this brokerage
        """
        pass

    def GetFillModel(self, security):
        """
        GetFillModel(self: BrokerageModelPythonWrapper, security: Security) -> IFillModel
        
            Gets a new fill model that represents this 
             brokerage's fill behavior
        
        
            security: The security to get fill model for
            Returns: The new fill model for this brokerage
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: BrokerageModelPythonWrapper, security: Security) -> Decimal
        
            Gets the brokerage's leverage for the specified 
             security
        
        
            security: The security's whose leverage we seek
            Returns: The leverage for the specified security
        """
        pass

    def GetSettlementModel(self, security, accountType=None):
        """
        GetSettlementModel(self: BrokerageModelPythonWrapper, security: Security) -> ISettlementModel
        
            Gets a new settlement model for the security
        
            security: The security to get a settlement model for
            Returns: The settlement model for this brokerage
        GetSettlementModel(self: BrokerageModelPythonWrapper, security: Security, accountType: AccountType) -> ISettlementModel
        
            Gets a new settlement model for the security
        
            security: The security to get a settlement model for
            accountType: The account type
            Returns: The settlement model for this brokerage
        """
        pass

    def GetSlippageModel(self, security):
        """
        GetSlippageModel(self: BrokerageModelPythonWrapper, security: Security) -> ISlippageModel
        
            Gets a new slippage model that represents this 
             brokerage's fill slippage behavior
        
        
            security: The security to get a slippage model for
            Returns: The new slippage model for this brokerage
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, model):
        """ __new__(cls: type, model: PyObject) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AccountType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the account type used by this model

Get: AccountType(self: BrokerageModelPythonWrapper) -> AccountType

"""

    DefaultMarkets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a map of the default markets to be used for each security type

Get: DefaultMarkets(self: BrokerageModelPythonWrapper) -> IReadOnlyDictionary[SecurityType, str]

"""

    RequiredFreeBuyingPowerPercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brokerages model percentage factor used to determine the required unused buying power for the account.
            From 1 to 0. Example: 0 means no unused buying power is required. 0.5 means 50% of the buying power should be left unused.

Get: RequiredFreeBuyingPowerPercent(self: BrokerageModelPythonWrapper) -> Decimal

"""



class BuyingPowerModelPythonWrapper(object, IBuyingPowerModel):
    """
    Wraps a Python.Runtime.PyObject object that represents a security's model of buying power
    
    BuyingPowerModelPythonWrapper(model: PyObject)
    """
    def GetBuyingPower(self, parameters):
        """
        GetBuyingPower(self: BuyingPowerModelPythonWrapper, parameters: BuyingPowerParameters) -> BuyingPower
        
            Gets the buying power available for a trade
        
            parameters: A parameters object containing the algorithm's 
             potrfolio, security, and order direction
        
            Returns: The buying power available for the trade
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: BuyingPowerModelPythonWrapper, security: Security) -> Decimal
        
            Gets the current leverage of the security
        
            security: The security to get leverage for
            Returns: The current leverage in the security
        """
        pass

    def GetMaximumOrderQuantityForDeltaBuyingPower(self, parameters):
        """
        GetMaximumOrderQuantityForDeltaBuyingPower(self: BuyingPowerModelPythonWrapper, parameters: GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> GetMaximumOrderQuantityResult
        
            Get the maximum market order quantity to obtain a 
             delta in the buying power used by a security.
           
                      The deltas sign defines the position 
             side to apply it to, positive long, negative 
             short.
        
        
            parameters: An object containing the portfolio, the security 
             and the delta buying power
        
            Returns: Returns the maximum allowed market order quantity 
             and if zero, also the reason
        """
        pass

    def GetMaximumOrderQuantityForTargetBuyingPower(self, parameters):
        """
        GetMaximumOrderQuantityForTargetBuyingPower(self: BuyingPowerModelPythonWrapper, parameters: GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> GetMaximumOrderQuantityResult
        
            Get the maximum market order quantity to obtain a 
             position with a given buying power percentage.
          
                       Will not take into account free buying 
             power.
        
        
            parameters: An object containing the portfolio, the security 
             and the target signed buying power percentage
        
            Returns: Returns the maximum allowed market order quantity 
             and if zero, also the reason
        """
        pass

    def GetReservedBuyingPowerForPosition(self, parameters):
        """
        GetReservedBuyingPowerForPosition(self: BuyingPowerModelPythonWrapper, parameters: ReservedBuyingPowerForPositionParameters) -> ReservedBuyingPowerForPosition
        
            Gets the amount of buying power reserved to 
             maintain the specified position
        
        
            parameters: A parameters object containing the security
            Returns: The reserved buying power in account currency
        """
        pass

    def HasSufficientBuyingPowerForOrder(self, parameters):
        """
        HasSufficientBuyingPowerForOrder(self: BuyingPowerModelPythonWrapper, parameters: HasSufficientBuyingPowerForOrderParameters) -> HasSufficientBuyingPowerForOrderResult
        
            Check if there is sufficient buying power to 
             execute this order.
        
        
            parameters: An object containing the portfolio, the security 
             and the order
        
            Returns: Returns buying power information for an order
        """
        pass

    def SetLeverage(self, security, leverage):
        """
        SetLeverage(self: BuyingPowerModelPythonWrapper, security: Security, leverage: Decimal)
            Sets the leverage for the applicable securities, 
             i.e, equities
        
        
            security: The security to set leverage for
            leverage: The new leverage
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, model):
        """ __new__(cls: type, model: PyObject) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class FeeModelPythonWrapper(FeeModel, IFeeModel):
    """
    Provides an order fee model that wraps a Python.Runtime.PyObject object that represents a model that simulates order fees
    
    FeeModelPythonWrapper(model: PyObject)
    """
    def GetOrderFee(self, parameters):
        """
        GetOrderFee(self: FeeModelPythonWrapper, parameters: OrderFeeParameters) -> OrderFee
        
            Get the fee for this order
        
            parameters: A QuantConnect.Orders.Fees.OrderFeeParameters 
             object
                    containing the security and 
             order
        
            Returns: The cost of the order in units of the account 
             currency
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, model):
        """ __new__(cls: type, model: PyObject) """
        pass


class FillModelPythonWrapper(FillModel, IFillModel):
    """
    Wraps a Python.Runtime.PyObject object that represents a model that simulates order fill events
    
    FillModelPythonWrapper(model: PyObject)
    """
    def Fill(self, parameters):
        """
        Fill(self: FillModelPythonWrapper, parameters: FillModelParameters) -> Fill
        
            Return an order event with the fill details
        
            parameters: A parameters object containing the security and 
             order
        
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def GetPrices(self, *args): #cannot find CLR method
        """
        GetPrices(self: FillModelPythonWrapper, asset: Security, direction: OrderDirection) -> Prices
        
            Get the minimum and maximum price for this 
             security in the last bar:
        
        
            asset: Security asset we're checking
            direction: The order direction, decides whether to pick bid 
             or ask
        """
        pass

    def LimitFill(self, asset, order):
        """
        LimitFill(self: FillModelPythonWrapper, asset: Security, order: LimitOrder) -> OrderEvent
        
            Limit Fill Model. Return an order event with the 
             fill details.
        
        
            asset: Stock Object to use to help model limit fill
            order: Order to fill. Alter the values directly if 
             filled.
        
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def MarketFill(self, asset, order):
        """
        MarketFill(self: FillModelPythonWrapper, asset: Security, order: MarketOrder) -> OrderEvent
        
            Model the slippage on a market order: fixed 
             percentage of order price
        
        
            asset: Asset we're trading this order
            order: Order to update
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def MarketOnCloseFill(self, asset, order):
        """
        MarketOnCloseFill(self: FillModelPythonWrapper, asset: Security, order: MarketOnCloseOrder) -> OrderEvent
        
            Market on Close Fill Model. Return an order event 
             with the fill details
        
        
            asset: Asset we're trading with this order
            order: Order to be filled
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def MarketOnOpenFill(self, asset, order):
        """
        MarketOnOpenFill(self: FillModelPythonWrapper, asset: Security, order: MarketOnOpenOrder) -> OrderEvent
        
            Market on Open Fill Model. Return an order event 
             with the fill details
        
        
            asset: Asset we're trading with this order
            order: Order to be filled
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def StopLimitFill(self, asset, order):
        """
        StopLimitFill(self: FillModelPythonWrapper, asset: Security, order: StopLimitOrder) -> OrderEvent
        
            Stop Limit Fill Model. Return an order event with 
             the fill details.
        
        
            asset: Asset we're trading this order
            order: Stop Limit Order to Check, return filled if true
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def StopMarketFill(self, asset, order):
        """
        StopMarketFill(self: FillModelPythonWrapper, asset: Security, order: StopMarketOrder) -> OrderEvent
        
            Stop Market Fill Model. Return an order event 
             with the fill details.
        
        
            asset: Asset we're trading this order
            order: Stop Order to Check, return filled if true
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, model):
        """ __new__(cls: type, model: PyObject) """
        pass

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The parameters instance to be used by the different XxxxFill() implementations

"""


    PythonWrapper = None


class MarginCallModelPythonWrapper(object, IMarginCallModel):
    """
    Provides a margin call model that wraps a Python.Runtime.PyObject object that represents the model responsible for picking which orders should be executed during a margin call
    
    MarginCallModelPythonWrapper(model: PyObject)
    """
    def ExecuteMarginCall(self, generatedMarginCallOrders):
        """ ExecuteMarginCall(self: MarginCallModelPythonWrapper, generatedMarginCallOrders: IEnumerable[SubmitOrderRequest]) -> List[OrderTicket] """
        pass

    def GetMarginCallOrders(self, issueMarginCallWarning):
        """
        GetMarginCallOrders(self: MarginCallModelPythonWrapper) -> (List[SubmitOrderRequest], bool)
        
            Scan the portfolio and the updated data for a 
             potential margin call situation which may get the 
             holdings below zero!
                    If there is a 
             margin call, liquidate the portfolio immediately 
             before the portfolio gets sub zero.
        
            Returns: True for a margin call on the holdings.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, model):
        """ __new__(cls: type, model: PyObject) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class PandasConverter(object):
    """
    Collection of methods that converts lists of objects in pandas.DataFrame
    
    PandasConverter()
    """
    def GetDataFrame(self, data):
        """
        GetDataFrame(self: PandasConverter, data: IEnumerable[Slice]) -> PyObject
        GetDataFrame[T](self: PandasConverter, data: IEnumerable[T]) -> PyObject
        """
        pass

    def GetIndicatorDataFrame(self, data):
        """ GetIndicatorDataFrame(self: PandasConverter, data: IDictionary[str, List[IndicatorDataPoint]]) -> PyObject """
        pass

    def ToString(self):
        """
        ToString(self: PandasConverter) -> str
        
            Returns a string that represent the current object
        """
        pass


class PandasData(object):
    """
    Organizes a list of data to create pandas.DataFrames
    
    PandasData(data: object)
    """
    def Add(self, *__args):
        """
        Add(self: PandasData, baseData: object)
            Adds security data object to the end of the lists
        
            baseData: QuantConnect.Data.IBaseData object that contains 
             security data
        
        Add(self: PandasData, ticks: IEnumerable[Tick], tradeBar: TradeBar, quoteBar: QuoteBar)
        """
        pass

    def ToPandasDataFrame(self, levels):
        """
        ToPandasDataFrame(self: PandasData, levels: int) -> PyObject
        
            Get the pandas.DataFrame of the current 
             QuantConnect.Python.PandasData state
        
        
            levels: Number of levels of the multi index
            Returns: pandas.DataFrame object
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, data):
        """ __new__(cls: type, data: object) """
        pass

    IsCustomData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets true if this is a custom data request, false for normal QC data

Get: IsCustomData(self: PandasData) -> bool

"""

    Levels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Implied levels of a multi index pandas.Series (depends on the security type)

Get: Levels(self: PandasData) -> int

"""



class PythonActivator(object):
    """
    Provides methods for creating new instances of python custom data objects
    
    PythonActivator(type: Type, value: PyObject)
    """
    @staticmethod # known case of __new__
    def __new__(self, type, value):
        """ __new__(cls: type, type: Type, value: PyObject) """
        pass

    Factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Method to return an instance of object

Get: Factory(self: PythonActivator) -> Func[Array[object], object]

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """System.Type of the object we wish to create

Get: Type(self: PythonActivator) -> Type

"""



class PythonData(DynamicData, IBaseData, IDynamicMetaObjectProvider):
    """
    Dynamic data class for Python algorithms.
                Stores properties of python instances in DynamicData dictionary
    
    PythonData()
    PythonData(pythonData: PyObject)
    """
    def DefaultResolution(self):
        """
        DefaultResolution(self: PythonData) -> Resolution
        
            Gets the default resolution for this data and 
             security type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: PythonData, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Source Locator for algorithm written in Python.
        
            config: Subscription configuration object
            date: Date of the data file we're looking for
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: STRING API Url.
        """
        pass

    def IsSparseData(self):
        """
        IsSparseData(self: PythonData) -> bool
        
            Indicates that the data set is expected to be 
             sparse
        
            Returns: True if the data set represented by this type is 
             expected to be sparse
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: PythonData, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Generic Reader Implementation for Python Custom 
             Data.
        
        
            config: Subscription configuration
            line: CSV line of data from the source
            date: Date of the requested line
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: PythonData) -> bool
        
            Indicates if there is support for mapping
            Returns: True indicates mapping should be used
        """
        pass

    def SupportedResolutions(self):
        """
        SupportedResolutions(self: PythonData) -> List[Resolution]
        
            Gets the supported resolution for this data and 
             security type
        """
        pass

    def __dir__(self, *args): #cannot find CLR method
        """ __dir__(self: IDynamicMetaObjectProvider) -> list """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pythonData=None):
        """
        __new__(cls: type)
        __new__(cls: type, pythonData: PyObject)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class PythonInitializer(object):
    """ Helper class for Python initialization """
    @staticmethod
    def AddPythonPaths(paths):
        """ AddPythonPaths(paths: IEnumerable[str]) """
        pass

    @staticmethod
    def Initialize():
        """
        Initialize()
            Initialize the Python.NET library
        """
        pass

    @staticmethod
    def SetPythonPathEnvironmentVariable(extraDirectories):
        """ SetPythonPathEnvironmentVariable(extraDirectories: IEnumerable[str]) """
        pass

    __all__ = [
        'AddPythonPaths',
        'Initialize',
        'SetPythonPathEnvironmentVariable',
    ]


class PythonQuandl(Quandl, IBaseData, IDynamicMetaObjectProvider):
    """
    Dynamic data class for Python algorithms.
    
    PythonQuandl()
    PythonQuandl(valueColumnName: str)
    """
    def __dir__(self, *args): #cannot find CLR method
        """ __dir__(self: IDynamicMetaObjectProvider) -> list """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, valueColumnName=None):
        """
        __new__(cls: type)
        __new__(cls: type, valueColumnName: str)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class PythonSlice(Slice, IExtendedDictionary[Symbol, object], IEnumerable[KeyValuePair[Symbol, BaseData]], IEnumerable):
    """
    Provides a data structure for all of an algorithm's data at a single time step
    
    PythonSlice(slice: Slice)
    """
    def ContainsKey(self, symbol):
        """
        ContainsKey(self: PythonSlice, symbol: Symbol) -> bool
        
            Determines whether this instance contains data 
             for the specified symbol
        
        
            symbol: The symbol we seek data for
            Returns: True if this instance contains data for the 
             symbol, false otherwise
        """
        pass

    def Get(self, *__args):
        """
        Get(self: PythonSlice, type: PyObject, symbol: Symbol) -> object
        
            Gets the data of the specified symbol and type.
        
            type: The type of data we seek
            symbol: The specific symbol was seek
            Returns: The data for the requested symbol
        Get(self: PythonSlice, type: PyObject) -> PyObject
        
            Gets the data of the specified symbol and type.
        
            type: The type of data we seek
            Returns: The data for the requested symbol
        """
        pass

    def TryGetValue(self, symbol, data):
        """
        TryGetValue(self: PythonSlice, symbol: Symbol) -> (bool, object)
        
            Gets the data associated with the specified symbol
        
            symbol: The symbol we want data for
            Returns: True if data was found, false otherwise
        """
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
    def __new__(self, slice):
        """ __new__(cls: type, slice: Slice) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of symbols held in this slice

Get: Count(self: PythonSlice) -> int

"""

    GetKeys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.Generic.ICollection containing the Symbol objects of the System.Collections.Generic.IDictionary.

"""

    GetValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.Generic.ICollection containing the values in the System.Collections.Generic.IDictionary.

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all the symbols in this slice

Get: Keys(self: PythonSlice) -> IReadOnlyList[Symbol]

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a list of all the data in this slice

Get: Values(self: PythonSlice) -> IReadOnlyList[BaseData]

"""



class PythonWrapper(object):
    """ Provides extension methods for managing python wrapper classes """
    @staticmethod
    def ValidateImplementationOf(model):
        """ ValidateImplementationOf[TInterface](model: PyObject) """
        pass

    __all__ = [
        'ValidateImplementationOf',
    ]


class SecurityInitializerPythonWrapper(object, ISecurityInitializer):
    """
    Wraps a Python.Runtime.PyObject object that represents a type capable of initializing a new security
    
    SecurityInitializerPythonWrapper(model: PyObject)
    """
    def Initialize(self, security):
        """
        Initialize(self: SecurityInitializerPythonWrapper, security: Security)
            Initializes the specified security
        
            security: The security to be initialized
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, model):
        """ __new__(cls: type, model: PyObject) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class SlippageModelPythonWrapper(object, ISlippageModel):
    """
    Wraps a Python.Runtime.PyObject object that represents a model that simulates market order slippage
    
    SlippageModelPythonWrapper(model: PyObject)
    """
    def GetSlippageApproximation(self, asset, order):
        """
        GetSlippageApproximation(self: SlippageModelPythonWrapper, asset: Security, order: Order) -> Decimal
        
            Slippage Model. Return a decimal cash slippage 
             approximation on the order.
        
        
            asset: The security matching the order
            order: The order to compute slippage for
            Returns: The slippage of the order in units of the account 
             currency
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, model):
        """ __new__(cls: type, model: PyObject) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class VolatilityModelPythonWrapper(BaseVolatilityModel, IVolatilityModel):
    """
    Provides a volatility model that wraps a Python.Runtime.PyObject object that represents a model that computes the volatility of a security
    
    VolatilityModelPythonWrapper(model: PyObject)
    """
    def GetHistoryRequirements(self, security, utcTime):
        """
        GetHistoryRequirements(self: VolatilityModelPythonWrapper, security: Security, utcTime: DateTime) -> IEnumerable[HistoryRequest]
        
            Returns history requirements for the volatility 
             model expressed in the form of history request
        
        
            security: The security of the request
            utcTime: The date/time of the request
            Returns: History request object list, or empty if no 
             requirements
        """
        pass

    def SetSubscriptionDataConfigProvider(self, subscriptionDataConfigProvider):
        """
        SetSubscriptionDataConfigProvider(self: VolatilityModelPythonWrapper, subscriptionDataConfigProvider: ISubscriptionDataConfigProvider)
            Sets the 
             QuantConnect.Interfaces.ISubscriptionDataConfigPro
             vider instance to use.
        
        
            subscriptionDataConfigProvider: Provides access to registered 
             QuantConnect.Data.SubscriptionDataConfig
        """
        pass

    def Update(self, security, data):
        """
        Update(self: VolatilityModelPythonWrapper, security: Security, data: BaseData)
            Updates this model using the new price 
             information in
                    the specified 
             security instance
        
        
            security: The security to calculate volatility for
            data: The new data used to update the model
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, model):
        """ __new__(cls: type, model: PyObject) """
        pass

    Volatility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the volatility of the security as a percentage

Get: Volatility(self: VolatilityModelPythonWrapper) -> Decimal

"""


    SubscriptionDataConfigProvider = None


