from flask import Blueprint
from flask import Flask ,request,jsonify
from Commons.Constant import Procedures
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
from DataRepository.GenericRepo import GenericRepository


generic = GenericRepository()

def CreateUsers(params):

    response = generic.Exec_Proc(Procedures.CreateUpdateUsers,params)
    return response

def LoginUser(params):

    response = generic.LoginUser(Procedures.LoginUser,params)
    return response


def GetRecentlyJoinUsers(params):

    response = generic.Exec_Search(Procedures.GetRecentlyJoinUsers,params)
    return response


def UpdatePassword(params):

    response = generic.Exec_Proc(Procedures.UpdatePassword,params)
    return response

# def GetUniversity(params):

#     response = generic.Exec_Search(Procedures.GetUniversity,params)
#     return response