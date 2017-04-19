from abc import ABCMeta, abstractmethod, abstractproperty

class Chip:


    __metaclass__ = ABCMeta

    @abstractmethod
    def Action(self): pass

    @property
    @abstractmethod
    def name(self):
        # Name property will be provided by the inheriting class
        # This will mostly be used for debugging
        pass
