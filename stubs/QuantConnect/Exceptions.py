# encoding: utf-8
# module QuantConnect.Exceptions calls itself Exceptions
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DllNotFoundPythonExceptionInterpreter(object, IExceptionInterpreter):
    """
    Interprets QuantConnect.Exceptions.DllNotFoundPythonExceptionInterpreter instances
    
    DllNotFoundPythonExceptionInterpreter()
    """
    def CanInterpret(self, exception):
        """
        CanInterpret(self: DllNotFoundPythonExceptionInterpreter, exception: Exception) -> bool
        
            Determines if this interpreter should be applied 
             to the specified exception.
        
        
            exception: The exception to check
            Returns: True if the exception can be interpreted, false 
             otherwise
        """
        pass

    def Interpret(self, exception, innerInterpreter):
        """
        Interpret(self: DllNotFoundPythonExceptionInterpreter, exception: Exception, innerInterpreter: IExceptionInterpreter) -> Exception
        
            Interprets the specified exception into a new 
             exception
        
        
            exception: The exception to be interpreted
            innerInterpreter: An interpreter that should be applied to the 
             inner exception.
        
            Returns: The interpreted exception
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the order that an instance of this class should be called

Get: Order(self: DllNotFoundPythonExceptionInterpreter) -> int

"""



class IExceptionInterpreter:
    """ Defines an exception interpreter. Interpretations are invoked on QuantConnect.Interfaces.IAlgorithm.RunTimeError """
    def CanInterpret(self, exception):
        """
        CanInterpret(self: IExceptionInterpreter, exception: Exception) -> bool
        
            Determines if this interpreter should be applied 
             to the specified exception.
        
        
            exception: The exception to check
            Returns: True if the exception can be interpreted, false 
             otherwise
        """
        pass

    def Interpret(self, exception, innerInterpreter):
        """
        Interpret(self: IExceptionInterpreter, exception: Exception, innerInterpreter: IExceptionInterpreter) -> Exception
        
            Interprets the specified exception into a new 
             exception
        
        
            exception: The exception to be interpreted
            innerInterpreter: An interpreter that should be applied to the 
             inner exception.
                    This provides a 
             link back allowing the inner exceptions to be 
             interpreted using the interpreters
                    
             configured in the 
             QuantConnect.Exceptions.IExceptionInterpreter. 
             Individual implementations *may* ignore
                 
                this value if required.
        
            Returns: The interpreted exception
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the order that a class that implements this interface should be called

Get: Order(self: IExceptionInterpreter) -> int

"""



class InvalidTokenPythonExceptionInterpreter(object, IExceptionInterpreter):
    """
    Interprets QuantConnect.Exceptions.InvalidTokenPythonExceptionInterpreter instances
    
    InvalidTokenPythonExceptionInterpreter()
    """
    def CanInterpret(self, exception):
        """
        CanInterpret(self: InvalidTokenPythonExceptionInterpreter, exception: Exception) -> bool
        
            Determines if this interpreter should be applied 
             to the specified exception.
        
        
            exception: The exception to check
            Returns: True if the exception can be interpreted, false 
             otherwise
        """
        pass

    def Interpret(self, exception, innerInterpreter):
        """
        Interpret(self: InvalidTokenPythonExceptionInterpreter, exception: Exception, innerInterpreter: IExceptionInterpreter) -> Exception
        
            Interprets the specified exception into a new 
             exception
        
        
            exception: The exception to be interpreted
            innerInterpreter: An interpreter that should be applied to the 
             inner exception.
        
            Returns: The interpreted exception
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the order that an instance of this class should be called

Get: Order(self: InvalidTokenPythonExceptionInterpreter) -> int

"""



class KeyErrorPythonExceptionInterpreter(object, IExceptionInterpreter):
    """
    Interprets QuantConnect.Exceptions.KeyErrorPythonExceptionInterpreter instances
    
    KeyErrorPythonExceptionInterpreter()
    """
    def CanInterpret(self, exception):
        """
        CanInterpret(self: KeyErrorPythonExceptionInterpreter, exception: Exception) -> bool
        
            Determines if this interpreter should be applied 
             to the specified exception.
        
        
            exception: The exception to check
            Returns: True if the exception can be interpreted, false 
             otherwise
        """
        pass

    def Interpret(self, exception, innerInterpreter):
        """
        Interpret(self: KeyErrorPythonExceptionInterpreter, exception: Exception, innerInterpreter: IExceptionInterpreter) -> Exception
        
            Interprets the specified exception into a new 
             exception
        
        
            exception: The exception to be interpreted
            innerInterpreter: An interpreter that should be applied to the 
             inner exception.
        
            Returns: The interpreted exception
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the order that an instance of this class should be called

Get: Order(self: KeyErrorPythonExceptionInterpreter) -> int

"""



class NoMethodMatchPythonExceptionInterpreter(object, IExceptionInterpreter):
    """
    Interprets QuantConnect.Exceptions.NoMethodMatchPythonExceptionInterpreter instances
    
    NoMethodMatchPythonExceptionInterpreter()
    """
    def CanInterpret(self, exception):
        """
        CanInterpret(self: NoMethodMatchPythonExceptionInterpreter, exception: Exception) -> bool
        
            Determines if this interpreter should be applied 
             to the specified exception.
        
        
            exception: The exception to check
            Returns: True if the exception can be interpreted, false 
             otherwise
        """
        pass

    def Interpret(self, exception, innerInterpreter):
        """
        Interpret(self: NoMethodMatchPythonExceptionInterpreter, exception: Exception, innerInterpreter: IExceptionInterpreter) -> Exception
        
            Interprets the specified exception into a new 
             exception
        
        
            exception: The exception to be interpreted
            innerInterpreter: An interpreter that should be applied to the 
             inner exception.
        
            Returns: The interpreted exception
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the order that an instance of this class should be called

Get: Order(self: NoMethodMatchPythonExceptionInterpreter) -> int

"""



class PythonExceptionInterpreter(object, IExceptionInterpreter):
    """
    Interprets QuantConnect.Exceptions.PythonExceptionInterpreter instances
    
    PythonExceptionInterpreter()
    """
    def CanInterpret(self, exception):
        """
        CanInterpret(self: PythonExceptionInterpreter, exception: Exception) -> bool
        
            Determines if this interpreter should be applied 
             to the specified exception. f
        
        
            exception: The exception to check
            Returns: True if the exception can be interpreted, false 
             otherwise
        """
        pass

    def Interpret(self, exception, innerInterpreter):
        """
        Interpret(self: PythonExceptionInterpreter, exception: Exception, innerInterpreter: IExceptionInterpreter) -> Exception
        
            Interprets the specified exception into a new 
             exception
        
        
            exception: The exception to be interpreted
            innerInterpreter: An interpreter that should be applied to the 
             inner exception.
        
            Returns: The interpreted exception
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the order that an instance of this class should be called

Get: Order(self: PythonExceptionInterpreter) -> int

"""



class ScheduledEventExceptionInterpreter(object, IExceptionInterpreter):
    """
    Interprets QuantConnect.Scheduling.ScheduledEventException instances
    
    ScheduledEventExceptionInterpreter()
    """
    def CanInterpret(self, exception):
        """
        CanInterpret(self: ScheduledEventExceptionInterpreter, exception: Exception) -> bool
        
            Determines if this interpreter should be applied 
             to the specified exception.
        
        
            exception: The exception to check
            Returns: True if the exception can be interpreted, false 
             otherwise
        """
        pass

    def Interpret(self, exception, innerInterpreter):
        """
        Interpret(self: ScheduledEventExceptionInterpreter, exception: Exception, innerInterpreter: IExceptionInterpreter) -> Exception
        
            Interprets the specified exception into a new 
             exception
        
        
            exception: The exception to be interpreted
            innerInterpreter: An interpreter that should be applied to the 
             inner exception.
                    This provides a 
             link back allowing the inner exceptions to be 
             interpreted using the interpreters
                    
             configured in the 
             QuantConnect.Exceptions.IExceptionInterpreter. 
             Individual implementations *may* ignore
                 
                this value if required.
        
            Returns: The interpreted exception
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the order that an instance of this class should be called

Get: Order(self: ScheduledEventExceptionInterpreter) -> int

"""



class StackExceptionInterpreter(object, IExceptionInterpreter):
    """
    Interprets exceptions using the configured interpretations
    
    StackExceptionInterpreter(interpreters: IEnumerable[IExceptionInterpreter])
    """
    def CanInterpret(self, exception):
        """
        CanInterpret(self: StackExceptionInterpreter, exception: Exception) -> bool
        
            Determines if this interpreter should be applied 
             to the specified exception.
        
        
            exception: The exception to check
            Returns: True if the exception can be interpreted, false 
             otherwise
        """
        pass

    @staticmethod
    def CreateFromAssemblies(assemblies):
        """ CreateFromAssemblies(assemblies: IEnumerable[Assembly]) -> StackExceptionInterpreter """
        pass

    def GetExceptionMessageHeader(self, exception):
        """
        GetExceptionMessageHeader(self: StackExceptionInterpreter, exception: Exception) -> str
        
            Combines the exception messages from this 
             exception and all inner exceptions.
        
        
            exception: The exception to create a collated message from
            Returns: The collate exception message
        """
        pass

    def Interpret(self, exception, innerInterpreter):
        """
        Interpret(self: StackExceptionInterpreter, exception: Exception, innerInterpreter: IExceptionInterpreter) -> Exception
        
            Interprets the specified exception into a new 
             exception
        
        
            exception: The exception to be interpreted
            innerInterpreter: An interpreter that should be applied to the 
             inner exception.
                    This provides a 
             link back allowing the inner exceptions to be 
             interpreted using the intepretators
                    
             configured in the 
             QuantConnect.Exceptions.StackExceptionInterpreter.
              Individual implementations *may* ignore
                
                 this value if required.
        
            Returns: The interpreted exception
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, interpreters):
        """ __new__(cls: type, interpreters: IEnumerable[IExceptionInterpreter]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Interpreters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the interpreters loaded into this instance

Get: Interpreters(self: StackExceptionInterpreter) -> IEnumerable[IExceptionInterpreter]

"""

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the order that an instance of this class should be called

Get: Order(self: StackExceptionInterpreter) -> int

"""



class UnsupportedOperandPythonExceptionInterpreter(object, IExceptionInterpreter):
    """
    Interprets QuantConnect.Exceptions.UnsupportedOperandPythonExceptionInterpreter instances
    
    UnsupportedOperandPythonExceptionInterpreter()
    """
    def CanInterpret(self, exception):
        """
        CanInterpret(self: UnsupportedOperandPythonExceptionInterpreter, exception: Exception) -> bool
        
            Determines if this interpreter should be applied 
             to the specified exception.
        
        
            exception: The exception to check
            Returns: True if the exception can be interpreted, false 
             otherwise
        """
        pass

    def Interpret(self, exception, innerInterpreter):
        """
        Interpret(self: UnsupportedOperandPythonExceptionInterpreter, exception: Exception, innerInterpreter: IExceptionInterpreter) -> Exception
        
            Interprets the specified exception into a new 
             exception
        
        
            exception: The exception to be interpreted
            innerInterpreter: An interpreter that should be applied to the 
             inner exception.
        
            Returns: The interpreted exception
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the order that an instance of this class should be called

Get: Order(self: UnsupportedOperandPythonExceptionInterpreter) -> int

"""



