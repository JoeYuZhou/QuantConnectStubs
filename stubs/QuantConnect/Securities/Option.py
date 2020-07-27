# encoding: utf-8
# module QuantConnect.Securities.Option calls itself Option
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ConstantQLRiskFreeRateEstimator(object, IQLRiskFreeRateEstimator):
    """
    Class implements default flat risk free curve, implementing QuantConnect.Securities.Option.IQLRiskFreeRateEstimator.
    
    ConstantQLRiskFreeRateEstimator(riskFreeRate: float)
    """
    def Estimate(self, security, slice, contract):
        """
        Estimate(self: ConstantQLRiskFreeRateEstimator, security: Security, slice: Slice, contract: OptionContract) -> float
        
            Returns current flat estimate of the risk free 
             rate
        
        
            security: The option security object
            slice: The current data slice. This can be used to 
             access other information
                    available 
             to the algorithm
        
            contract: The option contract to evaluate
            Returns: The estimate
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, riskFreeRate):
        """ __new__(cls: type, riskFreeRate: float) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class CurrentPriceOptionPriceModel(object, IOptionPriceModel):
    """
    Provides a default implementation of QuantConnect.Securities.Option.IOptionPriceModel that does not compute any
                greeks and uses the current price for the theoretical price. 
                This is a stub implementation until the real models are implemented
    
    CurrentPriceOptionPriceModel()
    """
    def Evaluate(self, security, slice, contract):
        """
        Evaluate(self: CurrentPriceOptionPriceModel, security: Security, slice: Slice, contract: OptionContract) -> OptionPriceModelResult
        
            Creates a new 
             QuantConnect.Securities.Option.OptionPriceModelRes
             ult containing the current 
             QuantConnect.Securities.Security.Price
                  
               and a default, empty instance of first Order 
             QuantConnect.Data.Market.Greeks
        
        
            security: The option security object
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
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class EmptyOptionChainProvider(object, IOptionChainProvider):
    """
    An implementation of QuantConnect.Interfaces.IOptionChainProvider that always returns an empty list of contracts
    
    EmptyOptionChainProvider()
    """
    def GetOptionContractList(self, symbol, date):
        """
        GetOptionContractList(self: EmptyOptionChainProvider, symbol: Symbol, date: DateTime) -> IEnumerable[Symbol]
        
            Gets the list of option contracts for a given 
             underlying symbol
        
        
            symbol: The underlying symbol
            date: The date for which to request the option chain 
             (only used in backtesting)
        
            Returns: The list of option contracts
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class IOptionPriceModel:
    """ Defines a model used to calculate the theoretical price of an option contract. """
    def Evaluate(self, security, slice, contract):
        """
        Evaluate(self: IOptionPriceModel, security: Security, slice: Slice, contract: OptionContract) -> OptionPriceModelResult
        
            Evaluates the specified option contract to 
             compute a theoretical price, IV and greeks
        
        
            security: The option security object
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


class Option(Security, ISecurityPrice, IDerivativeSecurity, IOptionPrice):
    """
    Option Security Object Implementation for Option Assets
    
    Option(exchangeHours: SecurityExchangeHours, config: SubscriptionDataConfig, quoteCurrency: Cash, symbolProperties: OptionSymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider)
    Option(symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: OptionSymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider, securityCache: SecurityCache)
    """
    def EvaluatePriceModel(self, slice, contract):
        """
        EvaluatePriceModel(self: Option, slice: Slice, contract: OptionContract) -> OptionPriceModelResult
        
            For this option security object, evaluates the 
             specified option
                    contract to compute 
             a theoretical price, IV and greeks
        
        
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

    def GetAggregateExerciseAmount(self):
        """
        GetAggregateExerciseAmount(self: Option) -> Decimal
        
            Aggregate exercise amount or aggregate contract 
             value. It is the total amount of cash one will 
             pay (or receive) for the shares of the
                  
               underlying stock if he/she decides to exercise 
             (or is assigned an exercise notice). This amount 
             is not the premium paid or received for an equity 
             option.
        """
        pass

    def GetExerciseQuantity(self, quantity):
        """
        GetExerciseQuantity(self: Option, quantity: Decimal) -> Decimal
        
            Returns the actual number of the underlying 
             shares that are going to change hands on 
             exercise. For instance, after reverse split
             
                    we may have 1 option contract with 
             multiplier of 100 with right to buy/sell only 50 
             shares of underlying stock.
        """
        pass

    def GetIntrinsicValue(self, underlyingPrice):
        """
        GetIntrinsicValue(self: Option, underlyingPrice: Decimal) -> Decimal
        
            Intrinsic value function of the option
        """
        pass

    def GetPayOff(self, underlyingPrice):
        """
        GetPayOff(self: Option, underlyingPrice: Decimal) -> Decimal
        
            Option payoff function at expiration time
        
            underlyingPrice: The price of the underlying
        """
        pass

    def IsAutoExercised(self, underlyingPrice):
        """
        IsAutoExercised(self: Option, underlyingPrice: Decimal) -> bool
        
            Checks if option is eligible for automatic 
             exercise on expiration
        """
        pass

    def SetDataNormalizationMode(self, mode):
        """
        SetDataNormalizationMode(self: Option, mode: DataNormalizationMode)
            Sets the data normalization mode to be used by 
             this security
        """
        pass

    def SetFilter(self, *__args):
        """
        SetFilter(self: Option, minStrike: int, maxStrike: int)
            Sets the 
             QuantConnect.Securities.Option.Option.ContractFilt
             er to a new instance of the filter
                    
             using the specified min and max strike values. 
             Contracts with expirations further than 35
              
                   days out will also be filtered.
        
        
            minStrike: The min strike rank relative to market price, for 
             example, -1 would put
                    a lower bound 
             of one strike under market price, where a +1 
             would put a lower bound of one strike
                   
              over market price
        
            maxStrike: The max strike rank relative to market place, for 
             example, -1 would put
                    an upper bound 
             of on strike under market price, where a +1 would 
             be an upper bound of one strike
                    over 
             market price
        
        SetFilter(self: Option, minExpiry: TimeSpan, maxExpiry: TimeSpan)
            Sets the 
             QuantConnect.Securities.Option.Option.ContractFilt
             er to a new instance of the filter
                    
             using the specified min and max strike and 
             expiration range values
        
        
            minExpiry: The minimum time until expiry to include, for 
             example, TimeSpan.FromDays(10)
                    would 
             exclude contracts expiring in more than 10 days
        
            maxExpiry: The maxmium time until expiry to include, for 
             example, TimeSpan.FromDays(10)
                    would 
             exclude contracts expiring in less than 10 days
        
        SetFilter(self: Option, minStrike: int, maxStrike: int, minExpiry: TimeSpan, maxExpiry: TimeSpan)
            Sets the 
             QuantConnect.Securities.Option.Option.ContractFilt
             er to a new instance of the filter
                    
             using the specified min and max strike and 
             expiration range values
        
        
            minStrike: The min strike rank relative to market price, for 
             example, -1 would put
                    a lower bound 
             of one strike under market price, where a +1 
             would put a lower bound of one strike
                   
              over market price
        
            maxStrike: The max strike rank relative to market place, for 
             example, -1 would put
                    an upper bound 
             of on strike under market price, where a +1 would 
             be an upper bound of one strike
                    over 
             market price
        
            minExpiry: The minimum time until expiry to include, for 
             example, TimeSpan.FromDays(10)
                    would 
             exclude contracts expiring in more than 10 days
        
            maxExpiry: The maxmium time until expiry to include, for 
             example, TimeSpan.FromDays(10)
                    would 
             exclude contracts expiring in less than 10 days
        
        SetFilter(self: Option, minStrike: int, maxStrike: int, minExpiryDays: int, maxExpiryDays: int)
            Sets the 
             QuantConnect.Securities.Option.Option.ContractFilt
             er to a new instance of the filter
                    
             using the specified min and max strike and 
             expiration range values
        
        
            minStrike: The min strike rank relative to market price, for 
             example, -1 would put
                    a lower bound 
             of one strike under market price, where a +1 
             would put a lower bound of one strike
                   
              over market price
        
            maxStrike: The max strike rank relative to market place, for 
             example, -1 would put
                    an upper bound 
             of on strike under market price, where a +1 would 
             be an upper bound of one strike
                    over 
             market price
        
            minExpiryDays: The minimum time, expressed in days, until expiry 
             to include, for example, 10
                    would 
             exclude contracts expiring in more than 10 days
        
            maxExpiryDays: The maximum time, expressed in days, until expiry 
             to include, for example, 10
                    would 
             exclude contracts expiring in less than 10 days
        
        SetFilter(self: Option, universeFunc: Func[OptionFilterUniverse, OptionFilterUniverse])SetFilter(self: Option, universeFunc: PyObject)
            Sets the 
             QuantConnect.Securities.Option.Option.ContractFilt
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
        __new__(cls: type, exchangeHours: SecurityExchangeHours, config: SubscriptionDataConfig, quoteCurrency: Cash, symbolProperties: OptionSymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider)
        __new__(cls: type, symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: OptionSymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider, securityCache: SecurityCache)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AskPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent ask price if available

Get: AskPrice(self: Option) -> Decimal

"""

    BidPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent bid price if available

Get: BidPrice(self: Option) -> Decimal

"""

    ContractFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the contract filter

Get: ContractFilter(self: Option) -> IDerivativeSecurityFilter

Set: ContractFilter(self: Option) = value
"""

    ContractMultiplier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The contract multiplier for the option security

Get: ContractMultiplier(self: Option) -> int

Set: ContractMultiplier(self: Option) = value
"""

    ContractUnitOfTrade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When the holder of an equity option exercises one contract, or when the writer of an equity option is assigned
            an exercise notice on one contract, this unit of trade, usually 100 shares of the underlying security, changes hands.

Get: ContractUnitOfTrade(self: Option) -> int

Set: ContractUnitOfTrade(self: Option) = value
"""

    EnableGreekApproximation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When enabled, approximates Greeks if corresponding pricing model didn't calculate exact numbers

Get: EnableGreekApproximation(self: Option) -> bool

Set: EnableGreekApproximation(self: Option) = value
"""

    ExerciseSettlement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if option contract has physical or cash settlement on exercise

Get: ExerciseSettlement(self: Option) -> SettlementType

Set: ExerciseSettlement(self: Option) = value
"""

    Expiry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the expiration date

Get: Expiry(self: Option) -> DateTime

"""

    IsOptionChain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this is the option chain security, false if it is a specific option contract

Get: IsOptionChain(self: Option) -> bool

"""

    IsOptionContract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this is a specific option contract security, false if it is the option chain security

Get: IsOptionContract(self: Option) -> bool

"""

    OptionExerciseModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fill model used to produce fill events for this security

Get: OptionExerciseModel(self: Option) -> IOptionExerciseModel

Set: OptionExerciseModel(self: Option) = value
"""

    PriceModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the price model for this option security

Get: PriceModel(self: Option) -> IOptionPriceModel

Set: PriceModel(self: Option) = value
"""

    Right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the right being purchased (call [right to buy] or put [right to sell])

Get: Right(self: Option) -> OptionRight

"""

    StrikePrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the strike price

Get: StrikePrice(self: Option) -> Decimal

"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the option style

Get: Style(self: Option) -> OptionStyle

"""

    Underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the underlying security object.

Get: Underlying(self: Option) -> Security

Set: Underlying(self: Option) = value
"""


    DefaultSettlementDays = 1
    DefaultSettlementTime = None
    SubscriptionsBag = None


class OptionCache(SecurityCache):
    """
    Option specific caching support
    
    OptionCache()
    """

class OptionDataFilter(SecurityDataFilter, ISecurityDataFilter):
    """
    Option packet by packet data filtering mechanism for dynamically detecting bad ticks.
    
    OptionDataFilter()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class OptionExchange(SecurityExchange):
    """
    Option exchange class - information and helper tools for option exchange properties
    
    OptionExchange(exchangeHours: SecurityExchangeHours)
    """
    @staticmethod # known case of __new__
    def __new__(self, exchangeHours):
        """ __new__(cls: type, exchangeHours: SecurityExchangeHours) """
        pass

    TradingDaysPerYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of trading days per year for this security, 252.

Get: TradingDaysPerYear(self: OptionExchange) -> int

"""



class OptionHolding(SecurityHolding):
    """
    Option holdings implementation of the base securities class
    
    OptionHolding(security: Option, currencyConverter: ICurrencyConverter)
    """
    @staticmethod # known case of __new__
    def __new__(self, security, currencyConverter):
        """ __new__(cls: type, security: Option, currencyConverter: ICurrencyConverter) """
        pass

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The security being held

"""



class OptionMarginModel(SecurityMarginModel, IBuyingPowerModel):
    """
    Represents a simple option margin model.
    
    OptionMarginModel(requiredFreeBuyingPowerPercent: Decimal)
    """
    def GetInitialMarginRequiredForOrder(self, *args): #cannot find CLR method
        """
        GetInitialMarginRequiredForOrder(self: OptionMarginModel, parameters: InitialMarginRequiredForOrderParameters) -> Decimal
        
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
        GetInitialMarginRequirement(self: OptionMarginModel, security: Security, quantity: Decimal) -> Decimal
        
            The margin that must be held in order to increase 
             the position by the provided quantity
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: OptionMarginModel, security: Security) -> Decimal
        
            Gets the current leverage of the security
        
            security: The security to get leverage for
            Returns: The current leverage in the security
        """
        pass

    def GetMaintenanceMargin(self, *args): #cannot find CLR method
        """
        GetMaintenanceMargin(self: OptionMarginModel, security: Security) -> Decimal
        
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

    def SetLeverage(self, security, leverage):
        """
        SetLeverage(self: OptionMarginModel, security: Security, leverage: Decimal)
            Sets the leverage for the applicable securities, 
             i.e, options.
        
        
            leverage: The new leverage
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, requiredFreeBuyingPowerPercent):
        """ __new__(cls: type, requiredFreeBuyingPowerPercent: Decimal) """
        pass

    RequiredFreeBuyingPowerPercent = None


class OptionPortfolioModel(SecurityPortfolioModel, ISecurityPortfolioModel):
    """
    Provides an implementation of QuantConnect.Securities.ISecurityPortfolioModel for options that supports
                default fills as well as option exercising.
    
    OptionPortfolioModel()
    """
    def ProcessExerciseFill(self, portfolio, security, order, fill):
        """
        ProcessExerciseFill(self: OptionPortfolioModel, portfolio: SecurityPortfolioManager, security: Security, order: Order, fill: OrderEvent)
            Processes exercise/assignment event to the 
             portfolio
        
        
            portfolio: The algorithm's portfolio
            security: Option security
            order: The order object to be applied
            fill: The order event fill object to be applied
        """
        pass

    def ProcessFill(self, portfolio, security, fill):
        """
        ProcessFill(self: OptionPortfolioModel, portfolio: SecurityPortfolioManager, security: Security, fill: OrderEvent)
            Performs application of an OrderEvent to the 
             portfolio
        
        
            portfolio: The algorithm's portfolio
            security: Option security
            fill: The order event fill object to be applied
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class OptionPriceModelResult(object):
    """
    Result type for QuantConnect.Securities.Option.IOptionPriceModel.Evaluate(QuantConnect.Securities.Security,QuantConnect.Data.Slice,QuantConnect.Data.Market.OptionContract)
    
    OptionPriceModelResult(theoreticalPrice: Decimal, greeks: Greeks)
    OptionPriceModelResult(theoreticalPrice: Decimal, impliedVolatility: Func[Decimal], greeks: Func[Greeks])
    """
    @staticmethod # known case of __new__
    def __new__(self, theoreticalPrice, *__args):
        """
        __new__(cls: type, theoreticalPrice: Decimal, greeks: Greeks)
        __new__(cls: type, theoreticalPrice: Decimal, impliedVolatility: Func[Decimal], greeks: Func[Greeks])
        """
        pass

    Greeks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the various sensitivities as computed by the QuantConnect.Securities.Option.IOptionPriceModel

Get: Greeks(self: OptionPriceModelResult) -> Greeks

"""

    ImpliedVolatility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the implied volatility of the option contract

Get: ImpliedVolatility(self: OptionPriceModelResult) -> Decimal

"""

    TheoreticalPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the theoretical price as computed by the QuantConnect.Securities.Option.IOptionPriceModel

Get: TheoreticalPrice(self: OptionPriceModelResult) -> Decimal

"""



class OptionPriceModels(object):
    """ Static class contains definitions of major option pricing models that can be used in LEAN """
    @staticmethod
    def AdditiveEquiprobabilities():
        """
        AdditiveEquiprobabilities() -> IOptionPriceModel
        
            Pricing engine for vanilla options using binomial 
             trees. Additive Equiprobabilities model.
                
                 QuantLib reference: 
             http://quantlib.org/reference/class_quant_lib_1_1_
             f_d_european_engine.html
        
            Returns: New option price model instance
        """
        pass

    @staticmethod
    def BaroneAdesiWhaley():
        """
        BaroneAdesiWhaley() -> IOptionPriceModel
        
            Barone-Adesi and Whaley pricing engine for 
             American options (1987)
                    QuantLib 
             reference: 
             http://quantlib.org/reference/class_quant_lib_1_1_
             barone_adesi_whaley_approximation_engine.html
        
            Returns: New option price model instance
        """
        pass

    @staticmethod
    def BinomialCoxRossRubinstein():
        """
        BinomialCoxRossRubinstein() -> IOptionPriceModel
        
            Pricing engine for vanilla options using binomial 
             trees. Cox-Ross-Rubinstein(CRR) model.
                  
               QuantLib reference: 
             http://quantlib.org/reference/class_quant_lib_1_1_
             f_d_european_engine.html
        
            Returns: New option price model instance
        """
        pass

    @staticmethod
    def BinomialJarrowRudd():
        """
        BinomialJarrowRudd() -> IOptionPriceModel
        
            Pricing engine for vanilla options using binomial 
             trees. Jarrow-Rudd model.
                    QuantLib 
             reference: 
             http://quantlib.org/reference/class_quant_lib_1_1_
             f_d_european_engine.html
        
            Returns: New option price model instance
        """
        pass

    @staticmethod
    def BinomialJoshi():
        """
        BinomialJoshi() -> IOptionPriceModel
        
            Pricing engine for vanilla options using binomial 
             trees. Joshi model.
                    QuantLib 
             reference: 
             http://quantlib.org/reference/class_quant_lib_1_1_
             f_d_european_engine.html
        
            Returns: New option price model instance
        """
        pass

    @staticmethod
    def BinomialLeisenReimer():
        """
        BinomialLeisenReimer() -> IOptionPriceModel
        
            Pricing engine for vanilla options using binomial 
             trees. Leisen-Reimer model.
                    QuantLib 
             reference: 
             http://quantlib.org/reference/class_quant_lib_1_1_
             f_d_european_engine.html
        
            Returns: New option price model instance
        """
        pass

    @staticmethod
    def BinomialTian():
        """
        BinomialTian() -> IOptionPriceModel
        
            Pricing engine for vanilla options using binomial 
             trees. Tian model.
                    QuantLib 
             reference: 
             http://quantlib.org/reference/class_quant_lib_1_1_
             f_d_european_engine.html
        
            Returns: New option price model instance
        """
        pass

    @staticmethod
    def BinomialTrigeorgis():
        """
        BinomialTrigeorgis() -> IOptionPriceModel
        
            Pricing engine for vanilla options using binomial 
             trees. Trigeorgis model.
                    QuantLib 
             reference: 
             http://quantlib.org/reference/class_quant_lib_1_1_
             f_d_european_engine.html
        
            Returns: New option price model instance
        """
        pass

    @staticmethod
    def BjerksundStensland():
        """
        BjerksundStensland() -> IOptionPriceModel
        
            Bjerksund and Stensland pricing engine for 
             American options (1993) 
                    QuantLib 
             reference: 
             http://quantlib.org/reference/class_quant_lib_1_1_
             bjerksund_stensland_approximation_engine.html
        
            Returns: New option price model instance
        """
        pass

    @staticmethod
    def BlackScholes():
        """
        BlackScholes() -> IOptionPriceModel
        
            Pricing engine for European vanilla options using 
             analytical formulae. 
                    QuantLib 
             reference: 
             http://quantlib.org/reference/class_quant_lib_1_1_
             analytic_european_engine.html
        
            Returns: New option price model instance
        """
        pass

    @staticmethod
    def CrankNicolsonFD():
        """
        CrankNicolsonFD() -> IOptionPriceModel
        
            Pricing engine for European options using 
             finite-differences. 
                    QuantLib 
             reference: 
             http://quantlib.org/reference/class_quant_lib_1_1_
             f_d_european_engine.html
        
            Returns: New option price model instance
        """
        pass

    @staticmethod
    def Integral():
        """
        Integral() -> IOptionPriceModel
        
            Pricing engine for European vanilla options using 
             integral approach. 
                    QuantLib 
             reference: 
             http://quantlib.org/reference/class_quant_lib_1_1_
             integral_engine.html
        
            Returns: New option price model instance
        """
        pass

    __all__ = [
        'AdditiveEquiprobabilities',
        'BaroneAdesiWhaley',
        'BinomialCoxRossRubinstein',
        'BinomialJarrowRudd',
        'BinomialJoshi',
        'BinomialLeisenReimer',
        'BinomialTian',
        'BinomialTrigeorgis',
        'BjerksundStensland',
        'BlackScholes',
        'CrankNicolsonFD',
        'Integral',
    ]


class OptionStrategies(object):
    # no doc
    @staticmethod
    def BearCallSpread(canonicalOption, leg1Strike, leg2Strike, expiration):
        """
        BearCallSpread(canonicalOption: Symbol, leg1Strike: Decimal, leg2Strike: Decimal, expiration: DateTime) -> OptionStrategy
        
            Method creates new Bear Call Spread strategy, 
             that consists of two calls with the same 
             expiration but different strikes.
                    
             The strike price of the short call is below the 
             strike of the long call. This is a credit spread.
        
        
            canonicalOption: Option symbol
            leg1Strike: The strike price of the short call
            leg2Strike: The strike price of the long call
            expiration: Option expiration date
            Returns: Option strategy specification
        """
        pass

    @staticmethod
    def BearPutSpread(canonicalOption, leg1Strike, leg2Strike, expiration):
        """
        BearPutSpread(canonicalOption: Symbol, leg1Strike: Decimal, leg2Strike: Decimal, expiration: DateTime) -> OptionStrategy
        
            Method creates new Bear Put Spread strategy, that 
             consists of two puts with the same expiration but 
             different strikes.
                    The strike price 
             of the short put is below the strike of the long 
             put. This is a debit spread.
        
        
            canonicalOption: Option symbol
            leg1Strike: The strike price of the long put
            leg2Strike: The strike price of the short put
            expiration: Option expiration date
            Returns: Option strategy specification
        """
        pass

    @staticmethod
    def BullCallSpread(canonicalOption, leg1Strike, leg2Strike, expiration):
        """
        BullCallSpread(canonicalOption: Symbol, leg1Strike: Decimal, leg2Strike: Decimal, expiration: DateTime) -> OptionStrategy
        
            Method creates new Bull Call Spread strategy, 
             that consists of two calls with the same 
             expiration but different strikes.
                    
             The strike price of the short call is higher than 
             the strike of the long call. This is a debit 
             spread.
        
        
            canonicalOption: Option symbol
            leg1Strike: The strike price of the long call
            leg2Strike: The strike price of the short call
            expiration: Option expiration date
            Returns: Option strategy specification
        """
        pass

    @staticmethod
    def BullPutSpread(canonicalOption, leg1Strike, leg2Strike, expiration):
        """
        BullPutSpread(canonicalOption: Symbol, leg1Strike: Decimal, leg2Strike: Decimal, expiration: DateTime) -> OptionStrategy
        
            Method creates new Bull Put Spread strategy, that 
             consists of two puts with the same expiration but 
             different strikes.
                    The strike price 
             of the short put is above the strike of the long 
             put. This is a credit spread.
        
        
            canonicalOption: Option symbol
            leg1Strike: The strike price of the short put
            leg2Strike: The strike price of the long put
            expiration: Option expiration date
            Returns: Option strategy specification
        """
        pass

    @staticmethod
    def CallButterfly(canonicalOption, leg1Strike, leg2Strike, leg3Strike, expiration):
        """
        CallButterfly(canonicalOption: Symbol, leg1Strike: Decimal, leg2Strike: Decimal, leg3Strike: Decimal, expiration: DateTime) -> OptionStrategy
        
            Method creates new Call Butterfly strategy, that 
             consists of two short calls at a middle strike, 
             and one long call each at a lower and upper 
             strike.
                    The upper and lower strikes 
             must both be equidistant from the middle strike.
        
        
            canonicalOption: Option symbol
            leg1Strike: The upper strike price of the long call
            leg2Strike: The middle strike price of the two short calls
            leg3Strike: The lower strike price of the long call
            expiration: Option expiration date
            Returns: Option strategy specification
        """
        pass

    @staticmethod
    def CallCalendarSpread(canonicalOption, strike, expiration1, expiration2):
        """
        CallCalendarSpread(canonicalOption: Symbol, strike: Decimal, expiration1: DateTime, expiration2: DateTime) -> OptionStrategy
        
            Method creates new Call Calendar Spread strategy, 
             that is a short one call option and long a second 
             call option with a more distant expiration.
        
        
            canonicalOption: Option symbol
            strike: The strike price of the both legs
            expiration1: Option expiration near date
            expiration2: Option expiration far date
            Returns: Option strategy specification
        """
        pass

    @staticmethod
    def PutButterfly(canonicalOption, leg1Strike, leg2Strike, leg3Strike, expiration):
        """
        PutButterfly(canonicalOption: Symbol, leg1Strike: Decimal, leg2Strike: Decimal, leg3Strike: Decimal, expiration: DateTime) -> OptionStrategy
        
            Method creates new Put Butterfly strategy, that 
             consists of two short puts at a middle strike, 
             and one long put each at a lower and upper 
             strike.
                    The upper and lower strikes 
             must both be equidistant from the middle strike.
        
        
            canonicalOption: Option symbol
            leg1Strike: The upper strike price of the long put
            leg2Strike: The middle strike price of the two short puts
            leg3Strike: The lower strike price of the long put
            expiration: Option expiration date
            Returns: Option strategy specification
        """
        pass

    @staticmethod
    def PutCalendarSpread(canonicalOption, strike, expiration1, expiration2):
        """
        PutCalendarSpread(canonicalOption: Symbol, strike: Decimal, expiration1: DateTime, expiration2: DateTime) -> OptionStrategy
        
            Method creates new Put Calendar Spread strategy, 
             that is a short one put option and long a second 
             put option with a more distant expiration.
        
        
            canonicalOption: Option symbol
            strike: The strike price of the both legs
            expiration1: Option expiration near date
            expiration2: Option expiration far date
            Returns: Option strategy specification
        """
        pass

    @staticmethod
    def Straddle(canonicalOption, strike, expiration):
        """
        Straddle(canonicalOption: Symbol, strike: Decimal, expiration: DateTime) -> OptionStrategy
        
            Method creates new Straddle strategy, that is a 
             combination of buying a call and buying a put, 
             both with the same strike price and expiration.
        
        
            canonicalOption: Option symbol
            strike: The strike price of the both legs
            expiration: Option expiration date
            Returns: Option strategy specification
        """
        pass

    @staticmethod
    def Strangle(canonicalOption, leg1Strike, leg2Strike, expiration):
        """
        Strangle(canonicalOption: Symbol, leg1Strike: Decimal, leg2Strike: Decimal, expiration: DateTime) -> OptionStrategy
        
            Method creates new Strangle strategy, that buying 
             a call option and a put option with the same 
             expiration date.
                    The strike price of 
             the call is above the strike of the put.
        
        
            canonicalOption: Option symbol
            leg1Strike: The strike price of the long call
            leg2Strike: The strike price of the long put
            expiration: Option expiration date
            Returns: Option strategy specification
        """
        pass

    __all__ = [
        'BearCallSpread',
        'BearPutSpread',
        'BullCallSpread',
        'BullPutSpread',
        'CallButterfly',
        'CallCalendarSpread',
        'PutButterfly',
        'PutCalendarSpread',
        'Straddle',
        'Strangle',
    ]


class OptionStrategy(object):
    """
    Option strategy specification class. Describes option strategy and its parameters for trading.
    
    OptionStrategy()
    """
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Option strategy name

Get: Name(self: OptionStrategy) -> str

Set: Name(self: OptionStrategy) = value
"""

    OptionLegs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Option strategy legs

Get: OptionLegs(self: OptionStrategy) -> List[OptionLegData]

Set: OptionLegs(self: OptionStrategy) = value
"""

    Underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Underlying symbol of the strategy

Get: Underlying(self: OptionStrategy) -> Symbol

Set: Underlying(self: OptionStrategy) = value
"""

    UnderlyingLegs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Option strategy underlying legs (usually 0 or 1 legs)

Get: UnderlyingLegs(self: OptionStrategy) -> List[UnderlyingLegData]

Set: UnderlyingLegs(self: OptionStrategy) = value
"""


    OptionLegData = None
    UnderlyingLegData = None


class OptionSymbol(object):
    """ Static class contains common utility methods specific to symbols representing the option contracts """
    @staticmethod
    def GetLastDayOfTrading(symbol):
        """
        GetLastDayOfTrading(symbol: Symbol) -> DateTime
        
            Returns the last trading date for the option 
             contract
        
        
            symbol: Option symbol
        """
        pass

    @staticmethod
    def IsOptionContractExpired(symbol, currentTimeUtc):
        """
        IsOptionContractExpired(symbol: Symbol, currentTimeUtc: DateTime) -> bool
        
            Returns true if the option contract is expired at 
             the specified time
        
        
            symbol: The option contract symbol
            currentTimeUtc: The current time (UTC)
            Returns: True if the option contract is expired at the 
             specified time, false otherwise
        """
        pass

    @staticmethod
    def IsStandard(symbol):
        """
        IsStandard(symbol: Symbol) -> bool
        
            Returns true if the option is a standard contract 
             that expires 3rd Friday of the month
        
        
            symbol: Option symbol
        """
        pass

    @staticmethod
    def IsStandardContract(symbol):
        """
        IsStandardContract(symbol: Symbol) -> bool
        
            Returns true if the option is a standard contract 
             that expires 3rd Friday of the month
        
        
            symbol: Option symbol
        """
        pass

    @staticmethod
    def IsWeekly(symbol):
        """
        IsWeekly(symbol: Symbol) -> bool
        
            Returns true if the option is a weekly contract 
             that expires on Friday , except 3rd Friday of the 
             month
        
        
            symbol: Option symbol
        """
        pass

    __all__ = [
        'GetLastDayOfTrading',
        'IsOptionContractExpired',
        'IsStandard',
        'IsStandardContract',
        'IsWeekly',
    ]


class OptionSymbolProperties(SymbolProperties):
    """
    Represents common properties for a specific option contract
    
    OptionSymbolProperties(description: str, quoteCurrency: str, contractMultiplier: Decimal, pipSize: Decimal, lotSize: Decimal)
    OptionSymbolProperties(properties: SymbolProperties)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, description: str, quoteCurrency: str, contractMultiplier: Decimal, pipSize: Decimal, lotSize: Decimal)
        __new__(cls: type, properties: SymbolProperties)
        """
        pass

    ContractUnitOfTrade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When the holder of an equity option exercises one contract, or when the writer of an equity option is assigned 
            an exercise notice on one contract, this unit of trade, usually 100 shares of the underlying security, changes hands.

Get: ContractUnitOfTrade(self: OptionSymbolProperties) -> int

"""



