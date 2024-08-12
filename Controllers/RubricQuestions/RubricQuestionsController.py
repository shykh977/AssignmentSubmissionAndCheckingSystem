from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.RubricQuestionsCores

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

RubricQuestions_Controller = Blueprint('RubricQuestions', __name__)

cors = Cores.RubricQuestionsCores


@RubricQuestions_Controller.route('/CreateRubricQuestions',methods=['POST'])
#@token_required
def CreateRubricQuestions():   
    params = request.json   
    response =cors.CreateRubricQuestions(params)
    return response



@RubricQuestions_Controller.route('/QuestionResultCheck',methods=['POST'])
#@token_required
def QuestionResultCheck():   
    params = request.json   
    response =cors.QuestionResultCheck(params)
    return response



@RubricQuestions_Controller.route('/CreateRubricQuestionsResult',methods=['POST'])
#@token_required
def CreateRubricQuestionsResult():   
   
    response =cors.CreateRubricQuestionsResult(request)
    return response




@RubricQuestions_Controller.route('/GetRubricQuestion',methods=['POST'])
#@token_required
def GetRubricQuestion():   
    params = request.json   
    return cors.GetRubricQuestion(params)



@RubricQuestions_Controller.route('/GetRubricQuestionResult',methods=['POST'])
#@token_required
def GetRubricQuestionResult():   
    params = request.json   
    return cors.GetRubricQuestionResult(params)



@RubricQuestions_Controller.route('/DeleteRubricQuestions',methods=['POST'])
#@token_required
def DeleteRubricQuestions():   
    params = request.json   
    response =cors.DeleteRubricQuestions(params)
    return response
