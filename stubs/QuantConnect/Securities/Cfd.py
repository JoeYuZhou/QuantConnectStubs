# encoding: utf-8
# module QuantConnect.Securities.Cfd calls itself Cfd
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Cfd(Security, ISecurityPrice):
    """
    CFD Security Object Implementation for CFD Assets
    
    Cfd(exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, config: SubscriptionDataConfig, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider)
    Cfd(symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider, securityCache: SecurityCache)
    """
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

    ContractMultiplier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the contract multiplier for this CFD security

Get: ContractMultiplier(self: Cfd) -> Decimal

"""

    MinimumPriceVariation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minimum price variation for this CFD security

Get: MinimumPriceVariation(self: Cfd) -> Decimal

"""


    SubscriptionsBag = None


class CfdCache(SecurityCache):
    """
    CFD specific caching support
    
    CfdCache()
    """

class CfdDataFilter(SecurityDataFilter, ISecurityDataFilter):
    """
    CFD packet by packet data filtering mechanism for dynamically detecting bad ticks.
    
    CfdDataFilter()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class CfdExchange(SecurityExchange):
    """
    CFD exchange class - information and helper tools for CFD exchange properties
    
    CfdExchange(exchangeHours: SecurityExchangeHours)
    """
    @staticmethod # known case of __new__
    def __new__(self, exchangeHours):
        """ __new__(cls: type, exchangeHours: SecurityExchangeHours) """
        pass

    TradingDaysPerYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of trading days per year for this security, used for performance statistics.

Get: TradingDaysPerYear(self: CfdExchange) -> int

"""



class CfdHolding(SecurityHolding):
    """
    CFD holdings implementation of the base securities class
    
    CfdHolding(security: Cfd, currencyConverter: ICurrencyConverter)
    """
    @staticmethod # known case of __new__
    def __new__(self, security, currencyConverter):
        """ __new__(cls: type, security: Cfd, currencyConverter: ICurrencyConverter) """
        pass

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The security being held

"""



