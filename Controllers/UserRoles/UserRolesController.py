from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.UserRoles

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

UserRoles_Controller = Blueprint('UserRoles', __name__)

cors = Cores.UserRoles


@UserRoles_Controller.route('/CreateUserRoles',methods=['POST'])
#@token_required
def CreateUserRoles():   
    params = request.json   
    response =cors.CreateUserRoles(params)
    return response


@UserRoles_Controller.route('/GetUserRoles',methods=['POST'])
#@token_required
def GetUserRoles():   
    params = request.json   

    return cors.GetUserRoles(params)


