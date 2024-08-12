from flask import Blueprint
from flask import Flask ,request,jsonify
from DataRepository.UserService import UserService
from DataSecureLayer.UserAccess import token_required
import Cores.CourseCores

app = Flask(__name__)
app.config['SECRET_KEY'] = '110022'

Course_Controller = Blueprint('Course', __name__)

cors = Cores.CourseCores


@Course_Controller.route('/CreateCourse',methods=['POST'])
#@token_required
def CreateCourse():   
    params = request.json   
    response =cors.CreateCourse(params)
    return response


@Course_Controller.route('/CreateEnroledCourses',methods=['POST'])
#@token_required
def CreateEnroledCourses():   
    params = request.json   
    response =cors.CreateEnroledCourses(params)
    return response


@Course_Controller.route('/GetCourse',methods=['POST'])
#@token_required
def GetCourse():   
    params = request.json   
    return cors.GetCourse(params)

@Course_Controller.route('/GetTotalUsersOfCourse',methods=['POST'])
#@token_required
def GetTotalUsersOfCourse():   
    params = request.json   
    return cors.GetTotalUsersOfCourse(params)


@Course_Controller.route('/GetCoursesDetail',methods=['POST'])
#@token_required
def GetCoursesDetail():   
    params = request.json   
    return cors.GetCoursesDetail(params)



@Course_Controller.route('/GetEnroledCourses',methods=['POST'])
#@token_required
def GetEnroledCourses():   
    params = request.json   
    return cors.GetEnroledCourses(params)


@Course_Controller.route('/DeleteCourse',methods=['POST'])
#@token_required
def DeleteCourse():   
    params = request.json   
    return cors.DeleteCourse(params)



