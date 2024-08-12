
import datetime
from flask import Blueprint
from flask import Flask ,request,jsonify
from Commons.Constant import Procedures
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
from DataRepository.GenericRepo import GenericRepository
from DataRepository.SendMail import Mailing

import random
import string
import uuid


generic = GenericRepository()
MailService = Mailing


def CreateExamInvite(params):
    
    
    InviteMail = params["InviteMail"]
    ExamsId = params["ExamsId"]
    InstructorId = params["InstructorId"]
    ExamCode =params["ExamCode"]
    Name =params["Name"]
  
   
    for x,y in zip(InviteMail, Name):

        ExamEntryCode =GetExamCode()

        a = { "InviteMail" : x,
              "ExamsId" :ExamsId,
              "InstructorId" :InstructorId,
              "InviteCode" :ExamEntryCode,
              "ExamCode":ExamCode
              }
        
        RegisterCandidate(x,y,ExamsId,ExamCode,ExamEntryCode)
        
       
        
        response = generic.Exec_Proc(Procedures.CreateExamInvite,a)
        #MailService.MailSend("","You Have New Exam ("+ ExamCode +")"," Dear Candidate \n Your Exam Has Been Created Your Exam Login Credentials \nEmail : "+ x +"\n EntryCode:"+ ExamEntryCode +"\n",x)


        #MailService.MailSend("","You Have New Assignemnt",params["AssignmentName"],x)
        
        


    
    return response


def CreateExamResult(params):

    ExamResultId =uuid.uuid4()

   


    obj = {
    "ExamResultId":ExamResultId,
    "EndDate": params["EndDate"],
    "ExamCode": params["ExamCode"],
    "StartDate": params["StartDate"],
    "StudentId": params["StudentId"]
    }

    response = generic.Exec_Proc(Procedures.CreateExamResult,obj)
    return jsonify({"ExamResultId" : ExamResultId})


def CreateExamQuestionsResult(params):

#197

    res = generic.Exec_Search(Procedures.GetExamQuestionsResult,{"ExamQuestionsId": params["ExamQuestionsId"] ,"StudentId":params["StudentId"]})

    ExamQuestionsResultId = uuid.uuid4()
    res2 = res[0]["Response"]
    #res3 = res[0]["Response"][0]["ExamQuestionsResultId"]
   

    if(res2 == []):


        obj = {
            "ExamId" :params["ExamId"],
            "ExamQuestionsId": params["ExamQuestionsId"],
            "ExamQuestionsResultId": ExamQuestionsResultId,
            "ExamResultId": params["ExamResultId"],
            "IsSolved": params["IsSolved"],
            "QuestionType": params["QuestionType"],
            "SkipTime":params["SkipTime"],
            "StudentId": params["StudentId"]
        }


        response = generic.Exec_Proc(Procedures.CreateExamQuestionsResult,obj)
        return jsonify({"ExamQuestionsResultId" : ExamQuestionsResultId})
    
    else:
        obj = {
            "ExamId" :params["ExamId"],
            "ExamQuestionsId": params["ExamQuestionsId"],
            "ExamQuestionsResultId": res[0]["Response"][0]["ExamQuestionsResultId"],
            "ExamResultId": params["ExamResultId"],
            "IsSolved": params["IsSolved"],
            "QuestionType": params["QuestionType"],
            "SkipTime":params["SkipTime"],
            "StudentId": params["StudentId"]
        }


        response = generic.Exec_Proc(Procedures.CreateExamQuestionsResult,obj)
        return jsonify({"ExamQuestionsResultId" : res[0]["Response"][0]["ExamQuestionsResultId"]})


def CreateSelectQuestionOptions(params):

    SelectQuestionOptionsId = uuid.uuid4()

    obj ={
        "SelectQuestionOptionsId":SelectQuestionOptionsId,
        "ExamQuestionsResultId" : params["ExamQuestionsResultId"],
        "Options":params["Options"],
        "IsAnswer":params["IsAnswer"]
    }

    response = generic.Exec_Proc(Procedures.CreateSelectQuestionOptions,params)
    return jsonify({"SelectQuestionOptionsId" : SelectQuestionOptionsId})


def CreateQuestionOptionsResultLog(params):

    response = generic.Exec_Proc(Procedures.CreateQuestionOptionsResultLog,params)
    return response


def AcceptExamLogin(params):

    dattime = datetime.datetime.now()

    obj ={
        "ExamInviteId" : params["ExamInviteId"],
        "StartTime" : dattime
    }

    response = generic.Exec_Proc(Procedures.AcceptExamLogin,params)
    return jsonify({"dattime":dattime})

############Get#################


def LoginExam(params):


    ValidInvite = generic.Exec_Search(Procedures.CheckExamInvite,params)

    res2 = ValidInvite[0]["Response"]

    if(res2 == []):
        return  jsonify({'Invalid Login': "You Are Not Invited Please Contact Your Instructor" })

         
    
    else:
         
        data ={
            "InviteCode"	: params["InviteCode"],
            "ExamCode"	    : params["ExamCode"]

        }


        response = generic.LoginUser(Procedures.LoginExam,data)

        return response
       

    

def GetInvitedExam(params):

    response = generic.Exec_Search(Procedures.GetInvitedExam,params)
    return response


def FinishExam(params):

    response = generic.Exec_Proc(Procedures.FinishExam,params)
    return response


def GetIsAcceptExam(params):

    response = generic.Exec_Search(Procedures.GetIsAcceptExam,params)
    return response

def GetExamResult(params):

    response = generic.Exec_Search(Procedures.GetExamResult,params)
    return response


def GetQuestionCount(params):

    response = generic.Exec_Search(Procedures.GetQuestionCount,params)
    return response

############### UTILL #################
def GetExamCode():
    # Define the pool of characters
    characters = string.ascii_letters + string.digits
    
    # Generate a random 6-character alphanumeric string
    random_string = ''.join(random.choice(characters) for _ in range(6))
    
    return random_string


def RegisterCandidate(Email,Name,ExamId,ExamCode,ExamEntryCode):


    obj ={
        "Email" :Email
    }

    res = generic.Exec_Search(Procedures.SearchStudent,obj)


    
    

   



    res2 = res[0]["Response"]

    Password =GetExamCode()

    if(res2 == []):

        Data ={
            "CourseID":ExamId,
            "CourseCode": ExamCode,
            "Name": Name,
            "Email":Email
        }
        
        UserData ={
            "UserName"	:Email,        	
            "UserPassword" :Password,	
            "UserType":		3
        }
        generic.Exec_Proc(Procedures.CreateStudent,Data)
        generic.Exec_Proc(Procedures.CreateUsers,UserData)


        MailService.MailSend("","You Have New Exam ("+ ExamCode +")"," Dear Candidate \n Your Exam Has Been Created Your Exam Login Credentials \n ExamCode : "+ ExamCode +"\n EntryCode:"+ ExamEntryCode +"\n"+"\n\n Your Portal Login Credentials Is \n\n UserName :"+ Email +"\n\n Password:"+ Password +"",Email)
    else:
        MailService.MailSend("","You Have New Exam ("+ ExamCode +")"," Dear Candidate \n Your Exam Has Been Created Your Exam Login Credentials \n ExamCode : "+ ExamCode +"\n EntryCode:"+ ExamEntryCode +"\n",Email)

    


    # if res.index[0]:
    #     print("Success")

    


    print(res)

