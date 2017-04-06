from abc import ABCMeta, abstractmethod

class DataPresenter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def format(self, data): raise NotImplementedError

    @abstractmethod
    def get_header(self): raise NotImplementedError