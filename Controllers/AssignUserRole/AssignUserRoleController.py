from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.AssignUserRole

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

AssignUserRole_Controller = Blueprint('AssignUserRole', __name__)

cors = Cores.AssignUserRole


@AssignUserRole_Controller.route('/CreateAssignUserRole',methods=['POST'])
#@token_required
def CreateAssignUserRole():   
    params = request.json   
    response =cors.CreateAssignUserRole(params)
    return response


@AssignUserRole_Controller.route('/GetAssignedUserRole',methods=['POST'])
#@token_required
def GetAssignedUserRole():   
    params = request.json   
    return cors.GetAssignedUserRole(params)
