# encoding: utf-8
# module QuantConnect.Data.Custom.USEnergy calls itself USEnergy
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class USEnergy(BaseData, IBaseData):
    """
    United States Energy Information Administration (EIA). This loads U.S. Energy data from QuantConnect's cache.
    
    USEnergy()
    """
    def Clone(self, fillForward=None):
        """
        Clone(self: USEnergy) -> BaseData
        
            Clones the data
            Returns: A clone of the object
        """
        pass

    def DefaultResolution(self):
        """
        DefaultResolution(self: USEnergy) -> Resolution
        
            Gets the default resolution for this data and 
             security type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: USEnergy, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Determines the location of the data
        
            config: Subscription configuration
            date: Date
            isLiveMode: Is live mode
            Returns: Location of the data as a SubscriptionDataSource
        """
        pass

    def IsSparseData(self):
        """
        IsSparseData(self: USEnergy) -> bool
        
            Indicates whether the data is sparse.
                   
              If true, we disable logging for missing files
        
            Returns: true
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: USEnergy, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Parses the data from the line provided and loads 
             it into LEAN
        
        
            config: Subscription configuration
            line: Line of data
            date: Date
            isLiveMode: Is live mode
            Returns: New instance of USEnergy
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: USEnergy) -> bool
        
            Indicates whether the data source is tied
               
                  to an underlying symbol and requires that 
             corporate
                    events be applied to it as 
             well, such as renames and delistings
        
            Returns: false
        """
        pass

    def SupportedResolutions(self):
        """
        SupportedResolutions(self: USEnergy) -> List[Resolution]
        
            Gets the supported resolution for this data and 
             security type
        """
        pass

    def ToString(self):
        """
        ToString(self: USEnergy) -> str
        
            Converts the instance to string
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Petroleum = None


