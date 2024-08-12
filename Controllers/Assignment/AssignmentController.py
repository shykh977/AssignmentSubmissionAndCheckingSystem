from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.AssignmentCores
import pip._vendor.requests as requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

Assignment_Controller = Blueprint('Assignment', __name__)

cors = Cores.AssignmentCores


api_endpoint = 'https://api.gptzero.me/v2/predict/files'

api_key = 'YOUR_API_KEY'




@Assignment_Controller.route('/BTG_Ai_Detector',methods=['POST'])
#@token_required
def predict():   


    pdf_file = request.files['File']


    headers = {
    'accept': 'application/json',
    'X-Api-Key': '5be2160ca87c4424bd8d9893ba3ee5aa',
}
    files = {'files': (pdf_file.filename, pdf_file.stream, pdf_file.content_type)}
    response = requests.post(api_endpoint, files=files, headers=headers)


    
    return response.json()


@Assignment_Controller.route('/CreateAssignmentNew',methods=['POST'])
#@token_required
def CreateAssignmentNew():   
    #params = request.form
    #file = request.files
    response =cors.CreateAssignmentNew(request)
    return response


@Assignment_Controller.route('/CreateStdAssignmentSubmission',methods=['POST'])
#@token_required
def CreateStdAssignmentSubmission():   
    #params = request.form
    #file = request.files
    response =cors.CreateStdAssignmentSubmission(request)
    return response


@Assignment_Controller.route('/GetStdAssignmentSubmission',methods=['POST'])
#@token_required
def GetStdAssignmentSubmission():   
  
    response =cors.GetStdAssignmentSubmission(request.json)
    return response





@Assignment_Controller.route('/CreateAssignment',methods=['POST'])
#@token_required
def CreateAssignment():   
    params = request.json   
    response =cors.CreateAssignment(params)
    return response


@Assignment_Controller.route('/GetAssignment',methods=['POST'])
#@token_required
def GetAssignment():   
    params = request.json   
    return cors.GetAssignment(params)

@Assignment_Controller.route('/DeleteAssignment',methods=['POST'])
#@token_required
def DeleteAssignment():   
    params = request.json   
    return cors.DeleteAssignment(params)


@Assignment_Controller.route('/GetAssignmentFromInstructor',methods=['POST'])
#@token_required
def GetAssignmentFromInstructor():   
    params = request.json   
    return cors.GetAssignmentFromInstructor(params)

@Assignment_Controller.route('/GetAssignmetForInvitedStudent',methods=['POST'])
#@token_required
def GetAssignmetForInvitedStudent():   
    params = request.json   
    return cors.GetAssignmetForInvitedStudent(params)


@Assignment_Controller.route('/GetInvitedStudentByAssignment',methods=['POST'])
#@token_required
def GetInvitedStudentByAssignment():   
    params = request.json   
    return cors.GetInvitedStudentByAssignment(params)


@Assignment_Controller.route('/GetInvitedStudents',methods=['POST'])
#@token_required
def GetInvitedStudents():   
    params = request.json   
    return cors.GetInvitedStudents(params)


@Assignment_Controller.route('/GetAssignemntResult',methods=['POST'])
def GetAssignemntResult():   
    params = request.json   
    return cors.GetAssignemntResult(params)







@Assignment_Controller.route('/CreateAssignmentInvites',methods=['POST'])
#@token_required
def CreateAssignmentInvites():   
    params = request.json   
    return cors.CreateAssignmentInvites(params)



@Assignment_Controller.route('/CreateRequestRegrade',methods=['POST'])
#@token_required
def CreateRequestRegrade():   
    params = request.json   
    return cors.CreateRequestRegrade(params)


@Assignment_Controller.route('/GetAssignmentSelection',methods=['POST'])
#@token_required
def GetAssignmentSelection():   
    params = request.json   
    return cors.GetAssignmentSelection(params)



@Assignment_Controller.route('/GetAssignmentStatus',methods=['POST'])
#@token_required
def GetAssignmentStatus():   
    params = request.json   
    return cors.GetAssignmentStatus(params)



@Assignment_Controller.route('/CreateAiDetector',methods=['POST'])
#@token_required
def CreateAiDetector():   
    params = request.json   
    return cors.CreateAiDetector(params)



@Assignment_Controller.route('/AcceptAssignmentInvites',methods=['POST'])
#@token_required
def AcceptAssignmentInvites():   
    params = request.json   
    return cors.AcceptAssignmentInvites(params)