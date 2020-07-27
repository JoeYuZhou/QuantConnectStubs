# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Alphas.Analysis.Providers calls itself Providers
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AlgorithmSecurityValuesProvider(object, ISecurityValuesProvider):
    """
    Provides an implementation of QuantConnect.Securities.ISecurityProvider that uses the QuantConnect.Securities.SecurityManager
                to get the price for the specified symbols
    
    AlgorithmSecurityValuesProvider(algorithm: IAlgorithm)
    """
    def GetAllValues(self):
        """
        GetAllValues(self: AlgorithmSecurityValuesProvider) -> ReadOnlySecurityValuesCollection
        
            Gets the current values for all the algorithm 
             securities (price/volatility)
        
            Returns: The insight target values for all the algorithm 
             securities
        """
        pass

    def GetValues(self, symbol):
        """
        GetValues(self: AlgorithmSecurityValuesProvider, symbol: Symbol) -> SecurityValues
        
            Gets the current values for the specified symbol 
             (price/volatility)
        
        
            symbol: The symbol to get price/volatility for
            Returns: The insight target values for the specified symbol
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, algorithm):
        """ __new__(cls: type, algorithm: IAlgorithm) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class DefaultInsightScoreFunctionProvider(object, IInsightScoreFunctionProvider):
    """
    Default implementation of QuantConnect.Algorithm.Framework.Alphas.Analysis.IInsightScoreFunctionProvider always returns the QuantConnect.Algorithm.Framework.Alphas.Analysis.Functions.BinaryInsightScoreFunction
    
    DefaultInsightScoreFunctionProvider()
    """
    def GetScoreFunction(self, insightType, scoreType):
        """ GetScoreFunction(self: DefaultInsightScoreFunctionProvider, insightType: InsightType, scoreType: InsightScoreType) -> IInsightScoreFunction """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


