import json

from lecturer import Lecturer



class Course(object):
    def __init__(self):
        self.lecturer = Lecturer()
        self.student_list = []
        self.weekly_hours = 0
        self.university_points = 1

    def add_course_to_list(lecturer_name, course_name, lecturer, weekly_hours, university_points):
        main_dictionary_path = open('main_dictionary.json')
        main_dictionary = json.load(main_dictionary_path)
        course = Course()
        lecturer['teach_course_list'].append(course_name)
        course.lecturer = lecturer
        course.weekly_hours = weekly_hours
        course.university_points = university_points

        main_dictionary["Users"][lecturer_name]['teach_course_list'].append(course_name)
        main_dictionary['Courses'][course_name] = course.__dict__

        with open('main_dictionary.json', 'w') as outfile:
            json.dump(main_dictionary, outfile)
