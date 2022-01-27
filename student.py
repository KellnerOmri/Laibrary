from person import Person
import json


class Student(Person):
    def __init__(self):
        self.student_id = 3
        self.register_course_list = ["Math"]

    def add_student_to_list(nick_name, first_name, last_name, password, id=1234, student_id=4, date="03/03/1994",
                            register_course_list=["Math", "English"], is_student=True):
        main_dictionary_path = open('main_dictionary.json')
        main_dictionary_json = json.load(main_dictionary_path)
        student = Student()
        student.id = id
        student.first_name = first_name
        student.last_name = last_name
        student.password = password
        student.student_id = student_id
        student.date = date
        student.register_course_list = register_course_list
        student.is_student = is_student
        main_dictionary_json['Users'][nick_name] = student.__dict__

        with open('main_dictionary.json', 'w') as outfile:
            json.dump(main_dictionary_json, outfile)
