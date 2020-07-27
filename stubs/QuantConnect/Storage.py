# encoding: utf-8
# module QuantConnect.Storage calls itself Storage
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ObjectStore(object, IObjectStore, IDisposable, IEnumerable[KeyValuePair[str, Array[Byte]]], IEnumerable):
    """
    Helper class for easier access to QuantConnect.Interfaces.IObjectStore methods
    
    ObjectStore(store: IObjectStore)
    """
    def ContainsKey(self, key):
        """
        ContainsKey(self: ObjectStore, key: str) -> bool
        
            Determines whether the store contains data for 
             the specified key
        
        
            key: The object key
            Returns: True if the key was found
        """
        pass

    def Delete(self, key):
        """
        Delete(self: ObjectStore, key: str) -> bool
        
            Deletes the object data for the specified key
        
            key: The object key
            Returns: True if the delete operation was successful
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ObjectStore)
            Performs application-defined tasks associated 
             with freeing, releasing, or resetting unmanaged 
             resources.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ObjectStore) -> IEnumerator[KeyValuePair[str, Array[Byte]]]
        
            Returns an enumerator that iterates through the 
             collection.
        
            Returns: A System.Collections.Generic.IEnumerator that can 
             be used to iterate through the collection.
        """
        pass

    def GetFilePath(self, key):
        """
        GetFilePath(self: ObjectStore, key: str) -> str
        
            Returns the file path for the specified key
        
            key: The object key
            Returns: The path for the file
        """
        pass

    def Initialize(self, algorithmName, userId, projectId, userToken, controls):
        """
        Initialize(self: ObjectStore, algorithmName: str, userId: int, projectId: int, userToken: str, controls: Controls)
            Initializes the object store
        
            algorithmName: The algorithm name
            userId: The user id
            projectId: The project id
            userToken: The user token
            controls: The job controls instance
        """
        pass

    def Read(self, key, encoding):
        """
        Read(self: ObjectStore, key: str, encoding: Encoding) -> str
        
            Returns the string object data for the specified 
             key
        
        
            key: The object key
            encoding: The string encoding used
            Returns: A string containing the data
        """
        pass

    def ReadBytes(self, key):
        """
        ReadBytes(self: ObjectStore, key: str) -> Array[Byte]
        
            Returns the object data for the specified key
        
            key: The object key
            Returns: A byte array containing the data
        """
        pass

    def ReadJson(self, key, encoding, settings):
        """ ReadJson[T](self: ObjectStore, key: str, encoding: Encoding, settings: JsonSerializerSettings) -> T """
        pass

    def ReadString(self, key, encoding):
        """
        ReadString(self: ObjectStore, key: str, encoding: Encoding) -> str
        
            Returns the string object data for the specified 
             key
        
        
            key: The object key
            encoding: The string encoding used
            Returns: A string containing the data
        """
        pass

    def ReadXml(self, key, encoding):
        """ ReadXml[T](self: ObjectStore, key: str, encoding: Encoding) -> T """
        pass

    def Save(self, key, text, encoding):
        """
        Save(self: ObjectStore, key: str, text: str, encoding: Encoding) -> bool
        
            Saves the object data in text format for the 
             specified key
        
        
            key: The object key
            text: The string object to be saved
            encoding: The string encoding used
            Returns: True if the object was saved successfully
        """
        pass

    def SaveBytes(self, key, contents):
        """
        SaveBytes(self: ObjectStore, key: str, contents: Array[Byte]) -> bool
        
            Saves the object data for the specified key
        
            key: The object key
            contents: The object data
            Returns: True if the save operation was successful
        """
        pass

    def SaveJson(self, key, obj, encoding, settings):
        """ SaveJson[T](self: ObjectStore, key: str, obj: T, encoding: Encoding, settings: JsonSerializerSettings) -> bool """
        pass

    def SaveString(self, key, text, encoding):
        """
        SaveString(self: ObjectStore, key: str, text: str, encoding: Encoding) -> bool
        
            Saves the object data in text format for the 
             specified key
        
        
            key: The object key
            text: The string object to be saved
            encoding: The string encoding used
            Returns: True if the object was saved successfully
        """
        pass

    def SaveXml(self, key, obj, encoding):
        """ SaveXml[T](self: ObjectStore, key: str, obj: T, encoding: Encoding) -> bool """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[str, Array[Byte]]](enumerable: IEnumerable[KeyValuePair[str, Array[Byte]]], value: KeyValuePair[str, Array[Byte]]) -> bool """
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

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, store):
        """ __new__(cls: type, store: IObjectStore) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ErrorRaised = None


