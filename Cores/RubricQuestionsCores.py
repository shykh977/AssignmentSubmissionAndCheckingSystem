
import os
from flask import Blueprint
from flask import Flask ,request,jsonify
from Commons.Constant import Procedures
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
from DataRepository.GenericRepo import GenericRepository
import uuid


generic = GenericRepository()


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def CreateRubricQuestions(params):



    QuestioniD = uuid.uuid4()

    params["QuestioniD"] = QuestioniD


    response = generic.Exec_Proc(Procedures.CreateRubricQuestions,params)
    return  jsonify({'QuestioniD': QuestioniD})



def QuestionResultCheck(params):

   
    response = generic.Exec_Proc(Procedures.CreateRubricQuestionsResult,params)
    return  response



def CreateRubricQuestionsResult(request):


    # file =request.files.getlist('PDF')

    # FilePath =""

    # pdf_target = os.path.join(APP_ROOT, '../static/pdf_image')

    # QuestioniD=request.form['QuestioniD']

    # for file in request.files.getlist('File'):
    #     filename = file.filename
    #     var3 = "".join([str(QuestioniD),filename])
    #     destination = "/".join([pdf_target,var3])

    #     FilePath = destination

    #     file.save(destination)


    

    obj ={

        "QuestioniD" :request.form['QuestioniD'],
        "StudentId" :request.form['StudentId'],
        "RubricID" :request.form['RubricID'],
        "Title" :request.form['Title'],
        "AnswerPageNo" :request.form['AnswerPageNo'],
        "ImagePath" :request.form['ImagePath'],
        "IsSubmitted" :1
        }

    response = generic.Exec_Proc(Procedures.CreateRubricQuestionsResult,obj)




    return response


def GetRubricQuestion(params):

    response = generic.Exec_Search(Procedures.GetRubricQuestion,params)
    return response


def GetRubricQuestionResult(params):

    response = generic.Exec_Search(Procedures.GetRubricQuestionResult,params)
    return response



def DeleteRubricQuestions(params):

    response = generic.Exec_Proc(Procedures.DeleteRubricQuestions,params)
    return response