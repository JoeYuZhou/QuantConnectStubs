# encoding: utf-8
# module QuantConnect.Data.Custom.SmartInsider calls itself SmartInsider
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class SmartInsiderEvent(BaseData, IBaseData):
    """
    SmartInsider Intention and Transaction events. These are fields
                that are shared between intentions and transactions.
    
    SmartInsiderEvent()
    SmartInsiderEvent(tsvLine: str)
    """
    def DataTimeZone(self):
        """
        DataTimeZone(self: SmartInsiderEvent) -> DateTimeZone
        
            Specifies the timezone of this data source
            Returns: Timezone
        """
        pass

    def FromRawData(self, line):
        """
        FromRawData(self: SmartInsiderEvent, line: str)
            Derived class instances populate their fields 
             from raw TSV
        
        
            line: Line of raw TSV (raw with fields 46, 36, 14, 7 
             removed in descending order)
        """
        pass

    @staticmethod
    def ParseDate(date):
        """
        ParseDate(date: str) -> DateTime
        
            Attempts to normalize and parse SmartInsider 
             dates that include a time component.
        
        
            date: Date string to parse
            Returns: DateTime object
        """
        pass

    def ToLine(self):
        """
        ToLine(self: SmartInsiderEvent) -> str
        
            Converts data to TSV
            Returns: String of TSV
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, tsvLine=None):
        """
        __new__(cls: type)
        __new__(cls: type, tsvLine: str)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AnnouncedIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Market in which the transaction was announced, this can reference more than one country

Get: AnnouncedIn(self: SmartInsiderEvent) -> str

Set: AnnouncedIn(self: SmartInsiderEvent) = value
"""

    AnnouncementDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Date Transaction was entered onto our system. Where a transaction is after the London market close (usually 4.30pm) this will be stated as the next day

Get: AnnouncementDate(self: SmartInsiderEvent) -> Nullable[DateTime]

Set: AnnouncementDate(self: SmartInsiderEvent) = value
"""

    CompanyID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Smart Insider proprietary identifier for the company

Get: CompanyID(self: SmartInsiderEvent) -> Nullable[int]

Set: CompanyID(self: SmartInsiderEvent) = value
"""

    CompanyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Company name. PLC is always excluded

Get: CompanyName(self: SmartInsiderEvent) -> str

Set: CompanyName(self: SmartInsiderEvent) = value
"""

    EventType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description of what has or will take place in an execution

Get: EventType(self: SmartInsiderEvent) -> Nullable[SmartInsiderEventType]

Set: EventType(self: SmartInsiderEvent) = value
"""

    ICBCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Numeric code that is the most granular level in ICB classification

Get: ICBCode(self: SmartInsiderEvent) -> Nullable[int]

Set: ICBCode(self: SmartInsiderEvent) = value
"""

    ICBIndustry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """FTSE Russell Sector Classification

Get: ICBIndustry(self: SmartInsiderEvent) -> str

Set: ICBIndustry(self: SmartInsiderEvent) = value
"""

    ICBSector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """FTSE Russell Sector Classification

Get: ICBSector(self: SmartInsiderEvent) -> str

Set: ICBSector(self: SmartInsiderEvent) = value
"""

    ICBSubSector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """FTSE Russell Sector Classification

Get: ICBSubSector(self: SmartInsiderEvent) -> str

Set: ICBSubSector(self: SmartInsiderEvent) = value
"""

    ICBSuperSector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """FTSE Russell Sector Classification

Get: ICBSuperSector(self: SmartInsiderEvent) -> str

Set: ICBSuperSector(self: SmartInsiderEvent) = value
"""

    ISIN = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Industry classification number

Get: ISIN(self: SmartInsiderEvent) -> str

Set: ISIN(self: SmartInsiderEvent) = value
"""

    LastCloseEnded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Date trading embargo (Close Period) is lifted as results are made public

Get: LastCloseEnded(self: SmartInsiderEvent) -> Nullable[DateTime]

Set: LastCloseEnded(self: SmartInsiderEvent) = value
"""

    LastIDsUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Date that company identifiers were changed. Can be a name, Ticker Symbol or ISIN change

Get: LastIDsUpdate(self: SmartInsiderEvent) -> Nullable[DateTime]

Set: LastIDsUpdate(self: SmartInsiderEvent) = value
"""

    LastUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The date when a transaction is updated after it has been reported. Not nullable

Get: LastUpdate(self: SmartInsiderEvent) -> DateTime

Set: LastUpdate(self: SmartInsiderEvent) = value
"""

    NextCloseBegin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Start date of next trading embargo ahead of scheduled results announcment

Get: NextCloseBegin(self: SmartInsiderEvent) -> Nullable[DateTime]

Set: NextCloseBegin(self: SmartInsiderEvent) = value
"""

    NextResultsAnnouncementsDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Announcement date of next results, this will be the end date of the next "Close Period"

Get: NextResultsAnnouncementsDate(self: SmartInsiderEvent) -> Nullable[DateTime]

Set: NextResultsAnnouncementsDate(self: SmartInsiderEvent) = value
"""

    PreviousResultsAnnouncementDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Announcement date of last results, this will be the end date of the last "Close Period"

Get: PreviousResultsAnnouncementDate(self: SmartInsiderEvent) -> Nullable[DateTime]

Set: PreviousResultsAnnouncementDate(self: SmartInsiderEvent) = value
"""

    SecurityDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of security. Does not contain nominal value

Get: SecurityDescription(self: SmartInsiderEvent) -> str

Set: SecurityDescription(self: SmartInsiderEvent) = value
"""

    TickerCountry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Country of local identifier, denoting where the trade took place

Get: TickerCountry(self: SmartInsiderEvent) -> str

Set: TickerCountry(self: SmartInsiderEvent) = value
"""

    TickerSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Local market identifier

Get: TickerSymbol(self: SmartInsiderEvent) -> str

Set: TickerSymbol(self: SmartInsiderEvent) = value
"""

    TimeProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Time the transaction was entered into Smart Insider systems and appeared on their website, time stated is local to London, UK

Get: TimeProcessed(self: SmartInsiderEvent) -> Nullable[DateTime]

Set: TimeProcessed(self: SmartInsiderEvent) = value
"""

    TimeProcessedUtc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Time the transaction was entered onto our systems and appeared on our website. Time stated is GMT standard

Get: TimeProcessedUtc(self: SmartInsiderEvent) -> Nullable[DateTime]

Set: TimeProcessedUtc(self: SmartInsiderEvent) = value
"""

    TimeReleased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Time the announcement first appeared on a Regulatory News Service or other disclosure system and became available to the market, time stated is local market time

Get: TimeReleased(self: SmartInsiderEvent) -> Nullable[DateTime]

Set: TimeReleased(self: SmartInsiderEvent) = value
"""

    TimeReleasedUtc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Time the announcement first appeared on a Regulatory News Service or other disclosure system and became available to the market. Time stated is GMT standard

Get: TimeReleasedUtc(self: SmartInsiderEvent) -> Nullable[DateTime]

Set: TimeReleasedUtc(self: SmartInsiderEvent) = value
"""

    TransactionID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Proprietary unique field. Not nullable

Get: TransactionID(self: SmartInsiderEvent) -> str

Set: TransactionID(self: SmartInsiderEvent) = value
"""

    USDMarketCap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The market capitalization at the time of the transaction stated in US Dollars

Get: USDMarketCap(self: SmartInsiderEvent) -> Nullable[Decimal]

Set: USDMarketCap(self: SmartInsiderEvent) = value
"""



class SmartInsiderEventType(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes what will or has taken place in an execution
    
    enum SmartInsiderEventType, values: Authorization (0), Cancellation (6), DownwardsRevision (4), Intention (1), PlanSuspension (8), RevisedDetails (5), SeekAuthorization (7), Transaction (2), UpwardsRevision (3)
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

    Authorization = None
    Cancellation = None
    DownwardsRevision = None
    Intention = None
    PlanSuspension = None
    RevisedDetails = None
    SeekAuthorization = None
    Transaction = None
    UpwardsRevision = None
    value__ = None


class SmartInsiderExecution(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes how the transaction was executed
    
    enum SmartInsiderExecution, values: Market (0), OffMarket (2), TenderOffer (1)
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

    Market = None
    OffMarket = None
    TenderOffer = None
    value__ = None


class SmartInsiderExecutionEntity(Enum, IComparable, IFormattable, IConvertible):
    """
    Entity that intends to or executed the transaction
    
    enum SmartInsiderExecutionEntity, values: Broker (2), EmployeeBenefitTrust (4), EmployerBenefitTrust (3), Issuer (0), Subsidiary (1), ThirdParty (5)
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

    Broker = None
    EmployeeBenefitTrust = None
    EmployerBenefitTrust = None
    Issuer = None
    Subsidiary = None
    ThirdParty = None
    value__ = None


class SmartInsiderExecutionHolding(Enum, IComparable, IFormattable, IConvertible):
    """
    Details regarding the way holdings will be or were processed in a buyback execution
    
    enum SmartInsiderExecutionHolding, values: Cancellation (1), Error (6), NotReported (4), SatisfyEmployeeTax (3), SatisfyStockVesting (5), Treasury (0), Trust (2)
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

    Cancellation = None
    Error = None
    NotReported = None
    SatisfyEmployeeTax = None
    SatisfyStockVesting = None
    Treasury = None
    Trust = None
    value__ = None


class SmartInsiderIntention(SmartInsiderEvent, IBaseData):
    """
    Smart Insider Intentions - Intention to execute a stock buyback and details about the future event
    
    SmartInsiderIntention()
    SmartInsiderIntention(line: str)
    """
    def Clone(self, fillForward=None):
        """
        Clone(self: SmartInsiderIntention) -> BaseData
        
            Clones the object to a new instance. This method
        
                         is required for custom data sources 
             that make use
                    of properties with 
             more complex types since otherwise
                    
             the values will default to null using the default 
             clone method
        
            Returns: A new cloned instance of this object
        """
        pass

    def FromRawData(self, line):
        """
        FromRawData(self: SmartInsiderIntention, line: str)
            Constructs a new instance from unformatted TSV 
             data
        
        
            line: Line of raw TSV (raw with fields 46, 36, 14, 7 
             removed in descending order)
        
            Returns: Instance of the object
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: SmartInsiderIntention, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
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
        Reader(self: SmartInsiderIntention, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Loads and reads the data to be used in LEAN
        
            config: Subscription configuration
            line: TSV line
            date: Algorithm date
            isLiveMode: Is live mode
            Returns: Instance of the object
        """
        pass

    def ToLine(self):
        """
        ToLine(self: SmartInsiderIntention) -> str
        
            Converts the data to TSV
            Returns: String of TSV
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, line=None):
        """
        __new__(cls: type)
        __new__(cls: type, line: str)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of shares to be or authorised to be traded

Get: Amount(self: SmartInsiderIntention) -> Nullable[int]

Set: Amount(self: SmartInsiderIntention) = value
"""

    AmountValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value of shares to be authorised to be traded

Get: AmountValue(self: SmartInsiderIntention) -> Nullable[Int64]

Set: AmountValue(self: SmartInsiderIntention) = value
"""

    AuthorizationEndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """End of the period the intention/authorisation applies to

Get: AuthorizationEndDate(self: SmartInsiderIntention) -> Nullable[DateTime]

Set: AuthorizationEndDate(self: SmartInsiderIntention) = value
"""

    AuthorizationStartDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """start of the period the intention/authorisation applies to

Get: AuthorizationStartDate(self: SmartInsiderIntention) -> Nullable[DateTime]

Set: AuthorizationStartDate(self: SmartInsiderIntention) = value
"""

    Execution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Describes how the transaction was executed

Get: Execution(self: SmartInsiderIntention) -> Nullable[SmartInsiderExecution]

Set: Execution(self: SmartInsiderIntention) = value
"""

    ExecutionEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Describes which entity intends to execute the transaction

Get: ExecutionEntity(self: SmartInsiderIntention) -> Nullable[SmartInsiderExecutionEntity]

Set: ExecutionEntity(self: SmartInsiderIntention) = value
"""

    ExecutionHolding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Describes what will be done with those shares following repurchase

Get: ExecutionHolding(self: SmartInsiderIntention) -> Nullable[SmartInsiderExecutionHolding]

Set: ExecutionHolding(self: SmartInsiderIntention) = value
"""

    MaximumPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum price shares will or may be purchased at

Get: MaximumPrice(self: SmartInsiderIntention) -> Nullable[Decimal]

Set: MaximumPrice(self: SmartInsiderIntention) = value
"""

    MinimumPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minimum price shares will or may be purchased at

Get: MinimumPrice(self: SmartInsiderIntention) -> Nullable[Decimal]

Set: MinimumPrice(self: SmartInsiderIntention) = value
"""

    NoteText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Free text which explains further details about the trade

Get: NoteText(self: SmartInsiderIntention) -> str

Set: NoteText(self: SmartInsiderIntention) = value
"""

    Percentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Percentage of oustanding shares to be authorised to be traded

Get: Percentage(self: SmartInsiderIntention) -> Nullable[Decimal]

Set: Percentage(self: SmartInsiderIntention) = value
"""

    PriceCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Currency of min/max prices (ISO Code)

Get: PriceCurrency(self: SmartInsiderIntention) -> str

Set: PriceCurrency(self: SmartInsiderIntention) = value
"""

    ValueCurrency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Currency of the value of shares to be/Authorised to be traded (ISO Code)

Get: ValueCurrency(self: SmartInsiderIntention) -> str

Set: ValueCurrency(self: SmartInsiderIntention) = value
"""



class SmartInsiderTransaction(SmartInsiderEvent, IBaseData):
    """
    Smart Insider Transaction - Execution of a stock buyback and details about the event occurred
    
    SmartInsiderTransaction()
    SmartInsiderTransaction(line: str)
    """
    def Clone(self, fillForward=None):
        """
        Clone(self: SmartInsiderTransaction) -> BaseData
        
            Clones the object to a new instance. This method
        
                         is required for custom data sources 
             that make use
                    of properties with 
             more complex types since otherwise
                    
             the values will default to null using the default 
             clone method
        
            Returns: A new cloned instance of this object
        """
        pass

    def FromRawData(self, line):
        """
        FromRawData(self: SmartInsiderTransaction, line: str)
            Creates an instance of the object by taking a 
             formatted TSV line
        
        
            line: Line of formatted TSV
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: SmartInsiderTransaction, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Specifies the location of the data and directs 
             LEAN where to load the data from
        
        
            config: Subscription configuration
            date: Date
            isLiveMode: Is live mode
            Returns: Subscription data source object pointing LEAN to 
             the data location
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: SmartInsiderTransaction, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Reads the data into LEAN for use in algorithms
        
            config: Subscription configuration
            line: Line of TSV
            date: Algorithm date
            isLiveMode: Is live mode
            Returns: Instance of the object
        """
        pass

    def ToLine(self):
        """
        ToLine(self: SmartInsiderTransaction) -> str
        
            Converts the data to TSV
            Returns: String of TSV
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, line=None):
        """
        __new__(cls: type)
        __new__(cls: type, line: str)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Amount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of shares traded

Get: Amount(self: SmartInsiderTransaction) -> Nullable[Decimal]

Set: Amount(self: SmartInsiderTransaction) = value
"""

    AmountAdjustedFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Multiplier which can be applied to 'Amount' field to account for subsequent corporate action

Get: AmountAdjustedFactor(self: SmartInsiderTransaction) -> Nullable[Decimal]

Set: AmountAdjustedFactor(self: SmartInsiderTransaction) = value
"""

    BuybackDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Date traded through the market

Get: BuybackDate(self: SmartInsiderTransaction) -> Nullable[DateTime]

Set: BuybackDate(self: SmartInsiderTransaction) = value
"""

    BuybackPercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Percentage of value of the trade as part of the issuers total Market Cap

Get: BuybackPercentage(self: SmartInsiderTransaction) -> Nullable[Decimal]

Set: BuybackPercentage(self: SmartInsiderTransaction) = value
"""

    ConversionRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Rate used to calculate 'Value (GBP)' from 'Price' multiplied by 'Amount'. Will be 1 where Currency is also 'GBP'

Get: ConversionRate(self: SmartInsiderTransaction) -> Nullable[Decimal]

Set: ConversionRate(self: SmartInsiderTransaction) = value
"""

    Currency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Currency of transation (ISO Code)

Get: Currency(self: SmartInsiderTransaction) -> str

Set: Currency(self: SmartInsiderTransaction) = value
"""

    EURValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Currency conversion rates are updated daily and values are calculated at rate prevailing on the trade date

Get: EURValue(self: SmartInsiderTransaction) -> Nullable[Decimal]

Set: EURValue(self: SmartInsiderTransaction) = value
"""

    Execution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Describes how transaction was executed

Get: Execution(self: SmartInsiderTransaction) -> Nullable[SmartInsiderExecution]

Set: Execution(self: SmartInsiderTransaction) = value
"""

    ExecutionEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Describes which entity carried out the transaction

Get: ExecutionEntity(self: SmartInsiderTransaction) -> Nullable[SmartInsiderExecutionEntity]

Set: ExecutionEntity(self: SmartInsiderTransaction) = value
"""

    ExecutionHolding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Describes what will be done with those shares following repurchase

Get: ExecutionHolding(self: SmartInsiderTransaction) -> Nullable[SmartInsiderExecutionHolding]

Set: ExecutionHolding(self: SmartInsiderTransaction) = value
"""

    ExecutionPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Denominated in Currency of Transaction

Get: ExecutionPrice(self: SmartInsiderTransaction) -> Nullable[Decimal]

Set: ExecutionPrice(self: SmartInsiderTransaction) = value
"""

    GBPValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Currency conversion rates are updated daily and values are calculated at rate prevailing on the trade date

Get: GBPValue(self: SmartInsiderTransaction) -> Nullable[Decimal]

Set: GBPValue(self: SmartInsiderTransaction) = value
"""

    NoteText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Free text which expains futher details about the trade

Get: NoteText(self: SmartInsiderTransaction) -> str

Set: NoteText(self: SmartInsiderTransaction) = value
"""

    PriceAdjustedFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Multiplier which can be applied to 'Price' and 'LastClose' fields to account for subsequent corporate actions

Get: PriceAdjustedFactor(self: SmartInsiderTransaction) -> Nullable[Decimal]

Set: PriceAdjustedFactor(self: SmartInsiderTransaction) = value
"""

    TreasuryHolding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Post trade holding of the Treasury or Trust in the security traded

Get: TreasuryHolding(self: SmartInsiderTransaction) -> Nullable[int]

Set: TreasuryHolding(self: SmartInsiderTransaction) = value
"""

    USDValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Currency conversion rates are updated daily and values are calculated at rate prevailing on the trade date

Get: USDValue(self: SmartInsiderTransaction) -> Nullable[Decimal]

Set: USDValue(self: SmartInsiderTransaction) = value
"""

    VolumePercentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Percentage of the volume traded on the day of the buyback.

Get: VolumePercentage(self: SmartInsiderTransaction) -> Nullable[Decimal]

Set: VolumePercentage(self: SmartInsiderTransaction) = value
"""



