from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.RubricCores

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

RubricCores_Controller = Blueprint('RubricCores', __name__)

cors = Cores.RubricCores


@RubricCores_Controller.route('/CreateRubric',methods=['POST'])
#@token_required
def CreateRubric():   
    params = request.json   
    response =cors.CreateRubric(params)
    return response


@RubricCores_Controller.route('/CreateRubricResult',methods=['POST'])
#@token_required
def CreateRubricResult():   
    # params = request.json   
    response =cors.CreateRubricResult(request)
    return response



@RubricCores_Controller.route('/GetRubric',methods=['POST'])
#@token_required
def GetRubric():   
    params = request.json   
    return cors.GetRubric(params)

@RubricCores_Controller.route('/DeleteRubric',methods=['POST'])
#@token_required
def DeleteRubric():   
    params = request.json   
    return cors.DeleteRubric(params)


