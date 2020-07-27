# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Portfolio calls itself Portfolio
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IPortfolioTarget:
    """
    Represents a portfolio target. This may be a percentage of total portfolio value

                or it may be a fixed number of shares.
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the quantity of this symbol the algorithm should hold



Get: Quantity(self: IPortfolioTarget) -> Decimal



"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the symbol of this target



Get: Symbol(self: IPortfolioTarget) -> Symbol



"""



class PortfolioTarget(object, IPortfolioTarget):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget that specifies a

                specified quantity of a security to be held by the algorithm

    

    PortfolioTarget(symbol: Symbol, quantity: Decimal)
    """
    @staticmethod
    def Percent(algorithm, symbol, percent, returnDeltaQuantity=None):
        """
        Percent(algorithm: IAlgorithm, symbol: Symbol, percent: float) -> IPortfolioTarget

        

            Creates a new target for the specified percent

        

            algorithm: The algorithm instance, used for getting total 

             portfolio value and current security price

        

            symbol: The symbol the target is for

            percent: The requested target percent of total portfolio 

             value

        

            Returns: A portfolio target for the specified 

             symbol/percent

        

        Percent(algorithm: IAlgorithm, symbol: Symbol, percent: Decimal, returnDeltaQuantity: bool) -> IPortfolioTarget

        

            Creates a new target for the specified percent

        

            algorithm: The algorithm instance, used for getting total 

             portfolio value and current security price

        

            symbol: The symbol the target is for

            percent: The requested target percent of total portfolio 

             value

        

            returnDeltaQuantity: True, result quantity will be the Delta required 

             to reach target percent.

                    False, the 

             result quantity will be the Total quantity to 

             reach the target percent, including current 

             holdings

        

            Returns: A portfolio target for the specified 

             symbol/percent
        """
        pass

    def ToString(self):
        """
        ToString(self: PortfolioTarget) -> str

        

            Returns a string that represents the current 

             object.

        

            Returns: A string that represents the current object.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol, quantity):
        """ __new__(cls: type, symbol: Symbol, quantity: Decimal) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the target quantity for the symbol



Get: Quantity(self: PortfolioTarget) -> Decimal



"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the symbol of this target



Get: Symbol(self: PortfolioTarget) -> Symbol



"""



class PortfolioTargetCollection(object, ICollection[IPortfolioTarget], IEnumerable[IPortfolioTarget], IEnumerable, IDictionary[Symbol, IPortfolioTarget], ICollection[KeyValuePair[Symbol, IPortfolioTarget]], IEnumerable[KeyValuePair[Symbol, IPortfolioTarget]]):
    """
    Provides a collection for managing QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTargets for each symbol

    

    PortfolioTargetCollection()
    """
    def Add(self, *__args):
        """
        Add(self: PortfolioTargetCollection, target: IPortfolioTarget)

            Adds the specified target to the collection. If a 

             target for the same symbol

                    already 

             exists it wil be overwritten.

        

        

            target: The portfolio target to add

        Add(self: PortfolioTargetCollection, target: KeyValuePair[Symbol, IPortfolioTarget])Add(self: PortfolioTargetCollection, symbol: Symbol, target: IPortfolioTarget)

            Adds the specified target to the collection. If a 

             target for the same symbol

                    already 

             exists it wil be overwritten.

        

        

            symbol: The symbol key

            target: The portfolio target to add
        """
        pass

    def AddRange(self, targets):
        """
        AddRange(self: PortfolioTargetCollection, targets: IEnumerable[IPortfolioTarget])AddRange(self: PortfolioTargetCollection, targets: Array[IPortfolioTarget])

            Adds the specified targets to the collection. If 

             a target for the same symbol

                    already 

             exists it will be overwritten.

        

        

            targets: The portfolio targets to add
        """
        pass

    def Clear(self):
        """
        Clear(self: PortfolioTargetCollection)

            Removes all portfolio targets from this collection
        """
        pass

    def ClearFulfilled(self, algorithm):
        """
        ClearFulfilled(self: PortfolioTargetCollection, algorithm: IAlgorithm)

            Removes fulfilled portfolio targets from this 

             collection.

                    Will only take into 

             account actual holdings and ignore open orders.
        """
        pass

    def Contains(self, target):
        """
        Contains(self: PortfolioTargetCollection, target: IPortfolioTarget) -> bool

        

            Determines whether or not the specified target 

             exists in this collection.

                    NOTE: 

             This checks for the exact specified target, not 

             by symbol. Use ContainsKey

                    to check 

             by symbol.

        

        

            target: The portfolio target to check for existence.

            Returns: True if the target exists, false otherwise

        Contains(self: PortfolioTargetCollection, target: KeyValuePair[Symbol, IPortfolioTarget]) -> bool
        """
        pass

    def ContainsKey(self, symbol):
        """
        ContainsKey(self: PortfolioTargetCollection, symbol: Symbol) -> bool

        

            Determines whether the specified symbol exists as 

             a key in this collection

        

        

            symbol: The symbol key

            Returns: True if the symbol exists in this collection, 

             false otherwise
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """
        CopyTo(self: PortfolioTargetCollection, array: Array[IPortfolioTarget], arrayIndex: int)

            Copies the targets in this collection to the 

             specified array

        

        

            array: The destination array to copy to

            arrayIndex: The index in the array to start copying to

        CopyTo(self: PortfolioTargetCollection, array: Array[KeyValuePair[Symbol, IPortfolioTarget]], arrayIndex: int)
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PortfolioTargetCollection) -> IEnumerator[IPortfolioTarget]

        

            Gets an enumerator to iterator over all portfolio 

             targets in this collection.

                    This is 

             the default enumerator for this collection.

        

            Returns: Portfolio targets enumerator
        """
        pass

    def OrderByMarginImpact(self, algorithm):
        """
        OrderByMarginImpact(self: PortfolioTargetCollection, algorithm: IAlgorithm) -> IEnumerable[IPortfolioTarget]

        

            Returned an ordered enumerable where position 

             reducing orders are executed first

                    

             and the remaining orders are executed in 

             decreasing order value.

                    Will NOT 

             return targets for securities that have no data 

             yet.

                    Will NOT return targets for 

             which current holdings + open orders quantity, 

             sum up to the target quantity

        

        

            algorithm: The algorithm instance
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: PortfolioTargetCollection, symbol: Symbol) -> bool

        

            Removes the target for the specified symbol if it 

             exists in this collection.

        

        

            symbol: The symbol to remove

            Returns: True if the symbol's target was removed, false if 

             it doesn't exist in the collection

        

        Remove(self: PortfolioTargetCollection, target: KeyValuePair[Symbol, IPortfolioTarget]) -> bool

        Remove(self: PortfolioTargetCollection, target: IPortfolioTarget) -> bool

        

            Removes the target if it exists in this 

             collection.

        

        

            target: The target to remove

            Returns: True if the target was removed, false if it 

             doesn't exist in the collection
        """
        pass

    def TryGetValue(self, symbol, target):
        """
        TryGetValue(self: PortfolioTargetCollection, symbol: Symbol) -> (bool, IPortfolioTarget)

        

            Attempts to retrieve the target for the specified 

             symbol

        

        

            symbol: The symbol

            Returns: True if the symbol's target was found, false if 

             it does not exist in this collection
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary[Symbol, IPortfolioTarget], key: Symbol) -> bool """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of targets in this collection



Get: Count(self: PortfolioTargetCollection) -> int



"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets `false`. This collection is not read-only.



Get: IsReadOnly(self: PortfolioTargetCollection) -> bool



"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the symbol keys for this collection



Get: Keys(self: PortfolioTargetCollection) -> ICollection[Symbol]



"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all portfolio targets in this collection

            Careful, will return targets for securities that might have no data yet.



Get: Values(self: PortfolioTargetCollection) -> ICollection[IPortfolioTarget]



"""



# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Portfolio calls itself Portfolio
# from QuantConnect.Algorithm.Framework, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AccumulativeInsightPortfolioConstructionModel(PortfolioConstructionModel, IPortfolioConstructionModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel that allocates percent of account

                to each insight, defaulting to 3%.

                For insights of direction QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Up, long targets are returned and

                for insights of direction QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Down, short targets are returned.

                By default, no rebalancing shall be done.

                Rules:

                   1. On active Up insight, increase position size by percent

                   2. On active Down insight, decrease position size by percent

                   3. On active Flat insight, move by percent towards 0

                   4. On expired insight, and no other active insight, emits a 0 target'''

    

    AccumulativeInsightPortfolioConstructionModel(rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias, percent: float)

    AccumulativeInsightPortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias, percent: float)

    AccumulativeInsightPortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias, percent: float)

    AccumulativeInsightPortfolioConstructionModel(rebalance: PyObject, portfolioBias: PortfolioBias, percent: float)

    AccumulativeInsightPortfolioConstructionModel(timeSpan: TimeSpan, portfolioBias: PortfolioBias, percent: float)

    AccumulativeInsightPortfolioConstructionModel(resolution: Resolution, portfolioBias: PortfolioBias, percent: float)
    """
    def DetermineTargetPercent(self, *args): #cannot find CLR method
        """ DetermineTargetPercent(self: AccumulativeInsightPortfolioConstructionModel, activeInsights: List[Insight]) -> Dictionary[Insight, float] """
        pass

    def GetTargetInsights(self, *args): #cannot find CLR method
        """
        GetTargetInsights(self: AccumulativeInsightPortfolioConstructionModel) -> List[Insight]

        

            Gets the target insights to calculate a portfolio 

             target percent for

        

            Returns: An enumerable of the target insights
        """
        pass

    def IsRebalanceDue(self, *args): #cannot find CLR method
        """
        IsRebalanceDue(self: PortfolioConstructionModel, insights: Array[Insight], algorithmUtc: DateTime) -> bool

        

            Determines if the portfolio should be rebalanced 

             base on the provided rebalancing func,

                  

               if any security change have been taken place or 

             if an insight has expired or a new insight 

             arrived

                    If the rebalancing function 

             has not been provided will return true.

        

        

            insights: The insights to create portfolio targets from

            algorithmUtc: The current algorithm UTC time

            Returns: True if should rebalance
        """
        pass

    def RefreshRebalance(self, *args): #cannot find CLR method
        """
        RefreshRebalance(self: PortfolioConstructionModel, algorithmUtc: DateTime)

            Refresh the next rebalance time and clears the 

             security changes flag
        """
        pass

    def SetPythonWrapper(self, *args): #cannot find CLR method
        """
        SetPythonWrapper(self: PortfolioConstructionModel, pythonWrapper: PortfolioConstructionModelPythonWrapper)

            Used to set the 

             QuantConnect.Algorithm.Framework.Portfolio.Portfol

             ioConstructionModelPythonWrapper instance if any
        """
        pass

    def SetRebalancingFunc(self, *args): #cannot find CLR method
        """
        SetRebalancingFunc(self: PortfolioConstructionModel, rebalance: PyObject)

            Python helper method to set the rebalancing 

             function.

                    This is required due to a 

             python net limitation not being able to use the 

             base type constructor, and also because

                 

                when python algorithms use C# portfolio 

             construction models, it can't convert python 

             methods into func nor resolve

                    the 

             correct constructor for the date rules, timespan 

             parameter.

                    For performance we prefer 

             python algorithms using the C# implementation

        

        

            rebalance: Rebalancing func or if a date rule, timedelta 

             will be converted into func.

                    For a 

             given algorithm UTC DateTime the func returns the 

             next expected rebalance time

                    or null 

             if unknown, in which case the function will be 

             called again in the next loop. Returning current 

             time

                    will trigger rebalance. If null 

             will be ignored
        """
        pass

    def ShouldCreateTargetForInsight(self, *args): #cannot find CLR method
        """
        ShouldCreateTargetForInsight(self: PortfolioConstructionModel, insight: Insight) -> bool

        

            Method that will determine if the portfolio 

             construction model should create a

                    

             target for this insight

        

        

            insight: The insight to create a target for

            Returns: True if the portfolio should create a target for 

             the insight
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias, percent: float)

        __new__(cls: type, rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias, percent: float)

        __new__(cls: type, rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias, percent: float)

        __new__(cls: type, rebalance: PyObject, portfolioBias: PortfolioBias, percent: float)

        __new__(cls: type, timeSpan: TimeSpan, portfolioBias: PortfolioBias, percent: float)

        __new__(cls: type, resolution: Resolution, portfolioBias: PortfolioBias, percent: float)
        """
        pass

    Algorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The algorithm instance



"""

    InsightCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides a collection for managing insights



"""


    PythonWrapper = None


class BlackLittermanOptimizationPortfolioConstructionModel(PortfolioConstructionModel, IPortfolioConstructionModel, INotifiedSecurityChanges):
    """
    Provides an implementation of Black-Litterman portfolio optimization. The model adjusts equilibrium market

                returns by incorporating views from multiple alpha models and therefore to get the optimal risky portfolio

                reflecting those views. If insights of all alpha models have None magnitude or there are linearly dependent

                vectors in link matrix of views, the expected return would be the implied excess equilibrium return.

                The interval of weights in optimization method can be changed based on the long-short algorithm.

                The default model uses the 0.0025 as weight-on-views scalar parameter tau. The optimization method

                maximizes the Sharpe ratio with the weight range from -1 to 1.

    

    BlackLittermanOptimizationPortfolioConstructionModel(timeSpan: TimeSpan, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, riskFreeRate: float, delta: float, tau: float, optimizer: IPortfolioOptimizer)

    BlackLittermanOptimizationPortfolioConstructionModel(rebalanceResolution: Resolution, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, riskFreeRate: float, delta: float, tau: float, optimizer: IPortfolioOptimizer)

    BlackLittermanOptimizationPortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, riskFreeRate: float, delta: float, tau: float, optimizer: IPortfolioOptimizer)

    BlackLittermanOptimizationPortfolioConstructionModel(rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, riskFreeRate: float, delta: float, tau: float, optimizer: IPortfolioOptimizer)

    BlackLittermanOptimizationPortfolioConstructionModel(rebalance: PyObject, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, riskFreeRate: float, delta: float, tau: float, optimizer: IPortfolioOptimizer)

    BlackLittermanOptimizationPortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, riskFreeRate: float, delta: float, tau: float, optimizer: IPortfolioOptimizer)
    """
    def DetermineTargetPercent(self, *args): #cannot find CLR method
        """ DetermineTargetPercent(self: BlackLittermanOptimizationPortfolioConstructionModel, lastActiveInsights: List[Insight]) -> Dictionary[Insight, float] """
        pass

    def # Error generating skeleton for function GetEquilibriumReturns: 'ascii' codec can't encode character '\u3A3' in position 37: ordinal not in range(128)

    def GetTargetInsights(self, *args): #cannot find CLR method
        """
        GetTargetInsights(self: BlackLittermanOptimizationPortfolioConstructionModel) -> List[Insight]

        

            Gets the target insights to calculate a portfolio 

             target percent for

        

            Returns: An enumerable of the target insights
        """
        pass

    def IsRebalanceDue(self, *args): #cannot find CLR method
        """
        IsRebalanceDue(self: PortfolioConstructionModel, insights: Array[Insight], algorithmUtc: DateTime) -> bool

        

            Determines if the portfolio should be rebalanced 

             base on the provided rebalancing func,

                  

               if any security change have been taken place or 

             if an insight has expired or a new insight 

             arrived

                    If the rebalancing function 

             has not been provided will return true.

        

        

            insights: The insights to create portfolio targets from

            algorithmUtc: The current algorithm UTC time

            Returns: True if should rebalance
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: BlackLittermanOptimizationPortfolioConstructionModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def RefreshRebalance(self, *args): #cannot find CLR method
        """
        RefreshRebalance(self: PortfolioConstructionModel, algorithmUtc: DateTime)

            Refresh the next rebalance time and clears the 

             security changes flag
        """
        pass

    def SetPythonWrapper(self, *args): #cannot find CLR method
        """
        SetPythonWrapper(self: PortfolioConstructionModel, pythonWrapper: PortfolioConstructionModelPythonWrapper)

            Used to set the 

             QuantConnect.Algorithm.Framework.Portfolio.Portfol

             ioConstructionModelPythonWrapper instance if any
        """
        pass

    def SetRebalancingFunc(self, *args): #cannot find CLR method
        """
        SetRebalancingFunc(self: PortfolioConstructionModel, rebalance: PyObject)

            Python helper method to set the rebalancing 

             function.

                    This is required due to a 

             python net limitation not being able to use the 

             base type constructor, and also because

                 

                when python algorithms use C# portfolio 

             construction models, it can't convert python 

             methods into func nor resolve

                    the 

             correct constructor for the date rules, timespan 

             parameter.

                    For performance we prefer 

             python algorithms using the C# implementation

        

        

            rebalance: Rebalancing func or if a date rule, timedelta 

             will be converted into func.

                    For a 

             given algorithm UTC DateTime the func returns the 

             next expected rebalance time

                    or null 

             if unknown, in which case the function will be 

             called again in the next loop. Returning current 

             time

                    will trigger rebalance. If null 

             will be ignored
        """
        pass

    def ShouldCreateTargetForInsight(self, *args): #cannot find CLR method
        """
        ShouldCreateTargetForInsight(self: BlackLittermanOptimizationPortfolioConstructionModel, insight: Insight) -> bool

        

            Method that will determine if the portfolio 

             construction model should create a

                    

             target for this insight

        

        

            insight: The insight to create a target for

            Returns: True if the portfolio should create a target for 

             the insight
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, timeSpan: TimeSpan, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, riskFreeRate: float, delta: float, tau: float, optimizer: IPortfolioOptimizer)

        __new__(cls: type, rebalanceResolution: Resolution, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, riskFreeRate: float, delta: float, tau: float, optimizer: IPortfolioOptimizer)

        __new__(cls: type, rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, riskFreeRate: float, delta: float, tau: float, optimizer: IPortfolioOptimizer)

        __new__(cls: type, rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, riskFreeRate: float, delta: float, tau: float, optimizer: IPortfolioOptimizer)

        __new__(cls: type, rebalance: PyObject, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, riskFreeRate: float, delta: float, tau: float, optimizer: IPortfolioOptimizer)

        __new__(cls: type, rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, riskFreeRate: float, delta: float, tau: float, optimizer: IPortfolioOptimizer)
        """
        pass

    Algorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The algorithm instance



"""

    InsightCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides a collection for managing insights



"""


    PythonWrapper = None


class EqualWeightingPortfolioConstructionModel(PortfolioConstructionModel, IPortfolioConstructionModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel that gives equal weighting to all

                securities. The target percent holdings of each security is 1/N where N is the number of securities. For

                insights of direction QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Up, long targets are returned and for insights of direction

                QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Down, short targets are returned.

    

    EqualWeightingPortfolioConstructionModel(rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias)

    EqualWeightingPortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias)

    EqualWeightingPortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias)

    EqualWeightingPortfolioConstructionModel(rebalance: PyObject, portfolioBias: PortfolioBias)

    EqualWeightingPortfolioConstructionModel(timeSpan: TimeSpan, portfolioBias: PortfolioBias)

    EqualWeightingPortfolioConstructionModel(resolution: Resolution, portfolioBias: PortfolioBias)
    """
    def DetermineTargetPercent(self, *args): #cannot find CLR method
        """ DetermineTargetPercent(self: EqualWeightingPortfolioConstructionModel, activeInsights: List[Insight]) -> Dictionary[Insight, float] """
        pass

    def GetTargetInsights(self, *args): #cannot find CLR method
        """
        GetTargetInsights(self: PortfolioConstructionModel) -> List[Insight]

        

            Gets the target insights to calculate a portfolio 

             target percent for

        

            Returns: An enumerable of the target insights
        """
        pass

    def IsRebalanceDue(self, *args): #cannot find CLR method
        """
        IsRebalanceDue(self: PortfolioConstructionModel, insights: Array[Insight], algorithmUtc: DateTime) -> bool

        

            Determines if the portfolio should be rebalanced 

             base on the provided rebalancing func,

                  

               if any security change have been taken place or 

             if an insight has expired or a new insight 

             arrived

                    If the rebalancing function 

             has not been provided will return true.

        

        

            insights: The insights to create portfolio targets from

            algorithmUtc: The current algorithm UTC time

            Returns: True if should rebalance
        """
        pass

    def RefreshRebalance(self, *args): #cannot find CLR method
        """
        RefreshRebalance(self: PortfolioConstructionModel, algorithmUtc: DateTime)

            Refresh the next rebalance time and clears the 

             security changes flag
        """
        pass

    def RespectPortfolioBias(self, *args): #cannot find CLR method
        """
        RespectPortfolioBias(self: EqualWeightingPortfolioConstructionModel, insight: Insight) -> bool

        

            Method that will determine if a given insight 

             respects the portfolio bias

        

        

            insight: The insight to create a target for

            Returns: True if the insight respects the portfolio bias
        """
        pass

    def SetPythonWrapper(self, *args): #cannot find CLR method
        """
        SetPythonWrapper(self: PortfolioConstructionModel, pythonWrapper: PortfolioConstructionModelPythonWrapper)

            Used to set the 

             QuantConnect.Algorithm.Framework.Portfolio.Portfol

             ioConstructionModelPythonWrapper instance if any
        """
        pass

    def SetRebalancingFunc(self, *args): #cannot find CLR method
        """
        SetRebalancingFunc(self: PortfolioConstructionModel, rebalance: PyObject)

            Python helper method to set the rebalancing 

             function.

                    This is required due to a 

             python net limitation not being able to use the 

             base type constructor, and also because

                 

                when python algorithms use C# portfolio 

             construction models, it can't convert python 

             methods into func nor resolve

                    the 

             correct constructor for the date rules, timespan 

             parameter.

                    For performance we prefer 

             python algorithms using the C# implementation

        

        

            rebalance: Rebalancing func or if a date rule, timedelta 

             will be converted into func.

                    For a 

             given algorithm UTC DateTime the func returns the 

             next expected rebalance time

                    or null 

             if unknown, in which case the function will be 

             called again in the next loop. Returning current 

             time

                    will trigger rebalance. If null 

             will be ignored
        """
        pass

    def ShouldCreateTargetForInsight(self, *args): #cannot find CLR method
        """
        ShouldCreateTargetForInsight(self: PortfolioConstructionModel, insight: Insight) -> bool

        

            Method that will determine if the portfolio 

             construction model should create a

                    

             target for this insight

        

        

            insight: The insight to create a target for

            Returns: True if the portfolio should create a target for 

             the insight
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias)

        __new__(cls: type, rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias)

        __new__(cls: type, rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias)

        __new__(cls: type, rebalance: PyObject, portfolioBias: PortfolioBias)

        __new__(cls: type, timeSpan: TimeSpan, portfolioBias: PortfolioBias)

        __new__(cls: type, resolution: Resolution, portfolioBias: PortfolioBias)
        """
        pass

    Algorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The algorithm instance



"""

    InsightCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides a collection for managing insights



"""


    PythonWrapper = None


class InsightWeightingPortfolioConstructionModel(EqualWeightingPortfolioConstructionModel, IPortfolioConstructionModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel that generates percent targets based on the

                QuantConnect.Algorithm.Framework.Alphas.Insight.Weight. The target percent holdings of each Symbol is given by the QuantConnect.Algorithm.Framework.Alphas.Insight.Weight

                from the last active QuantConnect.Algorithm.Framework.Alphas.Insight for that symbol.

                For insights of direction QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Up, long targets are returned and for insights of direction

                QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Down, short targets are returned.

                If the sum of all the last active QuantConnect.Algorithm.Framework.Alphas.Insight per symbol is bigger than 1, it will factor down each target

                percent holdings proportionally so the sum is 1.

                It will ignore QuantConnect.Algorithm.Framework.Alphas.Insight that have no QuantConnect.Algorithm.Framework.Alphas.Insight.Weight value.

    

    InsightWeightingPortfolioConstructionModel(rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias)

    InsightWeightingPortfolioConstructionModel(rebalance: PyObject, portfolioBias: PortfolioBias)

    InsightWeightingPortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias)

    InsightWeightingPortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias)

    InsightWeightingPortfolioConstructionModel(timeSpan: TimeSpan, portfolioBias: PortfolioBias)

    InsightWeightingPortfolioConstructionModel(resolution: Resolution, portfolioBias: PortfolioBias)
    """
    def DetermineTargetPercent(self, *args): #cannot find CLR method
        """ DetermineTargetPercent(self: InsightWeightingPortfolioConstructionModel, activeInsights: List[Insight]) -> Dictionary[Insight, float] """
        pass

    def GetTargetInsights(self, *args): #cannot find CLR method
        """
        GetTargetInsights(self: PortfolioConstructionModel) -> List[Insight]

        

            Gets the target insights to calculate a portfolio 

             target percent for

        

            Returns: An enumerable of the target insights
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: InsightWeightingPortfolioConstructionModel, insight: Insight) -> float

        

            Method that will determine which member will be 

             used to compute the weights and gets its value

        

        

            insight: The insight to create a target for

            Returns: The value of the selected insight member
        """
        pass

    def IsRebalanceDue(self, *args): #cannot find CLR method
        """
        IsRebalanceDue(self: PortfolioConstructionModel, insights: Array[Insight], algorithmUtc: DateTime) -> bool

        

            Determines if the portfolio should be rebalanced 

             base on the provided rebalancing func,

                  

               if any security change have been taken place or 

             if an insight has expired or a new insight 

             arrived

                    If the rebalancing function 

             has not been provided will return true.

        

        

            insights: The insights to create portfolio targets from

            algorithmUtc: The current algorithm UTC time

            Returns: True if should rebalance
        """
        pass

    def RefreshRebalance(self, *args): #cannot find CLR method
        """
        RefreshRebalance(self: PortfolioConstructionModel, algorithmUtc: DateTime)

            Refresh the next rebalance time and clears the 

             security changes flag
        """
        pass

    def RespectPortfolioBias(self, *args): #cannot find CLR method
        """
        RespectPortfolioBias(self: EqualWeightingPortfolioConstructionModel, insight: Insight) -> bool

        

            Method that will determine if a given insight 

             respects the portfolio bias

        

        

            insight: The insight to create a target for

            Returns: True if the insight respects the portfolio bias
        """
        pass

    def SetPythonWrapper(self, *args): #cannot find CLR method
        """
        SetPythonWrapper(self: PortfolioConstructionModel, pythonWrapper: PortfolioConstructionModelPythonWrapper)

            Used to set the 

             QuantConnect.Algorithm.Framework.Portfolio.Portfol

             ioConstructionModelPythonWrapper instance if any
        """
        pass

    def SetRebalancingFunc(self, *args): #cannot find CLR method
        """
        SetRebalancingFunc(self: PortfolioConstructionModel, rebalance: PyObject)

            Python helper method to set the rebalancing 

             function.

                    This is required due to a 

             python net limitation not being able to use the 

             base type constructor, and also because

                 

                when python algorithms use C# portfolio 

             construction models, it can't convert python 

             methods into func nor resolve

                    the 

             correct constructor for the date rules, timespan 

             parameter.

                    For performance we prefer 

             python algorithms using the C# implementation

        

        

            rebalance: Rebalancing func or if a date rule, timedelta 

             will be converted into func.

                    For a 

             given algorithm UTC DateTime the func returns the 

             next expected rebalance time

                    or null 

             if unknown, in which case the function will be 

             called again in the next loop. Returning current 

             time

                    will trigger rebalance. If null 

             will be ignored
        """
        pass

    def ShouldCreateTargetForInsight(self, *args): #cannot find CLR method
        """
        ShouldCreateTargetForInsight(self: InsightWeightingPortfolioConstructionModel, insight: Insight) -> bool

        

            Method that will determine if the portfolio 

             construction model should create a

                    

             target for this insight

        

        

            insight: The insight to create a target for

            Returns: True if the portfolio should create a target for 

             the insight
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias)

        __new__(cls: type, rebalance: PyObject, portfolioBias: PortfolioBias)

        __new__(cls: type, rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias)

        __new__(cls: type, rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias)

        __new__(cls: type, timeSpan: TimeSpan, portfolioBias: PortfolioBias)

        __new__(cls: type, resolution: Resolution, portfolioBias: PortfolioBias)
        """
        pass

    Algorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The algorithm instance



"""

    InsightCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides a collection for managing insights



"""


    PythonWrapper = None


class ConfidenceWeightedPortfolioConstructionModel(InsightWeightingPortfolioConstructionModel, IPortfolioConstructionModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel that generates percent targets based on the

                QuantConnect.Algorithm.Framework.Alphas.Insight.Confidence. The target percent holdings of each Symbol is given by the QuantConnect.Algorithm.Framework.Alphas.Insight.Confidence

                from the last active QuantConnect.Algorithm.Framework.Alphas.Insight for that symbol.

                For insights of direction QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Up, long targets are returned and for insights of direction

                QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Down, short targets are returned.

                If the sum of all the last active QuantConnect.Algorithm.Framework.Alphas.Insight per symbol is bigger than 1, it will factor down each target

                percent holdings proportionally so the sum is 1.

                It will ignore QuantConnect.Algorithm.Framework.Alphas.Insight that have no QuantConnect.Algorithm.Framework.Alphas.Insight.Confidence value.

    

    ConfidenceWeightedPortfolioConstructionModel(rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias)

    ConfidenceWeightedPortfolioConstructionModel(rebalance: PyObject, portfolioBias: PortfolioBias)

    ConfidenceWeightedPortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias)

    ConfidenceWeightedPortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias)

    ConfidenceWeightedPortfolioConstructionModel(timeSpan: TimeSpan, portfolioBias: PortfolioBias)

    ConfidenceWeightedPortfolioConstructionModel(resolution: Resolution, portfolioBias: PortfolioBias)
    """
    def DetermineTargetPercent(self, *args): #cannot find CLR method
        """ DetermineTargetPercent(self: InsightWeightingPortfolioConstructionModel, activeInsights: List[Insight]) -> Dictionary[Insight, float] """
        pass

    def GetTargetInsights(self, *args): #cannot find CLR method
        """
        GetTargetInsights(self: PortfolioConstructionModel) -> List[Insight]

        

            Gets the target insights to calculate a portfolio 

             target percent for

        

            Returns: An enumerable of the target insights
        """
        pass

    def GetValue(self, *args): #cannot find CLR method
        """
        GetValue(self: ConfidenceWeightedPortfolioConstructionModel, insight: Insight) -> float

        

            Method that will determine which member will be 

             used to compute the weights and gets its value

        

        

            insight: The insight to create a target for

            Returns: The value of the selected insight member
        """
        pass

    def IsRebalanceDue(self, *args): #cannot find CLR method
        """
        IsRebalanceDue(self: PortfolioConstructionModel, insights: Array[Insight], algorithmUtc: DateTime) -> bool

        

            Determines if the portfolio should be rebalanced 

             base on the provided rebalancing func,

                  

               if any security change have been taken place or 

             if an insight has expired or a new insight 

             arrived

                    If the rebalancing function 

             has not been provided will return true.

        

        

            insights: The insights to create portfolio targets from

            algorithmUtc: The current algorithm UTC time

            Returns: True if should rebalance
        """
        pass

    def RefreshRebalance(self, *args): #cannot find CLR method
        """
        RefreshRebalance(self: PortfolioConstructionModel, algorithmUtc: DateTime)

            Refresh the next rebalance time and clears the 

             security changes flag
        """
        pass

    def RespectPortfolioBias(self, *args): #cannot find CLR method
        """
        RespectPortfolioBias(self: EqualWeightingPortfolioConstructionModel, insight: Insight) -> bool

        

            Method that will determine if a given insight 

             respects the portfolio bias

        

        

            insight: The insight to create a target for

            Returns: True if the insight respects the portfolio bias
        """
        pass

    def SetPythonWrapper(self, *args): #cannot find CLR method
        """
        SetPythonWrapper(self: PortfolioConstructionModel, pythonWrapper: PortfolioConstructionModelPythonWrapper)

            Used to set the 

             QuantConnect.Algorithm.Framework.Portfolio.Portfol

             ioConstructionModelPythonWrapper instance if any
        """
        pass

    def SetRebalancingFunc(self, *args): #cannot find CLR method
        """
        SetRebalancingFunc(self: PortfolioConstructionModel, rebalance: PyObject)

            Python helper method to set the rebalancing 

             function.

                    This is required due to a 

             python net limitation not being able to use the 

             base type constructor, and also because

                 

                when python algorithms use C# portfolio 

             construction models, it can't convert python 

             methods into func nor resolve

                    the 

             correct constructor for the date rules, timespan 

             parameter.

                    For performance we prefer 

             python algorithms using the C# implementation

        

        

            rebalance: Rebalancing func or if a date rule, timedelta 

             will be converted into func.

                    For a 

             given algorithm UTC DateTime the func returns the 

             next expected rebalance time

                    or null 

             if unknown, in which case the function will be 

             called again in the next loop. Returning current 

             time

                    will trigger rebalance. If null 

             will be ignored
        """
        pass

    def ShouldCreateTargetForInsight(self, *args): #cannot find CLR method
        """
        ShouldCreateTargetForInsight(self: ConfidenceWeightedPortfolioConstructionModel, insight: Insight) -> bool

        

            Method that will determine if the portfolio 

             construction model should create a

                    

             target for this insight

        

        

            insight: The insight to create a target for

            Returns: True if the portfolio should create a target for 

             the insight
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias)

        __new__(cls: type, rebalance: PyObject, portfolioBias: PortfolioBias)

        __new__(cls: type, rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias)

        __new__(cls: type, rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias)

        __new__(cls: type, timeSpan: TimeSpan, portfolioBias: PortfolioBias)

        __new__(cls: type, resolution: Resolution, portfolioBias: PortfolioBias)
        """
        pass

    Algorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The algorithm instance



"""

    InsightCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides a collection for managing insights



"""


    PythonWrapper = None


class MaximumSharpeRatioPortfolioOptimizer(object, IPortfolioOptimizer):
    """
    Provides an implementation of a portfolio optimizer that maximizes the portfolio Sharpe Ratio.

                The interval of weights in optimization method can be changed based on the long-short algorithm.

                The default model uses flat risk free rate and weight for an individual security range from -1 to 1.

    

    MaximumSharpeRatioPortfolioOptimizer(lower: float, upper: float, riskFreeRate: float)
    """
    def GetBoundaryConditions(self, *args): #cannot find CLR method
        """
        GetBoundaryConditions(self: MaximumSharpeRatioPortfolioOptimizer, size: int) -> IEnumerable[LinearConstraint]

        

                

            size: number of variables

            Returns: enumeration of linear constaraint objects
        """
        pass

    def GetBudgetConstraint(self, *args): #cannot find CLR method
        """
        GetBudgetConstraint(self: MaximumSharpeRatioPortfolioOptimizer, size: int) -> LinearConstraint

        

                

            size: number of variables

            Returns: linear constaraint object
        """
        pass

    def Optimize(self, historicalReturns, expectedReturns, covariance):
        """ Optimize(self: MaximumSharpeRatioPortfolioOptimizer, historicalReturns: Array[float], expectedReturns: Array[float], covariance: Array[float]) -> Array[float] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lower, upper, riskFreeRate):
        """ __new__(cls: type, lower: float, upper: float, riskFreeRate: float) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class MeanVarianceOptimizationPortfolioConstructionModel(PortfolioConstructionModel, IPortfolioConstructionModel, INotifiedSecurityChanges):
    """
    Provides an implementation of Mean-Variance portfolio optimization based on modern portfolio theory.

                The interval of weights in optimization method can be changed based on the long-short algorithm.

                The default model uses the last three months daily price to calculate the optimal weight

                with the weight range from -1 to 1 and minimize the portfolio variance with a target return of 2%

    

    MeanVarianceOptimizationPortfolioConstructionModel(rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

    MeanVarianceOptimizationPortfolioConstructionModel(rebalanceResolution: Resolution, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

    MeanVarianceOptimizationPortfolioConstructionModel(timeSpan: TimeSpan, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

    MeanVarianceOptimizationPortfolioConstructionModel(rebalance: PyObject, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

    MeanVarianceOptimizationPortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

    MeanVarianceOptimizationPortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)
    """
    def DetermineTargetPercent(self, *args): #cannot find CLR method
        """ DetermineTargetPercent(self: MeanVarianceOptimizationPortfolioConstructionModel, activeInsights: List[Insight]) -> Dictionary[Insight, float] """
        pass

    def GetTargetInsights(self, *args): #cannot find CLR method
        """
        GetTargetInsights(self: PortfolioConstructionModel) -> List[Insight]

        

            Gets the target insights to calculate a portfolio 

             target percent for

        

            Returns: An enumerable of the target insights
        """
        pass

    def IsRebalanceDue(self, *args): #cannot find CLR method
        """
        IsRebalanceDue(self: PortfolioConstructionModel, insights: Array[Insight], algorithmUtc: DateTime) -> bool

        

            Determines if the portfolio should be rebalanced 

             base on the provided rebalancing func,

                  

               if any security change have been taken place or 

             if an insight has expired or a new insight 

             arrived

                    If the rebalancing function 

             has not been provided will return true.

        

        

            insights: The insights to create portfolio targets from

            algorithmUtc: The current algorithm UTC time

            Returns: True if should rebalance
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: MeanVarianceOptimizationPortfolioConstructionModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def RefreshRebalance(self, *args): #cannot find CLR method
        """
        RefreshRebalance(self: PortfolioConstructionModel, algorithmUtc: DateTime)

            Refresh the next rebalance time and clears the 

             security changes flag
        """
        pass

    def SetPythonWrapper(self, *args): #cannot find CLR method
        """
        SetPythonWrapper(self: PortfolioConstructionModel, pythonWrapper: PortfolioConstructionModelPythonWrapper)

            Used to set the 

             QuantConnect.Algorithm.Framework.Portfolio.Portfol

             ioConstructionModelPythonWrapper instance if any
        """
        pass

    def SetRebalancingFunc(self, *args): #cannot find CLR method
        """
        SetRebalancingFunc(self: PortfolioConstructionModel, rebalance: PyObject)

            Python helper method to set the rebalancing 

             function.

                    This is required due to a 

             python net limitation not being able to use the 

             base type constructor, and also because

                 

                when python algorithms use C# portfolio 

             construction models, it can't convert python 

             methods into func nor resolve

                    the 

             correct constructor for the date rules, timespan 

             parameter.

                    For performance we prefer 

             python algorithms using the C# implementation

        

        

            rebalance: Rebalancing func or if a date rule, timedelta 

             will be converted into func.

                    For a 

             given algorithm UTC DateTime the func returns the 

             next expected rebalance time

                    or null 

             if unknown, in which case the function will be 

             called again in the next loop. Returning current 

             time

                    will trigger rebalance. If null 

             will be ignored
        """
        pass

    def ShouldCreateTargetForInsight(self, *args): #cannot find CLR method
        """
        ShouldCreateTargetForInsight(self: MeanVarianceOptimizationPortfolioConstructionModel, insight: Insight) -> bool

        

            Method that will determine if the portfolio 

             construction model should create a

                    

             target for this insight

        

        

            insight: The insight to create a target for

            Returns: True if the portfolio should create a target for 

             the insight
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, rebalancingDateRules: IDateRule, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

        __new__(cls: type, rebalanceResolution: Resolution, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

        __new__(cls: type, timeSpan: TimeSpan, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

        __new__(cls: type, rebalance: PyObject, portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

        __new__(cls: type, rebalancingFunc: Func[DateTime, DateTime], portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)

        __new__(cls: type, rebalancingFunc: Func[DateTime, Nullable[DateTime]], portfolioBias: PortfolioBias, lookback: int, period: int, resolution: Resolution, targetReturn: float, optimizer: IPortfolioOptimizer)
        """
        pass

    Algorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The algorithm instance



"""

    InsightCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides a collection for managing insights



"""


    PythonWrapper = None


class MinimumVariancePortfolioOptimizer(object, IPortfolioOptimizer):
    """
    Provides an implementation of a minimum variance portfolio optimizer that calculate the optimal weights

                with the weight range from -1 to 1 and minimize the portfolio variance with a target return of 2%

    

    MinimumVariancePortfolioOptimizer(lower: float, upper: float, targetReturn: float)
    """
    def GetBoundaryConditions(self, *args): #cannot find CLR method
        """
        GetBoundaryConditions(self: MinimumVariancePortfolioOptimizer, size: int) -> IEnumerable[LinearConstraint]

        

                

            size: number of variables

            Returns: enumeration of linear constaraint objects
        """
        pass

    def GetBudgetConstraint(self, *args): #cannot find CLR method
        """
        GetBudgetConstraint(self: MinimumVariancePortfolioOptimizer, size: int) -> LinearConstraint

        

                

            size: number of variables

            Returns: linear constaraint object
        """
        pass

    def Optimize(self, historicalReturns, expectedReturns, covariance):
        """ Optimize(self: MinimumVariancePortfolioOptimizer, historicalReturns: Array[float], expectedReturns: Array[float], covariance: Array[float]) -> Array[float] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lower, upper, targetReturn):
        """ __new__(cls: type, lower: float, upper: float, targetReturn: float) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ReturnsSymbolData(object):
    """
    Contains returns specific to a symbol required for optimization model

    

    ReturnsSymbolData(symbol: Symbol, lookback: int, period: int)
    """
    def Add(self, time, value):
        """
        Add(self: ReturnsSymbolData, time: DateTime, value: Decimal)

            Adds an item to this window and shifts all other 

             elements

        

        

            time: The time associated with the value

            value: The value to use to update this window
        """
        pass

    def Reset(self):
        """
        Reset(self: ReturnsSymbolData)

            Resets all indicators of this object to its 

             initial state
        """
        pass

    def Update(self, time, value):
        """
        Update(self: ReturnsSymbolData, time: DateTime, value: Decimal) -> bool

        

            Updates the state of the RateOfChange with the 

             given value and returns true

                    if this 

             indicator is ready, false otherwise

        

        

            time: The time associated with the value

            value: The value to use to update this indicator

            Returns: True if this indicator is ready, false otherwise
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbol, lookback, period):
        """ __new__(cls: type, symbol: Symbol, lookback: int, period: int) """
        pass

    Returns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Historical returns



Get: Returns(self: ReturnsSymbolData) -> Dictionary[DateTime, float]



"""



class ReturnsSymbolDataExtensions(object):
    """ Extension methods for QuantConnect.Algorithm.Framework.Portfolio.ReturnsSymbolData """
    @staticmethod
    def FormReturnsMatrix(symbolData, symbols):
        """ FormReturnsMatrix(symbolData: Dictionary[Symbol, ReturnsSymbolData], symbols: IEnumerable[Symbol]) -> Array[float] """
        pass

    __all__ = [
        'FormReturnsMatrix',
    ]


class SectorWeightingPortfolioConstructionModel(EqualWeightingPortfolioConstructionModel, IPortfolioConstructionModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Portfolio.IPortfolioConstructionModel that generates percent targets based on the

                QuantConnect.Data.Fundamental.CompanyReference.IndustryTemplateCode. 

                The target percent holdings of each sector is 1/S where S is the number of sectors and

                the target percent holdings of each security is 1/N where N is the number of securities of each sector.

                For insights of direction QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Up, long targets are returned and for insights of direction

                QuantConnect.Algorithm.Framework.Alphas.InsightDirection.Down, short targets are returned.

                It will ignore QuantConnect.Algorithm.Framework.Alphas.Insight for symbols that have no QuantConnect.Data.Fundamental.CompanyReference.IndustryTemplateCode value.

    

    SectorWeightingPortfolioConstructionModel(rebalancingDateRules: IDateRule)

    SectorWeightingPortfolioConstructionModel(rebalancingFunc: Func[DateTime, Nullable[DateTime]])

    SectorWeightingPortfolioConstructionModel(rebalancingFunc: Func[DateTime, DateTime])

    SectorWeightingPortfolioConstructionModel(rebalance: PyObject)

    SectorWeightingPortfolioConstructionModel(timeSpan: TimeSpan)

    SectorWeightingPortfolioConstructionModel(resolution: Resolution)
    """
    def DetermineTargetPercent(self, *args): #cannot find CLR method
        """ DetermineTargetPercent(self: SectorWeightingPortfolioConstructionModel, activeInsights: List[Insight]) -> Dictionary[Insight, float] """
        pass

    def GetSectorCode(self, *args): #cannot find CLR method
        """
        GetSectorCode(self: SectorWeightingPortfolioConstructionModel, security: Security) -> str

        

            Gets the sector code

        

            security: The security to create a sector code for

            Returns: The value of the sector code for the security
        """
        pass

    def GetTargetInsights(self, *args): #cannot find CLR method
        """
        GetTargetInsights(self: PortfolioConstructionModel) -> List[Insight]

        

            Gets the target insights to calculate a portfolio 

             target percent for

        

            Returns: An enumerable of the target insights
        """
        pass

    def IsRebalanceDue(self, *args): #cannot find CLR method
        """
        IsRebalanceDue(self: PortfolioConstructionModel, insights: Array[Insight], algorithmUtc: DateTime) -> bool

        

            Determines if the portfolio should be rebalanced 

             base on the provided rebalancing func,

                  

               if any security change have been taken place or 

             if an insight has expired or a new insight 

             arrived

                    If the rebalancing function 

             has not been provided will return true.

        

        

            insights: The insights to create portfolio targets from

            algorithmUtc: The current algorithm UTC time

            Returns: True if should rebalance
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: SectorWeightingPortfolioConstructionModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def RefreshRebalance(self, *args): #cannot find CLR method
        """
        RefreshRebalance(self: PortfolioConstructionModel, algorithmUtc: DateTime)

            Refresh the next rebalance time and clears the 

             security changes flag
        """
        pass

    def RespectPortfolioBias(self, *args): #cannot find CLR method
        """
        RespectPortfolioBias(self: EqualWeightingPortfolioConstructionModel, insight: Insight) -> bool

        

            Method that will determine if a given insight 

             respects the portfolio bias

        

        

            insight: The insight to create a target for

            Returns: True if the insight respects the portfolio bias
        """
        pass

    def SetPythonWrapper(self, *args): #cannot find CLR method
        """
        SetPythonWrapper(self: PortfolioConstructionModel, pythonWrapper: PortfolioConstructionModelPythonWrapper)

            Used to set the 

             QuantConnect.Algorithm.Framework.Portfolio.Portfol

             ioConstructionModelPythonWrapper instance if any
        """
        pass

    def SetRebalancingFunc(self, *args): #cannot find CLR method
        """
        SetRebalancingFunc(self: PortfolioConstructionModel, rebalance: PyObject)

            Python helper method to set the rebalancing 

             function.

                    This is required due to a 

             python net limitation not being able to use the 

             base type constructor, and also because

                 

                when python algorithms use C# portfolio 

             construction models, it can't convert python 

             methods into func nor resolve

                    the 

             correct constructor for the date rules, timespan 

             parameter.

                    For performance we prefer 

             python algorithms using the C# implementation

        

        

            rebalance: Rebalancing func or if a date rule, timedelta 

             will be converted into func.

                    For a 

             given algorithm UTC DateTime the func returns the 

             next expected rebalance time

                    or null 

             if unknown, in which case the function will be 

             called again in the next loop. Returning current 

             time

                    will trigger rebalance. If null 

             will be ignored
        """
        pass

    def ShouldCreateTargetForInsight(self, *args): #cannot find CLR method
        """
        ShouldCreateTargetForInsight(self: SectorWeightingPortfolioConstructionModel, insight: Insight) -> bool

        

            Method that will determine if the portfolio 

             construction model should create a

                    

             target for this insight

        

        

            insight: The insight to create a target for

            Returns: True if the portfolio should create a target for 

             the insight
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, rebalancingDateRules: IDateRule)

        __new__(cls: type, rebalancingFunc: Func[DateTime, Nullable[DateTime]])

        __new__(cls: type, rebalancingFunc: Func[DateTime, DateTime])

        __new__(cls: type, rebalance: PyObject)

        __new__(cls: type, timeSpan: TimeSpan)

        __new__(cls: type, resolution: Resolution)
        """
        pass

    Algorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The algorithm instance



"""

    InsightCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Provides a collection for managing insights



"""


    PythonWrapper = None


class UnconstrainedMeanVariancePortfolioOptimizer(object, IPortfolioOptimizer):
    """
    Provides an implementation of a portfolio optimizer with unconstrained mean variance.

    

    UnconstrainedMeanVariancePortfolioOptimizer()
    """
    def Optimize(self, historicalReturns, expectedReturns, covariance):
        """ Optimize(self: UnconstrainedMeanVariancePortfolioOptimizer, historicalReturns: Array[float], expectedReturns: Array[float], covariance: Array[float]) -> Array[float] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


