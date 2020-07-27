# encoding: utf-8
# module QuantConnect.Algorithm.Framework calls itself Framework
# from QuantConnect.Algorithm.Framework, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class NotifiedSecurityChanges(object):
    """ Provides convenience methods for updating collections in responses to securities changed events """
    @staticmethod
    def Update(changes, add, remove):
        """ Update(changes: SecurityChanges, add: Action[Security], remove: Action[Security]) """
        pass

    @staticmethod
    def UpdateCollection(securities, changes, valueFactory=None):
        """ UpdateCollection(securities: ICollection[Security], changes: SecurityChanges)UpdateCollection[TValue](securities: ICollection[TValue], changes: SecurityChanges, valueFactory: Func[Security, TValue]) """
        pass

    @staticmethod
    def UpdateDictionary(dictionary, changes, *__args):
        """ UpdateDictionary[TValue](dictionary: IDictionary[Security, TValue], changes: SecurityChanges, valueFactory: Func[Security, TValue])UpdateDictionary[TValue](dictionary: IDictionary[Symbol, TValue], changes: SecurityChanges, valueFactory: Func[Security, TValue])UpdateDictionary[(TKey, TValue)](dictionary: IDictionary[TKey, TValue], changes: SecurityChanges, keyFactory: Func[Security, TKey], valueFactory: Func[Security, TValue]) """
        pass

    __all__ = [
        'Update',
        'UpdateCollection',
        'UpdateDictionary',
    ]


# variables with complex values

