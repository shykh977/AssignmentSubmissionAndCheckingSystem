
from flask import Blueprint
from flask import Flask ,request,jsonify
from Commons.Constant import Procedures
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
from DataRepository.GenericRepo import GenericRepository

generic = GenericRepository()

def CreateAssignmentType(params):

    response = generic.Exec_Proc(Procedures.CreateAssignmentType,params)
    return response


def GetAssignmentType(params):

    response = generic.Exec_Search(Procedures.GetAssignmentType,params)
    return response


def DeleteAssignmentType(params):

    response = generic.Exec_Proc(Procedures.DeleteAssignmentType,params)
    return response