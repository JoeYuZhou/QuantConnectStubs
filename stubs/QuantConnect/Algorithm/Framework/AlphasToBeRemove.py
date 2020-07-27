# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Alphas calls itself Alphas
# from QuantConnect.Algorithm, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AlphaModel(object, IAlphaModel, INotifiedSecurityChanges, INamedModel):
    """
    Provides a base class for alpha models.

    

    AlphaModel()
    """
    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: AlphaModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def Update(self, algorithm, data):
        """
        Update(self: AlphaModel, algorithm: QCAlgorithm, data: Slice) -> IEnumerable[Insight]

        

            Updates this alpha model with the latest data 

             from the algorithm.

                    This is called 

             each time the algorithm receives data for 

             subscribed securities

        

        

            algorithm: The algorithm instance

            data: The new data available

            Returns: The new insights generated
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines a name for a framework model



Get: Name(self: AlphaModel) -> str



Set: Name(self: AlphaModel) = value

"""



class AlphaModelExtensions(object):
    """ Provides extension methods for alpha models """
    @staticmethod
    def GetModelName(model):
        """
        GetModelName(model: IAlphaModel) -> str

        

            Gets the name of the alpha model
        """
        pass

    __all__ = [
        'GetModelName',
    ]


class AlphaModelPythonWrapper(AlphaModel, IAlphaModel, INotifiedSecurityChanges, INamedModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Alphas.IAlphaModel that wraps a Python.Runtime.PyObject object

    

    AlphaModelPythonWrapper(model: PyObject)
    """
    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: AlphaModelPythonWrapper, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def Update(self, algorithm, data):
        """
        Update(self: AlphaModelPythonWrapper, algorithm: QCAlgorithm, data: Slice) -> IEnumerable[Insight]

        

            Updates this alpha model with the latest data 

             from the algorithm.

                    This is called 

             each time the algorithm receives data for 

             subscribed securities

        

        

            algorithm: The algorithm instance

            data: The new data available

            Returns: The new insights generated
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, model):
        """ __new__(cls: type, model: PyObject) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines a name for a framework model



Get: Name(self: AlphaModelPythonWrapper) -> str



"""



class CompositeAlphaModel(AlphaModel, IAlphaModel, INotifiedSecurityChanges, INamedModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Alphas.IAlphaModel that combines multiple alpha

                models into a single alpha model and properly sets each insights 'SourceModel' property.

    

    CompositeAlphaModel(*alphaModels: Array[IAlphaModel])

    CompositeAlphaModel(*alphaModels: Array[PyObject])

    CompositeAlphaModel(alphaModel: PyObject)
    """
    def AddAlpha(self, *__args):
        """
        AddAlpha(self: CompositeAlphaModel, alphaModel: IAlphaModel)

            Adds a new 

             QuantConnect.Algorithm.Framework.Alphas.AlphaModel

        

        

            alphaModel: The alpha model to add

        AddAlpha(self: CompositeAlphaModel, pyAlphaModel: PyObject)

            Adds a new 

             QuantConnect.Algorithm.Framework.Alphas.AlphaModel

        

        

            pyAlphaModel: The alpha model to add
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: CompositeAlphaModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed.

                    This 

             method patches this call through the each of the 

             wrapped models.

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def Update(self, algorithm, data):
        """
        Update(self: CompositeAlphaModel, algorithm: QCAlgorithm, data: Slice) -> IEnumerable[Insight]

        

            Updates this alpha model with the latest data 

             from the algorithm.

                    This is called 

             each time the algorithm receives data for 

             subscribed securities.

                    This method 

             patches this call through the each of the wrapped 

             models.

        

        

            algorithm: The algorithm instance

            data: The new data available

            Returns: The new insights generated
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, *alphaModels: Array[IAlphaModel])

        __new__(cls: type, *alphaModels: Array[PyObject])

        __new__(cls: type, alphaModel: PyObject)
        """
        pass


class IAlphaModel(INotifiedSecurityChanges):
    """ Algorithm framework model that produces insights """
    def Update(self, algorithm, data):
        """
        Update(self: IAlphaModel, algorithm: QCAlgorithm, data: Slice) -> IEnumerable[Insight]

        

            Updates this alpha model with the latest data 

             from the algorithm.

                    This is called 

             each time the algorithm receives data for 

             subscribed securities

        

        

            algorithm: The algorithm instance

            data: The new data available

            Returns: The new insights generated
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class INamedModel:
    """
    Provides a marker interface allowing models to define their own names.

                If not specified, the framework will use the model's type name.

                Implementation of this is not required unless you plan on running multiple models

                of the same type w/ different parameters.
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines a name for a framework model



Get: Name(self: INamedModel) -> str



"""



class NullAlphaModel(AlphaModel, IAlphaModel, INotifiedSecurityChanges, INamedModel):
    """
    Provides a null implementation of an alpha model

    

    NullAlphaModel()
    """
    def Update(self, algorithm, data):
        """
        Update(self: NullAlphaModel, algorithm: QCAlgorithm, data: Slice) -> IEnumerable[Insight]

        

            Updates this alpha model with the latest data 

             from the algorithm.

                    This is called 

             each time the algorithm receives data for 

             subscribed securities

        

        

            algorithm: The algorithm instance

            data: The new data available

            Returns: The new insights generated
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Alphas calls itself Alphas
# from QuantConnect.Algorithm.Framework, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BasePairsTradingAlphaModel(AlphaModel, IAlphaModel, INotifiedSecurityChanges, INamedModel):
    """
    This alpha model is designed to accept every possible pair combination

                from securities selected by the universe selection model

                This model generates alternating long ratio/short ratio insights emitted as a group

    

    BasePairsTradingAlphaModel(lookback: int, resolution: Resolution, threshold: Decimal)
    """
    def HasPassedTest(self, algorithm, asset1, asset2):
        """
        HasPassedTest(self: BasePairsTradingAlphaModel, algorithm: QCAlgorithm, asset1: Symbol, asset2: Symbol) -> bool

        

            Check whether the assets pass a pairs trading test

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            asset1: The first asset's symbol in the pair

            asset2: The second asset's symbol in the pair

            Returns: True if the statistical test for the pair is 

             successful
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: BasePairsTradingAlphaModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def Update(self, algorithm, data):
        """
        Update(self: BasePairsTradingAlphaModel, algorithm: QCAlgorithm, data: Slice) -> IEnumerable[Insight]

        

            Updates this alpha model with the latest data 

             from the algorithm.

                    This is called 

             each time the algorithm receives data for 

             subscribed securities

        

        

            algorithm: The algorithm instance

            data: The new data available

            Returns: The new insights generated
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lookback, resolution, threshold):
        """ __new__(cls: type, lookback: int, resolution: Resolution, threshold: Decimal) """
        pass

    Securities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of security objects present in the universe



Get: Securities(self: BasePairsTradingAlphaModel) -> HashSet[Security]



"""



class ConstantAlphaModel(AlphaModel, IAlphaModel, INotifiedSecurityChanges, INamedModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Alphas.IAlphaModel that always returns the same insight for each security

    

    ConstantAlphaModel(type: InsightType, direction: InsightDirection, period: TimeSpan)

    ConstantAlphaModel(type: InsightType, direction: InsightDirection, period: TimeSpan, magnitude: Nullable[float], confidence: Nullable[float], weight: Nullable[float])
    """
    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: ConstantAlphaModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def ShouldEmitInsight(self, *args): #cannot find CLR method
        """ ShouldEmitInsight(self: ConstantAlphaModel, utcTime: DateTime, symbol: Symbol) -> bool """
        pass

    def Update(self, algorithm, data):
        """
        Update(self: ConstantAlphaModel, algorithm: QCAlgorithm, data: Slice) -> IEnumerable[Insight]

        

            Creates a constant insight for each security as 

             specified via the constructor

        

        

            algorithm: The algorithm instance

            data: The new data available

            Returns: The new insights generated
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type, direction, period, magnitude=None, confidence=None, weight=None):
        """
        __new__(cls: type, type: InsightType, direction: InsightDirection, period: TimeSpan)

        __new__(cls: type, type: InsightType, direction: InsightDirection, period: TimeSpan, magnitude: Nullable[float], confidence: Nullable[float], weight: Nullable[float])
        """
        pass


class EmaCrossAlphaModel(AlphaModel, IAlphaModel, INotifiedSecurityChanges, INamedModel):
    """
    Alpha model that uses an EMA cross to create insights

    

    EmaCrossAlphaModel(fastPeriod: int, slowPeriod: int, resolution: Resolution)
    """
    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: EmaCrossAlphaModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def Update(self, algorithm, data):
        """
        Update(self: EmaCrossAlphaModel, algorithm: QCAlgorithm, data: Slice) -> IEnumerable[Insight]

        

            Updates this alpha model with the latest data 

             from the algorithm.

                    This is called 

             each time the algorithm receives data for 

             subscribed securities

        

        

            algorithm: The algorithm instance

            data: The new data available

            Returns: The new insights generated
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fastPeriod, slowPeriod, resolution):
        """ __new__(cls: type, fastPeriod: int, slowPeriod: int, resolution: Resolution) """
        pass


class HistoricalReturnsAlphaModel(AlphaModel, IAlphaModel, INotifiedSecurityChanges, INamedModel):
    """
    Alpha model that uses historical returns to create insights

    

    HistoricalReturnsAlphaModel(lookback: int, resolution: Resolution)
    """
    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: HistoricalReturnsAlphaModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def Update(self, algorithm, data):
        """
        Update(self: HistoricalReturnsAlphaModel, algorithm: QCAlgorithm, data: Slice) -> IEnumerable[Insight]

        

            Updates this alpha model with the latest data 

             from the algorithm.

                    This is called 

             each time the algorithm receives data for 

             subscribed securities

        

        

            algorithm: The algorithm instance

            data: The new data available

            Returns: The new insights generated
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lookback, resolution):
        """ __new__(cls: type, lookback: int, resolution: Resolution) """
        pass


class MacdAlphaModel(AlphaModel, IAlphaModel, INotifiedSecurityChanges, INamedModel):
    """
    Defines a custom alpha model that uses MACD crossovers. The MACD signal line is

                used to generate up/down insights if it's stronger than the bounce threshold.

                If the MACD signal is within the bounce threshold then a flat price insight is returned.

    

    MacdAlphaModel(fastPeriod: int, slowPeriod: int, signalPeriod: int, movingAverageType: MovingAverageType, resolution: Resolution)
    """
    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: MacdAlphaModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed.

                    This 

             initializes the MACD for each added security and 

             cleans up the indicator for each removed 

             security.

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def Update(self, algorithm, data):
        """
        Update(self: MacdAlphaModel, algorithm: QCAlgorithm, data: Slice) -> IEnumerable[Insight]

        

            Determines an insight for each security based on 

             it's current MACD signal

        

        

            algorithm: The algorithm instance

            data: The new data available

            Returns: The new insights generated
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fastPeriod, slowPeriod, signalPeriod, movingAverageType, resolution):
        """ __new__(cls: type, fastPeriod: int, slowPeriod: int, signalPeriod: int, movingAverageType: MovingAverageType, resolution: Resolution) """
        pass


class PearsonCorrelationPairsTradingAlphaModel(BasePairsTradingAlphaModel, IAlphaModel, INotifiedSecurityChanges, INamedModel):
    """
    This alpha model is designed to rank every pair combination by its pearson correlation

                and trade the pair with the hightest correlation

                This model generates alternating long ratio/short ratio insights emitted as a group

    

    PearsonCorrelationPairsTradingAlphaModel(lookback: int, resolution: Resolution, threshold: Decimal, minimumCorrelation: float)
    """
    def HasPassedTest(self, algorithm, asset1, asset2):
        """
        HasPassedTest(self: PearsonCorrelationPairsTradingAlphaModel, algorithm: QCAlgorithm, asset1: Symbol, asset2: Symbol) -> bool

        

            Check whether the assets pass a pairs trading test

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            asset1: The first asset's symbol in the pair

            asset2: The second asset's symbol in the pair

            Returns: True if the statistical test for the pair is 

             successful
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: PearsonCorrelationPairsTradingAlphaModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lookback, resolution, threshold, minimumCorrelation):
        """ __new__(cls: type, lookback: int, resolution: Resolution, threshold: Decimal, minimumCorrelation: float) """
        pass


class RsiAlphaModel(AlphaModel, IAlphaModel, INotifiedSecurityChanges, INamedModel):
    """
    Uses Wilder's RSI to create insights. Using default settings, a cross over below 30 or above 70 will

                trigger a new insight.

    

    RsiAlphaModel(period: int, resolution: Resolution)
    """
    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: RsiAlphaModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Cleans out old security data and initializes the 

             RSI for any newly added securities.

                    

             This functional also seeds any new indicators 

             using a history request.

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def Update(self, algorithm, data):
        """
        Update(self: RsiAlphaModel, algorithm: QCAlgorithm, data: Slice) -> IEnumerable[Insight]

        

            Updates this alpha model with the latest data 

             from the algorithm.

                    This is called 

             each time the algorithm receives data for 

             subscribed securities

        

        

            algorithm: The algorithm instance

            data: The new data available

            Returns: The new insights generated
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, period, resolution):
        """ __new__(cls: type, period: int, resolution: Resolution) """
        pass



