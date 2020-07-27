# encoding: utf-8
# module QuantConnect.Benchmarks calls itself Benchmarks
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class FuncBenchmark(object, IBenchmark):
    """
    Creates a benchmark defined by a function
    
    FuncBenchmark(benchmark: Func[DateTime, Decimal])
    """
    def Evaluate(self, time):
        """
        Evaluate(self: FuncBenchmark, time: DateTime) -> Decimal
        
            Evaluates this benchmark at the specified time
        
            time: The time to evaluate the benchmark at
            Returns: The value of the benchmark at the specified time
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, benchmark):
        """ __new__(cls: type, benchmark: Func[DateTime, Decimal]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class IBenchmark:
    """ Specifies how to compute a benchmark for an algorithm """
    def Evaluate(self, time):
        """
        Evaluate(self: IBenchmark, time: DateTime) -> Decimal
        
            Evaluates this benchmark at the specified time
        
            time: The time to evaluate the benchmark at
            Returns: The value of the benchmark at the specified time
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class SecurityBenchmark(object, IBenchmark):
    """
    Creates a benchmark defined by the closing price of a QuantConnect.Benchmarks.SecurityBenchmark.Security instance
    
    SecurityBenchmark(security: Security)
    """
    def Evaluate(self, time):
        """
        Evaluate(self: SecurityBenchmark, time: DateTime) -> Decimal
        
            Evaluates this benchmark at the specified time in 
             units of the account's currency.
        
        
            time: The time to evaluate the benchmark at
            Returns: The value of the benchmark at the specified time
        
                         in units of the account's currency.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, security):
        """ __new__(cls: type, security: Security) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Security = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The benchmark security

Get: Security(self: SecurityBenchmark) -> Security

"""



