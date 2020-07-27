# encoding: utf-8
# module QuantConnect.Securities.Equity calls itself Equity
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Equity(Security, ISecurityPrice):
    """
    Equity Security Type : Extension of the underlying Security class for equity specific behaviours.
    
    Equity(symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider, securityCache: SecurityCache)
    Equity(exchangeHours: SecurityExchangeHours, config: SubscriptionDataConfig, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider)
    """
    def SetDataNormalizationMode(self, mode):
        """
        SetDataNormalizationMode(self: Equity, mode: DataNormalizationMode)
            Sets the data normalization mode to be used by 
             this security
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider, securityCache: SecurityCache)
        __new__(cls: type, exchangeHours: SecurityExchangeHours, config: SubscriptionDataConfig, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DefaultSettlementDays = 3
    DefaultSettlementTime = None
    SubscriptionsBag = None


class EquityCache(SecurityCache):
    """
    Equity cache override.
    
    EquityCache()
    """

class EquityDataFilter(SecurityDataFilter, ISecurityDataFilter):
    """
    Equity security type data filter
    
    EquityDataFilter()
    """
    def Filter(self, vehicle, data):
        """
        Filter(self: EquityDataFilter, vehicle: Security, data: BaseData) -> bool
        
            Equity filter the data: true - accept, false - 
             fail.
        
        
            vehicle: Security asset
            data: Data class
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class EquityExchange(SecurityExchange):
    """
    Equity exchange information
    
    EquityExchange()
    EquityExchange(exchangeHours: SecurityExchangeHours)
    """
    @staticmethod # known case of __new__
    def __new__(self, exchangeHours=None):
        """
        __new__(cls: type)
        __new__(cls: type, exchangeHours: SecurityExchangeHours)
        """
        pass

    TradingDaysPerYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of trading days in an equity calendar year - 252

Get: TradingDaysPerYear(self: EquityExchange) -> int

"""



class EquityHolding(SecurityHolding):
    """
    Holdings class for equities securities: no specific properties here but it is a placeholder for future equities specific behaviours.
    
    EquityHolding(security: Security, currencyConverter: ICurrencyConverter)
    """
    @staticmethod # known case of __new__
    def __new__(self, security, currencyConverter):
        """ __new__(cls: type, security: Security, currencyConverter: ICurrencyConverter) """
        pass

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The security being held

"""



