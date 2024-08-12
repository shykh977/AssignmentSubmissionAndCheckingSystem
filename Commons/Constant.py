class Procedures:



    LoginUser ="usp_LoginUsers"

    ###Place All Create Procedures Here
    CreateAssignment= "usp_Create_Update_Assignment"
    CreateAssignmentType="usp_Create_Update_AssignmentType"
    CreateCourse="usp_Create_Update_Course"
    CreateRubric="usp_Create_Update_Rubric"
    CreateRubricQuestions="usp_Create_Update_RubricQuestions"
    CreateRubricSubQuestions="usp_Create_Update_RubricSubQuestions"
    CreateStudent="usp_Create_Update_Student"
    CreateSubmissionType="usp_Create_Update_SubmissionType"
    CreateDepartment="usp_Create_Update_Department"
    CreateUniversity="usp_Create_Update_University"
    CreateFaculty =  "usp_Create_Update_Faculty"
    CreateAssignmentInvites ="usp_Create_Update_AssignmentInvites"
    CreateEnroledCourses ="usp_Create_Update_EnroledCourses"
    LoginUser="usp_LoginUsers"
    
    UpdatePassword="usp_UpdatePassword"

    CreateUsers ="usp_Create_Update_Users"

    CreateRubricResult="usp_Create_Update_RubricResult"
    CreateRubricQuestionsResult="usp_Create_Update_RubricQuestionsResult"
    CreateRubricSubQuestionsResult="usp_Create_Update_RubricSubQuestionsResult"

   #  CreateRubricQuestionsResult="usp_Create_Update_RubricQuestionsResultNew"
   #  CreateRubricSubQuestionsResult="usp_Create_Update_RubricSubQuestionsResultNew"

    SubQuestionResultCheck="usp_SubQuestionResultCheck"
    CreateRequestRegrade="usp_Create_Update_RequestRegrade"
    CreateAiDetector ="usp_Create_Update_AiDetector"
    CreateStdAssignmentSubmission="usp_Create_Update_StdAssignmentSubmission"

    AcceptAssignmentInvites="usp_AcceptAssignmentInvites"
   

    ###############################################
    ##################----Exam Soft----############
    ###############################################

    CreateExamType="usp_Create_Update_ExamType"
    CreateExamLocation="usp_Create_Update_ExamLocation"
    CreateExamSlot="usp_Create_Update_ExamSlot"
    CreateExams="usp_Create_Update_Exams"
    CreateExamsQuestions="usp_Create_Update_ExamsQuestions"
    CreateQuestionOptions="usp_Create_Update_QuestionOptions"

    CreateExamResult ="usp_Create_Update_ExamResult"
    CreateExamQuestionsResult="usp_Create_Update_ExamQuestionsResult"
    CreateSelectQuestionOptions="usp_Create_Update_SelectQuestionOptions"
    CreateExamInvite="usp_Create_Update_ExamInvite"
    CreateQuestionOptionsResultLog="usp_Create_Update_QuestionOptionsResultLog"
    AcceptExamLogin="usp_AcceptExamLogin"

    FinishExam="usp_FinishExam"




    ###Place All GET Procedures Here
    GetAssignment= "usp_GetAssignment"
    GetAssignmentType= "usp_GetAssignmentType"
    GetCourse= "usp_GetCourse"
    GetRubric= "usp_GetRubric"
    GetRubricQuestion= "usp_GetRubricQuestion"
    GetRubricSubQuestions= "usp_GetRubricSubQuestions"
    GetStudent= "usp_GetStudents"
    GetSubmissionType= "usp_GetSubmissionType"
    GetTerm ="usp_GetTerm"
    GetUniversity="usp_GetUniversity"
    GetDepartment ="usp_GetDepartment"
    GetEnroledCourses="usp_GetEnroledCourses"
    GetCoursesDetail ="usp_GetCoursesDetailNew"
    SearchStudent="usp_SearchStudent"
    GetInvitedStudents="usp_GetInitedStudent"
    GetRubricQuestionResult="usp_GetRubricQuestionResult"
    GetRubricSubQuestionsResult="usp_GetRubricSubQuestionsResult"

    GetRecentlyJoinUsers="usp_GetRecentlyJoinUsers"

    GetAssignemntResult="usp_GetAssignemntResult"

    GetAssignmentSelection="usg_GetAssignmentSelection"

    GetInvitedStudentByAssignment="usp_GetInvitedStudentByAssignment"

    GetTotalUsersOfCourse="usp_GetTotalUsersOfCourse"

    GetAssignmentStatus="usp_GetAssignmentStatus"

    CheckAssignemntInvites="usp_CheckAssignemntInvites"
    GetStdAssignmentSubmission="usp_GetStdAssignmentSubmission"
    GetAssignmentFromInstructor="usp_GetAssignmentFromInstructor"
    GetAssignmetForInvitedStudent="usp_GetAssignetForInvitedStudent"

    ###############################################
    ##################----Exam Soft----############
    ###############################################
    GetExam="usp_GetExam"
    GetExamType="usp_GetExamType"
    GetExamLocation="usp_GetExamLocation"
    GetExamSlot="usp_GetExamSlot"
    GetQuestionOptions="usp_GetQuestionOptions"
    GetExamQuestion="usp_GetExamQuestion"
    CheckExamInvite="usp_CheckExamInvite"
    LoginExam="usp_LoginExam"
    GetInvitedExam="usp_GetInvitedExam"
    GetIsAcceptExam="usp_GetIsAcceptExam"
    GetExamResult="usp_GetExamResult"
    GetQuestionCount="usp_GetQuestionCount"
    GetExamQuestionsResult="usp_GetExamQuestionsResult"

    ###Place All Delete Procedures Here
    DeleteAssignment= "usp_AssignmentDelete"
    DeleteAssignmentType= "usp_AssignmentTypeDelete"
    DeleteCourse= "usp_CourseDelete"
    DeleteRubric= "usp_RubricDelete"
    DeleteRubricQuestions= "usp_RubricQuestionsDelete"
    DeleteRubricSubQuestions= "usp_RubricSubQuestionsDelete"
    DeleteStudent= "usp_StudentDelete"
    DeleteSubmissionType= "usp_SubmissionTypeDelete"
    DeletedAssignment="usp_DeletedAssignment"

       ###############################################
    ##################----Exam Soft----############
    ###############################################

    DeleteExam="usp_DeleteExam"
    DeleteExamType="usp_DeleteExamType"
    DeleteExamLocation="usp_DeleteExamLocation"
    DeleteExamSlot="usp_DeleteExamSlot"
    DeleteExamsQuestions="usp_DeleteExamsQuestions"
    DeleteQuestionOptions="usp_DeleteQuestionOptions"