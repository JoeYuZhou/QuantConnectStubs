# encoding: utf-8
# module QuantConnect.Data.Custom.Fred calls itself Fred
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Fred(BaseData, IBaseData):
    """ Fred() """
    def Clone(self, fillForward=None):
        """
        Clone(self: Fred) -> BaseData
        
            Clones the data
            Returns: A clone of the object
        """
        pass

    def DefaultResolution(self):
        """
        DefaultResolution(self: Fred) -> Resolution
        
            Gets the default resolution for this data and 
             security type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: Fred, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Return the URL string source of the file. This 
             will be converted to a stream
        
        
            config: Configuration object
            date: Date of this source file
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: String URL of source file.
        """
        pass

    def IsSparseData(self):
        """
        IsSparseData(self: Fred) -> bool
        
            Indicates whether the data is sparse.
                   
              If true, we disable logging for missing files
        
            Returns: true
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: Fred, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
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
        RequiresMapping(self: Fred) -> bool
        
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
        SupportedResolutions(self: Fred) -> List[Resolution]
        
            Gets the supported resolution for this data and 
             security type
        """
        pass

    def ToString(self):
        """
        ToString(self: Fred) -> str
        
            Converts the instance to string
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CBOE = None
    CentralBankInterventions = None
    CommercialPaper = None
    ICEBofAML = None
    LIBOR = None
    OECDRecessionIndicators = None
    TradeWeightedIndexes = None
    Wilshire = None


class FredApi(BaseData, IBaseData):
    """ FredApi() """
    def GetSource(self, config, date, *__args):
        """
        GetSource(self: FredApi, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Return the URL string source of the file. This 
             will be converted to a stream
        
        
            config: Configuration object
            date: Date of this source file
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: String URL of source file.
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: FredApi, config: SubscriptionDataConfig, content: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Readers the specified configuration.
        
            config: The configuration.
            content: The content.
            date: The date.
            isLiveMode: if set to true [is live mode].
        """
        pass

    @staticmethod
    def SetAuthCode(authCode):
        """
        SetAuthCode(authCode: str)
            Sets the EIA API token.
        
            authCode: The EIA API token
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: FredApi) -> int

Set: Count(self: FredApi) = value
"""

    FileType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileType(self: FredApi) -> str

Set: FileType(self: FredApi) = value
"""

    Limit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Limit(self: FredApi) -> int

Set: Limit(self: FredApi) = value
"""

    ObservationEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObservationEnd(self: FredApi) -> str

Set: ObservationEnd(self: FredApi) = value
"""

    Observations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Observations(self: FredApi) -> IList[Observation]

Set: Observations(self: FredApi) = value
"""

    ObservationStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObservationStart(self: FredApi) -> str

Set: ObservationStart(self: FredApi) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: FredApi) -> int

Set: Offset(self: FredApi) = value
"""

    OrderBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderBy(self: FredApi) -> str

Set: OrderBy(self: FredApi) = value
"""

    OutputType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputType(self: FredApi) -> int

Set: OutputType(self: FredApi) = value
"""

    RealtimeEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RealtimeEnd(self: FredApi) -> str

Set: RealtimeEnd(self: FredApi) = value
"""

    RealtimeStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RealtimeStart(self: FredApi) -> str

Set: RealtimeStart(self: FredApi) = value
"""

    SortOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SortOrder(self: FredApi) -> str

Set: SortOrder(self: FredApi) = value
"""

    Units = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Units(self: FredApi) -> str

Set: Units(self: FredApi) = value
"""


    AuthCode = ''
    IsAuthCodeSet = False


class Observation(object):
    """ Observation() """
    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: Observation) -> DateTime

Set: Date(self: Observation) = value
"""

    RealtimeEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RealtimeEnd(self: Observation) -> str

Set: RealtimeEnd(self: Observation) = value
"""

    RealtimeStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RealtimeStart(self: Observation) -> str

Set: RealtimeStart(self: Observation) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: Observation) -> str

Set: Value(self: Observation) = value
"""



