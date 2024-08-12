import abc


class iExecuteProc( abc.ABC ):
    @abc.abstractclassmethod
    def Exec_Proc(self,ProcName,Params):
        pass

    @abc.abstractclassmethod
    def Exec_Search(self,ProcName,Params):
        pass


    @abc.abstractclassmethod
    def LoginUser(self,ProcName,Params):
        pass


