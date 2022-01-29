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
        main_dictionary['Books'][serial_num] = book.__dict__

        with open('main_dictionary.json', 'w') as outfile:
            json.dump(main_dictionary, outfile)

    def get_book(username, serial_number_book):
        main_dictionary_path = open('main_dictionary.json')
        main_dictionary = json.load(main_dictionary_path)

        main_dictionary['Books'][serial_number_book]['inventory_quantity'] -= 1
        main_dictionary['Users'][username]['book_list'][serial_number_book] = main_dictionary['Books'][serial_number_book]

        with open('main_dictionary.json', 'w') as outfile:
            json.dump(main_dictionary, outfile)

    def get_books_list_by_course_filter(course):
        book_list_filter=dict()
        main_dictionary_path = open('main_dictionary.json')
        main_dictionary = json.load(main_dictionary_path)
        for serial_number_book in main_dictionary["Books"]:
            if course in main_dictionary["Books"][serial_number_book]['useful_courses_list']:
                book_list_filter[serial_number_book] = main_dictionary["Books"][serial_number_book]

        return book_list_filter