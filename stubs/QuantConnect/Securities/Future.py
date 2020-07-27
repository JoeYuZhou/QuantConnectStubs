# encoding: utf-8
# module QuantConnect.Securities.Future calls itself Future
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class EmptyFutureChainProvider(object, IFutureChainProvider):
    """
    An implementation of QuantConnect.Interfaces.IFutureChainProvider that always returns an empty list of contracts
    
    EmptyFutureChainProvider()
    """
    def GetFutureContractList(self, symbol, date):
        """
        GetFutureContractList(self: EmptyFutureChainProvider, symbol: Symbol, date: DateTime) -> IEnumerable[Symbol]
        
            Gets the list of future contracts for a given 
             underlying symbol
        
        
            symbol: The underlying symbol
            date: The date for which to request the future chain 
             (only used in backtesting)
        
            Returns: The list of future contracts
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class Future(Security, ISecurityPrice, IDerivativeSecurity):
    """
    Futures Security Object Implementation for Futures Assets
    
    Future(exchangeHours: SecurityExchangeHours, config: SubscriptionDataConfig, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider)
    Future(symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider, securityCache: SecurityCache)
    """
    def SetFilter(self, *__args):
        """
        SetFilter(self: Future, minExpiry: TimeSpan, maxExpiry: TimeSpan)
            Sets the 
             QuantConnect.Securities.Future.Future.ContractFilt
             er to a new instance of the filter
                    
             using the specified expiration range values
        
        
            minExpiry: The minimum time until expiry to include, for 
             example, TimeSpan.FromDays(10)
                    would 
             exclude contracts expiring in more than 10 days
        
            maxExpiry: The maximum time until expiry to include, for 
             example, TimeSpan.FromDays(10)
                    would 
             exclude contracts expiring in less than 10 days
        
        SetFilter(self: Future, minExpiryDays: int, maxExpiryDays: int)
            Sets the 
             QuantConnect.Securities.Future.Future.ContractFilt
             er to a new instance of the filter
                    
             using the specified expiration range values
        
        
            minExpiryDays: The minimum time, expressed in days, until expiry 
             to include, for example, 10
                    would 
             exclude contracts expiring in more than 10 days
        
            maxExpiryDays: The maximum time, expressed in days, until expiry 
             to include, for example, 10
                    would 
             exclude contracts expiring in less than 10 days
        
        SetFilter(self: Future, universeFunc: Func[FutureFilterUniverse, FutureFilterUniverse])SetFilter(self: Future, universeFunc: PyObject)
            Sets the 
             QuantConnect.Securities.Future.Future.ContractFilt
             er to a new universe selection function
        
        
            universeFunc: new universe selection function
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, exchangeHours: SecurityExchangeHours, config: SubscriptionDataConfig, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider)
        __new__(cls: type, symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider, securityCache: SecurityCache)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ContractFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the contract filter

Get: ContractFilter(self: Future) -> IDerivativeSecurityFilter

Set: ContractFilter(self: Future) = value
"""

    Expiry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the expiration date

Get: Expiry(self: Future) -> DateTime

"""

    IsFutureChain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this is the future chain security, false if it is a specific future contract

Get: IsFutureChain(self: Future) -> bool

"""

    IsFutureContract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this is a specific future contract security, false if it is the future chain security

Get: IsFutureContract(self: Future) -> bool

"""

    SettlementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if futures contract has physical or cash settlement on settlement

Get: SettlementType(self: Future) -> SettlementType

Set: SettlementType(self: Future) = value
"""

    Underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the underlying security object.

Get: Underlying(self: Future) -> Security

Set: Underlying(self: Future) = value
"""


    DefaultSettlementDays = 1
    DefaultSettlementTime = None
    SubscriptionsBag = None


class FutureCache(SecurityCache):
    """
    Future specific caching support
    
    FutureCache()
    """

class FutureExchange(SecurityExchange):
    """
    Future exchange class - information and helper tools for future exchange properties
    
    FutureExchange(exchangeHours: SecurityExchangeHours)
    """
    @staticmethod # known case of __new__
    def __new__(self, exchangeHours):
        """ __new__(cls: type, exchangeHours: SecurityExchangeHours) """
        pass

    TradingDaysPerYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of trading days per year for this security, 252.

Get: TradingDaysPerYear(self: FutureExchange) -> int

"""



class FutureHolding(SecurityHolding):
    """
    Future holdings implementation of the base securities class
    
    FutureHolding(security: Security, currencyConverter: ICurrencyConverter)
    """
    @staticmethod # known case of __new__
    def __new__(self, security, currencyConverter):
        """ __new__(cls: type, security: Security, currencyConverter: ICurrencyConverter) """
        pass

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The security being held

"""



class FutureMarginModel(SecurityMarginModel, IBuyingPowerModel):
    """
    Represents a simple margin model for margin futures. Margin file contains Initial and Maintenance margins
    
    FutureMarginModel(requiredFreeBuyingPowerPercent: Decimal, security: Security)
    """
    def GetInitialMarginRequiredForOrder(self, *args): #cannot find CLR method
        """
        GetInitialMarginRequiredForOrder(self: FutureMarginModel, parameters: InitialMarginRequiredForOrderParameters) -> Decimal
        
            Gets the total margin required to execute the 
             specified order in units of the account currency 
             including fees
        
        
            parameters: An object containing the portfolio, the security 
             and the order
        
            Returns: The total margin in terms of the currency quoted 
             in the order
        """
        pass

    def GetInitialMarginRequirement(self, *args): #cannot find CLR method
        """
        GetInitialMarginRequirement(self: FutureMarginModel, security: Security, quantity: Decimal) -> Decimal
        
            The margin that must be held in order to increase 
             the position by the provided quantity
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: FutureMarginModel, security: Security) -> Decimal
        
            Gets the current leverage of the security
        
            security: The security to get leverage for
            Returns: The current leverage in the security
        """
        pass

    def GetMaintenanceMargin(self, *args): #cannot find CLR method
        """
        GetMaintenanceMargin(self: FutureMarginModel, security: Security) -> Decimal
        
            Gets the margin currently alloted to the 
             specified holding
        
        
            security: The security to compute maintenance margin for
            Returns: The maintenance margin required for the
        """
        pass

    def GetMarginRemaining(self, *args): #cannot find CLR method
        """
        GetMarginRemaining(self: BuyingPowerModel, portfolio: SecurityPortfolioManager, security: Security, direction: OrderDirection) -> Decimal
        
            Gets the margin cash available for a trade
        
            portfolio: The algorithm's portfolio
            security: The security to be traded
            direction: The direction of the trade
            Returns: The margin available for the trade
        """
        pass

    def GetMaximumOrderQuantityForTargetBuyingPower(self, parameters):
        """
        GetMaximumOrderQuantityForTargetBuyingPower(self: FutureMarginModel, parameters: GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> GetMaximumOrderQuantityResult
        
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

    def SetLeverage(self, security, leverage):
        """
        SetLeverage(self: FutureMarginModel, security: Security, leverage: Decimal)
            Sets the leverage for the applicable securities, 
             i.e, futures
        
        
            leverage: The new leverage
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, requiredFreeBuyingPowerPercent, security):
        """ __new__(cls: type, requiredFreeBuyingPowerPercent: Decimal, security: Security) """
        pass

    EnableIntradayMargins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True will enable usage of intraday margins.

Get: EnableIntradayMargins(self: FutureMarginModel) -> bool

Set: EnableIntradayMargins(self: FutureMarginModel) = value
"""

    InitialIntradayMarginRequirement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Initial Intraday margin for the contract effective from the date of change

Get: InitialIntradayMarginRequirement(self: FutureMarginModel) -> Decimal

"""

    InitialOvernightMarginRequirement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Initial Overnight margin requirement for the contract effective from the date of change

Get: InitialOvernightMarginRequirement(self: FutureMarginModel) -> Decimal

"""

    MaintenanceIntradayMarginRequirement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maintenance Intraday margin requirement for the contract effective from the date of change

Get: MaintenanceIntradayMarginRequirement(self: FutureMarginModel) -> Decimal

"""

    MaintenanceOvernightMarginRequirement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maintenance Overnight margin requirement for the contract effective from the date of change

Get: MaintenanceOvernightMarginRequirement(self: FutureMarginModel) -> Decimal

"""


    RequiredFreeBuyingPowerPercent = None


class FuturesExpiryFunctions(object):
    """
    Calculate the date of a futures expiry given an expiry month and year
    
    FuturesExpiryFunctions()
    """
    @staticmethod
    def FuturesExpiryFunction(symbol):
        """
        FuturesExpiryFunction(symbol: Symbol) -> Func[DateTime, DateTime]
        
            Method to retrieve the Function for a specific 
             future symbol
        """
        pass

    DairyReportDates = None
    EnbridgeNoticeOfShipmentDates = None
    FuturesExpiryDictionary = None


class FuturesExpiryUtilityFunctions(object):
    """ Class to implement common functions used in FuturesExpiryFunctions """
    @staticmethod
    def AddBusinessDays(time, n, useEquityHolidays, holidayList):
        """ AddBusinessDays(time: DateTime, n: int, useEquityHolidays: bool, holidayList: IEnumerable[DateTime]) -> DateTime """
        pass

    @staticmethod
    def DairyLastTradeDate(time, lastTradeTime):
        """ DairyLastTradeDate(time: DateTime, lastTradeTime: Nullable[TimeSpan]) -> DateTime """
        pass

    @staticmethod
    def ExpiresInPreviousMonth(underlying):
        """
        ExpiresInPreviousMonth(underlying: str) -> int
        
            Returns the number of months prior to the 
             contract month that the future expires
        
        
            underlying: The future symbol
            Returns: The number of months prior it expires
        """
        pass

    @staticmethod
    def LastThursday(time):
        """
        LastThursday(time: DateTime) -> DateTime
        
            Method to retrieve the last weekday of any month
        
            time: Date from the given month
            Returns: Last day of the we
        """
        pass

    @staticmethod
    def LastWeekday(time, dayofWeek):
        """
        LastWeekday(time: DateTime, dayofWeek: DayOfWeek) -> DateTime
        
            Method to retrieve the last weekday of any month
        
            time: Date from the given month
            dayofWeek: the last weekday to be found
            Returns: Last day of the we
        """
        pass

    @staticmethod
    def NotHoliday(time):
        """
        NotHoliday(time: DateTime) -> bool
        
            Method to check whether a given time is holiday 
             or not
        
        
            time: The DateTime for consideration
            Returns: True if the time is not a holidays, otherwise 
             returns false
        """
        pass

    @staticmethod
    def NotPrecededByHoliday(thursday):
        """
        NotPrecededByHoliday(thursday: DateTime) -> bool
        
            This function takes Thursday as input and returns 
             true if four weekdays preceding it are not 
             Holidays
        
        
            thursday: DateTime of a given Thursday
            Returns: False if DayOfWeek is not Thursday or is not 
             preceded by four weekdays,Otherwise returns True
        """
        pass

    @staticmethod
    def NthBusinessDay(time, nthBusinessDay, additionalHolidays):
        """ NthBusinessDay(time: DateTime, nthBusinessDay: int, additionalHolidays: IEnumerable[DateTime]) -> DateTime """
        pass

    @staticmethod
    def NthFriday(time, n):
        """
        NthFriday(time: DateTime, n: int) -> DateTime
        
            Method to retrieve the Nth Friday of the given 
             month
        
        
            time: Date from the given month
            n: The order of the Friday in the period
            Returns: Nth Friday of given month
        """
        pass

    @staticmethod
    def NthLastBusinessDay(time, n, holidayList):
        """ NthLastBusinessDay(time: DateTime, n: int, holidayList: IEnumerable[DateTime]) -> DateTime """
        pass

    @staticmethod
    def NthWeekday(time, n, dayofWeek):
        """
        NthWeekday(time: DateTime, n: int, dayofWeek: DayOfWeek) -> DateTime
        
            Method to retrieve the Nth Weekday of the given 
             month
        
        
            time: Date from the given month
            n: The order of the Weekday in the period
            dayofWeek: The day of the week
            Returns: Nth Weekday of given month
        """
        pass

    @staticmethod
    def SecondFriday(time):
        """
        SecondFriday(time: DateTime) -> DateTime
        
            Method to retrieve the 2nd Friday of the given 
             month
        
        
            time: Date from the given month
            Returns: 2nd Friday of given month
        """
        pass

    @staticmethod
    def ThirdFriday(time):
        """
        ThirdFriday(time: DateTime) -> DateTime
        
            Method to retrieve the 3rd Friday of the given 
             month
        
        
            time: Date from the given month
            Returns: 3rd Friday of given month
        """
        pass

    @staticmethod
    def ThirdWednesday(time):
        """
        ThirdWednesday(time: DateTime) -> DateTime
        
            Method to retrieve third Wednesday of the given 
             month (usually Monday).
        
        
            time: Date from the given month
            Returns: Third Wednesday of the given month
        """
        pass

    __all__ = [
        'AddBusinessDays',
        'DairyLastTradeDate',
        'ExpiresInPreviousMonth',
        'LastThursday',
        'LastWeekday',
        'NotHoliday',
        'NotPrecededByHoliday',
        'NthBusinessDay',
        'NthFriday',
        'NthLastBusinessDay',
        'NthWeekday',
        'SecondFriday',
        'ThirdFriday',
        'ThirdWednesday',
    ]


