# encoding: utf-8
# module QuantConnect.Securities.Interfaces calls itself Interfaces
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AdjustmentType(Enum, IComparable, IFormattable, IConvertible):
    """
    Enum defines types of possible price adjustments in continuous contract modeling.
    
    enum AdjustmentType, values: BackAdjusted (1), ForwardAdjusted (0)
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

    BackAdjusted = None
    ForwardAdjusted = None
    value__ = None


class IContinuousContractModel:
    """
    Continuous contract model interface. Interfaces is implemented by different classes
                realizing various methods for modeling continuous security series. Primarily, modeling of continuous futures.
                Continuous contracts are used in backtesting of otherwise expiring derivative contracts.
                Continuous contracts are not traded, and are not products traded on exchanges.
    """
    def GetContinuousData(self, dateTime):
        """
        GetContinuousData(self: IContinuousContractModel, dateTime: DateTime) -> IEnumerator[BaseData]
        
            Method returns continuous prices from the list of 
             current and historical data series for one root 
             symbol.
                    It returns enumerator of 
             stitched continuous quotes, produced by the 
             model.
                    e.g. 6BH15, 6BM15, 6BU15, 
             6BZ15 will result in one 6B continuous historical 
             series for 2015
        
            Returns: Continuous prices
        """
        pass

    def GetCurrentSymbol(self, dateTime):
        """
        GetCurrentSymbol(self: IContinuousContractModel, dateTime: DateTime) -> Symbol
        
            Returns current symbol name that corresponds to 
             the current continuous model,
                    or 
             null if none.
        
            Returns: Current symbol name
        """
        pass

    def GetRollDates(self):
        """
        GetRollDates(self: IContinuousContractModel) -> IEnumerator[DateTime]
        
            Returns the list of roll dates for the contract.
            Returns: The list of roll dates
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AdjustmentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Adjustment type, implemented by the model

Get: AdjustmentType(self: IContinuousContractModel) -> AdjustmentType

Set: AdjustmentType(self: IContinuousContractModel) = value
"""

    InputSeries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of current and historical data series for one root symbol.
            e.g. 6BH16, 6BM16, 6BU16, 6BZ16

Get: InputSeries(self: IContinuousContractModel) -> IEnumerator[BaseData]

Set: InputSeries(self: IContinuousContractModel) = value
"""



class ISecurityDataFilter:
    """ Security data filter interface. Defines pattern for the user defined data filter techniques. """
    def Filter(self, vehicle, data):
        """
        Filter(self: ISecurityDataFilter, vehicle: Security, data: BaseData) -> bool
        
            Filter out a tick from this security, with this 
             new data:
        
        
            vehicle: Security of this filter.
            data: New data packet we're checking
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


