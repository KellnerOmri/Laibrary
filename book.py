import copy
import json
import datetime as datetime2
from datetime import datetime


class Book(object):
    def __init__(self):
        self.name = ""
        self.author = ""
        self.inventory_quantity = 1
        self.useful_courses_list = []
        self.quantity_ordered = 0

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

        if serial_number_book not in main_dictionary["Users"][username]["book_list"]:
            main_dictionary['Books'][serial_number_book]['inventory_quantity'] -= 1
            main_dictionary['Books'][serial_number_book]['quantity_ordered'] += 1
            book_dettails_for_user = copy.copy(main_dictionary['Books'][serial_number_book])

            book_dettails_for_user.pop('inventory_quantity')
            book_dettails_for_user.pop('quantity_ordered')
            main_dictionary['Users'][username]['book_list'][serial_number_book] = book_dettails_for_user
            main_dictionary['Users'][username]['book_list'][serial_number_book][
                'order_date'] = datetime2.datetime.now().date().strftime('%y-%m-%d')
            main_dictionary['Users'][username]['book_list'][serial_number_book]['return_date'] = (
                    datetime2.datetime.now() + datetime2.timedelta(days=7)).date().strftime('%y-%m-%d')

            with open('main_dictionary.json', 'w') as outfile:
                json.dump(main_dictionary, outfile)

    def return_book(username, serial_number_book):
        main_dictionary_path = open('main_dictionary.json')
        main_dictionary = json.load(main_dictionary_path)

        main_dictionary['Books'][serial_number_book]['inventory_quantity'] += 1
        main_dictionary['Books'][serial_number_book]['quantity_ordered'] -= 1
        if datetime.strptime(main_dictionary['Users'][username]['book_list'][serial_number_book]['return_date'],
                             '%y-%m-%d').date() < datetime.now().date():
            main_dictionary['Users'][username]['fee'] += 50

        del main_dictionary['Users'][username]["book_list"][serial_number_book]

        with open('main_dictionary.json', 'w') as outfile:
            json.dump(main_dictionary, outfile)

    def get_books_list_by_course_filter(username, course, author_name):
        book_list_filter = dict()
        main_dictionary_path = open('main_dictionary.json')
        main_dictionary = json.load(main_dictionary_path)
        if course == "All":
            for serial_number_book in main_dictionary["Books"]:
                if serial_number_book not in main_dictionary["Users"][username]["book_list"]:
                    book_list_filter[serial_number_book] = main_dictionary["Books"][serial_number_book]
        else:
            for serial_number_book in main_dictionary["Books"]:
                if serial_number_book not in main_dictionary["Users"][username]["book_list"]:
                    if course in main_dictionary["Books"][serial_number_book]['useful_courses_list']:
                        book_list_filter[serial_number_book] = main_dictionary["Books"][serial_number_book]
        book_list_filter = get_books_list_by_author_filter(book_list_filter, author_name)
        return book_list_filter

    def Extending_loan(username, serial_number_book):
        main_dictionary_path = open('main_dictionary.json')
        main_dictionary = json.load(main_dictionary_path)
        return_date_str = main_dictionary['Users'][username]['book_list'][serial_number_book]['return_date']
        return_date_obj = datetime.strptime(return_date_str, '%y-%m-%d').date()

        return_date_str = (return_date_obj + datetime2.timedelta(days=7)).date().strftime('%y-%m-%d')
        main_dictionary['Users'][username]['book_list'][serial_number_book]['return_date'] = return_date_str

        with open('main_dictionary.json', 'w') as outfile:
            json.dump(main_dictionary, outfile)


def get_books_list_by_author_filter(book_list_filter, author_name):
    temp_book_list = dict()
    if author_name != '':
        for book_serial_number in book_list_filter:
            if author_name == book_list_filter[book_serial_number]['author']:
                temp_book_list[book_serial_number] = book_list_filter[book_serial_number]
        return temp_book_list
    return book_list_filter
