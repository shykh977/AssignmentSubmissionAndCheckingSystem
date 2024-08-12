
from flask import Blueprint
from flask import Flask ,request,jsonify
from Commons.Constant import Procedures
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
from DataRepository.GenericRepo import GenericRepository

generic = GenericRepository()

def CreateUpdateDepartment(params):

    response = generic.Exec_Proc(Procedures.CreateDepartment,params)
    return response


def GetDepartment(params):

    response = generic.Exec_Search(Procedures.GetDepartment,params)
    return response