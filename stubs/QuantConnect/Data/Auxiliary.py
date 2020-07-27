# encoding: utf-8
# module QuantConnect.Data.Auxiliary calls itself Auxiliary
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class FactorFile(object, IEnumerable[FactorFileRow], IEnumerable):
    """
    Represents an entire factor file for a specified symbol
    
    FactorFile(permtick: str, data: IEnumerable[FactorFileRow], factorFileMinimumDate: Nullable[DateTime])
    """
    def Apply(self, data, exchangeHours):
        """ Apply(self: FactorFile, data: List[BaseData], exchangeHours: SecurityExchangeHours) -> FactorFile """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: FactorFile) -> IEnumerator[FactorFileRow]
        
            Returns an enumerator that iterates through the 
             collection.
        
            Returns: A System.Collections.Generic.IEnumerator that can 
             be used to iterate through the collection.
        """
        pass

    def GetPriceScaleFactor(self, searchDate):
        """
        GetPriceScaleFactor(self: FactorFile, searchDate: DateTime) -> Decimal
        
            Gets the price scale factor that includes 
             dividend and split adjustments for the specified 
             search date
        """
        pass

    def GetScalingFactors(self, searchDate):
        """
        GetScalingFactors(self: FactorFile, searchDate: DateTime) -> FactorFileRow
        
            Gets price and split factors to be applied at the 
             specified date
        """
        pass

    def GetSplitFactor(self, searchDate):
        """
        GetSplitFactor(self: FactorFile, searchDate: DateTime) -> Decimal
        
            Gets the split factor to be applied at the 
             specified date
        """
        pass

    def GetSplitsAndDividends(self, symbol, exchangeHours):
        """
        GetSplitsAndDividends(self: FactorFile, symbol: Symbol, exchangeHours: SecurityExchangeHours) -> List[BaseData]
        
            Gets all of the splits and dividends represented 
             by this factor file
        
        
            symbol: The symbol to ues for the dividend and split 
             objects
        
            exchangeHours: Exchange hours used for resolving the previous 
             trading day
        
            Returns: All splits and diviends represented by this 
             factor file in chronological order
        """
        pass

    def HasDividendEventOnNextTradingDay(self, date, priceFactorRatio):
        """
        HasDividendEventOnNextTradingDay(self: FactorFile, date: DateTime) -> (bool, Decimal)
        
            Returns true if the specified date is the last 
             trading day before a dividend event
                    
             is to be fired
        
        
            date: The date to check the factor file for a dividend 
             event
        """
        pass

    @staticmethod
    def HasScalingFactors(permtick, market):
        """
        HasScalingFactors(permtick: str, market: str) -> bool
        
            Checks whether or not a symbol has scaling factors
        """
        pass

    def HasSplitEventOnNextTradingDay(self, date, splitFactor):
        """
        HasSplitEventOnNextTradingDay(self: FactorFile, date: DateTime) -> (bool, Decimal)
        
            Returns true if the specified date is the last 
             trading day before a split event
                    is 
             to be fired
        """
        pass

    @staticmethod
    def Parse(permtick, lines):
        """ Parse(permtick: str, lines: IEnumerable[str]) -> FactorFile """
        pass

    @staticmethod
    def Read(permtick, market):
        """
        Read(permtick: str, market: str) -> FactorFile
        
            Reads a FactorFile in from the 
             QuantConnect.Globals.DataFolder.
        """
        pass

    def ToCsvLines(self):
        """
        ToCsvLines(self: FactorFile) -> IEnumerable[str]
        
            Writes this factor file data to an enumerable of 
             csv lines
        
            Returns: An enumerable of lines representing this factor 
             file
        """
        pass

    def WriteToCsv(self, symbol):
        """
        WriteToCsv(self: FactorFile, symbol: Symbol)
            Write the factor file to the correct place in the 
             default Data folder
        
        
            symbol: The symbol this factor file represents
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[FactorFileRow](enumerable: IEnumerable[FactorFileRow], value: FactorFileRow) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, permtick, data, factorFileMinimumDate):
        """ __new__(cls: type, permtick: str, data: IEnumerable[FactorFileRow], factorFileMinimumDate: Nullable[DateTime]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    FactorFileMinimumDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minimum tradeable date for the symbol

Get: FactorFileMinimumDate(self: FactorFile) -> Nullable[DateTime]

Set: FactorFileMinimumDate(self: FactorFile) = value
"""

    MostRecentFactorChange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the most recent factor change in the factor file

Get: MostRecentFactorChange(self: FactorFile) -> DateTime

"""

    Permtick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the symbol this factor file represents

Get: Permtick(self: FactorFile) -> str

"""

    SortedFactorFileData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The factor file data rows sorted by date

Get: SortedFactorFileData(self: FactorFile) -> SortedList[DateTime, FactorFileRow]

Set: SortedFactorFileData(self: FactorFile) = value
"""



class FactorFileRow(object):
    """
    Defines a single row in a factor_factor file. This is a csv file ordered as {date, price factor, split factor, reference price}
    
    FactorFileRow(date: DateTime, priceFactor: Decimal, splitFactor: Decimal, referencePrice: Decimal)
    """
    def Apply(self, *__args):
        """
        Apply(self: FactorFileRow, dividend: Dividend, exchangeHours: SecurityExchangeHours) -> FactorFileRow
        
            Applies the dividend to this factor file row.
           
                      This dividend date must be on or before 
             the factor
                    file row date
        
        
            dividend: The dividend to apply with reference price and 
             distribution specified
        
            exchangeHours: Exchange hours used for resolving the previous 
             trading day
        
            Returns: A new factor file row that applies the dividend 
             to this row's factors
        
        Apply(self: FactorFileRow, split: Split, exchangeHours: SecurityExchangeHours) -> FactorFileRow
        
            Applies the split to this factor file row.
              
                   This split date must be on or before the 
             factor
                    file row date
        
        
            split: The split to apply with reference price and split 
             factor specified
        
            exchangeHours: Exchange hours used for resolving the previous 
             trading day
        
            Returns: A new factor file row that applies the split to 
             this row's factors
        """
        pass

    def GetDividend(self, futureFactorFileRow, symbol, exchangeHours):
        """
        GetDividend(self: FactorFileRow, futureFactorFileRow: FactorFileRow, symbol: Symbol, exchangeHours: SecurityExchangeHours) -> Dividend
        
            Creates a new dividend from this factor file row 
             and the one chronologically in front of it
              
                   This dividend may have a distribution of 
             zero if this row doesn't represent a dividend
        
        
            futureFactorFileRow: The next factor file row in time
            symbol: The symbol to use for the dividend
            exchangeHours: Exchange hours used for resolving the previous 
             trading day
        
            Returns: A new dividend instance
        """
        pass

    def GetSplit(self, futureFactorFileRow, symbol, exchangeHours):
        """
        GetSplit(self: FactorFileRow, futureFactorFileRow: FactorFileRow, symbol: Symbol, exchangeHours: SecurityExchangeHours) -> Split
        
            Creates a new split from this factor file row and 
             the one chronologically in front of it
                  
               This split may have a split factor of one if 
             this row doesn't represent a split
        
        
            futureFactorFileRow: The next factor file row in time
            symbol: The symbol to use for the split
            exchangeHours: Exchange hours used for resolving the previous 
             trading day
        
            Returns: A new split instance
        """
        pass

    @staticmethod
    def Parse(lines, factorFileMinimumDate):
        """ Parse(lines: IEnumerable[str]) -> (List[FactorFileRow], Nullable[DateTime]) """
        pass

    @staticmethod
    def Read(permtick, market, factorFileMinimumDate):
        """ Read(permtick: str, market: str) -> (IEnumerable[FactorFileRow], Nullable[DateTime]) """
        pass

    def ToCsv(self, source):
        """
        ToCsv(self: FactorFileRow, source: str) -> str
        
            Writes this row to csv format
        """
        pass

    def ToString(self):
        """
        ToString(self: FactorFileRow) -> str
        
            Returns a string that represents the current 
             object.
        
            Returns: A string that represents the current object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, date, priceFactor, splitFactor, referencePrice):
        """ __new__(cls: type, date: DateTime, priceFactor: Decimal, splitFactor: Decimal, referencePrice: Decimal) """
        pass

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the date associated with this data

Get: Date(self: FactorFileRow) -> DateTime

"""

    PriceFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the price factor associated with this data

Get: PriceFactor(self: FactorFileRow) -> Decimal

Set: PriceFactor(self: FactorFileRow) = value
"""

    PriceScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the combined factor used to create adjusted prices from raw prices

Get: PriceScaleFactor(self: FactorFileRow) -> Decimal

"""

    ReferencePrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the raw closing value from the trading date before the updated factor takes effect

Get: ReferencePrice(self: FactorFileRow) -> Decimal

"""

    SplitFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the split factor associated with the date

Get: SplitFactor(self: FactorFileRow) -> Decimal

Set: SplitFactor(self: FactorFileRow) = value
"""



class LocalDiskFactorFileProvider(object, IFactorFileProvider):
    """
    Provides an implementation of QuantConnect.Interfaces.IFactorFileProvider that searches the local disk
    
    LocalDiskFactorFileProvider()
    LocalDiskFactorFileProvider(mapFileProvider: IMapFileProvider)
    """
    def Get(self, symbol):
        """
        Get(self: LocalDiskFactorFileProvider, symbol: Symbol) -> FactorFile
        
            Gets a QuantConnect.Data.Auxiliary.FactorFile 
             instance for the specified symbol, or null if not 
             found
        
        
            symbol: The security's symbol whose factor file we seek
            Returns: The resolved factor file, or null if not found
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, mapFileProvider=None):
        """
        __new__(cls: type)
        __new__(cls: type, mapFileProvider: IMapFileProvider)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class LocalDiskMapFileProvider(object, IMapFileProvider):
    """
    Provides a default implementation of QuantConnect.Interfaces.IMapFileProvider that reads from
                the local disk
    
    LocalDiskMapFileProvider()
    """
    def Get(self, market):
        """
        Get(self: LocalDiskMapFileProvider, market: str) -> MapFileResolver
        
            Gets a 
             QuantConnect.Data.Auxiliary.MapFileResolver 
             representing all the map
                    files for 
             the specified market
        
        
            market: The equity market, for example, 'usa'
            Returns: A QuantConnect.Data.Auxiliary.MapFileRow 
             containing all map files for the specified market
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class MapFile(object, IEnumerable[MapFileRow], IEnumerable):
    """
    Represents an entire map file for a specified symbol
    
    MapFile(permtick: str, data: IEnumerable[MapFileRow])
    """
    def GetEnumerator(self):
        """
        GetEnumerator(self: MapFile) -> IEnumerator[MapFileRow]
        
            Returns an enumerator that iterates through the 
             collection.
        
            Returns: A System.Collections.Generic.IEnumerator that can 
             be used to iterate through the collection.
        """
        pass

    @staticmethod
    def GetMapFilePath(permtick, market):
        """
        GetMapFilePath(permtick: str, market: str) -> str
        
            Constructs the map file path for the specified 
             market and symbol
        
        
            permtick: The symbol as on disk, OIH or OIH.1
            market: The market this symbol belongs to
            Returns: The file path to the requested map file
        """
        pass

    @staticmethod
    def GetMapFiles(mapFileDirectory):
        """
        GetMapFiles(mapFileDirectory: str) -> IEnumerable[MapFile]
        
            Reads all the map files in the specified directory
        
            mapFileDirectory: The map file directory path
            Returns: An enumerable of all map files
        """
        pass

    def GetMappedSymbol(self, searchDate, defaultReturnValue):
        """
        GetMappedSymbol(self: MapFile, searchDate: DateTime, defaultReturnValue: str) -> str
        
            Memory overload search method for finding the 
             mapped symbol for this date.
        
        
            searchDate: date for symbol we need to find.
            defaultReturnValue: Default return value if search was got no result.
            Returns: Symbol on this date.
        """
        pass

    def HasData(self, date):
        """
        HasData(self: MapFile, date: DateTime) -> bool
        
            Determines if there's data for the requested date
        """
        pass

    @staticmethod
    def Read(permtick, market):
        """
        Read(permtick: str, market: str) -> MapFile
        
            Reads in an entire map file for the requested 
             symbol from the DataFolder
        """
        pass

    def ToCsvLines(self):
        """
        ToCsvLines(self: MapFile) -> IEnumerable[str]
        
            Reads and writes each 
             QuantConnect.Data.Auxiliary.MapFileRow
        
            Returns: Enumerable of csv lines
        """
        pass

    def WriteToCsv(self, market):
        """
        WriteToCsv(self: MapFile, market: str)
            Writes the map file to a CSV file
        
            market: The market to save the MapFile to
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MapFileRow](enumerable: IEnumerable[MapFileRow], value: MapFileRow) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, permtick, data):
        """ __new__(cls: type, permtick: str, data: IEnumerable[MapFileRow]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    DelistingDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the last date in the map file which is indicative of a delisting event

Get: DelistingDate(self: MapFile) -> DateTime

"""

    FirstDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the first date in this map file

Get: FirstDate(self: MapFile) -> DateTime

"""

    FirstTicker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the first ticker for the security represented by this map file

Get: FirstTicker(self: MapFile) -> str

"""

    Permtick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the entity's unique symbol, i.e OIH.1

Get: Permtick(self: MapFile) -> str

"""



class MapFileResolver(object, IEnumerable[MapFile], IEnumerable):
    """
    Provides a means of mapping a symbol at a point in time to the map file
                containing that share class's mapping information
    
    MapFileResolver(mapFiles: IEnumerable[MapFile])
    """
    @staticmethod
    def Create(*__args):
        """
        Create(dataDirectory: str, market: str) -> MapFileResolver
        
            Creates a new instance of the 
             QuantConnect.Data.Auxiliary.MapFileResolver class 
             by reading all map files
                    for the 
             specified market into memory
        
        
            dataDirectory: The root data directory
            market: The equity market to produce a map file 
             collection for
        
            Returns: The collection of map files capable of mapping 
             equity symbols within the specified market
        
        Create(mapFileDirectory: str) -> MapFileResolver
        
            Creates a new instance of the 
             QuantConnect.Data.Auxiliary.MapFileResolver class 
             by reading all map files
                    for the 
             specified market into memory
        
        
            mapFileDirectory: The directory containing the map files
            Returns: The collection of map files capable of mapping 
             equity symbols within the specified market
        """
        pass

    def GetByPermtick(self, permtick):
        """
        GetByPermtick(self: MapFileResolver, permtick: str) -> MapFile
        
            Gets the map file matching the specified permtick
        
            permtick: The permtick to match on
            Returns: The map file matching the permtick, or null if 
             not found
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MapFileResolver) -> IEnumerator[MapFile]
        
            Returns an enumerator that iterates through the 
             collection.
        
            Returns: A System.Collections.Generic.IEnumerator that can 
             be used to iterate through the collection.
        """
        pass

    def ResolveMapFile(self, symbol, date):
        """
        ResolveMapFile(self: MapFileResolver, symbol: str, date: DateTime) -> MapFile
        
            Resolves the map file path containing the mapping 
             information for the symbol defined at date
        
        
            symbol: The symbol as of date to be mapped
            date: The date associated with the symbol
            Returns: The map file responsible for mapping the symbol, 
             if no map file is found, null is returned
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MapFile](enumerable: IEnumerable[MapFile], value: MapFile) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, mapFiles):
        """ __new__(cls: type, mapFiles: IEnumerable[MapFile]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Empty = None


class MapFileRow(object, IEquatable[MapFileRow]):
    """
    Represents a single row in a map_file. This is a csv file ordered as {date, mapped symbol}
    
    MapFileRow(date: DateTime, mappedSymbol: str)
    """
    def Equals(self, *__args):
        """
        Equals(self: MapFileRow, other: MapFileRow) -> bool
        
            Indicates whether the current object is equal to 
             another object of the same type.
        
        
            other: An object to compare with this object.
            Returns: true if the current object is equal to the other 
             parameter; otherwise, false.
        
        Equals(self: MapFileRow, obj: object) -> bool
        
            Determines whether the specified System.Object is 
             equal to the current System.Object.
        
        
            obj: The object to compare with the current object.
            Returns: true if the specified object  is equal to the 
             current object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: MapFileRow) -> int
        
            Serves as a hash function for a particular type.
            Returns: A hash code for the current System.Object.
        """
        pass

    @staticmethod
    def Parse(line):
        """
        Parse(line: str) -> MapFileRow
        
            Parses the specified line into a MapFileRow
        """
        pass

    @staticmethod
    def Read(*__args):
        """
        Read(permtick: str, market: str) -> IEnumerable[MapFileRow]
        
            Reads in the map_file for the specified equity 
             symbol
        
        Read(path: str) -> IEnumerable[MapFileRow]
        
            Reads in the map_file at the specified path
        """
        pass

    def ToCsv(self):
        """
        ToCsv(self: MapFileRow) -> str
        
            Writes this row to csv format
        """
        pass

    def ToString(self):
        """ ToString(self: MapFileRow) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, date, mappedSymbol):
        """ __new__(cls: type, date: DateTime, mappedSymbol: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the date associated with this data

Get: Date(self: MapFileRow) -> DateTime

"""

    MappedSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the mapped symbol

Get: MappedSymbol(self: MapFileRow) -> str

"""



class MappingExtensions(object):
    """ Mapping extensions helper methods """
    @staticmethod
    def ResolveMapFile(mapFileResolver, symbol, dataType):
        """
        ResolveMapFile(mapFileResolver: MapFileResolver, symbol: Symbol, dataType: Type) -> MapFile
        
            Helper method to resolve the mapping file to use.
        
            mapFileResolver: The map file resolver
            symbol: The symbol that we want to map
            dataType: The configuration data type 
             QuantConnect.Data.SubscriptionDataConfig.Type
        
            Returns: The mapping file to use
        """
        pass

    __all__ = [
        'ResolveMapFile',
    ]


class ZipEntryName(BaseData, IBaseData):
    """
    Defines a data type that just produces data points from the zip entry names in a zip file
    
    ZipEntryName()
    """
    def GetSource(self, config, date, *__args):
        """
        GetSource(self: ZipEntryName, config: SubscriptionDataConfig, date: DateTime, isLiveMode: bool) -> SubscriptionDataSource
        
            Return the URL string source of the file. This 
             will be converted to a stream
        
        
            config: Configuration object
            date: Date of this source file
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: String URL of source file.
        """
        pass

    def Reader(self, config, *__args):
        """
        Reader(self: ZipEntryName, config: SubscriptionDataConfig, line: str, date: DateTime, isLiveMode: bool) -> BaseData
        
            Reader converts each line of the data source into 
             BaseData objects. Each data type creates its own 
             factory method, and returns a new instance of the 
             object
                    each time it is called. The 
             returned object is assumed to be time stamped in 
             the config.ExchangeTimeZone.
        
        
            config: Subscription data config setup object
            line: Line of the source document
            date: Date of the requested data
            isLiveMode: true if we're in live mode, false for backtesting 
             mode
        
            Returns: Instance of the T:BaseData object generated by 
             this line of the CSV
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


