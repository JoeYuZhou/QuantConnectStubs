# encoding: utf-8
# module QuantConnect.Util.RateLimit calls itself RateLimit
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BusyWaitSleepStrategy(object, ISleepStrategy):
    """
    Provides a CPU intensive means of waiting for more tokens to be available in QuantConnect.Util.RateLimit.ITokenBucket.
                This strategy is only viable when the requested number of tokens is expected to become available in an
                extremely short period of time. This implementation aims to keep the current thread executing to prevent
                potential content switches arising from a thread yielding or sleeping strategy.
    
    BusyWaitSleepStrategy()
    """
    def Sleep(self):
        """
        Sleep(self: BusyWaitSleepStrategy)
            Provides a CPU intensive sleep by executing 
             System.Threading.Thread.SpinWait(System.Int32) 
             for a single spin.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class FixedIntervalRefillStrategy(object, IRefillStrategy):
    """
    Provides a refill strategy that has a constant, quantized refill rate.
                For example, after 1 minute passes add 5 units. If 59 seconds has passed, it will add zero unit,
                but if 2 minutes have passed, then 10 units would be added.
    
    FixedIntervalRefillStrategy(timeProvider: ITimeProvider, refillAmount: Int64, refillInterval: TimeSpan)
    """
    def Refill(self):
        """
        Refill(self: FixedIntervalRefillStrategy) -> Int64
        
            Computes the number of new tokens made available 
             to the bucket for consumption by determining the
        
                         number of time intervals that have 
             passed and multiplying by the number of tokens to 
             refill for
                    each time interval.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, timeProvider, refillAmount, refillInterval):
        """ __new__(cls: type, timeProvider: ITimeProvider, refillAmount: Int64, refillInterval: TimeSpan) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class IRefillStrategy:
    """ Provides a strategy for making tokens available for consumption in the QuantConnect.Util.RateLimit.ITokenBucket """
    def Refill(self):
        """
        Refill(self: IRefillStrategy) -> Int64
        
            Computes the number of new tokens made available, 
             typically via the passing of time.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISleepStrategy:
    """
    Defines a strategy for sleeping the current thread of execution. This is currently used via the
                QuantConnect.Util.RateLimit.ITokenBucket.Consume(System.Int64,System.Int64) in order to wait for new tokens to become available for consumption.
    """
    def Sleep(self):
        """
        Sleep(self: ISleepStrategy)
            Sleeps the current thread in an implementation 
             specific way
                    and for an 
             implementation specific amount of time
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITokenBucket:
    """
    Defines a token bucket for rate limiting
                See: https://en.wikipedia.org/wiki/Token_bucket
    """
    def Consume(self, tokens, timeout):
        """
        Consume(self: ITokenBucket, tokens: Int64, timeout: Int64)
            Blocks until the specified number of tokens are 
             available for consumption
                    and then 
             consumes that number of tokens.
        
        
            tokens: The number of tokens to consume
            timeout: The maximum amount of time, in milliseconds, to 
             block. A System.TimeoutException
                    is 
             throw in the event it takes longer than the 
             stated timeout to consume the requested number of 
             tokens.
                    The default timeout is set 
             to infinite, which will block forever.
        """
        pass

    def TryConsume(self, tokens):
        """
        TryConsume(self: ITokenBucket, tokens: Int64) -> bool
        
            Attempts to consume the specified number of 
             tokens from the bucket. If the
                    
             requested number of tokens are not immediately 
             available, then this method
                    will 
             return false to indicate that zero tokens have 
             been consumed.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AvailableTokens = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total number of currently available tokens for consumption

Get: AvailableTokens(self: ITokenBucket) -> Int64

"""

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum capacity of tokens this bucket can hold.

Get: Capacity(self: ITokenBucket) -> Int64

"""



class LeakyBucket(object, ITokenBucket):
    """
    Provides an implementation of QuantConnect.Util.RateLimit.ITokenBucket that implements the leaky bucket algorithm
                See: https://en.wikipedia.org/wiki/Leaky_bucket
    
    LeakyBucket(capacity: Int64, refillAmount: Int64, refillInterval: TimeSpan)
    LeakyBucket(capacity: Int64, sleep: ISleepStrategy, refill: IRefillStrategy, timeProvider: ITimeProvider)
    """
    def Consume(self, tokens, timeout):
        """
        Consume(self: LeakyBucket, tokens: Int64, timeout: Int64)
            Blocks until the specified number of tokens are 
             available for consumption
                    and then 
             consumes that number of tokens.
        
        
            tokens: The number of tokens to consume
            timeout: The maximum amount of time, in milliseconds, to 
             block. An exception is
                    throw in the 
             event it takes longer than the stated timeout to 
             consume the requested number
                    of 
             tokens
        """
        pass

    def TryConsume(self, tokens):
        """
        TryConsume(self: LeakyBucket, tokens: Int64) -> bool
        
            Attempts to consume the specified number of 
             tokens from the bucket. If the
                    
             requested number of tokens are not immediately 
             available, then this method
                    will 
             return false to indicate that zero tokens have 
             been consumed.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, capacity, *__args):
        """
        __new__(cls: type, capacity: Int64, refillAmount: Int64, refillInterval: TimeSpan)
        __new__(cls: type, capacity: Int64, sleep: ISleepStrategy, refill: IRefillStrategy, timeProvider: ITimeProvider)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AvailableTokens = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total number of currently available tokens for consumption

Get: AvailableTokens(self: LeakyBucket) -> Int64

"""

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the maximum capacity of tokens this bucket can hold.

Get: Capacity(self: LeakyBucket) -> Int64

"""



class ThreadSleepStrategy(object, ISleepStrategy):
    """
    Provides a CPU non-intensive means of waiting for more tokens to be available in QuantConnect.Util.RateLimit.ITokenBucket.
                This strategy should be the most commonly used as it either sleeps or yields the currently executing thread,
                allowing for other threads to execute while the current thread is blocked and waiting for new tokens to become
                available in the bucket for consumption.
    
    ThreadSleepStrategy(milliseconds: int)
    """
    def Sleep(self):
        """
        Sleep(self: ThreadSleepStrategy)
            Sleeps the current thread using the initialized 
             number of milliseconds
        """
        pass

    @staticmethod
    def Sleeping(milliseconds):
        """
        Sleeping(milliseconds: int) -> ISleepStrategy
        
            Gets an instance of 
             QuantConnect.Util.RateLimit.ISleepStrategy that 
             sleeps the current thread for
                    the 
             specified number of milliseconds
        
        
            milliseconds: The duration of time to sleep, in milliseconds
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, milliseconds):
        """ __new__(cls: type, milliseconds: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Yielding = None


class TokenBucket(object):
    """
    Provides extension methods for interacting with QuantConnect.Util.RateLimit.ITokenBucket instances as well
                as access to the QuantConnect.Util.RateLimit.TokenBucket.NullTokenBucket via QuantConnect.Util.RateLimit.TokenBucket.Null
    """
    @staticmethod
    def Consume(bucket, tokens, timeout):
        """
        Consume(bucket: ITokenBucket, tokens: Int64, timeout: TimeSpan)
            Provides an overload of 
             QuantConnect.Util.RateLimit.ITokenBucket.Consume(S
             ystem.Int64,System.Int64) that accepts a 
             System.TimeSpan timeout
        """
        pass

    Null = None
    __all__ = [
        'Consume',
    ]


