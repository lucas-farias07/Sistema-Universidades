#----------------------------------------------------
from __init__ import  session, StudentsRegistration, Courses, Subjects, Teachers #sessionmaker object (for database connection) and tables
from __init__ import RED, GREEN, CYAN, RESET #color codes
from shared.objects import Student, Course, Subject, Teacher #classes for objects
from shared.enums import EN_Tuition, EN_area #dictionary with the tuition status
#----------------------------------------------------
import sqlalchemy as db #for database manipulation and reading
#----------------------------------------------------


def search(pId: int, pTable: db.Table):
    RegistrationId = StudentsRegistration.c.RegistrationId
    CourseId = Courses.c.CourseId
    SubjectId = Subjects.c.SubjectId
    TeacherId = Teachers.c.TeacherId
    ids = {
        StudentsRegistration: RegistrationId,
        Courses: CourseId,
        Subjects: SubjectId,
        Teachers: TeacherId
    }

    obj = db.select(pTable).where(ids[pTable] == pId)
    ans = session.execute(obj).fetchall()
    return [i for i in ans[0]]


def findStudent():
    #gets a object of the class Student from the registration number
    registrationNum = input("Enter the student's registration number: ")
    student = Student(*search(registrationNum, StudentsRegistration))

    #rule for color of tuition payment
    isPaid = RED
    if student.tuition_isPaid: isPaid = GREEN

    #interface    
    print(f"""
-    Registration number: {CYAN}{student.registration}{RESET}
-    Student name: {CYAN}{student.student_name}{RESET}
-    Tuition is paid: {isPaid}{EN_Tuition[student.tuition_isPaid]}{RESET}
-    Date of registration: {CYAN}{student.date_registration}{RESET}
-    Date of renovation of registration: {CYAN}{student.date_renovation_of_registration}{RESET}
""")
    
    #input to continue
    input("Press enter to continue...")

def findCourse():
    #gets a object of the class Course from the course id
    courseNum = input("Enter the course id: ")
    course = Course(*search(courseNum, Courses))

    print(f"""
-    Course id: {CYAN}{course.course_id}{RESET}
-    Course name: {CYAN}{course.course_name}{RESET}
-    Duration: {CYAN}{course.duration} Years{RESET}  
-    Area: {CYAN}{course.area}{RESET}
""")
    
    input("Press enter to continue...")

def findSubject():

    #gets a object of the class Subject from the subject id
    subjectNum = input("Enter the subject id: ")
    subject = Subject(*search(subjectNum, Subjects))

    print(f"""
-    Course id: {CYAN}{subject.subject_id}{RESET}
-    Course name: {CYAN}{subject.name}{RESET}
-    Duration: {CYAN}{subject.duration} Hours{RESET}  
-    Area: {CYAN}{subject.area}{RESET}
""")
    input("Press enter to continue...")

def findTeacher():
    teacherNum = input("Enter the teacher id: ")
    teacher = Teacher(*search(teacherNum, Teachers))

    contact = teacher.contact_number	
    if teacher.contact_number is None: contact = "{RED} Not informed {RESET}"

    print(f"""
-    Teacher id: {CYAN}{teacher.teacher_id}{RESET}
-    Teacher name: {CYAN}{teacher.name}{RESET}
-    Passport number: {CYAN}{teacher.passport_number}{RESET}  
-    Phone Number: {CYAN}{contact}{RESET}
-    E-mail address: {CYAN}{teacher.email}{RESET}
""")
    input("Press enter to continue...")

def exportToFile():
    #gets the data from the database
    students = session.execute(db.select(StudentsRegistration)).fetchall()
    courses = session.execute(db.select(Courses)).fetchall()
    subjects = session.execute(db.select(Subjects)).fetchall()
    teachers = session.execute(db.select(Teachers)).fetchall()

    #writes the data to a file
    with open("reports/database.txt", "w") as file:
        file.write(f"-----Students-----\n")
        for i in students:
            file.write(f"   Registration number: {i[0]}\n")
            file.write(f"   Student name: {i[1]}\n")
            file.write(f"   Tuition is paid: {EN_Tuition[i[2]]}\n")
            file.write(f"   Date of registration: {i[3]}\n")
            file.write(f"   Date of renovation of registration: {i[4]}\n\n")

        file.write(f"-----Courses-----\n")
        for i in courses:
            file.write(f"   Course id: {i[0]}\n")
            file.write(f"   Course name: {i[1]}\n")
            file.write(f"   Duration: {i[2]} Years\n")
            file.write(f"   Area: {EN_area[i[3]]}\n\n")

        file.write(f"-----Subjects-----\n")
        for i in subjects:
            file.write(f"   Subject id: {i[0]}\n")
            file.write(f"   Subject name: {i[1]}\n")
            file.write(f"   Duration: {i[2]} Hours\n")
            file.write(f"   Area: {EN_area[i[3]]}\n\n")

        file.write(f"-----Teachers-----\n")
        for i in teachers:
            file.write(f"   Teacher id: {i[0]}\n")
            file.write(f"   Teacher name: {i[1]}\n")
            file.write(f"   Passport number: {i[2]}\n")
            file.write(f"   Phone number: {i[3]}\n")
            file.write(f"   E-mail address: {i[4]}\n\n")

    print(f"{GREEN}Data exported to database.txt{RESET}")
    input("Press enter to continue...")