
from Controllers.Assignment.AssignmentController import Assignment_Controller
from Controllers.AssignmentType.AssignmentTypeController import AssignmentType_Controller
from Controllers.Course.CourseController import Course_Controller
from Controllers.Rubric.RubricController import RubricCores_Controller
from Controllers.RubricQuestions.RubricQuestionsController import RubricQuestions_Controller
from Controllers.RubricSubQuestions.RubricSubQuestionsController import RubricSubQuestions_Controller
from Controllers.Student.StudentController import Student_Controller
from Controllers.SubmissionType.SubmissionTypeController import SubmissionType_Controller

from Controllers.University.UniversityController import Univesity_Controller
from Controllers.Department.DepartmentController import Department_Controller
from Controllers.Faculty.FacultyController import Faculty_Controller
from Controllers.Users.UsersController import Users_Controller
from Controllers.UserRoles.UserRolesController import UserRoles_Controller
from Controllers.Exam.ExamController import Exam_Controller
from Controllers.ExamResult.ExamResultController import ExamResult_Controller

def register_blueprints(app):
  
    app.register_blueprint(Assignment_Controller)
    app.register_blueprint(AssignmentType_Controller)
    app.register_blueprint(Course_Controller)
    app.register_blueprint(RubricCores_Controller)
    app.register_blueprint(RubricQuestions_Controller)
    app.register_blueprint(RubricSubQuestions_Controller)
    app.register_blueprint(Student_Controller)
    app.register_blueprint(SubmissionType_Controller)
    app.register_blueprint(Univesity_Controller)
    app.register_blueprint(Department_Controller)
    app.register_blueprint(Faculty_Controller)
    app.register_blueprint(Users_Controller)
    app.register_blueprint(UserRoles_Controller)
    app.register_blueprint(Exam_Controller)
    app.register_blueprint(ExamResult_Controller)