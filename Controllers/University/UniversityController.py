from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.UniversityCores

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

Univesity_Controller = Blueprint('University', __name__)

cors = Cores.UniversityCores


@Univesity_Controller.route('/CreateUniversity',methods=['POST'])
#@token_required
def CreateUniversity():   
    params = request.json   
    response =cors.CreateUniversity(params)
    return response


@Univesity_Controller.route('/GetUniversity',methods=['POST'])
#@token_required
def GetUniversity():   
    params = request.json   
    


    response =cors.GetUniversity(params)
    return response









# @Society_Controller.route("/GetEntry",methods=['POST'])
# def GetEntry():
   
#     params = request.json
   
#     procname = 'usp_LoginUsers' 
#     o1 = ExecuteProc()
#     response = o1.Exec_Search(procname,params)
#     return response

# @Society_Controller.route("/LoginUsers",methods=['POST'])
# def LoginUser():
   
#     params = request.json
   
#     procname = 'usp_LoginUsers' 
#     o1 = UserService()
#     response = o1.LoginUserService(procname,params,app)
#     return response