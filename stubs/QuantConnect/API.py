# encoding: utf-8
# module QuantConnect.Api calls itself Api
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RestResponse(object):
    """
    Base API response class for the QuantConnect API.
    
    RestResponse()
    """
    Errors = None
    Success = None


class AuthenticationResponse(RestResponse):
    """
    Verify if the credentials are OK.
    
    AuthenticationResponse()
    """

class Backtest(RestResponse):
    """
    Backtest response packet from the QuantConnect.com API.
    
    Backtest()
    """
    BacktestId = None
    Completed = None
    Created = None
    Error = None
    Name = None
    Note = None
    Progress = None
    Result = None
    StackTrace = None


class BacktestList(RestResponse):
    """
    Collection container for a list of backtests for a project
    
    BacktestList()
    """
    Backtests = None


class BacktestReport(RestResponse):
    """
    Backtest Report Response wrapper
    
    BacktestReport()
    """
    Report = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """HTML data of the report with embedded base64 images

Get: Report(self: BacktestReport) -> str

Set: Report(self: BacktestReport) = value
"""



class Compile(RestResponse):
    """
    Response from the compiler on a build event
    
    Compile()
    """
    CompileId = None
    Logs = None
    State = None


class CompileState(Enum, IComparable, IFormattable, IConvertible):
    """
    State of the compilation request
    
    enum CompileState, values: BuildError (2), BuildSuccess (1), InQueue (0)
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

    BuildError = None
    BuildSuccess = None
    InQueue = None
    value__ = None


class Link(RestResponse):
    """
    Response from reading purchased data
    
    Link()
    """
    DataLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Link to the data

Get: DataLink(self: Link) -> str

Set: DataLink(self: Link) = value
"""



class Project(RestResponse):
    """
    Response from reading a project by id.
    
    Project()
    """
    Created = None
    Language = None
    Modified = None
    Name = None
    ProjectId = None


class ProjectFile(object):
    """
    File for a project
    
    ProjectFile()
    """
    DateModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DateTime project file was modified

Get: DateModified(self: ProjectFile) -> DateTime

Set: DateModified(self: ProjectFile) = value
"""


    Code = None
    Name = None


class ProjectFilesResponse(RestResponse):
    """
    Response received when reading all files of a project
    
    ProjectFilesResponse()
    """
    Files = None


class ProjectResponse(RestResponse):
    """
    Project list response
    
    ProjectResponse()
    """
    Projects = None


