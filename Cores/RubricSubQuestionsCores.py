
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
def CreateRubricSubQuestions(params):



    SubQuestionID = uuid.uuid4()

    params["SubQuestionID"] = SubQuestionID

    response = generic.Exec_Proc(Procedures.CreateRubricSubQuestions,params)
    return  jsonify({'SubQuestionID': SubQuestionID})



def SubQuestionResultCheck(params):

    response = generic.Exec_Proc(Procedures.CreateRubricSubQuestionsResult,params)
    return  response




def CreateRubricSubQuestionsResult(request):



    # file =request.files.getlist('PDF')

    # FilePath =""

    # pdf_target = os.path.join(APP_ROOT, '../static/pdf_image')

    # SubQuestionID=request.form['SubQuestionID']

    # for file in request.files.getlist('File'):
    #     filename = file.filename
    #     var3 = "".join([str(SubQuestionID),filename])
    #     destination = "/".join([pdf_target,var3])

    #     FilePath = destination

    #     file.save(destination)



    obj = {
        "SubQuestionID":request.form['SubQuestionID'],
        "StudentId":request.form['StudentId'],
        "QuestionID":request.form['QuestionID'],
        "Title":request.form['Title'],
        "AnswerPageNo":request.form['Title'],
        "ImagePath" :request.form['ImagePath'],
        "IsSubmitted" :1
        }


    response = generic.Exec_Proc(Procedures.CreateRubricSubQuestionsResult,obj)
    return response



def GetRubricSubQuestions(params):

    response = generic.Exec_Search(Procedures.GetRubricSubQuestions,params)
    return response


def GetRubricSubQuestionsResult(params):

    response = generic.Exec_Search(Procedures.GetRubricSubQuestionsResult,params)
    return response


def DeleteRubricSubQuestions(params):

    response = generic.Exec_Proc(Procedures.DeleteRubricSubQuestions,params)
    return response