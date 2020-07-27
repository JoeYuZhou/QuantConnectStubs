# encoding: utf-8
# module QuantConnect.Configuration calls itself Configuration
# from QuantConnect.Configuration, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ApplicationParser(object):
    """ Command Line application parser """
    @staticmethod
    def Parse(applicationName, applicationDescription, applicationHelpText, args, options, noArgsShowHelp):
        """ Parse(applicationName: str, applicationDescription: str, applicationHelpText: str, args: Array[str], options: List[CommandLineOption], noArgsShowHelp: bool) -> Dictionary[str, object] """
        pass

    __all__ = [
        'Parse',
    ]


class CommandLineOption(object):
    """
    Auxiliary class to keep information about a specific command line option
    
    CommandLineOption(name: str, type: CommandOptionType, description: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name, type, description):
        """ __new__(cls: type, name: str, type: CommandOptionType, description: str) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Command line option description

Get: Description(self: CommandLineOption) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Command line option name

Get: Name(self: CommandLineOption) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Command line option type

Get: Type(self: CommandLineOption) -> CommandOptionType

"""



class Config(object):
    """ Configuration class loads the required external setup variables to launch the Lean engine. """
    @staticmethod
    def Flatten(*__args):
        """
        Flatten(overrideEnvironment: str) -> JObject
        
            Flattens the jobject with respect to the selected 
             environment and then
                    removes the 
             'environments' node
        
        
            overrideEnvironment: The environment to use
            Returns: The flattened JObject
        Flatten(config: JObject, overrideEnvironment: str) -> JObject
        
            Flattens the jobject with respect to the selected 
             environment and then
                    removes the 
             'environments' node
        
        
            config: The configuration represented as a JObject
            overrideEnvironment: The environment to use
            Returns: The flattened JObject
        """
        pass

    @staticmethod
    def Get(key, defaultValue):
        """
        Get(key: str, defaultValue: str) -> str
        
            Get the matching config setting from the file 
             searching for this key.
        
        
            key: String key value we're seaching for in the config 
             file.
        
            Returns: String value of the configuration setting or 
             empty string if nothing found.
        """
        pass

    @staticmethod
    def GetBool(key, defaultValue):
        """
        GetBool(key: str, defaultValue: bool) -> bool
        
            Get a boolean value configuration setting by a 
             configuration key.
        
        
            key: String value of the configuration key.
            defaultValue: The default value to use if not found in 
             configuration
        
            Returns: Boolean value of the config setting.
        """
        pass

    @staticmethod
    def GetDouble(key, defaultValue):
        """
        GetDouble(key: str, defaultValue: float) -> float
        
            Get the double value of a config string.
        
            key: Search key from the config file
            defaultValue: The default value to use if not found in 
             configuration
        
            Returns: Double value of the config setting.
        """
        pass

    @staticmethod
    def GetEnvironment():
        """
        GetEnvironment() -> str
        
            Gets the currently selected environment. If 
             sub-environments are defined,
                    
             they'll be returned as {env1}.{env2}
        
            Returns: The fully qualified currently selected environment
        """
        pass

    @staticmethod
    def GetInt(key, defaultValue):
        """
        GetInt(key: str, defaultValue: int) -> int
        
            Get the int value of a config string.
        
            key: Search key from the config file
            defaultValue: The default value to use if not found in 
             configuration
        
            Returns: Int value of the config setting.
        """
        pass

    @staticmethod
    def GetToken(key):
        """
        GetToken(key: str) -> JToken
        
            Gets the underlying JToken for the specified key
        """
        pass

    @staticmethod
    def GetValue(key, defaultValue):
        """ GetValue[T](key: str, defaultValue: T) -> T """
        pass

    @staticmethod
    def MergeCommandLineArgumentsWithConfiguration(cliArguments):
        """ MergeCommandLineArgumentsWithConfiguration(cliArguments: Dictionary[str, object]) """
        pass

    @staticmethod
    def Reset():
        """
        Reset()
            Resets the config settings to their default 
             values.
                    Called in regression tests 
             where multiple algorithms are run sequentially,
         
                        and we need to guarantee that every 
             test starts with the same configuration.
        """
        pass

    @staticmethod
    def Set(key, value):
        """
        Set(key: str, value: str)
            Sets a configuration value. This is really only 
             used to help testing. The key heye can be
               
                  specified as {environment}.key to set a 
             value on a specific environment
        
        
            key: The key to be set
            value: The new value
        """
        pass

    @staticmethod
    def SetConfigurationFile(fileName):
        """
        SetConfigurationFile(fileName: str)
            Set configuration file on-fly
        """
        pass

    @staticmethod
    def TryGetValue(key, *__args):
        """
        TryGetValue[T](key: str) -> (bool, T)
        TryGetValue[T](key: str, defaultValue: T) -> (bool, T)
        """
        pass

    @staticmethod
    def Write():
        """
        Write()
            Write the contents of the serialized 
             configuration back to the disk.
        """
        pass

    __all__ = [
        'Flatten',
        'Get',
        'GetBool',
        'GetDouble',
        'GetEnvironment',
        'GetInt',
        'GetToken',
        'GetValue',
        'MergeCommandLineArgumentsWithConfiguration',
        'Reset',
        'Set',
        'SetConfigurationFile',
        'TryGetValue',
        'Write',
    ]


class LeanArgumentParser(object):
    """ Command Line arguments parser for Lean configuration """
    @staticmethod
    def ParseArguments(args):
        """
        ParseArguments(args: Array[str]) -> Dictionary[str, object]
        
            Argument parser contructor
        """
        pass

    __all__ = [
        'ParseArguments',
    ]


class ReportArgumentParser(object):
    """ Command Line arguments parser for Report Creator """
    @staticmethod
    def ParseArguments(args):
        """
        ParseArguments(args: Array[str]) -> Dictionary[str, object]
        
            Parse and construct the args.
        """
        pass

    __all__ = [
        'ParseArguments',
    ]


class ToolboxArgumentParser(object):
    """ Command Line arguments parser for Toolbox configuration """
    @staticmethod
    def ParseArguments(args):
        """
        ParseArguments(args: Array[str]) -> Dictionary[str, object]
        
            Argument parser contructor
        """
        pass

    __all__ = [
        'ParseArguments',
    ]


