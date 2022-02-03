import json


class Person(object):
    def __init__(self):
        self.id = ""
        self.first_name = ""
        self.last_name = ""
        self.date = ""
        self.password = ""
        self.nick_name = ""
        self.book_list = {}

    def Pay_fee(username):
        main_dictionary_path = open('main_dictionary.json')
        main_dictionary_json = json.load(main_dictionary_path)
        main_dictionary_json['Users'][username]['fee'] = 0
        with open('main_dictionary.json', 'w') as outfile:
            json.dump(main_dictionary_json, outfile)
