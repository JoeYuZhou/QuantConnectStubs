# encoding: utf-8
# module QuantConnect.Data.Custom.CBOE calls itself CBOE
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CBOE(TradeBar, IBaseData, IBaseDataBar, IBar):
    """ CBOE() """
    def DefaultResolution(self):
        """
        DefaultResolution(self: CBOE) -> Resolution
        
            Gets the default resolution for this data and 
             security type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: CBOE, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Gets the source location of the CBOE file
        """
        pass

    def IsSparseData(self):
        """
        IsSparseData(self: CBOE) -> bool
        
            Determines if data source is sparse
            Returns: false
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: CBOE, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Reads the data from the source and creates a 
             BaseData instance
        
        
            config: Configuration
            line: Line of data
            date: Date we're requesting data for
            isLiveMode: Is live mode
            Returns: New BaseData instance to be used in the algorithm
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: CBOE) -> bool
        
            Determines whether the data source requires 
             mapping
        
            Returns: false
        """
        pass

    def SupportedResolutions(self):
        """
        SupportedResolutions(self: CBOE) -> List[Resolution]
        
            Gets the supported resolution for this data and 
             security type
        """
        pass

    def ToString(self):
        """
        ToString(self: CBOE) -> str
        
            Converts the instance to a string
            Returns: String containing open, high, low, close
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


