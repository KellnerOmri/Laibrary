from copy import deepcopy

from person import Person
import json


class Student(Person):
    def __init__(self):
        self.register_course_list = ["Math"]
        self.book_list = {}


    def add_student_to_list(person, register_course_list=["Math"],book_list={}):
        main_dictionary_path = open('main_dictionary.json')
        main_dictionary_json = json.load(main_dictionary_path)
        student = Student()
        student.id = person.id.get()
        student.first_name = person.first_name.get()
        student.last_name = person.last_name.get()
        student.password = person.password.get()
        student.date = person.date.get()
        student.register_course_list = register_course_list
        student.is_student = True
        main_dictionary_json['Users'][person.nick_name.get()] = student.__dict__

        with open('main_dictionary.json', 'w') as outfile:
            json.dump(main_dictionary_json, outfile)
