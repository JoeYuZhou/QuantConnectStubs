# encoding: utf-8
# module QuantConnect.Indicators.CandlestickPatterns calls itself CandlestickPatterns
# from QuantConnect.Indicators, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CandlestickPattern(WindowIndicator[IBaseDataBar], IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """ Abstract base class for a candlestick pattern indicator """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def GetCandleAverage(self, *args): #cannot find CLR method
        """
        GetCandleAverage(type: CandleSettingType, sum: Decimal, tradeBar: IBaseDataBar) -> Decimal
        
            Returns the average range of the previous candles
        
            type: The type of setting to use
            sum: The sum of the previous candles ranges
            tradeBar: The input candle
        """
        pass

    def GetCandleColor(self, *args): #cannot find CLR method
        """
        GetCandleColor(tradeBar: IBaseDataBar) -> CandleColor
        
            Returns the candle color of a candle
        
            tradeBar: The input candle
        """
        pass

    def GetCandleGapDown(self, *args): #cannot find CLR method
        """
        GetCandleGapDown(tradeBar: IBaseDataBar, previousBar: IBaseDataBar) -> bool
        
            Returns true if the candle is lower than the 
             previous one
        """
        pass

    def GetCandleGapUp(self, *args): #cannot find CLR method
        """
        GetCandleGapUp(tradeBar: IBaseDataBar, previousBar: IBaseDataBar) -> bool
        
            Returns true if the candle is higher than the 
             previous one
        """
        pass

    def GetCandleRange(self, *args): #cannot find CLR method
        """
        GetCandleRange(type: CandleSettingType, tradeBar: IBaseDataBar) -> Decimal
        
            Returns the range of a candle
        
            type: The type of setting to use
            tradeBar: The input candle
        """
        pass

    def GetHighLowRange(self, *args): #cannot find CLR method
        """
        GetHighLowRange(tradeBar: IBaseDataBar) -> Decimal
        
            Returns the full range of the candle
        
            tradeBar: The input candle
        """
        pass

    def GetLowerShadow(self, *args): #cannot find CLR method
        """
        GetLowerShadow(tradeBar: IBaseDataBar) -> Decimal
        
            Returns the range of the candle's lower shadow
        
            tradeBar: The input candle
        """
        pass

    def GetRealBody(self, *args): #cannot find CLR method
        """
        GetRealBody(tradeBar: IBaseDataBar) -> Decimal
        
            Returns the distance between the close and the 
             open of a candle
        
        
            tradeBar: The input candle
        """
        pass

    def GetRealBodyGapDown(self, *args): #cannot find CLR method
        """
        GetRealBodyGapDown(tradeBar: IBaseDataBar, previousBar: IBaseDataBar) -> bool
        
            Returns true if the candle is lower than the 
             previous one (with no body overlap)
        """
        pass

    def GetRealBodyGapUp(self, *args): #cannot find CLR method
        """
        GetRealBodyGapUp(tradeBar: IBaseDataBar, previousBar: IBaseDataBar) -> bool
        
            Returns true if the candle is higher than the 
             previous one (with no body overlap)
        """
        pass

    def GetUpperShadow(self, *args): #cannot find CLR method
        """
        GetUpperShadow(tradeBar: IBaseDataBar) -> Decimal
        
            Returns the range of the candle's upper shadow
        
            tradeBar: The input candle
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str, period: int) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class AbandonedBaby(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Abandoned Baby candlestick pattern
    
    AbandonedBaby(name: str, penetration: Decimal)
    AbandonedBaby(penetration: Decimal)
    AbandonedBaby()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: AbandonedBaby, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: AbandonedBaby)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, penetration: Decimal)
        __new__(cls: type, penetration: Decimal)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: AbandonedBaby) -> bool

"""



class AdvanceBlock(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Advance Block candlestick pattern
    
    AdvanceBlock(name: str)
    AdvanceBlock()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: AdvanceBlock, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: AdvanceBlock)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: AdvanceBlock) -> bool

"""



class BeltHold(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Belt-hold candlestick pattern indicator
    
    BeltHold(name: str)
    BeltHold()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: BeltHold, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: BeltHold)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: BeltHold) -> bool

"""



class Breakaway(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Breakaway candlestick pattern indicator
    
    Breakaway(name: str)
    Breakaway()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Breakaway, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Breakaway)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Breakaway) -> bool

"""



class CandleColor(Enum, IComparable, IFormattable, IConvertible):
    """
    Colors of a candle
    
    enum CandleColor, values: Black (-1), White (1)
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

    Black = None
    value__ = None
    White = None


class CandleRangeType(Enum, IComparable, IFormattable, IConvertible):
    """
    Types of candlestick ranges
    
    enum CandleRangeType, values: HighLow (1), RealBody (0), Shadows (2)
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

    HighLow = None
    RealBody = None
    Shadows = None
    value__ = None


class CandleSetting(object):
    """
    Represents a candle setting
    
    CandleSetting(rangeType: CandleRangeType, averagePeriod: int, factor: Decimal)
    """
    @staticmethod # known case of __new__
    def __new__(self, rangeType, averagePeriod, factor):
        """ __new__(cls: type, rangeType: CandleRangeType, averagePeriod: int, factor: Decimal) """
        pass

    AveragePeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of previous candles to average

Get: AveragePeriod(self: CandleSetting) -> int

"""

    Factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A multiplier to calculate candle ranges

Get: Factor(self: CandleSetting) -> Decimal

"""

    RangeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The candle range type

Get: RangeType(self: CandleSetting) -> CandleRangeType

"""



class CandleSettings(object):
    """ Candle settings for all candlestick patterns """
    @staticmethod
    def Get(type):
        """
        Get(type: CandleSettingType) -> CandleSetting
        
            Returns the candle setting for the requested type
        
            type: The candle setting type
        """
        pass

    @staticmethod
    def Set(type, setting):
        """
        Set(type: CandleSettingType, setting: CandleSetting)
            Changes the default candle setting for the 
             requested type
        
        
            type: The candle setting type
            setting: The candle setting
        """
        pass

    __all__ = [
        'Get',
        'Set',
    ]


class CandleSettingType(Enum, IComparable, IFormattable, IConvertible):
    """
    Types of candlestick settings
    
    enum CandleSettingType, values: BodyDoji (3), BodyLong (0), BodyShort (2), BodyVeryLong (1), Equal (10), Far (9), Near (8), ShadowLong (4), ShadowShort (6), ShadowVeryLong (5), ShadowVeryShort (7)
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

    BodyDoji = None
    BodyLong = None
    BodyShort = None
    BodyVeryLong = None
    Equal = None
    Far = None
    Near = None
    ShadowLong = None
    ShadowShort = None
    ShadowVeryLong = None
    ShadowVeryShort = None
    value__ = None


class ClosingMarubozu(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Closing Marubozu candlestick pattern indicator
    
    ClosingMarubozu(name: str)
    ClosingMarubozu()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ClosingMarubozu, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: ClosingMarubozu)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: ClosingMarubozu) -> bool

"""



class ConcealedBabySwallow(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Concealed Baby Swallow candlestick pattern
    
    ConcealedBabySwallow(name: str)
    ConcealedBabySwallow()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ConcealedBabySwallow, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: ConcealedBabySwallow)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: ConcealedBabySwallow) -> bool

"""



class Counterattack(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Counterattack candlestick pattern
    
    Counterattack(name: str)
    Counterattack()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Counterattack, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Counterattack)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Counterattack) -> bool

"""



class DarkCloudCover(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Dark Cloud Cover candlestick pattern
    
    DarkCloudCover(name: str, penetration: Decimal)
    DarkCloudCover(penetration: Decimal)
    DarkCloudCover()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: DarkCloudCover, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: DarkCloudCover)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, penetration: Decimal)
        __new__(cls: type, penetration: Decimal)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: DarkCloudCover) -> bool

"""



class Doji(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Doji candlestick pattern indicator
    
    Doji(name: str)
    Doji()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Doji, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Doji)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Doji) -> bool

"""



class DojiStar(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Doji Star candlestick pattern indicator
    
    DojiStar(name: str)
    DojiStar()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: DojiStar, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: DojiStar)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: DojiStar) -> bool

"""



class DragonflyDoji(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Dragonfly Doji candlestick pattern indicator
    
    DragonflyDoji(name: str)
    DragonflyDoji()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: DragonflyDoji, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: DragonflyDoji)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: DragonflyDoji) -> bool

"""



class Engulfing(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Engulfing candlestick pattern
    
    Engulfing(name: str)
    Engulfing()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Engulfing, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Engulfing) -> bool

"""



class EveningDojiStar(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Evening Doji Star candlestick pattern
    
    EveningDojiStar(name: str, penetration: Decimal)
    EveningDojiStar(penetration: Decimal)
    EveningDojiStar()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: EveningDojiStar, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: EveningDojiStar)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, penetration: Decimal)
        __new__(cls: type, penetration: Decimal)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: EveningDojiStar) -> bool

"""



class EveningStar(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Evening Star candlestick pattern
    
    EveningStar(name: str, penetration: Decimal)
    EveningStar(penetration: Decimal)
    EveningStar()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: EveningStar, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: EveningStar)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, penetration: Decimal)
        __new__(cls: type, penetration: Decimal)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: EveningStar) -> bool

"""



class GapSideBySideWhite(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Up/Down-gap side-by-side white lines candlestick pattern
    
    GapSideBySideWhite(name: str)
    GapSideBySideWhite()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: GapSideBySideWhite, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: GapSideBySideWhite)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: GapSideBySideWhite) -> bool

"""



class GravestoneDoji(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Gravestone Doji candlestick pattern indicator
    
    GravestoneDoji(name: str)
    GravestoneDoji()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: GravestoneDoji, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: GravestoneDoji)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: GravestoneDoji) -> bool

"""



class Hammer(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Hammer candlestick pattern indicator
    
    Hammer(name: str)
    Hammer()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Hammer, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Hammer)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Hammer) -> bool

"""



class HangingMan(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Hanging Man candlestick pattern indicator
    
    HangingMan(name: str)
    HangingMan()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: HangingMan, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: HangingMan)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: HangingMan) -> bool

"""



class Harami(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Harami candlestick pattern indicator
    
    Harami(name: str)
    Harami()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Harami, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Harami)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Harami) -> bool

"""



class HaramiCross(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Harami Cross candlestick pattern indicator
    
    HaramiCross(name: str)
    HaramiCross()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: HaramiCross, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: HaramiCross)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: HaramiCross) -> bool

"""



class HighWaveCandle(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    High-Wave Candle candlestick pattern indicator
    
    HighWaveCandle(name: str)
    HighWaveCandle()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: HighWaveCandle, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: HighWaveCandle)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: HighWaveCandle) -> bool

"""



class Hikkake(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Hikkake candlestick pattern
    
    Hikkake(name: str)
    Hikkake()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Hikkake, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Hikkake)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Hikkake) -> bool

"""



class HikkakeModified(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Hikkake Modified candlestick pattern
    
    HikkakeModified(name: str)
    HikkakeModified()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: HikkakeModified, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: HikkakeModified)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: HikkakeModified) -> bool

"""



class HomingPigeon(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Homing Pigeon candlestick pattern indicator
    
    HomingPigeon(name: str)
    HomingPigeon()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: HomingPigeon, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: HomingPigeon)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: HomingPigeon) -> bool

"""



class IdenticalThreeCrows(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Identical Three Crows candlestick pattern
    
    IdenticalThreeCrows(name: str)
    IdenticalThreeCrows()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: IdenticalThreeCrows, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: IdenticalThreeCrows)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: IdenticalThreeCrows) -> bool

"""



class InNeck(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    In-Neck candlestick pattern indicator
    
    InNeck(name: str)
    InNeck()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: InNeck, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: InNeck)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: InNeck) -> bool

"""



class InvertedHammer(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Inverted Hammer candlestick pattern indicator
    
    InvertedHammer(name: str)
    InvertedHammer()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: InvertedHammer, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: InvertedHammer)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: InvertedHammer) -> bool

"""



class Kicking(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Kicking candlestick pattern
    
    Kicking(name: str)
    Kicking()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Kicking, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Kicking)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Kicking) -> bool

"""



class KickingByLength(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Kicking (bull/bear determined by the longer marubozu) candlestick pattern
    
    KickingByLength(name: str)
    KickingByLength()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: KickingByLength, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: KickingByLength)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: KickingByLength) -> bool

"""



class LadderBottom(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Ladder Bottom candlestick pattern indicator
    
    LadderBottom(name: str)
    LadderBottom()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: LadderBottom, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: LadderBottom)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: LadderBottom) -> bool

"""



class LongLeggedDoji(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Long Legged Doji candlestick pattern indicator
    
    LongLeggedDoji(name: str)
    LongLeggedDoji()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: LongLeggedDoji, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: LongLeggedDoji)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: LongLeggedDoji) -> bool

"""



class LongLineCandle(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Long Line Candle candlestick pattern indicator
    
    LongLineCandle(name: str)
    LongLineCandle()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: LongLineCandle, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: LongLineCandle)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: LongLineCandle) -> bool

"""



class Marubozu(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Marubozu candlestick pattern indicator
    
    Marubozu(name: str)
    Marubozu()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Marubozu, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Marubozu)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Marubozu) -> bool

"""



class MatchingLow(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Matching Low candlestick pattern indicator
    
    MatchingLow(name: str)
    MatchingLow()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: MatchingLow, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: MatchingLow)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: MatchingLow) -> bool

"""



class MatHold(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Mat Hold candlestick pattern
    
    MatHold(name: str, penetration: Decimal)
    MatHold(penetration: Decimal)
    MatHold()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: MatHold, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: MatHold)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, penetration: Decimal)
        __new__(cls: type, penetration: Decimal)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: MatHold) -> bool

"""



class MorningDojiStar(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Morning Doji Star candlestick pattern
    
    MorningDojiStar(name: str, penetration: Decimal)
    MorningDojiStar(penetration: Decimal)
    MorningDojiStar()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: MorningDojiStar, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: MorningDojiStar)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, penetration: Decimal)
        __new__(cls: type, penetration: Decimal)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: MorningDojiStar) -> bool

"""



class MorningStar(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Morning Star candlestick pattern
    
    MorningStar(name: str, penetration: Decimal)
    MorningStar(penetration: Decimal)
    MorningStar()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: MorningStar, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: MorningStar)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, penetration: Decimal)
        __new__(cls: type, penetration: Decimal)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: MorningStar) -> bool

"""



class OnNeck(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    On-Neck candlestick pattern indicator
    
    OnNeck(name: str)
    OnNeck()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: OnNeck, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: OnNeck)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: OnNeck) -> bool

"""



class Piercing(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Piercing candlestick pattern
    
    Piercing(name: str)
    Piercing()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Piercing, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Piercing)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Piercing) -> bool

"""



class RickshawMan(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Rickshaw Man candlestick pattern
    
    RickshawMan(name: str)
    RickshawMan()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: RickshawMan, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: RickshawMan)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: RickshawMan) -> bool

"""



class RiseFallThreeMethods(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Rising/Falling Three Methods candlestick pattern
    
    RiseFallThreeMethods(name: str)
    RiseFallThreeMethods()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: RiseFallThreeMethods, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: RiseFallThreeMethods)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: RiseFallThreeMethods) -> bool

"""



class SeparatingLines(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Separating Lines candlestick pattern indicator
    
    SeparatingLines(name: str)
    SeparatingLines()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: SeparatingLines, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: SeparatingLines)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: SeparatingLines) -> bool

"""



class ShootingStar(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Shooting Star candlestick pattern
    
    ShootingStar(name: str)
    ShootingStar()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ShootingStar, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: ShootingStar)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: ShootingStar) -> bool

"""



class ShortLineCandle(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Short Line Candle candlestick pattern indicator
    
    ShortLineCandle(name: str)
    ShortLineCandle()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ShortLineCandle, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: ShortLineCandle)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: ShortLineCandle) -> bool

"""



class SpinningTop(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Spinning Top candlestick pattern indicator
    
    SpinningTop(name: str)
    SpinningTop()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: SpinningTop, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: SpinningTop)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: SpinningTop) -> bool

"""



class StalledPattern(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Stalled Pattern candlestick pattern
    
    StalledPattern(name: str)
    StalledPattern()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: StalledPattern, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: StalledPattern)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: StalledPattern) -> bool

"""



class StickSandwich(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Stick Sandwich candlestick pattern indicator
    
    StickSandwich(name: str)
    StickSandwich()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: StickSandwich, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: StickSandwich)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: StickSandwich) -> bool

"""



class Takuri(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Takuri (Dragonfly Doji with very long lower shadow) candlestick pattern indicator
    
    Takuri(name: str)
    Takuri()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Takuri, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Takuri)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Takuri) -> bool

"""



class TasukiGap(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Tasuki Gap candlestick pattern indicator
    
    TasukiGap(name: str)
    TasukiGap()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: TasukiGap, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: TasukiGap)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: TasukiGap) -> bool

"""



class ThreeBlackCrows(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Three Black Crows candlestick pattern
    
    ThreeBlackCrows(name: str)
    ThreeBlackCrows()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ThreeBlackCrows, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: ThreeBlackCrows)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: ThreeBlackCrows) -> bool

"""



class ThreeInside(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Three Inside Up/Down candlestick pattern
    
    ThreeInside(name: str)
    ThreeInside()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ThreeInside, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: ThreeInside)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: ThreeInside) -> bool

"""



class ThreeLineStrike(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Three Line Strike candlestick pattern
    
    ThreeLineStrike(name: str)
    ThreeLineStrike()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ThreeLineStrike, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: ThreeLineStrike)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: ThreeLineStrike) -> bool

"""



class ThreeOutside(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Three Outside Up/Down candlestick pattern
    
    ThreeOutside(name: str)
    ThreeOutside()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ThreeOutside, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: ThreeOutside) -> bool

"""



class ThreeStarsInSouth(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Three Stars In The South candlestick pattern
    
    ThreeStarsInSouth(name: str)
    ThreeStarsInSouth()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ThreeStarsInSouth, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: ThreeStarsInSouth)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: ThreeStarsInSouth) -> bool

"""



class ThreeWhiteSoldiers(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Three Advancing White Soldiers candlestick pattern
    
    ThreeWhiteSoldiers(name: str)
    ThreeWhiteSoldiers()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ThreeWhiteSoldiers, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: ThreeWhiteSoldiers)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: ThreeWhiteSoldiers) -> bool

"""



class Thrusting(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Thrusting candlestick pattern indicator
    
    Thrusting(name: str)
    Thrusting()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Thrusting, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Thrusting)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Thrusting) -> bool

"""



class Tristar(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Tristar candlestick pattern indicator
    
    Tristar(name: str)
    Tristar()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Tristar, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Tristar)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: Tristar) -> bool

"""



class TwoCrows(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Two Crows candlestick pattern indicator
    
    TwoCrows(name: str)
    TwoCrows()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: TwoCrows, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: TwoCrows)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: TwoCrows) -> bool

"""



class UniqueThreeRiver(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Unique Three River candlestick pattern
    
    UniqueThreeRiver(name: str)
    UniqueThreeRiver()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: UniqueThreeRiver, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: UniqueThreeRiver)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: UniqueThreeRiver) -> bool

"""



class UpDownGapThreeMethods(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Up/Down Gap Three Methods candlestick pattern
    
    UpDownGapThreeMethods(name: str)
    UpDownGapThreeMethods()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: UpDownGapThreeMethods, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: UpDownGapThreeMethods) -> bool

"""



class UpsideGapTwoCrows(CandlestickPattern, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    Upside Gap Two Crows candlestick pattern
    
    UpsideGapTwoCrows(name: str)
    UpsideGapTwoCrows()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: UpsideGapTwoCrows, window: IReadOnlyWindow[IBaseDataBar], input: IBaseDataBar) -> Decimal
        ComputeNextValue(self: WindowIndicator[IBaseDataBar], input: IBaseDataBar) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseDataBar], consolidated: IndicatorDataPoint)
            Event invocator for the Updated event
        
            consolidated: This is the new piece of data produced by this 
             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: UpsideGapTwoCrows)
            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> IndicatorResult """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type, name: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized

Get: IsReady(self: UpsideGapTwoCrows) -> bool

"""



