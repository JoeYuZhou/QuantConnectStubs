# encoding: utf-8
# module QuantConnect.Securities.Forex calls itself Forex
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Forex(Security, ISecurityPrice, IBaseCurrencySymbol):
    """
    FOREX Security Object Implementation for FOREX Assets
    
    Forex(exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, config: SubscriptionDataConfig, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider)
    Forex(symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider, securityCache: SecurityCache)
    """
    @staticmethod
    def DecomposeCurrencyPair(currencyPair, baseCurrency, quoteCurrency):
        """
        DecomposeCurrencyPair(currencyPair: str) -> (str, str)
        
            Decomposes the specified currency pair into a 
             base and quote currency provided as out 
             parameters
        
        
            currencyPair: The input currency pair to be decomposed, for 
             example, "EURUSD"
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, config: SubscriptionDataConfig, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider)
        __new__(cls: type, symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider, securityCache: SecurityCache)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BaseCurrencySymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the currency acquired by going long this currency pair

Get: BaseCurrencySymbol(self: Forex) -> str

"""


    SubscriptionsBag = None


class ForexCache(SecurityCache):
    """
    Forex specific caching support
    
    ForexCache()
    """

class ForexDataFilter(SecurityDataFilter, ISecurityDataFilter):
    """
    Forex packet by packet data filtering mechanism for dynamically detecting bad ticks.
    
    ForexDataFilter()
    """
    def Filter(self, vehicle, data):
        """
        Filter(self: ForexDataFilter, vehicle: Security, data: BaseData) -> bool
        
            Forex data filter: a true value means accept the 
             packet, a false means fail.
        
        
            vehicle: Security asset
            data: Data object we're scanning to filter
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ForexExchange(SecurityExchange):
    """
    Forex exchange class - information and helper tools for forex exchange properties
    
    ForexExchange()
    ForexExchange(exchangeHours: SecurityExchangeHours)
    """
    @staticmethod # known case of __new__
    def __new__(self, exchangeHours=None):
        """
        __new__(cls: type)
        __new__(cls: type, exchangeHours: SecurityExchangeHours)
        """
        pass

    TradingDaysPerYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of trading days per year for this security, used for performance statistics.

Get: TradingDaysPerYear(self: ForexExchange) -> int

"""



class ForexHolding(SecurityHolding):
    """
    FOREX holdings implementation of the base securities class
    
    ForexHolding(security: Forex, currencyConverter: ICurrencyConverter)
    """
    def TotalCloseProfitPips(self):
        """
        TotalCloseProfitPips(self: ForexHolding) -> Decimal
        
            Profit in pips if we closed the holdings right 
             now including the approximate fees
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, security, currencyConverter):
        """ __new__(cls: type, security: Forex, currencyConverter: ICurrencyConverter) """
        pass

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The security being held

"""



