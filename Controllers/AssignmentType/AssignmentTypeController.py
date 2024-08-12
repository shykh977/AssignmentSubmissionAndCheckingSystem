from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.AssignmentTypeCores

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

AssignmentType_Controller = Blueprint('AssignmentType', __name__)

cors = Cores.AssignmentTypeCores


@AssignmentType_Controller.route('/CreateAssignmentType',methods=['POST'])
#@token_required
def CreateAssignmentType():   
    params = request.json   
    response =cors.CreateAssignmentType(params)
    return response


@AssignmentType_Controller.route('/GetAssignmentType',methods=['POST'])
#@token_required
def GetAssignmentType():   
    params = request.json   
    return cors.GetAssignmentType(params)


@AssignmentType_Controller.route('/DeleteAssignmentType',methods=['POST'])
#@token_required
def DeleteAssignmentType():   
    params = request.json   
    return cors.DeleteAssignmentType(params)


