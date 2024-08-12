import json
from sqlalchemy import bindparam, create_engine,text
from sqlalchemy.orm import sessionmaker
from DataConnectionLayer.DbConfig import DbConfig
from    IDataRepository.IGenericRepo import iExecuteProc
from    Commons.Constant import Procedures  
from flask import jsonify

import pyodbc

from Models.Society import Society

conn = DbConfig()

session =  conn.GetConnection()

#connection_string = 'mssql+pyodbc://sa:BTG12345#@192.168.5.250/WaterJar?driver=ODBC+Driver+17+for+SQL+Server'
# engine = create_engine(connection_string, echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()



class GenericRepository(iExecuteProc):
    def Exec_Proc(self,ProcName,Params):
       
       
       keys =[]
       for key in Params.keys():  
        # x = key.split(',')
        keys.append(key)    
        converted_array = [f"@{item}=:"+item +"" for item in keys]
        converted_string = ", ".join(converted_array)
       ExecCommand = text("EXEC "+ProcName+" "+converted_string)
       print("EXEC "+ProcName+" "+converted_string)
       result = session.execute(ExecCommand, Params)
       session.commit()
       response =""   
       if result.rowcount > 0:
         response = jsonify({'StatusMessage': 'Success'}), 200
       else:        
         response =jsonify({'StatusMessage': ' Request Has Been Decline From Server'}), 500
       return response
    


    # def Exec_Search(self,ProcName,Params):
    #    keys =[]
    #    for key in Params.keys():  
    #     # x = key.split(',')
    #     keys.append(key)    
    #     converted_array = [f":{item}" for item in keys]
    #     converted_string = ", ".join(converted_array)
    #    ExecCommand = text("EXEC "+ProcName+" "+converted_string)
    #   #  ExecCommand = text("EXEC "+ProcName)
    #    bind_params = {f":{param}": value for param, value in Params.items()}

    #    print("ExecCommand:", ExecCommand)
    #    print("bind_params:", bind_params)

    #   #  result = session.execute(ExecCommand, Params)
    #    result = session.execute(ExecCommand, bind_params)
    #    rows = result.fetchall()
    #    data ={}
    #    for items in rows:
    #     data.update(items._mapping)
    #    return  data
    # pass



    def Exec_Search(self,ProcName,Params):
       keys =[]
       for key  in Params:  
        # x = key.split(',')
        keys.append(key)    
        converted_array = [f"@{item}=:"+item +"" for item in keys]
        converted_string = ", ".join(converted_array)
       ExecCommand = text("EXEC "+ProcName+" "+converted_string)
       print("EXEC "+ProcName+" "+converted_string)
       result = session.execute(ExecCommand, Params) 
       rows = result.fetchall()
       data = []
       for items in rows:
        data.append(dict(items._mapping))

       response = ({"Response": data}),200
       return  response
    


    def LoginUser(self,ProcName,Params):
       keys =[]
       for key  in Params:  
        # x = key.split(',')
        keys.append(key)    
        converted_array = [f"@{item}=:"+item +"" for item in keys]
        converted_string = ", ".join(converted_array)
       ExecCommand = text("EXEC "+ProcName+" "+converted_string)
       print("EXEC "+ProcName+" "+converted_string)
       result = session.execute(ExecCommand, Params) 
       rows = result.fetchall()
       data = []
       for items in rows:
        data.append(dict(items._mapping))


       if data ==[]:
         response = ({"Response": "Invalid Login Data"}),401
       else:
         response = ({"Response": data}),200
         
    
       return  response
    








    # def Exec_Search(self, ProcName, Params):
    #   param_names = list(Params.keys())  # Get the parameter names from Params dictionary
    #   converted_array = [bindparam(param, value=Params[param]) for param in param_names]
    #   ExecCommand = text("EXEC " + ProcName + " " + ", ".join(converted_array))
      
    #   # Execute the command
    #   result = session.execute(ExecCommand)
      
    #   rows = result.fetchall()
    #   data = {}
    #   for items in rows:
    #       data.update(items._mapping)
    #   return data







# o1 = ExecuteProc()

# o1.Exec_Proc()