# encoding: utf-8
# module QuantConnect.Data.Custom.USTreasury calls itself USTreasury
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class USTreasuryYieldCurveRate(BaseData, IBaseData):
    """
    U.S. Treasury yield curve data
    
    USTreasuryYieldCurveRate()
    """
    def Clone(self, fillForward=None):
        """
        Clone(self: USTreasuryYieldCurveRate) -> BaseData
        
            Clones the object. This method implementation is 
             required
                    so that we don't have any 
             null values for our properties
                    when 
             the user attempts to use it in backtesting/live 
             trading
        
            Returns: Cloned instance
        """
        pass

    def DefaultResolution(self):
        """
        DefaultResolution(self: USTreasuryYieldCurveRate) -> Resolution
        
            Gets the default resolution for this data and 
             security type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: USTreasuryYieldCurveRate, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Specifies the location of the data and directs 
             LEAN where to load the data from
        
        
            config: Subscription configuration
            date: Algorithm date
            isLiveMode: Is live mode
            Returns: Subscription data source object pointing LEAN to 
             the data location
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: USTreasuryYieldCurveRate, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Reads and parses yield curve data from a csv file
        
            config: Subscription configuration
            line: CSV line containing yield curve data
            date: Date request was made for
            isLiveMode: Is live mode
            Returns: YieldCurve instance
        """
        pass

    def SupportedResolutions(self):
        """
        SupportedResolutions(self: USTreasuryYieldCurveRate) -> List[Resolution]
        
            Gets the supported resolution for this data and 
             security type
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FiveYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Five year yield curve

Get: FiveYear(self: USTreasuryYieldCurveRate) -> Nullable[Decimal]

"""

    OneMonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """One month yield curve

Get: OneMonth(self: USTreasuryYieldCurveRate) -> Nullable[Decimal]

"""

    OneYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """One year yield curve

Get: OneYear(self: USTreasuryYieldCurveRate) -> Nullable[Decimal]

"""

    SevenYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Seven year yield curve

Get: SevenYear(self: USTreasuryYieldCurveRate) -> Nullable[Decimal]

"""

    SixMonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Six month yield curve

Get: SixMonth(self: USTreasuryYieldCurveRate) -> Nullable[Decimal]

"""

    TenYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ten year yield curve

Get: TenYear(self: USTreasuryYieldCurveRate) -> Nullable[Decimal]

"""

    ThirtyYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Thirty year yield curve

Get: ThirtyYear(self: USTreasuryYieldCurveRate) -> Nullable[Decimal]

"""

    ThreeMonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Three month yield curve

Get: ThreeMonth(self: USTreasuryYieldCurveRate) -> Nullable[Decimal]

"""

    ThreeYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Three year yield curve

Get: ThreeYear(self: USTreasuryYieldCurveRate) -> Nullable[Decimal]

"""

    TwentyYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Twenty year yield curve

Get: TwentyYear(self: USTreasuryYieldCurveRate) -> Nullable[Decimal]

"""

    TwoMonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Two month yield curve

Get: TwoMonth(self: USTreasuryYieldCurveRate) -> Nullable[Decimal]

"""

    TwoYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Two year yield curve

Get: TwoYear(self: USTreasuryYieldCurveRate) -> Nullable[Decimal]

"""



