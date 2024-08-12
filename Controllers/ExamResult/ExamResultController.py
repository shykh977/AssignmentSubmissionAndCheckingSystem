from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.ExamResultCores
import pip._vendor.requests as requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

ExamResult_Controller = Blueprint('ExamResult', __name__)

cors = Cores.ExamResultCores





@ExamResult_Controller.route('/CreateExamInvite',methods=['POST'])
#@token_required
def CreateExamInvite():   

    return cors.CreateExamInvite(request.json)


@ExamResult_Controller.route('/CreateExamResult',methods=['POST'])
#@token_required
def CreateExamResult():   

    return cors.CreateExamResult(request.json)


@ExamResult_Controller.route('/CreateExamQuestionsResult',methods=['POST'])
#@token_required
def CreateExamQuestionsResult():   

    return cors.CreateExamQuestionsResult(request.json)


@ExamResult_Controller.route('/CreateSelectQuestionOptions',methods=['POST'])
#@token_required
def CreateSelectQuestionOptions():   

    return cors.CreateSelectQuestionOptions(request.json)



@ExamResult_Controller.route('/CreateQuestionOptionsResultLog',methods=['POST'])
#@token_required
def CreateQuestionOptionsResultLog():   

    return cors.CreateQuestionOptionsResultLog(request.json)



@ExamResult_Controller.route('/LoginExam',methods=['POST'])
#@token_required
def LoginExam():   

    return cors.LoginExam(request.json)


@ExamResult_Controller.route('/GetInvitedExam',methods=['POST'])
#@token_required
def GetInvitedExam():   

    return cors.GetInvitedExam(request.json)


@ExamResult_Controller.route('/AcceptExamLogin',methods=['POST'])
#@token_required
def AcceptExamLogin():   

    return cors.AcceptExamLogin(request.json)


@ExamResult_Controller.route('/GetIsAcceptExam',methods=['POST'])
#@token_required
def GetIsAcceptExam():   

    return cors.GetIsAcceptExam(request.json)


@ExamResult_Controller.route('/GetExamResult',methods=['POST'])
#@token_required
def GetExamResult():   

    return cors.GetExamResult(request.json)


@ExamResult_Controller.route('/GetQuestionCount',methods=['POST'])
#@token_required
def GetQuestionCount():   

    return cors.GetQuestionCount(request.json)


@ExamResult_Controller.route('/FinishExam',methods=['POST'])
#@token_required
def FinishExam():   

    return cors.FinishExam(request.json)