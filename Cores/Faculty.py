from flask import Blueprint
from flask import Flask ,request,jsonify
from Commons.Constant import Procedures
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
from DataRepository.GenericRepo import GenericRepository


generic = GenericRepository()

def CreateFaculty(params):

    response = generic.Exec_Proc(Procedures.CreateFaculty,params)
    return response


def GetFaculty(params):

    response = generic.Exec_Search(Procedures.GetFaculty,params)
    return response