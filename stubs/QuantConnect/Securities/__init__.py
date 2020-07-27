# encoding: utf-8
# module QuantConnect.Securities calls itself Securities
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AccountCurrencyImmediateSettlementModel(object, ISettlementModel):
    """
    Represents the model responsible for applying cash settlement rules
    
    AccountCurrencyImmediateSettlementModel()
    """
    def ApplyFunds(self, portfolio, security, applicationTimeUtc, currency, amount):
        """
        ApplyFunds(self: AccountCurrencyImmediateSettlementModel, portfolio: SecurityPortfolioManager, security: Security, applicationTimeUtc: DateTime, currency: str, amount: Decimal)
            Applies cash settlement rules
        
            portfolio: The algorithm's portfolio
            security: The fill's security
            applicationTimeUtc: The fill time (in UTC)
            currency: The currency symbol
            amount: The amount of cash to apply
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class AccountEvent(object):
    """
    Messaging class signifying a change in a user's account
    
    AccountEvent(currencySymbol: str, cashBalance: Decimal)
    """
    def ToString(self):
        """
        ToString(self: AccountEvent) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, currencySymbol, cashBalance):
        """ __new__(cls: type, currencySymbol: str, cashBalance: Decimal) """
        pass

    CashBalance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total cash balance of the account in units of QuantConnect.Securities.AccountEvent.CurrencySymbol

Get: CashBalance(self: AccountEvent) -> Decimal

"""

    CurrencySymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the currency symbol

Get: CurrencySymbol(self: AccountEvent) -> str

"""



class AdjustedPriceVariationModel(object, IPriceVariationModel):
    """
    Provides an implementation of QuantConnect.Securities.IPriceVariationModel
                for use when data is QuantConnect.DataNormalizationMode.Adjusted.
    
    AdjustedPriceVariationModel()
    """
    def GetMinimumPriceVariation(self, parameters):
        """
        GetMinimumPriceVariation(self: AdjustedPriceVariationModel, parameters: GetMinimumPriceVariationParameters) -> Decimal
        
            Get the minimum price variation from a security
        
            parameters: An object containing the method parameters
            Returns: Zero
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class BrokerageModelSecurityInitializer(object, ISecurityInitializer):
    """
    Provides an implementation of QuantConnect.Securities.ISecurityInitializer that initializes a security
                by settings the QuantConnect.Securities.Security.FillModel, QuantConnect.Securities.Security.FeeModel,
                QuantConnect.Securities.Security.SlippageModel, and the QuantConnect.Securities.Security.SettlementModel properties
    
    BrokerageModelSecurityInitializer()
    BrokerageModelSecurityInitializer(brokerageModel: IBrokerageModel, securitySeeder: ISecuritySeeder)
    """
    def Initialize(self, security):
        """
        Initialize(self: BrokerageModelSecurityInitializer, security: Security)
            Initializes the specified security by setting up 
             the models
        
        
            security: The security to be initialized
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, brokerageModel=None, securitySeeder=None):
        """
        __new__(cls: type)
        __new__(cls: type, brokerageModel: IBrokerageModel, securitySeeder: ISecuritySeeder)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class BuyingPower(object):
    """
    Defines the result for QuantConnect.Securities.IBuyingPowerModel.GetBuyingPower(QuantConnect.Securities.BuyingPowerParameters)
    
    BuyingPower(buyingPower: Decimal)
    """
    @staticmethod # known case of __new__
    def __new__(self, buyingPower):
        """ __new__(cls: type, buyingPower: Decimal) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the buying power

Get: Value(self: BuyingPower) -> Decimal

"""



class BuyingPowerModel(object, IBuyingPowerModel):
    """
    Provides a base class for all buying power models
    
    BuyingPowerModel()
    BuyingPowerModel(initialMarginRequirement: Decimal, maintenanceMarginRequirement: Decimal, requiredFreeBuyingPowerPercent: Decimal)
    BuyingPowerModel(leverage: Decimal, requiredFreeBuyingPowerPercent: Decimal)
    """
    def GetBuyingPower(self, parameters):
        """
        GetBuyingPower(self: BuyingPowerModel, parameters: BuyingPowerParameters) -> BuyingPower
        
            Gets the buying power available for a trade
        
            parameters: A parameters object containing the algorithm's 
             portfolio, security, and order direction
        
            Returns: The buying power available for the trade
        """
        pass

    def GetInitialMarginRequiredForOrder(self, *args): #cannot find CLR method
        """
        GetInitialMarginRequiredForOrder(self: BuyingPowerModel, parameters: InitialMarginRequiredForOrderParameters) -> Decimal
        
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
        GetInitialMarginRequirement(self: BuyingPowerModel, security: Security, quantity: Decimal) -> Decimal
        
            The margin that must be held in order to increase 
             the position by the provided quantity
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: BuyingPowerModel, security: Security) -> Decimal
        
            Gets the current leverage of the security
        
            security: The security to get leverage for
            Returns: The current leverage in the security
        """
        pass

    def GetMaintenanceMargin(self, *args): #cannot find CLR method
        """
        GetMaintenanceMargin(self: BuyingPowerModel, security: Security) -> Decimal
        
            Gets the margin currently allocated to the 
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

    def GetMaximumOrderQuantityForDeltaBuyingPower(self, parameters):
        """
        GetMaximumOrderQuantityForDeltaBuyingPower(self: BuyingPowerModel, parameters: GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> GetMaximumOrderQuantityResult
        
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
        GetMaximumOrderQuantityForTargetBuyingPower(self: BuyingPowerModel, parameters: GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> GetMaximumOrderQuantityResult
        
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
        GetReservedBuyingPowerForPosition(self: BuyingPowerModel, parameters: ReservedBuyingPowerForPositionParameters) -> ReservedBuyingPowerForPosition
        
            Gets the amount of buying power reserved to 
             maintain the specified position
        
        
            parameters: A parameters object containing the security
            Returns: The reserved buying power in account currency
        """
        pass

    def HasSufficientBuyingPowerForOrder(self, parameters):
        """
        HasSufficientBuyingPowerForOrder(self: BuyingPowerModel, parameters: HasSufficientBuyingPowerForOrderParameters) -> HasSufficientBuyingPowerForOrderResult
        
            Check if there is sufficient buying power to 
             execute this order.
        
        
            parameters: An object containing the portfolio, the security 
             and the order
        
            Returns: Returns buying power information for an order
        """
        pass

    def SetLeverage(self, security, leverage):
        """
        SetLeverage(self: BuyingPowerModel, security: Security, leverage: Decimal)
            Sets the leverage for the applicable securities, 
             i.e, equities
        
        
            leverage: The new leverage
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, initialMarginRequirement: Decimal, maintenanceMarginRequirement: Decimal, requiredFreeBuyingPowerPercent: Decimal)
        __new__(cls: type, leverage: Decimal, requiredFreeBuyingPowerPercent: Decimal)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    RequiredFreeBuyingPowerPercent = None


class BuyingPowerModelExtensions(object):
    """ Provides extension methods as backwards compatibility shims """
    @staticmethod
    def GetBuyingPower(model, portfolio, security, direction):
        """
        GetBuyingPower(model: IBuyingPowerModel, portfolio: SecurityPortfolioManager, security: Security, direction: OrderDirection) -> Decimal
        
            Gets the buying power available for a trade
        
            model: The QuantConnect.Securities.IBuyingPowerModel
            portfolio: The algorithm's portfolio
            security: The security to be traded
            direction: The direction of the trade
            Returns: The buying power available for the trade
        """
        pass

    @staticmethod
    def GetMaximumOrderQuantityForTargetBuyingPower(model, portfolio, security, target):
        """
        GetMaximumOrderQuantityForTargetBuyingPower(model: IBuyingPowerModel, portfolio: SecurityPortfolioManager, security: Security, target: Decimal) -> GetMaximumOrderQuantityResult
        
            Get the maximum market order quantity to obtain a 
             position with a given value in account currency
        
        
            model: The QuantConnect.Securities.IBuyingPowerModel
            portfolio: The algorithm's portfolio
            security: The security to be traded
            target: The target percent holdings
            Returns: Returns the maximum allowed market order quantity 
             and if zero, also the reason
        """
        pass

    @staticmethod
    def GetReservedBuyingPowerForPosition(model, security):
        """
        GetReservedBuyingPowerForPosition(model: IBuyingPowerModel, security: Security) -> Decimal
        
            Gets the amount of buying power reserved to 
             maintain the specified position
        
        
            model: The QuantConnect.Securities.IBuyingPowerModel
            security: The security
            Returns: The reserved buying power in account currency
        """
        pass

    @staticmethod
    def HasSufficientBuyingPowerForOrder(model, portfolio, security, order):
        """
        HasSufficientBuyingPowerForOrder(model: IBuyingPowerModel, portfolio: SecurityPortfolioManager, security: Security, order: Order) -> HasSufficientBuyingPowerForOrderResult
        
            Check if there is sufficient buying power to 
             execute this order.
        
        
            model: The QuantConnect.Securities.IBuyingPowerModel
            portfolio: The algorithm's portfolio
            security: The security to be traded
            order: The order
            Returns: Returns buying power information for an order
        """
        pass

    __all__ = [
        'GetBuyingPower',
        'GetMaximumOrderQuantityForTargetBuyingPower',
        'GetReservedBuyingPowerForPosition',
        'HasSufficientBuyingPowerForOrder',
    ]


class BuyingPowerParameters(object):
    """
    Defines the parameters for QuantConnect.Securities.IBuyingPowerModel.GetBuyingPower(QuantConnect.Securities.BuyingPowerParameters)
    
    BuyingPowerParameters(portfolio: SecurityPortfolioManager, security: Security, direction: OrderDirection)
    """
    def Result(self, buyingPower, currency):
        """
        Result(self: BuyingPowerParameters, buyingPower: Decimal, currency: str) -> BuyingPower
        
            Creates the result using the specified buying 
             power
        
        
            buyingPower: The buying power
            currency: The units the buying power is denominated in
            Returns: The buying power
        """
        pass

    def ResultInAccountCurrency(self, buyingPower):
        """
        ResultInAccountCurrency(self: BuyingPowerParameters, buyingPower: Decimal) -> BuyingPower
        
            Creates the result using the specified buying 
             power in units of the account currency
        
        
            buyingPower: The buying power
            Returns: The buying power
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, portfolio, security, direction):
        """ __new__(cls: type, portfolio: SecurityPortfolioManager, security: Security, direction: OrderDirection) """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the direction in which buying power is to be computed

Get: Direction(self: BuyingPowerParameters) -> OrderDirection

"""

    Portfolio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the algorithm's portfolio

Get: Portfolio(self: BuyingPowerParameters) -> SecurityPortfolioManager

"""

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security

Get: Security(self: BuyingPowerParameters) -> Security

"""



class Cash(object):
    """
    Represents a holding of a currency in cash.
    
    Cash(symbol: str, amount: Decimal, conversionRate: Decimal)
    """
    def AddAmount(self, amount):
        """
        AddAmount(self: Cash, amount: Decimal) -> Decimal
        
            Adds the specified amount of currency to this 
             Cash instance and returns the new total.
                
                 This operation is thread-safe
        
        
            amount: The amount of currency to be added
            Returns: The amount of currency directly after the addition
        """
        pass

    def EnsureCurrencyDataFeed(self, securities, subscriptions, marketMap, changes, securityService, accountCurrency, defaultResolution):
        """ EnsureCurrencyDataFeed(self: Cash, securities: SecurityManager, subscriptions: SubscriptionManager, marketMap: IReadOnlyDictionary[SecurityType, str], changes: SecurityChanges, securityService: ISecurityService, accountCurrency: str, defaultResolution: Resolution) -> SubscriptionDataConfig """
        pass

    def SetAmount(self, amount):
        """
        SetAmount(self: Cash, amount: Decimal)
            Sets the Quantity to the specified amount
        
            amount: The amount to set the quantity to
        """
        pass

    def ToString(self):
        """
        ToString(self: Cash) -> str
        
            Returns a System.String that represents the 
             current QuantConnect.Securities.Cash.
        
            Returns: A System.String that represents the current 
             QuantConnect.Securities.Cash.
        """
        pass

    def Update(self, data):
        """
        Update(self: Cash, data: BaseData)
            Updates this cash object with the specified data
        
            data: The new data for this cash object
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol, amount, conversionRate):
        """ __new__(cls: type, symbol: str, amount: Decimal, conversionRate: Decimal) """
        pass

    Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of cash held

Get: Amount(self: Cash) -> Decimal

"""

    ConversionRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the conversion rate into account currency

Get: ConversionRate(self: Cash) -> Decimal

"""

    ConversionRateSecurity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security used to apply conversion rates.
            If this cash represents the account currency, then null is returned.

Get: ConversionRateSecurity(self: Cash) -> Security

"""

    CurrencySymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The symbol of the currency, such as $

Get: CurrencySymbol(self: Cash) -> str

"""

    SecuritySymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the symbol of the security required to provide conversion rates.
            If this cash represents the account currency, then QuantConnect.Symbol.Empty
            is returned

Get: SecuritySymbol(self: Cash) -> Symbol

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the symbol used to represent this cash

Get: Symbol(self: Cash) -> str

"""

    ValueInAccountCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of this cash in the account currency

Get: ValueInAccountCurrency(self: Cash) -> Decimal

"""


    Updated = None


class CashAmount(object):
    """
    Represents a cash amount which can be converted to account currency using a currency converter
    
    CashAmount(amount: Decimal, currency: str)
    """
    def Equals(self, obj):
        """
        Equals(self: CashAmount, obj: object) -> bool
        
            Used to compare two 
             QuantConnect.Securities.CashAmount instances.
           
                      Useful to compare against the default 
             instance
        
        
            obj: The other object to compare with
            Returns: True if 
             QuantConnect.Securities.CashAmount.Currency and 
             QuantConnect.Securities.CashAmount.Amount are 
             equal
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, amount, currency):
        """
        __new__(cls: type, amount: Decimal, currency: str)
        __new__[CashAmount]() -> CashAmount
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of cash

Get: Amount(self: CashAmount) -> Decimal

"""

    Currency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The currency in which the cash amount is denominated

Get: Currency(self: CashAmount) -> str

"""



class ICurrencyConverter:
    """ Provides the ability to convert cash amounts to the account currency """
    def ConvertToAccountCurrency(self, cashAmount):
        """
        ConvertToAccountCurrency(self: ICurrencyConverter, cashAmount: CashAmount) -> CashAmount
        
            Converts a cash amount to the account currency
        
            cashAmount: The QuantConnect.Securities.CashAmount instance 
             to convert
        
            Returns: A new QuantConnect.Securities.CashAmount instance 
             denominated in the account currency
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AccountCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets account currency

Get: AccountCurrency(self: ICurrencyConverter) -> str

"""



class CashBook(object, IDictionary[str, Cash], ICollection[KeyValuePair[str, Cash]], IEnumerable[KeyValuePair[str, Cash]], IEnumerable, ICurrencyConverter):
    """
    Provides a means of keeping track of the different cash holdings of an algorithm
    
    CashBook()
    """
    def Add(self, *__args):
        """
        Add(self: CashBook, symbol: str, quantity: Decimal, conversionRate: Decimal)
            Adds a new cash of the specified symbol and 
             quantity
        
        
            symbol: The symbol used to reference the new cash
            quantity: The amount of new cash to start
            conversionRate: The conversion rate used to determine the initial
             
                    portfolio value/starting capital 
             impact caused by this currency position.
        
        Add(self: CashBook, item: KeyValuePair[str, Cash])Add(self: CashBook, symbol: str, value: Cash)
            Add the specified key and value.
        
            symbol: The symbol of the Cash value.
            value: Value.
        """
        pass

    def Clear(self):
        """
        Clear(self: CashBook)
            Clear this instance of all Cash entries.
        """
        pass

    def Contains(self, item):
        """ Contains(self: CashBook, item: KeyValuePair[str, Cash]) -> bool """
        pass

    def ContainsKey(self, symbol):
        """
        ContainsKey(self: CashBook, symbol: str) -> bool
        
            Determines whether the current instance contains 
             an entry with the specified symbol.
        
        
            symbol: Key.
            Returns: true, if key was contained, false otherwise.
        """
        pass

    def Convert(self, sourceQuantity, sourceCurrency, destinationCurrency):
        """
        Convert(self: CashBook, sourceQuantity: Decimal, sourceCurrency: str, destinationCurrency: str) -> Decimal
        
            Converts a quantity of source currency units into 
             the specified destination currency
        
        
            sourceQuantity: The quantity of source currency to be converted
            sourceCurrency: The source currency symbol
            destinationCurrency: The destination currency symbol
            Returns: The converted value
        """
        pass

    def ConvertToAccountCurrency(self, *__args):
        """
        ConvertToAccountCurrency(self: CashBook, sourceQuantity: Decimal, sourceCurrency: str) -> Decimal
        
            Converts a quantity of source currency units into 
             the account currency
        
        
            sourceQuantity: The quantity of source currency to be converted
            sourceCurrency: The source currency symbol
            Returns: The converted value
        ConvertToAccountCurrency(self: CashBook, cashAmount: CashAmount) -> CashAmount
        
            Converts a cash amount to the account currency
        
            cashAmount: The QuantConnect.Securities.CashAmount instance 
             to convert
        
            Returns: A new QuantConnect.Securities.CashAmount instance 
             denominated in the account currency
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: CashBook, array: Array[KeyValuePair[str, Cash]], arrayIndex: int) """
        pass

    def EnsureCurrencyDataFeeds(self, securities, subscriptions, marketMap, changes, securityService, defaultResolution):
        """ EnsureCurrencyDataFeeds(self: CashBook, securities: SecurityManager, subscriptions: SubscriptionManager, marketMap: IReadOnlyDictionary[SecurityType, str], changes: SecurityChanges, securityService: ISecurityService, defaultResolution: Resolution) -> List[SubscriptionDataConfig] """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: CashBook) -> IEnumerator[KeyValuePair[str, Cash]]
        
            Gets the enumerator.
            Returns: The enumerator.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: CashBook, symbol: str) -> bool
        
            Remove the Cash item corresponding to the 
             specified symbol
        
        
            symbol: The symbolto be removed
        Remove(self: CashBook, item: KeyValuePair[str, Cash]) -> bool
        """
        pass

    def ToString(self):
        """
        ToString(self: CashBook) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    def TryGetValue(self, symbol, value):
        """
        TryGetValue(self: CashBook, symbol: str) -> (bool, Cash)
        
            Try to get the value.
        
            symbol: The symbol.
            Returns: true, if get value was tryed, false otherwise.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary[str, Cash], key: str) -> bool """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AccountCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the base currency used

Get: AccountCurrency(self: CashBook) -> str

Set: AccountCurrency(self: CashBook) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count of Cash items in this CashBook.

Get: Count(self: CashBook) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: CashBook) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the keys.

Get: Keys(self: CashBook) -> ICollection[str]

"""

    TotalValueInAccountCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total value of the cash book in units of the base currency

Get: TotalValueInAccountCurrency(self: CashBook) -> Decimal

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the values.

Get: Values(self: CashBook) -> ICollection[Cash]

"""


    Updated = None
    UpdateType = None


class CashBuyingPowerModel(BuyingPowerModel, IBuyingPowerModel):
    """
    Represents a buying power model for cash accounts
    
    CashBuyingPowerModel()
    """
    def GetBuyingPower(self, parameters):
        """
        GetBuyingPower(self: CashBuyingPowerModel, parameters: BuyingPowerParameters) -> BuyingPower
        
            Gets the buying power available for a trade
        
            parameters: A parameters object containing the algorithm's 
             potrfolio, security, and order direction
        
            Returns: The buying power available for the trade
        """
        pass

    def GetInitialMarginRequiredForOrder(self, *args): #cannot find CLR method
        """
        GetInitialMarginRequiredForOrder(self: BuyingPowerModel, parameters: InitialMarginRequiredForOrderParameters) -> Decimal
        
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
        GetInitialMarginRequirement(self: BuyingPowerModel, security: Security, quantity: Decimal) -> Decimal
        
            The margin that must be held in order to increase 
             the position by the provided quantity
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: CashBuyingPowerModel, security: Security) -> Decimal
        
            Gets the current leverage of the security
        
            security: The security to get leverage for
            Returns: The current leverage in the security
        """
        pass

    def GetMaintenanceMargin(self, *args): #cannot find CLR method
        """
        GetMaintenanceMargin(self: BuyingPowerModel, security: Security) -> Decimal
        
            Gets the margin currently allocated to the 
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

    def GetMaximumOrderQuantityForDeltaBuyingPower(self, parameters):
        """
        GetMaximumOrderQuantityForDeltaBuyingPower(self: CashBuyingPowerModel, parameters: GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> GetMaximumOrderQuantityResult
        
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
        GetMaximumOrderQuantityForTargetBuyingPower(self: CashBuyingPowerModel, parameters: GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> GetMaximumOrderQuantityResult
        
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
        GetReservedBuyingPowerForPosition(self: CashBuyingPowerModel, parameters: ReservedBuyingPowerForPositionParameters) -> ReservedBuyingPowerForPosition
        
            Gets the amount of buying power reserved to 
             maintain the specified position
        
        
            parameters: A parameters object containing the security
            Returns: The reserved buying power in account currency
        """
        pass

    def HasSufficientBuyingPowerForOrder(self, parameters):
        """
        HasSufficientBuyingPowerForOrder(self: CashBuyingPowerModel, parameters: HasSufficientBuyingPowerForOrderParameters) -> HasSufficientBuyingPowerForOrderResult
        
            Check if there is sufficient buying power to 
             execute this order.
        
        
            parameters: An object containing the portfolio, the security 
             and the order
        
            Returns: Returns buying power information for an order
        """
        pass

    def SetLeverage(self, security, leverage):
        """
        SetLeverage(self: CashBuyingPowerModel, security: Security, leverage: Decimal)
            Sets the leverage for the applicable securities, 
             i.e, equities
        
        
            security: The security to set leverage for
            leverage: The new leverage
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    RequiredFreeBuyingPowerPercent = None


class CompositeSecurityInitializer(object, ISecurityInitializer):
    """
    Provides an implementation of QuantConnect.Securities.ISecurityInitializer that executes
                each initializer in order
    
    CompositeSecurityInitializer(*initializers: Array[ISecurityInitializer])
    """
    def Initialize(self, security):
        """
        Initialize(self: CompositeSecurityInitializer, security: Security)
            Execute each of the internally held initializers 
             in sequence
        
        
            security: The security to be initialized
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, initializers):
        """ __new__(cls: type, *initializers: Array[ISecurityInitializer]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class DefaultMarginCallModel(object, IMarginCallModel):
    """
    Represents the model responsible for picking which orders should be executed during a margin call
    
    DefaultMarginCallModel(portfolio: SecurityPortfolioManager, defaultOrderProperties: IOrderProperties)
    """
    def ExecuteMarginCall(self, generatedMarginCallOrders):
        """ ExecuteMarginCall(self: DefaultMarginCallModel, generatedMarginCallOrders: IEnumerable[SubmitOrderRequest]) -> List[OrderTicket] """
        pass

    def GenerateMarginCallOrder(self, *args): #cannot find CLR method
        """
        GenerateMarginCallOrder(self: DefaultMarginCallModel, security: Security, totalPortfolioValue: Decimal, totalUsedMargin: Decimal) -> SubmitOrderRequest
        
            Generates a new order for the specified security 
             taking into account the total margin
                    
             used by the account. Returns null when no margin 
             call is to be issued.
        
        
            security: The security to generate a margin call order for
            totalPortfolioValue: The net liquidation value for the entire account
            totalUsedMargin: The total margin used by the account in units of 
             base currency
        
            Returns: An order object representing a liquidation order 
             to be executed to bring the account within margin 
             requirements
        """
        pass

    def GetMarginCallOrders(self, issueMarginCallWarning):
        """
        GetMarginCallOrders(self: DefaultMarginCallModel) -> (List[SubmitOrderRequest], bool)
        
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
    def __new__(self, portfolio, defaultOrderProperties):
        """ __new__(cls: type, portfolio: SecurityPortfolioManager, defaultOrderProperties: IOrderProperties) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DefaultOrderProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default order properties to be used in margin call orders

"""

    Portfolio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the portfolio that margin calls will be transacted against

"""



class DelayedSettlementModel(object, ISettlementModel):
    """
    Represents the model responsible for applying cash settlement rules
    
    DelayedSettlementModel(numberOfDays: int, timeOfDay: TimeSpan)
    """
    def ApplyFunds(self, portfolio, security, applicationTimeUtc, currency, amount):
        """
        ApplyFunds(self: DelayedSettlementModel, portfolio: SecurityPortfolioManager, security: Security, applicationTimeUtc: DateTime, currency: str, amount: Decimal)
            Applies cash settlement rules
        
            portfolio: The algorithm's portfolio
            security: The fill's security
            applicationTimeUtc: The fill time (in UTC)
            currency: The currency symbol
            amount: The amount of cash to apply
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, numberOfDays, timeOfDay):
        """ __new__(cls: type, numberOfDays: int, timeOfDay: TimeSpan) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class DynamicSecurityData(object, IDynamicMetaObjectProvider):
    """
    Provides access to a security's data via it's type. This implementation supports dynamic access
                by type name.
    
    DynamicSecurityData(registeredTypes: IRegisteredSecurityDataTypesProvider, cache: SecurityCache)
    """
    def Get(self, type=None):
        """
        Get[T](self: DynamicSecurityData) -> T
        Get(self: DynamicSecurityData, type: Type) -> PyObject
        
            Get the matching cached object in a python 
             friendly accessor
        
        
            type: Type to search for
            Returns: Matching object
        """
        pass

    def GetAll(self, type=None):
        """
        GetAll[T](self: DynamicSecurityData) -> IReadOnlyList[T]
        GetAll(self: DynamicSecurityData, type: Type) -> IList
        
            Get all the matching types with a python friendly 
             overload.
        
        
            type: Search type
            Returns: List of matching objects cached
        """
        pass

    def GetMetaObject(self, parameter):
        """
        GetMetaObject(self: DynamicSecurityData, parameter: Expression) -> DynamicMetaObject
        
            Returns the System.Dynamic.DynamicMetaObject 
             responsible for binding operations performed on 
             this object.
        
        
            parameter: The expression tree representation of the runtime 
             value.
        
            Returns: The System.Dynamic.DynamicMetaObject to bind this 
             object.
        """
        pass

    def GetProperty(self, name):
        """
        GetProperty(self: DynamicSecurityData, name: str) -> object
        
            Gets the property's value with the specified 
             name. This is a case-insensitve search.
        
        
            name: The property name to access
            Returns: object value of BaseData
        """
        pass

    def HasData(self):
        """ HasData[T](self: DynamicSecurityData) -> bool """
        pass

    def HasProperty(self, name):
        """
        HasProperty(self: DynamicSecurityData, name: str) -> bool
        
            Gets whether or not this dynamic data instance 
             has a property with the specified name.
                 
                This is a case-insensitive search.
        
        
            name: The property name to check for
            Returns: True if the property exists, false otherwise
        """
        pass

    def SetProperty(self, name, value):
        """
        SetProperty(self: DynamicSecurityData, name: str, value: object) -> object
        
            Sets the property with the specified name to the 
             value. This is a case-insensitve search.
        
        
            name: The property name to set
            value: The new property value
            Returns: Returns the input value back to the caller
        """
        pass

    def __dir__(self, *args): #cannot find CLR method
        """ __dir__(self: IDynamicMetaObjectProvider) -> list """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, registeredTypes, cache):
        """ __new__(cls: type, registeredTypes: IRegisteredSecurityDataTypesProvider, cache: SecurityCache) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class SecurityPriceVariationModel(object, IPriceVariationModel):
    """
    Provides default implementation of QuantConnect.Securities.IPriceVariationModel
                for use in defining the minimum price variation.
    
    SecurityPriceVariationModel()
    """
    def GetMinimumPriceVariation(self, parameters):
        """
        GetMinimumPriceVariation(self: SecurityPriceVariationModel, parameters: GetMinimumPriceVariationParameters) -> Decimal
        
            Get the minimum price variation from a security
        
            parameters: An object containing the method parameters
            Returns: Decimal minimum price variation of a given 
             security
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class EquityPriceVariationModel(SecurityPriceVariationModel, IPriceVariationModel):
    """
    Provides an implementation of QuantConnect.Securities.IPriceVariationModel
                for use in defining the minimum price variation for a given equity
        
    EquityPriceVariationModel()
    """
    def GetMinimumPriceVariation(self, parameters):
        """
        GetMinimumPriceVariation(self: EquityPriceVariationModel, parameters: GetMinimumPriceVariationParameters) -> Decimal
        
            Get the minimum price variation from a security
        
            parameters: An object containing the method parameters
            Returns: Decimal minimum price variation of a given 
             security
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ErrorCurrencyConverter(object, ICurrencyConverter):
    """
    Provides an implementation of QuantConnect.Securities.ICurrencyConverter for use in
                tests that don't depend on this behavior.
    """
    def ConvertToAccountCurrency(self, cashAmount):
        """
        ConvertToAccountCurrency(self: ErrorCurrencyConverter, cashAmount: CashAmount) -> CashAmount
        
            Converts a cash amount to the account currency
        
            cashAmount: The QuantConnect.Securities.CashAmount instance 
             to convert
        
            Returns: A new QuantConnect.Securities.CashAmount instance 
             denominated in the account currency
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AccountCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets account currency

Get: AccountCurrency(self: ErrorCurrencyConverter) -> str

"""


    Instance = None


class FuncSecurityDerivativeFilter(object, IDerivativeSecurityFilter):
    """
    Provides a functional implementation of QuantConnect.Securities.IDerivativeSecurityFilter
    
    FuncSecurityDerivativeFilter(filter: Func[IDerivativeSecurityFilterUniverse, IDerivativeSecurityFilterUniverse])
    """
    def Filter(self, universe):
        """
        Filter(self: FuncSecurityDerivativeFilter, universe: IDerivativeSecurityFilterUniverse) -> IDerivativeSecurityFilterUniverse
        
            Filters the input set of symbols represented by 
             the universe
        
        
            universe: Derivative symbols universe used in filtering
            Returns: The filtered set of symbols
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, filter):
        """ __new__(cls: type, filter: Func[IDerivativeSecurityFilterUniverse, IDerivativeSecurityFilterUniverse]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class FuncSecurityInitializer(object, ISecurityInitializer):
    """
    Provides a functional implementation of QuantConnect.Securities.ISecurityInitializer
    
    FuncSecurityInitializer(initializer: Action[Security])
    """
    def Initialize(self, security):
        """
        Initialize(self: FuncSecurityInitializer, security: Security)
            Initializes the specified security
        
            security: The security to be initialized
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, initializer):
        """ __new__(cls: type, initializer: Action[Security]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class FuncSecuritySeeder(object, ISecuritySeeder):
    """
    Seed a security price from a history function
    
    FuncSecuritySeeder(seedFunction: Func[Security, BaseData])
    """
    def SeedSecurity(self, security):
        """
        SeedSecurity(self: FuncSecuritySeeder, security: Security) -> bool
        
            Seed the security
        
            security: QuantConnect.Securities.Security being seeded
            Returns: true if the security was seeded, false otherwise
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, seedFunction):
        """ __new__(cls: type, seedFunction: Func[Security, BaseData]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class FutureExpirationCycles(object):
    """ Static class contains definitions of popular futures expiration cycles """
    AllYear = None
    February = None
    FGHJKMNQUVXZ = None
    FHKNQUVZ = None
    FHKNQUX = None
    HKNUVZ = None
    HKNUZ = None
    HMUZ = None
    January = None
    March = None
    __all__ = [
        'AllYear',
        'February',
        'FGHJKMNQUVXZ',
        'FHKNQUVZ',
        'FHKNQUX',
        'HKNUVZ',
        'HKNUZ',
        'HMUZ',
        'January',
        'March',
    ]


class IDerivativeSecurityFilterUniverse(IEnumerable[Symbol], IEnumerable):
    """ Represents derivative symbols universe used in filtering. """
    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Symbol](enumerable: IEnumerable[Symbol], value: Symbol) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsDynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the universe is dynamic and filter needs to be reapplied during trading day

Get: IsDynamic(self: IDerivativeSecurityFilterUniverse) -> bool

"""

    Underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The underlying price data

Get: Underlying(self: IDerivativeSecurityFilterUniverse) -> BaseData

"""



class FutureFilterUniverse(object, IDerivativeSecurityFilterUniverse, IEnumerable[Symbol], IEnumerable):
    """
    Represents futures symbols universe used in filtering.
    
    FutureFilterUniverse(allSymbols: IEnumerable[Symbol], underlying: BaseData)
    """
    def BackMonth(self):
        """
        BackMonth(self: FutureFilterUniverse) -> FutureFilterUniverse
        
            Returns first of back month contracts
        """
        pass

    def BackMonths(self):
        """
        BackMonths(self: FutureFilterUniverse) -> FutureFilterUniverse
        
            Returns a list of back month contracts
        """
        pass

    def Contracts(self, *__args):
        """
        Contracts(self: FutureFilterUniverse, contracts: IEnumerable[Symbol]) -> FutureFilterUniverse
        Contracts(self: FutureFilterUniverse, contractSelector: Func[IEnumerable[Symbol], IEnumerable[Symbol]]) -> FutureFilterUniverse
        """
        pass

    def Expiration(self, *__args):
        """
        Expiration(self: FutureFilterUniverse, minExpiry: TimeSpan, maxExpiry: TimeSpan) -> FutureFilterUniverse
        
            Applies filter selecting futures contracts based 
             on a range of expiration dates relative to the 
             current day
        
        
            minExpiry: The minimum time until expiry to include, for 
             example, TimeSpan.FromDays(10)
                    would 
             exclude contracts expiring in more than 10 days
        
            maxExpiry: The maxmium time until expiry to include, for 
             example, TimeSpan.FromDays(10)
                    would 
             exclude contracts expiring in less than 10 days
        
        Expiration(self: FutureFilterUniverse, minExpiryDays: int, maxExpiryDays: int) -> FutureFilterUniverse
        
            Applies filter selecting futures contracts based 
             on a range of expiration dates relative to the 
             current day
        
        
            minExpiryDays: The minimum time, expressed in days, until expiry 
             to include, for example, 10
                    would 
             exclude contracts expiring in more than 10 days
        
            maxExpiryDays: The maximum time, expressed in days, until expiry 
             to include, for example, 10
                    would 
             exclude contracts expiring in less than 10 days
        """
        pass

    def ExpirationCycle(self, months):
        """
        ExpirationCycle(self: FutureFilterUniverse, months: Array[int]) -> FutureFilterUniverse
        
            Applies filter selecting futures contracts based 
             on expiration cycles. See 
             QuantConnect.Securities.FutureExpirationCycles 
             for details
        """
        pass

    def FrontMonth(self):
        """
        FrontMonth(self: FutureFilterUniverse) -> FutureFilterUniverse
        
            Returns front month contract
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: FutureFilterUniverse) -> IEnumerator[Symbol]
        
            IEnumerable interface method implementation
        """
        pass

    def OnlyApplyFilterAtMarketOpen(self):
        """
        OnlyApplyFilterAtMarketOpen(self: FutureFilterUniverse) -> FutureFilterUniverse
        
            Instructs the engine to only filter options 
             contracts on the first time step of each market 
             day.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Symbol](enumerable: IEnumerable[Symbol], value: Symbol) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, allSymbols, underlying):
        """ __new__(cls: type, allSymbols: IEnumerable[Symbol], underlying: BaseData) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsDynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the universe is dynamic and filter needs to be reapplied

Get: IsDynamic(self: FutureFilterUniverse) -> bool

"""

    Underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The underlying price data

Get: Underlying(self: FutureFilterUniverse) -> BaseData

"""



class FutureFilterUniverseEx(object):
    """ Extensions for Linq support """
    @staticmethod
    def Select(universe, mapFunc):
        """ Select(universe: FutureFilterUniverse, mapFunc: Func[Symbol, Symbol]) -> FutureFilterUniverse """
        pass

    @staticmethod
    def SelectMany(universe, mapFunc):
        """ SelectMany(universe: FutureFilterUniverse, mapFunc: Func[Symbol, IEnumerable[Symbol]]) -> FutureFilterUniverse """
        pass

    @staticmethod
    def Where(universe, predicate):
        """ Where(universe: FutureFilterUniverse, predicate: Func[Symbol, bool]) -> FutureFilterUniverse """
        pass

    __all__ = [
        'Select',
        'SelectMany',
        'Where',
    ]


class Futures(object):
    """ Futures static class contains shortcut definitions of major futures contracts available for trading """
    Currencies = None
    Dairy = None
    Energies = None
    Financials = None
    Forestry = None
    Grains = None
    Indices = None
    Meats = None
    Metals = None
    Softs = None
    __all__ = [
        'Currencies',
        'Dairy',
        'Energies',
        'Financials',
        'Forestry',
        'Grains',
        'Indices',
        'Meats',
        'Metals',
        'Softs',
    ]


class GetMaximumOrderQuantityForDeltaBuyingPowerParameters(object):
    """
    Defines the parameters for QuantConnect.Securities.IBuyingPowerModel.GetMaximumOrderQuantityForDeltaBuyingPower(QuantConnect.Securities.GetMaximumOrderQuantityForDeltaBuyingPowerParameters)
    
    GetMaximumOrderQuantityForDeltaBuyingPowerParameters(portfolio: SecurityPortfolioManager, security: Security, deltaBuyingPower: Decimal, silenceNonErrorReasons: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, portfolio, security, deltaBuyingPower, silenceNonErrorReasons):
        """ __new__(cls: type, portfolio: SecurityPortfolioManager, security: Security, deltaBuyingPower: Decimal, silenceNonErrorReasons: bool) """
        pass

    DeltaBuyingPower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The delta buying power.

Get: DeltaBuyingPower(self: GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> Decimal

"""

    Portfolio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the algorithm's portfolio

Get: Portfolio(self: GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> SecurityPortfolioManager

"""

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security

Get: Security(self: GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> Security

"""

    SilenceNonErrorReasons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True enables the QuantConnect.Securities.IBuyingPowerModel to skip setting QuantConnect.Securities.GetMaximumOrderQuantityResult.Reason
            for non error situations, for performance

Get: SilenceNonErrorReasons(self: GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> bool

"""



class GetMaximumOrderQuantityForTargetBuyingPowerParameters(object):
    """
    Defines the parameters for QuantConnect.Securities.IBuyingPowerModel.GetMaximumOrderQuantityForTargetBuyingPower(QuantConnect.Securities.GetMaximumOrderQuantityForTargetBuyingPowerParameters)
    
    GetMaximumOrderQuantityForTargetBuyingPowerParameters(portfolio: SecurityPortfolioManager, security: Security, targetBuyingPower: Decimal, silenceNonErrorReasons: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, portfolio, security, targetBuyingPower, silenceNonErrorReasons):
        """ __new__(cls: type, portfolio: SecurityPortfolioManager, security: Security, targetBuyingPower: Decimal, silenceNonErrorReasons: bool) """
        pass

    Portfolio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the algorithm's portfolio

Get: Portfolio(self: GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> SecurityPortfolioManager

"""

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security

Get: Security(self: GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> Security

"""

    SilenceNonErrorReasons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True enables the QuantConnect.Securities.IBuyingPowerModel to skip setting QuantConnect.Securities.GetMaximumOrderQuantityResult.Reason
            for non error situations, for performance

Get: SilenceNonErrorReasons(self: GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> bool

"""

    TargetBuyingPower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the target signed percentage buying power

Get: TargetBuyingPower(self: GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> Decimal

"""



class GetMaximumOrderQuantityResult(object):
    """
    Contains the information returned by QuantConnect.Securities.IBuyingPowerModel.GetMaximumOrderQuantityForTargetBuyingPower(QuantConnect.Securities.GetMaximumOrderQuantityForTargetBuyingPowerParameters)
                and  QuantConnect.Securities.IBuyingPowerModel.GetMaximumOrderQuantityForDeltaBuyingPower(QuantConnect.Securities.GetMaximumOrderQuantityForDeltaBuyingPowerParameters)
    
    GetMaximumOrderQuantityResult(quantity: Decimal, reason: str)
    GetMaximumOrderQuantityResult(quantity: Decimal, reason: str, isError: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, quantity, reason, isError=None):
        """
        __new__(cls: type, quantity: Decimal, reason: str)
        __new__(cls: type, quantity: Decimal, reason: str, isError: bool)
        """
        pass

    IsError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the zero order quantity is an error condition and will be shown to the user.

Get: IsError(self: GetMaximumOrderQuantityResult) -> bool

"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the maximum quantity for the order

Get: Quantity(self: GetMaximumOrderQuantityResult) -> Decimal

"""

    Reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the reason for which the maximum order quantity is zero

Get: Reason(self: GetMaximumOrderQuantityResult) -> str

"""



class GetMinimumPriceVariationParameters(object):
    """
    Defines the parameters for QuantConnect.Securities.IPriceVariationModel.GetMinimumPriceVariation(QuantConnect.Securities.GetMinimumPriceVariationParameters)
    
    GetMinimumPriceVariationParameters(security: Security, referencePrice: Decimal)
    """
    @staticmethod # known case of __new__
    def __new__(self, security, referencePrice):
        """ __new__(cls: type, security: Security, referencePrice: Decimal) """
        pass

    ReferencePrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the reference price to be used for the calculation

Get: ReferencePrice(self: GetMinimumPriceVariationParameters) -> Decimal

"""

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security

Get: Security(self: GetMinimumPriceVariationParameters) -> Security

"""



class HasSufficientBuyingPowerForOrderParameters(object):
    """
    Defines the parameters for QuantConnect.Securities.IBuyingPowerModel.HasSufficientBuyingPowerForOrder(QuantConnect.Securities.HasSufficientBuyingPowerForOrderParameters)
    
    HasSufficientBuyingPowerForOrderParameters(portfolio: SecurityPortfolioManager, security: Security, order: Order)
    """
    @staticmethod # known case of __new__
    def __new__(self, portfolio, security, order):
        """ __new__(cls: type, portfolio: SecurityPortfolioManager, security: Security, order: Order) """
        pass

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order

Get: Order(self: HasSufficientBuyingPowerForOrderParameters) -> Order

"""

    Portfolio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the algorithm's portfolio

Get: Portfolio(self: HasSufficientBuyingPowerForOrderParameters) -> SecurityPortfolioManager

"""

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security

Get: Security(self: HasSufficientBuyingPowerForOrderParameters) -> Security

"""



class HasSufficientBuyingPowerForOrderResult(object):
    """
    Contains the information returned by QuantConnect.Securities.IBuyingPowerModel.HasSufficientBuyingPowerForOrder(QuantConnect.Securities.HasSufficientBuyingPowerForOrderParameters)
    
    HasSufficientBuyingPowerForOrderResult(isSufficient: bool, reason: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, isSufficient, reason):
        """ __new__(cls: type, isSufficient: bool, reason: str) """
        pass

    IsSufficient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if there is sufficient buying power to execute an order

Get: IsSufficient(self: HasSufficientBuyingPowerForOrderResult) -> bool

"""

    Reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the reason for insufficient buying power to execute an order

Get: Reason(self: HasSufficientBuyingPowerForOrderResult) -> str

"""



class IBaseCurrencySymbol:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BaseCurrencySymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the currency acquired by going long this currency pair

Get: BaseCurrencySymbol(self: IBaseCurrencySymbol) -> str

"""



class IBuyingPowerModel:
    """ Represents a security's model of buying power """
    def GetBuyingPower(self, parameters):
        """
        GetBuyingPower(self: IBuyingPowerModel, parameters: BuyingPowerParameters) -> BuyingPower
        
            Gets the buying power available for a trade
        
            parameters: A parameters object containing the algorithm's 
             potrfolio, security, and order direction
        
            Returns: The buying power available for the trade
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: IBuyingPowerModel, security: Security) -> Decimal
        
            Gets the current leverage of the security
        
            security: The security to get leverage for
            Returns: The current leverage in the security
        """
        pass

    def GetMaximumOrderQuantityForDeltaBuyingPower(self, parameters):
        """
        GetMaximumOrderQuantityForDeltaBuyingPower(self: IBuyingPowerModel, parameters: GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> GetMaximumOrderQuantityResult
        
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
        GetMaximumOrderQuantityForTargetBuyingPower(self: IBuyingPowerModel, parameters: GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> GetMaximumOrderQuantityResult
        
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
        GetReservedBuyingPowerForPosition(self: IBuyingPowerModel, parameters: ReservedBuyingPowerForPositionParameters) -> ReservedBuyingPowerForPosition
        
            Gets the amount of buying power reserved to 
             maintain the specified position
        
        
            parameters: A parameters object containing the security
            Returns: The reserved buying power in account currency
        """
        pass

    def HasSufficientBuyingPowerForOrder(self, parameters):
        """
        HasSufficientBuyingPowerForOrder(self: IBuyingPowerModel, parameters: HasSufficientBuyingPowerForOrderParameters) -> HasSufficientBuyingPowerForOrderResult
        
            Check if there is sufficient buying power to 
             execute this order.
        
        
            parameters: An object containing the portfolio, the security 
             and the order
        
            Returns: Returns buying power information for an order
        """
        pass

    def SetLeverage(self, security, leverage):
        """
        SetLeverage(self: IBuyingPowerModel, security: Security, leverage: Decimal)
            Sets the leverage for the applicable securities, 
             i.e, equities
        
        
            security: The security to set leverage for
            leverage: The new leverage
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IdentityCurrencyConverter(object, ICurrencyConverter):
    """
    Provides an implementation of QuantConnect.Securities.ICurrencyConverter that does NOT perform conversions.
                This implementation will throw if the specified cashAmount is not in units of account currency.
    
    IdentityCurrencyConverter(accountCurrency: str)
    """
    def ConvertToAccountCurrency(self, cashAmount):
        """
        ConvertToAccountCurrency(self: IdentityCurrencyConverter, cashAmount: CashAmount) -> CashAmount
        
            Converts a cash amount to the account currency.
         
                        This implementation can only handle 
             cash amounts in units of the account currency.
        
        
            cashAmount: The QuantConnect.Securities.CashAmount instance 
             to convert
        
            Returns: A new QuantConnect.Securities.CashAmount instance 
             denominated in the account currency
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, accountCurrency):
        """ __new__(cls: type, accountCurrency: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AccountCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets account currency

Get: AccountCurrency(self: IdentityCurrencyConverter) -> str

"""



class IDerivativeSecurity:
    """ Defines a security as a derivative of another security """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the underlying security for the derivative

Get: Underlying(self: IDerivativeSecurity) -> Security

Set: Underlying(self: IDerivativeSecurity) = value
"""



class IDerivativeSecurityFilter:
    """ Filters a set of derivative symbols using the underlying price data. """
    def Filter(self, universe):
        """
        Filter(self: IDerivativeSecurityFilter, universe: IDerivativeSecurityFilterUniverse) -> IDerivativeSecurityFilterUniverse
        
            Filters the input set of symbols represented by 
             the universe
        
        
            universe: derivative symbols universe used in filtering
            Returns: The filtered set of symbols
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IMarginCallModel:
    """ Represents the model responsible for picking which orders should be executed during a margin call """
    def ExecuteMarginCall(self, generatedMarginCallOrders):
        """ ExecuteMarginCall(self: IMarginCallModel, generatedMarginCallOrders: IEnumerable[SubmitOrderRequest]) -> List[OrderTicket] """
        pass

    def GetMarginCallOrders(self, issueMarginCallWarning):
        """
        GetMarginCallOrders(self: IMarginCallModel) -> (List[SubmitOrderRequest], bool)
        
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
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ImmediateSettlementModel(object, ISettlementModel):
    """
    Represents the model responsible for applying cash settlement rules
    
    ImmediateSettlementModel()
    """
    def ApplyFunds(self, portfolio, security, applicationTimeUtc, currency, amount):
        """
        ApplyFunds(self: ImmediateSettlementModel, portfolio: SecurityPortfolioManager, security: Security, applicationTimeUtc: DateTime, currency: str, amount: Decimal)
            Applies cash settlement rules
        
            portfolio: The algorithm's portfolio
            security: The fill's security
            applicationTimeUtc: The fill time (in UTC)
            currency: The currency symbol
            amount: The amount of cash to apply
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class IndicatorVolatilityModel(object, IVolatilityModel):
    """
    IndicatorVolatilityModel[T](indicator: IIndicator[T])
    IndicatorVolatilityModel[T](indicator: IIndicator[T], indicatorUpdate: Action[Security, BaseData, IIndicator[T]])
    """
    def GetHistoryRequirements(self, security, utcTime):
        """
        GetHistoryRequirements(self: IndicatorVolatilityModel[T], security: Security, utcTime: DateTime) -> IEnumerable[HistoryRequest]
        
            Returns history requirements for the volatility 
             model expressed in the form of history request
        
        
            security: The security of the request
            utcTime: The date/time of the request
            Returns: History request object list, or empty if no 
             requirements
        """
        pass

    def Update(self, security, data):
        """
        Update(self: IndicatorVolatilityModel[T], security: Security, data: BaseData)
            Updates this model using the new price 
             information in
                    the specified 
             security instance
        
        
            security: The security to calculate volatility for
            data: The new piece of data for the security
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, indicator, indicatorUpdate=None):
        """
        __new__(cls: type, indicator: IIndicator[T])
        __new__(cls: type, indicator: IIndicator[T], indicatorUpdate: Action[Security, BaseData, IIndicator[T]])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Volatility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the volatility of the security as a percentage

Get: Volatility(self: IndicatorVolatilityModel[T]) -> Decimal

"""



class InitialMarginRequiredForOrderParameters(object):
    """
    Defines the parameters for QuantConnect.Securities.BuyingPowerModel.GetInitialMarginRequiredForOrder(QuantConnect.Securities.InitialMarginRequiredForOrderParameters)
    
    InitialMarginRequiredForOrderParameters(currencyConverter: ICurrencyConverter, security: Security, order: Order)
    """
    @staticmethod # known case of __new__
    def __new__(self, currencyConverter, security, order):
        """ __new__(cls: type, currencyConverter: ICurrencyConverter, security: Security, order: Order) """
        pass

    CurrencyConverter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the currency converter

Get: CurrencyConverter(self: InitialMarginRequiredForOrderParameters) -> ICurrencyConverter

"""

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order

Get: Order(self: InitialMarginRequiredForOrderParameters) -> Order

"""

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security

Get: Security(self: InitialMarginRequiredForOrderParameters) -> Security

"""



class IOrderEventProvider:
    """ Represents a type with a new QuantConnect.Orders.OrderEvent event System.EventHandler. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    NewOrderEvent = None


class IOrderProvider:
    """ Represents a type capable of fetching Order instances by its QC order id or by a brokerage id """
    def GetOpenOrders(self, filter):
        """ GetOpenOrders(self: IOrderProvider, filter: Func[Order, bool]) -> List[Order] """
        pass

    def GetOpenOrderTickets(self, filter):
        """ GetOpenOrderTickets(self: IOrderProvider, filter: Func[OrderTicket, bool]) -> IEnumerable[OrderTicket] """
        pass

    def GetOrderByBrokerageId(self, brokerageId):
        """
        GetOrderByBrokerageId(self: IOrderProvider, brokerageId: str) -> Order
        
            Gets the order by its brokerage id
        
            brokerageId: The brokerage id to fetch
            Returns: The first order matching the brokerage id, or 
             null if no match is found
        """
        pass

    def GetOrderById(self, orderId):
        """
        GetOrderById(self: IOrderProvider, orderId: int) -> Order
        
            Get the order by its id
        
            orderId: Order id to fetch
            Returns: A clone of the order with the specified id, or 
             null if no match is found
        """
        pass

    def GetOrders(self, filter):
        """ GetOrders(self: IOrderProvider, filter: Func[Order, bool]) -> IEnumerable[Order] """
        pass

    def GetOrderTicket(self, orderId):
        """
        GetOrderTicket(self: IOrderProvider, orderId: int) -> OrderTicket
        
            Gets the order ticket for the specified order id. 
             Returns null if not found
        
        
            orderId: The order's id
            Returns: The order ticket with the specified id, or null 
             if not found
        """
        pass

    def GetOrderTickets(self, filter):
        """ GetOrderTickets(self: IOrderProvider, filter: Func[OrderTicket, bool]) -> IEnumerable[OrderTicket] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    OrdersCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current number of orders that have been processed

Get: OrdersCount(self: IOrderProvider) -> int

"""



class IOrderProcessor(IOrderProvider):
    """ Represents a type capable of processing orders """
    def Process(self, request):
        """
        Process(self: IOrderProcessor, request: OrderRequest) -> OrderTicket
        
            Adds the specified order to be processed
        
            request: The QuantConnect.Orders.OrderRequest to be 
             processed
        
            Returns: The QuantConnect.Orders.OrderTicket for the 
             corresponding 
             QuantConnect.Orders.OrderRequest.OrderId
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IPriceVariationModel:
    """ Gets the minimum price variation of a given security """
    def GetMinimumPriceVariation(self, parameters):
        """
        GetMinimumPriceVariation(self: IPriceVariationModel, parameters: GetMinimumPriceVariationParameters) -> Decimal
        
            Get the minimum price variation from a security
        
            parameters: An object containing the method parameters
            Returns: Decimal minimum price variation of a given 
             security
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IRegisteredSecurityDataTypesProvider:
    """ Provides the set of base data types registered in the algorithm """
    def RegisterType(self, type):
        """
        RegisterType(self: IRegisteredSecurityDataTypesProvider, type: Type) -> bool
        
            Registers the specified type w/ the provider
            Returns: True if the type was previously not registered
        """
        pass

    def TryGetType(self, name, type):
        """
        TryGetType(self: IRegisteredSecurityDataTypesProvider, name: str) -> (bool, Type)
        
            Determines if the specified type is registered or 
             not and returns it
        
            Returns: True if the type was previously registered
        """
        pass

    def UnregisterType(self, type):
        """
        UnregisterType(self: IRegisteredSecurityDataTypesProvider, type: Type) -> bool
        
            Removes the registration for the specified type
            Returns: True if the type was previously registered
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISecurityInitializer:
    """ Represents a type capable of initializing a new security """
    def Initialize(self, security):
        """
        Initialize(self: ISecurityInitializer, security: Security)
            Initializes the specified security
        
            security: The security to be initialized
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISecurityPortfolioModel:
    """ Performs order fill application to portfolio """
    def ProcessFill(self, portfolio, security, fill):
        """
        ProcessFill(self: ISecurityPortfolioModel, portfolio: SecurityPortfolioManager, security: Security, fill: OrderEvent)
            Performs application of an OrderEvent to the 
             portfolio
        
        
            portfolio: The algorithm's portfolio
            security: The fill's security
            fill: The order event fill object to be applied
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISecurityProvider:
    """ Represents a type capable of fetching the holdings for the specified symbol """
    def GetSecurity(self, symbol):
        """
        GetSecurity(self: ISecurityProvider, symbol: Symbol) -> Security
        
            Retrieves a summary of the holdings for the 
             specified symbol
        
        
            symbol: The symbol to get holdings for
            Returns: The holdings for the symbol or null if the symbol 
             is invalid and/or not in the portfolio
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISecuritySeeder:
    """ Used to seed the security with the correct price """
    def SeedSecurity(self, security):
        """
        SeedSecurity(self: ISecuritySeeder, security: Security) -> bool
        
            Seed the security
        
            security: QuantConnect.Securities.Security being seeded
            Returns: true if the security was seeded, false otherwise
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISettlementModel:
    """ Represents the model responsible for applying cash settlement rules """
    def ApplyFunds(self, portfolio, security, applicationTimeUtc, currency, amount):
        """
        ApplyFunds(self: ISettlementModel, portfolio: SecurityPortfolioManager, security: Security, applicationTimeUtc: DateTime, currency: str, amount: Decimal)
            Applies cash settlement rules
        
            portfolio: The algorithm's portfolio
            security: The fill's security
            applicationTimeUtc: The fill time (in UTC)
            currency: The currency symbol
            amount: The amount of cash to apply
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IVolatilityModel:
    """ Represents a model that computes the volatility of a security """
    def GetHistoryRequirements(self, security, utcTime):
        """
        GetHistoryRequirements(self: IVolatilityModel, security: Security, utcTime: DateTime) -> IEnumerable[HistoryRequest]
        
            Returns history requirements for the volatility 
             model expressed in the form of history request
        
        
            security: The security of the request
            utcTime: The date/time of the request
            Returns: History request object list, or empty if no 
             requirements
        """
        pass

    def Update(self, security, data):
        """
        Update(self: IVolatilityModel, security: Security, data: BaseData)
            Updates this model using the new price 
             information in
                    the specified 
             security instance
        
        
            security: The security to calculate volatility for
            data: The new data used to update the model
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Volatility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the volatility of the security as a percentage

Get: Volatility(self: IVolatilityModel) -> Decimal

"""



class LocalMarketHours(object):
    """
    Represents the market hours under normal conditions for an exchange and a specific day of the week in terms of local time
    
    LocalMarketHours(day: DayOfWeek, *segments: Array[MarketHoursSegment])
    LocalMarketHours(day: DayOfWeek, segments: IEnumerable[MarketHoursSegment])
    LocalMarketHours(day: DayOfWeek, extendedMarketOpen: TimeSpan, marketOpen: TimeSpan, marketClose: TimeSpan, extendedMarketClose: TimeSpan)
    LocalMarketHours(day: DayOfWeek, marketOpen: TimeSpan, marketClose: TimeSpan)
    """
    @staticmethod
    def ClosedAllDay(dayOfWeek):
        """
        ClosedAllDay(dayOfWeek: DayOfWeek) -> LocalMarketHours
        
            Gets a QuantConnect.Securities.LocalMarketHours 
             instance that is always closed
        
        
            dayOfWeek: The day of week
            Returns: A QuantConnect.Securities.LocalMarketHours 
             instance that is always closed
        """
        pass

    def GetMarketClose(self, time, extendedMarket):
        """
        GetMarketClose(self: LocalMarketHours, time: TimeSpan, extendedMarket: bool) -> Nullable[TimeSpan]
        
            Gets the market closing time of day
        
            time: The reference time, the close returned will be 
             the first close after the specified time if there 
             are multiple market open segments
        
            extendedMarket: True to include extended market hours, false for 
             regular market hours
        
            Returns: The market's closing time of day
        """
        pass

    def GetMarketOpen(self, time, extendedMarket):
        """
        GetMarketOpen(self: LocalMarketHours, time: TimeSpan, extendedMarket: bool) -> Nullable[TimeSpan]
        
            Gets the market opening time of day
        
            time: The reference time, the open returned will be the 
             first open after the specified time if there are 
             multiple market open segments
        
            extendedMarket: True to include extended market hours, false for 
             regular market hours
        
            Returns: The market's opening time of day
        """
        pass

    def IsOpen(self, *__args):
        """
        IsOpen(self: LocalMarketHours, time: TimeSpan, extendedMarket: bool) -> bool
        
            Determines if the exchange is open at the 
             specified time
        
        
            time: The time of day to check
            extendedMarket: True to check exended market hours, false to 
             check regular market hours
        
            Returns: True if the exchange is considered open, false 
             otherwise
        
        IsOpen(self: LocalMarketHours, start: TimeSpan, end: TimeSpan, extendedMarket: bool) -> bool
        
            Determines if the exchange is open during the 
             specified interval
        
        
            start: The start time of the interval
            end: The end time of the interval
            extendedMarket: True to check exended market hours, false to 
             check regular market hours
        
            Returns: True if the exchange is considered open, false 
             otherwise
        """
        pass

    @staticmethod
    def OpenAllDay(dayOfWeek):
        """
        OpenAllDay(dayOfWeek: DayOfWeek) -> LocalMarketHours
        
            Gets a QuantConnect.Securities.LocalMarketHours 
             instance that is always open
        
        
            dayOfWeek: The day of week
            Returns: A QuantConnect.Securities.LocalMarketHours 
             instance that is always open
        """
        pass

    def ToString(self):
        """
        ToString(self: LocalMarketHours) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, day, *__args):
        """
        __new__(cls: type, day: DayOfWeek, *segments: Array[MarketHoursSegment])
        __new__(cls: type, day: DayOfWeek, segments: IEnumerable[MarketHoursSegment])
        __new__(cls: type, day: DayOfWeek, extendedMarketOpen: TimeSpan, marketOpen: TimeSpan, marketClose: TimeSpan, extendedMarketClose: TimeSpan)
        __new__(cls: type, day: DayOfWeek, marketOpen: TimeSpan, marketClose: TimeSpan)
        """
        pass

    DayOfWeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the day of week these hours apply to

Get: DayOfWeek(self: LocalMarketHours) -> DayOfWeek

"""

    IsClosedAllDay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether or not this exchange is closed all day

Get: IsClosedAllDay(self: LocalMarketHours) -> bool

"""

    IsOpenAllDay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether or not this exchange is closed all day

Get: IsOpenAllDay(self: LocalMarketHours) -> bool

"""

    MarketDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the tradable time during the market day.
            For a normal US equity trading day this is 6.5 hours.
            This does NOT account for extended market hours and only
            considers QuantConnect.Securities.MarketHoursState.Market

Get: MarketDuration(self: LocalMarketHours) -> TimeSpan

"""

    Segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the individual market hours segments that define the hours of operation for this day

Get: Segments(self: LocalMarketHours) -> IEnumerable[MarketHoursSegment]

"""



class MarginCallModel(object):
    """ Provides access to a null implementation for QuantConnect.Securities.IMarginCallModel """
    Null = None
    __all__ = [
        'Null',
    ]


class MarketHoursDatabase(object):
    """
    Provides access to exchange hours and raw data times zones in various markets
    
    MarketHoursDatabase(exchangeHours: IReadOnlyDictionary[SecurityDatabaseKey, Entry])
    """
    def ContainsKey(self, *args): #cannot find CLR method
        """
        ContainsKey(self: MarketHoursDatabase, key: SecurityDatabaseKey) -> bool
        
            Determines if the database contains the specified 
             key
        
        
            key: The key to search for
            Returns: True if an entry is found, otherwise false
        """
        pass

    @staticmethod
    def FromDataFolder(dataFolder=None):
        """
        FromDataFolder() -> MarketHoursDatabase
        
            Gets the instance of the 
             QuantConnect.Securities.MarketHoursDatabase class 
             produced by reading in the market hours
                 
                data found in /Data/market-hours/
        
            Returns: A QuantConnect.Securities.MarketHoursDatabase 
             class that represents the data in the 
             market-hours folder
        
        FromDataFolder(dataFolder: str) -> MarketHoursDatabase
        
            Gets the instance of the 
             QuantConnect.Securities.MarketHoursDatabase class 
             produced by reading in the market hours
                 
                data found in /Data/market-hours/
        
        
            dataFolder: Path to the data folder
            Returns: A QuantConnect.Securities.MarketHoursDatabase 
             class that represents the data in the 
             market-hours folder
        """
        pass

    @staticmethod
    def FromFile(path):
        """
        FromFile(path: str) -> MarketHoursDatabase
        
            Reads the specified file as a market hours 
             database instance
        
        
            path: The market hours database file path
            Returns: A new instance of the 
             QuantConnect.Securities.MarketHoursDatabase class
        """
        pass

    @staticmethod
    def GetDatabaseSymbolKey(symbol):
        """
        GetDatabaseSymbolKey(symbol: Symbol) -> str
        
            Gets the correct string symbol to use as a 
             database key
        
        
            symbol: The symbol
            Returns: The symbol string used in the database ke
        """
        pass

    def GetDataTimeZone(self, market, symbol, securityType):
        """
        GetDataTimeZone(self: MarketHoursDatabase, market: str, symbol: Symbol, securityType: SecurityType) -> DateTimeZone
        
            Performs a lookup using the specified information 
             and returns the data's time zone if found,
              
                   if an entry is not found, an exception is 
             thrown
        
        
            market: The market the exchange resides in, i.e, 'usa', 
             'fxcm', ect...
        
            symbol: The particular symbol being traded
            securityType: The security type of the symbol
            Returns: The raw data time zone for the specified security
        """
        pass

    def GetEntry(self, market, symbol, securityType):
        """
        GetEntry(self: MarketHoursDatabase, market: str, symbol: str, securityType: SecurityType) -> Entry
        
            Gets the entry for the specified 
             market/symbol/security-type
        
        
            market: The market the exchange resides in, i.e, 'usa', 
             'fxcm', ect...
        
            symbol: The particular symbol being traded
            securityType: The security type of the symbol
            Returns: The entry matching the specified 
             market/symbol/security-type
        
        GetEntry(self: MarketHoursDatabase, market: str, symbol: Symbol, securityType: SecurityType) -> Entry
        
            Gets the entry for the specified 
             market/symbol/security-type
        
        
            market: The market the exchange resides in, i.e, 'usa', 
             'fxcm', ect...
        
            symbol: The particular symbol being traded (Symbol class)
            securityType: The security type of the symbol
            Returns: The entry matching the specified 
             market/symbol/security-type
        """
        pass

    def GetExchangeHours(self, *__args):
        """
        GetExchangeHours(self: MarketHoursDatabase, configuration: SubscriptionDataConfig) -> SecurityExchangeHours
        
            Convenience method for retrieving exchange hours 
             from market hours database using a subscription 
             config
        
        
            configuration: The subscription data config to get exchange 
             hours for
        
            Returns: The configure exchange hours for the specified 
             configuration
        
        GetExchangeHours(self: MarketHoursDatabase, market: str, symbol: Symbol, securityType: SecurityType) -> SecurityExchangeHours
        
            Convenience method for retrieving exchange hours 
             from market hours database using a subscription 
             config
        
        
            market: The market the exchange resides in, i.e, 'usa', 
             'fxcm', ect...
        
            symbol: The particular symbol being traded
            securityType: The security type of the symbol
            Returns: The exchange hours for the specified security
        """
        pass

    @staticmethod
    def Reset():
        """
        Reset()
            Resets the market hours database, forcing a 
             reload when reused.
                    Called in tests 
             where multiple algorithms are run sequentially,
         
                        and we need to guarantee that every 
             test starts with the same environment.
        """
        pass

    def SetEntry(self, market, symbol, securityType, exchangeHours, dataTimeZone):
        """
        SetEntry(self: MarketHoursDatabase, market: str, symbol: str, securityType: SecurityType, exchangeHours: SecurityExchangeHours, dataTimeZone: DateTimeZone) -> Entry
        
            Sets the entry for the specified 
             market/symbol/security-type.
                    This is 
             intended to be used by custom data and other data 
             sources that don't have explicit
                    
             entries in market-hours-database.csv. At run 
             time, the algorithm can update the market hours
         
                        database via calls to AddData.
        
        
            market: The market the exchange resides in, i.e, 'usa', 
             'fxcm', ect...
        
            symbol: The particular symbol being traded
            securityType: The security type of the symbol
            exchangeHours: The exchange hours for the specified symbol
            dataTimeZone: The time zone of the symbol's raw data. Optional, 
             defaults to the exchange time zone
        
            Returns: The entry matching the specified 
             market/symbol/security-type
        """
        pass

    def SetEntryAlwaysOpen(self, market, symbol, securityType, timeZone):
        """
        SetEntryAlwaysOpen(self: MarketHoursDatabase, market: str, symbol: str, securityType: SecurityType, timeZone: DateTimeZone) -> Entry
        
            Convenience method for the common custom data 
             case.
                    Sets the entry for the 
             specified symbol using 
             SecurityExchangeHours.AlwaysOpen(timeZone)
              
                   This sets the data time zone equal to the 
             exchange time zone as well.
        
        
            market: The market the exchange resides in, i.e, 'usa', 
             'fxcm', ect...
        
            symbol: The particular symbol being traded
            securityType: The security type of the symbol
            timeZone: The time zone of the symbol's exchange and raw 
             data
        
            Returns: The entry matching the specified 
             market/symbol/security-type
        """
        pass

    def TryGetEntry(self, market, symbol, securityType, entry):
        """
        TryGetEntry(self: MarketHoursDatabase, market: str, symbol: Symbol, securityType: SecurityType) -> (bool, Entry)
        TryGetEntry(self: MarketHoursDatabase, market: str, symbol: str, securityType: SecurityType) -> (bool, Entry)
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, exchangeHours):
        """ __new__(cls: type, exchangeHours: IReadOnlyDictionary[SecurityDatabaseKey, Entry]) """
        pass

    ExchangeHoursListing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all the exchange hours held by this provider

Get: ExchangeHoursListing(self: MarketHoursDatabase) -> List[KeyValuePair[SecurityDatabaseKey, Entry]]

"""


    Entry = None


class MarketHoursSegment(object):
    """
    Represents the state of an exchange during a specified time range
    
    MarketHoursSegment(state: MarketHoursState, start: TimeSpan, end: TimeSpan)
    """
    @staticmethod
    def ClosedAllDay():
        """
        ClosedAllDay() -> MarketHoursSegment
        
            Gets a new market hours segment representing 
             being open all day
        """
        pass

    def Contains(self, time):
        """
        Contains(self: MarketHoursSegment, time: TimeSpan) -> bool
        
            Determines whether or not the specified time is 
             contained within this segment
        
        
            time: The time to check
            Returns: True if this segment contains the specified time, 
             false otherwise
        """
        pass

    @staticmethod
    def GetMarketHoursSegments(extendedMarketOpen, marketOpen, marketClose, extendedMarketClose):
        """
        GetMarketHoursSegments(extendedMarketOpen: TimeSpan, marketOpen: TimeSpan, marketClose: TimeSpan, extendedMarketClose: TimeSpan) -> Array[MarketHoursSegment]
        
            Creates the market hours segments for the 
             specified market open/close times
        
        
            extendedMarketOpen: The extended market open time. If no pre market, 
             set to market open
        
            marketOpen: The regular market open time
            marketClose: The regular market close time
            extendedMarketClose: The extended market close time. If no post 
             market, set to market close
        
            Returns: An array of 
             QuantConnect.Securities.MarketHoursSegment 
             representing the specified market open/close 
             times
        """
        pass

    @staticmethod
    def OpenAllDay():
        """
        OpenAllDay() -> MarketHoursSegment
        
            Gets a new market hours segment representing 
             being open all day
        """
        pass

    def Overlaps(self, start, end):
        """
        Overlaps(self: MarketHoursSegment, start: TimeSpan, end: TimeSpan) -> bool
        
            Determines whether or not the specified time 
             range overlaps with this segment
        
        
            start: The start of the range
            end: The end of the range
            Returns: True if the specified range overlaps this time 
             segment, false otherwise
        """
        pass

    def ToString(self):
        """
        ToString(self: MarketHoursSegment) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, state, start, end):
        """ __new__(cls: type, state: MarketHoursState, start: TimeSpan, end: TimeSpan) """
        pass

    End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the end time for this segment

Get: End(self: MarketHoursSegment) -> TimeSpan

"""

    Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the start time for this segment

Get: Start(self: MarketHoursSegment) -> TimeSpan

"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the market hours state for this segment

Get: State(self: MarketHoursSegment) -> MarketHoursState

"""



class MarketHoursState(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the open/close state for a QuantConnect.Securities.MarketHoursSegment
    
    enum MarketHoursState, values: Closed (0), Market (2), PostMarket (3), PreMarket (1)
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

    Closed = None
    Market = None
    PostMarket = None
    PreMarket = None
    value__ = None


class OptionFilterUniverse(object, IDerivativeSecurityFilterUniverse, IEnumerable[Symbol], IEnumerable):
    """
    Represents options symbols universe used in filtering.
    
    OptionFilterUniverse()
    OptionFilterUniverse(allSymbols: IEnumerable[Symbol], underlying: BaseData)
    """
    def BackMonth(self):
        """
        BackMonth(self: OptionFilterUniverse) -> OptionFilterUniverse
        
            Returns first of back month contracts
        """
        pass

    def BackMonths(self):
        """
        BackMonths(self: OptionFilterUniverse) -> OptionFilterUniverse
        
            Returns a list of back month contracts
        """
        pass

    def CallsOnly(self):
        """
        CallsOnly(self: OptionFilterUniverse) -> OptionFilterUniverse
        
            Sets universe of call options (if any) as a 
             selection
        """
        pass

    def Contracts(self, *__args):
        """
        Contracts(self: OptionFilterUniverse, contracts: IEnumerable[Symbol]) -> OptionFilterUniverse
        Contracts(self: OptionFilterUniverse, contractSelector: Func[IEnumerable[Symbol], IEnumerable[Symbol]]) -> OptionFilterUniverse
        """
        pass

    def Expiration(self, *__args):
        """
        Expiration(self: OptionFilterUniverse, minExpiry: TimeSpan, maxExpiry: TimeSpan) -> OptionFilterUniverse
        
            Applies filter selecting options contracts based 
             on a range of expiration dates relative to the 
             current day
        
        
            minExpiry: The minimum time until expiry to include, for 
             example, TimeSpan.FromDays(10)
                    would 
             exclude contracts expiring in more than 10 days
        
            maxExpiry: The maxmium time until expiry to include, for 
             example, TimeSpan.FromDays(10)
                    would 
             exclude contracts expiring in less than 10 days
        
        Expiration(self: OptionFilterUniverse, minExpiryDays: int, maxExpiryDays: int) -> OptionFilterUniverse
        
            Applies filter selecting options contracts based 
             on a range of expiration dates relative to the 
             current day
        
        
            minExpiryDays: The minimum time, expressed in days, until expiry 
             to include, for example, 10
                    would 
             exclude contracts expiring in more than 10 days
        
            maxExpiryDays: The maximum time, expressed in days, until expiry 
             to include, for example, 10
                    would 
             exclude contracts expiring in less than 10 days
        """
        pass

    def FrontMonth(self):
        """
        FrontMonth(self: OptionFilterUniverse) -> OptionFilterUniverse
        
            Returns front month contract
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: OptionFilterUniverse) -> IEnumerator[Symbol]
        
            IEnumerable interface method implementation
        """
        pass

    def IncludeWeeklys(self):
        """
        IncludeWeeklys(self: OptionFilterUniverse) -> OptionFilterUniverse
        
            Includes universe of weeklys options (if any) 
             into selection
        """
        pass

    def OnlyApplyFilterAtMarketOpen(self):
        """
        OnlyApplyFilterAtMarketOpen(self: OptionFilterUniverse) -> OptionFilterUniverse
        
            Instructs the engine to only filter options 
             contracts on the first time step of each market 
             day.
        """
        pass

    def PutsOnly(self):
        """
        PutsOnly(self: OptionFilterUniverse) -> OptionFilterUniverse
        
            Sets universe of put options (if any) as a 
             selection
        """
        pass

    def Refresh(self, allSymbols, underlying, exchangeDateChange):
        """ Refresh(self: OptionFilterUniverse, allSymbols: IEnumerable[Symbol], underlying: BaseData, exchangeDateChange: bool) """
        pass

    def Strikes(self, minStrike, maxStrike):
        """
        Strikes(self: OptionFilterUniverse, minStrike: int, maxStrike: int) -> OptionFilterUniverse
        
            Applies filter selecting options contracts based 
             on a range of strikes in relative terms
        
        
            minStrike: The minimum strike relative to the underlying 
             price, for example, -1 would filter out contracts 
             further than 1 strike below market price
        
            maxStrike: The maximum strike relative to the underlying 
             price, for example, +1 would filter out contracts 
             further than 1 strike above market price
        """
        pass

    def WeeklysOnly(self):
        """
        WeeklysOnly(self: OptionFilterUniverse) -> OptionFilterUniverse
        
            Sets universe of weeklys options (if any) as a 
             selection
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Symbol](enumerable: IEnumerable[Symbol], value: Symbol) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, allSymbols=None, underlying=None):
        """
        __new__(cls: type)
        __new__(cls: type, allSymbols: IEnumerable[Symbol], underlying: BaseData)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsDynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the universe is dynamic and filter needs to be reapplied

Get: IsDynamic(self: OptionFilterUniverse) -> bool

"""

    Underlying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The underlying price data

Get: Underlying(self: OptionFilterUniverse) -> BaseData

"""


    Type = None


class OptionFilterUniverseEx(object):
    """ Extensions for Linq support """
    @staticmethod
    def Select(universe, mapFunc):
        """ Select(universe: OptionFilterUniverse, mapFunc: Func[Symbol, Symbol]) -> OptionFilterUniverse """
        pass

    @staticmethod
    def SelectMany(universe, mapFunc):
        """ SelectMany(universe: OptionFilterUniverse, mapFunc: Func[Symbol, IEnumerable[Symbol]]) -> OptionFilterUniverse """
        pass

    @staticmethod
    def Where(universe, predicate):
        """ Where(universe: OptionFilterUniverse, predicate: Func[Symbol, bool]) -> OptionFilterUniverse """
        pass

    __all__ = [
        'Select',
        'SelectMany',
        'Where',
    ]


class OrderProviderExtensions(object):
    """ Provides extension methods for the QuantConnect.Securities.IOrderProvider interface """
    @staticmethod
    def GetOrderByBrokerageId(orderProvider, brokerageId):
        """
        GetOrderByBrokerageId(orderProvider: IOrderProvider, brokerageId: Int64) -> Order
        
            Gets the order by its brokerage id
        
            orderProvider: The order provider to search
            brokerageId: The brokerage id to fetch
            Returns: The first order matching the brokerage id, or 
             null if no match is found
        
        GetOrderByBrokerageId(orderProvider: IOrderProvider, brokerageId: int) -> Order
        
            Gets the order by its brokerage id
        
            orderProvider: The order provider to search
            brokerageId: The brokerage id to fetch
            Returns: The first order matching the brokerage id, or 
             null if no match is found
        """
        pass

    __all__ = [
        'GetOrderByBrokerageId',
    ]


class SecurityMarginModel(BuyingPowerModel, IBuyingPowerModel):
    """
    Represents a simple, constant margin model by specifying the percentages of required margin.
    
    SecurityMarginModel()
    SecurityMarginModel(initialMarginRequirement: Decimal, maintenanceMarginRequirement: Decimal, requiredFreeBuyingPowerPercent: Decimal)
    SecurityMarginModel(leverage: Decimal, requiredFreeBuyingPowerPercent: Decimal)
    """
    def GetInitialMarginRequiredForOrder(self, *args): #cannot find CLR method
        """
        GetInitialMarginRequiredForOrder(self: BuyingPowerModel, parameters: InitialMarginRequiredForOrderParameters) -> Decimal
        
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
        GetInitialMarginRequirement(self: BuyingPowerModel, security: Security, quantity: Decimal) -> Decimal
        
            The margin that must be held in order to increase 
             the position by the provided quantity
        """
        pass

    def GetMaintenanceMargin(self, *args): #cannot find CLR method
        """
        GetMaintenanceMargin(self: BuyingPowerModel, security: Security) -> Decimal
        
            Gets the margin currently allocated to the 
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, initialMarginRequirement: Decimal, maintenanceMarginRequirement: Decimal, requiredFreeBuyingPowerPercent: Decimal)
        __new__(cls: type, leverage: Decimal, requiredFreeBuyingPowerPercent: Decimal)
        """
        pass

    RequiredFreeBuyingPowerPercent = None


class PatternDayTradingMarginModel(SecurityMarginModel, IBuyingPowerModel):
    """
    Represents a simple margining model where margin/leverage depends on market state (open or close).
                During regular market hours, leverage is 4x, otherwise 2x
    
    PatternDayTradingMarginModel()
    PatternDayTradingMarginModel(closedMarketLeverage: Decimal, openMarketLeverage: Decimal)
    """
    def GetInitialMarginRequiredForOrder(self, *args): #cannot find CLR method
        """
        GetInitialMarginRequiredForOrder(self: BuyingPowerModel, parameters: InitialMarginRequiredForOrderParameters) -> Decimal
        
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
        GetInitialMarginRequirement(self: PatternDayTradingMarginModel, security: Security, quantity: Decimal) -> Decimal
        
            The percentage of an order's absolute cost that 
             must be held in free cash in order to place the 
             order
        """
        pass

    def GetLeverage(self, security):
        """
        GetLeverage(self: PatternDayTradingMarginModel, security: Security) -> Decimal
        
            Gets the current leverage of the security
        
            security: The security to get leverage for
            Returns: The current leverage in the security
        """
        pass

    def GetMaintenanceMargin(self, *args): #cannot find CLR method
        """
        GetMaintenanceMargin(self: PatternDayTradingMarginModel, security: Security) -> Decimal
        
            The percentage of the holding's absolute cost 
             that must be held in free cash in order to avoid 
             a margin call
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
        SetLeverage(self: PatternDayTradingMarginModel, security: Security, leverage: Decimal)
            Sets the leverage for the applicable securities, 
             i.e, equities
        
        
            security: The security to set leverage to
            leverage: The new leverage
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, closedMarketLeverage=None, openMarketLeverage=None):
        """
        __new__(cls: type)
        __new__(cls: type, closedMarketLeverage: Decimal, openMarketLeverage: Decimal)
        """
        pass

    RequiredFreeBuyingPowerPercent = None


class RegisteredSecurityDataTypesProvider(object, IRegisteredSecurityDataTypesProvider):
    """
    Provides an implementation of QuantConnect.Securities.IRegisteredSecurityDataTypesProvider that permits the
                consumer to modify the expected types
    
    RegisteredSecurityDataTypesProvider()
    """
    def RegisterType(self, type):
        """
        RegisterType(self: RegisteredSecurityDataTypesProvider, type: Type) -> bool
        
            Registers the specified type w/ the provider
            Returns: True if the type was previously not registered
        """
        pass

    def TryGetType(self, name, type):
        """
        TryGetType(self: RegisteredSecurityDataTypesProvider, name: str) -> (bool, Type)
        
            Gets an enumerable of data types expected to be 
             contained in a 
             QuantConnect.Securities.DynamicSecurityData 
             instance
        """
        pass

    def UnregisterType(self, type):
        """
        UnregisterType(self: RegisteredSecurityDataTypesProvider, type: Type) -> bool
        
            Removes the registration for the specified type
            Returns: True if the type was previously registered
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Null = None


class RelativeStandardDeviationVolatilityModel(BaseVolatilityModel, IVolatilityModel):
    """
    Provides an implementation of QuantConnect.Securities.IVolatilityModel that computes the
                relative standard deviation as the volatility of the security
    
    RelativeStandardDeviationVolatilityModel(periodSpan: TimeSpan, periods: int)
    """
    def GetHistoryRequirements(self, security, utcTime):
        """
        GetHistoryRequirements(self: RelativeStandardDeviationVolatilityModel, security: Security, utcTime: DateTime) -> IEnumerable[HistoryRequest]
        
            Returns history requirements for the volatility 
             model expressed in the form of history request
        
        
            security: The security of the request
            utcTime: The date/time of the request
            Returns: History request object list, or empty if no 
             requirements
        """
        pass

    def Update(self, security, data):
        """
        Update(self: RelativeStandardDeviationVolatilityModel, security: Security, data: BaseData)
            Updates this model using the new price 
             information in
                    the specified 
             security instance
        
        
            security: The security to calculate volatility for
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, periodSpan, periods):
        """ __new__(cls: type, periodSpan: TimeSpan, periods: int) """
        pass

    Volatility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the volatility of the security as a percentage

Get: Volatility(self: RelativeStandardDeviationVolatilityModel) -> Decimal

"""


    SubscriptionDataConfigProvider = None


class ReservedBuyingPowerForPosition(object):
    """
    Defines the result for QuantConnect.Securities.IBuyingPowerModel.GetReservedBuyingPowerForPosition(QuantConnect.Securities.ReservedBuyingPowerForPositionParameters)
    
    ReservedBuyingPowerForPosition(reservedBuyingPowerForPosition: Decimal)
    """
    @staticmethod # known case of __new__
    def __new__(self, reservedBuyingPowerForPosition):
        """ __new__(cls: type, reservedBuyingPowerForPosition: Decimal) """
        pass

    AbsoluteUsedBuyingPower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the reserved buying power

Get: AbsoluteUsedBuyingPower(self: ReservedBuyingPowerForPosition) -> Decimal

"""



class ReservedBuyingPowerForPositionParameters(object):
    """
    Defines the parameters for QuantConnect.Securities.IBuyingPowerModel.GetReservedBuyingPowerForPosition(QuantConnect.Securities.ReservedBuyingPowerForPositionParameters)
    
    ReservedBuyingPowerForPositionParameters(security: Security)
    """
    def ResultInAccountCurrency(self, reservedBuyingPower):
        """
        ResultInAccountCurrency(self: ReservedBuyingPowerForPositionParameters, reservedBuyingPower: Decimal) -> ReservedBuyingPowerForPosition
        
            Creates the result using the specified reserved 
             buying power in units of the account currency
        
        
            reservedBuyingPower: The reserved buying power in units of the account 
             currency
        
            Returns: The reserved buying power
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, security):
        """ __new__(cls: type, security: Security) """
        pass

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security

Get: Security(self: ReservedBuyingPowerForPositionParameters) -> Security

"""



class Security(object, ISecurityPrice):
    """
    A base vehicle properties class for providing a common interface to all assets in QuantConnect.
    
    Security(exchangeHours: SecurityExchangeHours, config: SubscriptionDataConfig, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypesProvider: IRegisteredSecurityDataTypesProvider, cache: SecurityCache)
    Security(symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypesProvider: IRegisteredSecurityDataTypesProvider, cache: SecurityCache)
    """
    def GetLastData(self):
        """
        GetLastData(self: Security) -> BaseData
        
            Get the last price update set to the security.
            Returns: BaseData object for this security
        """
        pass

    def IsCustomData(self):
        """
        IsCustomData(self: Security) -> bool
        
            Returns true if the security contains at least 
             one subscription that represents custom data
        """
        pass

    def RefreshDataNormalizationModeProperty(self):
        """
        RefreshDataNormalizationModeProperty(self: Security)
            This method will refresh the value of the 
             QuantConnect.Securities.Security.DataNormalization
             Mode property.
                    This is required for 
             backward-compatibility.
                    TODO: to be 
             deleted with the DataNormalizationMode property
        """
        pass

    def SetBuyingPowerModel(self, *__args):
        """
        SetBuyingPowerModel(self: Security, buyingPowerModel: IBuyingPowerModel)
            Sets the buying power model
        
            buyingPowerModel: Model that represents a security's model of 
             buying power
        
        SetBuyingPowerModel(self: Security, pyObject: PyObject)
            Sets the buying power model
        
            pyObject: Model that represents a security's model of 
             buying power
        """
        pass

    def SetDataNormalizationMode(self, mode):
        """
        SetDataNormalizationMode(self: Security, mode: DataNormalizationMode)
            Sets the data normalization mode to be used by 
             this security
        """
        pass

    def SetFeeModel(self, feelModel):
        """
        SetFeeModel(self: Security, feelModel: IFeeModel)
            Sets the fee model
        
            feelModel: Model that represents a fee model
        SetFeeModel(self: Security, feelModel: PyObject)
            Sets the fee model
        
            feelModel: Model that represents a fee model
        """
        pass

    def SetFillModel(self, fillModel):
        """
        SetFillModel(self: Security, fillModel: IFillModel)
            Sets the fill model
        
            fillModel: Model that represents a fill model
        SetFillModel(self: Security, fillModel: PyObject)
            Sets the fill model
        
            fillModel: Model that represents a fill model
        """
        pass

    def SetLeverage(self, leverage):
        """
        SetLeverage(self: Security, leverage: Decimal)
            Set the leverage parameter for this security
        
            leverage: Leverage for this asset
        """
        pass

    def SetLocalTimeKeeper(self, localTimeKeeper):
        """
        SetLocalTimeKeeper(self: Security, localTimeKeeper: LocalTimeKeeper)
            Sets the QuantConnect.LocalTimeKeeper to be used 
             for this QuantConnect.Securities.Security.
              
                   This is the source of this instance's time.
        
        
            localTimeKeeper: The source of this 
             QuantConnect.Securities.Security's time.
        """
        pass

    def SetMarginModel(self, *__args):
        """
        SetMarginModel(self: Security, marginModel: IBuyingPowerModel)
            Sets the margin model
        
            marginModel: Model that represents a security's model of 
             buying power
        
        SetMarginModel(self: Security, pyObject: PyObject)
            Sets the margin model
        
            pyObject: Model that represents a security's model of 
             buying power
        """
        pass

    def SetMarketPrice(self, data):
        """
        SetMarketPrice(self: Security, data: BaseData)
            Update any security properties based on the 
             latest market data and time
        
        
            data: New data packet from LEAN
        """
        pass

    def SetRealTimePrice(self, data):
        """
        SetRealTimePrice(self: Security, data: BaseData)
            Update any security properties based on the 
             latest realtime data and time
        
        
            data: New data packet from LEAN
        """
        pass

    def SetSlippageModel(self, slippageModel):
        """
        SetSlippageModel(self: Security, slippageModel: ISlippageModel)
            Sets the slippage model
        
            slippageModel: Model that represents a slippage model
        SetSlippageModel(self: Security, slippageModel: PyObject)
            Sets the slippage model
        
            slippageModel: Model that represents a slippage model
        """
        pass

    def SetVolatilityModel(self, volatilityModel):
        """
        SetVolatilityModel(self: Security, volatilityModel: IVolatilityModel)
            Sets the volatility model
        
            volatilityModel: Model that represents a volatility model
        SetVolatilityModel(self: Security, volatilityModel: PyObject)
            Sets the volatility model
        
            volatilityModel: Model that represents a volatility model
        """
        pass

    def ToString(self):
        """
        ToString(self: Security) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    def Update(self, data, dataType, containsFillForwardData):
        """ Update(self: Security, data: IReadOnlyList[BaseData], dataType: Type, containsFillForwardData: Nullable[bool]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, exchangeHours: SecurityExchangeHours, config: SubscriptionDataConfig, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypesProvider: IRegisteredSecurityDataTypesProvider, cache: SecurityCache)
        __new__(cls: type, symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: SymbolProperties, currencyConverter: ICurrencyConverter, registeredTypesProvider: IRegisteredSecurityDataTypesProvider, cache: SecurityCache)
        __new__(cls: type, symbol: Symbol, quoteCurrency: Cash, symbolProperties: SymbolProperties, exchange: SecurityExchange, cache: SecurityCache, portfolioModel: ISecurityPortfolioModel, fillModel: IFillModel, feeModel: IFeeModel, slippageModel: ISlippageModel, settlementModel: ISettlementModel, volatilityModel: IVolatilityModel, buyingPowerModel: IBuyingPowerModel, dataFilter: ISecurityDataFilter, priceVariationModel: IPriceVariationModel, currencyConverter: ICurrencyConverter, registeredTypesProvider: IRegisteredSecurityDataTypesProvider)
        __new__(cls: type, config: SubscriptionDataConfig, quoteCurrency: Cash, symbolProperties: SymbolProperties, exchange: SecurityExchange, cache: SecurityCache, portfolioModel: ISecurityPortfolioModel, fillModel: IFillModel, feeModel: IFeeModel, slippageModel: ISlippageModel, settlementModel: ISettlementModel, volatilityModel: IVolatilityModel, buyingPowerModel: IBuyingPowerModel, dataFilter: ISecurityDataFilter, priceVariationModel: IPriceVariationModel, currencyConverter: ICurrencyConverter, registeredTypesProvider: IRegisteredSecurityDataTypesProvider)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AskPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent ask price if available

Get: AskPrice(self: Security) -> Decimal

"""

    AskSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent ask size if available

Get: AskSize(self: Security) -> Decimal

"""

    BidPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent bid price if available

Get: BidPrice(self: Security) -> Decimal

"""

    BidSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent bid size if available

Get: BidSize(self: Security) -> Decimal

"""

    BuyingPowerModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the buying power model used for this security

Get: BuyingPowerModel(self: Security) -> IBuyingPowerModel

Set: BuyingPowerModel(self: Security) = value
"""

    Cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Data cache for the security to store previous price information.

Get: Cache(self: Security) -> SecurityCache

Set: Cache(self: Security) = value
"""

    Close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this uses tradebar data, return the most recent close.

Get: Close(self: Security) -> Decimal

"""

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides dynamic access to data in the cache

Get: Data(self: Security) -> object

"""

    DataFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Customizable data filter to filter outlier ticks before they are passed into user event handlers.
            By default all ticks are passed into the user algorithms.

Get: DataFilter(self: Security) -> ISecurityDataFilter

Set: DataFilter(self: Security) = value
"""

    DataNormalizationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the data normalization mode used for this security

Get: DataNormalizationMode(self: Security) -> DataNormalizationMode

"""

    Exchange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Exchange class contains the market opening hours, along with pre-post market hours.

Get: Exchange(self: Security) -> SecurityExchange

Set: Exchange(self: Security) = value
"""

    FeeModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fee model used to compute order fees for this security

Get: FeeModel(self: Security) -> IFeeModel

Set: FeeModel(self: Security) = value
"""

    FillModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fill model used to produce fill events for this security

Get: FillModel(self: Security) -> IFillModel

Set: FillModel(self: Security) = value
"""

    Fundamentals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the fundamental data associated with the security if there is any, otherwise null.

Get: Fundamentals(self: Security) -> Fundamentals

"""

    HasData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """There has been at least one datapoint since our algorithm started running for us to determine price.

Get: HasData(self: Security) -> bool

"""

    High = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this uses tradebar data, return the most recent high.

Get: High(self: Security) -> Decimal

"""

    Holdings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Holdings class contains the portfolio, cash and processes order fills.

Get: Holdings(self: Security) -> SecurityHolding

Set: Holdings(self: Security) = value
"""

    HoldStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Read only property that checks if we currently own stock in the company.

Get: HoldStock(self: Security) -> bool

"""

    Invested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for HoldStock - Do we have any of this security

Get: Invested(self: Security) -> bool

"""

    IsDelisted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the security has been delisted from exchanges and is no longer tradable

Get: IsDelisted(self: Security) -> bool

Set: IsDelisted(self: Security) = value
"""

    IsExtendedMarketHours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the security will continue feeding data after the primary market hours have closed. This was a configurable setting set in initialization.

Get: IsExtendedMarketHours(self: Security) -> bool

"""

    IsFillDataForward = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the data will use previous bars when there was no trading in this time period. This was a configurable datastream setting set in initialization.

Get: IsFillDataForward(self: Security) -> bool

"""

    IsTradable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether or not this security should be considered tradable

Get: IsTradable(self: Security) -> bool

Set: IsTradable(self: Security) = value
"""

    Leverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Leverage for this Security.

Get: Leverage(self: Security) -> Decimal

"""

    LocalTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Local time for this market

Get: LocalTime(self: Security) -> DateTime

"""

    Low = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this uses tradebar data, return the most recent low.

Get: Low(self: Security) -> Decimal

"""

    MarginModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the buying power model used for this security, an alias for QuantConnect.Securities.Security.BuyingPowerModel

Get: MarginModel(self: Security) -> IBuyingPowerModel

Set: MarginModel(self: Security) = value
"""

    Open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this uses tradebar data, return the most recent open.

Get: Open(self: Security) -> Decimal

"""

    OpenInterest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Access to the open interest of the security today

Get: OpenInterest(self: Security) -> Int64

"""

    PortfolioModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the portfolio model used by this security

Get: PortfolioModel(self: Security) -> ISecurityPortfolioModel

Set: PortfolioModel(self: Security) = value
"""

    Price = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the current value of the security.

Get: Price(self: Security) -> Decimal

"""

    PriceVariationModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Customizable price variation model used to define the minimum price variation of this security.
            By default minimum price variation is a constant find in the symbol-properties-database.

Get: PriceVariationModel(self: Security) -> IPriceVariationModel

Set: PriceVariationModel(self: Security) = value
"""

    QuoteCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Cash object used for converting the quote currency to the account currency

Get: QuoteCurrency(self: Security) -> Cash

"""

    Resolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Resolution of data requested for this security.

Get: Resolution(self: Security) -> Resolution

"""

    SettlementModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the settlement model used for this security

Get: SettlementModel(self: Security) -> ISettlementModel

Set: SettlementModel(self: Security) = value
"""

    SlippageModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Slippage model use to compute slippage of market orders

Get: SlippageModel(self: Security) -> ISlippageModel

Set: SlippageModel(self: Security) = value
"""

    SubscriptionDataConfig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the subscription configuration for this security

Get: SubscriptionDataConfig(self: Security) -> SubscriptionDataConfig

"""

    Subscriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all the subscriptions for this security

Get: Subscriptions(self: Security) -> IEnumerable[SubscriptionDataConfig]

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """QuantConnect.Securities.Security.Symbol for the asset.

Get: Symbol(self: Security) -> Symbol

"""

    SymbolProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the symbol properties for this security

Get: SymbolProperties(self: Security) -> SymbolProperties

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of the security.

Get: Type(self: Security) -> SecurityType

"""

    VolatilityModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the volatility model used for this security

Get: VolatilityModel(self: Security) -> IVolatilityModel

Set: VolatilityModel(self: Security) = value
"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Access to the volume of the equity today

Get: Volume(self: Security) -> Decimal

"""


    NullLeverage = None
    SubscriptionsBag = None


class SecurityCache(object):
    """
    Base class caching caching spot for security data and any other temporary properties.
    
    SecurityCache()
    """
    def AddData(self, data):
        """
        AddData(self: SecurityCache, data: BaseData)
            Add a new market data point to the local security 
             cache for the current market price.
                    
             Rules:
                        Don't cache fill forward 
             data.
                        Always return the last 
             observation.
                        If two consecutive 
             data has the same time stamp and one is Quotebars 
             and the other Tradebar, prioritize the Quotebar.
        """
        pass

    def AddDataList(self, data, dataType, containsFillForwardData):
        """ AddDataList(self: SecurityCache, data: IReadOnlyList[BaseData], dataType: Type, containsFillForwardData: Nullable[bool]) """
        pass

    def GetAll(self):
        """ GetAll[T](self: SecurityCache) -> IEnumerable[T] """
        pass

    def GetData(self):
# Error generating skeleton for function GetData: Method must be called on a Type for which Type.IsGenericParameter is false.

    def HasData(self, type):
        """
        HasData(self: SecurityCache, type: Type) -> bool
        
            Gets whether or not this dynamic data instance 
             has data stored for the specified type
        """
        pass

    def Reset(self):
        """
        Reset(self: SecurityCache)
            Reset cache storage and free memory
        """
        pass

    @staticmethod
    def ShareTypeCacheInstance(sourceToShare, targetToModify):
        """
        ShareTypeCacheInstance(sourceToShare: SecurityCache, targetToModify: SecurityCache)
            Helper method that modifies the target security 
             cache instance to use the
                    type cache 
             of the source
        
        
            sourceToShare: The source cache to use
            targetToModify: The target security cache that will be modified
        """
        pass

    def StoreData(self, data, dataType):
        """ StoreData(self: SecurityCache, data: IReadOnlyList[BaseData], dataType: Type) """
        pass

    def TryGetValue(self, type, data):
        """ TryGetValue(self: SecurityCache, type: Type) -> (bool, IReadOnlyList[BaseData]) """
        pass

    AskPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent ask submitted to this cache

Get: AskPrice(self: SecurityCache) -> Decimal

"""

    AskSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent ask size submitted to this cache

Get: AskSize(self: SecurityCache) -> Decimal

"""

    BidPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent bid submitted to this cache

Get: BidPrice(self: SecurityCache) -> Decimal

"""

    BidSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent bid size submitted to this cache

Get: BidSize(self: SecurityCache) -> Decimal

"""

    Close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent close submitted to this cache

Get: Close(self: SecurityCache) -> Decimal

"""

    High = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent high submitted to this cache

Get: High(self: SecurityCache) -> Decimal

"""

    Low = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent low submitted to this cache

Get: Low(self: SecurityCache) -> Decimal

"""

    Open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent open submitted to this cache

Get: Open(self: SecurityCache) -> Decimal

"""

    OpenInterest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent open interest submitted to this cache

Get: OpenInterest(self: SecurityCache) -> Int64

"""

    Price = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent price submitted to this cache

Get: Price(self: SecurityCache) -> Decimal

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent volume submitted to this cache

Get: Volume(self: SecurityCache) -> Decimal

"""



class SecurityCacheDataStoredEventArgs(EventArgs):
    """
    Event args for SecurityCache.DataStored event
    
    SecurityCacheDataStoredEventArgs(dataType: Type, data: IReadOnlyList[BaseData])
    """
    @staticmethod # known case of __new__
    def __new__(self, dataType, data):
        """ __new__(cls: type, dataType: Type, data: IReadOnlyList[BaseData]) """
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of data points stored

Get: Data(self: SecurityCacheDataStoredEventArgs) -> IReadOnlyList[BaseData]

"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of data that was stored, such as QuantConnect.Data.Market.TradeBar

Get: DataType(self: SecurityCacheDataStoredEventArgs) -> Type

"""



class SecurityCacheProvider(object):
    """
    A helper class that will provide QuantConnect.Securities.SecurityCache instances
    
    SecurityCacheProvider(securityProvider: ISecurityProvider)
    """
    def GetSecurityCache(self, symbol):
        """
        GetSecurityCache(self: SecurityCacheProvider, symbol: Symbol) -> SecurityCache
        
            Will return the 
             QuantConnect.Securities.SecurityCache instance to 
             use for a give Symbol.
                    If the 
             provided Symbol is a custom type which has an 
             underlying we will try to use the
                    
             underlying SecurityCache type cache, if the 
             underlying is not present we will keep track
            
                     of the custom Symbol in case it is added 
             later.
        
            Returns: The cache instance to use
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, securityProvider):
        """ __new__(cls: type, securityProvider: ISecurityProvider) """
        pass


class SecurityDatabaseKey(object, IEquatable[SecurityDatabaseKey]):
    """
    Represents the key to a single entry in the QuantConnect.Securities.MarketHoursDatabase or the QuantConnect.Securities.SymbolPropertiesDatabase
    
    SecurityDatabaseKey(market: str, symbol: str, securityType: SecurityType)
    """
    def Equals(self, *__args):
        """
        Equals(self: SecurityDatabaseKey, other: SecurityDatabaseKey) -> bool
        
            Indicates whether the current object is equal to 
             another object of the same type.
        
        
            other: An object to compare with this object.
            Returns: true if the current object is equal to the other 
             parameter; otherwise, false.
        
        Equals(self: SecurityDatabaseKey, obj: object) -> bool
        
            Determines whether the specified object is equal 
             to the current object.
        
        
            obj: The object to compare with the current object.
            Returns: true if the specified object  is equal to the 
             current object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: SecurityDatabaseKey) -> int
        
            Serves as the default hash function.
            Returns: A hash code for the current object.
        """
        pass

    @staticmethod
    def Parse(key):
        """
        Parse(key: str) -> SecurityDatabaseKey
        
            Parses the specified string as a 
             QuantConnect.Securities.SecurityDatabaseKey
        
        
            key: The string representation of the key
            Returns: A new QuantConnect.Securities.SecurityDatabaseKey 
             instance
        """
        pass

    def ToString(self):
        """
        ToString(self: SecurityDatabaseKey) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, market, symbol, securityType):
        """ __new__(cls: type, market: str, symbol: str, securityType: SecurityType) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Market = None
    SecurityType = None
    Symbol = None
    Wildcard = '[*]'


class SecurityDataFilter(object, ISecurityDataFilter):
    """
    Base class implementation for packet by packet data filtering mechanism to dynamically detect bad ticks.
    
    SecurityDataFilter()
    """
    def Filter(self, vehicle, data):
        """
        Filter(self: SecurityDataFilter, vehicle: Security, data: BaseData) -> bool
        
            Filter the data packet passing through this 
             method by returning true to accept, or false to 
             fail/reject the data point.
        
        
            vehicle: Security vehicle for filter
            data: BasData data object we're filtering
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class SecurityExchange(object):
    """
    Base exchange class providing information and helper tools for reading the current exchange situation
    
    SecurityExchange(exchangeHours: SecurityExchangeHours)
    """
    def DateIsOpen(self, dateToCheck):
        """
        DateIsOpen(self: SecurityExchange, dateToCheck: DateTime) -> bool
        
            Check if the *date* is open.
        
            dateToCheck: Date to check
            Returns: Return true if the exchange is open for this date
        """
        pass

    def DateTimeIsOpen(self, dateTime):
        """
        DateTimeIsOpen(self: SecurityExchange, dateTime: DateTime) -> bool
        
            Check if this DateTime is open.
        
            dateTime: DateTime to check
            Returns: Boolean true if the market is open
        """
        pass

    def IsClosingSoon(self, minutesToClose):
        """
        IsClosingSoon(self: SecurityExchange, minutesToClose: int) -> bool
        
            Determines if the exchange is going to close in 
             the next provided minutes
        
        
            minutesToClose: Minutes to close to check
            Returns: Returns true if the exchange is going to close in 
             the next provided minutes
        """
        pass

    def IsOpenDuringBar(self, barStartTime, barEndTime, isExtendedMarketHours):
        """
        IsOpenDuringBar(self: SecurityExchange, barStartTime: DateTime, barEndTime: DateTime, isExtendedMarketHours: bool) -> bool
        
            Determines if the exchange was open at any time 
             between start and stop
        """
        pass

    def SetLocalDateTimeFrontier(self, newLocalTime):
        """
        SetLocalDateTimeFrontier(self: SecurityExchange, newLocalTime: DateTime)
            Set the current datetime in terms of the 
             exchange's local time zone
        
        
            newLocalTime: Most recent data tick
        """
        pass

    def SetMarketHours(self, marketHoursSegments, days):
        """ SetMarketHours(self: SecurityExchange, marketHoursSegments: IEnumerable[MarketHoursSegment], *days: Array[DayOfWeek]) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, exchangeHours):
        """ __new__(cls: type, exchangeHours: SecurityExchangeHours) """
        pass

    ClosingSoon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean property for quickly testing if the exchange is 10 minutes away from closing.

Get: ClosingSoon(self: SecurityExchange) -> bool

"""

    ExchangeOpen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean property for quickly testing if the exchange is open.

Get: ExchangeOpen(self: SecurityExchange) -> bool

"""

    Hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the QuantConnect.Securities.SecurityExchangeHours for this exchange

Get: Hours(self: SecurityExchange) -> SecurityExchangeHours

"""

    LocalTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Time from the most recent data

Get: LocalTime(self: SecurityExchange) -> DateTime

"""

    TimeZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time zone for this exchange

Get: TimeZone(self: SecurityExchange) -> DateTimeZone

"""

    TradingDaysPerYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of trading days per year for this security. By default the market is open 365 days per year.

Get: TradingDaysPerYear(self: SecurityExchange) -> int

"""



class SecurityExchangeHours(object):
    """
    Represents the schedule of a security exchange. This includes daily regular and extended market hours
                as well as holidays, early closes and late opens.
    
    SecurityExchangeHours(timeZone: DateTimeZone, holidayDates: IEnumerable[DateTime], marketHoursForEachDayOfWeek: IReadOnlyDictionary[DayOfWeek, LocalMarketHours], earlyCloses: IReadOnlyDictionary[DateTime, TimeSpan], lateOpens: IReadOnlyDictionary[DateTime, TimeSpan])
    """
    @staticmethod
    def AlwaysOpen(timeZone):
        """
        AlwaysOpen(timeZone: DateTimeZone) -> SecurityExchangeHours
        
            Gets a 
             QuantConnect.Securities.SecurityExchangeHours 
             instance that is always open
        """
        pass

    def GetMarketHours(self, localDateTime):
        """
        GetMarketHours(self: SecurityExchangeHours, localDateTime: DateTime) -> LocalMarketHours
        
            Helper to access the market hours field based on 
             the day of week
        
        
            localDateTime: The local date time to retrieve market hours for
        """
        pass

    def GetNextMarketClose(self, localDateTime, extendedMarket):
        """
        GetNextMarketClose(self: SecurityExchangeHours, localDateTime: DateTime, extendedMarket: bool) -> DateTime
        
            Gets the local date time corresponding to the 
             next market close following the specified time
        
        
            localDateTime: The time to begin searching for market close 
             (non-inclusive)
        
            extendedMarket: True to include extended market hours in the 
             search
        
            Returns: The next market closing date time following the 
             specified local date time
        """
        pass

    def GetNextMarketOpen(self, localDateTime, extendedMarket):
        """
        GetNextMarketOpen(self: SecurityExchangeHours, localDateTime: DateTime, extendedMarket: bool) -> DateTime
        
            Gets the local date time corresponding to the 
             next market open following the specified time
        
        
            localDateTime: The time to begin searching for market open 
             (non-inclusive)
        
            extendedMarket: True to include extended market hours in the 
             search
        
            Returns: The next market opening date time following the 
             specified local date time
        """
        pass

    def GetNextTradingDay(self, date):
        """
        GetNextTradingDay(self: SecurityExchangeHours, date: DateTime) -> DateTime
        
            Gets the next trading day
        
            date: The date to start searching at
            Returns: The next trading day
        """
        pass

    def GetPreviousTradingDay(self, localDate):
        """
        GetPreviousTradingDay(self: SecurityExchangeHours, localDate: DateTime) -> DateTime
        
            Gets the previous trading day
        
            localDate: The date to start searching at in this exchange's 
             time zones
        
            Returns: The previous trading day
        """
        pass

    def IsDateOpen(self, localDateTime):
        """
        IsDateOpen(self: SecurityExchangeHours, localDateTime: DateTime) -> bool
        
            Determines if the exchange will be open on the 
             date specified by the local date time
        
        
            localDateTime: The date time to check if the day is open
            Returns: True if the exchange will be open on the 
             specified date, false otherwise
        """
        pass

    def IsOpen(self, *__args):
        """
        IsOpen(self: SecurityExchangeHours, localDateTime: DateTime, extendedMarket: bool) -> bool
        
            Determines if the exchange is open at the 
             specified local date time.
        
        
            localDateTime: The time to check represented as a local time
            extendedMarket: True to use the extended market hours, false for 
             just regular market hours
        
            Returns: True if the exchange is considered open at the 
             specified time, false otherwise
        
        IsOpen(self: SecurityExchangeHours, startLocalDateTime: DateTime, endLocalDateTime: DateTime, extendedMarket: bool) -> bool
        
            Determines if the exchange is open at any point 
             in time over the specified interval.
        
        
            startLocalDateTime: The start of the interval in local time
            endLocalDateTime: The end of the interval in local time
            extendedMarket: True to use the extended market hours, false for 
             just regular market hours
        
            Returns: True if the exchange is considered open at the 
             specified time, false otherwise
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, timeZone, holidayDates, marketHoursForEachDayOfWeek, earlyCloses, lateOpens):
        """ __new__(cls: type, timeZone: DateTimeZone, holidayDates: IEnumerable[DateTime], marketHoursForEachDayOfWeek: IReadOnlyDictionary[DayOfWeek, LocalMarketHours], earlyCloses: IReadOnlyDictionary[DateTime, TimeSpan], lateOpens: IReadOnlyDictionary[DateTime, TimeSpan]) """
        pass

    EarlyCloses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the early closes for this exchange

Get: EarlyCloses(self: SecurityExchangeHours) -> IReadOnlyDictionary[DateTime, TimeSpan]

"""

    Holidays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the holidays for the exchange

Get: Holidays(self: SecurityExchangeHours) -> HashSet[DateTime]

"""

    LateOpens = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the late opens for this exchange

Get: LateOpens(self: SecurityExchangeHours) -> IReadOnlyDictionary[DateTime, TimeSpan]

"""

    MarketHours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the market hours for this exchange

Get: MarketHours(self: SecurityExchangeHours) -> IReadOnlyDictionary[DayOfWeek, LocalMarketHours]

"""

    RegularMarketDuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most common tradable time during the market week.
            For a normal US equity trading day this is 6.5 hours.
            This does NOT account for extended market hours and only
            considers QuantConnect.Securities.MarketHoursState.Market

Get: RegularMarketDuration(self: SecurityExchangeHours) -> TimeSpan

"""

    TimeZone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time zone this exchange resides in

Get: TimeZone(self: SecurityExchangeHours) -> DateTimeZone

"""



class SecurityHolding(object):
    """
    SecurityHolding is a base class for purchasing and holding a market item which manages the asset portfolio
    
    SecurityHolding(security: Security, currencyConverter: ICurrencyConverter)
    """
    def AddNewFee(self, newFee):
        """
        AddNewFee(self: SecurityHolding, newFee: Decimal)
            Adds a fee to the running total of total fees in 
             units of the account's currency.
        """
        pass

    def AddNewProfit(self, profitLoss):
        """
        AddNewProfit(self: SecurityHolding, profitLoss: Decimal)
            Adds a profit record to the running total of 
             profit in units of the account's currency.
        
        
            profitLoss: The cash change in portfolio from closing a 
             position
        """
        pass

    def AddNewSale(self, saleValue):
        """
        AddNewSale(self: SecurityHolding, saleValue: Decimal)
            Adds a new sale value to the running total 
             trading volume in units of the account's 
             currency.
        """
        pass

    def SetHoldings(self, averagePrice, quantity):
        """
        SetHoldings(self: SecurityHolding, averagePrice: Decimal, quantity: int)
            Set the quantity of holdings and their average 
             price after processing a portfolio fill.
        
        SetHoldings(self: SecurityHolding, averagePrice: Decimal, quantity: Decimal)
            Set the quantity of holdings and their average 
             price after processing a portfolio fill.
        """
        pass

    def SetLastTradeProfit(self, lastTradeProfit):
        """
        SetLastTradeProfit(self: SecurityHolding, lastTradeProfit: Decimal)
            Set the last trade profit for this security from 
             a Portfolio.ProcessFill call in units of the 
             account's currency.
        
        
            lastTradeProfit: Value of the last trade profit
        """
        pass

    def TotalCloseProfit(self):
        """
        TotalCloseProfit(self: SecurityHolding) -> Decimal
        
            Profit if we closed the holdings right now 
             including the approximate fees in units of the 
             account's currency.
        """
        pass

    def UpdateMarketPrice(self, closingPrice):
        """
        UpdateMarketPrice(self: SecurityHolding, closingPrice: Decimal)
            Update local copy of closing price value.
        
            closingPrice: Price of the underlying asset to be used for 
             calculating market price / portfolio value
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, security, currencyConverter):
        """
        __new__(cls: type, security: Security, currencyConverter: ICurrencyConverter)
        __new__(cls: type, holding: SecurityHolding)
        """
        pass

    AbsoluteHoldingsCost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Absolute holdings cost for current holdings in units of the account's currency.

Get: AbsoluteHoldingsCost(self: SecurityHolding) -> Decimal

"""

    AbsoluteHoldingsValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Absolute of the market value of our holdings in units of the account's currency.

Get: AbsoluteHoldingsValue(self: SecurityHolding) -> Decimal

"""

    AbsoluteQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Absolute quantity of holdings of this security

Get: AbsoluteQuantity(self: SecurityHolding) -> Decimal

"""

    AveragePrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Average price of the security holdings.

Get: AveragePrice(self: SecurityHolding) -> Decimal

"""

    HoldingsCost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Acquisition cost of the security total holdings in units of the account's currency.

Get: HoldingsCost(self: SecurityHolding) -> Decimal

"""

    HoldingsValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Market value of our holdings in units of the account's currency.

Get: HoldingsValue(self: SecurityHolding) -> Decimal

"""

    HoldStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean flat indicating if we hold any of the security

Get: HoldStock(self: SecurityHolding) -> bool

"""

    Invested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean flat indicating if we hold any of the security

Get: Invested(self: SecurityHolding) -> bool

"""

    IsLong = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean flag indicating we have a net positive holding of the security.

Get: IsLong(self: SecurityHolding) -> bool

"""

    IsShort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """BBoolean flag indicating we have a net negative holding of the security.

Get: IsShort(self: SecurityHolding) -> bool

"""

    LastTradeProfit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Record of the closing profit from the last trade conducted in units of the account's currency.

Get: LastTradeProfit(self: SecurityHolding) -> Decimal

"""

    Leverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Leverage of the underlying security.

Get: Leverage(self: SecurityHolding) -> Decimal

"""

    NetProfit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the net for this company measured by the profit less fees in units of the account's currency.

Get: NetProfit(self: SecurityHolding) -> Decimal

"""

    Price = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Current market price of the security.

Get: Price(self: SecurityHolding) -> Decimal

"""

    Profit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Calculate the total profit for this security in units of the account's currency.

Get: Profit(self: SecurityHolding) -> Decimal

"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Quantity of the security held.

Get: Quantity(self: SecurityHolding) -> Decimal

"""

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The security being held

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbol identifier of the underlying security.

Get: Symbol(self: SecurityHolding) -> Symbol

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current target holdings for this security

Get: Target(self: SecurityHolding) -> IPortfolioTarget

Set: Target(self: SecurityHolding) = value
"""

    TotalFees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total fees for this company since the algorithm started in units of the account's currency.

Get: TotalFees(self: SecurityHolding) -> Decimal

"""

    TotalSaleVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total transaction volume for this security since the algorithm started in units of the account's currency.

Get: TotalSaleVolume(self: SecurityHolding) -> Decimal

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The security type of the symbol

Get: Type(self: SecurityHolding) -> SecurityType

"""

    UnleveredAbsoluteHoldingsCost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unlevered absolute acquisition cost of the security total holdings in units of the account's currency.

Get: UnleveredAbsoluteHoldingsCost(self: SecurityHolding) -> Decimal

"""

    UnleveredHoldingsCost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unlevered Acquisition cost of the security total holdings in units of the account's currency.

Get: UnleveredHoldingsCost(self: SecurityHolding) -> Decimal

"""

    UnrealizedProfit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unrealized profit of this security when absolute quantity held is more than zero in units of the account's currency.

Get: UnrealizedProfit(self: SecurityHolding) -> Decimal

"""

    UnrealizedProfitPercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unrealized profit as a percenage of holdings cost

Get: UnrealizedProfitPercent(self: SecurityHolding) -> Decimal

"""



class SecurityInitializer(object):
    """ Provides static access to the QuantConnect.Securities.SecurityInitializer.Null security initializer """
    Null = None
    __all__ = [
        'Null',
    ]


class SecurityManager(ExtendedDictionary[Security], IExtendedDictionary[Symbol, Security], IDictionary[Symbol, Security], ICollection[KeyValuePair[Symbol, Security]], IEnumerable[KeyValuePair[Symbol, Security]], IEnumerable, INotifyCollectionChanged):
    """
    Enumerable security management class for grouping security objects into an array and providing any common properties.
    
    SecurityManager(timeKeeper: ITimeKeeper)
    """
    def Add(self, *__args):
        """
        Add(self: SecurityManager, symbol: Symbol, security: Security)
            Add a new security with this symbol to the 
             collection.
        
        
            symbol: symbol for security we're trading
            security: security object
        Add(self: SecurityManager, security: Security)
            Add a new security with this symbol to the 
             collection.
        
        
            security: security object
        Add(self: SecurityManager, pair: KeyValuePair[Symbol, Security])
        """
        pass

    def Clear(self):
        """
        Clear(self: SecurityManager)
            Clear the securities array to delete all the 
             portfolio and asset information.
        """
        pass

    def Contains(self, pair):
        """ Contains(self: SecurityManager, pair: KeyValuePair[Symbol, Security]) -> bool """
        pass

    def ContainsKey(self, symbol):
        """
        ContainsKey(self: SecurityManager, symbol: Symbol) -> bool
        
            Check if this collection contains this symbol.
        
            symbol: Symbol we're checking for.
            Returns: Bool true if contains this symbol pair
        """
        pass

    def CopyTo(self, array, number):
        """ CopyTo(self: SecurityManager, array: Array[KeyValuePair[Symbol, Security]], number: int) """
        pass

    def CreateSecurity(self, symbol, *__args):
        """
        CreateSecurity(self: SecurityManager, symbol: Symbol, subscriptionDataConfigList: List[SubscriptionDataConfig], leverage: Decimal, addToSymbolCache: bool) -> Security
        CreateSecurity(self: SecurityManager, symbol: Symbol, subscriptionDataConfig: SubscriptionDataConfig, leverage: Decimal, addToSymbolCache: bool) -> Security
        
            Creates a new security
        """
        pass

    def OnCollectionChanged(self, *args): #cannot find CLR method
        """
        OnCollectionChanged(self: SecurityManager, changedEventArgs: NotifyCollectionChangedEventArgs)
            Event invocator for the 
             QuantConnect.Securities.SecurityManager.Collection
             Changed event
        
        
            changedEventArgs: Event arguments for the 
             QuantConnect.Securities.SecurityManager.Collection
             Changed event
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: SecurityManager, pair: KeyValuePair[Symbol, Security]) -> bool
        Remove(self: SecurityManager, symbol: Symbol) -> bool
        
            Remove this symbol security: Dictionary interface 
             implementation.
        
        
            symbol: Symbol we're searching for
            Returns: true success
        """
        pass

    def SetLiveMode(self, isLiveMode):
        """
        SetLiveMode(self: SecurityManager, isLiveMode: bool)
            Set live mode state of the algorithm
        
            isLiveMode: True, live mode is enabled
        """
        pass

    def SetSecurityService(self, securityService):
        """
        SetSecurityService(self: SecurityManager, securityService: SecurityService)
            Sets the Security Service to be used
        """
        pass

    def TryGetValue(self, symbol, security):
        """
        TryGetValue(self: SecurityManager, symbol: Symbol) -> (bool, Security)
        
            Try and get this security object with matching 
             symbol and return true on success.
        
        
            symbol: String search symbol
            Returns: True on successfully locating the security object
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary[Symbol, Security], key: Symbol) -> bool """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, timeKeeper):
        """ __new__(cls: type, timeKeeper: ITimeKeeper) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Count of the number of securities in the collection.

Get: Count(self: SecurityManager) -> int

"""

    GetKeys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.Generic.ICollection containing the Symbol objects of the System.Collections.Generic.IDictionary.

"""

    GetValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.Generic.ICollection containing the values in the System.Collections.Generic.IDictionary.

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Flag indicating if the internal array is read only.

Get: IsReadOnly(self: SecurityManager) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of the symbol-keys in the collection of securities.

Get: Keys(self: SecurityManager) -> ICollection[Symbol]

"""

    UtcTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent time this manager was updated

Get: UtcTime(self: SecurityManager) -> DateTime

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get a list of the security objects for this collection.

Get: Values(self: SecurityManager) -> ICollection[Security]

"""


    CollectionChanged = None


class SecurityPortfolioManager(ExtendedDictionary[SecurityHolding], IExtendedDictionary[Symbol, SecurityHolding], IDictionary[Symbol, SecurityHolding], ICollection[KeyValuePair[Symbol, SecurityHolding]], IEnumerable[KeyValuePair[Symbol, SecurityHolding]], IEnumerable, ISecurityProvider):
    """
    Portfolio manager class groups popular properties and makes them accessible through one interface.
                It also provide indexing by the vehicle symbol to get the Security.Holding objects.
    
    SecurityPortfolioManager(securityManager: SecurityManager, transactions: SecurityTransactionManager, defaultOrderProperties: IOrderProperties)
    """
    def Add(self, *__args):
        """
        Add(self: SecurityPortfolioManager, symbol: Symbol, holding: SecurityHolding)
            Add a new securities string-security to the 
             portfolio.
        
        
            symbol: Symbol of dictionary
            holding: SecurityHoldings object
        Add(self: SecurityPortfolioManager, pair: KeyValuePair[Symbol, SecurityHolding])
        """
        pass

    def AddTransactionRecord(self, time, transactionProfitLoss):
        """
        AddTransactionRecord(self: SecurityPortfolioManager, time: DateTime, transactionProfitLoss: Decimal)
            Record the transaction value and time in a list 
             to later be processed for statistics creation.
        
        
            time: Time of order processed
            transactionProfitLoss: Profit Loss.
        """
        pass

    def AddUnsettledCashAmount(self, item):
        """
        AddUnsettledCashAmount(self: SecurityPortfolioManager, item: UnsettledCashAmount)
            Adds an item to the list of unsettled cash amounts
        
            item: The item to add
        """
        pass

    def ApplyDividend(self, dividend, liveMode, mode):
        """
        ApplyDividend(self: SecurityPortfolioManager, dividend: Dividend, liveMode: bool, mode: DataNormalizationMode)
            Applies a dividend to the portfolio
        
            dividend: The dividend to be applied
            liveMode: True if live mode, false for backtest
            mode: The QuantConnect.DataNormalizationMode for this 
             security
        """
        pass

    def ApplySplit(self, split, liveMode, mode):
        """
        ApplySplit(self: SecurityPortfolioManager, split: Split, liveMode: bool, mode: DataNormalizationMode)
            Applies a split to the portfolio
        
            split: The split to be applied
            liveMode: True if live mode, false for backtest
            mode: The QuantConnect.DataNormalizationMode for this 
             security
        """
        pass

    def Clear(self):
        """
        Clear(self: SecurityPortfolioManager)
            Clear the portfolio of securities objects.
        """
        pass

    def Contains(self, pair):
        """ Contains(self: SecurityPortfolioManager, pair: KeyValuePair[Symbol, SecurityHolding]) -> bool """
        pass

    def ContainsKey(self, symbol):
        """
        ContainsKey(self: SecurityPortfolioManager, symbol: Symbol) -> bool
        
            Check if the portfolio contains this symbol 
             string.
        
        
            symbol: String search symbol for the security
            Returns: Boolean true if portfolio contains this symbol
        """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: SecurityPortfolioManager, array: Array[KeyValuePair[Symbol, SecurityHolding]], index: int) """
        pass

    def GetBuyingPower(self, symbol, direction):
        """
        GetBuyingPower(self: SecurityPortfolioManager, symbol: Symbol, direction: OrderDirection) -> Decimal
        
            Gets the margin available for trading a specific 
             symbol in a specific direction.
                    
             Alias for 
             QuantConnect.Securities.SecurityPortfolioManager.G
             etMarginRemaining(System.Decimal)
        
        
            symbol: The symbol to compute margin remaining for
            direction: The order/trading direction
            Returns: The maximum order size that is currently 
             executable in the specified direction
        """
        pass

    def GetMarginRemaining(self, *__args):
        """
        GetMarginRemaining(self: SecurityPortfolioManager, totalPortfolioValue: Decimal) -> Decimal
        
            Gets the remaining margin on the account in the 
             account's currency
                    for the given 
             total portfolio value
        
        
            totalPortfolioValue: The total portfolio value 
             QuantConnect.Securities.SecurityPortfolioManager.T
             otalPortfolioValue
        
        GetMarginRemaining(self: SecurityPortfolioManager, symbol: Symbol, direction: OrderDirection) -> Decimal
        
            Gets the margin available for trading a specific 
             symbol in a specific direction.
        
        
            symbol: The symbol to compute margin remaining for
            direction: The order/trading direction
            Returns: The maximum order size that is currently 
             executable in the specified direction
        """
        pass

    def InvalidateTotalPortfolioValue(self):
        """
        InvalidateTotalPortfolioValue(self: SecurityPortfolioManager)
            Will flag the current 
             QuantConnect.Securities.SecurityPortfolioManager.T
             otalPortfolioValue as invalid
                    so it 
             is recalculated when gotten
        """
        pass

    def LogMarginInformation(self, orderRequest):
        """
        LogMarginInformation(self: SecurityPortfolioManager, orderRequest: OrderRequest)
            Logs margin information for debugging
        """
        pass

    def ProcessFill(self, fill):
        """
        ProcessFill(self: SecurityPortfolioManager, fill: OrderEvent)
            Calculate the new average price after processing 
             a partial/complete order fill event.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: SecurityPortfolioManager, pair: KeyValuePair[Symbol, SecurityHolding]) -> bool
        Remove(self: SecurityPortfolioManager, symbol: Symbol) -> bool
        
            Remove this symbol from the portfolio.
        
            symbol: Symbol of dictionary
        """
        pass

    def ScanForCashSettlement(self, timeUtc):
        """
        ScanForCashSettlement(self: SecurityPortfolioManager, timeUtc: DateTime)
            Scan the portfolio to check if unsettled funds 
             should be settled
        """
        pass

    def SetAccountCurrency(self, accountCurrency):
        """
        SetAccountCurrency(self: SecurityPortfolioManager, accountCurrency: str)
            Sets the account currency cash symbol this 
             algorithm is to manage.
        
        
            accountCurrency: The account currency cash symbol to set
        """
        pass

    def SetCash(self, *__args):
        """
        SetCash(self: SecurityPortfolioManager, cash: Decimal)
            Set the account currency cash this algorithm is 
             to manage.
        
        
            cash: Decimal cash value of portfolio
        SetCash(self: SecurityPortfolioManager, symbol: str, cash: Decimal, conversionRate: Decimal)
            Set the cash for the specified symbol
        
            symbol: The cash symbol to set
            cash: Decimal cash value of portfolio
            conversionRate: The current conversion rate for the
        """
        pass

    def SetMarginCallModel(self, *__args):
        """
        SetMarginCallModel(self: SecurityPortfolioManager, marginCallModel: IMarginCallModel)
            Sets the margin call model
        
            marginCallModel: Model that represents a portfolio's model to 
             executed margin call orders.
        
        SetMarginCallModel(self: SecurityPortfolioManager, pyObject: PyObject)
            Sets the margin call model
        
            pyObject: Model that represents a portfolio's model to 
             executed margin call orders.
        """
        pass

    def TryGetValue(self, symbol, holding):
        """
        TryGetValue(self: SecurityPortfolioManager, symbol: Symbol) -> (bool, SecurityHolding)
        
            Attempt to get the value of the securities 
             holding class if this symbol exists.
        
        
            symbol: String search symbol
            Returns: Boolean true if successful locating and setting 
             the holdings object
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary[Symbol, SecurityHolding], key: Symbol) -> bool """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, securityManager, transactions, defaultOrderProperties):
        """ __new__(cls: type, securityManager: SecurityManager, transactions: SecurityTransactionManager, defaultOrderProperties: IOrderProperties) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Cash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sum of all currencies in account in US dollars (only settled cash)

Get: Cash(self: SecurityPortfolioManager) -> Decimal

"""

    CashBook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the cash book that keeps track of all currency holdings (only settled cash)

Get: CashBook(self: SecurityPortfolioManager) -> CashBook

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Count the securities objects in the portfolio.

Get: Count(self: SecurityPortfolioManager) -> int

"""

    GetKeys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.Generic.ICollection containing the Symbol objects of the System.Collections.Generic.IDictionary.

"""

    GetValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.Generic.ICollection containing the values in the System.Collections.Generic.IDictionary.

"""

    HoldStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean flag indicating we have any holdings in the portfolio.

Get: HoldStock(self: SecurityPortfolioManager) -> bool

"""

    Invested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for HoldStock. Check if we have and holdings.

Get: Invested(self: SecurityPortfolioManager) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check if the underlying securities array is read only.

Get: IsReadOnly(self: SecurityPortfolioManager) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbol keys collection of the underlying assets in the portfolio.

Get: Keys(self: SecurityPortfolioManager) -> ICollection[Symbol]

"""

    MarginCallModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the QuantConnect.Securities.SecurityPortfolioManager.MarginCallModel for the portfolio. This
            is used to executed margin call orders.

Get: MarginCallModel(self: SecurityPortfolioManager) -> IMarginCallModel

Set: MarginCallModel(self: SecurityPortfolioManager) = value
"""

    MarginRemaining = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the remaining margin on the account in the account's currency

Get: MarginRemaining(self: SecurityPortfolioManager) -> Decimal

"""

    TotalAbsoluteHoldingsCost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total absolute holdings cost of the portfolio. This sums up the individual
            absolute cost of each holding

Get: TotalAbsoluteHoldingsCost(self: SecurityPortfolioManager) -> Decimal

"""

    TotalFees = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total fees paid during the algorithm operation across all securities in portfolio.

Get: TotalFees(self: SecurityPortfolioManager) -> Decimal

"""

    TotalHoldingsValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Absolute sum the individual items in portfolio.

Get: TotalHoldingsValue(self: SecurityPortfolioManager) -> Decimal

"""

    TotalMarginUsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total margin used across all securities in the account's currency

Get: TotalMarginUsed(self: SecurityPortfolioManager) -> Decimal

"""

    TotalPortfolioValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total portfolio value if we sold all holdings at current market rates.

Get: TotalPortfolioValue(self: SecurityPortfolioManager) -> Decimal

"""

    TotalProfit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sum of all gross profit across all securities in portfolio.

Get: TotalProfit(self: SecurityPortfolioManager) -> Decimal

"""

    TotalSaleVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total sale volume since the start of algorithm operations.

Get: TotalSaleVolume(self: SecurityPortfolioManager) -> Decimal

"""

    TotalUnleveredAbsoluteHoldingsCost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Absolute value of cash discounted from our total cash by the holdings we own.

Get: TotalUnleveredAbsoluteHoldingsCost(self: SecurityPortfolioManager) -> Decimal

"""

    TotalUnrealisedProfit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the total unrealised profit in our portfolio from the individual security unrealized profits.

Get: TotalUnrealisedProfit(self: SecurityPortfolioManager) -> Decimal

"""

    TotalUnrealizedProfit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the total unrealised profit in our portfolio from the individual security unrealized profits.

Get: TotalUnrealizedProfit(self: SecurityPortfolioManager) -> Decimal

"""

    UnsettledCash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sum of all currencies in account in US dollars (only unsettled cash)

Get: UnsettledCash(self: SecurityPortfolioManager) -> Decimal

"""

    UnsettledCashBook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the cash book that keeps track of all currency holdings (only unsettled cash)

Get: UnsettledCashBook(self: SecurityPortfolioManager) -> CashBook

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Collection of securities objects in the portfolio.

Get: Values(self: SecurityPortfolioManager) -> ICollection[SecurityHolding]

"""


    Securities = None
    Transactions = None


class SecurityPortfolioModel(object, ISecurityPortfolioModel):
    """
    Provides a default implementation of QuantConnect.Securities.ISecurityPortfolioModel that simply
                applies the fills to the algorithm's portfolio. This implementation is intended to
                handle all security types.
    
    SecurityPortfolioModel()
    """
    def ProcessFill(self, portfolio, security, fill):
        """
        ProcessFill(self: SecurityPortfolioModel, portfolio: SecurityPortfolioManager, security: Security, fill: OrderEvent)
            Performs application of an OrderEvent to the 
             portfolio
        
        
            portfolio: The algorithm's portfolio
            security: The fill's security
            fill: The order event fill object to be applied
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class SecurityProviderExtensions(object):
    """ Provides extension methods for the QuantConnect.Securities.ISecurityProvider interface. """
    @staticmethod
    def GetHoldingsQuantity(provider, symbol):
        """
        GetHoldingsQuantity(provider: ISecurityProvider, symbol: Symbol) -> Decimal
        
            Extension method to return the quantity of 
             holdings, if no holdings are present, then zero 
             is returned.
        
        
            provider: The QuantConnect.Securities.ISecurityProvider
            symbol: The symbol we want holdings quantity for
            Returns: The quantity of holdings for the specified symbol
        """
        pass

    __all__ = [
        'GetHoldingsQuantity',
    ]


class SecuritySeeder(object):
    """ Provides access to a null implementation for QuantConnect.Securities.ISecuritySeeder """
    Null = None
    __all__ = [
        'Null',
    ]


class SecurityService(object, ISecurityService):
    """
    This class implements interface QuantConnect.Interfaces.ISecurityService providing methods for creating new QuantConnect.Securities.Security
    
    SecurityService(cashBook: CashBook, marketHoursDatabase: MarketHoursDatabase, symbolPropertiesDatabase: SymbolPropertiesDatabase, securityInitializerProvider: ISecurityInitializerProvider, registeredTypes: IRegisteredSecurityDataTypesProvider, cacheProvider: SecurityCacheProvider)
    """
    def CreateSecurity(self, symbol, *__args):
        """
        CreateSecurity(self: SecurityService, symbol: Symbol, subscriptionDataConfigList: List[SubscriptionDataConfig], leverage: Decimal, addToSymbolCache: bool) -> Security
        CreateSecurity(self: SecurityService, symbol: Symbol, subscriptionDataConfig: SubscriptionDataConfig, leverage: Decimal, addToSymbolCache: bool) -> Security
        
            Creates a new security
        """
        pass

    def SetLiveMode(self, isLiveMode):
        """
        SetLiveMode(self: SecurityService, isLiveMode: bool)
            Set live mode state of the algorithm
        
            isLiveMode: True, live mode is enabled
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cashBook, marketHoursDatabase, symbolPropertiesDatabase, securityInitializerProvider, registeredTypes, cacheProvider):
        """ __new__(cls: type, cashBook: CashBook, marketHoursDatabase: MarketHoursDatabase, symbolPropertiesDatabase: SymbolPropertiesDatabase, securityInitializerProvider: ISecurityInitializerProvider, registeredTypes: IRegisteredSecurityDataTypesProvider, cacheProvider: SecurityCacheProvider) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class SecurityTransactionManager(object, IOrderProvider):
    """
    Algorithm Transactions Manager - Recording Transactions
    
    SecurityTransactionManager(algorithm: IAlgorithm, security: SecurityManager)
    """
    def AddOrder(self, request):
        """
        AddOrder(self: SecurityTransactionManager, request: SubmitOrderRequest) -> OrderTicket
        
            Add an order to collection and return the unique 
             order id or negative if an error.
        
        
            request: A request detailing the order to be submitted
            Returns: New unique, increasing orderid
        """
        pass

    def AddTransactionRecord(self, time, transactionProfitLoss):
        """
        AddTransactionRecord(self: SecurityTransactionManager, time: DateTime, transactionProfitLoss: Decimal)
            Record the transaction value and time in a list 
             to later be processed for statistics creation.
        
        
            time: Time of order processed
            transactionProfitLoss: Profit Loss.
        """
        pass

    def CancelOpenOrders(self, symbol=None, tag=None):
        """
        CancelOpenOrders(self: SecurityTransactionManager) -> List[OrderTicket]
        
            Cancels all open orders for all symbols
            Returns: List containing the cancelled order tickets
        CancelOpenOrders(self: SecurityTransactionManager, symbol: Symbol, tag: str) -> List[OrderTicket]
        
            Cancels all open orders for the specified symbol
        
            symbol: The symbol whose orders are to be cancelled
            tag: Custom order tag
            Returns: List containing the cancelled order tickets
        """
        pass

    def CancelOrder(self, orderId, orderTag):
        """
        CancelOrder(self: SecurityTransactionManager, orderId: int, orderTag: str) -> OrderTicket
        
            Added alias for RemoveOrder -
        
            orderId: Order id we wish to cancel
            orderTag: Tag to indicate from where this method was called
        """
        pass

    def GetIncrementOrderId(self):
        """
        GetIncrementOrderId(self: SecurityTransactionManager) -> int
        
            Get a new order id, and increment the internal 
             counter.
        
            Returns: New unique int order id.
        """
        pass

    def GetOpenOrders(self, *__args):
        """
        GetOpenOrders(self: SecurityTransactionManager, symbol: Symbol) -> List[Order]
        
            Get a list of all open orders for a symbol.
        
            symbol: The symbol for which to return the orders
            Returns: List of open orders.
        GetOpenOrders(self: SecurityTransactionManager, filter: Func[Order, bool]) -> List[Order]
        """
        pass

    def GetOpenOrderTickets(self, *__args):
        """
        GetOpenOrderTickets(self: SecurityTransactionManager, symbol: Symbol) -> IEnumerable[OrderTicket]
        
            Get an enumerable of open 
             QuantConnect.Orders.OrderTicket for the specified 
             symbol
        
        
            symbol: The symbol for which to return the order tickets
            Returns: An enumerable of open 
             QuantConnect.Orders.OrderTicket.
        
        GetOpenOrderTickets(self: SecurityTransactionManager, filter: Func[OrderTicket, bool]) -> IEnumerable[OrderTicket]
        """
        pass

    def GetOrderByBrokerageId(self, brokerageId):
        """
        GetOrderByBrokerageId(self: SecurityTransactionManager, brokerageId: str) -> Order
        
            Gets the order by its brokerage id
        
            brokerageId: The brokerage id to fetch
            Returns: The first order matching the brokerage id, or 
             null if no match is found
        """
        pass

    def GetOrderById(self, orderId):
        """
        GetOrderById(self: SecurityTransactionManager, orderId: int) -> Order
        
            Get the order by its id
        
            orderId: Order id to fetch
            Returns: A clone of the order with the specified id, or 
             null if no match is found
        """
        pass

    def GetOrders(self, filter):
        """ GetOrders(self: SecurityTransactionManager, filter: Func[Order, bool]) -> IEnumerable[Order] """
        pass

    def GetOrderTicket(self, orderId):
        """
        GetOrderTicket(self: SecurityTransactionManager, orderId: int) -> OrderTicket
        
            Gets the order ticket for the specified order id. 
             Returns null if not found
        
        
            orderId: The order's id
            Returns: The order ticket with the specified id, or null 
             if not found
        """
        pass

    def GetOrderTickets(self, filter):
        """ GetOrderTickets(self: SecurityTransactionManager, filter: Func[OrderTicket, bool]) -> IEnumerable[OrderTicket] """
        pass

    def ProcessRequest(self, request):
        """
        ProcessRequest(self: SecurityTransactionManager, request: OrderRequest) -> OrderTicket
        
            Processes the order request
        
            request: The request to be processed
            Returns: The order ticket for the request
        """
        pass

    def RemoveOrder(self, orderId, tag):
        """
        RemoveOrder(self: SecurityTransactionManager, orderId: int, tag: str) -> OrderTicket
        
            Remove this order from outstanding queue: user is 
             requesting a cancel.
        
        
            orderId: Specific order id to remove
            tag: Tag request
        """
        pass

    def SetOrderProcessor(self, orderProvider):
        """
        SetOrderProcessor(self: SecurityTransactionManager, orderProvider: IOrderProcessor)
            Sets the QuantConnect.Securities.IOrderProvider 
             used for fetching orders for the algorithm
        
        
            orderProvider: The QuantConnect.Securities.IOrderProvider to be 
             used to manage fetching orders
        """
        pass

    def UpdateOrder(self, request):
        """
        UpdateOrder(self: SecurityTransactionManager, request: UpdateOrderRequest) -> OrderTicket
        
            Update an order yet to be filled such as stop or 
             limit orders.
        
        
            request: Request detailing how the order should be updated
        """
        pass

    def WaitForOrder(self, orderId):
        """
        WaitForOrder(self: SecurityTransactionManager, orderId: int) -> bool
        
            Wait for a specific order to be either Filled, 
             Invalid or Canceled
        
        
            orderId: The id of the order to wait for
            Returns: True if we successfully wait for the fill, false 
             if we were unable
                    to wait. This may 
             be because it is not a market order or because 
             the timeout
                    was reached
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, algorithm, security):
        """ __new__(cls: type, algorithm: IAlgorithm, security: SecurityManager) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    LastOrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the last order id.

Get: LastOrderId(self: SecurityTransactionManager) -> int

"""

    MarketOrderFillTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Configurable timeout for market order fills

Get: MarketOrderFillTimeout(self: SecurityTransactionManager) -> TimeSpan

Set: MarketOrderFillTimeout(self: SecurityTransactionManager) = value
"""

    MinimumOrderQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Configurable minimum order size to ignore bad orders, or orders with unrealistic sizes

Get: MinimumOrderQuantity(self: SecurityTransactionManager) -> int

"""

    MinimumOrderSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Configurable minimum order value to ignore bad orders, or orders with unrealistic sizes

Get: MinimumOrderSize(self: SecurityTransactionManager) -> Decimal

"""

    OrdersCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current number of orders that have been processed

Get: OrdersCount(self: SecurityTransactionManager) -> int

"""

    TransactionRecord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Trade record of profits and losses for each trade statistics calculations

Get: TransactionRecord(self: SecurityTransactionManager) -> Dictionary[DateTime, Decimal]

"""

    UtcTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time the security information was last updated

Get: UtcTime(self: SecurityTransactionManager) -> DateTime

"""



class StandardDeviationOfReturnsVolatilityModel(BaseVolatilityModel, IVolatilityModel):
    """
    Provides an implementation of QuantConnect.Securities.IVolatilityModel that computes the
                annualized sample standard deviation of daily returns as the volatility of the security
    
    StandardDeviationOfReturnsVolatilityModel(periods: int)
    """
    def GetHistoryRequirements(self, security, utcTime):
        """
        GetHistoryRequirements(self: StandardDeviationOfReturnsVolatilityModel, security: Security, utcTime: DateTime) -> IEnumerable[HistoryRequest]
        
            Returns history requirements for the volatility 
             model expressed in the form of history request
        
        
            security: The security of the request
            utcTime: The date of the request
            Returns: History request object list, or empty if no 
             requirements
        """
        pass

    def Update(self, security, data):
        """
        Update(self: StandardDeviationOfReturnsVolatilityModel, security: Security, data: BaseData)
            Updates this model using the new price 
             information in
                    the specified 
             security instance
        
        
            security: The security to calculate volatility for
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, periods):
        """ __new__(cls: type, periods: int) """
        pass

    Volatility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the volatility of the security as a percentage

Get: Volatility(self: StandardDeviationOfReturnsVolatilityModel) -> Decimal

"""


    SubscriptionDataConfigProvider = None


class SymbolProperties(object):
    """
    Represents common properties for a specific security, uniquely identified by market, symbol and security type
    
    SymbolProperties(description: str, quoteCurrency: str, contractMultiplier: Decimal, minimumPriceVariation: Decimal, lotSize: Decimal)
    """
    @staticmethod
    def GetDefault(quoteCurrency):
        """
        GetDefault(quoteCurrency: str) -> SymbolProperties
        
            Gets a default instance of the 
             QuantConnect.Securities.SymbolProperties class 
             for the specified quoteCurrency
        
        
            quoteCurrency: The quote currency of the symbol
            Returns: A default instance of 
             theQuantConnect.Securities.SymbolProperties class
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, description, quoteCurrency, contractMultiplier, minimumPriceVariation, lotSize):
        """ __new__(cls: type, description: str, quoteCurrency: str, contractMultiplier: Decimal, minimumPriceVariation: Decimal, lotSize: Decimal) """
        pass

    ContractMultiplier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The contract multiplier for the security

Get: ContractMultiplier(self: SymbolProperties) -> Decimal

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The description of the security

Get: Description(self: SymbolProperties) -> str

"""

    LotSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The lot size (lot size of the order) for the security

Get: LotSize(self: SymbolProperties) -> Decimal

"""

    MinimumPriceVariation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minimum price variation (tick size) for the security

Get: MinimumPriceVariation(self: SymbolProperties) -> Decimal

"""

    QuoteCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The quote currency of the security

Get: QuoteCurrency(self: SymbolProperties) -> str

"""



class SymbolPropertiesDatabase(object):
    """ Provides access to specific properties for various symbols """
    def ContainsKey(self, market, symbol, securityType):
        """
        ContainsKey(self: SymbolPropertiesDatabase, market: str, symbol: str, securityType: SecurityType) -> bool
        
            Check whether symbol properties exists for the 
             specified market/symbol/security-type
        
        
            market: The market the exchange resides in, i.e, 'usa', 
             'fxcm', ect...
        
            symbol: The particular symbol being traded
            securityType: The security type of the symbol
        ContainsKey(self: SymbolPropertiesDatabase, market: str, symbol: Symbol, securityType: SecurityType) -> bool
        
            Check whether symbol properties exists for the 
             specified market/symbol/security-type
        
        
            market: The market the exchange resides in, i.e, 'usa', 
             'fxcm', ect...
        
            symbol: The particular symbol being traded (Symbol class)
            securityType: The security type of the symbol
        """
        pass

    @staticmethod
    def FromDataFolder():
        """
        FromDataFolder() -> SymbolPropertiesDatabase
        
            Gets the instance of the 
             QuantConnect.Securities.SymbolPropertiesDatabase 
             class produced by reading in the symbol 
             properties
                    data found in 
             /Data/symbol-properties/
        
            Returns: A 
             QuantConnect.Securities.SymbolPropertiesDatabase 
             class that represents the data in the 
             symbol-properties folder
        """
        pass

    def GetSymbolProperties(self, market, symbol, securityType, defaultQuoteCurrency):
        """
        GetSymbolProperties(self: SymbolPropertiesDatabase, market: str, symbol: str, securityType: SecurityType, defaultQuoteCurrency: str) -> SymbolProperties
        
            Gets the symbol properties for the specified 
             market/symbol/security-type
        
        
            market: The market the exchange resides in, i.e, 'usa', 
             'fxcm', ect...
        
            symbol: The particular symbol being traded
            securityType: The security type of the symbol
            defaultQuoteCurrency: Specifies the quote currency to be used when 
             returning a default instance of an entry is not 
             found in the database
        
            Returns: The symbol properties matching the specified 
             market/symbol/security-type or null if not found
        
        GetSymbolProperties(self: SymbolPropertiesDatabase, market: str, symbol: Symbol, securityType: SecurityType, defaultQuoteCurrency: str) -> SymbolProperties
        
            Gets the symbol properties for the specified 
             market/symbol/security-type
        
        
            market: The market the exchange resides in, i.e, 'usa', 
             'fxcm', ect...
        
            symbol: The particular symbol being traded (Symbol class)
            securityType: The security type of the symbol
            defaultQuoteCurrency: Specifies the quote currency to be used when 
             returning a default instance of an entry is not 
             found in the database
        
            Returns: The symbol properties matching the specified 
             market/symbol/security-type or null if not found
        """
        pass

    def TryGetMarket(self, symbol, securityType, market):
        """
        TryGetMarket(self: SymbolPropertiesDatabase, symbol: str, securityType: SecurityType) -> (bool, str)
        
            Tries to get the market for the provided 
             symbol/security type
        
        
            symbol: The particular symbol being traded
            securityType: The security type of the symbol
            Returns: True if market was retrieved, false otherwise
        """
        pass


class UniverseManager(object, IDictionary[Symbol, Universe], ICollection[KeyValuePair[Symbol, Universe]], IEnumerable[KeyValuePair[Symbol, Universe]], IEnumerable, INotifyCollectionChanged):
    """
    Manages the algorithm's collection of universes
    
    UniverseManager()
    """
    def Add(self, *__args):
        """
        Add(self: UniverseManager, item: KeyValuePair[Symbol, Universe])Add(self: UniverseManager, key: Symbol, universe: Universe)
            Adds an element with the provided key and value 
             to the System.Collections.Generic.IDictionary.
        
        
            key: The object to use as the key of the element to 
             add.
        
            universe: The object to use as the value of the element to 
             add.
        """
        pass

    def Clear(self):
        """
        Clear(self: UniverseManager)
            Removes all items from the 
             System.Collections.Generic.ICollection.
        """
        pass

    def Contains(self, item):
        """ Contains(self: UniverseManager, item: KeyValuePair[Symbol, Universe]) -> bool """
        pass

    def ContainsKey(self, key):
        """
        ContainsKey(self: UniverseManager, key: Symbol) -> bool
        
            Determines whether the 
             System.Collections.Generic.IDictionary contains 
             an element with the specified key.
        
        
            key: The key to locate in the 
             System.Collections.Generic.IDictionary.
        
            Returns: true if the 
             System.Collections.Generic.IDictionary contains 
             an element with the key; otherwise, false.
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: UniverseManager, array: Array[KeyValuePair[Symbol, Universe]], arrayIndex: int) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: UniverseManager) -> IEnumerator[KeyValuePair[Symbol, Universe]]
        
            Returns an enumerator that iterates through the 
             collection.
        
            Returns: A System.Collections.Generic.IEnumerator that can 
             be used to iterate through the collection.
        """
        pass

    def OnCollectionChanged(self, *args): #cannot find CLR method
        """
        OnCollectionChanged(self: UniverseManager, e: NotifyCollectionChangedEventArgs)
            Event invocator for the 
             QuantConnect.Securities.UniverseManager.Collection
             Changed event
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: UniverseManager, item: KeyValuePair[Symbol, Universe]) -> bool
        Remove(self: UniverseManager, key: Symbol) -> bool
        
            Removes the element with the specified key from 
             the System.Collections.Generic.IDictionary.
        
        
            key: The key of the element to remove.
            Returns: true if the element is successfully removed; 
             otherwise, false.  This method also returns false 
             if key was not found in the original 
             System.Collections.Generic.IDictionary.
        """
        pass

    def TryGetValue(self, key, value):
        """
        TryGetValue(self: UniverseManager, key: Symbol) -> (bool, Universe)
        
            Gets the value associated with the specified key.
        
            key: The key whose value to get.
            Returns: true if the object that implements 
             System.Collections.Generic.IDictionary contains 
             an element with the specified key; otherwise, 
             false.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary[Symbol, Universe], key: Symbol) -> bool """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ActiveSecurities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Read-only dictionary containing all active securities. An active security is
            a security that is currently selected by the universe or has holdings or open orders.

Get: ActiveSecurities(self: UniverseManager) -> IReadOnlyDictionary[Symbol, Security]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained in the System.Collections.Generic.ICollection.

Get: Count(self: UniverseManager) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the System.Collections.Generic.ICollection is read-only.

Get: IsReadOnly(self: UniverseManager) -> bool

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.Generic.ICollection containing the keys of the System.Collections.Generic.IDictionary.

Get: Keys(self: UniverseManager) -> ICollection[Symbol]

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.Generic.ICollection containing the values in the System.Collections.Generic.IDictionary.

Get: Values(self: UniverseManager) -> ICollection[Universe]

"""


    CollectionChanged = None


class UnsettledCashAmount(object):
    """
    Represents a pending cash amount waiting for settlement time
    
    UnsettledCashAmount(settlementTimeUtc: DateTime, currency: str, amount: Decimal)
    """
    @staticmethod # known case of __new__
    def __new__(self, settlementTimeUtc, currency, amount):
        """ __new__(cls: type, settlementTimeUtc: DateTime, currency: str, amount: Decimal) """
        pass

    Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The amount of cash

Get: Amount(self: UnsettledCashAmount) -> Decimal

"""

    Currency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The currency symbol

Get: Currency(self: UnsettledCashAmount) -> str

"""

    SettlementTimeUtc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The settlement time (in UTC)

Get: SettlementTimeUtc(self: UnsettledCashAmount) -> DateTime

"""



class VolatilityModel(object):
    """ Provides access to a null implementation for QuantConnect.Securities.IVolatilityModel """
    Null = None
    __all__ = [
        'Null',
    ]


# variables with complex values

