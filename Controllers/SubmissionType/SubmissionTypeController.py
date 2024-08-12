from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.SubmissionTypeCores

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

SubmissionType_Controller = Blueprint('SubmissionType', __name__)

cors = Cores.SubmissionTypeCores


@SubmissionType_Controller.route('/CreateSubmissionType',methods=['POST'])
#@token_required
def CreateSubmissionType():   
    params = request.json   
    response =cors.CreateSubmissionType(params)
    return response


@SubmissionType_Controller.route('/GetSubmissionType',methods=['POST'])
#@token_required
def GetSubmissionType():   
    params = request.json   
    return cors.GetSubmissionType(params)


@SubmissionType_Controller.route('/GetTerm',methods=['POST'])
#@token_required
def GetTerm():   
    params = request.json   
    return cors.GetTerm(params)



@SubmissionType_Controller.route('/DeleteSubmissionType',methods=['POST'])
#@token_required
def DeleteSubmissionType():   
    params = request.json   
    return cors.DeleteSubmissionType(params)


