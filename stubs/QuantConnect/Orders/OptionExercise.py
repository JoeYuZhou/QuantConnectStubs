# encoding: utf-8
# module QuantConnect.Orders.OptionExercise calls itself OptionExercise
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DefaultExerciseModel(object, IOptionExerciseModel):
    """
    Represents the default option exercise model (physical, cash settlement)
    
    DefaultExerciseModel()
    """
    def OptionExercise(self, option, order):
        """
        OptionExercise(self: DefaultExerciseModel, option: Option, order: OptionExerciseOrder) -> IEnumerable[OrderEvent]
        
            Default option exercise model for the basic 
             equity/index option security class.
        
        
            option: Option we're trading this order
            order: Order to update
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class IOptionExerciseModel:
    """ Represents a model that simulates option exercise and lapse events """
    def OptionExercise(self, option, order):
        """
        OptionExercise(self: IOptionExerciseModel, option: Option, order: OptionExerciseOrder) -> IEnumerable[OrderEvent]
        
            Model the option exercise
        
            option: Option we're trading this order
            order: Order to update
            Returns: Order fill information detailing the average 
             price and quantity filled.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


