
from flask import Blueprint
from flask import Flask ,request,jsonify
from Commons.Constant import Procedures
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
from DataRepository.GenericRepo import GenericRepository
import uuid


generic = GenericRepository()

def CreateExamType(params):

    response = generic.Exec_Proc(Procedures.CreateExamType,params)
    return response

def CreateExamSlot(params):

    response = generic.Exec_Proc(Procedures.CreateExamSlot,params)
    return response

def CreateExamLocation(params):

    response = generic.Exec_Proc(Procedures.CreateExamLocation,params)
    return response

def CreateExams(params):

    response = generic.Exec_Proc(Procedures.CreateExams,params)
    return response

def CreateExamsQuestions(params):


    ExamQuestionsId = uuid.uuid4()
    params["ExamQuestionsId"] =ExamQuestionsId

    response = generic.Exec_Proc(Procedures.CreateExamsQuestions,params)
    return jsonify({"ExamQuestionsId": ExamQuestionsId})

def CreateQuestionOptions(params):

    response = generic.Exec_Proc(Procedures.CreateQuestionOptions,params)
    return response


############Get#################

def GetExamType(params):

    response = generic.Exec_Search(Procedures.GetExamType,params)
    return response

def GetExamSlot(params):

    response = generic.Exec_Search(Procedures.GetExamSlot,params)
    return response

def GetExamLocation(params):

    response = generic.Exec_Search(Procedures.GetExamLocation,params)
    return response

def GetExam(params):

    response = generic.Exec_Search(Procedures.GetExam,params)
    return response


def GetExamQuestion(params):

    response = generic.Exec_Search(Procedures.GetExamQuestion,params)
    return response

def GetQuestionOptions(params):

    response = generic.Exec_Search(Procedures.GetQuestionOptions,params)
    return response

#########Delete#########
def DeleteExamType(params):

    response = generic.Exec_Proc(Procedures.DeleteExamType,params)
    return response

def DeleteExamSlot(params):

    response = generic.Exec_Proc(Procedures.DeleteExamSlot,params)
    return response

def DeleteExamLocation(params):

    response = generic.Exec_Proc(Procedures.DeleteExamLocation,params)
    return response

def DeleteExam(params):

    response = generic.Exec_Proc(Procedures.DeleteExam,params)
    return response

def DeleteExamsQuestions(params):

    response = generic.Exec_Proc(Procedures.DeleteExamsQuestions,params)
    return response

def DeleteQuestionOptions(params):

    response = generic.Exec_Proc(Procedures.DeleteQuestionOptions,params)
    return response