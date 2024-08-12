from flask import Blueprint
from flask import Flask ,request,jsonify
from Commons.Constant import Procedures
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
from DataRepository.GenericRepo import GenericRepository


generic = GenericRepository()

def CreateUniversity(params):

    response = generic.Exec_Proc(Procedures.CreateUniversity,params)
    return response


def GetUniversity(params):

    response = generic.Exec_Search(Procedures.GetUniversity,params)
    return response