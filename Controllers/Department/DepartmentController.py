from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.DepartmentCores

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

Department_Controller = Blueprint('Department', __name__)

cors = Cores.DepartmentCores


@Department_Controller.route('/CreateDepartment',methods=['POST'])
#@token_required
def CreateUpdateDepartment():   
    params = request.json   
    response =cors.CreateUpdateDepartment(params)
    return response


@Department_Controller.route('/GetDepartment',methods=['POST'])
#@token_required
def GetDepartment():   
    params = request.json   
    return cors.GetDepartment(params)


