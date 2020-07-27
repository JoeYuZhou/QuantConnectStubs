# encoding: utf-8
# module QuantConnect.Orders.Slippage calls itself Slippage
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AlphaStreamsSlippageModel(object, ISlippageModel):
    """
    Represents a slippage model that uses a constant percentage of slip
    
    AlphaStreamsSlippageModel()
    """
    def GetSlippageApproximation(self, asset, order):
        """
        GetSlippageApproximation(self: AlphaStreamsSlippageModel, asset: Security, order: Order) -> Decimal
        
            Return a decimal cash slippage approximation on 
             the order.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ConstantSlippageModel(object, ISlippageModel):
    """
    Represents a slippage model that uses a constant percentage of slip
    
    ConstantSlippageModel(slippagePercent: Decimal)
    """
    def GetSlippageApproximation(self, asset, order):
        """
        GetSlippageApproximation(self: ConstantSlippageModel, asset: Security, order: Order) -> Decimal
        
            Slippage Model. Return a decimal cash slippage 
             approximation on the order.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, slippagePercent):
        """ __new__(cls: type, slippagePercent: Decimal) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ISlippageModel:
    """ Represents a model that simulates market order slippage """
    def GetSlippageApproximation(self, asset, order):
        """
        GetSlippageApproximation(self: ISlippageModel, asset: Security, order: Order) -> Decimal
        
            Slippage Model. Return a decimal cash slippage 
             approximation on the order.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class VolumeShareSlippageModel(object, ISlippageModel):
    """
    Represents a slippage model that is calculated by multiplying the price impact constant
                by the square of the ratio of the order to the total volume.
    
    VolumeShareSlippageModel(volumeLimit: Decimal, priceImpact: Decimal)
    """
    def GetSlippageApproximation(self, asset, order):
        """
        GetSlippageApproximation(self: VolumeShareSlippageModel, asset: Security, order: Order) -> Decimal
        
            Slippage Model. Return a decimal cash slippage 
             approximation on the order.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, volumeLimit, priceImpact):
        """ __new__(cls: type, volumeLimit: Decimal, priceImpact: Decimal) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


