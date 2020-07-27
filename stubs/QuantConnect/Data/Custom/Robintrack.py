# encoding: utf-8
# module QuantConnect.Data.Custom.Robintrack calls itself Robintrack
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RobintrackHoldings(BaseData, IBaseData):
    """
    Aggregate unique user stock holdings
                
                 Data sourced from Robintrack - https://robintrack.net
    
    RobintrackHoldings()
    """
    def Clone(self, fillForward=None):
        """
        Clone(self: RobintrackHoldings) -> BaseData
        
            Creates a clone of the current object
            Returns: Copy of the current object
        """
        pass

    def DataTimeZone(self):
        """
        DataTimeZone(self: RobintrackHoldings) -> DateTimeZone
        
            Sets the data timezone
            Returns: Timezone
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: RobintrackHoldings, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Gets the source of the file
        
            config: Subscription config
            date: Data for the given date to read
            isLiveMode: Is live mode
            Returns: Subscription data source
        """
        pass

    @staticmethod
    def Read(line, dateFormat):
        """
        Read(line: str, dateFormat: str) -> RobintrackHoldings
        
            Parses a line of Robintrack data with an optional 
             dateFormat
        
        
            line: Line to parse
            dateFormat: Date format to parse timestamp in
            Returns: Instance of this class
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: RobintrackHoldings, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Reads the data from the source provided in 
             QuantConnect.Data.Custom.Robintrack.RobintrackHold
             ings.GetSource(QuantConnect.Data.SubscriptionDataC
             onfig,System.DateTime,System.Boolean)
                   
              and converts it into an instance of this class 
             (QuantConnect.Data.Custom.Robintrack.RobintrackHol
             dings).
        
        
            config: Subscription config
            line: Line to parse
            date: Date that the data is being read
            isLiveMode: Is live mode
            Returns: Instance of 
             QuantConnect.Data.Custom.Robintrack.RobintrackHold
             ings casted as QuantConnect.Data.BaseData
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: RobintrackHoldings) -> bool
        
            Enables mapping of the underlying symbol
            Returns: true
        """
        pass

    def SupportedResolutions(self):
        """
        SupportedResolutions(self: RobintrackHoldings) -> List[Resolution]
        
            Provides list of supported resolutions
            Returns: List of supported resolutions
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    TotalUniqueHoldings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total number of unique holdings across all stocks by users

Get: TotalUniqueHoldings(self: RobintrackHoldings) -> Decimal

Set: TotalUniqueHoldings(self: RobintrackHoldings) = value
"""

    UniverseHoldingPercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Percentage of the U.S. equities universe that unique users hold stock for

Get: UniverseHoldingPercent(self: RobintrackHoldings) -> Decimal

"""

    UsersHolding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of unique users holding a given stock

Get: UsersHolding(self: RobintrackHoldings) -> int

Set: UsersHolding(self: RobintrackHoldings) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for QuantConnect.Data.Custom.Robintrack.RobintrackHoldings.UsersHolding

Get: Value(self: RobintrackHoldings) -> Decimal

"""



