# encoding: utf-8
# module QuantConnect.Logging calls itself Logging
# from QuantConnect.Logging, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CompositeLogHandler(object, ILogHandler, IDisposable):
    """
    Provides an QuantConnect.Logging.ILogHandler implementation that composes multiple handlers
    
    CompositeLogHandler()
    CompositeLogHandler(*handlers: Array[ILogHandler])
    """
    def Debug(self, text):
        """
        Debug(self: CompositeLogHandler, text: str)
            Write debug message to log
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CompositeLogHandler)
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def Error(self, text):
        """
        Error(self: CompositeLogHandler, text: str)
            Write error message to log
        """
        pass

    def Trace(self, text):
        """
        Trace(self: CompositeLogHandler, text: str)
            Write debug message to log
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
    def __new__(self, handlers=None):
        """
        __new__(cls: type)
        __new__(cls: type, *handlers: Array[ILogHandler])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class CompositeNLogHandler(object, ILogHandler, IDisposable):
    """
    Provides an QuantConnect.Logging.ILogHandler implementation that composes multiple handlers
    
    CompositeNLogHandler()
    CompositeNLogHandler(*handlers: Array[ILogHandler])
    """
    def Debug(self, text):
        """
        Debug(self: CompositeNLogHandler, text: str)
            Write debug message to log
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CompositeNLogHandler)
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def Error(self, text):
        """
        Error(self: CompositeNLogHandler, text: str)
            Write error message to log
        """
        pass

    def Trace(self, text):
        """
        Trace(self: CompositeNLogHandler, text: str)
            Write debug message to log
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
    def __new__(self, handlers=None):
        """
        __new__(cls: type)
        __new__(cls: type, *handlers: Array[ILogHandler])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ConsoleLogHandler(object, ILogHandler, IDisposable):
    """
    ILogHandler implementation that writes log output to console.
    
    ConsoleLogHandler()
    ConsoleLogHandler(dateFormat: str)
    """
    def Debug(self, text):
        """
        Debug(self: ConsoleLogHandler, text: str)
            Write debug message to log
        
            text: The debug text to log
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ConsoleLogHandler)
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def Error(self, text):
        """
        Error(self: ConsoleLogHandler, text: str)
            Write error message to log
        
            text: The error text to log
        """
        pass

    def Trace(self, text):
        """
        Trace(self: ConsoleLogHandler, text: str)
            Write debug message to log
        
            text: The trace text to log
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
    def __new__(self, dateFormat=None):
        """
        __new__(cls: type)
        __new__(cls: type, dateFormat: str)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class FileLogHandler(object, ILogHandler, IDisposable):
    """
    Provides an implementation of QuantConnect.Logging.ILogHandler that writes all log messages to a file on disk.
    
    FileLogHandler(filepath: str, useTimestampPrefix: bool)
    FileLogHandler()
    """
    def CreateMessage(self, *args): #cannot find CLR method
        """
        CreateMessage(self: FileLogHandler, text: str, level: str) -> str
        
            Creates the message to be logged
        
            text: The text to be logged
            level: The logging leel
        """
        pass

    def Debug(self, text):
        """
        Debug(self: FileLogHandler, text: str)
            Write debug message to log
        
            text: The debug text to log
        """
        pass

    def Dispose(self):
        """
        Dispose(self: FileLogHandler)
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def Error(self, text):
        """
        Error(self: FileLogHandler, text: str)
            Write error message to log
        
            text: The error text to log
        """
        pass

    def Trace(self, text):
        """
        Trace(self: FileLogHandler, text: str)
            Write debug message to log
        
            text: The trace text to log
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
    def __new__(self, filepath=None, useTimestampPrefix=None):
        """
        __new__(cls: type, filepath: str, useTimestampPrefix: bool)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class FunctionalLogHandler(object, ILogHandler, IDisposable):
    """
    ILogHandler implementation that writes log output to result handler
    
    FunctionalLogHandler()
    FunctionalLogHandler(debug: Action[str], trace: Action[str], error: Action[str])
    """
    def Debug(self, text):
        """
        Debug(self: FunctionalLogHandler, text: str)
            Write debug message to log
        
            text: The debug text to log
        """
        pass

    def Dispose(self):
        """
        Dispose(self: FunctionalLogHandler)
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def Error(self, text):
        """
        Error(self: FunctionalLogHandler, text: str)
            Write error message to log
        
            text: The error text to log
        """
        pass

    def Trace(self, text):
        """
        Trace(self: FunctionalLogHandler, text: str)
            Write debug message to log
        
            text: The trace text to log
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
    def __new__(self, debug=None, trace=None, error=None):
        """
        __new__(cls: type)
        __new__(cls: type, debug: Action[str], trace: Action[str], error: Action[str])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ILogHandler(IDisposable):
    """ Interface for redirecting log output """
    def Debug(self, text):
        """
        Debug(self: ILogHandler, text: str)
            Write debug message to log
        
            text: The debug text to log
        """
        pass

    def Error(self, text):
        """
        Error(self: ILogHandler, text: str)
            Write error message to log
        
            text: The error text to log
        """
        pass

    def Trace(self, text):
        """
        Trace(self: ILogHandler, text: str)
            Write debug message to log
        
            text: The trace text to log
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Log(object):
    """ Logging management class. """
    @staticmethod
    def Debug(text, level, delay):
        """
        Debug(text: str, level: int, delay: int)
            Output to the console, and sleep the thread for a 
             little period to monitor the results.
        
        
            level: debug level
        """
        pass

    @staticmethod
    def Error(*__args):
        """
        Error(error: str, overrideMessageFloodProtection: bool)
            Log error
        
            error: String Error
            overrideMessageFloodProtection: Force sending a message, overriding the "do not 
             flood" directive
        
        Error(exception: Exception, message: str, overrideMessageFloodProtection: bool)
            Log error
        
            exception: The exception to be logged
            message: An optional message to be logged, if 
             null/whitespace the messge text will be extracted
        
            overrideMessageFloodProtection: Force sending a message, overriding the "do not 
             flood" directive
        
        Error(format: str, *args: Array[object])
            Writes the message in red
        """
        pass

    @staticmethod
    def Trace(*__args):
        """
        Trace(traceText: str, overrideMessageFloodProtection: bool)
            Log trace
        Trace(format: str, *args: Array[object])
            Writes the message in normal text
        """
        pass

    @staticmethod
    def VarDump(obj, recursion):
        """
        VarDump(obj: object, recursion: int) -> str
        
            C# Equivalent of Print_r in PHP:
        """
        pass

    DebuggingEnabled = False
    DebuggingLevel = 1
    FilePath = 'log.txt'
    LogHandler = None
    __all__ = [
        'Debug',
        'Error',
        'Trace',
        'VarDump',
    ]


class LogEntry(object):
    """
    Log entry wrapper to make logging simpler:
    
    LogEntry(message: str)
    LogEntry(message: str, time: DateTime, type: LogType)
    """
    def ToString(self):
        """
        ToString(self: LogEntry) -> str
        
            Helper override on the log entry.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message, time=None, type=None):
        """
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, time: DateTime, type: LogType)
        """
        pass

    Message = None
    MessageType = None
    Time = None


class LogHandlerExtensions(object):
    """ Logging extensions. """
    @staticmethod
    def Debug(logHandler, text, args):
        """
        Debug(logHandler: ILogHandler, text: str, *args: Array[object])
            Write debug message to log
        
            text: Message
            args: Arguments to format.
        """
        pass

    @staticmethod
    def Error(logHandler, text, args):
        """
        Error(logHandler: ILogHandler, text: str, *args: Array[object])
            Write error message to log
        
            text: Message
            args: Arguments to format.
        """
        pass

    @staticmethod
    def Trace(logHandler, text, args):
        """
        Trace(logHandler: ILogHandler, text: str, *args: Array[object])
            Write debug message to log
        
            text: Message
            args: Arguments to format.
        """
        pass

    __all__ = [
        'Debug',
        'Error',
        'Trace',
    ]


class LogType(Enum, IComparable, IFormattable, IConvertible):
    """
    Error level
    
    enum LogType, values: Debug (0), Error (2), Trace (1)
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

    Debug = None
    Error = None
    Trace = None
    value__ = None


class NLogHandler(object, ILogHandler, IDisposable):
    """
    Provides an implementation of QuantConnect.Logging.ILogHandler that writes all log messages to a file on disk.
    
    NLogHandler()
    """
    def CreateMessage(self, *args): #cannot find CLR method
        """
        CreateMessage(self: NLogHandler, text: str, level: str) -> str
        
            Creates the message to be logged
        
            text: The text to be logged
            level: The logging leel
        """
        pass

    def Debug(self, text):
        """
        Debug(self: NLogHandler, text: str)
            Write debug message to log
        
            text: The debug text to log
        """
        pass

    def Dispose(self):
        """
        Dispose(self: NLogHandler)
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def Error(self, text):
        """
        Error(self: NLogHandler, text: str)
            Write error message to log
        
            text: The error text to log
        """
        pass

    def Trace(self, text):
        """
        Trace(self: NLogHandler, text: str)
            Write debug message to log
        
            text: The trace text to log
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class QueueLogHandler(object, ILogHandler, IDisposable):
    """
    ILogHandler implementation that queues all logs and writes them when instructed.
    
    QueueLogHandler()
    """
    def Debug(self, text):
        """
        Debug(self: QueueLogHandler, text: str)
            Write debug message to log
        
            text: The debug text to log
        """
        pass

    def Dispose(self):
        """
        Dispose(self: QueueLogHandler)
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def Error(self, text):
        """
        Error(self: QueueLogHandler, text: str)
            Write error message to log
        
            text: The error text to log
        """
        pass

    def OnLogEvent(self, *args): #cannot find CLR method
        """
        OnLogEvent(self: QueueLogHandler, log: LogEntry)
            Raise a log event safely
        """
        pass

    def Trace(self, text):
        """
        Trace(self: QueueLogHandler, text: str)
            Write debug message to log
        
            text: The trace text to log
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Logs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Public access to the queue for log processing.

Get: Logs(self: QueueLogHandler) -> ConcurrentQueue[LogEntry]

"""


    LogEvent = None
    LogEventRaised = None


class RegressionFileLogHandler(FileLogHandler, ILogHandler, IDisposable):
    """
    Provides an implementation of QuantConnect.Logging.ILogHandler that writes all log messages to a file on disk
                without timestamps.
    
    RegressionFileLogHandler()
    """
    def CreateMessage(self, *args): #cannot find CLR method
        """
        CreateMessage(self: FileLogHandler, text: str, level: str) -> str
        
            Creates the message to be logged
        
            text: The text to be logged
            level: The logging leel
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


class WhoCalledMe(object):
    """ Provides methods for determining higher stack frames """
    @staticmethod
    def GetMethodName(frame):
        """
        GetMethodName(frame: int) -> str
        
            Gets the method name of the caller
        
            frame: The number of stack frames to retrace from the 
             caller's position
        
            Returns: The method name of the containing scope 'frame' 
             stack frames above the caller
        """
        pass

    __all__ = [
        'GetMethodName',
    ]


