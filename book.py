import json


class Book(object):
    def __init__(self):
        self.name = ""
        self.author = ""
        self.inventory_quantity = 0
        self.useful_courses_list = []

    def add_book_to_list(serial_num, name, author, inventory_quantity, useful_courses_list):
        main_dictionary_path = open('main_dictionary.json')
        main_dictionary = json.load(main_dictionary_path)
        book = Book()
        book.useful_courses_list = useful_courses_list
        book.inventory_quantity = inventory_quantity
        book.author = author
        book.name = name

        for course in book.useful_courses_list:
            main_dictionary['Books'][course][serial_num] = book.__dict__

        with open('main_dictionary.json', 'w') as outfile:
            json.dump(main_dictionary, outfile)
