# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Selection calls itself Selection
# from QuantConnect.Algorithm, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class UniverseSelectionModel(object, IUniverseSelectionModel):
    """
    Provides a base class for universe selection models.

    

    UniverseSelectionModel()
    """
    def CreateUniverses(self, algorithm):
        """
        CreateUniverses(self: UniverseSelectionModel, algorithm: QCAlgorithm) -> IEnumerable[Universe]

        

            Creates the universes for this algorithm. Called 

             once after 

             QuantConnect.Interfaces.IAlgorithm.Initialize

        

        

            algorithm: The algorithm instance to create universes for

            Returns: The universes to be used by the algorithm
        """
        pass

    def GetNextRefreshTimeUtc(self):
        """
        GetNextRefreshTimeUtc(self: UniverseSelectionModel) -> DateTime

        

            Gets the next time the framework should invoke 

             the `CreateUniverses` method to refresh the set 

             of universes.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class CompositeUniverseSelectionModel(UniverseSelectionModel, IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that combines multiple universe

                selection models into a single model.

    

    CompositeUniverseSelectionModel(*universeSelectionModels: Array[IUniverseSelectionModel])

    CompositeUniverseSelectionModel(*universeSelectionModels: Array[PyObject])

    CompositeUniverseSelectionModel(universeSelectionModel: PyObject)
    """
    def AddUniverseSelection(self, *__args):
        """
        AddUniverseSelection(self: CompositeUniverseSelectionModel, universeSelectionModel: IUniverseSelectionModel)

            Adds a new 

             QuantConnect.Algorithm.Framework.Selection.IUniver

             seSelectionModel

        

        

            universeSelectionModel: The universe selection model to add

        AddUniverseSelection(self: CompositeUniverseSelectionModel, pyUniverseSelectionModel: PyObject)

            Adds a new 

             QuantConnect.Algorithm.Framework.Selection.IUniver

             seSelectionModel

        

        

            pyUniverseSelectionModel: The universe selection model to add
        """
        pass

    def CreateUniverses(self, algorithm):
        """
        CreateUniverses(self: CompositeUniverseSelectionModel, algorithm: QCAlgorithm) -> IEnumerable[Universe]

        

            Creates the universes for this algorithm.

        

            algorithm: The algorithm instance to create universes for

            Returns: The universes to be used by the algorithm
        """
        pass

    def GetNextRefreshTimeUtc(self):
        """
        GetNextRefreshTimeUtc(self: CompositeUniverseSelectionModel) -> DateTime

        

            Gets the next time the framework should invoke 

             the `CreateUniverses` method to refresh the set 

             of universes.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, *universeSelectionModels: Array[IUniverseSelectionModel])

        __new__(cls: type, *universeSelectionModels: Array[PyObject])

        __new__(cls: type, universeSelectionModel: PyObject)
        """
        pass


class CustomUniverse(UserDefinedUniverse, IDisposable, INotifyCollectionChanged, ITimeTriggeredUniverse):
    """
    Defines a universe as a set of dynamically set symbols.

    

    CustomUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, interval: TimeSpan, selector: Func[DateTime, IEnumerable[str]])
    """
    def GetSubscriptionRequests(self, security, currentTimeUtc, maximumEndTimeUtc, subscriptionService=None):
        """
        GetSubscriptionRequests(self: CustomUniverse, security: Security, currentTimeUtc: DateTime, maximumEndTimeUtc: DateTime, subscriptionService: ISubscriptionDataConfigService) -> IEnumerable[SubscriptionRequest]

        

            Gets the subscription requests to be added for 

             the specified security

        

        

            security: The security to get subscriptions for

            currentTimeUtc: The current time in utc. This is the frontier 

             time of the algorithm

        

            maximumEndTimeUtc: The max end time

            subscriptionService: Instance which implements 

             QuantConnect.Interfaces.ISubscriptionDataConfigSer

             vice interface

        

            Returns: All subscriptions required by this security
        """
        pass

    def OnCollectionChanged(self, *args): #cannot find CLR method
        """
        OnCollectionChanged(self: UserDefinedUniverse, e: NotifyCollectionChangedEventArgs)

            Event invocator for the 

             QuantConnect.Data.UniverseSelection.UserDefinedUni

             verse.CollectionChanged event

        

        

            e: The notify collection changed event arguments
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, configuration, universeSettings, interval, selector):
        """ __new__(cls: type, configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, interval: TimeSpan, selector: Func[DateTime, IEnumerable[str]]) """
        pass


class CustomUniverseSelectionModel(UniverseSelectionModel, IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that simply

                subscribes to the specified set of symbols

    

    CustomUniverseSelectionModel(name: str, selector: Func[DateTime, IEnumerable[str]])

    CustomUniverseSelectionModel(name: str, selector: PyObject)

    CustomUniverseSelectionModel(securityType: SecurityType, name: str, market: str, selector: Func[DateTime, IEnumerable[str]], universeSettings: UniverseSettings, interval: TimeSpan)

    CustomUniverseSelectionModel(securityType: SecurityType, name: str, market: str, selector: PyObject, universeSettings: UniverseSettings, interval: TimeSpan)
    """
    def CreateUniverses(self, algorithm):
        """
        CreateUniverses(self: CustomUniverseSelectionModel, algorithm: QCAlgorithm) -> IEnumerable[Universe]

        

            Creates the universes for this algorithm. Called 

             at algorithm start.

        

            Returns: The universes defined by this model
        """
        pass

    def Select(self, algorithm, date):
        """ Select(self: CustomUniverseSelectionModel, algorithm: QCAlgorithm, date: DateTime) -> IEnumerable[str] """
        pass

    def ToString(self):
        """
        ToString(self: CustomUniverseSelectionModel) -> str

        

            Returns a string that represents the current 

             object
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, selector: Func[DateTime, IEnumerable[str]])

        __new__(cls: type, name: str, selector: PyObject)

        __new__(cls: type, securityType: SecurityType, name: str, market: str, selector: Func[DateTime, IEnumerable[str]], universeSettings: UniverseSettings, interval: TimeSpan)

        __new__(cls: type, securityType: SecurityType, name: str, market: str, selector: PyObject, universeSettings: UniverseSettings, interval: TimeSpan)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class IUniverseSelectionModel:
    """ Algorithm framework model that defines the universes to be used by an algorithm """
    def CreateUniverses(self, algorithm):
        """
        CreateUniverses(self: IUniverseSelectionModel, algorithm: QCAlgorithm) -> IEnumerable[Universe]

        

            Creates the universes for this algorithm. Called 

             once after 

             QuantConnect.Interfaces.IAlgorithm.Initialize

        

        

            algorithm: The algorithm instance to create universes for

            Returns: The universes to be used by the algorithm
        """
        pass

    def GetNextRefreshTimeUtc(self):
        """
        GetNextRefreshTimeUtc(self: IUniverseSelectionModel) -> DateTime

        

            Gets the next time the framework should invoke 

             the `CreateUniverses` method to refresh the set 

             of universes.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ManualUniverse(UserDefinedUniverse, IDisposable, INotifyCollectionChanged, ITimeTriggeredUniverse):
    """
    Defines a universe as a set of manually set symbols. This differs from QuantConnect.Data.UniverseSelection.UserDefinedUniverse

                in that these securities were not added via AddSecurity.

    

    ManualUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, symbols: IEnumerable[Symbol])

    ManualUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, symbols: IEnumerable[Symbol])

    ManualUniverse(configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, symbols: Array[Symbol])
    """
    def GetSubscriptionRequests(self, security, currentTimeUtc, maximumEndTimeUtc, subscriptionService=None):
        """
        GetSubscriptionRequests(self: ManualUniverse, security: Security, currentTimeUtc: DateTime, maximumEndTimeUtc: DateTime, subscriptionService: ISubscriptionDataConfigService) -> IEnumerable[SubscriptionRequest]

        

            Gets the subscription requests to be added for 

             the specified security

        

        

            security: The security to get subscriptions for

            currentTimeUtc: The current time in utc. This is the frontier 

             time of the algorithm

        

            maximumEndTimeUtc: The max end time

            subscriptionService: Instance which implements 

             QuantConnect.Interfaces.ISubscriptionDataConfigSer

             vice interface

        

            Returns: All subscriptions required by this security
        """
        pass

    def OnCollectionChanged(self, *args): #cannot find CLR method
        """
        OnCollectionChanged(self: UserDefinedUniverse, e: NotifyCollectionChangedEventArgs)

            Event invocator for the 

             QuantConnect.Data.UniverseSelection.UserDefinedUni

             verse.CollectionChanged event

        

        

            e: The notify collection changed event arguments
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, configuration, universeSettings, *__args):
        """
        __new__(cls: type, configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer, symbols: IEnumerable[Symbol])

        __new__(cls: type, configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, symbols: IEnumerable[Symbol])

        __new__(cls: type, configuration: SubscriptionDataConfig, universeSettings: UniverseSettings, symbols: Array[Symbol])
        """
        pass


class ManualUniverseSelectionModel(UniverseSelectionModel, IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that simply

                subscribes to the specified set of symbols

    

    ManualUniverseSelectionModel()

    ManualUniverseSelectionModel(symbols: IEnumerable[Symbol])

    ManualUniverseSelectionModel(*symbols: Array[Symbol])

    ManualUniverseSelectionModel(symbols: IEnumerable[Symbol], universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)
    """
    def CreateUniverses(self, algorithm):
        """
        CreateUniverses(self: ManualUniverseSelectionModel, algorithm: QCAlgorithm) -> IEnumerable[Universe]

        

            Creates the universes for this algorithm.

               

                  Called at algorithm start.

        

            Returns: The universes defined by this model
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, symbols=None, universeSettings=None, securityInitializer=None):
        """
        __new__(cls: type)

        __new__(cls: type, symbols: IEnumerable[Symbol])

        __new__(cls: type, *symbols: Array[Symbol])

        __new__(cls: type, symbols: IEnumerable[Symbol], universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)
        """
        pass


class NullUniverseSelectionModel(UniverseSelectionModel, IUniverseSelectionModel):
    """
    Provides a null implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel

    

    NullUniverseSelectionModel()
    """
    def CreateUniverses(self, algorithm):
        """
        CreateUniverses(self: NullUniverseSelectionModel, algorithm: QCAlgorithm) -> IEnumerable[Universe]

        

            Creates the universes for this algorithm.

               

                  Called at algorithm start.

        

            Returns: The universes defined by this model
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UniverseSelectionModelPythonWrapper(UniverseSelectionModel, IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that wraps a Python.Runtime.PyObject object

    

    UniverseSelectionModelPythonWrapper(model: PyObject)
    """
    def CreateUniverses(self, algorithm):
        """
        CreateUniverses(self: UniverseSelectionModelPythonWrapper, algorithm: QCAlgorithm) -> IEnumerable[Universe]

        

            Creates the universes for this algorithm. Called 

             once after 

             QuantConnect.Interfaces.IAlgorithm.Initialize

        

        

            algorithm: The algorithm instance to create universes for

            Returns: The universes to be used by the algorithm
        """
        pass

    def GetNextRefreshTimeUtc(self):
        """
        GetNextRefreshTimeUtc(self: UniverseSelectionModelPythonWrapper) -> DateTime

        

            Gets the next time the framework should invoke 

             the `CreateUniverses` method to refresh the set 

             of universes.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, model):
        """ __new__(cls: type, model: PyObject) """
        pass


# appened from framework
# encoding: utf-8
# module QuantConnect.Algorithm.Framework.Selection calls itself Selection
# from QuantConnect.Algorithm.Framework, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class FundamentalUniverseSelectionModel(UniverseSelectionModel, IUniverseSelectionModel):
    """ Provides a base class for defining equity coarse/fine fundamental selection models """
    @staticmethod
    def Coarse(coarseSelector):
        """ Coarse(coarseSelector: Func[IEnumerable[CoarseFundamental], IEnumerable[Symbol]]) -> IUniverseSelectionModel """
        pass

    def CreateCoarseFundamentalUniverse(self, algorithm):
        """
        CreateCoarseFundamentalUniverse(self: FundamentalUniverseSelectionModel, algorithm: QCAlgorithm) -> Universe

        

            Creates the coarse fundamental universe object.

         

                        This is provided to allow more 

             flexibility when creating coarse universe, such 

             as using algorithm.Universe.DollarVolume.Top(5)

        

        

            algorithm: The algorithm instance

            Returns: The coarse fundamental universe
        """
        pass

    def CreateUniverses(self, algorithm):
        """
        CreateUniverses(self: FundamentalUniverseSelectionModel, algorithm: QCAlgorithm) -> IEnumerable[Universe]

        

            Creates a new fundamental universe using this 

             class's selection functions

        

        

            algorithm: The algorithm instance to create universes for

            Returns: The universe defined by this model
        """
        pass

    @staticmethod
    def Fine(coarseSelector, fineSelector):
        """ Fine(coarseSelector: Func[IEnumerable[CoarseFundamental], IEnumerable[Symbol]], fineSelector: Func[IEnumerable[FineFundamental], IEnumerable[Symbol]]) -> IUniverseSelectionModel """
        pass

    def SelectCoarse(self, algorithm, coarse):
        """ SelectCoarse(self: FundamentalUniverseSelectionModel, algorithm: QCAlgorithm, coarse: IEnumerable[CoarseFundamental]) -> IEnumerable[Symbol] """
        pass

    def SelectFine(self, algorithm, fine):
        """ SelectFine(self: FundamentalUniverseSelectionModel, algorithm: QCAlgorithm, fine: IEnumerable[FineFundamental]) -> IEnumerable[Symbol] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, filterFineData: bool)

        __new__(cls: type, filterFineData: bool, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)
        """
        pass


class CoarseFundamentalUniverseSelectionModel(FundamentalUniverseSelectionModel, IUniverseSelectionModel):
    """
    Portfolio selection model that uses coarse selectors. For US equities only.

    

    CoarseFundamentalUniverseSelectionModel(coarseSelector: Func[IEnumerable[CoarseFundamental], IEnumerable[Symbol]], universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)

    CoarseFundamentalUniverseSelectionModel(coarseSelector: PyObject, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)
    """
    def SelectCoarse(self, algorithm, coarse):
        """ SelectCoarse(self: CoarseFundamentalUniverseSelectionModel, algorithm: QCAlgorithm, coarse: IEnumerable[CoarseFundamental]) -> IEnumerable[Symbol] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, coarseSelector, universeSettings, securityInitializer):
        """
        __new__(cls: type, coarseSelector: Func[IEnumerable[CoarseFundamental], IEnumerable[Symbol]], universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)

        __new__(cls: type, coarseSelector: PyObject, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)
        """
        pass


class EmaCrossUniverseSelectionModel(FundamentalUniverseSelectionModel, IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.FundamentalUniverseSelectionModel that subscribes

                to symbols with the larger delta by percentage between the two exponential moving average

    

    EmaCrossUniverseSelectionModel(fastPeriod: int, slowPeriod: int, universeCount: int, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)
    """
    def SelectCoarse(self, algorithm, coarse):
        """ SelectCoarse(self: EmaCrossUniverseSelectionModel, algorithm: QCAlgorithm, coarse: IEnumerable[CoarseFundamental]) -> IEnumerable[Symbol] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fastPeriod, slowPeriod, universeCount, universeSettings, securityInitializer):
        """ __new__(cls: type, fastPeriod: int, slowPeriod: int, universeCount: int, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer) """
        pass


class InceptionDateUniverseSelectionModel(CustomUniverseSelectionModel, IUniverseSelectionModel):
    """
    Inception Date Universe that accepts a Dictionary of DateTime keyed by String that represent

                the Inception date for each ticker

    

    InceptionDateUniverseSelectionModel(name: str, tickersByDate: Dictionary[str, DateTime])

    InceptionDateUniverseSelectionModel(name: str, tickersByDate: PyObject)
    """
    def Select(self, algorithm, date):
        """
        Select(self: InceptionDateUniverseSelectionModel, algorithm: QCAlgorithm, date: DateTime) -> IEnumerable[str]

        

            Returns all tickers that are trading at current 

             algorithm Time
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, tickersByDate):
        """
        __new__(cls: type, name: str, tickersByDate: Dictionary[str, DateTime])

        __new__(cls: type, name: str, tickersByDate: PyObject)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class EnergyETFUniverse(InceptionDateUniverseSelectionModel, IUniverseSelectionModel):
    """ EnergyETFUniverse() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class FineFundamentalUniverseSelectionModel(FundamentalUniverseSelectionModel, IUniverseSelectionModel):
    """
    Portfolio selection model that uses coarse/fine selectors. For US equities only.

    

    FineFundamentalUniverseSelectionModel(coarseSelector: Func[IEnumerable[CoarseFundamental], IEnumerable[Symbol]], fineSelector: Func[IEnumerable[FineFundamental], IEnumerable[Symbol]], universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)

    FineFundamentalUniverseSelectionModel(coarseSelector: PyObject, fineSelector: PyObject, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)
    """
    def SelectCoarse(self, algorithm, coarse):
        """ SelectCoarse(self: FineFundamentalUniverseSelectionModel, algorithm: QCAlgorithm, coarse: IEnumerable[CoarseFundamental]) -> IEnumerable[Symbol] """
        pass

    def SelectFine(self, algorithm, fine):
        """ SelectFine(self: FineFundamentalUniverseSelectionModel, algorithm: QCAlgorithm, fine: IEnumerable[FineFundamental]) -> IEnumerable[Symbol] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, coarseSelector, fineSelector, universeSettings, securityInitializer):
        """
        __new__(cls: type, coarseSelector: Func[IEnumerable[CoarseFundamental], IEnumerable[Symbol]], fineSelector: Func[IEnumerable[FineFundamental], IEnumerable[Symbol]], universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)

        __new__(cls: type, coarseSelector: PyObject, fineSelector: PyObject, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)
        """
        pass


class FutureUniverseSelectionModel(UniverseSelectionModel, IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that subscribes to future chains

    

    FutureUniverseSelectionModel(refreshInterval: TimeSpan, futureChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]])

    FutureUniverseSelectionModel(refreshInterval: TimeSpan, futureChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)

    FutureUniverseSelectionModel(refreshInterval: TimeSpan, futureChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], universeSettings: UniverseSettings)
    """
    def CreateFutureChainSecurity(self, *args): #cannot find CLR method
        """
        CreateFutureChainSecurity(self: FutureUniverseSelectionModel, algorithm: QCAlgorithm, symbol: Symbol, settings: UniverseSettings, initializer: ISecurityInitializer) -> Future

        

            Creates the canonical 

             QuantConnect.Securities.Future.Future chain 

             security for a given symbol

        

        

            algorithm: The algorithm instance to create universes for

            symbol: Symbol of the future

            settings: Universe settings define attributes of created 

             subscriptions, such as their resolution and the 

             minimum time in universe before they can be 

             removed

        

            initializer: Performs extra initialization (such as setting 

             models) after we create a new security object

        

            Returns: QuantConnect.Securities.Future.Future for the 

             given symbol

        

        CreateFutureChainSecurity(self: FutureUniverseSelectionModel, subscriptionDataConfigService: ISubscriptionDataConfigService, symbol: Symbol, settings: UniverseSettings, securityManager: SecurityManager) -> Future

        

            Creates the canonical 

             QuantConnect.Securities.Future.Future chain 

             security for a given symbol

        

        

            subscriptionDataConfigService: The service used to create new 

             QuantConnect.Data.SubscriptionDataConfig

        

            symbol: Symbol of the future

            settings: Universe settings define attributes of created 

             subscriptions, such as their resolution and the 

             minimum time in universe before they can be 

             removed

        

            securityManager: Used to create new 

             QuantConnect.Securities.Security

        

            Returns: QuantConnect.Securities.Future.Future for the 

             given symbol
        """
        pass

    def CreateUniverses(self, algorithm):
        """
        CreateUniverses(self: FutureUniverseSelectionModel, algorithm: QCAlgorithm) -> IEnumerable[Universe]

        

            Creates the universes for this algorithm. Called 

             once after 

             QuantConnect.Interfaces.IAlgorithm.Initialize

        

        

            algorithm: The algorithm instance to create universes for

            Returns: The universes to be used by the algorithm
        """
        pass

    def Filter(self, *args): #cannot find CLR method
        """
        Filter(self: FutureUniverseSelectionModel, filter: FutureFilterUniverse) -> FutureFilterUniverse

        

            Defines the future chain universe filter
        """
        pass

    def GetNextRefreshTimeUtc(self):
        """
        GetNextRefreshTimeUtc(self: FutureUniverseSelectionModel) -> DateTime

        

            Gets the next time the framework should invoke 

             the `CreateUniverses` method to refresh the set 

             of universes.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, refreshInterval, futureChainSymbolSelector, universeSettings=None, securityInitializer=None):
        """
        __new__(cls: type, refreshInterval: TimeSpan, futureChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]])

        __new__(cls: type, refreshInterval: TimeSpan, futureChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)

        __new__(cls: type, refreshInterval: TimeSpan, futureChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], universeSettings: UniverseSettings)
        """
        pass


class LiquidETFUniverse(InceptionDateUniverseSelectionModel, IUniverseSelectionModel):
    """
    Universe Selection Model that adds the following ETFs at their inception date

    

    LiquidETFUniverse()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Grouping = None


class MetalsETFUniverse(InceptionDateUniverseSelectionModel, IUniverseSelectionModel):
    """
    Universe Selection Model that adds the following Metals ETFs at their inception date

                2004-11-18   GLD    SPDR Gold Trust

                2005-01-28   IAU    iShares Gold Trust

                2006-04-28   SLV    iShares Silver Trust

                2006-05-22   GDX    VanEck Vectors Gold Miners ETF

                2008-12-04   AGQ    ProShares Ultra Silver

                2009-11-11   GDXJ   VanEck Vectors Junior Gold Miners ETF

                2010-01-08   PPLT   Aberdeen Standard Platinum Shares ETF

                2010-12-08   NUGT   Direxion Daily Gold Miners Bull 3X Shares

                2010-12-08   DUST   Direxion Daily Gold Miners Bear 3X Shares

                2011-10-17   USLV   VelocityShares 3x Long Silver ETN

                2011-10-17   UGLD   VelocityShares 3x Long Gold ETN

                2013-10-03   JNUG   Direxion Daily Junior Gold Miners Index Bull 3x Shares

                2013-10-03   JDST   Direxion Daily Junior Gold Miners Index Bear 3X Shares

    

    MetalsETFUniverse()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class OpenInterestFutureUniverseSelectionModel(FutureUniverseSelectionModel, IUniverseSelectionModel):
    """
    Selects contracts in a futures universe, sorted by open interest.  This allows the selection to identifiy current

                    active contract.

    

    OpenInterestFutureUniverseSelectionModel(algorithm: IAlgorithm, futureChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], chainContractsLookupLimit: Nullable[int], resultsLimit: Nullable[int])
    """
    def CreateFutureChainSecurity(self, *args): #cannot find CLR method
        """
        CreateFutureChainSecurity(self: FutureUniverseSelectionModel, algorithm: QCAlgorithm, symbol: Symbol, settings: UniverseSettings, initializer: ISecurityInitializer) -> Future

        

            Creates the canonical 

             QuantConnect.Securities.Future.Future chain 

             security for a given symbol

        

        

            algorithm: The algorithm instance to create universes for

            symbol: Symbol of the future

            settings: Universe settings define attributes of created 

             subscriptions, such as their resolution and the 

             minimum time in universe before they can be 

             removed

        

            initializer: Performs extra initialization (such as setting 

             models) after we create a new security object

        

            Returns: QuantConnect.Securities.Future.Future for the 

             given symbol

        

        CreateFutureChainSecurity(self: FutureUniverseSelectionModel, subscriptionDataConfigService: ISubscriptionDataConfigService, symbol: Symbol, settings: UniverseSettings, securityManager: SecurityManager) -> Future

        

            Creates the canonical 

             QuantConnect.Securities.Future.Future chain 

             security for a given symbol

        

        

            subscriptionDataConfigService: The service used to create new 

             QuantConnect.Data.SubscriptionDataConfig

        

            symbol: Symbol of the future

            settings: Universe settings define attributes of created 

             subscriptions, such as their resolution and the 

             minimum time in universe before they can be 

             removed

        

            securityManager: Used to create new 

             QuantConnect.Securities.Security

        

            Returns: QuantConnect.Securities.Future.Future for the 

             given symbol
        """
        pass

    def Filter(self, *args): #cannot find CLR method
        """
        Filter(self: OpenInterestFutureUniverseSelectionModel, filter: FutureFilterUniverse) -> FutureFilterUniverse

        

            Defines the future chain universe filter
        """
        pass

    def FilterByOpenInterest(self, contracts):
        """ FilterByOpenInterest(self: OpenInterestFutureUniverseSelectionModel, contracts: IReadOnlyDictionary[Symbol, SecurityExchangeHours]) -> IEnumerable[Symbol] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, algorithm, futureChainSymbolSelector, chainContractsLookupLimit, resultsLimit):
        """ __new__(cls: type, algorithm: IAlgorithm, futureChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], chainContractsLookupLimit: Nullable[int], resultsLimit: Nullable[int]) """
        pass


class OptionUniverseSelectionModel(UniverseSelectionModel, IUniverseSelectionModel):
    """
    Provides an implementation of QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel that subscribes to option chains

    

    OptionUniverseSelectionModel(refreshInterval: TimeSpan, optionChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]])

    OptionUniverseSelectionModel(refreshInterval: TimeSpan, optionChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)

    OptionUniverseSelectionModel(refreshInterval: TimeSpan, optionChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], universeSettings: UniverseSettings)
    """
    def CreateOptionChainSecurity(self, *args): #cannot find CLR method
        """
        CreateOptionChainSecurity(self: OptionUniverseSelectionModel, algorithm: QCAlgorithm, symbol: Symbol, settings: UniverseSettings, initializer: ISecurityInitializer) -> Option

        

            Creates the canonical 

             QuantConnect.Securities.Option.Option chain 

             security for a given symbol

        

        

            algorithm: The algorithm instance to create universes for

            symbol: Symbol of the option

            settings: Universe settings define attributes of created 

             subscriptions, such as their resolution and the 

             minimum time in universe before they can be 

             removed

        

            initializer: Performs extra initialization (such as setting 

             models) after we create a new security object

        

            Returns: QuantConnect.Securities.Option.Option for the 

             given symbol

        

        CreateOptionChainSecurity(self: OptionUniverseSelectionModel, subscriptionDataConfigService: ISubscriptionDataConfigService, symbol: Symbol, settings: UniverseSettings, securityManager: SecurityManager) -> Option

        

            Creates the canonical 

             QuantConnect.Securities.Option.Option chain 

             security for a given symbol

        

        

            subscriptionDataConfigService: The service used to create new 

             QuantConnect.Data.SubscriptionDataConfig

        

            symbol: Symbol of the option

            settings: Universe settings define attributes of created 

             subscriptions, such as their resolution and the 

             minimum time in universe before they can be 

             removed

        

            securityManager: Used to create new 

             QuantConnect.Securities.Security

        

            Returns: QuantConnect.Securities.Option.Option for the 

             given symbol
        """
        pass

    def CreateUniverses(self, algorithm):
        """
        CreateUniverses(self: OptionUniverseSelectionModel, algorithm: QCAlgorithm) -> IEnumerable[Universe]

        

            Creates the universes for this algorithm. Called 

             once after 

             QuantConnect.Interfaces.IAlgorithm.Initialize

        

        

            algorithm: The algorithm instance to create universes for

            Returns: The universes to be used by the algorithm
        """
        pass

    def Filter(self, *args): #cannot find CLR method
        """
        Filter(self: OptionUniverseSelectionModel, filter: OptionFilterUniverse) -> OptionFilterUniverse

        

            Defines the option chain universe filter
        """
        pass

    def GetNextRefreshTimeUtc(self):
        """
        GetNextRefreshTimeUtc(self: OptionUniverseSelectionModel) -> DateTime

        

            Gets the next time the framework should invoke 

             the `CreateUniverses` method to refresh the set 

             of universes.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, refreshInterval, optionChainSymbolSelector, universeSettings=None, securityInitializer=None):
        """
        __new__(cls: type, refreshInterval: TimeSpan, optionChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]])

        __new__(cls: type, refreshInterval: TimeSpan, optionChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)

        __new__(cls: type, refreshInterval: TimeSpan, optionChainSymbolSelector: Func[DateTime, IEnumerable[Symbol]], universeSettings: UniverseSettings)
        """
        pass


class QC500UniverseSelectionModel(FundamentalUniverseSelectionModel, IUniverseSelectionModel):
    """
    Defines the QC500 universe as a universe selection model for framework algorithm

                For details: https://github.com/QuantConnect/Lean/pull/1663

    

    QC500UniverseSelectionModel()

    QC500UniverseSelectionModel(universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)
    """
    def SelectCoarse(self, algorithm, coarse):
        """ SelectCoarse(self: QC500UniverseSelectionModel, algorithm: QCAlgorithm, coarse: IEnumerable[CoarseFundamental]) -> IEnumerable[Symbol] """
        pass

    def SelectFine(self, algorithm, fine):
        """ SelectFine(self: QC500UniverseSelectionModel, algorithm: QCAlgorithm, fine: IEnumerable[FineFundamental]) -> IEnumerable[Symbol] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, universeSettings=None, securityInitializer=None):
        """
        __new__(cls: type)

        __new__(cls: type, universeSettings: UniverseSettings, securityInitializer: ISecurityInitializer)
        """
        pass


class ScheduledUniverseSelectionModel(UniverseSelectionModel, IUniverseSelectionModel):
    """
    Defines a universe selection model that invokes a selector function on a specific scheduled given by an QuantConnect.Scheduling.IDateRule and an QuantConnect.Scheduling.ITimeRule

    

    ScheduledUniverseSelectionModel(dateRule: IDateRule, timeRule: ITimeRule, selector: Func[DateTime, IEnumerable[Symbol]], settings: UniverseSettings, initializer: ISecurityInitializer)

    ScheduledUniverseSelectionModel(timeZone: DateTimeZone, dateRule: IDateRule, timeRule: ITimeRule, selector: Func[DateTime, IEnumerable[Symbol]], settings: UniverseSettings, initializer: ISecurityInitializer)

    ScheduledUniverseSelectionModel(dateRule: IDateRule, timeRule: ITimeRule, selector: PyObject, settings: UniverseSettings, initializer: ISecurityInitializer)

    ScheduledUniverseSelectionModel(timeZone: DateTimeZone, dateRule: IDateRule, timeRule: ITimeRule, selector: PyObject, settings: UniverseSettings, initializer: ISecurityInitializer)
    """
    def CreateUniverses(self, algorithm):
        """
        CreateUniverses(self: ScheduledUniverseSelectionModel, algorithm: QCAlgorithm) -> IEnumerable[Universe]

        

            Creates the universes for this algorithm. Called 

             once after 

             QuantConnect.Interfaces.IAlgorithm.Initialize

        

        

            algorithm: The algorithm instance to create universes for

            Returns: The universes to be used by the algorithm
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, dateRule: IDateRule, timeRule: ITimeRule, selector: Func[DateTime, IEnumerable[Symbol]], settings: UniverseSettings, initializer: ISecurityInitializer)

        __new__(cls: type, timeZone: DateTimeZone, dateRule: IDateRule, timeRule: ITimeRule, selector: Func[DateTime, IEnumerable[Symbol]], settings: UniverseSettings, initializer: ISecurityInitializer)

        __new__(cls: type, dateRule: IDateRule, timeRule: ITimeRule, selector: PyObject, settings: UniverseSettings, initializer: ISecurityInitializer)

        __new__(cls: type, timeZone: DateTimeZone, dateRule: IDateRule, timeRule: ITimeRule, selector: PyObject, settings: UniverseSettings, initializer: ISecurityInitializer)
        """
        pass


class SP500SectorsETFUniverse(InceptionDateUniverseSelectionModel, IUniverseSelectionModel):
    """
    Universe Selection Model that adds the following SP500 Sectors ETFs at their inception date

                1998-12-22   XLB   Materials Select Sector SPDR ETF

                1998-12-22   XLE   Energy Select Sector SPDR Fund

                1998-12-22   XLF   Financial Select Sector SPDR Fund

                1998-12-22   XLI   Industrial Select Sector SPDR Fund

                1998-12-22   XLK   Technology Select Sector SPDR Fund

                1998-12-22   XLP   Consumer Staples Select Sector SPDR Fund

                1998-12-22   XLU   Utilities Select Sector SPDR Fund

                1998-12-22   XLV   Health Care Select Sector SPDR Fund

                1998-12-22   XLY   Consumer Discretionary Select Sector SPDR Fund

    

    SP500SectorsETFUniverse()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class TechnologyETFUniverse(InceptionDateUniverseSelectionModel, IUniverseSelectionModel):
    """
    Universe Selection Model that adds the following Technology ETFs at their inception date

                1998-12-22   XLK    Technology Select Sector SPDR Fund

                1999-03-10   QQQ    Invesco QQQ

                2001-07-13   SOXX   iShares PHLX Semiconductor ETF

                2001-07-13   IGV    iShares Expanded Tech-Software Sector ETF

                2004-01-30   VGT    Vanguard Information Technology ETF

                2006-04-25   QTEC   First Trust NASDAQ 100 Technology

                2006-06-23   FDN    First Trust Dow Jones Internet Index

                2007-05-10   FXL    First Trust Technology AlphaDEX Fund

                2008-12-17   TECL   Direxion Daily Technology Bull 3X Shares

                2008-12-17   TECS   Direxion Daily Technology Bear 3X Shares

                2010-03-11   SOXL   Direxion Daily Semiconductor Bull 3x Shares

                2010-03-11   SOXS   Direxion Daily Semiconductor Bear 3x Shares

                2011-07-06   SKYY   First Trust ISE Cloud Computing Index Fund

                2011-12-21   SMH    VanEck Vectors Semiconductor ETF

                2013-08-01   KWEB   KraneShares CSI China Internet ETF

                2013-10-24   FTEC   Fidelity MSCI Information Technology Index ETF

    

    TechnologyETFUniverse()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class USTreasuriesETFUniverse(InceptionDateUniverseSelectionModel, IUniverseSelectionModel):
    """
    Universe Selection Model that adds the following US Treasuries ETFs at their inception date

                2002-07-26   IEF    iShares 7-10 Year Treasury Bond ETF

                2002-07-26   SHY    iShares 1-3 Year Treasury Bond ETF

                2002-07-26   TLT    iShares 20+ Year Treasury Bond ETF

                2007-01-11   SHV    iShares Short Treasury Bond ETF

                2007-01-11   IEI    iShares 3-7 Year Treasury Bond ETF

                2007-01-11   TLH    iShares 10-20 Year Treasury Bond ETF

                2007-12-10   EDV    Vanguard Ext Duration Treasury ETF

                2007-05-30   BIL    SPDR Barclays 1-3 Month T-Bill ETF

                2007-05-30   SPTL   SPDR Portfolio Long Term Treasury ETF

                2008-05-01   TBT    UltraShort Barclays 20+ Year Treasury

                2009-04-16   TMF    Direxion Daily 20-Year Treasury Bull 3X

                2009-04-16   TMV    Direxion Daily 20-Year Treasury Bear 3X

                2009-08-20   TBF    ProShares Short 20+ Year Treasury

                2009-11-23   VGSH   Vanguard Short-Term Treasury ETF

                2009-11-23   VGIT   Vanguard Intermediate-Term Treasury ETF

                2009-11-24   VGLT   Vanguard Long-Term Treasury ETF

                2010-08-06   SCHO   Schwab Short-Term U.S. Treasury ETF

                2010-08-06   SCHR   Schwab Intermediate-Term U.S. Treasury ETF

                2011-12-01   SPTS   SPDR Portfolio Short Term Treasury ETF

                2012-02-24   GOVT   iShares U.S. Treasury Bond ETF

    

    USTreasuriesETFUniverse()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class VolatilityETFUniverse(InceptionDateUniverseSelectionModel, IUniverseSelectionModel):
    """ VolatilityETFUniverse() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


