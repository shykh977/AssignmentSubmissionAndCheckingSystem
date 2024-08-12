from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.Faculty

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

Faculty_Controller = Blueprint('Faculty', __name__)

cors = Cores.Faculty


@Faculty_Controller.route('/CreateFaculty',methods=['POST'])
#@token_required
def CreateFaculty():   
    params = request.json   
    response =cors.CreateFaculty(params)
    return response


@Faculty_Controller.route('/GetFaculty',methods=['POST'])
#@token_required
def GetFaculty():   
    params = request.json    
    return cors.GetFaculty(params)

