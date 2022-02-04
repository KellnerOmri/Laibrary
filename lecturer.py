import json

from person import Person


class Lecturer(Person):
    def __init__(self):
        self.teach_course_list = []
        self.book_list = {}

    def add_lecturer_to_list(person):
        main_dictionary_path = open('main_dictionary.json')
        main_dictionary_json = json.load(main_dictionary_path)
        lecturer = Lecturer()
        lecturer.id = person.id.get()
        lecturer.first_name = person.first_name.get()
        lecturer.last_name = person.last_name.get()
        lecturer.password = person.password.get()
        lecturer.date = person.date.get()
        lecturer.is_student = False
        main_dictionary_json['Users'][person.nick_name.get()] = lecturer.__dict__

        with open('main_dictionary.json', 'w') as outfile:
            json.dump(main_dictionary_json, outfile)
