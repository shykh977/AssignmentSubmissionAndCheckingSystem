import datetime
import json
import jwt
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from DataConnectionLayer.DbConfig import DbConfig
from    IDataRepository.IGenericRepo import iExecuteProc
from    Commons.Constant import Procedures  
from flask import jsonify

import pyodbc

from IDataRepository.IUserService import IuserService


conn = DbConfig()

session =  conn.GetConnection()



class UserService(IuserService):
   
    def LoginUserService(self,ProcName,Params,app):
       keys =[]
       for key in Params.keys():  
        # x = key.split(',')
        keys.append(key)    
        converted_array = [f":{item}" for item in keys]
        converted_string = ", ".join(converted_array)
       ExecCommand = text("EXEC "+ProcName+" "+converted_string)
       result = session.execute(ExecCommand, Params)
       
      
       
      

       if result.rowcount != 0:
        # Create a JWT token and return it to the client
        rows = result.fetchone()
        token = jwt.encode({'UserName': rows._data[0], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})
       
       else:
         
        return jsonify({'message': 'Invalid credentials'}), 401

    #    token = jwt.encode({'UserName': rows._data[1], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
    #    return jsonify({'token': token.decode('UTF-8')})
       
    pass