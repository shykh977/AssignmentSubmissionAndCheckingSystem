
import json
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
import os
import pip._vendor.requests as requests

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

generic = GenericRepository()
MailService = Mailing





def CreateAssignmentNew(request):

    #res =request.form['AssignmentName']
    file =request.files['File']

    api_endpoint ="http://192.168.5.250:7868/api/Uploader/UploadAssignment"

    #api_endpoint ="https://localhost:7180/api/Uploader/UploadAssignment"


    

    headers = {
    'accept': 'multipart/form-data',
    #'X-Api-Key': '5be2160ca87c4424bd8d9893ba3ee5aa',
    }
    Newfiles = {'File': (file.filename, file.stream, file.content_type)}
    response = requests.post(api_endpoint, files=Newfiles, headers=headers)


    path =response.text

    data = json.loads(path)

    url = data['Response']

    

    FilePath =url

    AssignmentID = uuid.uuid4()
    # pdf_target = os.path.join(APP_ROOT, '../static/pdf')

    

    # for file in request.files.getlist('File'):
    #     filename = file.filename
    #     var3 = "".join([str(AssignmentID),filename])
    #     destination = "/".join([pdf_target,var3])

    #     FilePath = destination

    #     file.save(destination)


    Obj ={
      "CourseID": request.form['CourseID'],
      "AssignmentTypeID": request.form['AssignmentTypeID'],
      "AssignmentName": request.form['AssignmentName'],
      "FileExt": request.form['FileExt'],
      "SubmitTypeID": request.form['SubmitTypeID'],
      "ReleaseDate": request.form['ReleaseDate'],
      "DueDate": request.form['DueDate'],
      "IsLateSubmition": int(request.form['IsLateSubmition']),
      "LateDueDate": request.form['LateDueDate'],
      "IsGroupSubmission": int(request.form['IsGroupSubmission']),
      "LimitGroupSize": request.form['LimitGroupSize'],
      "IsApproved": int(request.form['IsApproved']) ,
      "EntryDate": request.form['EntryDate'],
      "DepatmentId":request.form['DepartmentID'],
      "AssignmentID" : AssignmentID,
      "FilePath" :FilePath,
      "IsAiDetector" :int(request.form['IsAiDetector']) ,
      "IsGradeScoping":int(request.form['IsGradeScoping']) ,
      "IsPlagiarism":int(request.form['IsPlagiarism']) ,
      "IsRecheck":int(request.form['IsRecheck'])

    }

    response = generic.Exec_Proc(Procedures.CreateAssignment,Obj)


   





    return  jsonify({'AssignmentID': AssignmentID ,"FilePath" :FilePath})


def CreateStdAssignmentSubmission(request):

    #res =request.form['AssignmentName']
    file =request.files['File']

    api_endpoint ="http://192.168.5.250:7868/api/Uploader/UploadAssignmentStudent"

    #api_endpoint ="https://localhost:7180/api/Uploader/UploadAssignment"


    

    headers = {
    'accept': 'multipart/form-data',
    #'X-Api-Key': '5be2160ca87c4424bd8d9893ba3ee5aa',
    }
    Newfiles = {'File': (file.filename, file.stream, file.content_type)}
    response = requests.post(api_endpoint, files=Newfiles, headers=headers)


    path =response.text

    data = json.loads(path)

    url = data['Response']

    

    FilePath =url

    
  
    Obj ={

        "StudentId" :request.form['StudentId'],
        "AssignmentId" :request.form['AssignmentId'],
        "AssignmentPath":FilePath

    }

    response = generic.Exec_Proc(Procedures.CreateStdAssignmentSubmission,Obj)


    return  jsonify({'AssignmentID': request.form['AssignmentId'] ,"FilePath" :FilePath})


def GetStdAssignmentSubmission(params):

    response = generic.Exec_Search(Procedures.GetStdAssignmentSubmission,params)
    return response



def CreateAssignment(params):

   
    InviteMail = params["InviteMail"]
    #MailService.MailSend("","You Have New Assignemnt",params["AssignmentName"],InviteMail)

    AssignemtnId = uuid.uuid4()
    for x in InviteMail:
        a = { "InviteMail" : x,
              "AssignemtnId" :AssignemtnId,
              "CouresId" :params["CourseID"]
              } 
        
       # RegisterStudents(x,"Name",params["CourseID"],params["AssignmentName"])
        #generic.Exec_Proc(Procedures.CreateAssignmentInvites,a)
        


    params["InviteMail"] = ""
    params["AssignmentID"] = AssignemtnId
   # response = generic.Exec_Proc(Procedures.CreateAssignment,params)

   # result = generic.Exec_Search(Procedures.GetStudent,'DepatmentId:'+ departmentId  +'')
    pdf_target = os.path.join(APP_ROOT, '../static/pdf')

    # Preparing directory
    if not os.path.isdir(pdf_target):
        os.mkdir(pdf_target)

    # Uploading File
    for file in request.files.getlist('file'):
        filename = file.filename
        destination = "/".join([pdf_target,filename])

        file.save(destination)
   

    return ""

def CreateAssignmentInvites(params):
    
    
    InviteMail = params["InviteMail"]
    AssignemtnId = params["AssignmentID"]
    CouresId = params["CourseID"]
    Name =params["Name"]
   
    for x,y in zip(InviteMail, Name):
        a = { "InviteMail" : x,
              "AssignemtnId" :AssignemtnId,
              "CouresId" :CouresId
              }        
        #MailService.MailSend("","You Have New Assignemnt",params["AssignmentName"],x)
        RegisterStudents(x,y,params["CourseID"],params["AssignmentName"])
        response = generic.Exec_Proc(Procedures.CreateAssignmentInvites,a)


    
    return response



def GetAssignment(params):

    response = generic.Exec_Search(Procedures.GetAssignment,params)
    return response

def DeleteAssignment(params):

    response = generic.Exec_Proc(Procedures.DeleteAssignment,params)
    return response


def GetAssignmentFromInstructor(params):

    response = generic.Exec_Search(Procedures.GetAssignmentFromInstructor,params)
    return response


def GetAssignmetForInvitedStudent(params):

    response = generic.Exec_Search(Procedures.GetAssignmetForInvitedStudent,params)
    return response


def GetAssignemntResult(params):

    response = generic.Exec_Search(Procedures.GetAssignemntResult,params)
    return response


def GetInvitedStudents(params):

    response = generic.Exec_Search(Procedures.GetInvitedStudents,params)
    return response


# def DeleteAssignment(params):

#     response = generic.Exec_Proc(Procedures.DeleteAssignment,params)
#     return response



def RegisterStudents(Email,Name,CourseID,AssignmentName):


    obj ={
        "Email" :Email
    }

    objCourseId ={
        "CourseID" :CourseID
    }
    
    GetCourse = generic.Exec_Search(Procedures.GetCourse,objCourseId)


    res = generic.Exec_Search(Procedures.SearchStudent,obj)


    
    courseNo = GetCourse[0]["Response"]

    CourseCode = courseNo[0]["CourseNo"]




    res2 = res[0]["Response"]

    Password =generate_password()

    if(res2 == []):

        Data ={
            "CourseID":CourseID,
            "CourseCode": CourseCode,
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


        MailService.MailSend("","You Have New Assignemnt Regarding Course ("+ CourseCode +")"," Dear Student \n Your Account Has Been Created Please Find You Login Credential Is \nEmail : "+ Email +"\n Password:"+ Password +"\n"+ AssignmentName +"",Email)
    else:
        MailService.MailSend("","You Have New Assignemnt Regarding Course ("+ CourseCode +")",AssignmentName,Email)

    


    # if res.index[0]:
    #     print("Success")

    


    print(res)


def CreateRequestRegrade(params):

    response = generic.Exec_Proc(Procedures.CreateRequestRegrade,params)
    return response


def GetAssignmentSelection(params):

    response = generic.Exec_Search(Procedures.GetAssignmentSelection,params)
    return response


def GetAssignmentStatus(params):

    response = generic.Exec_Search(Procedures.GetAssignmentStatus,params)
    return response



def GetInvitedStudentByAssignment(params):

    response = generic.Exec_Search(Procedures.GetInvitedStudentByAssignment,params)
    return response


def CreateAiDetector(params):

    response = generic.Exec_Proc(Procedures.CreateAiDetector,params)
    return response


def AcceptAssignmentInvites(params):

    response = generic.Exec_Proc(Procedures.AcceptAssignmentInvites,params)
    return response




def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
    # obj = {
    #     "CourseID" :	CourseID,
    #     "Name"		:Name,
    #     "Email"		:Email
    # }

    # response = generic.Exec_Proc(Procedures.CreateStudent,obj)