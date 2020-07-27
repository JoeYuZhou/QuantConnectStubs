# encoding: utf-8
# module QuantConnect.Orders.TimeInForces calls itself TimeInForces
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DayTimeInForce(TimeInForce, ITimeInForceHandler):
    """
    Day Time In Force - order expires at market close
    
    DayTimeInForce()
    """
    def IsFillValid(self, security, order, fill):
        """
        IsFillValid(self: DayTimeInForce, security: Security, order: Order, fill: OrderEvent) -> bool
        
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
        IsOrderExpired(self: DayTimeInForce, security: Security, order: Order) -> bool
        
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


class GoodTilCanceledTimeInForce(TimeInForce, ITimeInForceHandler):
    """
    Good Til Canceled Time In Force - order does never expires
    
    GoodTilCanceledTimeInForce()
    """
    def IsFillValid(self, security, order, fill):
        """
        IsFillValid(self: GoodTilCanceledTimeInForce, security: Security, order: Order, fill: OrderEvent) -> bool
        
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
        IsOrderExpired(self: GoodTilCanceledTimeInForce, security: Security, order: Order) -> bool
        
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


class GoodTilDateTimeInForce(TimeInForce, ITimeInForceHandler):
    """
    Good Til Date Time In Force - order expires and will be cancelled on a fixed date/time
    
    GoodTilDateTimeInForce(expiry: DateTime)
    """
    def GetForexOrderExpiryDateTime(self, order):
        """
        GetForexOrderExpiryDateTime(self: GoodTilDateTimeInForce, order: Order) -> DateTime
        
            Returns the expiry date and time (UTC) for a 
             Forex order
        """
        pass

    def IsFillValid(self, security, order, fill):
        """
        IsFillValid(self: GoodTilDateTimeInForce, security: Security, order: Order, fill: OrderEvent) -> bool
        
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
        IsOrderExpired(self: GoodTilDateTimeInForce, security: Security, order: Order) -> bool
        
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

    @staticmethod # known case of __new__
    def __new__(self, expiry):
        """ __new__(cls: type, expiry: DateTime) """
        pass

    Expiry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The date/time on which the order will expire and will be cancelled

Get: Expiry(self: GoodTilDateTimeInForce) -> DateTime

"""



