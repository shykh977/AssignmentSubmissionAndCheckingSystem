from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.RubricSubQuestionsCores

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

RubricSubQuestions_Controller = Blueprint('RubricSubQuestions', __name__)

cors = Cores.RubricSubQuestionsCores


@RubricSubQuestions_Controller.route('/CreateRubricSubQuestions',methods=['POST'])
#@token_required
def CreateRubricSubQuestions():   
    params = request.json   
    response =cors.CreateRubricSubQuestions(params)
    return response


@RubricSubQuestions_Controller.route('/CreateRubricSubQuestionsResult',methods=['POST'])
#@token_required
def CreateRubricSubQuestionsResult():   
    response =cors.CreateRubricSubQuestionsResult(request)
    return response

@RubricSubQuestions_Controller.route('/SubQuestionResultCheck',methods=['POST'])
#@token_required
def SubQuestionResultCheck():   
    params = request.json   
    response =cors.SubQuestionResultCheck(params)
    return response


@RubricSubQuestions_Controller.route('/GetRubricSubQuestions',methods=['POST'])
#@token_required
def GetRubricSubQuestions():   
    params = request.json   
    return cors.GetRubricSubQuestions(params)



@RubricSubQuestions_Controller.route('/GetRubricSubQuestionsResult',methods=['POST'])
#@token_required
def GetRubricSubQuestionsResult():   
    params = request.json   
    return cors.GetRubricSubQuestionsResult(params)



@RubricSubQuestions_Controller.route('/DeleteRubricSubQuestions',methods=['POST'])
#@token_required
def DeleteRubricSubQuestions():   
    params = request.json   
    return cors.DeleteRubricSubQuestions(params)

