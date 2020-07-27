# encoding: utf-8
# module QuantConnect.Parameters calls itself Parameters
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ParameterAttribute(Attribute, _Attribute):
    """
    Specifies a field or property is a parameter that can be set
                from an QuantConnect.Packets.AlgorithmNodePacket.Parameters dictionary
    
    ParameterAttribute(name: str)
    """
    @staticmethod
    def ApplyAttributes(parameters, instance):
        """ ApplyAttributes(parameters: Dictionary[str, str], instance: object) """
        pass

    @staticmethod
    def GetParametersFromAssembly(assembly):
        """
        GetParametersFromAssembly(assembly: Assembly) -> Dictionary[str, str]
        
            Resolves all parameter attributes from the 
             specified compiled assembly path
        
        
            assembly: The assembly to inspect
            Returns: Parameters dictionary keyed by parameter name 
             with a value of the member type
        """
        pass

    @staticmethod
    def GetParametersFromType(type):
        """
        GetParametersFromType(type: Type) -> IEnumerable[KeyValuePair[str, str]]
        
            Resolves all parameter attributes from the 
             specified type
        
        
            type: The type to inspect
            Returns: Parameters dictionary keyed by parameter name 
             with a value of the member type
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of this parameter

Get: Name(self: ParameterAttribute) -> str

"""


    BindingFlags = None


