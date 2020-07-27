# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Risk calls itself Risk
# from QuantConnect.Algorithm, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RiskManagementModel(object, IRiskManagementModel, INotifiedSecurityChanges):
    """
    Provides a base class for risk management models

    

    RiskManagementModel()
    """
    def ManageRisk(self, algorithm, targets):
        """
        ManageRisk(self: RiskManagementModel, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget]) -> IEnumerable[IPortfolioTarget]

        

            Manages the algorithm's risk at each time step

        

            algorithm: The algorithm instance

            targets: The current portfolio targets to be assessed for 

             risk
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: RiskManagementModel, algorithm: QCAlgorithm, changes: SecurityChanges)

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


class CompositeRiskManagementModel(RiskManagementModel, IRiskManagementModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that combines multiple risk

                models into a single risk management model and properly sets each insights 'SourceModel' property.

    

    CompositeRiskManagementModel(*riskManagementModels: Array[IRiskManagementModel])

    CompositeRiskManagementModel(riskManagementModels: IEnumerable[IRiskManagementModel])

    CompositeRiskManagementModel(*riskManagementModels: Array[PyObject])

    CompositeRiskManagementModel(riskManagementModel: PyObject)
    """
    def AddRiskManagement(self, *__args):
        """
        AddRiskManagement(self: CompositeRiskManagementModel, riskManagementModel: IRiskManagementModel)

            Adds a new 

             QuantConnect.Algorithm.Framework.Risk.IRiskManagem

             entModel instance

        

        

            riskManagementModel: The risk management model to add

        AddRiskManagement(self: CompositeRiskManagementModel, pyRiskManagementModel: PyObject)

            Adds a new 

             QuantConnect.Algorithm.Framework.Risk.IRiskManagem

             entModel instance

        

        

            pyRiskManagementModel: The risk management model to add
        """
        pass

    def ManageRisk(self, algorithm, targets):
        """
        ManageRisk(self: CompositeRiskManagementModel, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget]) -> IEnumerable[IPortfolioTarget]

        

            Manages the algorithm's risk at each time step.

         

                        This method patches this call through 

             the each of the wrapped models.

        

        

            algorithm: The algorithm instance

            targets: The current portfolio targets to be assessed for 

             risk

        

            Returns: The new portfolio targets
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: CompositeRiskManagementModel, algorithm: QCAlgorithm, changes: SecurityChanges)

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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, *riskManagementModels: Array[IRiskManagementModel])

        __new__(cls: type, riskManagementModels: IEnumerable[IRiskManagementModel])

        __new__(cls: type, *riskManagementModels: Array[PyObject])

        __new__(cls: type, riskManagementModel: PyObject)
        """
        pass


class IRiskManagementModel(INotifiedSecurityChanges):
    """ Algorithm framework model that manages an algorithm's risk/downside """
    def ManageRisk(self, algorithm, targets):
        """
        ManageRisk(self: IRiskManagementModel, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget]) -> IEnumerable[IPortfolioTarget]

        

            Manages the algorithm's risk at each time step

        

            algorithm: The algorithm instance

            targets: The current portfolio targets to be assessed for 

             risk
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class NullRiskManagementModel(RiskManagementModel, IRiskManagementModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that does nothing

    

    NullRiskManagementModel()
    """
    def ManageRisk(self, algorithm, targets):
        """
        ManageRisk(self: NullRiskManagementModel, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget]) -> IEnumerable[IPortfolioTarget]

        

            Manages the algorithm's risk at each time step

        

            algorithm: The algorithm instance

            targets: The current portfolio targets to be assessed for 

             risk
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class RiskManagementModelPythonWrapper(RiskManagementModel, IRiskManagementModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that wraps a Python.Runtime.PyObject object

    

    RiskManagementModelPythonWrapper(model: PyObject)
    """
    def ManageRisk(self, algorithm, targets):
        """
        ManageRisk(self: RiskManagementModelPythonWrapper, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget]) -> IEnumerable[IPortfolioTarget]

        

            Manages the algorithm's risk at each time step

        

            algorithm: The algorithm instance

            targets: The current portfolio targets to be assessed for 

             risk
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: RiskManagementModelPythonWrapper, algorithm: QCAlgorithm, changes: SecurityChanges)

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


# appended from framework
# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Risk calls itself Risk
# from QuantConnect.Algorithm.Framework, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class MaximumDrawdownPercentPerSecurity(RiskManagementModel, IRiskManagementModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that limits the drawdown

                per holding to the specified percentage

    

    MaximumDrawdownPercentPerSecurity(maximumDrawdownPercent: Decimal)
    """
    def ManageRisk(self, algorithm, targets):
        """
        ManageRisk(self: MaximumDrawdownPercentPerSecurity, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget]) -> IEnumerable[IPortfolioTarget]

        

            Manages the algorithm's risk at each time step

        

            algorithm: The algorithm instance

            targets: The current portfolio targets to be assessed for 

             risk
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, maximumDrawdownPercent):
        """ __new__(cls: type, maximumDrawdownPercent: Decimal) """
        pass


class MaximumDrawdownPercentPortfolio(RiskManagementModel, IRiskManagementModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that limits the drawdown of the portfolio

                to the specified percentage. Once this is triggered the algorithm will need to be manually restarted.

    

    MaximumDrawdownPercentPortfolio(maximumDrawdownPercent: Decimal, isTrailing: bool)
    """
    def ManageRisk(self, algorithm, targets):
        """
        ManageRisk(self: MaximumDrawdownPercentPortfolio, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget]) -> IEnumerable[IPortfolioTarget]

        

            Manages the algorithm's risk at each time step

        

            algorithm: The algorithm instance

            targets: The current portfolio targets to be assessed for 

             risk
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, maximumDrawdownPercent, isTrailing):
        """ __new__(cls: type, maximumDrawdownPercent: Decimal, isTrailing: bool) """
        pass


class MaximumSectorExposureRiskManagementModel(RiskManagementModel, IRiskManagementModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that limits

                the sector exposure to the specified percentage

    

    MaximumSectorExposureRiskManagementModel(maximumSectorExposure: Decimal)
    """
    def ManageRisk(self, algorithm, targets):
        """
        ManageRisk(self: MaximumSectorExposureRiskManagementModel, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget]) -> IEnumerable[IPortfolioTarget]

        

            Manages the algorithm's risk at each time step

        

            algorithm: The algorithm instance

            targets: The current portfolio targets to be assessed for 

             risk
        """
        pass

    def OnSecuritiesChanged(self, algorithm, changes):
        """
        OnSecuritiesChanged(self: MaximumSectorExposureRiskManagementModel, algorithm: QCAlgorithm, changes: SecurityChanges)

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
    def __new__(self, maximumSectorExposure):
        """ __new__(cls: type, maximumSectorExposure: Decimal) """
        pass


class MaximumUnrealizedProfitPercentPerSecurity(RiskManagementModel, IRiskManagementModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that limits the unrealized profit

                per holding to the specified percentage

    

    MaximumUnrealizedProfitPercentPerSecurity(maximumUnrealizedProfitPercent: Decimal)
    """
    def ManageRisk(self, algorithm, targets):
        """
        ManageRisk(self: MaximumUnrealizedProfitPercentPerSecurity, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget]) -> IEnumerable[IPortfolioTarget]

        

            Manages the algorithm's risk at each time step

        

            algorithm: The algorithm instance

            targets: The current portfolio targets to be assessed for 

             risk
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, maximumUnrealizedProfitPercent):
        """ __new__(cls: type, maximumUnrealizedProfitPercent: Decimal) """
        pass


class TrailingStopRiskManagementModel(RiskManagementModel, IRiskManagementModel, INotifiedSecurityChanges):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel that limits the maximum possible loss

                measured from the highest unrealized profit

    

    TrailingStopRiskManagementModel(maximumDrawdownPercent: Decimal)
    """
    def ManageRisk(self, algorithm, targets):
        """
        ManageRisk(self: TrailingStopRiskManagementModel, algorithm: QCAlgorithm, targets: Array[IPortfolioTarget]) -> IEnumerable[IPortfolioTarget]

        

            Manages the algorithm's risk at each time step

        

            algorithm: The algorithm instance

            targets: The current portfolio targets to be assessed for 

             risk
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, maximumDrawdownPercent):
        """ __new__(cls: type, maximumDrawdownPercent: Decimal) """
        pass


