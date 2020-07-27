# encoding: utf-8
# module QuantConnect.Brokerages calls itself Brokerages
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DefaultBrokerageModel(object, IBrokerageModel):
    """
    Provides a default implementation of QuantConnect.Brokerages.IBrokerageModel that allows all orders and uses
                the default transaction models
    
    DefaultBrokerageModel(accountType: AccountType)
    """
    def ApplySplit(self, tickets, split):
        """ ApplySplit(self: DefaultBrokerageModel, tickets: List[OrderTicket], split: Split) """
        pass

    def CanExecuteOrder(self, security, order):
        """
        CanExecuteOrder(self: DefaultBrokerageModel, security: Security, order: Order) -> bool
        
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
        
        
            security: The security being traded
            order: The order to test for execution
            Returns: True if the brokerage would be able to perform 
             the execution, false otherwise
        """
        pass

    def CanSubmitOrder(self, security, order, message):
        """
        CanSubmitOrder(self: DefaultBrokerageModel, security: Security, order: Order) -> (bool, BrokerageMessageEvent)
        
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
        CanUpdateOrder(self: DefaultBrokerageModel, security: Security, order: Order, request: UpdateOrderRequest) -> (bool, BrokerageMessageEvent)
        
            Returns true if the brokerage would allow 
             updating the order as specified by the request
        
        
            security: The security of the order
            order: The order to be updated
            request: The requested update to be made to the order
            Returns: True if the brokerage would allow updating the 
             order, false otherwise
        """
        pass

    def GetBuyingPowerModel(self, security, accountType=None):
        """
        GetBuyingPowerModel(self: DefaultBrokerageModel, security: Security) -> IBuyingPowerModel
        
            Gets a new buying power model for the security, 
             returning the default model with the security's 
             configured leverage.
                    For cash 
             accounts, leverage = 1 is used.
        
        
            security: The security to get a buying power model for
            Returns: The buying power model for this brokerage/security
        GetBuyingPowerModel(self: DefaultBrokerageModel, security: Security, accountType: AccountType) -> IBuyingPowerModel
        
            Gets a new buying power model for the security
        
            security: The security to get a buying power model for
            accountType: The account type
            Returns: The buying power model for this brokerage/security
        """
        pass

    def GetFeeModel(self, security):
        """
        GetFeeModel(self: DefaultBrokerageModel, security: Security) -> IFeeModel
        
            Gets a new fee model that represents this 
             brokerage's fee structure
        
        
            security: The security to get a fee model for
            Returns: The new fee model for this brokerage
        """
        pass

    def GetFillModel(self, security):
        """
        GetFillModel(self: DefaultBrokerageModel, security: Security) -> IFillModel
        
            Gets a new fill model that represents this 
             brokerage's fill behavior
        
        
            security: The security to get fill model for
            Returns: The new fill model for this brokerage
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: DefaultBrokerageModel, security: Security) -> Decimal
        
            Gets the brokerage's leverage for the specified 
             security
        
        
            security: The security's whose leverage we seek
            Returns: The leverage for the specified security
        """
        pass

    def GetSettlementModel(self, security, accountType=None):
        """
        GetSettlementModel(self: DefaultBrokerageModel, security: Security) -> ISettlementModel
        
            Gets a new settlement model for the security
        
            security: The security to get a settlement model for
            Returns: The settlement model for this brokerage
        GetSettlementModel(self: DefaultBrokerageModel, security: Security, accountType: AccountType) -> ISettlementModel
        
            Gets a new settlement model for the security
        
            security: The security to get a settlement model for
            accountType: The account type
            Returns: The settlement model for this brokerage
        """
        pass

    def GetSlippageModel(self, security):
        """
        GetSlippageModel(self: DefaultBrokerageModel, security: Security) -> ISlippageModel
        
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
    def __new__(self, accountType):
        """ __new__(cls: type, accountType: AccountType) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AccountType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the account type used by this model

Get: AccountType(self: DefaultBrokerageModel) -> AccountType

"""

    DefaultMarkets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a map of the default markets to be used for each security type

Get: DefaultMarkets(self: DefaultBrokerageModel) -> IReadOnlyDictionary[SecurityType, str]

"""

    RequiredFreeBuyingPowerPercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brokerages model percentage factor used to determine the required unused buying power for the account.
            From 1 to 0. Example: 0 means no unused buying power is required. 0.5 means 50% of the buying power should be left unused.

Get: RequiredFreeBuyingPowerPercent(self: DefaultBrokerageModel) -> Decimal

"""


    DefaultMarketMap = None


class AlpacaBrokerageModel(DefaultBrokerageModel, IBrokerageModel):
    """
    Alpaca Brokerage Model Implementation for Back Testing.
    
    AlpacaBrokerageModel(orderProvider: IOrderProvider, accountType: AccountType)
    """
    def CanSubmitOrder(self, security, order, message):
        """
        CanSubmitOrder(self: AlpacaBrokerageModel, security: Security, order: Order) -> (bool, BrokerageMessageEvent)
        
            Returns true if the brokerage could accept this 
             order. This takes into account
                    order 
             type, security type, and order size limits.
        
        
            order: The order to be processed
            Returns: True if the brokerage could process the order, 
             false otherwise
        """
        pass

    def GetFeeModel(self, security):
        """
        GetFeeModel(self: AlpacaBrokerageModel, security: Security) -> IFeeModel
        
            Gets a new fee model that represents this 
             brokerage's fee structure
        
        
            security: The security to get a fee model for
            Returns: The new fee model for this brokerage
        """
        pass

    def GetFillModel(self, security):
        """
        GetFillModel(self: AlpacaBrokerageModel, security: Security) -> IFillModel
        
            Gets a new fill model that represents this 
             brokerage's fill behavior
        
        
            security: The security to get fill model for
            Returns: The new fill model for this brokerage
        """
        pass

    def GetSlippageModel(self, security):
        """
        GetSlippageModel(self: AlpacaBrokerageModel, security: Security) -> ISlippageModel
        
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
    def __new__(self, orderProvider, accountType):
        """ __new__(cls: type, orderProvider: IOrderProvider, accountType: AccountType) """
        pass

    DefaultMarkets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a map of the default markets to be used for each security type

Get: DefaultMarkets(self: AlpacaBrokerageModel) -> IReadOnlyDictionary[SecurityType, str]

"""


    DefaultMarketMap = None


class AlphaStreamsBrokerageModel(DefaultBrokerageModel, IBrokerageModel):
    """
    Provides properties specific to Alpha Streams
    
    AlphaStreamsBrokerageModel(accountType: AccountType)
    """
    def GetFeeModel(self, security):
        """
        GetFeeModel(self: AlphaStreamsBrokerageModel, security: Security) -> IFeeModel
        
            Gets a new fee model that represents this 
             brokerage's fee structure
        
        
            security: The security to get a fee model for
            Returns: The new fee model for this brokerage
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: AlphaStreamsBrokerageModel, security: Security) -> Decimal
        
            Gets the brokerage's leverage for the specified 
             security
        
        
            security: The security's whose leverage we seek
            Returns: The leverage for the specified security
        """
        pass

    def GetSettlementModel(self, security, accountType=None):
        """
        GetSettlementModel(self: AlphaStreamsBrokerageModel, security: Security) -> ISettlementModel
        
            Gets a new settlement model for the security
        
            security: The security to get a settlement model for
            Returns: The settlement model for this brokerage
        """
        pass

    def GetSlippageModel(self, security):
        """
        GetSlippageModel(self: AlphaStreamsBrokerageModel, security: Security) -> ISlippageModel
        
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
    def __new__(self, accountType):
        """ __new__(cls: type, accountType: AccountType) """
        pass


class BitfinexBrokerageModel(DefaultBrokerageModel, IBrokerageModel):
    """
    Provides Bitfinex specific properties
    
    BitfinexBrokerageModel(accountType: AccountType)
    """
    def GetBuyingPowerModel(self, security, accountType=None):
        """
        GetBuyingPowerModel(self: BitfinexBrokerageModel, security: Security) -> IBuyingPowerModel
        
            Gets a new buying power model for the security, 
             returning the default model with the security's 
             configured leverage.
                    For cash 
             accounts, leverage = 1 is used.
                    For 
             margin trading, max leverage = 3.3
        
        
            security: The security to get a buying power model for
            Returns: The buying power model for this brokerage/security
        """
        pass

    def GetFeeModel(self, security):
        """
        GetFeeModel(self: BitfinexBrokerageModel, security: Security) -> IFeeModel
        
            Provides Bitfinex fee model
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: BitfinexBrokerageModel, security: Security) -> Decimal
        
            Bitfinex global leverage rule
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountType):
        """ __new__(cls: type, accountType: AccountType) """
        pass

    DefaultMarkets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a map of the default markets to be used for each security type

Get: DefaultMarkets(self: BitfinexBrokerageModel) -> IReadOnlyDictionary[SecurityType, str]

"""



class BrokerageFactoryAttribute(Attribute, _Attribute):
    """
    Represents the brokerage factory type required to load a data queue handler
    
    BrokerageFactoryAttribute(type: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type):
        """ __new__(cls: type, type: Type) """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of the brokerage factory

Get: Type(self: BrokerageFactoryAttribute) -> Type

Set: Type(self: BrokerageFactoryAttribute) = value
"""



class BrokerageMessageEvent(object):
    """
    Represents a message received from a brokerage
    
    BrokerageMessageEvent(type: BrokerageMessageType, code: int, message: str)
    BrokerageMessageEvent(type: BrokerageMessageType, code: str, message: str)
    """
    @staticmethod
    def Disconnected(message):
        """
        Disconnected(message: str) -> BrokerageMessageEvent
        
            Creates a new 
             QuantConnect.Brokerages.BrokerageMessageEvent to 
             represent a disconnect message
        
        
            message: The message from the brokerage
            Returns: A brokerage disconnect message
        """
        pass

    @staticmethod
    def Reconnected(message):
        """
        Reconnected(message: str) -> BrokerageMessageEvent
        
            Creates a new 
             QuantConnect.Brokerages.BrokerageMessageEvent to 
             represent a reconnect message
        
        
            message: The message from the brokerage
            Returns: A brokerage reconnect message
        """
        pass

    def ToString(self):
        """
        ToString(self: BrokerageMessageEvent) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type, code, message):
        """
        __new__(cls: type, type: BrokerageMessageType, code: int, message: str)
        __new__(cls: type, type: BrokerageMessageType, code: str, message: str)
        """
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brokerage specific code for this message, zero if no code was specified

Get: Code(self: BrokerageMessageEvent) -> str

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the message text received from the brokerage

Get: Message(self: BrokerageMessageEvent) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of brokerage message

Get: Type(self: BrokerageMessageEvent) -> BrokerageMessageType

"""



class BrokerageMessageType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of message received from an IBrokerage implementation
    
    enum BrokerageMessageType, values: Disconnect (4), Error (2), Information (0), Reconnect (3), Warning (1)
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

    Disconnect = None
    Error = None
    Information = None
    Reconnect = None
    value__ = None
    Warning = None


class BrokerageModel(object):
    """ Provides factory method for creating an QuantConnect.Brokerages.IBrokerageModel from the QuantConnect.Brokerages.BrokerageName enum """
    @staticmethod
    def Create(orderProvider, brokerage, accountType):
        """
        Create(orderProvider: IOrderProvider, brokerage: BrokerageName, accountType: AccountType) -> IBrokerageModel
        
            Creates a new 
             QuantConnect.Brokerages.IBrokerageModel for the 
             specified QuantConnect.Brokerages.BrokerageName
        
        
            orderProvider: The order provider
            brokerage: The name of the brokerage
            accountType: The account type
            Returns: The model for the specified brokerage
        """
        pass

    __all__ = [
        'Create',
    ]


class BrokerageName(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifices what transaction model and submit/execution rules to use
    
    enum BrokerageName, values: Alpaca (13), AlphaStreams (14), Bitfinex (5), Default (0), FxcmBrokerage (4), GDAX (12), InteractiveBrokersBrokerage (1), OandaBrokerage (3), QuantConnectBrokerage (0), TradierBrokerage (2)
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

    Alpaca = None
    AlphaStreams = None
    Bitfinex = None
    Default = None
    FxcmBrokerage = None
    GDAX = None
    InteractiveBrokersBrokerage = None
    OandaBrokerage = None
    QuantConnectBrokerage = None
    TradierBrokerage = None
    value__ = None


class DefaultBrokerageMessageHandler(object, IBrokerageMessageHandler):
    """
    Provides a default implementation o QuantConnect.Brokerages.IBrokerageMessageHandler that will forward
                messages as follows:
                Information -> IResultHandler.Debug
                Warning     -> IResultHandler.Error && IApi.SendUserEmail
                Error       -> IResultHandler.Error && IAlgorithm.RunTimeError
    
    DefaultBrokerageMessageHandler(algorithm: IAlgorithm, job: AlgorithmNodePacket, api: IApi, initialDelay: Nullable[TimeSpan], openThreshold: Nullable[TimeSpan])
    """
    def Handle(self, message):
        """
        Handle(self: DefaultBrokerageMessageHandler, message: BrokerageMessageEvent)
            Handles the message
        
            message: The message to be handled
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, algorithm, job, api, initialDelay, openThreshold):
        """ __new__(cls: type, algorithm: IAlgorithm, job: AlgorithmNodePacket, api: IApi, initialDelay: Nullable[TimeSpan], openThreshold: Nullable[TimeSpan]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class DowngradeErrorCodeToWarningBrokerageMessageHandler(object, IBrokerageMessageHandler):
    """
    Provides an implementation of QuantConnect.Brokerages.IBrokerageMessageHandler that converts specified error codes into warnings
    
    DowngradeErrorCodeToWarningBrokerageMessageHandler(brokerageMessageHandler: IBrokerageMessageHandler, errorCodesToIgnore: Array[str])
    """
    def Handle(self, message):
        """
        Handle(self: DowngradeErrorCodeToWarningBrokerageMessageHandler, message: BrokerageMessageEvent)
            Handles the message
        
            message: The message to be handled
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, brokerageMessageHandler, errorCodesToIgnore):
        """ __new__(cls: type, brokerageMessageHandler: IBrokerageMessageHandler, errorCodesToIgnore: Array[str]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class FxcmBrokerageModel(DefaultBrokerageModel, IBrokerageModel):
    """
    Provides FXCM specific properties
    
    FxcmBrokerageModel(accountType: AccountType)
    """
    def CanSubmitOrder(self, security, order, message):
        """
        CanSubmitOrder(self: FxcmBrokerageModel, security: Security, order: Order) -> (bool, BrokerageMessageEvent)
        
            Returns true if the brokerage could accept this 
             order. This takes into account
                    order 
             type, security type, and order size limits.
        
        
            order: The order to be processed
            Returns: True if the brokerage could process the order, 
             false otherwise
        """
        pass

    def CanUpdateOrder(self, security, order, request, message):
        """
        CanUpdateOrder(self: FxcmBrokerageModel, security: Security, order: Order, request: UpdateOrderRequest) -> (bool, BrokerageMessageEvent)
        
            Returns true if the brokerage would allow 
             updating the order as specified by the request
        
        
            security: The security of the order
            order: The order to be updated
            request: The requested update to be made to the order
            Returns: True if the brokerage would allow updating the 
             order, false otherwise
        """
        pass

    def GetFeeModel(self, security):
        """
        GetFeeModel(self: FxcmBrokerageModel, security: Security) -> IFeeModel
        
            Gets a new fee model that represents this 
             brokerage's fee structure
        
        
            security: The security to get a fee model for
            Returns: The new fee model for this brokerage
        """
        pass

    def GetFillModel(self, security):
        """
        GetFillModel(self: FxcmBrokerageModel, security: Security) -> IFillModel
        
            Gets a new fill model that represents this 
             brokerage's fill behavior
        
        
            security: The security to get fill model for
            Returns: The new fill model for this brokerage
        """
        pass

    def GetSettlementModel(self, security, accountType=None):
        """
        GetSettlementModel(self: FxcmBrokerageModel, security: Security) -> ISettlementModel
        
            Gets a new settlement model for the security
        
            security: The security to get a settlement model for
            Returns: The settlement model for this brokerage
        """
        pass

    def GetSlippageModel(self, security):
        """
        GetSlippageModel(self: FxcmBrokerageModel, security: Security) -> ISlippageModel
        
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
    def __new__(self, accountType):
        """ __new__(cls: type, accountType: AccountType) """
        pass

    DefaultMarkets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a map of the default markets to be used for each security type

Get: DefaultMarkets(self: FxcmBrokerageModel) -> IReadOnlyDictionary[SecurityType, str]

"""


    DefaultMarketMap = None


class GDAXBrokerageModel(DefaultBrokerageModel, IBrokerageModel):
    """
    Provides GDAX specific properties
    
    GDAXBrokerageModel(accountType: AccountType)
    """
    def CanSubmitOrder(self, security, order, message):
        """
        CanSubmitOrder(self: GDAXBrokerageModel, security: Security, order: Order) -> (bool, BrokerageMessageEvent)
        
            Evaluates whether exchange will accept order. 
             Will reject order update
        """
        pass

    def CanUpdateOrder(self, security, order, request, message):
        """
        CanUpdateOrder(self: GDAXBrokerageModel, security: Security, order: Order, request: UpdateOrderRequest) -> (bool, BrokerageMessageEvent)
        
            Gdax does no support update of orders
        """
        pass

    def GetBuyingPowerModel(self, security, accountType=None):
        """
        GetBuyingPowerModel(self: GDAXBrokerageModel, security: Security) -> IBuyingPowerModel
        
            Gets a new buying power model for the security, 
             returning the default model with the security's 
             configured leverage.
                    For cash 
             accounts, leverage = 1 is used.
        
        
            security: The security to get a buying power model for
            Returns: The buying power model for this brokerage/security
        """
        pass

    def GetFeeModel(self, security):
        """
        GetFeeModel(self: GDAXBrokerageModel, security: Security) -> IFeeModel
        
            Provides GDAX fee model
        """
        pass

    def GetFillModel(self, security):
        """
        GetFillModel(self: GDAXBrokerageModel, security: Security) -> IFillModel
        
            GDAX fills order using the latest Trade or Quote 
             data
        
        
            security: The security to get fill model for
            Returns: The new fill model for this brokerage
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: GDAXBrokerageModel, security: Security) -> Decimal
        
            GDAX global leverage rule
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountType):
        """ __new__(cls: type, accountType: AccountType) """
        pass


class IBrokerageMessageHandler:
    """
    Provides an plugin point to allow algorithms to directly handle the messages
                that come from their brokerage
    """
    def Handle(self, message):
        """
        Handle(self: IBrokerageMessageHandler, message: BrokerageMessageEvent)
            Handles the message
        
            message: The message to be handled
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IBrokerageModel:
    """ Models brokerage transactions, fees, and order """
    def ApplySplit(self, tickets, split):
        """ ApplySplit(self: IBrokerageModel, tickets: List[OrderTicket], split: Split) """
        pass

    def CanExecuteOrder(self, security, order):
        """
        CanExecuteOrder(self: IBrokerageModel, security: Security, order: Order) -> bool
        
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
        CanSubmitOrder(self: IBrokerageModel, security: Security, order: Order) -> (bool, BrokerageMessageEvent)
        
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
        CanUpdateOrder(self: IBrokerageModel, security: Security, order: Order, request: UpdateOrderRequest) -> (bool, BrokerageMessageEvent)
        
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
        GetBuyingPowerModel(self: IBrokerageModel, security: Security) -> IBuyingPowerModel
        
            Gets a new buying power model for the security
        
            security: The security to get a buying power model for
            Returns: The buying power model for this brokerage/security
        GetBuyingPowerModel(self: IBrokerageModel, security: Security, accountType: AccountType) -> IBuyingPowerModel
        
            Gets a new buying power model for the security
        
            security: The security to get a buying power model for
            accountType: The account type
            Returns: The buying power model for this brokerage/security
        """
        pass

    def GetFeeModel(self, security):
        """
        GetFeeModel(self: IBrokerageModel, security: Security) -> IFeeModel
        
            Gets a new fee model that represents this 
             brokerage's fee structure
        
        
            security: The security to get a fee model for
            Returns: The new fee model for this brokerage
        """
        pass

    def GetFillModel(self, security):
        """
        GetFillModel(self: IBrokerageModel, security: Security) -> IFillModel
        
            Gets a new fill model that represents this 
             brokerage's fill behavior
        
        
            security: The security to get fill model for
            Returns: The new fill model for this brokerage
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: IBrokerageModel, security: Security) -> Decimal
        
            Gets the brokerage's leverage for the specified 
             security
        
        
            security: The security's whose leverage we seek
            Returns: The leverage for the specified security
        """
        pass

    def GetSettlementModel(self, security, accountType=None):
        """
        GetSettlementModel(self: IBrokerageModel, security: Security) -> ISettlementModel
        
            Gets a new settlement model for the security
        
            security: The security to get a settlement model for
            Returns: The settlement model for this brokerage
        GetSettlementModel(self: IBrokerageModel, security: Security, accountType: AccountType) -> ISettlementModel
        
            Gets a new settlement model for the security
        
            security: The security to get a settlement model for
            accountType: The account type
            Returns: The settlement model for this brokerage
        """
        pass

    def GetSlippageModel(self, security):
        """
        GetSlippageModel(self: IBrokerageModel, security: Security) -> ISlippageModel
        
            Gets a new slippage model that represents this 
             brokerage's fill slippage behavior
        
        
            security: The security to get a slippage model for
            Returns: The new slippage model for this brokerage
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AccountType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the account type used by this model

Get: AccountType(self: IBrokerageModel) -> AccountType

"""

    DefaultMarkets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a map of the default markets to be used for each security type

Get: DefaultMarkets(self: IBrokerageModel) -> IReadOnlyDictionary[SecurityType, str]

"""

    RequiredFreeBuyingPowerPercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the brokerages model percentage factor used to determine the required unused buying power for the account.
            From 1 to 0. Example: 0 means no unused buying power is required. 0.5 means 50% of the buying power should be left unused.

Get: RequiredFreeBuyingPowerPercent(self: IBrokerageModel) -> Decimal

"""



class InteractiveBrokersBrokerageModel(DefaultBrokerageModel, IBrokerageModel):
    """
    Provides properties specific to interactive brokers
    
    InteractiveBrokersBrokerageModel(accountType: AccountType)
    """
    def CanExecuteOrder(self, security, order):
        """
        CanExecuteOrder(self: InteractiveBrokersBrokerageModel, security: Security, order: Order) -> bool
        
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
        
        
            order: The order to test for execution
            Returns: True if the brokerage would be able to perform 
             the execution, false otherwise
        """
        pass

    def CanSubmitOrder(self, security, order, message):
        """
        CanSubmitOrder(self: InteractiveBrokersBrokerageModel, security: Security, order: Order) -> (bool, BrokerageMessageEvent)
        
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
        CanUpdateOrder(self: InteractiveBrokersBrokerageModel, security: Security, order: Order, request: UpdateOrderRequest) -> (bool, BrokerageMessageEvent)
        
            Returns true if the brokerage would allow 
             updating the order as specified by the request
        
        
            security: The security of the order
            order: The order to be updated
            request: The requested update to be made to the order
            Returns: True if the brokerage would allow updating the 
             order, false otherwise
        """
        pass

    def GetFeeModel(self, security):
        """
        GetFeeModel(self: InteractiveBrokersBrokerageModel, security: Security) -> IFeeModel
        
            Gets a new fee model that represents this 
             brokerage's fee structure
        
        
            security: The security to get a fee model for
            Returns: The new fee model for this brokerage
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountType):
        """ __new__(cls: type, accountType: AccountType) """
        pass

    DefaultMarkets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a map of the default markets to be used for each security type

Get: DefaultMarkets(self: InteractiveBrokersBrokerageModel) -> IReadOnlyDictionary[SecurityType, str]

"""


    DefaultMarketMap = None


class OandaBrokerageModel(DefaultBrokerageModel, IBrokerageModel):
    """
    Oanda Brokerage Model Implementation for Back Testing.
    
    OandaBrokerageModel(accountType: AccountType)
    """
    def CanSubmitOrder(self, security, order, message):
        """
        CanSubmitOrder(self: OandaBrokerageModel, security: Security, order: Order) -> (bool, BrokerageMessageEvent)
        
            Returns true if the brokerage could accept this 
             order. This takes into account
                    order 
             type, security type, and order size limits.
        
        
            order: The order to be processed
            Returns: True if the brokerage could process the order, 
             false otherwise
        """
        pass

    def GetFeeModel(self, security):
        """
        GetFeeModel(self: OandaBrokerageModel, security: Security) -> IFeeModel
        
            Gets a new fee model that represents this 
             brokerage's fee structure
        
        
            security: The security to get a fee model for
            Returns: The new fee model for this brokerage
        """
        pass

    def GetFillModel(self, security):
        """
        GetFillModel(self: OandaBrokerageModel, security: Security) -> IFillModel
        
            Gets a new fill model that represents this 
             brokerage's fill behavior
        
        
            security: The security to get fill model for
            Returns: The new fill model for this brokerage
        """
        pass

    def GetSettlementModel(self, security, accountType=None):
        """
        GetSettlementModel(self: OandaBrokerageModel, security: Security) -> ISettlementModel
        
            Gets a new settlement model for the security
        
            security: The security to get a settlement model for
            Returns: The settlement model for this brokerage
        """
        pass

    def GetSlippageModel(self, security):
        """
        GetSlippageModel(self: OandaBrokerageModel, security: Security) -> ISlippageModel
        
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
    def __new__(self, accountType):
        """ __new__(cls: type, accountType: AccountType) """
        pass

    DefaultMarkets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a map of the default markets to be used for each security type

Get: DefaultMarkets(self: OandaBrokerageModel) -> IReadOnlyDictionary[SecurityType, str]

"""


    DefaultMarketMap = None


class TradierBrokerageModel(DefaultBrokerageModel, IBrokerageModel):
    """
    Provides tradier specific properties
    
    TradierBrokerageModel(accountType: AccountType)
    """
    def ApplySplit(self, tickets, split):
        """ ApplySplit(self: TradierBrokerageModel, tickets: List[OrderTicket], split: Split) """
        pass

    def CanExecuteOrder(self, security, order):
        """
        CanExecuteOrder(self: TradierBrokerageModel, security: Security, order: Order) -> bool
        
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
        CanSubmitOrder(self: TradierBrokerageModel, security: Security, order: Order) -> (bool, BrokerageMessageEvent)
        
            Returns true if the brokerage could accept this 
             order. This takes into account
                    order 
             type, security type, and order size limits.
        
        
            security: The security of the order
            order: The order to be processed
            Returns: True if the brokerage could process the order, 
             false otherwise
        """
        pass

    def CanUpdateOrder(self, security, order, request, message):
        """
        CanUpdateOrder(self: TradierBrokerageModel, security: Security, order: Order, request: UpdateOrderRequest) -> (bool, BrokerageMessageEvent)
        
            Returns true if the brokerage would allow 
             updating the order as specified by the request
        
        
            security: The security of the order
            order: The order to be updated
            request: The requested update to be made to the order
            Returns: True if the brokerage would allow updating the 
             order, false otherwise
        """
        pass

    def GetFeeModel(self, security):
        """
        GetFeeModel(self: TradierBrokerageModel, security: Security) -> IFeeModel
        
            Gets a new fee model that represents this 
             brokerage's fee structure
        
        
            security: The security to get a fee model for
            Returns: The new fee model for this brokerage
        """
        pass

    def GetFillModel(self, security):
        """
        GetFillModel(self: TradierBrokerageModel, security: Security) -> IFillModel
        
            Gets a new fill model that represents this 
             brokerage's fill behavior
        
        
            security: The security to get fill model for
            Returns: The new fill model for this brokerage
        """
        pass

    def GetSlippageModel(self, security):
        """
        GetSlippageModel(self: TradierBrokerageModel, security: Security) -> ISlippageModel
        
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
    def __new__(self, accountType):
        """ __new__(cls: type, accountType: AccountType) """
        pass


