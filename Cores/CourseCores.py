
from flask import Blueprint
from flask import Flask ,request,jsonify
from Commons.Constant import Procedures
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
from DataRepository.GenericRepo import GenericRepository

generic = GenericRepository()

def CreateCourse(params):

    response = generic.Exec_Proc(Procedures.CreateCourse,params)
    return response

def CreateEnroledCourses(params):


    obj ={
        "StudentId"	:params["StudentId"],
        "CourseCode" :params["CourseCode"]

    }

    CourseId =generic.Exec_Search(Procedures.CheckAssignemntInvites,obj)

    res2 = CourseId[0]["Response"]

    if(res2 == []):
        return jsonify({"Error" :"Your Are Not Invited In Any Course Or Assignment"}),403
    else:
        response = generic.Exec_Proc(Procedures.CreateEnroledCourses,params)

        return response


    
   


def GetEnroledCourses(params):

    response = generic.Exec_Search(Procedures.GetEnroledCourses,params)
    return response


def GetCourse(params):

    response = generic.Exec_Search(Procedures.GetCourse,params)
    return response

def GetTotalUsersOfCourse(params):

    response = generic.Exec_Search(Procedures.GetTotalUsersOfCourse,params)
    return response


def GetCoursesDetail(params):

    response = generic.Exec_Search(Procedures.GetCoursesDetail,params)
    return response



def DeleteCourse(params):

    response = generic.Exec_Proc(Procedures.DeleteCourse,params)
    return response