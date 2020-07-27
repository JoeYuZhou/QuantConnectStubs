# encoding: utf-8
# module QuantConnect.Data.Custom.SEC calls itself SEC
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ISECReport(IBaseData):
    """
    Base interface for all SEC report types.
                Using an interface, we can retrieve all report types with a single
                call to QuantConnect.Data.Slice.Get
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Report = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Contents of the actual SEC report

Get: Report(self: ISECReport) -> SECReportSubmission

"""



class SECReport10K(BaseData, IBaseData, ISECReport):
    """
    SEC 10-K report (annual earnings) QuantConnect.Data.BaseData implementation.
                Using this class, you can retrieve SEC report data for a security if it exists.
                If the ticker you want no longer trades, you can also use the CIK of the company
                you want data for as well except for currently traded stocks. This may change in the future.
    
    SECReport10K()
    SECReport10K(report: SECReportSubmission)
    """
    def Clone(self, fillForward=None):
        """
        Clone(self: SECReport10K) -> BaseData
        
            Clones the current object into a new object
            Returns: BaseData clone of the current object
        """
        pass

    def DefaultResolution(self):
        """
        DefaultResolution(self: SECReport10K) -> Resolution
        
            Gets the default resolution for this data and 
             security type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: SECReport10K, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Returns a subscription data source pointing 
             towards SEC 10-K report data
        
        
            config: User configuration
            date: Date data has been requested for
            isLiveMode: Is livetrading
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: SECReport10K, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Parses the data into QuantConnect.Data.BaseData
        
            config: User subscription config
            line: Line of source file to parse
            date: Date data was requested for
            isLiveMode: Is livetrading mode
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: SECReport10K) -> bool
        
            Indicates if there is support for mapping
            Returns: True indicates mapping should be used
        """
        pass

    def SupportedResolutions(self):
        """
        SupportedResolutions(self: SECReport10K) -> List[Resolution]
        
            Gets the supported resolution for this data and 
             security type
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, report=None):
        """
        __new__(cls: type)
        __new__(cls: type, report: SECReportSubmission)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Report = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Contents of the actual SEC report

Get: Report(self: SECReport10K) -> SECReportSubmission

"""



class SECReport10Q(BaseData, IBaseData, ISECReport):
    """
    SEC 10-Q report (quarterly earnings) QuantConnect.Data.BaseData implementation.
                Using this class, you can retrieve SEC report data for a security if it exists.
                If the ticker you want no longer trades, you can also use the CIK of the company
                you want data for as well except for currently traded stocks. This may change in the future.
    
    SECReport10Q()
    SECReport10Q(report: SECReportSubmission)
    """
    def Clone(self, fillForward=None):
        """
        Clone(self: SECReport10Q) -> BaseData
        
            Clones the current object into a new object
            Returns: BaseData clone of the current object
        """
        pass

    def DefaultResolution(self):
        """
        DefaultResolution(self: SECReport10Q) -> Resolution
        
            Gets the default resolution for this data and 
             security type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: SECReport10Q, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Returns a subscription data source pointing 
             towards SEC 10-Q report data
        
        
            config: User configuration
            date: Date data has been requested for
            isLiveMode: Is livetrading
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: SECReport10Q, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Parses the data into QuantConnect.Data.BaseData
        
            config: User subscription config
            line: Line of source file to parse
            date: Date data was requested for
            isLiveMode: Is livetrading mode
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: SECReport10Q) -> bool
        
            Indicates if there is support for mapping
            Returns: True indicates mapping should be used
        """
        pass

    def SupportedResolutions(self):
        """
        SupportedResolutions(self: SECReport10Q) -> List[Resolution]
        
            Gets the supported resolution for this data and 
             security type
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, report=None):
        """
        __new__(cls: type)
        __new__(cls: type, report: SECReportSubmission)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Report = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Contents of the actual SEC report

Get: Report(self: SECReport10Q) -> SECReportSubmission

"""



class SECReport8K(BaseData, IBaseData, ISECReport):
    """
    SEC 8-K report (important investor notices) QuantConnect.Data.BaseData implementation.
                Using this class, you can retrieve SEC report data for a security if it exists.
                If the ticker you want no longer trades, you can also use the CIK of the company
                you want data for as well except for currently traded stocks. This may change in the future.
    
    SECReport8K()
    SECReport8K(report: SECReportSubmission)
    """
    def Clone(self, fillForward=None):
        """
        Clone(self: SECReport8K) -> BaseData
        
            Clones the current object into a new object
            Returns: BaseData clone of the current object
        """
        pass

    def DefaultResolution(self):
        """
        DefaultResolution(self: SECReport8K) -> Resolution
        
            Gets the default resolution for this data and 
             security type
        """
        pass

    def GetSource(self, config, date, *__args):
        """
        GetSource(self: SECReport8K, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Returns a subscription data source pointing 
             towards SEC 8-K report data
        
        
            config: User configuration
            date: Date data has been requested for
            isLiveMode: Is livetrading
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: SECReport8K, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Parses the data into instance of 
             QuantConnect.Data.BaseData
        
        
            config: User subscription config
            line: Line of source file to parse
            date: Date data was requested for
            isLiveMode: Is live trading mode
        """
        pass

    def RequiresMapping(self):
        """
        RequiresMapping(self: SECReport8K) -> bool
        
            Indicates if there is support for mapping
            Returns: True indicates mapping should be used
        """
        pass

    def SupportedResolutions(self):
        """
        SupportedResolutions(self: SECReport8K) -> List[Resolution]
        
            Gets the supported resolution for this data and 
             security type
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, report=None):
        """
        __new__(cls: type)
        __new__(cls: type, report: SECReportSubmission)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Report = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Contents of the actual SEC report

Get: Report(self: SECReport8K) -> SECReportSubmission

"""



class SECReportBusinessAddress(object):
    """ SECReportBusinessAddress() """
    City = None
    Phone = None
    State = None
    StreetOne = None
    StreetTwo = None
    Zip = None


class SECReportCompanyData(object):
    """ SECReportCompanyData() """
    AssignedSic = None
    Cik = None
    ConformedName = None
    FiscalYearEnd = None
    IrsNumber = None
    StateOfIncorporation = None


class SECReportDateTimeConverter(IsoDateTimeConverter):
    """
    Specifies format for parsing System.DateTime values from SEC data
    
    SECReportDateTimeConverter()
    """

class SECReportDocument(object):
    """ SECReportDocument() """
    Description = None
    Filename = None
    FormType = None
    Sequence = None
    Text = None


class SECReportFactory(object):
    """ SECReportFactory() """
    def CreateSECReport(self, xmlText):
        """
        CreateSECReport(self: SECReportFactory, xmlText: str) -> ISECReport
        
            Factory method creates SEC report by 
             deserializing XML formatted SEC data to 
             QuantConnect.Data.Custom.SEC.SECReportSubmission
        
        
            xmlText: XML text containing SEC data
        """
        pass


class SECReportFiler(object):
    """ SECReportFiler() """
    BusinessAddress = None
    CompanyData = None
    FormerCompanies = None
    MailingAddress = None
    Values = None


class SECReportFilingValues(object):
    """ SECReportFilingValues() """
    Act = None
    FileNumber = None
    FilmNumber = None
    FormType = None


class SECReportFormerCompany(object):
    """ SECReportFormerCompany() """
    Changed = None
    FormerConformedName = None


class SECReportIndexDirectory(object):
    """ SECReportIndexDirectory() """
    Items = None
    Name = None
    ParentDirectory = None


class SECReportIndexFile(object):
    """ SECReportIndexFile() """
    Directory = None


class SECReportIndexItem(object):
    """ SECReportIndexItem() """
    FileType = None
    LastModified = None
    Name = None
    Size = None


class SECReportMailAddress(object):
    """ SECReportMailAddress() """
    City = None
    State = None
    StreetOne = None
    StreetTwo = None
    Zip = None


class SECReportSubmission(object):
    """ SECReportSubmission() """
    AccessionNumber = None
    Documents = None
    Filers = None
    FilingDate = None
    FilingDateChange = None
    FormType = None
    Items = None
    MadeAvailableAt = None
    Period = None
    PublicDocumentCount = None


