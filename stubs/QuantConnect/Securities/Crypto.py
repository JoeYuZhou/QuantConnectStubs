# encoding: utf-8
# module QuantConnect.Securities.Crypto calls itself Crypto
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Crypto(Security, ISecurityPrice, IBaseCurrencySymbol):
    """
    Crypto Security Object Implementation for Crypto Assets
    
    Crypto(exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, config: SubscriptionDataConfig, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider)
    Crypto(symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider, securityCache: SecurityCache)
    """
    @staticmethod
    def DecomposeCurrencyPair(symbol, symbolProperties, baseCurrency, quoteCurrency):
        """
        DecomposeCurrencyPair(symbol: Symbol, symbolProperties: SymbolProperties) -> (str, str)
        
            Decomposes the specified currency pair into a 
             base and quote currency provided as out 
             parameters
        
        
            symbol: The input symbol to be decomposed
            symbolProperties: The symbol properties for this security
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

Get: BaseCurrencySymbol(self: Crypto) -> str

"""

    Price = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the current value of the security.

Get: Price(self: Crypto) -> Decimal

"""


    SubscriptionsBag = None


class CryptoExchange(SecurityExchange):
    """
    Crypto exchange class - information and helper tools for Crypto exchange properties
    
    CryptoExchange(market: str)
    CryptoExchange(exchangeHours: SecurityExchangeHours)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, market: str)
        __new__(cls: type, exchangeHours: SecurityExchangeHours)
        """
        pass


class CryptoHolding(SecurityHolding):
    """
    Crypto holdings implementation of the base securities class
    
    CryptoHolding(security: Crypto, currencyConverter: ICurrencyConverter)
    """
    @staticmethod # known case of __new__
    def __new__(self, security, currencyConverter):
        """ __new__(cls: type, security: Crypto, currencyConverter: ICurrencyConverter) """
        pass

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The security being held

"""



