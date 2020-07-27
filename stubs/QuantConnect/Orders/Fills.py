# encoding: utf-8
# module QuantConnect.Orders.Fills calls itself Fills
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Fill(object):
    """
    Defines the result for QuantConnect.Orders.Fills.IFillModel.Fill(QuantConnect.Orders.Fills.FillModelParameters)
    
    Fill(orderEvent: OrderEvent)
    """
    @staticmethod # known case of __new__
    def __new__(self, orderEvent):
        """ __new__(cls: type, orderEvent: OrderEvent) """
        pass

    OrderEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The order event associated to this QuantConnect.Orders.Fills.Fill instance

Get: OrderEvent(self: Fill) -> OrderEvent

"""



class FillModel(object, IFillModel):
    """
    Provides a base class for all fill models
    
    FillModel()
    """
    def Fill(self, parameters):
        """
        Fill(self: FillModel, parameters: FillModelParameters) -> Fill
        
            Return an order event with the fill details
        
            parameters: A QuantConnect.Orders.Fills.FillModelParameters 
             object containing the security and order
        
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def GetPrices(self, *args): #cannot find CLR method
        """
        GetPrices(self: FillModel, asset: Security, direction: OrderDirection) -> Prices
        
            Get the minimum and maximum price for this 
             security in the last bar:
        
        
            asset: Security asset we're checking
            direction: The order direction, decides whether to pick bid 
             or ask
        """
        pass

    def IsExchangeOpen(self, *args): #cannot find CLR method
        """
        IsExchangeOpen(asset: Security, isExtendedMarketHours: bool) -> bool
        
            Determines if the exchange is open using the 
             current time of the asset
        """
        pass

    def LimitFill(self, asset, order):
        """
        LimitFill(self: FillModel, asset: Security, order: LimitOrder) -> OrderEvent
        
            Default limit order fill model in the base 
             security class.
        
        
            asset: Security asset we're filling
            order: Order packet to model
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def MarketFill(self, asset, order):
        """
        MarketFill(self: FillModel, asset: Security, order: MarketOrder) -> OrderEvent
        
            Default market fill model for the base security 
             class. Fills at the last traded price.
        
        
            asset: Security asset we're filling
            order: Order packet to model
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def MarketOnCloseFill(self, asset, order):
        """
        MarketOnCloseFill(self: FillModel, asset: Security, order: MarketOnCloseOrder) -> OrderEvent
        
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
        MarketOnOpenFill(self: FillModel, asset: Security, order: MarketOnOpenOrder) -> OrderEvent
        
            Market on Open Fill Model. Return an order event 
             with the fill details
        
        
            asset: Asset we're trading with this order
            order: Order to be filled
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def SetPythonWrapper(self, pythonWrapper):
        """
        SetPythonWrapper(self: FillModel, pythonWrapper: FillModelPythonWrapper)
            Used to set the 
             QuantConnect.Python.FillModelPythonWrapper 
             instance if any
        """
        pass

    def StopLimitFill(self, asset, order):
        """
        StopLimitFill(self: FillModel, asset: Security, order: StopLimitOrder) -> OrderEvent
        
            Default stop limit fill model implementation in 
             base class security. (Stop Limit Order Type)
        
        
            asset: Security asset we're filling
            order: Order packet to model
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def StopMarketFill(self, asset, order):
        """
        StopMarketFill(self: FillModel, asset: Security, order: StopMarketOrder) -> OrderEvent
        
            Default stop fill model implementation in base 
             class security. (Stop Market Order Type)
        
        
            asset: Security asset we're filling
            order: Order packet to model
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The parameters instance to be used by the different XxxxFill() implementations

"""


    Prices = None
    PythonWrapper = None


class FillModelParameters(object):
    """
    Defines the parameters for the QuantConnect.Orders.Fills.IFillModel method
    
    FillModelParameters(security: Security, order: Order, configProvider: ISubscriptionDataConfigProvider, stalePriceTimeSpan: TimeSpan)
    """
    @staticmethod # known case of __new__
    def __new__(self, security, order, configProvider, stalePriceTimeSpan):
        """ __new__(cls: type, security: Security, order: Order, configProvider: ISubscriptionDataConfigProvider, stalePriceTimeSpan: TimeSpan) """
        pass

    ConfigProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the QuantConnect.Data.SubscriptionDataConfig provider

Get: ConfigProvider(self: FillModelParameters) -> ISubscriptionDataConfigProvider

"""

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the QuantConnect.Orders.Fills.FillModelParameters.Order

Get: Order(self: FillModelParameters) -> Order

"""

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the QuantConnect.Orders.Fills.FillModelParameters.Security

Get: Security(self: FillModelParameters) -> Security

"""

    StalePriceTimeSpan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minimum time span elapsed to consider a market fill price as stale (defaults to one hour)

Get: StalePriceTimeSpan(self: FillModelParameters) -> TimeSpan

"""



class IFillModel:
    """ Represents a model that simulates order fill events """
    def Fill(self, parameters):
        """
        Fill(self: IFillModel, parameters: FillModelParameters) -> Fill
        
            Return an order event with the fill details
        
            parameters: A QuantConnect.Orders.Fills.FillModelParameters 
             object containing the security and order
        
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ImmediateFillModel(FillModel, IFillModel):
    """
    Represents the default fill model used to simulate order fills
    
    ImmediateFillModel()
    """
    def GetPrices(self, *args): #cannot find CLR method
        """
        GetPrices(self: FillModel, asset: Security, direction: OrderDirection) -> Prices
        
            Get the minimum and maximum price for this 
             security in the last bar:
        
        
            asset: Security asset we're checking
            direction: The order direction, decides whether to pick bid 
             or ask
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The parameters instance to be used by the different XxxxFill() implementations

"""


    PythonWrapper = None


class LatestPriceFillModel(ImmediateFillModel, IFillModel):
    """
    This fill model is provided because currently the data sourced for Crypto
                is limited to one minute snapshots for Quote data. This fill model will
                ignore the trade/quote distinction and return the latest pricing information
                in order to determine the correct fill price
    
    LatestPriceFillModel()
    """
    def GetPrices(self, *args): #cannot find CLR method
        """
        GetPrices(self: LatestPriceFillModel, asset: Security, direction: OrderDirection) -> Prices
        
            Get the minimum and maximum price for this 
             security in the last bar
                    Ignore the 
             Trade/Quote distinction - fill with the latest 
             pricing information
        
        
            asset: Security asset we're checking
            direction: The order direction, decides whether to pick bid 
             or ask
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The parameters instance to be used by the different XxxxFill() implementations

"""


    PythonWrapper = None


