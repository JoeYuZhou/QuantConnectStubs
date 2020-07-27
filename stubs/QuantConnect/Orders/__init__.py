# encoding: utf-8
# module QuantConnect.Orders calls itself Orders
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class OrderProperties(object, IOrderProperties):
    """
    Contains additional properties and settings for an order
    
    OrderProperties()
    """
    def Clone(self):
        """
        Clone(self: OrderProperties) -> IOrderProperties
        
            Returns a new instance clone of this object
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    TimeInForce = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the length of time over which an order will continue working before it is cancelled

Get: TimeInForce(self: OrderProperties) -> TimeInForce

Set: TimeInForce(self: OrderProperties) = value
"""



class BitfinexOrderProperties(OrderProperties, IOrderProperties):
    """
    Contains additional properties and settings for an order submitted to Bitfinex brokerage
    
    BitfinexOrderProperties()
    """
    def Clone(self):
        """
        Clone(self: BitfinexOrderProperties) -> IOrderProperties
        
            Returns a new instance clone of this object
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Hidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The hidden order option ensures an order does not appear in the order book; thus does not influence other market participants.
            If you place a hidden order, you will always pay the taker fee. If you place a limit order that hits a hidden order, you will always pay the maker fee.

Get: Hidden(self: BitfinexOrderProperties) -> bool

Set: Hidden(self: BitfinexOrderProperties) = value
"""

    PostOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This flag will ensure the order executes only as a maker (no fee) order.
            If part of the order results in taking liquidity rather than providing,
            it will be rejected and no part of the order will execute.
            Note: this flag is only applied to Limit orders.

Get: PostOnly(self: BitfinexOrderProperties) -> bool

Set: PostOnly(self: BitfinexOrderProperties) = value
"""



class OrderRequest(object):
    """ Represents a request to submit, update, or cancel an order """
    def SetResponse(self, response, status):
        """
        SetResponse(self: OrderRequest, response: OrderResponse, status: OrderRequestStatus)
            Sets the 
             QuantConnect.Orders.OrderRequest.Response for 
             this request
        
        
            response: The response to this request
            status: The current status of this request
        """
        pass

    def ToString(self):
        """
        ToString(self: OrderRequest) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, time: DateTime, orderId: int, tag: str) """
        pass

    OrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order id the request acts on

Get: OrderId(self: OrderRequest) -> int

"""

    OrderRequestType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of this order request

Get: OrderRequestType(self: OrderRequest) -> OrderRequestType

"""

    Response = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the response for this request. If this request was never processed then this
            will equal QuantConnect.Orders.OrderResponse.Unprocessed. This value is never equal to null.

Get: Response(self: OrderRequest) -> OrderResponse

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the status of this request

Get: Status(self: OrderRequest) -> OrderRequestStatus

"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a tag for this request

Get: Tag(self: OrderRequest) -> str

"""

    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the UTC time the request was created

Get: Time(self: OrderRequest) -> DateTime

"""



class CancelOrderRequest(OrderRequest):
    """
    Defines a request to cancel an order
    
    CancelOrderRequest(time: DateTime, orderId: int, tag: str)
    """
    def ToString(self):
        """
        ToString(self: CancelOrderRequest) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, time, orderId, tag):
        """ __new__(cls: type, time: DateTime, orderId: int, tag: str) """
        pass

    OrderRequestType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets QuantConnect.Orders.OrderRequestType.Cancel

Get: OrderRequestType(self: CancelOrderRequest) -> OrderRequestType

"""



class GDAXOrderProperties(OrderProperties, IOrderProperties):
    """
    Contains additional properties and settings for an order submitted to GDAX brokerage
    
    GDAXOrderProperties()
    """
    def Clone(self):
        """
        Clone(self: GDAXOrderProperties) -> IOrderProperties
        
            Returns a new instance clone of this object
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    PostOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This flag will ensure the order executes only as a maker (no fee) order.
            If part of the order results in taking liquidity rather than providing,
            it will be rejected and no part of the order will execute.
            Note: this flag is only applied to Limit orders.

Get: PostOnly(self: GDAXOrderProperties) -> bool

Set: PostOnly(self: GDAXOrderProperties) = value
"""



class InteractiveBrokersOrderProperties(OrderProperties, IOrderProperties):
    """
    Contains additional properties and settings for an order submitted to Interactive Brokers
    
    InteractiveBrokersOrderProperties()
    """
    def Clone(self):
        """
        Clone(self: InteractiveBrokersOrderProperties) -> IOrderProperties
        
            Returns a new instance clone of this object
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Account = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The linked account for which to submit the order (only used by Financial Advisors)

Get: Account(self: InteractiveBrokersOrderProperties) -> str

Set: Account(self: InteractiveBrokersOrderProperties) = value
"""

    FaGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The account group for the order (only used by Financial Advisors)

Get: FaGroup(self: InteractiveBrokersOrderProperties) -> str

Set: FaGroup(self: InteractiveBrokersOrderProperties) = value
"""

    FaMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The allocation method for the account group order (only used by Financial Advisors)
            Supported allocation methods are: EqualQuantity, NetLiq, AvailableEquity, PctChange

Get: FaMethod(self: InteractiveBrokersOrderProperties) -> str

Set: FaMethod(self: InteractiveBrokersOrderProperties) = value
"""

    FaPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The percentage for the percent change method (only used by Financial Advisors)

Get: FaPercentage(self: InteractiveBrokersOrderProperties) -> int

Set: FaPercentage(self: InteractiveBrokersOrderProperties) = value
"""

    FaProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The allocation profile to be used for the order (only used by Financial Advisors)

Get: FaProfile(self: InteractiveBrokersOrderProperties) -> str

Set: FaProfile(self: InteractiveBrokersOrderProperties) = value
"""



class Order(object):
    """ Order struct for placing new trade """
    def ApplyUpdateOrderRequest(self, request):
        """
        ApplyUpdateOrderRequest(self: Order, request: UpdateOrderRequest)
            Modifies the state of this order to match the 
             update request
        
        
            request: The request to update this order object
        """
        pass

    def Clone(self):
        """
        Clone(self: Order) -> Order
        
            Creates a deep-copy clone of this order
            Returns: A copy of this order
        """
        pass

    def CopyTo(self, *args): #cannot find CLR method
        """
        CopyTo(self: Order, order: Order)
            Copies base Order properties to the specified 
             order
        
        
            order: The target of the copy
        """
        pass

    @staticmethod
    def CreateOrder(request):
        """
        CreateOrder(request: SubmitOrderRequest) -> Order
        
            Creates an QuantConnect.Orders.Order to match the 
             specified request
        
        
            request: The QuantConnect.Orders.SubmitOrderRequest to 
             create an order for
        
            Returns: The QuantConnect.Orders.Order that matches the 
             request
        """
        pass

    @staticmethod
    def FromSerialized(serializedOrder):
        """
        FromSerialized(serializedOrder: SerializedOrder) -> Order
        
            Creates a new Order instance from a 
             SerializedOrder instance
        """
        pass

    def GetValue(self, security):
        """
        GetValue(self: Order, security: Security) -> Decimal
        
            Gets the value of this order at the given market 
             price in units of the account currency
                  
               NOTE: Some order types derive value from other 
             parameters, such as limit prices
        
        
            security: The security matching this order's symbol
            Returns: The value of this order given the current market 
             price
        """
        pass

    def GetValueImpl(self, *args): #cannot find CLR method
        """
        GetValueImpl(self: Order, security: Security) -> Decimal
        
            Gets the order value in units of the security's 
             quote currency for a single unit.
                    A 
             single unit here is a single share of stock, or a 
             single barrel of oil, or the
                    cost of 
             a single share in an option contract.
        
        
            security: The security matching this order's symbol
        """
        pass

    def ToString(self):
        """
        ToString(self: Order) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
        """
        pass

    AbsoluteQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the absolute quantity for this order

Get: AbsoluteQuantity(self: Order) -> Decimal

"""

    BrokerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Brokerage Id for this order for when the brokerage splits orders into multiple pieces

Get: BrokerId(self: Order) -> List[str]

"""

    CanceledTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the utc time this order was canceled, or null if the order was not canceled.

Get: CanceledTime(self: Order) -> Nullable[DateTime]

"""

    ContingentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Order id to process before processing this order.

Get: ContingentId(self: Order) -> int

"""

    CreatedTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the utc time this order was created. Alias for QuantConnect.Orders.Order.Time

Get: CreatedTime(self: Order) -> DateTime

"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Order Direction Property based off Quantity.

Get: Direction(self: Order) -> OrderDirection

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Order ID.

Get: Id(self: Order) -> int

"""

    IsMarketable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the order is a marketable order.

Get: IsMarketable(self: Order) -> bool

"""

    LastFillTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the utc time the last fill was received, or null if no fills have been received

Get: LastFillTime(self: Order) -> Nullable[DateTime]

"""

    LastUpdateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the utc time this order was last updated, or null if the order has not been updated.

Get: LastUpdateTime(self: Order) -> Nullable[DateTime]

"""

    OrderSubmissionData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the price data at the time the order was submitted

Get: OrderSubmissionData(self: Order) -> OrderSubmissionData

"""

    Price = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Price of the Order.

Get: Price(self: Order) -> Decimal

"""

    PriceCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Currency for the order price

Get: PriceCurrency(self: Order) -> str

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Additional properties of the order

Get: Properties(self: Order) -> IOrderProperties

"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of shares to execute.

Get: Quantity(self: Order) -> Decimal

"""

    SecurityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The symbol's security type

Get: SecurityType(self: Order) -> SecurityType

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Status of the Order

Get: Status(self: Order) -> OrderStatus

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Symbol of the Asset

Get: Symbol(self: Order) -> Symbol

"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tag the order with some custom data

Get: Tag(self: Order) -> str

"""

    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the utc time the order was created.

Get: Time(self: Order) -> DateTime

"""

    TimeInForce = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Order Time In Force

Get: TimeInForce(self: Order) -> TimeInForce

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Order Type

Get: Type(self: Order) -> OrderType

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the executed value of this order. If the order has not yet filled,
            then this will return zero.

Get: Value(self: Order) -> Decimal

"""



class LimitOrder(Order):
    """
    Limit order type definition
    
    LimitOrder()
    LimitOrder(symbol: Symbol, quantity: Decimal, limitPrice: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def ApplyUpdateOrderRequest(self, request):
        """
        ApplyUpdateOrderRequest(self: LimitOrder, request: UpdateOrderRequest)
            Modifies the state of this order to match the 
             update request
        
        
            request: The request to update this order object
        """
        pass

    def Clone(self):
        """
        Clone(self: LimitOrder) -> Order
        
            Creates a deep-copy clone of this order
            Returns: A copy of this order
        """
        pass

    def ToString(self):
        """
        ToString(self: LimitOrder) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol=None, quantity=None, limitPrice=None, time=None, tag=None, properties=None):
        """
        __new__(cls: type)
        __new__(cls: type, symbol: Symbol, quantity: Decimal, limitPrice: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
        """
        pass

    LimitPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Limit price for this order.

Get: LimitPrice(self: LimitOrder) -> Decimal

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Limit Order Type

Get: Type(self: LimitOrder) -> OrderType

"""



class MarketOnCloseOrder(Order):
    """
    Market on close order type - submits a market order on exchange close
    
    MarketOnCloseOrder()
    MarketOnCloseOrder(symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def Clone(self):
        """
        Clone(self: MarketOnCloseOrder) -> Order
        
            Creates a deep-copy clone of this order
            Returns: A copy of this order
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol=None, quantity=None, time=None, tag=None, properties=None):
        """
        __new__(cls: type)
        __new__(cls: type, symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """MarketOnClose Order Type

Get: Type(self: MarketOnCloseOrder) -> OrderType

"""


    DefaultSubmissionTimeBuffer = None


class MarketOnOpenOrder(Order):
    """
    Market on Open order type, submits a market order when the exchange opens
    
    MarketOnOpenOrder()
    MarketOnOpenOrder(symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def Clone(self):
        """
        Clone(self: MarketOnOpenOrder) -> Order
        
            Creates a deep-copy clone of this order
            Returns: A copy of this order
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol=None, quantity=None, time=None, tag=None, properties=None):
        """
        __new__(cls: type)
        __new__(cls: type, symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """MarketOnOpen Order Type

Get: Type(self: MarketOnOpenOrder) -> OrderType

"""



class MarketOrder(Order):
    """
    Market order type definition
    
    MarketOrder()
    MarketOrder(symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def Clone(self):
        """
        Clone(self: MarketOrder) -> Order
        
            Creates a deep-copy clone of this order
            Returns: A copy of this order
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol=None, quantity=None, time=None, tag=None, properties=None):
        """
        __new__(cls: type)
        __new__(cls: type, symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Market Order Type

Get: Type(self: MarketOrder) -> OrderType

"""



class OptionExerciseOrder(Order):
    """
    Option exercise order type definition
    
    OptionExerciseOrder()
    OptionExerciseOrder(symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def Clone(self):
        """
        Clone(self: OptionExerciseOrder) -> Order
        
            Creates a deep-copy clone of this order
            Returns: A copy of this order
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol=None, quantity=None, time=None, tag=None, properties=None):
        """
        __new__(cls: type)
        __new__(cls: type, symbol: Symbol, quantity: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Option Exercise Order Type

Get: Type(self: OptionExerciseOrder) -> OrderType

"""



class OrderDirection(Enum, IComparable, IFormattable, IConvertible):
    """
    Direction of the order
    
    enum OrderDirection, values: Buy (0), Hold (2), Sell (1)
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

    Buy = None
    Hold = None
    Sell = None
    value__ = None


class OrderError(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the possible error states during presubmission checks
    
    enum OrderError, values: CanNotUpdateFilledOrder (-8), GeneralError (-7), InsufficientCapital (-4), MarketClosed (-3), MaxOrdersExceeded (-5), NoData (-2), None (0), TimestampError (-6), ZeroQuantity (-1)
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

    CanNotUpdateFilledOrder = None
    GeneralError = None
    InsufficientCapital = None
    MarketClosed = None
    MaxOrdersExceeded = None
    NoData = None
    None = None
    TimestampError = None
    value__ = None
    ZeroQuantity = None


class OrderEvent(object):
    """
    Order Event - Messaging class signifying a change in an order state and record the change in the user's algorithm portfolio
    
    OrderEvent()
    OrderEvent(orderId: int, symbol: Symbol, utcTime: DateTime, status: OrderStatus, direction: OrderDirection, fillPrice: Decimal, fillQuantity: Decimal, orderFee: OrderFee, message: str)
    OrderEvent(order: Order, utcTime: DateTime, orderFee: OrderFee, message: str)
    """
    def Clone(self):
        """
        Clone(self: OrderEvent) -> OrderEvent
        
            Returns a clone of the current object.
            Returns: The new clone object
        """
        pass

    @staticmethod
    def FromSerialized(serializedOrderEvent):
        """
        FromSerialized(serializedOrderEvent: SerializedOrderEvent) -> OrderEvent
        
            Creates a new instance based on the provided 
             serialized order event
        """
        pass

    def ToString(self):
        """
        ToString(self: OrderEvent) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, orderId: int, symbol: Symbol, utcTime: DateTime, status: OrderStatus, direction: OrderDirection, fillPrice: Decimal, fillQuantity: Decimal, orderFee: OrderFee, message: str)
        __new__(cls: type, order: Order, utcTime: DateTime, orderFee: OrderFee, message: str)
        """
        pass

    AbsoluteFillQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Public Property Absolute Getter of Quantity -Filled

Get: AbsoluteFillQuantity(self: OrderEvent) -> Decimal

"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Order direction.

Get: Direction(self: OrderEvent) -> OrderDirection

Set: Direction(self: OrderEvent) = value
"""

    FillPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fill price information about the order

Get: FillPrice(self: OrderEvent) -> Decimal

Set: FillPrice(self: OrderEvent) = value
"""

    FillPriceCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Currency for the fill price

Get: FillPriceCurrency(self: OrderEvent) -> str

Set: FillPriceCurrency(self: OrderEvent) = value
"""

    FillQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of shares of the order that was filled in this event.

Get: FillQuantity(self: OrderEvent) -> Decimal

Set: FillQuantity(self: OrderEvent) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique order event id for each order

Get: Id(self: OrderEvent) -> int

Set: Id(self: OrderEvent) = value
"""

    IsAssignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the order event is an assignment

Get: IsAssignment(self: OrderEvent) -> bool

Set: IsAssignment(self: OrderEvent) = value
"""

    LimitPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current limit price

Get: LimitPrice(self: OrderEvent) -> Nullable[Decimal]

Set: LimitPrice(self: OrderEvent) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Any message from the exchange.

Get: Message(self: OrderEvent) -> str

Set: Message(self: OrderEvent) = value
"""

    OrderFee = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fee associated with the order

Get: OrderFee(self: OrderEvent) -> OrderFee

Set: OrderFee(self: OrderEvent) = value
"""

    OrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Id of the order this event comes from.

Get: OrderId(self: OrderEvent) -> int

Set: OrderId(self: OrderEvent) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current order quantity

Get: Quantity(self: OrderEvent) -> Decimal

Set: Quantity(self: OrderEvent) = value
"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Status message of the order.

Get: Status(self: OrderEvent) -> OrderStatus

Set: Status(self: OrderEvent) = value
"""

    StopPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current stop price

Get: StopPrice(self: OrderEvent) -> Nullable[Decimal]

Set: StopPrice(self: OrderEvent) = value
"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Easy access to the order symbol associated with this event.

Get: Symbol(self: OrderEvent) -> Symbol

Set: Symbol(self: OrderEvent) = value
"""

    UtcTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The date and time of this event (UTC).

Get: UtcTime(self: OrderEvent) -> DateTime

Set: UtcTime(self: OrderEvent) = value
"""



class OrderExtensions(object):
    """ Provides extension methods for the QuantConnect.Orders.Order class and for the QuantConnect.Orders.OrderStatus enumeration """
    @staticmethod
    def IsClosed(status):
        """
        IsClosed(status: OrderStatus) -> bool
        
            Determines if the specified status is in a closed 
             state.
        
        
            status: The status to check
            Returns: True if the status is 
             QuantConnect.Orders.OrderStatus.Filled, 
             QuantConnect.Orders.OrderStatus.Canceled, or 
             QuantConnect.Orders.OrderStatus.Invalid
        """
        pass

    @staticmethod
    def IsFill(status):
        """
        IsFill(status: OrderStatus) -> bool
        
            Determines if the specified status is a fill, 
             that is, QuantConnect.Orders.OrderStatus.Filled
         
                        order 
             QuantConnect.Orders.OrderStatus.PartiallyFilled
        
        
            status: The status to check
            Returns: True if the status is 
             QuantConnect.Orders.OrderStatus.Filled or 
             QuantConnect.Orders.OrderStatus.PartiallyFilled, 
             false otherwise
        """
        pass

    @staticmethod
    def IsLimitOrder(orderType):
        """
        IsLimitOrder(orderType: OrderType) -> bool
        
            Determines whether or not the specified order is 
             a limit order
        
        
            orderType: The order to check
            Returns: True if the order is a limit order, false 
             otherwise
        """
        pass

    @staticmethod
    def IsOpen(status):
        """
        IsOpen(status: OrderStatus) -> bool
        
            Determines if the specified status is in an open 
             state.
        
        
            status: The status to check
            Returns: True if the status is not 
             QuantConnect.Orders.OrderStatus.Filled, 
             QuantConnect.Orders.OrderStatus.Canceled, or 
             QuantConnect.Orders.OrderStatus.Invalid
        """
        pass

    @staticmethod
    def IsStopOrder(orderType):
        """
        IsStopOrder(orderType: OrderType) -> bool
        
            Determines whether or not the specified order is 
             a stop order
        
        
            orderType: The order to check
            Returns: True if the order is a stop order, false otherwise
        """
        pass

    __all__ = [
        'IsClosed',
        'IsFill',
        'IsLimitOrder',
        'IsOpen',
        'IsStopOrder',
    ]


class OrderField(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies an order field that does not apply to all order types
    
    enum OrderField, values: LimitPrice (0), StopPrice (1)
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

    LimitPrice = None
    StopPrice = None
    value__ = None


class OrderJsonConverter(JsonConverter):
    """
    Provides an implementation of Newtonsoft.Json.JsonConverter that can deserialize Orders
    
    OrderJsonConverter()
    """
    def CanConvert(self, objectType):
        """
        CanConvert(self: OrderJsonConverter, objectType: Type) -> bool
        
            Determines whether this instance can convert the 
             specified object type.
        
        
            objectType: Type of the object.
            Returns: true if this instance can convert the specified 
             object type; otherwise, false.
        """
        pass

    @staticmethod
    def CreateOrderFromJObject(jObject):
        """
        CreateOrderFromJObject(jObject: JObject) -> Order
        
            Create an order from a simple JObject
            Returns: Order Object
        """
        pass

    def ReadJson(self, reader, objectType, existingValue, serializer):
        """
        ReadJson(self: OrderJsonConverter, reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object
        
            Reads the JSON representation of the object.
        
            reader: The Newtonsoft.Json.JsonReader to read from.
            objectType: Type of the object.
            existingValue: The existing value of object being read.
            serializer: The calling serializer.
            Returns: The object value.
        """
        pass

    def WriteJson(self, writer, value, serializer):
        """
        WriteJson(self: OrderJsonConverter, writer: JsonWriter, value: object, serializer: JsonSerializer)
            Writes the JSON representation of the object.
        
            writer: The Newtonsoft.Json.JsonWriter to write to.
            value: The value.
            serializer: The calling serializer.
        """
        pass

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this Newtonsoft.Json.JsonConverter can write JSON.

Get: CanWrite(self: OrderJsonConverter) -> bool

"""



class OrderRequestStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the status of a request
    
    enum OrderRequestStatus, values: Error (3), Processed (2), Processing (1), Unprocessed (0)
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

    Error = None
    Processed = None
    Processing = None
    Unprocessed = None
    value__ = None


class OrderRequestType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of QuantConnect.Orders.OrderRequest
    
    enum OrderRequestType, values: Cancel (2), Submit (0), Update (1)
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

    Cancel = None
    Submit = None
    Update = None
    value__ = None


class OrderResponse(object):
    """
    Represents a response to an QuantConnect.Orders.OrderRequest. See QuantConnect.Orders.OrderRequest.Response property for
                a specific request's response value
    """
    @staticmethod
    def Error(request, errorCode, errorMessage):
        """
        Error(request: OrderRequest, errorCode: OrderResponseErrorCode, errorMessage: str) -> OrderResponse
        
            Helper method to create an error response from a 
             request
        """
        pass

    @staticmethod
    def InvalidStatus(request, order):
        """
        InvalidStatus(request: OrderRequest, order: Order) -> OrderResponse
        
            Helper method to create an error response due to 
             an invalid order status
        """
        pass

    @staticmethod
    def Success(request):
        """
        Success(request: OrderRequest) -> OrderResponse
        
            Helper method to create a successful response 
             from a request
        """
        pass

    def ToString(self):
        """
        ToString(self: OrderResponse) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod
    def UnableToFindOrder(request):
        """
        UnableToFindOrder(request: OrderRequest) -> OrderResponse
        
            Helper method to create an error response due to 
             a bad order id
        """
        pass

    @staticmethod
    def WarmingUp(request):
        """
        WarmingUp(request: OrderRequest) -> OrderResponse
        
            Helper method to create an error response due to 
             algorithm still in warmup mode
        """
        pass

    @staticmethod
    def ZeroQuantity(request):
        """
        ZeroQuantity(request: OrderRequest) -> OrderResponse
        
            Helper method to create an error response due to 
             a zero order quantity
        """
        pass

    ErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error code for this response.

Get: ErrorCode(self: OrderResponse) -> OrderResponseErrorCode

"""

    ErrorMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the error message if the QuantConnect.Orders.OrderResponse.ErrorCode does not equal QuantConnect.Orders.OrderResponseErrorCode.None, otherwise
            gets System.String.Empty

Get: ErrorMessage(self: OrderResponse) -> str

"""

    IsError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets true if this response represents an error, false otherwise

Get: IsError(self: OrderResponse) -> bool

"""

    IsProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets true if this response has been processed, false otherwise

Get: IsProcessed(self: OrderResponse) -> bool

"""

    IsSuccess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets true if this response represents a successful request, false otherwise
            If this is an unprocessed response, IsSuccess will return false.

Get: IsSuccess(self: OrderResponse) -> bool

"""

    OrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order id

Get: OrderId(self: OrderResponse) -> int

"""


    Unprocessed = None


class OrderResponseErrorCode(Enum, IComparable, IFormattable, IConvertible):
    """
    Error detail code
    
    enum OrderResponseErrorCode, values: AlgorithmWarmingUp (-24), BrokerageFailedToCancelOrder (-8), BrokerageFailedToSubmitOrder (-5), BrokerageFailedToUpdateOrder (-6), BrokerageHandlerRefusedToUpdateOrder (-7), BrokerageModelRefusedToSubmitOrder (-4), BrokerageModelRefusedToUpdateOrder (-25), ConversionRateZero (-27), ExceededMaximumOrders (-20), ExchangeNotOpen (-15), ForexBaseAndQuoteCurrenciesRequired (-17), ForexConversionRateZero (-18), InsufficientBuyingPower (-3), InvalidOrderStatus (-9), InvalidRequest (-22), MarketOnCloseOrderTooLate (-21), MissingSecurity (-14), None (0), NonExercisableSecurity (-29), NonTradableSecurity (-28), OrderAlreadyExists (-2), OrderQuantityLessThanLoteSize (-30), OrderQuantityZero (-11), PreOrderChecksError (-13), ProcessingError (-1), QuoteCurrencyRequired (-26), RequestCanceled (-23), SecurityHasNoData (-19), SecurityPriceZero (-16), UnableToFindOrder (-10), UnsupportedRequestType (-12)
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

    AlgorithmWarmingUp = None
    BrokerageFailedToCancelOrder = None
    BrokerageFailedToSubmitOrder = None
    BrokerageFailedToUpdateOrder = None
    BrokerageHandlerRefusedToUpdateOrder = None
    BrokerageModelRefusedToSubmitOrder = None
    BrokerageModelRefusedToUpdateOrder = None
    ConversionRateZero = None
    ExceededMaximumOrders = None
    ExchangeNotOpen = None
    ForexBaseAndQuoteCurrenciesRequired = None
    ForexConversionRateZero = None
    InsufficientBuyingPower = None
    InvalidOrderStatus = None
    InvalidRequest = None
    MarketOnCloseOrderTooLate = None
    MissingSecurity = None
    None = None
    NonExercisableSecurity = None
    NonTradableSecurity = None
    OrderAlreadyExists = None
    OrderQuantityLessThanLoteSize = None
    OrderQuantityZero = None
    PreOrderChecksError = None
    ProcessingError = None
    QuoteCurrencyRequired = None
    RequestCanceled = None
    SecurityHasNoData = None
    SecurityPriceZero = None
    UnableToFindOrder = None
    UnsupportedRequestType = None
    value__ = None


class OrderSizing(object):
    """ Provides methods for computing a maximum order size. """
    @staticmethod
    def AdjustByLotSize(security, quantity):
        """
        AdjustByLotSize(security: Security, quantity: Decimal) -> Decimal
        
            Adjusts the provided order quantity to respect 
             the securities lot size.
                    If the 
             quantity is missing 1M part of the lot size it 
             will be rounded up
                    since we suppose 
             it's due to floating point error, this is 
             required to avoid diff
                    between Py 
             and C#
        
        
            security: The security instance
            quantity: The desired quantity to adjust, can be signed
            Returns: The signed adjusted quantity
        """
        pass

    @staticmethod
    def GetOrderSizeForMaximumValue(security, maximumOrderValueInAccountCurrency, desiredOrderSize):
        """
        GetOrderSizeForMaximumValue(security: Security, maximumOrderValueInAccountCurrency: Decimal, desiredOrderSize: Decimal) -> Decimal
        
            Adjust the provided order size to respect the 
             maximum total order value
        
        
            security: The security object
            maximumOrderValueInAccountCurrency: The maximum order value in units of the account 
             currency
        
            desiredOrderSize: The desired order size to adjust
            Returns: The signed adjusted order size
        """
        pass

    @staticmethod
    def GetOrderSizeForPercentVolume(security, maximumPercentCurrentVolume, desiredOrderSize):
        """
        GetOrderSizeForPercentVolume(security: Security, maximumPercentCurrentVolume: Decimal, desiredOrderSize: Decimal) -> Decimal
        
            Adjust the provided order size to respect maximum 
             order size based on a percentage of current 
             volume.
        
        
            security: The security object
            maximumPercentCurrentVolume: The maximum percentage of the current bar's volume
            desiredOrderSize: The desired order size to adjust
            Returns: The signed adjusted order size
        """
        pass

    @staticmethod
    def GetUnorderedQuantity(algorithm, target):
        """
        GetUnorderedQuantity(algorithm: IAlgorithm, target: IPortfolioTarget) -> Decimal
        
            Gets the remaining quantity to be ordered to 
             reach the specified target quantity.
        
        
            algorithm: The algorithm instance
            target: The portfolio target
            Returns: The signed remaining quantity to be ordered
        """
        pass

    __all__ = [
        'AdjustByLotSize',
        'GetOrderSizeForMaximumValue',
        'GetOrderSizeForPercentVolume',
        'GetUnorderedQuantity',
    ]


class OrderStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    Fill status of the order class.
    
    enum OrderStatus, values: Canceled (5), CancelPending (8), Filled (3), Invalid (7), New (0), None (6), PartiallyFilled (2), Submitted (1), UpdateSubmitted (9)
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

    Canceled = None
    CancelPending = None
    Filled = None
    Invalid = None
    New = None
    None = None
    PartiallyFilled = None
    Submitted = None
    UpdateSubmitted = None
    value__ = None


class OrderSubmissionData(object):
    """
    The purpose of this class is to store time and price information
                available at the time an order was submitted.
    
    OrderSubmissionData(bidPrice: Decimal, askPrice: Decimal, lastPrice: Decimal)
    """
    def Clone(self):
        """
        Clone(self: OrderSubmissionData) -> OrderSubmissionData
        
            Return a new instance clone of this object
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, bidPrice, askPrice, lastPrice):
        """ __new__(cls: type, bidPrice: Decimal, askPrice: Decimal, lastPrice: Decimal) """
        pass

    AskPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ask price at order submission time

Get: AskPrice(self: OrderSubmissionData) -> Decimal

"""

    BidPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bid price at order submission time

Get: BidPrice(self: OrderSubmissionData) -> Decimal

"""

    LastPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current price at order submission time

Get: LastPrice(self: OrderSubmissionData) -> Decimal

"""



class OrderTicket(object):
    """
    Provides a single reference to an order for the algorithm to maintain. As the order gets
                updated this ticket will also get updated
    
    OrderTicket(transactionManager: SecurityTransactionManager, submitRequest: SubmitOrderRequest)
    """
    def Cancel(self, tag):
        """
        Cancel(self: OrderTicket, tag: str) -> OrderResponse
        
            Submits a new request to cancel this order
        """
        pass

    def Get(self, field):
        """
        Get(self: OrderTicket, field: OrderField) -> Decimal
        
            Gets the specified field from the ticket
        
            field: The order field to get
            Returns: The value of the field
        """
        pass

    def GetMostRecentOrderRequest(self):
        """
        GetMostRecentOrderRequest(self: OrderTicket) -> OrderRequest
        
            Gets the most recent 
             QuantConnect.Orders.OrderRequest for this ticket
        
            Returns: The most recent QuantConnect.Orders.OrderRequest 
             for this ticket
        """
        pass

    def GetMostRecentOrderResponse(self):
        """
        GetMostRecentOrderResponse(self: OrderTicket) -> OrderResponse
        
            Gets the most recent 
             QuantConnect.Orders.OrderResponse for this ticket
        
            Returns: The most recent QuantConnect.Orders.OrderResponse 
             for this ticket
        """
        pass

    @staticmethod
    def InvalidCancelOrderId(transactionManager, request):
        """
        InvalidCancelOrderId(transactionManager: SecurityTransactionManager, request: CancelOrderRequest) -> OrderTicket
        
            Creates a new QuantConnect.Orders.OrderTicket 
             that represents trying to cancel an order for 
             which no ticket exists
        """
        pass

    @staticmethod
    def InvalidSubmitRequest(transactionManager, request, response):
        """
        InvalidSubmitRequest(transactionManager: SecurityTransactionManager, request: SubmitOrderRequest, response: OrderResponse) -> OrderTicket
        
            Creates a new QuantConnect.Orders.OrderTicket 
             that represents trying to submit a new order that 
             had errors embodied in the response
        """
        pass

    @staticmethod
    def InvalidUpdateOrderId(transactionManager, request):
        """
        InvalidUpdateOrderId(transactionManager: SecurityTransactionManager, request: UpdateOrderRequest) -> OrderTicket
        
            Creates a new QuantConnect.Orders.OrderTicket 
             that represents trying to update an order for 
             which no ticket exists
        """
        pass

    @staticmethod
    def InvalidWarmingUp(transactionManager, submit):
        """
        InvalidWarmingUp(transactionManager: SecurityTransactionManager, submit: SubmitOrderRequest) -> OrderTicket
        
            Creates a new QuantConnect.Orders.OrderTicket 
             that is invalidated because the algorithm was in 
             the middle of warm up still
        """
        pass

    def ToString(self):
        """
        ToString(self: OrderTicket) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    def Update(self, fields):
        """
        Update(self: OrderTicket, fields: UpdateOrderFields) -> OrderResponse
        
            Submits an QuantConnect.Orders.UpdateOrderRequest 
             with the 
             QuantConnect.Securities.SecurityTransactionManager
              to update
                    the ticket with data 
             specified in fields
        
        
            fields: Defines what properties of the order should be 
             updated
        
            Returns: The QuantConnect.Orders.OrderResponse from 
             updating the order
        """
        pass

    def UpdateLimitPrice(self, limitPrice, tag):
        """
        UpdateLimitPrice(self: OrderTicket, limitPrice: Decimal, tag: str) -> OrderResponse
        
            Submits an QuantConnect.Orders.UpdateOrderRequest 
             with the 
             QuantConnect.Securities.SecurityTransactionManager
              to update
                    the ticker with 
             limitprice specified in limitPrice and with tag 
             specified in quantity
        
            Returns: QuantConnect.Orders.OrderResponse from updating 
             the order
        """
        pass

    def UpdateQuantity(self, quantity, tag):
        """
        UpdateQuantity(self: OrderTicket, quantity: Decimal, tag: str) -> OrderResponse
        
            Submits an QuantConnect.Orders.UpdateOrderRequest 
             with the 
             QuantConnect.Securities.SecurityTransactionManager
              to update
                    the ticket with quantity 
             specified in quantity and with tag specified in 
             quantity
        
            Returns: QuantConnect.Orders.OrderResponse from updating 
             the order
        """
        pass

    def UpdateStopPrice(self, stopPrice, tag):
        """
        UpdateStopPrice(self: OrderTicket, stopPrice: Decimal, tag: str) -> OrderResponse
        
            Submits an QuantConnect.Orders.UpdateOrderRequest 
             with the 
             QuantConnect.Securities.SecurityTransactionManager
              to update
                    the ticker with stopprice 
             specified in stopPrice and with tag specified in 
             quantity
        
            Returns: QuantConnect.Orders.OrderResponse from updating 
             the order
        """
        pass

    def UpdateTag(self, tag):
        """
        UpdateTag(self: OrderTicket, tag: str) -> OrderResponse
        
            Submits an QuantConnect.Orders.UpdateOrderRequest 
             with the 
             QuantConnect.Securities.SecurityTransactionManager
              to update
                    the ticket with tag 
             specified in tag
        
            Returns: QuantConnect.Orders.OrderResponse from updating 
             the order
        """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(ticket: OrderTicket) -> int """
        pass

    def __long__(self, *args): #cannot find CLR method
        """ __int__(ticket: OrderTicket) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, transactionManager, submitRequest):
        """ __new__(cls: type, transactionManager: SecurityTransactionManager, submitRequest: SubmitOrderRequest) """
        pass

    AverageFillPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the average fill price for this ticket. If no fills have been processed
            then this will return a value of zero.

Get: AverageFillPrice(self: OrderTicket) -> Decimal

"""

    CancelRequest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the QuantConnect.Orders.CancelOrderRequest if this order was canceled. If this order
            was not canceled, this will return null

Get: CancelRequest(self: OrderTicket) -> CancelOrderRequest

"""

    HasOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the order has been set for this ticket

Get: HasOrder(self: OrderTicket) -> bool

"""

    OrderClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a wait handle that can be used to wait until this order has filled

Get: OrderClosed(self: OrderTicket) -> WaitHandle

"""

    OrderEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a list of all order events for this ticket

Get: OrderEvents(self: OrderTicket) -> IReadOnlyList[OrderEvent]

"""

    OrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order id of this ticket

Get: OrderId(self: OrderTicket) -> int

"""

    OrderSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a wait handle that can be used to wait until the order has been set

Get: OrderSet(self: OrderTicket) -> WaitHandle

"""

    OrderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of order

Get: OrderType(self: OrderTicket) -> OrderType

"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of units ordered

Get: Quantity(self: OrderTicket) -> Decimal

"""

    QuantityFilled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total qantity filled for this ticket. If no fills have been processed
            then this will return a value of zero.

Get: QuantityFilled(self: OrderTicket) -> Decimal

"""

    SecurityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the QuantConnect.Orders.OrderTicket.Symbol's QuantConnect.Orders.OrderTicket.SecurityType

Get: SecurityType(self: OrderTicket) -> SecurityType

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current status of this order ticket

Get: Status(self: OrderTicket) -> OrderStatus

"""

    SubmitRequest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the QuantConnect.Orders.SubmitOrderRequest that initiated this order

Get: SubmitRequest(self: OrderTicket) -> SubmitOrderRequest

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the symbol being ordered

Get: Symbol(self: OrderTicket) -> Symbol

"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order's current tag

Get: Tag(self: OrderTicket) -> str

"""

    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the time this order was last updated

Get: Time(self: OrderTicket) -> DateTime

"""

    UpdateRequests = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a list of QuantConnect.Orders.UpdateOrderRequest containing an item for each
            QuantConnect.Orders.UpdateOrderRequest that was sent for this order id

Get: UpdateRequests(self: OrderTicket) -> IReadOnlyList[UpdateOrderRequest]

"""



class OrderType(Enum, IComparable, IFormattable, IConvertible):
    """
    Type of the order: market, limit or stop
    
    enum OrderType, values: Limit (1), Market (0), MarketOnClose (5), MarketOnOpen (4), OptionExercise (6), StopLimit (3), StopMarket (2)
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

    Limit = None
    Market = None
    MarketOnClose = None
    MarketOnOpen = None
    OptionExercise = None
    StopLimit = None
    StopMarket = None
    value__ = None


class StopLimitOrder(Order):
    """
    Stop Market Order Type Definition
    
    StopLimitOrder()
    StopLimitOrder(symbol: Symbol, quantity: Decimal, stopPrice: Decimal, limitPrice: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def ApplyUpdateOrderRequest(self, request):
        """
        ApplyUpdateOrderRequest(self: StopLimitOrder, request: UpdateOrderRequest)
            Modifies the state of this order to match the 
             update request
        
        
            request: The request to update this order object
        """
        pass

    def Clone(self):
        """
        Clone(self: StopLimitOrder) -> Order
        
            Creates a deep-copy clone of this order
            Returns: A copy of this order
        """
        pass

    def ToString(self):
        """
        ToString(self: StopLimitOrder) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol=None, quantity=None, stopPrice=None, limitPrice=None, time=None, tag=None, properties=None):
        """
        __new__(cls: type)
        __new__(cls: type, symbol: Symbol, quantity: Decimal, stopPrice: Decimal, limitPrice: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
        """
        pass

    LimitPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Limit price for the stop limit order

Get: LimitPrice(self: StopLimitOrder) -> Decimal

"""

    StopPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Stop price for this stop market order.

Get: StopPrice(self: StopLimitOrder) -> Decimal

"""

    StopTriggered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Signal showing the "StopLimitOrder" has been converted into a Limit Order

Get: StopTriggered(self: StopLimitOrder) -> bool

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """StopLimit Order Type

Get: Type(self: StopLimitOrder) -> OrderType

"""



class StopMarketOrder(Order):
    """
    Stop Market Order Type Definition
    
    StopMarketOrder()
    StopMarketOrder(symbol: Symbol, quantity: Decimal, stopPrice: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def ApplyUpdateOrderRequest(self, request):
        """
        ApplyUpdateOrderRequest(self: StopMarketOrder, request: UpdateOrderRequest)
            Modifies the state of this order to match the 
             update request
        
        
            request: The request to update this order object
        """
        pass

    def Clone(self):
        """
        Clone(self: StopMarketOrder) -> Order
        
            Creates a deep-copy clone of this order
            Returns: A copy of this order
        """
        pass

    def ToString(self):
        """
        ToString(self: StopMarketOrder) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol=None, quantity=None, stopPrice=None, time=None, tag=None, properties=None):
        """
        __new__(cls: type)
        __new__(cls: type, symbol: Symbol, quantity: Decimal, stopPrice: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """StopMarket Order Type

Get: Type(self: StopMarketOrder) -> OrderType

"""


    StopPrice = None


class SubmitOrderRequest(OrderRequest):
    """
    Defines a request to submit a new order
    
    SubmitOrderRequest(orderType: OrderType, securityType: SecurityType, symbol: Symbol, quantity: Decimal, stopPrice: Decimal, limitPrice: Decimal, time: DateTime, tag: str, properties: IOrderProperties)
    """
    def ToString(self):
        """
        ToString(self: SubmitOrderRequest) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, orderType, securityType, symbol, quantity, stopPrice, limitPrice, time, tag, properties):
        """ __new__(cls: type, orderType: OrderType, securityType: SecurityType, symbol: Symbol, quantity: Decimal, stopPrice: Decimal, limitPrice: Decimal, time: DateTime, tag: str, properties: IOrderProperties) """
        pass

    LimitPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the limit price of the order, zero if not a limit order

Get: LimitPrice(self: SubmitOrderRequest) -> Decimal

"""

    OrderProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order properties for this request

Get: OrderProperties(self: SubmitOrderRequest) -> IOrderProperties

"""

    OrderRequestType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets QuantConnect.Orders.OrderRequestType.Submit

Get: OrderRequestType(self: SubmitOrderRequest) -> OrderRequestType

"""

    OrderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the order type od the order

Get: OrderType(self: SubmitOrderRequest) -> OrderType

"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the quantity of the order

Get: Quantity(self: SubmitOrderRequest) -> Decimal

"""

    SecurityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the security type of the symbol

Get: SecurityType(self: SubmitOrderRequest) -> SecurityType

"""

    StopPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stop price of the order, zero if not a stop order

Get: StopPrice(self: SubmitOrderRequest) -> Decimal

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the symbol to be traded

Get: Symbol(self: SubmitOrderRequest) -> Symbol

"""



class TimeInForce(object, ITimeInForceHandler):
    """ Time In Force - defines the length of time over which an order will continue working before it is canceled """
    @staticmethod
    def GoodTilDate(expiry):
        """
        GoodTilDate(expiry: DateTime) -> TimeInForce
        
            Gets a 
             QuantConnect.Orders.TimeInForces.GoodTilDateTimeIn
             Force instance
        """
        pass

    def IsFillValid(self, security, order, fill):
        """
        IsFillValid(self: TimeInForce, security: Security, order: Order, fill: OrderEvent) -> bool
        
            Checks if an order fill is valid
        
            security: The security matching the order
            order: The order to be checked
            fill: The order fill to be checked
            Returns: Returns true if the order fill can be emitted, 
             false otherwise
        """
        pass

    def IsOrderExpired(self, security, order):
        """
        IsOrderExpired(self: TimeInForce, security: Security, order: Order) -> bool
        
            Checks if an order is expired
        
            security: The security matching the order
            order: The order to be checked
            Returns: Returns true if the order has expired, false 
             otherwise
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Day = None
    GoodTilCanceled = None


class TimeInForceJsonConverter(JsonConverter):
    """
    Provides an implementation of Newtonsoft.Json.JsonConverter that can deserialize TimeInForce objects
    
    TimeInForceJsonConverter()
    """
    def CanConvert(self, objectType):
        """
        CanConvert(self: TimeInForceJsonConverter, objectType: Type) -> bool
        
            Determines whether this instance can convert the 
             specified object type.
        
        
            objectType: Type of the object.
            Returns: true if this instance can convert the specified 
             object type; otherwise, false.
        """
        pass

    def ReadJson(self, reader, objectType, existingValue, serializer):
        """
        ReadJson(self: TimeInForceJsonConverter, reader: JsonReader, objectType: Type, existingValue: object, serializer: JsonSerializer) -> object
        
            Reads the JSON representation of the object.
        
            reader: The Newtonsoft.Json.JsonReader to read from.
            objectType: Type of the object.
            existingValue: The existing value of object being read.
            serializer: The calling serializer.
            Returns: The object value.
        """
        pass

    def WriteJson(self, writer, value, serializer):
        """
        WriteJson(self: TimeInForceJsonConverter, writer: JsonWriter, value: object, serializer: JsonSerializer)
            Writes the JSON representation of the object.
        
            writer: The Newtonsoft.Json.JsonWriter to write to.
            value: The value.
            serializer: The calling serializer.
        """
        pass

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this Newtonsoft.Json.JsonConverter can write JSON.

Get: CanWrite(self: TimeInForceJsonConverter) -> bool

"""



class UpdateOrderFields(object):
    """
    Specifies the data in an order to be updated
    
    UpdateOrderFields()
    """
    LimitPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specify to update the limit price of the order

Get: LimitPrice(self: UpdateOrderFields) -> Nullable[Decimal]

Set: LimitPrice(self: UpdateOrderFields) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specify to update the quantity of the order

Get: Quantity(self: UpdateOrderFields) -> Nullable[Decimal]

Set: Quantity(self: UpdateOrderFields) = value
"""

    StopPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specify to update the stop price of the order

Get: StopPrice(self: UpdateOrderFields) -> Nullable[Decimal]

Set: StopPrice(self: UpdateOrderFields) = value
"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specify to update the order's tag

Get: Tag(self: UpdateOrderFields) -> str

Set: Tag(self: UpdateOrderFields) = value
"""



class UpdateOrderRequest(OrderRequest):
    """
    Defines a request to update an order's values
    
    UpdateOrderRequest(time: DateTime, orderId: int, fields: UpdateOrderFields)
    """
    def ToString(self):
        """
        ToString(self: UpdateOrderRequest) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, time, orderId, fields):
        """ __new__(cls: type, time: DateTime, orderId: int, fields: UpdateOrderFields) """
        pass

    LimitPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the new limit price of the order, null to not change the limit price

Get: LimitPrice(self: UpdateOrderRequest) -> Nullable[Decimal]

"""

    OrderRequestType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets QuantConnect.Orders.OrderRequestType.Update

Get: OrderRequestType(self: UpdateOrderRequest) -> OrderRequestType

"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the new quantity of the order, null to not change the quantity

Get: Quantity(self: UpdateOrderRequest) -> Nullable[Decimal]

"""

    StopPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the new stop price of the order, null to not change the stop price

Get: StopPrice(self: UpdateOrderRequest) -> Nullable[Decimal]

"""



# variables with complex values

