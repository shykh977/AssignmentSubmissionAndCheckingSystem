
import os
import uuid
from flask import Blueprint
from flask import Flask ,request,jsonify
from Commons.Constant import Procedures
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
from DataRepository.GenericRepo import GenericRepository
import uuid


generic = GenericRepository()
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def CreateRubric(params):



    RubricID  = uuid.uuid4()
    params["RubricID"] = RubricID

    response = generic.Exec_Proc(Procedures.CreateRubric,params)

    return jsonify({'RubricID': RubricID})

def CreateRubricResult(request):



    

    file =request.files.getlist('PDF')

    FilePath =""

    pdf_target = os.path.join(APP_ROOT, '../static/pdf_image')

    RubricID=request.form['RubricID']

    for file in request.files.getlist('File'):
        filename = file.filename
        var3 = "".join([str(RubricID),filename])
        destination = "/".join([pdf_target,var3])

        FilePath = destination

        file.save(destination)

    obj ={
        "RubricID":request.form['RubricID'],
        "StudentId":request.form['StudentId'],
        "RubricTitle":request.form['RubricTitle'],
        "AssignmentID":request.form['AssignmentID'],
        "AnswerPageNo" :request.form['AnswerPageNo'],
        "ImagePath" :FilePath,
        "IsSubmitted" :1
        }

    response = generic.Exec_Proc(Procedures.CreateRubricResult,obj)
    return response






def GetRubric(params):

    response = generic.Exec_Search(Procedures.GetRubric,params)
    return response


def DeleteRubric(params):

    response = generic.Exec_Search(Procedures.DeleteRubric,params)
    return response