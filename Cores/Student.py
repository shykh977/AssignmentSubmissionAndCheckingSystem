from flask import Blueprint
from flask import Flask ,request,jsonify
from Commons.Constant import Procedures
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
from DataRepository.GenericRepo import GenericRepository


generic = GenericRepository()

def CreateStudent(params):

    response = generic.Exec_Proc(Procedures.CreateUpdateStudent,params)
    return response


def GetStudents(params):

    response = generic.Exec_Search(Procedures.GetStudents,params)
    return response