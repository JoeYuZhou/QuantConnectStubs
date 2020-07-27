# encoding: utf-8
# module QuantConnect.Notifications calls itself Notifications
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Notification(object):
    """ Local/desktop implementation of messaging system for Lean Engine. """
    def Send(self):
        """
        Send(self: Notification)
            Method for sending implementations of 
             notification object types.
        """
        pass


class NotificationEmail(Notification):
    """
    Email notification data.
    
    NotificationEmail(address: str, subject: str, message: str, data: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, address, subject, message, data):
        """ __new__(cls: type, address: str, subject: str, message: str, data: str) """
        pass

    Address = None
    Data = None
    Message = None
    Subject = None


class NotificationManager(object):
    """
    Local/desktop implementation of messaging system for Lean Engine.
    
    NotificationManager(liveMode: bool)
    """
    def Email(self, address, subject, message, data):
        """
        Email(self: NotificationManager, address: str, subject: str, message: str, data: str) -> bool
        
            Send an email to the address specified for live 
             trading notifications.
        
        
            address: Email address to send to
            subject: Subject of the email
            message: Message body, up to 10kb
            data: Data attachment (optional)
        """
        pass

    def Sms(self, phoneNumber, message):
        """
        Sms(self: NotificationManager, phoneNumber: str, message: str) -> bool
        
            Send an SMS to the phone number specified
        
            phoneNumber: Phone number to send to
            message: Message to send
        """
        pass

    def Web(self, address, data):
        """
        Web(self: NotificationManager, address: str, data: object) -> bool
        
            Place REST POST call to the specified address 
             with the specified DATA.
        
        
            address: Endpoint address
            data: Data to send in body JSON encoded (optional)
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, liveMode):
        """ __new__(cls: type, liveMode: bool) """
        pass

    Messages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Public access to the messages

Get: Messages(self: NotificationManager) -> ConcurrentQueue[Notification]

Set: Messages(self: NotificationManager) = value
"""



class NotificationSms(Notification):
    """
    Sms Notification Class
    
    NotificationSms(number: str, message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, number, message):
        """ __new__(cls: type, number: str, message: str) """
        pass

    Message = None
    PhoneNumber = None


class NotificationWeb(Notification):
    """
    Web Notification Class
    
    NotificationWeb(address: str, data: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, address, data):
        """ __new__(cls: type, address: str, data: object) """
        pass

    Address = None
    Data = None


