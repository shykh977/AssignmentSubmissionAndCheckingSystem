from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.ExamCores

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

Exam_Controller = Blueprint('Exam', __name__)

cors = Cores.ExamCores


@Exam_Controller.route('/CreateExamType',methods=['POST'])
#@token_required
def CreateExamType():   
    params = request.json   
    response =cors.CreateExamType(params)
    return response


@Exam_Controller.route('/CreateExamSlot',methods=['POST'])
#@token_required
def CreateExamSlot():   
    params = request.json   
    response =cors.CreateExamSlot(params)
    return response


@Exam_Controller.route('/CreateExamLocation',methods=['POST'])
#@token_required
def CreateExamLocation():   
    params = request.json   
    response =cors.CreateExamLocation(params)
    return response


@Exam_Controller.route('/CreateExams',methods=['POST'])
#@token_required
def CreateExams():   
    params = request.json   
    response =cors.CreateExams(params)
    return response

@Exam_Controller.route('/CreateExamsQuestions',methods=['POST'])
#@token_required
def CreateExamsQuestions():   
    params = request.json   
    response =cors.CreateExamsQuestions(params)
    return response


@Exam_Controller.route('/CreateQuestionOptions',methods=['POST'])
#@token_required
def CreateQuestionOptions():   
    params = request.json   
    response =cors.CreateQuestionOptions(params)
    return response

############---GET---############


@Exam_Controller.route('/GetExamType',methods=['POST'])
#@token_required
def GetExamType():   
    params = request.json   
    response =cors.GetExamType(params)
    return response


@Exam_Controller.route('/GetExamSlot',methods=['POST'])
#@token_required
def GetExamSlot():   
    params = request.json   
    response =cors.GetExamSlot(params)
    return response


@Exam_Controller.route('/GetExamLocation',methods=['POST'])
#@token_required
def GetExamLocation():   
    params = request.json   
    response =cors.GetExamLocation(params)
    return response


@Exam_Controller.route('/GetExam',methods=['POST'])
#@token_required
def GetExam():   
    params = request.json   
    response =cors.GetExam(params)
    return response


@Exam_Controller.route('/GetExamQuestion',methods=['POST'])
#@token_required
def GetExamQuestion():   
    params = request.json   
    response =cors.GetExamQuestion(params)
    return response

@Exam_Controller.route('/GetQuestionOptions',methods=['POST'])
#@token_required
def GetQuestionOptions():   
    params = request.json   
    response =cors.GetQuestionOptions(params)
    return response

############---Delete---############

@Exam_Controller.route('/DeleteExam',methods=['POST'])
#@token_required
def DeleteExam():   
    params = request.json   
    response =cors.DeleteExam(params)
    return response

@Exam_Controller.route('/DeleteExamSlot',methods=['POST'])
#@token_required
def DeleteExamSlot():   
    params = request.json   
    response =cors.DeleteExamSlot(params)
    return response

@Exam_Controller.route('/DeleteExamLocation',methods=['POST'])
#@token_required
def DeleteExamLocation():   
    params = request.json   
    response =cors.DeleteExamLocation(params)
    return response

@Exam_Controller.route('/DeleteExamType',methods=['POST'])
#@token_required
def DeleteExamType():   
    params = request.json   
    response =cors.DeleteExamType(params)
    return response


@Exam_Controller.route('/DeleteExamsQuestions',methods=['POST'])
#@token_required
def DeleteExamsQuestions():   
    params = request.json   
    response =cors.DeleteExamsQuestions(params)
    return response


@Exam_Controller.route('/DeleteQuestionOptions',methods=['POST'])
#@token_required
def DeleteQuestionOptions():   
    params = request.json   
    response =cors.DeleteQuestionOptions(params)
    return response