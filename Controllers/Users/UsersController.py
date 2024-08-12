from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.Users

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

Users_Controller = Blueprint('Users', __name__)

cors = Cores.Users


@Users_Controller.route('/CreateUsers',methods=['POST'])
#@token_required
def CreateUsers():   
    params = request.json   
    response =cors.CreateUsers(params)
    return response


@Users_Controller.route('/LoginUser',methods=['POST'])
#@token_required
def LoginUser():   
    params = request.json   
    response =cors.LoginUser(params)
    return response


@Users_Controller.route('/GetRecentlyJoinUsers',methods=['POST'])
#@token_required
def GetRecentlyJoinUsers():   
    params = request.json   
    response =cors.GetRecentlyJoinUsers(params)
    return response

@Users_Controller.route('/UpdatePassword',methods=['POST'])
#@token_required
def UpdatePassword():   
    params = request.json   
    response =cors.UpdatePassword(params)
    return response


# @Univesity_Controller.route('/GetUniversity',methods=['POST'])
# #@token_required
# def GetUniversity():   
#     params = request.json   
#     response =cors.GetUniversity(params)
#     return response

