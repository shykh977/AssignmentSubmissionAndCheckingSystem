
from flask import Blueprint
from flask import Flask ,request,jsonify
from Commons.Constant import Procedures
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
from DataRepository.GenericRepo import GenericRepository

generic = GenericRepository()

def CreateSubmissionType(params):

    response = generic.Exec_Proc(Procedures.CreateSubmissionType,params)
    return response


def GetSubmissionType(params):

    response = generic.Exec_Search(Procedures.GetSubmissionType,params)
    return response

def GetTerm(params):

    response = generic.Exec_Search(Procedures.GetTerm,params)
    return response



def DeleteSubmissionType(params):

    response = generic.Exec_Proc(Procedures.DeleteSubmissionType,params)
    return response