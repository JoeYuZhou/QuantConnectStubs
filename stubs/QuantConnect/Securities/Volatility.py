# encoding: utf-8
# module QuantConnect.Securities.Volatility calls itself Volatility
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BaseVolatilityModel(object, IVolatilityModel):
    """
    Represents a base model that computes the volatility of a security
    
    BaseVolatilityModel()
    """
    def GetHistoryRequirements(self, security, utcTime):
        """
        GetHistoryRequirements(self: BaseVolatilityModel, security: Security, utcTime: DateTime) -> IEnumerable[HistoryRequest]
        
            Returns history requirements for the volatility 
             model expressed in the form of history request
        
        
            security: The security of the request
            utcTime: The date/time of the request
            Returns: History request object list, or empty if no 
             requirements
        """
        pass

    def SetSubscriptionDataConfigProvider(self, subscriptionDataConfigProvider):
        """
        SetSubscriptionDataConfigProvider(self: BaseVolatilityModel, subscriptionDataConfigProvider: ISubscriptionDataConfigProvider)
            Sets the 
             QuantConnect.Interfaces.ISubscriptionDataConfigPro
             vider instance to use.
        
        
            subscriptionDataConfigProvider: Provides access to registered 
             QuantConnect.Data.SubscriptionDataConfig
        """
        pass

    def Update(self, security, data):
        """
        Update(self: BaseVolatilityModel, security: Security, data: BaseData)
            Updates this model using the new price 
             information in
                    the specified 
             security instance
        
        
            security: The security to calculate volatility for
            data: The new data used to update the model
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Volatility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the volatility of the security as a percentage

Get: Volatility(self: BaseVolatilityModel) -> Decimal

"""


    SubscriptionDataConfigProvider = None


