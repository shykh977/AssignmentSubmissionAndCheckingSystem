from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.StudentCores

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

Student_Controller = Blueprint('Student', __name__)

cors = Cores.StudentCores


@Student_Controller.route('/CreateStudent',methods=['POST'])
#@token_required
def CreateStudent():   
    params = request.json   
    response =cors.CreateStudent(params)
    return response


@Student_Controller.route('/GetStudent',methods=['POST'])
#@token_required
def GetStudent():   
    params = request.json   
    return cors.GetStudent(params)


@Student_Controller.route('/DeleteStudent',methods=['POST'])
#@token_required
def DeleteStudent():   
    params = request.json   
    return cors.DeleteStudent(params)


