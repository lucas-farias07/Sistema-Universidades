from shared.enums import EN_area, EN_Tuition

class Student:
    def __init__(self, registration=None, student_name=None, tuition_isPaid=None, date_registration=None, date_renovation_of_registration=None):
        self.registration = registration
        self.student_name = student_name
        self.tuition_isPaid = tuition_isPaid
        self.date_registration = date_registration
        self.date_renovation_of_registration = date_renovation_of_registration

class Course:
    def __init__(self, course_id=None, course_name=None, duration=None, area=None):
        self.course_id = course_id
        self.course_name = course_name
        self.duration = duration
        self.area = EN_area[area]

class Subject:
    def __init__(self, subject_id=None, name=None, duration=None, area=None):
        self.subject_id = subject_id
        self.name = name
        self.duration = duration    
        self.area = EN_area[area]  

class Teacher:
    def __init__(self, teacher_id, name=None, passport_number=None, contact_number=None, email=None):
        self.teacher_id = teacher_id
        self.name = name
        self.passport_number = passport_number
        self.contact_number = contact_number
        self.email = email

