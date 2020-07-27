# encoding: utf-8
# module QuantConnect.Indicators calls itself Indicators
# from QuantConnect.Indicators, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Indicator(IndicatorBase[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator):
    """
    Represents a type capable of ingesting a piece of data and producing a new piece of data.

                Indicators can be used to filter and transform data into a new, more informative form.
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """ ComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        """ __new__(cls: type, name: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class MovingAverageConvergenceDivergence(Indicator, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator creates two moving averages defined on a base indicator and produces the difference

                between the fast and slow averages.

    

    MovingAverageConvergenceDivergence(fastPeriod: int, slowPeriod: int, signalPeriod: int, type: MovingAverageType)

    MovingAverageConvergenceDivergence(name: str, fastPeriod: int, slowPeriod: int, signalPeriod: int, type: MovingAverageType)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: MovingAverageConvergenceDivergence, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: MovingAverageConvergenceDivergence)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, fastPeriod: int, slowPeriod: int, signalPeriod: int, type: MovingAverageType)

        __new__(cls: type, name: str, fastPeriod: int, slowPeriod: int, signalPeriod: int, type: MovingAverageType)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Fast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the fast average indicator



Get: Fast(self: MovingAverageConvergenceDivergence) -> IndicatorBase[IndicatorDataPoint]



"""

    Histogram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Developed by Thomas Aspray in 1986, the MACD-Histogram measures the distance between MACD and its signal line, 

            is an oscillator that fluctuates above and below the zero line.

            Bullish or bearish divergences in the MACD-Histogram can alert chartists to an imminent signal line crossover in MACD.



Get: Histogram(self: MovingAverageConvergenceDivergence) -> IndicatorBase[IndicatorDataPoint]



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: MovingAverageConvergenceDivergence) -> bool



"""

    Signal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the signal of the MACD



Get: Signal(self: MovingAverageConvergenceDivergence) -> IndicatorBase[IndicatorDataPoint]



"""

    Slow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the slow average indicator



Get: Slow(self: MovingAverageConvergenceDivergence) -> IndicatorBase[IndicatorDataPoint]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: MovingAverageConvergenceDivergence) -> int



"""



class AbsolutePriceOscillator(MovingAverageConvergenceDivergence, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Absolute Price Oscillator (APO)

                The Absolute Price Oscillator is calculated using the following formula:

                APO[i] = FastMA[i] - SlowMA[i]

    

    AbsolutePriceOscillator(name: str, fastPeriod: int, slowPeriod: int, movingAverageType: MovingAverageType)

    AbsolutePriceOscillator(fastPeriod: int, slowPeriod: int, movingAverageType: MovingAverageType)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: MovingAverageConvergenceDivergence, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, fastPeriod: int, slowPeriod: int, movingAverageType: MovingAverageType)

        __new__(cls: type, fastPeriod: int, slowPeriod: int, movingAverageType: MovingAverageType)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class AccelerationBands(IndicatorBase[IBaseDataBar], IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Acceleration Bands created by Price Headley plots upper and lower envelope bands around a moving average.

    

    AccelerationBands(name: str, period: int, width: Decimal, movingAverageType: MovingAverageType)

    AccelerationBands(period: int, width: Decimal)

    AccelerationBands(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: AccelerationBands, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
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
        Reset(self: AccelerationBands)

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
        __new__(cls: type, name: str, period: int, width: Decimal, movingAverageType: MovingAverageType)

        __new__(cls: type, period: int, width: Decimal)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: AccelerationBands) -> bool



"""

    LowerBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the lower acceleration band  (Low * (1 - Width * (High - Low)/ (High + Low)))



Get: LowerBand(self: AccelerationBands) -> IndicatorBase[IndicatorDataPoint]



"""

    MiddleBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the middle acceleration band (moving average)



Get: MiddleBand(self: AccelerationBands) -> IndicatorBase[IndicatorDataPoint]



"""

    MovingAverageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of moving average



Get: MovingAverageType(self: AccelerationBands) -> MovingAverageType



"""

    UpperBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the upper acceleration band  (High * ( 1 + Width * (High - Low) / (High + Low)))



Get: UpperBand(self: AccelerationBands) -> IndicatorBase[IndicatorDataPoint]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: AccelerationBands) -> int



"""



class TradeBarIndicator(IndicatorBase[TradeBar], IIndicator[TradeBar], IComparable[IIndicator[TradeBar]], IComparable, IIndicator):
    """
    The TradeBarIndicator is an indicator that accepts TradeBar data as its input.

                

                This type is more of a shim/typedef to reduce the need to refer to things as IndicatorBase<TradeBar>
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """ ComputeNextValue(self: IndicatorBase[TradeBar], input: TradeBar) -> Decimal """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[TradeBar], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[TradeBar], input: TradeBar) -> IndicatorResult """
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
        """ __new__(cls: type, name: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class AccumulationDistribution(TradeBarIndicator, IIndicator[TradeBar], IComparable[IIndicator[TradeBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Accumulation/Distribution (AD)

                The Accumulation/Distribution is calculated using the following formula:

                AD = AD + ((Close - Low) - (High - Close)) / (High - Low) * Volume

    

    AccumulationDistribution()

    AccumulationDistribution(name: str)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: AccumulationDistribution, input: TradeBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[TradeBar], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[TradeBar], input: TradeBar) -> IndicatorResult """
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
        __new__(cls: type)

        __new__(cls: type, name: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: AccumulationDistribution) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: AccumulationDistribution) -> int



"""



class AccumulationDistributionOscillator(TradeBarIndicator, IIndicator[TradeBar], IComparable[IIndicator[TradeBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Accumulation/Distribution Oscillator (ADOSC)

                The Accumulation/Distribution Oscillator is calculated using the following formula:

                ADOSC = EMA(fast,AD) - EMA(slow,AD)

    

    AccumulationDistributionOscillator(fastPeriod: int, slowPeriod: int)

    AccumulationDistributionOscillator(name: str, fastPeriod: int, slowPeriod: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: AccumulationDistributionOscillator, input: TradeBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[TradeBar], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: AccumulationDistributionOscillator)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[TradeBar], input: TradeBar) -> IndicatorResult """
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
        __new__(cls: type, fastPeriod: int, slowPeriod: int)

        __new__(cls: type, name: str, fastPeriod: int, slowPeriod: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: AccumulationDistributionOscillator) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: AccumulationDistributionOscillator) -> int



"""



class ArnaudLegouxMovingAverage(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Smooth and high sensitive moving Average. This moving average reduce lag of the information

                but still being smooth to reduce noises.

                Is a weighted moving average, which weights have a Normal shape;

                the parameters Sigma and Offset affect the kurtosis and skewness of the weights respectively.

                Source: http://www.arnaudlegoux.com/index.html

    

    ArnaudLegouxMovingAverage(name: str, period: int, sigma: int, offset: Decimal)

    ArnaudLegouxMovingAverage(name: str, period: int)

    ArnaudLegouxMovingAverage(period: int, sigma: int, offset: Decimal)

    ArnaudLegouxMovingAverage(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ArnaudLegouxMovingAverage, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int, sigma: int, offset: Decimal)

        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int, sigma: int, offset: Decimal)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: ArnaudLegouxMovingAverage) -> int



"""



class BarIndicator(IndicatorBase[IBaseDataBar], IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator):
    """
    The BarIndicator is an indicator that accepts IBaseDataBar data as its input.

                

                This type is more of a shim/typedef to reduce the need to refer to things as IndicatorBase<IBaseDataBar>
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """ ComputeNextValue(self: IndicatorBase[IBaseDataBar], input: IBaseDataBar) -> Decimal """
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
        """ __new__(cls: type, name: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class AroonOscillator(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Aroon Oscillator is the difference between AroonUp and AroonDown. The value of this

                indicator fluctuates between -100 and +100. An upward trend bias is present when the oscillator

                is positive, and a negative trend bias is present when the oscillator is negative. AroonUp/Down

                values over 75 identify strong trends in their respective direction.

    

    AroonOscillator(upPeriod: int, downPeriod: int)

    AroonOscillator(name: str, upPeriod: int, downPeriod: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: AroonOscillator, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
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
        Reset(self: AroonOscillator)

            Resets this indicator and both sub-indicators 

             (AroonUp and AroonDown)
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
        __new__(cls: type, upPeriod: int, downPeriod: int)

        __new__(cls: type, name: str, upPeriod: int, downPeriod: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AroonDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the AroonDown indicator



Get: AroonDown(self: AroonOscillator) -> IndicatorBase[IndicatorDataPoint]



"""

    AroonUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the AroonUp indicator



Get: AroonUp(self: AroonOscillator) -> IndicatorBase[IndicatorDataPoint]



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: AroonOscillator) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: AroonOscillator) -> int



"""



class AverageDirectionalIndex(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes Average Directional Index which measures trend strength without regard to trend direction.

                Firstly, it calculates the Directional Movement and the True Range value, and then the values are accumulated and smoothed

                using a custom smoothing method proposed by Wilder. For an n period smoothing, 1/n of each period's value is added to the total period.

                From these accumulated values we are therefore able to derived the 'Positive Directional Index' (+DI) and 'Negative Directional Index' (-DI)

                which is used to calculate the Average Directional Index.

                Computation source:

                https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_directional_index_adx

    

    AverageDirectionalIndex(period: int)

    AverageDirectionalIndex(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: AverageDirectionalIndex, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
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
        Reset(self: AverageDirectionalIndex)

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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: AverageDirectionalIndex) -> bool



"""

    NegativeDirectionalIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of the Minus Directional Indicator



Get: NegativeDirectionalIndex(self: AverageDirectionalIndex) -> IndicatorBase[IndicatorDataPoint]



"""

    PositiveDirectionalIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the index of the Plus Directional Indicator



Get: PositiveDirectionalIndex(self: AverageDirectionalIndex) -> IndicatorBase[IndicatorDataPoint]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: AverageDirectionalIndex) -> int



"""



class AverageDirectionalMovementIndexRating(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Average Directional Movement Index Rating (ADXR). 

                The Average Directional Movement Index Rating is calculated with the following formula:

                ADXR[i] = (ADX[i] + ADX[i - period + 1]) / 2

    

    AverageDirectionalMovementIndexRating(name: str, period: int)

    AverageDirectionalMovementIndexRating(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: AverageDirectionalMovementIndexRating, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
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
        Reset(self: AverageDirectionalMovementIndexRating)

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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ADX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Average Directional Index indicator instance being used



Get: ADX(self: AverageDirectionalMovementIndexRating) -> AverageDirectionalIndex



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: AverageDirectionalMovementIndexRating) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: AverageDirectionalMovementIndexRating) -> int



"""



class AverageTrueRange(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The AverageTrueRange indicator is a measure of volatility introduced by Welles Wilder in his

                 book: New Concepts in Technical Trading Systems. This indicator computes the TrueRange and then

                 smoothes the TrueRange over a given period.

                

                 TrueRange is defined as the maximum of the following:

                   High - Low

                   ABS(High - PreviousClose)

                   ABS(Low - PreviousClose)

    

    AverageTrueRange(name: str, period: int, movingAverageType: MovingAverageType)

    AverageTrueRange(period: int, movingAverageType: MovingAverageType)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: AverageTrueRange, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    @staticmethod
    def ComputeTrueRange(previous, current):
        """
        ComputeTrueRange(previous: IBaseDataBar, current: IBaseDataBar) -> Decimal

        

            Computes the TrueRange from the current and 

             previous trade bars

                    

                     

             TrueRange is defined as the maximum of the 

             following:

                       High - Low

                   

                 ABS(High - PreviousClose)

                       

             ABS(Low - PreviousClose)

        

        

            previous: The previous trade bar

            current: The current trade bar

            Returns: The true range
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
        Reset(self: AverageTrueRange)

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
        __new__(cls: type, name: str, period: int, movingAverageType: MovingAverageType)

        __new__(cls: type, period: int, movingAverageType: MovingAverageType)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: AverageTrueRange) -> bool



"""

    TrueRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the true range which is the more volatile calculation to be smoothed by this indicator



Get: TrueRange(self: AverageTrueRange) -> IndicatorBase[IBaseDataBar]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: AverageTrueRange) -> int



"""



class BalanceOfPower(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Balance Of Power (BOP).

                The Balance Of Power is calculated with the following formula:

                BOP = (Close - Open) / (High - Low)

    

    BalanceOfPower()

    BalanceOfPower(name: str)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: BalanceOfPower, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
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
        __new__(cls: type)

        __new__(cls: type, name: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: BalanceOfPower) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: BalanceOfPower) -> int



"""



class BollingerBands(Indicator, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator creates a moving average (middle band) with an upper band and lower band

                fixed at k standard deviations above and below the moving average.

    

    BollingerBands(period: int, k: Decimal, movingAverageType: MovingAverageType)

    BollingerBands(name: str, period: int, k: Decimal, movingAverageType: MovingAverageType)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: BollingerBands, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of the following 

             sub-indicators from the given state:

                    

             StandardDeviation, MiddleBand, UpperBand, 

             LowerBand

        

        

            input: The input given to the indicator

            Returns: The input is returned unmodified.
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: BollingerBands)

            Resets this indicator and all sub-indicators 

             (StandardDeviation, LowerBand, MiddleBand, 

             UpperBand)
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int, k: Decimal, movingAverageType: MovingAverageType)

        __new__(cls: type, name: str, period: int, k: Decimal, movingAverageType: MovingAverageType)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BandWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Bollinger BandWidth indicator

            BandWidth = ((Upper Band - Lower Band) / Middle Band) * 100



Get: BandWidth(self: BollingerBands) -> IndicatorBase[IndicatorDataPoint]



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: BollingerBands) -> bool



"""

    LowerBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the lower Bollinger band (middleBand - k * stdDev)



Get: LowerBand(self: BollingerBands) -> IndicatorBase[IndicatorDataPoint]



"""

    MiddleBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the middle Bollinger band (moving average)



Get: MiddleBand(self: BollingerBands) -> IndicatorBase[IndicatorDataPoint]



"""

    MovingAverageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of moving average



Get: MovingAverageType(self: BollingerBands) -> MovingAverageType



"""

    PercentB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Bollinger %B

            %B = (Price - Lower Band)/(Upper Band - Lower Band)



Get: PercentB(self: BollingerBands) -> IndicatorBase[IndicatorDataPoint]



"""

    Price = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Price level



Get: Price(self: BollingerBands) -> IndicatorBase[IndicatorDataPoint]



"""

    StandardDeviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the standard deviation



Get: StandardDeviation(self: BollingerBands) -> IndicatorBase[IndicatorDataPoint]



"""

    UpperBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the upper Bollinger band (middleBand + k * stdDev)



Get: UpperBand(self: BollingerBands) -> IndicatorBase[IndicatorDataPoint]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: BollingerBands) -> int



"""



class ChandeMomentumOscillator(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Chande Momentum Oscillator (CMO).

                CMO calculation is mostly identical to RSI.

                The only difference is in the last step of calculation:

                RSI = gain / (gain+loss)

                CMO = (gain-loss) / (gain+loss)

    

    ChandeMomentumOscillator(period: int)

    ChandeMomentumOscillator(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ChandeMomentumOscillator, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: ChandeMomentumOscillator)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: ChandeMomentumOscillator) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: ChandeMomentumOscillator) -> int



"""



class CommodityChannelIndex(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional commodity channel index (CCI)

                

                 CCI = (Typical Price - 20-period SMA of TP) / (.015 * Mean Deviation)

                 Typical Price (TP) = (High + Low + Close)/3

                 Constant = 0.015

                

                 There are four steps to calculating the Mean Deviation, first, subtract

                 the most recent 20-period average of the typical price from each period's

                 typical price. Second, take the absolute values of these numbers. Third,

                 sum the absolute values. Fourth, divide by the total number of periods (20).

    

    CommodityChannelIndex(period: int, movingAverageType: MovingAverageType)

    CommodityChannelIndex(name: str, period: int, movingAverageType: MovingAverageType)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: CommodityChannelIndex, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
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
        Reset(self: CommodityChannelIndex)

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
        __new__(cls: type, period: int, movingAverageType: MovingAverageType)

        __new__(cls: type, name: str, period: int, movingAverageType: MovingAverageType)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: CommodityChannelIndex) -> bool



"""

    MovingAverageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of moving average



Get: MovingAverageType(self: CommodityChannelIndex) -> MovingAverageType



"""

    TypicalPriceAverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Keep track of the simple moving average of the typical price



Get: TypicalPriceAverage(self: CommodityChannelIndex) -> IndicatorBase[IndicatorDataPoint]



"""

    TypicalPriceMeanDeviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Keep track of the mean absolute deviation of the typical price



Get: TypicalPriceMeanDeviation(self: CommodityChannelIndex) -> IndicatorBase[IndicatorDataPoint]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: CommodityChannelIndex) -> int



"""



class CompositeIndicator(IndicatorBase[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator):
    """
    CompositeIndicator[T](name: str, left: IndicatorBase[T], right: IndicatorBase[T], composer: IndicatorComposer)

    CompositeIndicator[T](left: IndicatorBase[T], right: IndicatorBase[T], composer: IndicatorComposer)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: CompositeIndicator[T], input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: CompositeIndicator[T])

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """
        ValidateAndComputeNextValue(self: CompositeIndicator[T], input: IndicatorDataPoint) -> IndicatorResult

        

            Computes the next value of this indicator from 

             the given state

                    and returns an 

             instance of the 

             QuantConnect.Indicators.IndicatorResult class

        

        

            input: The input given to the indicator

            Returns: An IndicatorResult object including the status of 

             the indicator
        """
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
        __new__(cls: type, name: str, left: IndicatorBase[T], right: IndicatorBase[T], composer: IndicatorComposer)

        __new__(cls: type, left: IndicatorBase[T], right: IndicatorBase[T], composer: IndicatorComposer)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: CompositeIndicator[T]) -> bool



"""

    Left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the 'left' indicator for the delegate



Get: Left(self: CompositeIndicator[T]) -> IndicatorBase[T]



"""

    Right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the 'right' indicator for the delegate



Get: Right(self: CompositeIndicator[T]) -> IndicatorBase[T]



"""


    IndicatorComposer = None


class ConstantIndicator(IndicatorBase[T], IIndicator[T], IComparable[IIndicator[T]], IComparable, IIndicator):
    """ ConstantIndicator[T](name: str, value: Decimal) """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ConstantIndicator[T], input: T) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[T], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: ConstantIndicator[T])

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """
        ValidateAndComputeNextValue(self: IndicatorBase[T], input: T) -> IndicatorResult

        

            Computes the next value of this indicator from 

             the given state

                    and returns an 

             instance of the 

             QuantConnect.Indicators.IndicatorResult class

        

        

            input: The input given to the indicator

            Returns: An IndicatorResult object including the status of 

             the indicator
        """
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
    def __new__(self, name, value):
        """ __new__(cls: type, name: str, value: Decimal) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets true since the ConstantIndicator is always ready to return the same value



Get: IsReady(self: ConstantIndicator[T]) -> bool



"""



class CoppockCurve(IndicatorBase[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
                    The goal of this indicator is to identify long-term buying opportunities in the S&P500 and Dow Industrials.

                Source: http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:coppock_curve

    

    CoppockCurve()

    CoppockCurve(shortRocPeriod: int, longRocPeriod: int, lwmaPeriod: int)

    CoppockCurve(name: str, shortRocPeriod: int, longRocPeriod: int, lwmaPeriod: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: CoppockCurve, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: CoppockCurve)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type)

        __new__(cls: type, shortRocPeriod: int, longRocPeriod: int, lwmaPeriod: int)

        __new__(cls: type, name: str, shortRocPeriod: int, longRocPeriod: int, lwmaPeriod: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: CoppockCurve) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: CoppockCurve) -> int



"""



class Delay(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    An indicator that delays its input for a certain period

    

    Delay(period: int)

    Delay(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Delay, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: Delay) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: Delay) -> int



"""



class DetrendedPriceOscillator(IndicatorBase[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Detrended Price Oscillator is an indicator designed to remove trend from price

                and make it easier to identify cycles.

                DPO does not extend to the last date because it is based on a displaced moving average.

                Is estimated as Price {X/2 + 1} periods ago less the X-period simple moving average.

                E.g.DPO(20) equals price 11 days ago less the 20-day SMA.

    

    DetrendedPriceOscillator(name: str, period: int)

    DetrendedPriceOscillator(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: DetrendedPriceOscillator, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: DetrendedPriceOscillator)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: DetrendedPriceOscillator) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: DetrendedPriceOscillator) -> int



"""



class DonchianChannel(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the upper and lower band of the Donchian Channel.

                The upper band is computed by finding the highest high over the given period.

                The lower band is computed by finding the lowest low over the given period.

                The primary output value of the indicator is the mean of the upper and lower band for 

                the given timeframe.

    

    DonchianChannel(period: int)

    DonchianChannel(upperPeriod: int, lowerPeriod: int)

    DonchianChannel(name: str, period: int)

    DonchianChannel(name: str, upperPeriod: int, lowerPeriod: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: DonchianChannel, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator, which by 

             convention is the mean value of the upper band 

             and lower band.
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
        Reset(self: DonchianChannel)

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
        __new__(cls: type, period: int)

        __new__(cls: type, upperPeriod: int, lowerPeriod: int)

        __new__(cls: type, name: str, period: int)

        __new__(cls: type, name: str, upperPeriod: int, lowerPeriod: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: DonchianChannel) -> bool



"""

    LowerBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the lower band of the Donchian Channel.



Get: LowerBand(self: DonchianChannel) -> IndicatorBase[IndicatorDataPoint]



"""

    UpperBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the upper band of the Donchian Channel.



Get: UpperBand(self: DonchianChannel) -> IndicatorBase[IndicatorDataPoint]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: DonchianChannel) -> int



"""



class DoubleExponentialMovingAverage(IndicatorBase[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Double Exponential Moving Average (DEMA).

                The Double Exponential Moving Average is calculated with the following formula:

                EMA2 = EMA(EMA(t,period),period)

                DEMA = 2 * EMA(t,period) - EMA2

                The Generalized DEMA (GD) is calculated with the following formula:

                GD = (volumeFactor+1) * EMA(t,period) - volumeFactor * EMA2

    

    DoubleExponentialMovingAverage(name: str, period: int, volumeFactor: Decimal)

    DoubleExponentialMovingAverage(period: int, volumeFactor: Decimal)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: DoubleExponentialMovingAverage, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: DoubleExponentialMovingAverage)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int, volumeFactor: Decimal)

        __new__(cls: type, period: int, volumeFactor: Decimal)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: DoubleExponentialMovingAverage) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: DoubleExponentialMovingAverage) -> int



"""



class ExponentialMovingAverage(Indicator, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional exponential moving average indicator (EMA)

    

    ExponentialMovingAverage(name: str, period: int)

    ExponentialMovingAverage(name: str, period: int, smoothingFactor: Decimal)

    ExponentialMovingAverage(period: int)

    ExponentialMovingAverage(period: int, smoothingFactor: Decimal)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ExponentialMovingAverage, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    @staticmethod
    def SmoothingFactorDefault(period):
        """
        SmoothingFactorDefault(period: int) -> Decimal

        

            Calculates the default smoothing factor for an 

             ExponentialMovingAverage indicator

        

        

            period: The period of the EMA

            Returns: The default smoothing factor
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, name: str, period: int, smoothingFactor: Decimal)

        __new__(cls: type, period: int)

        __new__(cls: type, period: int, smoothingFactor: Decimal)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: ExponentialMovingAverage) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: ExponentialMovingAverage) -> int



"""



class FilteredIdentity(IndicatorBase[IBaseData], IIndicator[IBaseData], IComparable[IIndicator[IBaseData]], IComparable, IIndicator):
    """
    Represents an indicator that is a ready after ingesting a single sample and

                always returns the same value as it is given if it passes a filter condition

    

    FilteredIdentity(name: str, filter: Func[IBaseData, bool])
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: FilteredIdentity, input: IBaseData) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseData], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseData], input: IBaseData) -> IndicatorResult """
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
    def __new__(self, name, filter):
        """ __new__(cls: type, name: str, filter: Func[IBaseData, bool]) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: FilteredIdentity) -> bool



"""



class FisherTransform(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Fisher transform is a mathematical process which is used to convert any data set to a modified

                 data set whose Probability Distribution Function is approximately Gaussian. Once the Fisher transform

                 is computed, the transformed data can then be analyzed in terms of it's deviation from the mean.

                

                 The equation is y = .5 * ln [ 1 + x / 1 - x ] where

                 x is the input

                 y is the output

                 ln is the natural logarithm

                

                 The Fisher transform has much sharper turning points than other indicators such as MACD

                

                 For more info, read chapter 1 of Cybernetic Analysis for Stocks and Futures by John F. Ehlers

                

                 We are implementing the latest version of this indicator found at Fig. 4 of

                 http://www.mesasoftware.com/papers/UsingTheFisherTransform.pdf

    

    FisherTransform(period: int)

    FisherTransform(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: FisherTransform, input: IBaseDataBar) -> Decimal

        

            Computes the next value in the transform.

               

                   value1 is a function used to normalize 

             price withing the last _period day range.

               

                   value1 is centered on its midpoint and then 

             doubled so that value1 wil swing between -1 and 

             +1.

                     value1 is also smoothed with an 

             exponential moving average whose alpha is 0.33.

         

                        

                     Since the smoothing may 

             allow value1 to exceed the _period day price 

             range, limits are introduced to

                     

             preclude the transform from blowing up by having 

             an input larger than unity.

        

        

            input: IndicatorDataPoint - the time and value of the 

             next price
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
        Reset(self: FisherTransform)

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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: FisherTransform) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: FisherTransform) -> int



"""



class FractalAdaptiveMovingAverage(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Fractal Adaptive Moving Average (FRAMA) by John Ehlers

    

    FractalAdaptiveMovingAverage(name: str, n: int, longPeriod: int)

    FractalAdaptiveMovingAverage(n: int, longPeriod: int)

    FractalAdaptiveMovingAverage(n: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: FractalAdaptiveMovingAverage, input: IBaseDataBar) -> Decimal

        

            Computes the average value

        

            input: The data for the calculation

            Returns: The average value
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
        Reset(self: FractalAdaptiveMovingAverage)

            Resets the average to its initial state
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
        __new__(cls: type, name: str, n: int, longPeriod: int)

        __new__(cls: type, n: int, longPeriod: int)

        __new__(cls: type, n: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns whether the indicator will return valid results



Get: IsReady(self: FractalAdaptiveMovingAverage) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: FractalAdaptiveMovingAverage) -> int



"""



class FunctionalIndicator(IndicatorBase[T], IIndicator[T], IComparable[IIndicator[T]], IComparable, IIndicator):
    """
    FunctionalIndicator[T](name: str, computeNextValue: Func[T, Decimal], isReady: Func[IndicatorBase[T], bool])

    FunctionalIndicator[T](name: str, computeNextValue: Func[T, Decimal], isReady: Func[IndicatorBase[T], bool], reset: Action)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: FunctionalIndicator[T], input: T) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[T], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: FunctionalIndicator[T])

            Resets this indicator to its initial state, 

             optionally using the reset action passed via the 

             constructor
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """
        ValidateAndComputeNextValue(self: IndicatorBase[T], input: T) -> IndicatorResult

        

            Computes the next value of this indicator from 

             the given state

                    and returns an 

             instance of the 

             QuantConnect.Indicators.IndicatorResult class

        

        

            input: The input given to the indicator

            Returns: An IndicatorResult object including the status of 

             the indicator
        """
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
    def __new__(self, name, computeNextValue, isReady, reset=None):
        """
        __new__(cls: type, name: str, computeNextValue: Func[T, Decimal], isReady: Func[IndicatorBase[T], bool])

        __new__(cls: type, name: str, computeNextValue: Func[T, Decimal], isReady: Func[IndicatorBase[T], bool], reset: Action)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: FunctionalIndicator[T]) -> bool



"""



class HeikinAshi(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Heikin-Ashi bar (HA)

                The Heikin-Ashi bar is calculated using the following formulas:

                HA_Close[0] = (Open[0] + High[0] + Low[0] + Close[0]) / 4

                HA_Open[0] = (HA_Open[1] + HA_Close[1]) / 2

                HA_High[0] = MAX(High[0], HA_Open[0], HA_Close[0])

                HA_Low[0] = MIN(Low[0], HA_Open[0], HA_Close[0])

    

    HeikinAshi(name: str)

    HeikinAshi()
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: HeikinAshi, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
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
        Reset(self: HeikinAshi)

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

    Close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Heikin-Ashi Close



Get: Close(self: HeikinAshi) -> IndicatorBase[IndicatorDataPoint]



"""

    CurrentBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Heikin-Ashi current TradeBar



Get: CurrentBar(self: HeikinAshi) -> TradeBar



"""

    High = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Heikin-Ashi High



Get: High(self: HeikinAshi) -> IndicatorBase[IndicatorDataPoint]



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: HeikinAshi) -> bool



"""

    Low = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Heikin-Ashi Low



Get: Low(self: HeikinAshi) -> IndicatorBase[IndicatorDataPoint]



"""

    Open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Heikin-Ashi Open



Get: Open(self: HeikinAshi) -> IndicatorBase[IndicatorDataPoint]



"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Heikin-Ashi Volume



Get: Volume(self: HeikinAshi) -> IndicatorBase[IndicatorDataPoint]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: HeikinAshi) -> int



"""



class HullMovingAverage(IndicatorBase[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Produces a Hull Moving Average as explained at http://www.alanhull.com/hull-moving-average/

                and derived from the instructions for the Excel VBA code at http://finance4traders.blogspot.com/2009/06/how-to-calculate-hull-moving-average.html

    

    HullMovingAverage(name: str, period: int)

    HullMovingAverage(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: HullMovingAverage, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: HullMovingAverage)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: HullMovingAverage) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: HullMovingAverage) -> int



"""



class IchimokuKinkoHyo(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Ichimoku Kinko Hyo indicator. It consists of the following main indicators:

                Tenkan-sen: (Highest High + Lowest Low) / 2 for the specific period (normally 9)

                Kijun-sen: (Highest High + Lowest Low) / 2 for the specific period (normally 26)

                Senkou A Span: (Tenkan-sen + Kijun-sen )/ 2 from a specific number of periods ago (normally 26)

                Senkou B Span: (Highest High + Lowest Low) / 2 for the specific period (normally 52), from a specific number of periods ago (normally 26)

    

    IchimokuKinkoHyo(tenkanPeriod: int, kijunPeriod: int, senkouAPeriod: int, senkouBPeriod: int, senkouADelayPeriod: int, senkouBDelayPeriod: int)

    IchimokuKinkoHyo(name: str, tenkanPeriod: int, kijunPeriod: int, senkouAPeriod: int, senkouBPeriod: int, senkouADelayPeriod: int, senkouBDelayPeriod: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: IchimokuKinkoHyo, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator
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
        Reset(self: IchimokuKinkoHyo)

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
        __new__(cls: type, tenkanPeriod: int, kijunPeriod: int, senkouAPeriod: int, senkouBPeriod: int, senkouADelayPeriod: int, senkouBDelayPeriod: int)

        __new__(cls: type, name: str, tenkanPeriod: int, kijunPeriod: int, senkouAPeriod: int, senkouBPeriod: int, senkouADelayPeriod: int, senkouBDelayPeriod: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Chikou = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Chikou Span component of the Ichimoku indicator



Get: Chikou(self: IchimokuKinkoHyo) -> IndicatorBase[IndicatorDataPoint]



"""

    DelayedKijunSenkouA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Delayed Kijun Senkou A component of the Ichimoku indicator



Get: DelayedKijunSenkouA(self: IchimokuKinkoHyo) -> WindowIndicator[IndicatorDataPoint]



"""

    DelayedMaximumSenkouB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Delayed Maximum Senkou B component of the Ichimoku indicator



Get: DelayedMaximumSenkouB(self: IchimokuKinkoHyo) -> WindowIndicator[IndicatorDataPoint]



"""

    DelayedMinimumSenkouB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Delayed Minimum Senkou B component of the Ichimoku indicator



Get: DelayedMinimumSenkouB(self: IchimokuKinkoHyo) -> WindowIndicator[IndicatorDataPoint]



"""

    DelayedTenkanSenkouA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Delayed Tenkan Senkou A component of the Ichimoku indicator



Get: DelayedTenkanSenkouA(self: IchimokuKinkoHyo) -> WindowIndicator[IndicatorDataPoint]



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if all of the sub-components of the Ichimoku indicator is ready



Get: IsReady(self: IchimokuKinkoHyo) -> bool



"""

    Kijun = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Kijun-sen component of the Ichimoku indicator



Get: Kijun(self: IchimokuKinkoHyo) -> IndicatorBase[IndicatorDataPoint]



"""

    KijunMaximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Kijun-sen Maximum component of the Ichimoku indicator



Get: KijunMaximum(self: IchimokuKinkoHyo) -> IndicatorBase[IndicatorDataPoint]



"""

    KijunMinimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Kijun-sen Minimum component of the Ichimoku indicator



Get: KijunMinimum(self: IchimokuKinkoHyo) -> IndicatorBase[IndicatorDataPoint]



"""

    SenkouA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Senkou A Span component of the Ichimoku indicator



Get: SenkouA(self: IchimokuKinkoHyo) -> IndicatorBase[IndicatorDataPoint]



"""

    SenkouB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Senkou B Span component of the Ichimoku indicator



Get: SenkouB(self: IchimokuKinkoHyo) -> IndicatorBase[IndicatorDataPoint]



"""

    SenkouBMaximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Senkou B Maximum component of the Ichimoku indicator



Get: SenkouBMaximum(self: IchimokuKinkoHyo) -> IndicatorBase[IndicatorDataPoint]



"""

    SenkouBMinimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Senkou B Minimum component of the Ichimoku indicator



Get: SenkouBMinimum(self: IchimokuKinkoHyo) -> IndicatorBase[IndicatorDataPoint]



"""

    Tenkan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Tenkan-sen component of the Ichimoku indicator



Get: Tenkan(self: IchimokuKinkoHyo) -> IndicatorBase[IndicatorDataPoint]



"""

    TenkanMaximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Tenkan-sen Maximum component of the Ichimoku indicator



Get: TenkanMaximum(self: IchimokuKinkoHyo) -> IndicatorBase[IndicatorDataPoint]



"""

    TenkanMinimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Tenkan-sen Minimum component of the Ichimoku indicator



Get: TenkanMinimum(self: IchimokuKinkoHyo) -> IndicatorBase[IndicatorDataPoint]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: IchimokuKinkoHyo) -> int



"""



class Identity(Indicator, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator):
    """
    Represents an indicator that is a ready after ingesting a single sample and

                    always returns the same value as it is given.

    

    Identity(name: str)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Identity, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: Identity) -> bool



"""



class IndicatorBase(object, IIndicator[T], IComparable[IIndicator[T]], IComparable, IIndicator):
    # no doc
    def CompareTo(self, *__args):
        """
        CompareTo(self: IndicatorBase[T], other: IIndicator[T]) -> int

        

            Compares the current object with another object 

             of the same type.

        

        

            other: An object to compare with this object.

            Returns: A value that indicates the relative order of the 

             objects being compared. The return value has the 

             following meanings: Value Meaning Less than zero 

             This object is less than the other parameter.Zero 

             This object is equal to other. Greater than zero 

             This object is greater than other.

        

        CompareTo(self: IndicatorBase[T], obj: object) -> int

        

            Compares the current instance with another object 

             of the same type and returns an integer that 

             indicates whether the current instance precedes, 

             follows, or occurs in the same position in the 

             sort order as the other object.

        

        

            obj: An object to compare with this instance.

            Returns: A value that indicates the relative order of the 

             objects being compared. The return value has 

             these meanings: Value Meaning Less than zero This 

             instance precedes obj in the sort order. Zero 

             This instance occurs in the same position in the 

             sort order as obj. Greater than zero This 

             instance follows obj in the sort order.
        """
        pass

    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: IndicatorBase[T], input: T) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: IndicatorBase[T], obj: object) -> bool

        

            Determines whether the specified object is equal 

             to the current object.

        

        

            obj: The object to compare with the current object.

            Returns: true if the specified object  is equal to the 

             current object; otherwise, false.
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[T], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: IndicatorBase[T])

            Resets this indicator to its initial state
        """
        pass

    def ToDetailedString(self):
        """
        ToDetailedString(self: IndicatorBase[T]) -> str

        

            Provides a more detailed string of this indicator 

             in the form of {Name} - {Value}

        

            Returns: A detailed string of this indicator's current 

             state
        """
        pass

    def ToString(self):
        """
        ToString(self: IndicatorBase[T]) -> str

        

            ToString Overload for Indicator Base

            Returns: String representation of the indicator
        """
        pass

    def Update(self, *__args):
        """
        Update(self: IndicatorBase[T], input: IBaseData) -> bool

        

            Updates the state of this indicator with the 

             given value and returns true

                    if this 

             indicator is ready, false otherwise

        

        

            input: The value to use to update this indicator

            Returns: True if this indicator is ready, false otherwise

        Update(self: IndicatorBase[T], time: DateTime, value: Decimal) -> bool

        

            Updates the state of this indicator with the 

             given value and returns true

                    if this 

             indicator is ready, false otherwise

        

        

            time: The time associated with the value

            value: The value to use to update this indicator

            Returns: True if this indicator is ready, false otherwise
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """
        ValidateAndComputeNextValue(self: IndicatorBase[T], input: T) -> IndicatorResult

        

            Computes the next value of this indicator from 

             the given state

                    and returns an 

             instance of the 

             QuantConnect.Indicators.IndicatorResult class

        

        

            input: The input given to the indicator

            Returns: An IndicatorResult object including the status of 

             the indicator
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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
        """ __new__(cls: type, name: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current state of this indicator. If the state has not been updated

            then the time on the value will equal DateTime.MinValue.



Get: Current(self: IndicatorBase[T]) -> IndicatorDataPoint



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: IndicatorBase[T]) -> bool



"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a name for this indicator



Get: Name(self: IndicatorBase[T]) -> str



"""

    Samples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of samples processed by this indicator



Get: Samples(self: IndicatorBase[T]) -> Int64



"""


    Updated = None


class IndicatorExtensions(object):
    """ Provides extension methods for Indicator """
    @staticmethod
    def EMA(left, period, smoothingFactor, waitForFirstToReady):
        """
        EMA[T](left: IndicatorBase[T], period: int, smoothingFactor: Nullable[Decimal], waitForFirstToReady: bool) -> ExponentialMovingAverage

        EMA(left: PyObject, period: int, smoothingFactor: Nullable[Decimal], waitForFirstToReady: bool) -> ExponentialMovingAverage
        """
        pass

    @staticmethod
    def MAX(left, period, waitForFirstToReady):
        """
        MAX(left: IIndicator, period: int, waitForFirstToReady: bool) -> Maximum

        

            Creates a new Maximum indicator with the 

             specified period from the left indicator

        

        

            left: The Maximum indicator will be created using the 

             data from left

        

            period: The period of the Maximum indicator

            waitForFirstToReady: True to only send updates to the second if 

             left.IsReady returns true, false to alway send 

             updates

        

            Returns: A reference to the Maximum indicator to allow for 

             method chaining

        

        MAX(left: PyObject, period: int, waitForFirstToReady: bool) -> Maximum

        

            Creates a new Maximum indicator with the 

             specified period from the left indicator

        

        

            left: The Maximum indicator will be created using the 

             data from left

        

            period: The period of the Maximum indicator

            waitForFirstToReady: True to only send updates to the second if 

             left.IsReady returns true, false to alway send 

             updates

        

            Returns: A reference to the Maximum indicator to allow for 

             method chaining
        """
        pass

    @staticmethod
    def MIN(left, period, waitForFirstToReady):
        """
        MIN[T](left: IndicatorBase[T], period: int, waitForFirstToReady: bool) -> Minimum

        MIN(left: PyObject, period: int, waitForFirstToReady: bool) -> Minimum

        

            Creates a new Minimum indicator with the 

             specified period from the left indicator

        

        

            left: The Minimum indicator will be created using the 

             data from left

        

            period: The period of the Minimum indicator

            waitForFirstToReady: True to only send updates to the second if 

             left.IsReady returns true, false to alway send 

             updates

        

            Returns: A reference to the Minimum indicator to allow for 

             method chaining
        """
        pass

    @staticmethod
    def Minus(left, *__args):
        """
        Minus[T](left: IndicatorBase[T], constant: Decimal) -> CompositeIndicator[T]

        Minus[T](left: IndicatorBase[T], right: IndicatorBase[T]) -> CompositeIndicator[T]

        Minus[T](left: IndicatorBase[T], right: IndicatorBase[T], name: str) -> CompositeIndicator[T]

        Minus(left: PyObject, constant: Decimal) -> object

        

            Creates a new CompositeIndicator such that the 

             result will be the difference of the left and 

             constant

        

        

            left: The left indicator

            constant: The subtrahend

            Returns: The difference of the left and right indicators

        Minus(left: PyObject, right: PyObject, name: str) -> object

        

            Creates a new CompositeIndicator such that the 

             result will be the difference of the left and 

             right

        

        

            left: The left indicator

            right: The right indicator

            name: The name of this indicator

            Returns: The difference of the left and right indicators
        """
        pass

    @staticmethod
    def Of(second, first, waitForFirstToReady):
# Error generating skeleton for function Of: Method must be called on a Type for which Type.IsGenericParameter is false.

    @staticmethod
    def Over(left, *__args):
        """
        Over[T](left: IndicatorBase[T], constant: Decimal) -> CompositeIndicator[T]

        Over[T](left: IndicatorBase[T], right: IndicatorBase[T]) -> CompositeIndicator[T]

        Over[T](left: IndicatorBase[T], right: IndicatorBase[T], name: str) -> CompositeIndicator[T]

        Over(left: PyObject, constant: Decimal) -> object

        

            Creates a new CompositeIndicator such that the 

             result will be the ratio of the left to the 

             constant

        

        

            left: The left indicator

            constant: The constant value denominator

            Returns: The ratio of the left to the right indicator

        Over(left: PyObject, right: PyObject, name: str) -> object

        

            Creates a new CompositeIndicator such that the 

             result will be the ratio of the left to the right

        

        

            left: The left indicator

            right: The right indicator

            name: The name of this indicator

            Returns: The ratio of the left to the right indicator
        """
        pass

    @staticmethod
    def Plus(left, *__args):
        """
        Plus[T](left: IndicatorBase[T], constant: Decimal) -> CompositeIndicator[T]

        Plus[T](left: IndicatorBase[T], right: IndicatorBase[T]) -> CompositeIndicator[T]

        Plus[T](left: IndicatorBase[T], right: IndicatorBase[T], name: str) -> CompositeIndicator[T]

        Plus(left: PyObject, constant: Decimal) -> object

        

            Creates a new CompositeIndicator such that the 

             result will be the sum of the left and the 

             constant

        

        

            left: The left indicator

            constant: The addend

            Returns: The sum of the left and right indicators

        Plus(left: PyObject, right: PyObject, name: str) -> object

        

            Creates a new CompositeIndicator such that the 

             result will be the sum of the left and right

        

        

            left: The left indicator

            right: The right indicator

            name: The name of this indicator

            Returns: The sum of the left and right indicators
        """
        pass

    @staticmethod
    def SMA(left, period, waitForFirstToReady):
        """
        SMA[T](left: IndicatorBase[T], period: int, waitForFirstToReady: bool) -> SimpleMovingAverage

        SMA(left: PyObject, period: int, waitForFirstToReady: bool) -> SimpleMovingAverage

        

            Initializes a new instance of the 

             SimpleMovingAverage class with the specified name 

             and period from the left indicator

        

        

            left: The SimpleMovingAverage indicator will be created 

             using the data from left

        

            period: The period of the SMA

            waitForFirstToReady: True to only send updates to the second if 

             first.IsReady returns true, false to alway send 

             updates to second

        

            Returns: The reference to the SimpleMovingAverage 

             indicator to allow for method chaining
        """
        pass

    @staticmethod
    def Times(left, *__args):
        """
        Times[T](left: IndicatorBase[T], constant: Decimal) -> CompositeIndicator[T]

        Times[T](left: IndicatorBase[T], right: IndicatorBase[T]) -> CompositeIndicator[T]

        Times[T](left: IndicatorBase[T], right: IndicatorBase[T], name: str) -> CompositeIndicator[T]

        Times(left: PyObject, constant: Decimal) -> object

        

            Creates a new CompositeIndicator such that the 

             result will be the product of the left and the 

             constant

        

        

            left: The left indicator

            constant: The constant value to multiple by

            Returns: The product of the left to the right indicators

        Times(left: PyObject, right: PyObject, name: str) -> object

        

            Creates a new CompositeIndicator such that the 

             result will be the product of the left to the 

             right

        

        

            left: The left indicator

            right: The right indicator

            name: The name of this indicator

            Returns: The product of the left to the right indicators
        """
        pass

    @staticmethod
    def Update(indicator, time, value):
        """ Update(indicator: IndicatorBase[IndicatorDataPoint], time: DateTime, value: Decimal) -> bool """
        pass

    @staticmethod
    def WeightedBy(value, weight, period):
        """
        WeightedBy[(T, TWeight)](value: IndicatorBase[T], weight: TWeight, period: int) -> CompositeIndicator[IndicatorDataPoint]

        WeightedBy(value: PyObject, weight: PyObject, period: int) -> CompositeIndicator[IndicatorDataPoint]

        

            Creates a new CompositeIndicator such that the 

             result will be average of a first indicator 

             weighted by a second one

        

        

            value: Indicator that will be averaged

            weight: Indicator that provides the average weights

            period: Average period

            Returns: Indicator that results of the average of first by 

             weights given by second
        """
        pass

    __all__ = [
        'EMA',
        'MAX',
        'MIN',
        'Minus',
        'Of',
        'Over',
        'Plus',
        'SMA',
        'Times',
        'Update',
        'WeightedBy',
    ]


class IndicatorResult(object):
    """
    Represents the result of an indicator's calculations

    

    IndicatorResult(value: Decimal, status: IndicatorStatus)
    """
    @staticmethod # known case of __new__
    def __new__(self, value, status):
        """ __new__(cls: type, value: Decimal, status: IndicatorStatus) """
        pass

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The indicator status



Get: Status(self: IndicatorResult) -> IndicatorStatus



"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The indicator output value



Get: Value(self: IndicatorResult) -> Decimal



"""



class IndicatorStatus(Enum, IComparable, IFormattable, IConvertible):
    """
    The possible states returned by QuantConnect.Indicators.IndicatorBase

    

    enum IndicatorStatus, values: InvalidInput (1), MathError (2), Success (0)
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

    InvalidInput = None
    MathError = None
    Success = None
    value__ = None


class IntradayVwap(IndicatorBase[BaseData], IIndicator[BaseData], IComparable[IIndicator[BaseData]], IComparable, IIndicator):
    """
    Defines the canonical intraday VWAP indicator

    

    IntradayVwap(name: str)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: IntradayVwap, input: BaseData) -> Decimal

        

            Computes the next value of this indicator from 

             the given state.

                    NOTE: This must be 

             overriden since it's abstract in the base, but

          

                       will never be invoked since we've 

             override the validate method above.

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[BaseData], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def TryGetVolumeAndAveragePrice(self, *args): #cannot find CLR method
        """
        TryGetVolumeAndAveragePrice(self: IntradayVwap, input: BaseData) -> (bool, Decimal, Decimal)

        

            Determines the volume and price to be used for 

             the current input in the VWAP computation
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """
        ValidateAndComputeNextValue(self: IntradayVwap, input: BaseData) -> IndicatorResult

        

            Computes the new VWAP
        """
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
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: IntradayVwap) -> bool



"""



class KaufmanAdaptiveMovingAverage(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Kaufman Adaptive Moving Average (KAMA).

                The Kaufman Adaptive Moving Average is calculated as explained here:

                http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:kaufman_s_adaptive_moving_average

    

    KaufmanAdaptiveMovingAverage(name: str, period: int, fastEmaPeriod: int, slowEmaPeriod: int)

    KaufmanAdaptiveMovingAverage(period: int, fastEmaPeriod: int, slowEmaPeriod: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: KaufmanAdaptiveMovingAverage, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: KaufmanAdaptiveMovingAverage)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int, fastEmaPeriod: int, slowEmaPeriod: int)

        __new__(cls: type, period: int, fastEmaPeriod: int, slowEmaPeriod: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: KaufmanAdaptiveMovingAverage) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: KaufmanAdaptiveMovingAverage) -> int



"""



class KeltnerChannels(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator creates a moving average (middle band) with an upper band and lower band

                fixed at k average true range multiples away from the middle band.

    

    KeltnerChannels(period: int, k: Decimal, movingAverageType: MovingAverageType)

    KeltnerChannels(name: str, period: int, k: Decimal, movingAverageType: MovingAverageType)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: KeltnerChannels, input: IBaseDataBar) -> Decimal

        

            Computes the next value for this indicator from 

             the given state.

        

        

            input: The TradeBar to this indicator on this time step

            Returns: A new value for this indicator
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
        Reset(self: KeltnerChannels)

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
        __new__(cls: type, period: int, k: Decimal, movingAverageType: MovingAverageType)

        __new__(cls: type, name: str, period: int, k: Decimal, movingAverageType: MovingAverageType)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AverageTrueRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the average true range



Get: AverageTrueRange(self: KeltnerChannels) -> IndicatorBase[IBaseDataBar]



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: KeltnerChannels) -> bool



"""

    LowerBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the lower band of the channel



Get: LowerBand(self: KeltnerChannels) -> IndicatorBase[IBaseDataBar]



"""

    MiddleBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the middle band of the channel



Get: MiddleBand(self: KeltnerChannels) -> IndicatorBase[IndicatorDataPoint]



"""

    UpperBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the upper band of the channel



Get: UpperBand(self: KeltnerChannels) -> IndicatorBase[IBaseDataBar]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: KeltnerChannels) -> int



"""



class LeastSquaresMovingAverage(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Least Squares Moving Average (LSMA) first calculates a least squares regression line

                over the preceding time periods, and then projects it forward to the current period. In

                essence, it calculates what the value would be if the regression line continued.

                Source: https://rtmath.net/helpFinAnalysis/html/b3fab79c-f4b2-40fb-8709-fdba43cdb363.htm

    

    LeastSquaresMovingAverage(name: str, period: int)

    LeastSquaresMovingAverage(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: LeastSquaresMovingAverage, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: LeastSquaresMovingAverage)

            Resets this indicator and all sub-indicators 

             (Intercept, Slope)
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The point where the regression line crosses the y-axis (price-axis)



Get: Intercept(self: LeastSquaresMovingAverage) -> IndicatorBase[IndicatorDataPoint]



"""

    Slope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The regression line slope



Get: Slope(self: LeastSquaresMovingAverage) -> IndicatorBase[IndicatorDataPoint]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: LeastSquaresMovingAverage) -> int



"""



class LinearWeightedMovingAverage(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional Weighted Moving Average indicator. The weight are linearly

                 distributed according to the number of periods in the indicator.

                

                 For example, a 4 period indicator will have a numerator of (4 * window[0]) + (3 * window[1]) + (2 * window[2]) + window[3]

                 and a denominator of 4 + 3 + 2 + 1 = 10

                

                 During the warm up period, IsReady will return false, but the LWMA will still be computed correctly because

                 the denominator will be the minimum of Samples factorial or Size factorial and

                 the computation iterates over that minimum value.

                

                 The RollingWindow of inputs is created when the indicator is created.

                 A RollingWindow of LWMAs is not saved.  That is up to the caller.

    

    LinearWeightedMovingAverage(name: str, period: int)

    LinearWeightedMovingAverage(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: LinearWeightedMovingAverage, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: LinearWeightedMovingAverage) -> int



"""



class LogReturn(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents the LogReturn indicator (LOGR)

                - log returns are useful for identifying price convergence/divergence in a given period

                - logr = log (current price / last price in period)

    

    LogReturn(name: str, period: int)

    LogReturn(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: LogReturn, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: LogReturn) -> int



"""



class MassIndex(IndicatorBase[TradeBar], IIndicator[TradeBar], IComparable[IIndicator[TradeBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Mass Index uses the high-low range to identify trend reversals based on range expansions.

                In this sense, the Mass Index is a volatility indicator that does not have a directional

                bias. Instead, the Mass Index identifies range bulges that can foreshadow a reversal of the

                current trend. Developed by Donald Dorsey.

    

    MassIndex(name: str, emaPeriod: int, sumPeriod: int)

    MassIndex(emaPeriod: int, sumPeriod: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: MassIndex, input: TradeBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[TradeBar], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: MassIndex)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[TradeBar], input: TradeBar) -> IndicatorResult """
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
        __new__(cls: type, name: str, emaPeriod: int, sumPeriod: int)

        __new__(cls: type, emaPeriod: int, sumPeriod: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: MassIndex) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: MassIndex) -> int



"""



class Maximum(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents an indicator capable of tracking the maximum value and how many periods ago it occurred

    

    Maximum(period: int)

    Maximum(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Maximum, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Maximum)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: Maximum) -> bool



"""

    PeriodsSinceMaximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of periods since the maximum value was encountered



Get: PeriodsSinceMaximum(self: Maximum) -> int



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: Maximum) -> int



"""



class MeanAbsoluteDeviation(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period mean absolute deviation.

    

    MeanAbsoluteDeviation(period: int)

    MeanAbsoluteDeviation(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: MeanAbsoluteDeviation, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: MeanAbsoluteDeviation)

            Resets this indicator and its sub-indicator Mean 

             to their initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: MeanAbsoluteDeviation) -> bool



"""

    Mean = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the mean used to compute the deviation



Get: Mean(self: MeanAbsoluteDeviation) -> IndicatorBase[IndicatorDataPoint]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: MeanAbsoluteDeviation) -> int



"""



class MidPoint(IndicatorBase[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the MidPoint (MIDPOINT)

                The MidPoint is calculated using the following formula:

                MIDPOINT = (Highest Value + Lowest Value) / 2

    

    MidPoint(name: str, period: int)

    MidPoint(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: MidPoint, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: MidPoint)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: MidPoint) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: MidPoint) -> int



"""



class MidPrice(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the MidPrice (MIDPRICE).

                The MidPrice is calculated using the following formula:

                MIDPRICE = (Highest High + Lowest Low) / 2

    

    MidPrice(name: str, period: int)

    MidPrice(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: MidPrice, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
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
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: MidPrice) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: MidPrice) -> int



"""



class Minimum(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents an indicator capable of tracking the minimum value and how many periods ago it occurred

    

    Minimum(period: int)

    Minimum(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Minimum, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Minimum)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: Minimum) -> bool



"""

    PeriodsSinceMinimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of periods since the minimum value was encountered



Get: PeriodsSinceMinimum(self: Minimum) -> int



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: Minimum) -> int



"""



class Momentum(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period change in a value using the following:

                value_0 - value_n

    

    Momentum(period: int)

    Momentum(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Momentum, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: Momentum) -> int



"""



class RateOfChange(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period rate of change in a value using the following:

                (value_0 - value_n) / value_n

    

    RateOfChange(period: int)

    RateOfChange(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: RateOfChange, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: RateOfChange) -> int



"""



class RateOfChangePercent(RateOfChange, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period percentage rate of change in a value using the following:

                100 * (value_0 - value_n) / value_n

    

    RateOfChangePercent(period: int)

    RateOfChangePercent(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: RateOfChangePercent, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class MomentumPercent(RateOfChangePercent, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period percentage rate of change in a value using the following:

                 100 * (value_0 - value_n) / value_n

                

                 This indicator yields the same results of RateOfChangePercent

    

    MomentumPercent(period: int)

    MomentumPercent(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: RateOfChangePercent, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class MomersionIndicator(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Oscillator indicator that measures momentum and mean-reversion over a specified

                period n.

                Source: Harris, Michael. "Momersion Indicator." Price Action Lab.,

                            13 Aug. 2015. Web. http://www.priceactionlab.com/Blog/2015/08/momersion-indicator/.

    

    MomersionIndicator(name: str, minPeriod: Nullable[int], fullPeriod: int)

    MomersionIndicator(minPeriod: Nullable[int], fullPeriod: int)

    MomersionIndicator(fullPeriod: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: MomersionIndicator, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: MomersionIndicator)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, minPeriod: Nullable[int], fullPeriod: int)

        __new__(cls: type, minPeriod: Nullable[int], fullPeriod: int)

        __new__(cls: type, fullPeriod: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: MomersionIndicator) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: MomersionIndicator) -> int



"""



class MoneyFlowIndex(TradeBarIndicator, IIndicator[TradeBar], IComparable[IIndicator[TradeBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Money Flow Index (MFI) is an oscillator that uses both price and volume to

                 measure buying and selling pressure

                

                 Typical Price = (High + Low + Close)/3

                 Money Flow = Typical Price x Volume

                 Positive Money Flow = Sum of the money flows of all days where the typical

                     price is greater than the previous day's typical price

                 Negative Money Flow = Sum of the money flows of all days where the typical

                     price is less than the previous day's typical price

                 Money Flow Ratio = (14-period Positive Money Flow)/(14-period Negative Money Flow)

                

                 Money Flow Index = 100 x  Positive Money Flow / ( Positive Money Flow + Negative Money Flow)

    

    MoneyFlowIndex(period: int)

    MoneyFlowIndex(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: MoneyFlowIndex, input: TradeBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[TradeBar], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: MoneyFlowIndex)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[TradeBar], input: TradeBar) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: MoneyFlowIndex) -> bool



"""

    NegativeMoneyFlow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sum of negative money flow to compute money flow ratio



Get: NegativeMoneyFlow(self: MoneyFlowIndex) -> IndicatorBase[IndicatorDataPoint]



"""

    PositiveMoneyFlow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sum of positive money flow to compute money flow ratio



Get: PositiveMoneyFlow(self: MoneyFlowIndex) -> IndicatorBase[IndicatorDataPoint]



"""

    PreviousTypicalPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current and previous typical price is used to determine positive or negative money flow



Get: PreviousTypicalPrice(self: MoneyFlowIndex) -> Decimal



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: MoneyFlowIndex) -> int



"""



class MovingAverageType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the different types of moving averages

    

    enum MovingAverageType, values: Alma (10), DoubleExponential (4), Exponential (1), Hull (9), Kama (8), LinearWeightedMovingAverage (3), Simple (0), T3 (7), Triangular (6), TripleExponential (5), Wilders (2)
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

    Alma = None
    DoubleExponential = None
    Exponential = None
    Hull = None
    Kama = None
    LinearWeightedMovingAverage = None
    Simple = None
    T3 = None
    Triangular = None
    TripleExponential = None
    value__ = None
    Wilders = None


class MovingAverageTypeExtensions(object):
    """ Provides extension methods for the MovingAverageType enumeration """
    @staticmethod
    def AsIndicator(movingAverageType, *__args):
        """
        AsIndicator(movingAverageType: MovingAverageType, period: int) -> IndicatorBase[IndicatorDataPoint]

        

            Creates a new indicator from the specified 

             MovingAverageType. So if MovingAverageType.Simple


             
                    is specified, then a new 

             SimpleMovingAverage will be returned.

        

        

            movingAverageType: The type of averaging indicator to create

            period: The smoothing period

            Returns: A new indicator that matches the MovingAverageType

        AsIndicator(movingAverageType: MovingAverageType, name: str, period: int) -> IndicatorBase[IndicatorDataPoint]

        

            Creates a new indicator from the specified 

             MovingAverageType. So if MovingAverageType.Simple


             
                    is specified, then a new 

             SimpleMovingAverage will be returned.

        

        

            movingAverageType: The type of averaging indicator to create

            name: The name of the new indicator

            period: The smoothing period

            Returns: A new indicator that matches the MovingAverageType
        """
        pass

    __all__ = [
        'AsIndicator',
    ]


class NormalizedAverageTrueRange(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Normalized Average True Range (NATR).

                The Normalized Average True Range is calculated with the following formula:

                NATR = (ATR(period) / Close) * 100

    

    NormalizedAverageTrueRange(name: str, period: int)

    NormalizedAverageTrueRange(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: NormalizedAverageTrueRange, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
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
        Reset(self: NormalizedAverageTrueRange)

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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: NormalizedAverageTrueRange) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: NormalizedAverageTrueRange) -> int



"""



class OnBalanceVolume(TradeBarIndicator, IIndicator[TradeBar], IComparable[IIndicator[TradeBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the On Balance Volume (OBV). 

                The On Balance Volume is calculated by determining the price of the current close price and previous close price.

                If the current close price is equivalent to the previous price the OBV remains the same,

                If the current close price is higher the volume of that day is added to the OBV, while a lower close price will

                result in negative value.

    

    OnBalanceVolume()

    OnBalanceVolume(name: str)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: OnBalanceVolume, input: TradeBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[TradeBar], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: OnBalanceVolume)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[TradeBar], input: TradeBar) -> IndicatorResult """
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
        __new__(cls: type)

        __new__(cls: type, name: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: OnBalanceVolume) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: OnBalanceVolume) -> int



"""



class ParabolicStopAndReverse(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Parabolic SAR Indicator 

                Based on TA-Lib implementation

    

    ParabolicStopAndReverse(name: str, afStart: Decimal, afIncrement: Decimal, afMax: Decimal)

    ParabolicStopAndReverse(afStart: Decimal, afIncrement: Decimal, afMax: Decimal)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: ParabolicStopAndReverse, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The trade bar input given to the indicator

            Returns: A new value for this indicator
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
        Reset(self: ParabolicStopAndReverse)

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
        __new__(cls: type, name: str, afStart: Decimal, afIncrement: Decimal, afMax: Decimal)

        __new__(cls: type, afStart: Decimal, afIncrement: Decimal, afMax: Decimal)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: ParabolicStopAndReverse) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: ParabolicStopAndReverse) -> int



"""



class PercentagePriceOscillator(AbsolutePriceOscillator, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Percentage Price Oscillator (PPO)

                The Percentage Price Oscillator is calculated using the following formula:

                PPO[i] = 100 * (FastMA[i] - SlowMA[i]) / SlowMA[i]

    

    PercentagePriceOscillator(name: str, fastPeriod: int, slowPeriod: int, movingAverageType: MovingAverageType)

    PercentagePriceOscillator(fastPeriod: int, slowPeriod: int, movingAverageType: MovingAverageType)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: PercentagePriceOscillator, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, fastPeriod: int, slowPeriod: int, movingAverageType: MovingAverageType)

        __new__(cls: type, fastPeriod: int, slowPeriod: int, movingAverageType: MovingAverageType)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class PythonIndicator(IndicatorBase[IBaseData], IIndicator[IBaseData], IComparable[IIndicator[IBaseData]], IComparable, IIndicator):
    """
    Provides a wrapper for QuantConnect.Indicators.IndicatorBase implementations written in python

    

    PythonIndicator()

    PythonIndicator(*args: Array[PyObject])

    PythonIndicator(indicator: PyObject)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: PythonIndicator, input: IBaseData) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IBaseData], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def SetIndicator(self, indicator):
        """
        SetIndicator(self: PythonIndicator, indicator: PyObject)

            Sets the python implementation of the indicator

        

            indicator: The python implementation of 

             QuantConnect.Indicators.IndicatorBase
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IBaseData], input: IBaseData) -> IndicatorResult """
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
        __new__(cls: type)

        __new__(cls: type, *args: Array[PyObject])

        __new__(cls: type, indicator: PyObject)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: PythonIndicator) -> bool



"""



class RateOfChangeRatio(RateOfChange, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Rate Of Change Ratio (ROCR). 

                The Rate Of Change Ratio is calculated with the following formula:

                ROCR = price / prevPrice

    

    RateOfChangeRatio(name: str, period: int)

    RateOfChangeRatio(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: RateOfChangeRatio, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class RegressionChannel(Indicator, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    The Regression Channel indicator extends the QuantConnect.Indicators.LeastSquaresMovingAverage

                with the inclusion of two (upper and lower) channel lines that are distanced from

                the linear regression line by a user defined number of standard deviations.

                Reference: http://www.onlinetradingconcepts.com/TechnicalAnalysis/LinRegChannel.html

    

    RegressionChannel(name: str, period: int, k: Decimal)

    RegressionChannel(period: int, k: Decimal)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: RegressionChannel, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: RegressionChannel)

            Resets this indicator and all sub-indicators 

             (StandardDeviation, LowerBand, MiddleBand, 

             UpperBand)
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int, k: Decimal)

        __new__(cls: type, period: int, k: Decimal)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The point where the regression line crosses the y-axis (price-axis)



Get: Intercept(self: RegressionChannel) -> IndicatorBase[IndicatorDataPoint]



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: RegressionChannel) -> bool



"""

    LinearRegression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the linear regression



Get: LinearRegression(self: RegressionChannel) -> LeastSquaresMovingAverage



"""

    LowerChannel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the lower channel (linear regression - k * stdDev)



Get: LowerChannel(self: RegressionChannel) -> IndicatorBase[IndicatorDataPoint]



"""

    Slope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The regression line slope



Get: Slope(self: RegressionChannel) -> IndicatorBase[IndicatorDataPoint]



"""

    UpperChannel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the upper channel (linear regression + k * stdDev)



Get: UpperChannel(self: RegressionChannel) -> IndicatorBase[IndicatorDataPoint]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: RegressionChannel) -> int



"""



class RelativeStrengthIndex(Indicator, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents the  Relative Strength Index (RSI) developed by K. Welles Wilder.

                You can optionally specified a different moving average type to be used in the computation

    

    RelativeStrengthIndex(period: int, movingAverageType: MovingAverageType)

    RelativeStrengthIndex(name: str, period: int, movingAverageType: MovingAverageType)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: RelativeStrengthIndex, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: RelativeStrengthIndex)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int, movingAverageType: MovingAverageType)

        __new__(cls: type, name: str, period: int, movingAverageType: MovingAverageType)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AverageGain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the indicator for average gain



Get: AverageGain(self: RelativeStrengthIndex) -> IndicatorBase[IndicatorDataPoint]



"""

    AverageLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the EMA for the down days



Get: AverageLoss(self: RelativeStrengthIndex) -> IndicatorBase[IndicatorDataPoint]



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: RelativeStrengthIndex) -> bool



"""

    MovingAverageType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of indicator used to compute AverageGain and AverageLoss



Get: MovingAverageType(self: RelativeStrengthIndex) -> MovingAverageType



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: RelativeStrengthIndex) -> int



"""



class SimpleMovingAverage(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents the traditional simple moving average indicator (SMA)

    

    SimpleMovingAverage(name: str, period: int)

    SimpleMovingAverage(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: SimpleMovingAverage, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: SimpleMovingAverage)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: SimpleMovingAverage) -> bool



"""

    RollingSum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A rolling sum for computing the average for the given period



Get: RollingSum(self: SimpleMovingAverage) -> IndicatorBase[IndicatorDataPoint]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: SimpleMovingAverage) -> int



"""



class Variance(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period population variance.

    

    Variance(period: int)

    Variance(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Variance, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Variance)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: Variance) -> int



"""



class StandardDeviation(Variance, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the n-period population standard deviation.

    

    StandardDeviation(period: int)

    StandardDeviation(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: StandardDeviation, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class Stochastic(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Slow Stochastics %K and %D. The Fast Stochastics %K is is computed by 

                (Current Close Price - Lowest Price of given Period) / (Highest Price of given Period - Lowest Price of given Period)

                multiplied by 100. Once the Fast Stochastics %K is calculated the Slow Stochastic %K is calculated by the average/smoothed price of

                of the Fast %K with the given period. The Slow Stochastics %D is then derived from the Slow Stochastics %K with the given period.

    

    Stochastic(name: str, period: int, kPeriod: int, dPeriod: int)

    Stochastic(period: int, kPeriod: int, dPeriod: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Stochastic, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator
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
        Reset(self: Stochastic)

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
        __new__(cls: type, name: str, period: int, kPeriod: int, dPeriod: int)

        __new__(cls: type, period: int, kPeriod: int, dPeriod: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FastStoch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the Fast Stochastics %K given Period.



Get: FastStoch(self: Stochastic) -> IndicatorBase[IBaseDataBar]



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: Stochastic) -> bool



"""

    StochD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the Slow Stochastics given Period D.



Get: StochD(self: Stochastic) -> IndicatorBase[IBaseDataBar]



"""

    StochK = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the Slow Stochastics given Period K.



Get: StochK(self: Stochastic) -> IndicatorBase[IBaseDataBar]



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: Stochastic) -> int



"""



class Sum(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents an indicator capable of tracking the sum for the given period

    

    Sum(name: str, period: int)

    Sum(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Sum, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Sum)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: Sum) -> int



"""



class SwissArmyKnife(Indicator, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Swiss Army Knife indicator by John Ehlers

    

    SwissArmyKnife(period: int, delta: float, tool: SwissArmyKnifeTool)

    SwissArmyKnife(name: str, period: int, delta: float, tool: SwissArmyKnifeTool)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: SwissArmyKnife, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: SwissArmyKnife)

            Resets to the initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, period: int, delta: float, tool: SwissArmyKnifeTool)

        __new__(cls: type, name: str, period: int, delta: float, tool: SwissArmyKnifeTool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: SwissArmyKnife) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: SwissArmyKnife) -> int



"""



class SwissArmyKnifeTool(Enum, IComparable, IFormattable, IConvertible):
    """
    The tools of the Swiss Army Knife. Some of the tools lend well to chaining with the "Of" Method, others may be treated as moving averages

    

    enum SwissArmyKnifeTool, values: BandPass (4), Butter (1), Gauss (0), HighPass (2), TwoPoleHighPass (3)
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

    BandPass = None
    Butter = None
    Gauss = None
    HighPass = None
    TwoPoleHighPass = None
    value__ = None


class T3MovingAverage(IndicatorBase[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the T3 Moving Average (T3).

                The T3 Moving Average is calculated with the following formula:

                EMA1(x, Period) = EMA(x, Period)

                EMA2(x, Period) = EMA(EMA1(x, Period),Period)

                GD(x, Period, volumeFactor) = (EMA1(x, Period)*(1+volumeFactor)) - (EMA2(x, Period)* volumeFactor)

                T3 = GD(GD(GD(t, Period, volumeFactor), Period, volumeFactor), Period, volumeFactor);

    

    T3MovingAverage(name: str, period: int, volumeFactor: Decimal)

    T3MovingAverage(period: int, volumeFactor: Decimal)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: T3MovingAverage, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: T3MovingAverage)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int, volumeFactor: Decimal)

        __new__(cls: type, period: int, volumeFactor: Decimal)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: T3MovingAverage) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: T3MovingAverage) -> int



"""



class TriangularMovingAverage(Indicator, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Triangular Moving Average (TRIMA). 

                The Triangular Moving Average is calculated with the following formula:

                (1) When the period is even, TRIMA(x,period)=SMA(SMA(x,period/2),(period/2)+1)

                (2) When the period is odd,  TRIMA(x,period)=SMA(SMA(x,(period+1)/2),(period+1)/2)

    

    TriangularMovingAverage(name: str, period: int)

    TriangularMovingAverage(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: TriangularMovingAverage, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: TriangularMovingAverage)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: TriangularMovingAverage) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: TriangularMovingAverage) -> int



"""



class TripleExponentialMovingAverage(IndicatorBase[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Triple Exponential Moving Average (TEMA). 

                The Triple Exponential Moving Average is calculated with the following formula:

                EMA1 = EMA(t,period)

                EMA2 = EMA(EMA(t,period),period)

                EMA3 = EMA(EMA(EMA(t,period),period),period)

                TEMA = 3 * EMA1 - 3 * EMA2 + EMA3

    

    TripleExponentialMovingAverage(name: str, period: int)

    TripleExponentialMovingAverage(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: TripleExponentialMovingAverage, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: TripleExponentialMovingAverage)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: TripleExponentialMovingAverage) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: TripleExponentialMovingAverage) -> int



"""



class Trix(Indicator, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the TRIX (1-period ROC of a Triple EMA)

                The TRIX is calculated as explained here:

                http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:trix

    

    Trix(name: str, period: int)

    Trix(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: Trix, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: Trix)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: Trix) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: Trix) -> int



"""



class TrueRange(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the True Range (TR).

                The True Range is the greatest of the following values:

                value1 = distance from today's high to today's low.

                value2 = distance from yesterday's close to today's high.

                value3 = distance from yesterday's close to today's low.

    

    TrueRange()

    TrueRange(name: str)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: TrueRange, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
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
        __new__(cls: type)

        __new__(cls: type, name: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: TrueRange) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: TrueRange) -> int



"""



class UltimateOscillator(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    This indicator computes the Ultimate Oscillator (ULTOSC)

                The Ultimate Oscillator is calculated as explained here:

                http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:ultimate_oscillator

    

    UltimateOscillator(period1: int, period2: int, period3: int)

    UltimateOscillator(name: str, period1: int, period2: int, period3: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: UltimateOscillator, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
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
        Reset(self: UltimateOscillator)

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
        __new__(cls: type, period1: int, period2: int, period3: int)

        __new__(cls: type, name: str, period1: int, period2: int, period3: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: UltimateOscillator) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: UltimateOscillator) -> int



"""



class VolumeWeightedAveragePriceIndicator(TradeBarIndicator, IIndicator[TradeBar], IComparable[IIndicator[TradeBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Volume Weighted Average Price (VWAP) Indicator:

                It is calculated by adding up the dollars traded for every transaction (price multiplied

                by number of shares traded) and then dividing by the total shares traded for the day.

    

    VolumeWeightedAveragePriceIndicator(period: int)

    VolumeWeightedAveragePriceIndicator(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: VolumeWeightedAveragePriceIndicator, input: TradeBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def GetTimeWeightedAveragePrice(self, *args): #cannot find CLR method
        """
        GetTimeWeightedAveragePrice(self: VolumeWeightedAveragePriceIndicator, input: TradeBar) -> Decimal

        

            Gets an estimated average price to use for the 

             interval covered by the input trade bar.

        

        

            input: The current trade bar input

            Returns: An estimated average price over the trade bar's 

             interval
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[TradeBar], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: VolumeWeightedAveragePriceIndicator)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[TradeBar], input: TradeBar) -> IndicatorResult """
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: VolumeWeightedAveragePriceIndicator) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: VolumeWeightedAveragePriceIndicator) -> int



"""



class WilderMovingAverage(Indicator, IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Represents the moving average indicator defined by Welles Wilder in his book:

                New Concepts in Technical Trading Systems.

    

    WilderMovingAverage(name: str, period: int)

    WilderMovingAverage(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: WilderMovingAverage, input: IndicatorDataPoint) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: WilderMovingAverage)

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: WilderMovingAverage) -> bool



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: WilderMovingAverage) -> int



"""



class WilliamsPercentR(BarIndicator, IIndicator[IBaseDataBar], IComparable[IIndicator[IBaseDataBar]], IComparable, IIndicator, IIndicatorWarmUpPeriodProvider):
    """
    Williams %R, or just %R, is the current closing price in relation to the high and low of

                the past N days (for a given N). The value of this indicator fluctuates between -100 and 0.

                The symbol is said to be oversold when the oscillator is below -80%,

                and overbought when the oscillator is above -20%.

    

    WilliamsPercentR(period: int)

    WilliamsPercentR(name: str, period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: WilliamsPercentR, input: IBaseDataBar) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator
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
        Reset(self: WilliamsPercentR)

            Resets this indicator and both sub-indicators 

             (Max and Min)
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
        __new__(cls: type, period: int)

        __new__(cls: type, name: str, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: WilliamsPercentR) -> bool



"""

    Maximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Maximum indicator



Get: Maximum(self: WilliamsPercentR) -> Maximum



"""

    Minimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Minimum indicator



Get: Minimum(self: WilliamsPercentR) -> Minimum



"""

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: WilliamsPercentR) -> int



"""



class WindowIdentity(WindowIndicator[IndicatorDataPoint], IIndicator[IndicatorDataPoint], IComparable[IIndicator[IndicatorDataPoint]], IComparable, IIndicator):
    """
    Represents an indicator that is a ready after ingesting enough samples (# samples > period) 

                and always returns the same value as it is given.

    

    WindowIdentity(name: str, period: int)

    WindowIdentity(period: int)
    """
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: WindowIdentity, window: IReadOnlyWindow[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal

        ComputeNextValue(self: WindowIndicator[IndicatorDataPoint], input: IndicatorDataPoint) -> Decimal
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[IndicatorDataPoint], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """ ValidateAndComputeNextValue(self: IndicatorBase[IndicatorDataPoint], input: IndicatorDataPoint) -> IndicatorResult """
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
        __new__(cls: type, name: str, period: int)

        __new__(cls: type, period: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: WindowIdentity) -> bool



"""



class WindowIndicator(IndicatorBase[T], IIndicator[T], IComparable[IIndicator[T]], IComparable, IIndicator):
    # no doc
    def ComputeNextValue(self, *args): #cannot find CLR method
        """
        ComputeNextValue(self: WindowIndicator[T], input: T) -> Decimal

        

            Computes the next value of this indicator from 

             the given state

        

        

            input: The input given to the indicator

            Returns: A new value for this indicator

        ComputeNextValue(self: WindowIndicator[T], window: IReadOnlyWindow[T], input: T) -> Decimal

        

            Computes the next value for this indicator from 

             the given state.

        

        

            window: The window of data held in this indicator

            input: The input value to this indicator on this time 

             step

        

            Returns: A new value for this indicator
        """
        pass

    def OnUpdated(self, *args): #cannot find CLR method
        """
        OnUpdated(self: IndicatorBase[T], consolidated: IndicatorDataPoint)

            Event invocator for the Updated event

        

            consolidated: This is the new piece of data produced by this 

             indicator
        """
        pass

    def Reset(self):
        """
        Reset(self: WindowIndicator[T])

            Resets this indicator to its initial state
        """
        pass

    def ValidateAndComputeNextValue(self, *args): #cannot find CLR method
        """
        ValidateAndComputeNextValue(self: IndicatorBase[T], input: T) -> IndicatorResult

        

            Computes the next value of this indicator from 

             the given state

                    and returns an 

             instance of the 

             QuantConnect.Indicators.IndicatorResult class

        

        

            input: The input given to the indicator

            Returns: An IndicatorResult object including the status of 

             the indicator
        """
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

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a flag indicating when this indicator is ready and fully initialized



Get: IsReady(self: WindowIndicator[T]) -> bool



"""

    Period = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the period of this window indicator



Get: Period(self: WindowIndicator[T]) -> int



"""



# variables with complex values

# encoding: utf-8
# module QuantConnect.Indicators calls itself Indicators
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# functions

def IIndicator(*args, **kwargs): # real signature unknown
    """
    Represents an indicator that can receive data updates and emit events when the value of

                the indicator has changed.
    """
    pass

# classes

class IIndicatorWarmUpPeriodProvider:
    """ Represents an indicator with a warm up period provider. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    WarmUpPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required period, in data points, for the indicator to be ready and fully initialized.



Get: WarmUpPeriod(self: IIndicatorWarmUpPeriodProvider) -> int



"""



class IndicatorDataPoint(BaseData, IBaseData, IEquatable[IndicatorDataPoint], IComparable[IndicatorDataPoint], IComparable):
    """
    Represents a piece of data at a specific time

    

    IndicatorDataPoint()

    IndicatorDataPoint(time: DateTime, value: Decimal)

    IndicatorDataPoint(symbol: Symbol, time: DateTime, value: Decimal)
    """
    def CompareTo(self, *__args):
        """
        CompareTo(self: IndicatorDataPoint, other: IndicatorDataPoint) -> int

        

            Compares the current object with another object 

             of the same type.

        

        

            other: An object to compare with this object.

            Returns: A value that indicates the relative order of the 

             objects being compared. The return value has the 

             following meanings: Value Meaning Less than zero 

             This object is less than the other parameter.Zero 

             This object is equal to other. Greater than zero 

             This object is greater than other.

        

        CompareTo(self: IndicatorDataPoint, obj: object) -> int

        

            Compares the current instance with another object 

             of the same type and returns an integer that 

             indicates whether the current instance precedes, 

             follows, or occurs in the same position in the 

             sort order as the other object.

        

        

            obj: An object to compare with this instance.

            Returns: A value that indicates the relative order of the 

             objects being compared. The return value has 

             these meanings: Value Meaning Less than zero This 

             instance precedes obj in the sort order. Zero 

             This instance occurs in the same position in the 

             sort order as obj. Greater than zero This 

             instance follows obj in the sort order.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: IndicatorDataPoint, other: IndicatorDataPoint) -> bool

        

            Indicates whether the current object is equal to 

             another object of the same type.

        

        

            other: An object to compare with this object.

            Returns: true if the current object is equal to the other 

             parameter; otherwise, false.

        

        Equals(self: IndicatorDataPoint, obj: object) -> bool

        

            Indicates whether this instance and a specified 

             object are equal.

        

        

            obj: Another object to compare to.

            Returns: true if obj and this instance are the same type 

             and represent the same value; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: IndicatorDataPoint) -> int

        

            Returns the hash code for this instance.

            Returns: A 32-bit signed integer that is the hash code for 

             this instance.
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: IndicatorDataPoint, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource

        

            This function is purposefully not implemented.
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: IndicatorDataPoint, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData

        

            This function is purposefully not implemented.
        """
        pass

    def ToString(self):
        """
        ToString(self: IndicatorDataPoint) -> str

        

            Returns a string representation of this DataPoint 

             instance using ISO8601 formatting for the date

        

            Returns: A System.String containing a fully qualified type 

             name.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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
        __new__(cls: type)

        __new__(cls: type, time: DateTime, value: Decimal)

        __new__(cls: type, symbol: Symbol, time: DateTime, value: Decimal)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class IndicatorUpdatedHandler(MulticastDelegate, ICloneable, ISerializable):
    """
    Event handler type for the IndicatorBase.Updated event

    

    IndicatorUpdatedHandler(object: object, method: IntPtr)
    """
    def BeginInvoke(self, sender, updated, callback, object):
        """ BeginInvoke(self: IndicatorUpdatedHandler, sender: object, updated: IndicatorDataPoint, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate

        

            Combines this System.Delegate with the specified 

             System.Delegate to form a new delegate.

        

        

            follow: The delegate to combine with this delegate.

            Returns: A delegate that is the new root of the 

             System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object

        

            Dynamically invokes (late-bound) the method 

             represented by the current delegate.

        

        

            args: An array of objects that are the arguments to 

             pass to the method represented by the current 

             delegate.-or- null, if the method represented by 

             the current delegate does not require arguments.

        

            Returns: The object returned by the method represented by 

             the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: IndicatorUpdatedHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo

        

            Returns a static method represented by the 

             current System.MulticastDelegate.

        

            Returns: A static method represented by the current 

             System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, updated):
        """ Invoke(self: IndicatorUpdatedHandler, sender: object, updated: IndicatorDataPoint) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate

        

            Removes an element from the invocation list of 

             this System.MulticastDelegate that is equal to 

             the specified delegate.

        

        

            value: The delegate to search for in the invocation list.

            Returns: If value is found in the invocation list for this 

             instance, then a new System.Delegate without 

             value in its invocation list; otherwise, this 

             instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class IReadOnlyWindow(IEnumerable[T], IEnumerable):
    # no doc
    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current number of elements in this window



Get: Count(self: IReadOnlyWindow[T]) -> int



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this window is ready, i.e,

                it has been filled to its capacity, this is when the Size==Count



Get: IsReady(self: IReadOnlyWindow[T]) -> bool



"""

    MostRecentlyRemoved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recently removed item from the window. This is the

                piece of data that just 'fell off' as a result of the most recent

                add. If no items have been removed, this will throw an exception.



Get: MostRecentlyRemoved(self: IReadOnlyWindow[T]) -> T



"""

    Samples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of samples that have been added to this window over its lifetime



Get: Samples(self: IReadOnlyWindow[T]) -> Decimal



"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of this window



Get: Size(self: IReadOnlyWindow[T]) -> int



"""



class RollingWindow(object, IReadOnlyWindow[T], IEnumerable[T], IEnumerable):
    """ RollingWindow[T](size: int) """
    def Add(self, item):
        """
        Add(self: RollingWindow[T], item: T)

            Adds an item to this window and shifts all other 

             elements

        

        

            item: The item to be added
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: RollingWindow[T]) -> IEnumerator[T]

        

            Returns an enumerator that iterates through the 

             collection.

        

            Returns: A System.Collections.Generic.IEnumerator that can 

             be used to iterate through the collection.
        """
        pass

    def Reset(self):
        """
        Reset(self: RollingWindow[T])

            Clears this window of all data
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
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

    @staticmethod # known case of __new__
    def __new__(self, size):
        """ __new__(cls: type, size: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current number of elements in this window



Get: Count(self: RollingWindow[T]) -> int



"""

    IsReady = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not this window is ready, i.e,

                it has been filled to its capacity



Get: IsReady(self: RollingWindow[T]) -> bool



"""

    MostRecentlyRemoved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recently removed item from the window. This is the

                piece of data that just 'fell off' as a result of the most recent

                add. If no items have been removed, this will throw an exception.



Get: MostRecentlyRemoved(self: RollingWindow[T]) -> T



"""

    Samples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of samples that have been added to this window over its lifetime



Get: Samples(self: RollingWindow[T]) -> Decimal



"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of this window



Get: Size(self: RollingWindow[T]) -> int



"""



