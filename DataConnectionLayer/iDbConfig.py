import abc


class IConnection( abc.ABC ):
    @abc.abstractclassmethod
    def GetConnection():
        pass