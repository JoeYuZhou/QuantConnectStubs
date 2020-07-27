# encoding: utf-8
# module QuantConnect.Orders.Fees calls itself Fees
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class FeeModel(object, IFeeModel):
    """
    Base class for any order fee model
    
    FeeModel()
    """
    def GetOrderFee(self, parameters):
        """
        GetOrderFee(self: FeeModel, parameters: OrderFeeParameters) -> OrderFee
        
            Gets the order fee associated with the specified 
             order.
        
        
            parameters: A QuantConnect.Orders.Fees.OrderFeeParameters 
             object
                    containing the security and 
             order
        
            Returns: The cost of the order in a 
             QuantConnect.Securities.CashAmount instance
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class AlphaStreamsFeeModel(FeeModel, IFeeModel):
    """
    Provides an implementation of QuantConnect.Orders.Fees.FeeModel that models order fees that alpha stream clients pay/receive
    
    AlphaStreamsFeeModel()
    """
    def GetOrderFee(self, parameters):
        """
        GetOrderFee(self: AlphaStreamsFeeModel, parameters: OrderFeeParameters) -> OrderFee
        
            Gets the order fee associated with the specified 
             order. This returns the cost
                    of the 
             transaction in the account currency
        
        
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


class BitfinexFeeModel(FeeModel, IFeeModel):
    """
    Provides an implementation of QuantConnect.Orders.Fees.FeeModel that models Bitfinex order fees
    
    BitfinexFeeModel()
    """
    def GetOrderFee(self, parameters):
        """
        GetOrderFee(self: BitfinexFeeModel, parameters: OrderFeeParameters) -> OrderFee
        
            Get the fee for this order in quote currency
        
            parameters: A QuantConnect.Orders.Fees.OrderFeeParameters 
             object
                    containing the security and 
             order
        
            Returns: The cost of the order in quote currency
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    MakerFee = None
    TakerFee = None


class ConstantFeeModel(FeeModel, IFeeModel):
    """
    Provides an order fee model that always returns the same order fee.
    
    ConstantFeeModel(fee: Decimal, currency: str)
    """
    def GetOrderFee(self, parameters):
        """
        GetOrderFee(self: ConstantFeeModel, parameters: OrderFeeParameters) -> OrderFee
        
            Returns the constant fee for the model in units 
             of the account currency
        
        
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
    def __new__(self, fee, currency):
        """ __new__(cls: type, fee: Decimal, currency: str) """
        pass


class FeeModelExtensions(object):
    """
    Provide extension method for QuantConnect.Orders.Fees.IFeeModel to enable
                backwards compatibility of invocations.
    """
    @staticmethod
    def GetOrderFee(model, security, order):
        """
        GetOrderFee(model: IFeeModel, security: Security, order: Order) -> Decimal
        
            Gets the order fee associated with the specified 
             order. This returns the cost
                    of the 
             transaction in the account currency
        
        
            model: The fee model
            security: The security matching the order
            order: The order to compute fees for
            Returns: The cost of the order in units of the account 
             currency
        """
        pass

    __all__ = [
        'GetOrderFee',
    ]


class FxcmFeeModel(FeeModel, IFeeModel):
    """
    Provides an implementation of QuantConnect.Orders.Fees.FeeModel that models FXCM order fees
    
    FxcmFeeModel(currency: str)
    """
    def GetOrderFee(self, parameters):
        """
        GetOrderFee(self: FxcmFeeModel, parameters: OrderFeeParameters) -> OrderFee
        
            Get the fee for this order in units of the 
             account currency
        
        
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
    def __new__(self, currency):
        """ __new__(cls: type, currency: str) """
        pass


class GDAXFeeModel(FeeModel, IFeeModel):
    """
    Provides an implementation of QuantConnect.Orders.Fees.FeeModel that models GDAX order fees
    
    GDAXFeeModel()
    """
    @staticmethod
    def GetFeePercentage(utcTime, isMaker):
        """
        GetFeePercentage(utcTime: DateTime, isMaker: bool) -> Decimal
        
            Returns the maker/taker fee percentage effective 
             at the requested date.
        
        
            utcTime: The date/time requested (UTC)
            isMaker: true if the maker percentage fee is requested, 
             false otherwise
        
            Returns: The fee percentage effective at the requested date
        """
        pass

    def GetOrderFee(self, parameters):
        """
        GetOrderFee(self: GDAXFeeModel, parameters: OrderFeeParameters) -> OrderFee
        
            Get the fee for this order in quote currency
        
            parameters: A QuantConnect.Orders.Fees.OrderFeeParameters 
             object
                    containing the security and 
             order
        
            Returns: The cost of the order in quote currency
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IFeeModel:
    """ Represents a model the simulates order fees """
    def GetOrderFee(self, parameters):
        """
        GetOrderFee(self: IFeeModel, parameters: OrderFeeParameters) -> OrderFee
        
            Gets the order fee associated with the specified 
             order.
        
        
            parameters: A QuantConnect.Orders.Fees.OrderFeeParameters 
             object
                    containing the security and 
             order
        
            Returns: The cost of the order in a 
             QuantConnect.Securities.CashAmount instance
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InteractiveBrokersFeeModel(FeeModel, IFeeModel):
    """
    Provides the default implementation of QuantConnect.Orders.Fees.IFeeModel
    
    InteractiveBrokersFeeModel(monthlyForexTradeAmountInUSDollars: Decimal, monthlyOptionsTradeAmountInContracts: Decimal)
    """
    def GetOrderFee(self, parameters):
        """
        GetOrderFee(self: InteractiveBrokersFeeModel, parameters: OrderFeeParameters) -> OrderFee
        
            Gets the order fee associated with the specified 
             order. This returns the cost
                    of the 
             transaction in the account currency
        
        
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
    def __new__(self, monthlyForexTradeAmountInUSDollars, monthlyOptionsTradeAmountInContracts):
        """ __new__(cls: type, monthlyForexTradeAmountInUSDollars: Decimal, monthlyOptionsTradeAmountInContracts: Decimal) """
        pass


class OrderFee(object):
    """
    Defines the result for QuantConnect.Orders.Fees.IFeeModel.GetOrderFee(QuantConnect.Orders.Fees.OrderFeeParameters)
    
    OrderFee(orderFee: CashAmount)
    """
    def ToString(self):
        """
        ToString(self: OrderFee) -> str
        
            This is for backward compatibility with old 
             'decimal' order fee
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, orderFee):
        """ __new__(cls: type, orderFee: CashAmount) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order fee

Get: Value(self: OrderFee) -> CashAmount

Set: Value(self: OrderFee) = value
"""


    Zero = None


class OrderFeeParameters(object):
    """
    Defines the parameters for QuantConnect.Orders.Fees.IFeeModel.GetOrderFee(QuantConnect.Orders.Fees.OrderFeeParameters)
    
    OrderFeeParameters(security: Security, order: Order)
    """
    @staticmethod # known case of __new__
    def __new__(self, security, order):
        """ __new__(cls: type, security: Security, order: Order) """
        pass

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order

Get: Order(self: OrderFeeParameters) -> Order

"""

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security

Get: Security(self: OrderFeeParameters) -> Security

"""



