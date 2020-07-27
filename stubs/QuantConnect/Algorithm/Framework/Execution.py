# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Execution calls itself Execution
# from QuantConnect.Algorithm, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ExecutionModel(object, IExecutionModel, INotifiedSecurityChanges):
    """
    Provides a base class for execution models

    

    ExecutionModel()
    """
    def Execute(self, algorithm, targets):
        """
        Execute(self: ExecutionModel, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget])

            Submit orders for the specified portolio targets.


             
                    This model is free to delay or 

             spread out these orders as it sees fit

        

        

            algorithm: The algorithm instance

            targets: The portfolio targets just emitted by the 

             portfolio construction model.

                    These 

             are always just the new/updated targets and not a 

             complete set of targets
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: ExecutionModel, algorithm: QCAlgorithm, changes: SecurityChanges)

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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ExecutionModelPythonWrapper(ExecutionModel, IExecutionModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Execution.IExecutionModel that wraps a Python.Runtime.PyObject object

    

    ExecutionModelPythonWrapper(model: PyObject)
    """
    def Execute(self, algorithm, targets):
        """
        Execute(self: ExecutionModelPythonWrapper, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget])

            Submit orders for the specified portolio targets.


             
                    This model is free to delay or 

             spread out these orders as it sees fit

        

        

            algorithm: The algorithm instance

            targets: The portfolio targets to be ordered
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: ExecutionModelPythonWrapper, algorithm: QCAlgorithm, changes: SecurityChanges)

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
    def __new__(self, model):
        """ __new__(cls: type, model: PyObject) """
        pass


class IExecutionModel(INotifiedSecurityChanges):
    """ Algorithm framework model that executes portfolio targets """
    def Execute(self, algorithm, targets):
        """
        Execute(self: IExecutionModel, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget])

            Submit orders for the specified portfolio 

             targets.

                    This model is free to delay 

             or spread out these orders as it sees fit

        

        

            algorithm: The algorithm instance

            targets: The portfolio targets just emitted by the 

             portfolio construction model.

                    These 

             are always just the new/updated targets and not a 

             complete set of targets
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ImmediateExecutionModel(ExecutionModel, IExecutionModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Execution.IExecutionModel that immediately submits

                market orders to achieve the desired portfolio targets

    

    ImmediateExecutionModel()
    """
    def Execute(self, algorithm, targets):
        """
        Execute(self: ImmediateExecutionModel, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget])

            Immediately submits orders for the specified 

             portfolio targets.

        

        

            algorithm: The algorithm instance

            targets: The portfolio targets to be ordered
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: ImmediateExecutionModel, algorithm: QCAlgorithm, changes: SecurityChanges)

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


class NullExecutionModel(ExecutionModel, IExecutionModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Execution.IExecutionModel that does nothing

    

    NullExecutionModel()
    """
    def Execute(self, algorithm, targets):
        """ Execute(self: NullExecutionModel, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


# from Algorithm.Framework
# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Execution calls itself Execution
# from QuantConnect.Algorithm.Framework, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class StandardDeviationExecutionModel(ExecutionModel, IExecutionModel, INotifiedSecurityChanges):
    """
    Execution model that submits orders while the current market prices is at least the configured number of standard

                deviations away from the mean in the favorable direction (below/above for buy/sell respectively)

    

    StandardDeviationExecutionModel(period: int, deviations: Decimal, resolution: Resolution)
    """
    def Execute(self, algorithm, targets):
        """
        Execute(self: StandardDeviationExecutionModel, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget])

            Executes market orders if the standard deviation 

             of price is more than the configured number of 

             deviations

                    in the favorable 

             direction.

        

        

            algorithm: The algorithm instance

            targets: The portfolio targets
        """
        pass

    def IsSafeToRemove(self, *args): #cannot find CLR method
        """
        IsSafeToRemove(self: StandardDeviationExecutionModel, algorithm: QCAlgorithm, symbol: Symbol) -> bool

        

            Determines if it's safe to remove the associated 

             symbol data
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: StandardDeviationExecutionModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def PriceIsFavorable(self, *args): #cannot find CLR method
        """ PriceIsFavorable(self: StandardDeviationExecutionModel, data: SymbolData, unorderedQuantity: Decimal) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, period, deviations, resolution):
        """ __new__(cls: type, period: int, deviations: Decimal, resolution: Resolution) """
        pass

    MaximumOrderValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum order value in units of the account currency.

            This defaults to $20,000. For example, if purchasing a stock with a price

            of $100, then the maximum order size would be 200 shares.



Get: MaximumOrderValue(self: StandardDeviationExecutionModel) -> Decimal



Set: MaximumOrderValue(self: StandardDeviationExecutionModel) = value

"""


    SymbolData = None


class VolumeWeightedAveragePriceExecutionModel(ExecutionModel, IExecutionModel, INotifiedSecurityChanges):
    """
    Execution model that submits orders while the current market price is more favorable that the current volume weighted average price.

    

    VolumeWeightedAveragePriceExecutionModel()
    """
    def Execute(self, algorithm, targets):
        """
        Execute(self: VolumeWeightedAveragePriceExecutionModel, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget])

            Submit orders for the specified portolio targets.


             
                    This model is free to delay or 

             spread out these orders as it sees fit

        

        

            algorithm: The algorithm instance

            targets: The portfolio targets to be ordered
        """
        pass

    def IsSafeToRemove(self, *args): #cannot find CLR method
        """
        IsSafeToRemove(self: VolumeWeightedAveragePriceExecutionModel, algorithm: QCAlgorithm, symbol: Symbol) -> bool

        

            Determines if it's safe to remove the associated 

             symbol data
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: VolumeWeightedAveragePriceExecutionModel, algorithm: QCAlgorithm, changes: SecurityChanges)

            Event fired each time the we add/remove 

             securities from the data feed

        

        

            algorithm: The algorithm instance that experienced the 

             change in securities

        

            changes: The security additions and removals from the 

             algorithm
        """
        pass

    def PriceIsFavorable(self, *args): #cannot find CLR method
        """ PriceIsFavorable(self: VolumeWeightedAveragePriceExecutionModel, data: SymbolData, unorderedQuantity: Decimal) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    MaximumOrderQuantityPercentVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum order quantity as a percentage of the current bar's volume.

            This defaults to 0.01m = 1%. For example, if the current bar's volume is 100, then

            the maximum order size would equal 1 share.



Get: MaximumOrderQuantityPercentVolume(self: VolumeWeightedAveragePriceExecutionModel) -> Decimal



Set: MaximumOrderQuantityPercentVolume(self: VolumeWeightedAveragePriceExecutionModel) = value

"""


    SymbolData = None


