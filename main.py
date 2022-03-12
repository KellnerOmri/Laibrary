from time import strftime
from tkinter import *

from course import Course
from lecturer import Lecturer
from person import Person
from student import Student
from book import Book
from PIL import ImageTk, Image
import json


def register_user(register_person, register_course_list, is_student):
    username_info = register_person.nick_name.get()
    if username_info in main_dictionary_json['Users']:
        Label(register_screen, text="User already exist", font="green", height='2', width='30').pack()
        return False

    if is_student.get():
        Student.add_student_to_list(register_person, get_useful_courses_list(register_course_list, 1))
    else:
        Lecturer.add_lecturer_to_list(register_person)

    Button(register_screen, text=f"registration success!", font="green", height='2', width='30').pack()


def register_user_screen():
    global register_screen
    register_screen = Toplevel(welcome_screen)
    init_screen_setting(register_screen, "500x300", "Register")

    global username
    global password
    register_person = Person()
    username = StringVar()
    password = StringVar()

    # init person
    register_person.id = StringVar()
    register_person.first_name = StringVar()
    register_person.last_name = StringVar()
    register_person.date = StringVar()
    register_person.nick_name = username
    register_person.password = password
    is_student = BooleanVar()

    Label(register_screen, text="Please enter the given given information", height="2", width="30").place(x=60, y=10)
    Label(register_screen, text="Username : ", width='30').place(x=10, y=50)
    Entry(register_screen, textvariable=username).place(x=160, y=50)

    Label(register_screen, text="Password : ", width='30').place(x=10, y=80)
    Entry(register_screen, textvariable=password).place(x=160, y=80)

    Label(register_screen, text="ID : ", width='30').place(x=10, y=110)
    id_entry = Entry(register_screen, textvariable=register_person.id)
    id_entry.place(x=160, y=110)

    Label(register_screen, text="First Name : ", width='30').place(x=10, y=140)
    Entry(register_screen, textvariable=register_person.first_name).place(x=160, y=140)

    Label(register_screen, text="Last Name : ", width='30').place(x=10, y=170)
    Entry(register_screen, textvariable=register_person.last_name).place(x=160, y=170)

    Label(register_screen, text="Date of birth : ", width='30').place(x=10, y=200)
    Entry(register_screen, textvariable=register_person.date).place(x=160, y=200)

    # radio button
    Radiobutton(register_screen, text='Student', value=True, variable=is_student).place(x=30, y=230)
    Radiobutton(register_screen, text='Lecturer', value=False, variable=is_student).place(x=160, y=230)

    Label(register_screen, text="Select witch courses would you like to register: ").place(x=30, y=270)
    place_y = 270
    register_course_list = dict()
    for course in main_dictionary_json["Courses"]:
        place_y += 30
        register_course_list[course] = IntVar()
        chk = Checkbutton(register_screen, text=f'{course}', variable=register_course_list[course])
        chk.place(x=30, y=place_y)

    Button(register_screen, text="submit", width='30',
           command=lambda: register_user(register_person, register_course_list, is_student)).place(x=60,
                                                                                                   y=place_y + 50)


def add_book_screen():
    global add_books_screen
    add_books_screen = Toplevel(menu_screen)
    init_screen_setting(add_books_screen, "780x620", "Add Book To Library")

    book_name = StringVar()
    serial_num = StringVar()
    author_name = StringVar()
    inventory_quantity = IntVar()

    Label(add_books_screen, anchor="center", font=("Helvetica", 14), bg='yellow',
          text="Please enter book's details").place(x=280, y=20)
    add_book_image = ImageTk.PhotoImage(
        (Image.open(r".\images\add_book_image.png")).resize((70, 70), Image.ANTIALIAS))
    Label(add_books_screen, image=add_book_image).place(x=20, y=20)

    Label(add_books_screen, text="book name :").place(x=20, y=190)
    Entry(add_books_screen, textvariable=book_name).place(x=160, y=190)

    Label(add_books_screen, text="Serial Number :").place(x=20, y=220)
    Entry(add_books_screen, textvariable=serial_num).place(x=160, y=220)

    Label(add_books_screen, text="Author :").place(x=20, y=250)
    Entry(add_books_screen, textvariable=author_name).place(x=160, y=250)

    Label(add_books_screen, text="Inventory quantity:").place(x=20, y=280)
    Entry(add_books_screen, textvariable=inventory_quantity).place(x=160, y=280)

    # checkbox
    Label(add_books_screen, text="Select courses that will use this book from the list:").place(x=20, y=330)
    place_x = 20
    course_list = dict()
    for course in main_dictionary_json["Courses"]:
        course_list[course] = IntVar()
        chk = Checkbutton(add_books_screen, text=f'{course}', variable=course_list[course])
        chk.place(x=place_x, y=350)
        place_x += 90

    Button(add_books_screen, text="submit", bg='blue', height='2', width='30',
           command=lambda: add_book(serial_num.get(), book_name.get(), author_name.get(),
                                    inventory_quantity.get(),
                                    get_useful_courses_list(course_list, 1))).place(x=300, y=500)
    back_to_menu(add_books_screen)


def add_book(serial_num, book_name, author_name, inventory_quantity, useful_courses_list):
    Book.add_book_to_list(serial_num, book_name, author_name, inventory_quantity, useful_courses_list)
    Label(add_books_screen, text=f"registration success!", width=30, height='2').place(x=210, y=360)


def back_to_menu(screen_name):
    img = (Image.open(r".\images\back_to_menu_image.png"))
    resized_image = img.resize((50, 50), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    Label(screen_name, text=f"Back to Menu").place(x=650, y=10)
    Button(screen_name, text=f"Back to Menu", image=new_image,
           command=lambda: close_profile_window(screen_name)).place(x=660, y=30)
    screen_name.mainloop()


class return_book_screen():
    def __init__(self):
        main_dictionary_json = json.load(open('main_dictionary.json'))
        return_book_screen = Toplevel(menu_screen)
        init_screen_setting(return_book_screen, "780x620", "Return Book To Library")

        return_book_image = ImageTk.PhotoImage(
            (Image.open(r".\images\return_book_image.png")).resize((70, 70), Image.ANTIALIAS))
        Label(return_book_screen, image=return_book_image).place(x=20, y=20)

        Label(return_book_screen, anchor="center", font=("Helvetica", 14),
              text="Please select a book that you would like to return library", bg='yellow').place(
            x=150,
            y=20)
        place_y = 100
        book_list = main_dictionary_json["Users"][username_verify.get()]["book_list"]
        for serial_number_book in book_list:
            Button(return_book_screen,
                   text=f"Serial Number : {serial_number_book} ,Book Name: {book_list[serial_number_book]['name']} "
                        f",Author: {book_list[serial_number_book]['author']}, Untill Date : {book_list[serial_number_book]['return_date']}",
                   command=lambda serial_number_book=serial_number_book: [Book.return_book(username_verify.get(),
                                                                                           serial_number_book),
                                                                          refref_db(self, return_book_screen)]).place(
                x=150,
                y=place_y)
            place_y += 30
        back_to_menu(return_book_screen)


class extending_loan_screen():
    def __init__(self):
        main_dictionary_json = json.load(open('main_dictionary.json'))

        extending_loan_screen = Toplevel(menu_screen)
        init_screen_setting(extending_loan_screen, "780x620", "Extending loan book request")

        Label(extending_loan_screen, anchor="center", font=("Helvetica", 14), bg='yellow',
              text="Select book for extending loan time").place(x=200, y=20)
        extending_book_loan_image = ImageTk.PhotoImage(
            (Image.open(r".\images\extending_book_loan_image.png")).resize((70, 70), Image.ANTIALIAS))
        Label(extending_loan_screen, image=extending_book_loan_image).place(x=20, y=20)

        Label(extending_loan_screen, text="Add a week to the loan time for each book clicked", font=("Helvetica", 10),
              fg='green').place(x=150, y=70)
        place_y = 100
        book_list = main_dictionary_json["Users"][username_verify.get()]["book_list"]
        for serial_number_book in book_list:
            Button(extending_loan_screen,
                   text=f"Serial Number : {serial_number_book} ,Book Name: {book_list[serial_number_book]['name']} "
                        f",Author: {book_list[serial_number_book]['author']}, Untill Date : {book_list[serial_number_book]['return_date']}",
                   command=lambda serial_number_book=serial_number_book: [Book.Extending_loan(username_verify.get(),
                                                                                              serial_number_book),
                                                                          refref_db(self,
                                                                                    extending_loan_screen)]).place(
                x=150, y=place_y)
            place_y += 30
        back_to_menu(extending_loan_screen)


class pay_fee_screen():
    def __init__(self):
        main_dictionary_json = json.load(open('main_dictionary.json'))
        global pay_fee_screen
        pay_fee_screen = Toplevel(menu_screen)
        init_screen_setting(pay_fee_screen, "780x620", "Pay Fee")
        Label(pay_fee_screen, text="Pay your fee to library man: ", bg='yellow', font=("Helvetica", 14)).place(x=250,
                                                                                                               y=20)

        payment_image = ImageTk.PhotoImage(
            (Image.open(r".\images\paymeny_image.png")).resize((70, 70), Image.ANTIALIAS))
        Label(pay_fee_screen, image=payment_image).place(x=20, y=20)

        fee = main_dictionary_json["Users"][username_verify.get()]['fee']
        if fee > 0:
            Label(pay_fee_screen, text="You can't order more books until your payment be paid up", fg='red',
                  font=("Helvetica", 8)).place(x=20, y=140)

            Label(pay_fee_screen, text=f"You have a debt to pay in the amount of {fee} NIS",
                  fg='red', font=("Helvetica", 14)).place(x=20, y=180)
            Button(pay_fee_screen, text="Pay debt", bg='blue', font=("Helvetica", 18),
                   command=lambda: [Person.Pay_fee(username_verify.get()),
                                    payment_receipt(self, 'The payment was successful')]).place(x=300,
                                                                                                y=500)
        else:
            Label(pay_fee_screen, text="You don't have a debt to pay", fg='green', height="2",
                  font=("Helvetica", 14)).place(x=20, y=90)

        back_to_menu(pay_fee_screen)

    def destroy(self):
        pay_fee_screen().destroy()


def success_payment_label(self):
    refref_db(self, pay_fee_screen)
    Label(pay_fee_screen, text="Payment received successfully,\n You can continue to order books", fg='green',
          height="2",
          font=("Helvetica", 13)).place(x=20, y=50)


def payment_receipt(self, msg):
    popup = Tk()
    popup.geometry('300x200')
    popup.geometry(
        "+{}+{}".format(int(popup.winfo_screenwidth() / 2 - popup.winfo_reqwidth() / 2),
                        int(popup.winfo_screenheight() / 2 - popup.winfo_reqheight() / 2)))
    popup.wm_title("Payment receipt")
    Label(popup, text=msg).pack(side="top", fill="x", pady=10)
    Button(popup, text="Okay", command=lambda: [popup.destroy(), success_payment_label(self)]).pack()
    popup.mainloop()


def add_course_screen():
    global add_course_screen
    add_course_screen = Toplevel(menu_screen)
    init_screen_setting(add_course_screen, "780x620", "Add Book To Library")

    course_name = StringVar()
    weekly_hours = IntVar()
    university_points = IntVar()

    Label(add_course_screen, text="Please enter course's details :", anchor="center", font=("Helvetica", 14),
          bg='yellow').place(x=250, y=20)
    add_course_image = ImageTk.PhotoImage(
        (Image.open(r".\images\add_course_image.png")).resize((70, 70), Image.ANTIALIAS))
    Label(add_course_screen, image=add_course_image).place(x=20, y=20)

    Label(add_course_screen, text="course name :").place(x=20, y=190)
    Entry(add_course_screen, textvariable=course_name).place(x=160, y=190)

    Label(add_course_screen, text="Weekly hours :").place(x=20, y=220)
    Entry(add_course_screen, textvariable=weekly_hours).place(x=160, y=220)

    Label(add_course_screen, text="University points :").place(x=20, y=250)
    Entry(add_course_screen, textvariable=university_points).place(x=160, y=250)

    Button(add_course_screen, text="submit", height='2', width='30', bg='blue',
           command=lambda: add_course(course_name.get(), weekly_hours.get(), university_points.get())).place(x=300,
                                                                                                             y=500)

    back_to_menu(add_course_screen)


def register_course_screen():
    main_dictionary_json = json.load(open('main_dictionary.json'))
    global register_course_screen
    register_course_screen = Toplevel(menu_screen)
    init_screen_setting(register_course_screen, "780x620", "Register To Course")

    Label(register_course_screen, anchor="center", font=("Helvetica", 14), bg='yellow',
          text="Choose witch course would you like to study").place(x=200, y=20)
    register_to_course_image = ImageTk.PhotoImage(
        (Image.open(r".\images\register_to_course_image.png")).resize((70, 70), Image.ANTIALIAS))
    Label(register_course_screen, image=register_to_course_image).place(x=20, y=20)

    Label(register_course_screen, anchor="center", font=("Helvetica", 9), fg='blue',
          text="Select for register course:").place(x=20, y=180)
    place_x = 20
    register_course_list = dict()
    remove_course_list = dict()
    for course in main_dictionary_json["Courses"]:
        if course not in main_dictionary_json["Users"][username_verify.get()]["register_course_list"]:
            register_course_list[course] = IntVar()
            chk = Checkbutton(register_course_screen, text=f'{course}', variable=register_course_list[course])
            chk.place(x=place_x, y=200)
            place_x += 90
        else:
            remove_course_list[course] = IntVar()
            remove_course_list[course].set(1)
            chk = Checkbutton(register_course_screen, text=f'{course}', variable=remove_course_list[course])
            chk.place(x=place_x, y=200)
            place_x += 90

    Button(register_course_screen, text="submit", bg='blue', height='2', width='30',
           command=lambda: Course.register_to_course(get_useful_courses_list(register_course_list, 1),
                                                     get_useful_courses_list(remove_course_list, 0),
                                                     username_verify.get())).place(x=300, y=500)
    back_to_menu(register_course_screen)


def add_course(course_name, weekly_hours, university_points):
    lecturer = main_dictionary_json['Users'][username_verify.get()]
    Course.add_course_to_list(username_verify.get(), course_name, lecturer, weekly_hours, university_points)
    Label(add_course_screen, text=f"registration success!", width=30, height='2').place(x=210, y=360)


def get_useful_courses_list(course_list, required_value):
    useful_courses_list = []
    for course in course_list:
        if course_list[course].get() == required_value:
            useful_courses_list.append(course)
    return useful_courses_list


def login_verify(password_verify):
    main_dictionary_json = json.load(open('main_dictionary.json'))
    user_name = username_verify.get()
    if user_name in main_dictionary_json['Users']:
        if main_dictionary_json['Users'][user_name]["password"] == password_verify.get():
            welcome_screen.destroy()
        else:
            Label(login_screen, text=f"wrong password", height="2", width="30").pack()
            print("wrong password")
    else:
        Label(login_screen, text=f"User {user_name} not found,please try again", height="2", width="30").pack()
        print("User not found")


class login():
    def __init__(self):
        main_dictionary_json = json.load(open('main_dictionary.json'))
        global login_screen
        global username_verify
        username_verify = StringVar()
        password_verify = StringVar()

        login_screen = Toplevel(welcome_screen)
        init_screen_setting(login_screen, "500x300", "Login")

        Label(login_screen, text="Please enter the information for login ", height='2', width='30').pack()
        Label(login_screen, text="", height='2', width='30').pack()
        Label(login_screen, text="username : ", height='2', width='30').pack()
        username_entry1 = Entry(login_screen, textvariable=username_verify)
        username_entry1.pack()
        Label(login_screen, text="password : ", height='2', width='30').pack()
        password_entry1 = Entry(login_screen, textvariable=password_verify)
        password_entry1.pack()
        Label(login_screen, text="", height='2', width='30').pack()
        Button(login_screen, text="login", height="2", width="30", command=lambda: login_verify(password_verify)).pack()


def design_menu_screen():
    def my_time():
        time_string = strftime('%H:%M:%S\n%x')
        l1.config(text=time_string)
        l1.after(1000, my_time)  # time delay of 1000 milliseconds

    my_font = ('times', 14, 'bold')  # display size and style

    l1 = Label(menu_screen, font=my_font, bg='yellow')
    l1.place(x=10, y=10)

    my_time()
    main_dictionary_json = json.load(open('main_dictionary.json'))
    is_student = main_dictionary_json['Users'][username_verify.get()]["is_student"]

    Label(text=f"Welcome {username_verify.get()} To Our Library Program", background='yellow',
          font=("Helvetica", 14)).place(x=250, y=10)

    Label(text="Order Book", anchor="center", font=("Helvetica", 14), bg='blue').place(x=350, y=90)
    order_book_image = ImageTk.PhotoImage(
        (Image.open(r".\images\order_book_image.png")).resize((70, 70), Image.ANTIALIAS))
    Button(text="Order Book", image=order_book_image,
           command=order_book_screen).place(x=250, y=60)
    if is_student:
        # Studio menu
        Label(text="Register to Course", anchor="center", font=("Helvetica", 14), bg='blue').place(x=350, y=450)
        register_to_course_image = ImageTk.PhotoImage(
            (Image.open(r".\images\register_to_course_image.png")).resize((70, 70), Image.ANTIALIAS))
        Button(text="Register to Course", image=register_to_course_image,
               command=register_course_screen).place(x=250, y=420)

    else:
        # Lecturer menu
        Label(text="Add Book", anchor="center", font=("Helvetica", 14), bg='blue').place(x=350, y=450)
        add_book_image = ImageTk.PhotoImage(
            (Image.open(r".\images\add_book_image.png")).resize((70, 70), Image.ANTIALIAS))
        Button(text="Add Book", image=add_book_image,
               command=add_book_screen).place(
            x=250, y=420)

        Label(text="Add Course", anchor="center", font=("Helvetica", 14), bg='blue').place(x=350, y=540)
        add_course_image = ImageTk.PhotoImage(
            (Image.open(r".\images\add_course_image.png")).resize((70, 70), Image.ANTIALIAS))
        Button(text="Add Course", image=add_course_image,
               command=add_course_screen).place(x=250, y=510)

    Label(text="Return Book", anchor="center", font=("Helvetica", 14), bg='blue').place(x=350, y=180)
    return_book_image = ImageTk.PhotoImage(
        (Image.open(r".\images\return_book_image.png")).resize((70, 70), Image.ANTIALIAS))
    Button(text="Return Book", image=return_book_image, command=return_book_screen).place(x=250, y=150)

    Label(text="Extending book loan", anchor="center", font=("Helvetica", 14), bg='blue').place(x=350, y=270)
    extending_book_loan_image = ImageTk.PhotoImage(
        (Image.open(r".\images\extending_book_loan_image.png")).resize((70, 70), Image.ANTIALIAS))
    Button(text="Extending book loan", image=extending_book_loan_image,
           command=extending_loan_screen).place(x=250, y=240)

    Label(text="Payment Fee", anchor="center", font=("Helvetica", 14), bg='blue').place(x=350, y=360)
    paymeny_image = ImageTk.PhotoImage(
        (Image.open(r".\images\paymeny_image.png")).resize((70, 70), Image.ANTIALIAS))
    Button(text="Payment Fee", image=paymeny_image,
           command=pay_fee_screen).place(x=250, y=330),

    Label(text="My Profile", anchor="center", font=("Helvetica", 14), bg='blue', width=9).place(x=660, y=120)
    profile_image = ImageTk.PhotoImage((Image.open(".\images\profile_image.png")).resize((100, 100), Image.ANTIALIAS))
    Button(text="My Profile", image=profile_image,
           command=my_profile_screen).place(x=660, y=10)

    exit_image = ImageTk.PhotoImage((Image.open(".\images\exit_image.png")).resize((100, 100), Image.ANTIALIAS))
    Button(text="Exit", image=exit_image,
           command=exit).place(x=660, y=500)
    menu_screen.mainloop()


class order_book_screen():
    main_dictionary_json = json.load(open('main_dictionary.json'))

    def __init__(self):
        global order_book_screen
        order_book_screen = Toplevel(menu_screen)
        init_screen_setting(order_book_screen, "780x620", "Order Book")
        book_serial_number = StringVar()
        author_name = StringVar()

        Label(order_book_screen, anchor="center", font=("Helvetica", 14), text=f"Please select book or insert details",
              bg='yellow').place(x=250, y=20)

        self.order_book_image = ImageTk.PhotoImage(
            (Image.open(r".\images\order_book_image.png")).resize((70, 70), Image.ANTIALIAS))
        Label(order_book_screen, image=self.order_book_image).place(x=20, y=20)

        Label(order_book_screen, text="Enter book's serial number: ").place(x=100, y=97)
        Entry(order_book_screen, width=20, textvariable=book_serial_number).place(x=270, y=98)

        Button(order_book_screen, text="Order Book", bg="orange",
               command=lambda: Book.get_book(username_verify.get(), book_serial_number.get())).place(x=400, y=95)

        Label(order_book_screen, anchor="center", font=("Helvetica", 12), fg='blue', text=f"Search books:").place(x=20,
                                                                                                                  y=130)

        Label(order_book_screen, text="Filter by book's Author: ").place(x=20, y=160)
        Entry(order_book_screen, width=20, textvariable=author_name).place(x=170, y=160)

        Label(order_book_screen, text="Filter by course").place(x=20, y=190)

        selected_course = StringVar(None, "All")

        place_x = 20
        Radiobutton(order_book_screen, text=f"All", value=f"All", variable=selected_course).place(
            x=place_x,
            y=210)
        place_x += 90

        for course in main_dictionary_json["Courses"]:
            Radiobutton(order_book_screen, text=f"{course}", value=f"{course}", variable=selected_course).place(
                x=place_x,
                y=210)
            place_x += 90

        Button(order_book_screen, text="Search ", height='2', width='30', bg="blue",
               command=lambda: get_books_list_by_course_filter(self, username_verify.get(), selected_course.get(),
                                                               author_name.get())).place(x=300, y=550)

        img = (Image.open(r".\images\back_to_menu_image.png"))
        resized_image = img.resize((50, 50), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(resized_image)
        Label(order_book_screen, text=f"Back to Menu").place(x=650, y=10)
        Button(order_book_screen, text=f"Back to Menu", image=self.new_image,
               command=lambda: close_profile_window(order_book_screen)).place(x=660, y=30)

    def destroy(self):
        order_book_screen().destroy()


def get_books_list_by_course_filter(self, username, selected_course, author_name):
    main_dictionary_json = json.load(open('main_dictionary.json'))
    order_book_screen.destroy()
    self.__init__()
    selected_course = selected_course
    book_list_filter = Book.get_books_list_by_course_filter(username, selected_course, author_name)
    Label(order_book_screen, fg='blue', text=f"Books of {selected_course} : ").place(x=10, y=230)
    place_y = 260
    for serial_number_book in book_list_filter:
        Button(order_book_screen,
               text=f"Serial Number : {serial_number_book} ,Book Name: {book_list_filter[serial_number_book]['name']} "
                    f",Author: {book_list_filter[serial_number_book]['author']}, "
                    f"Inventory: {book_list_filter[serial_number_book]['inventory_quantity']}",
               command=lambda serial_number_book=serial_number_book: [Book.get_book(username_verify.get(),
                                                                                    serial_number_book),
                                                                      get_books_list_by_course_filter(self, username,
                                                                                                      selected_course,
                                                                                                      author_name)]).place(
            x=10,
            y=place_y)
        place_y += 30

    back_to_menu(order_book_screen)


def my_profile_screen():
    profile_screen = Toplevel(menu_screen)
    init_screen_setting(profile_screen, "780x620", "Profile")

    Label(profile_screen, anchor="center", font=("Helvetica", 14), bg='yellow',
          text="My Profile").place(x=340, y=20)
    profile_image = ImageTk.PhotoImage(
        (Image.open(r".\images\profile_image.png")).resize((70, 70), Image.ANTIALIAS))
    Label(profile_screen, image=profile_image).place(x=20, y=20)

    Label(profile_screen, text=f"ID: {main_dictionary_json['Users'][username_verify.get()]['id']}",
          width='30').place(x=280, y=210)
    Label(profile_screen, text=f"First Name: {main_dictionary_json['Users'][username_verify.get()]['first_name']}",
          width='30').place(x=280, y=240)
    Label(profile_screen, text=f"Last Name: {main_dictionary_json['Users'][username_verify.get()]['last_name']}",
          width='30').place(x=280, y=270)
    Label(profile_screen, text=f"Date of birth : {main_dictionary_json['Users'][username_verify.get()]['date']}",
          width='30').place(x=280, y=300)
    Label(profile_screen, text=f"Username : {username_verify.get()}",
          width='30').place(x=280, y=330)
    Label(profile_screen, text=f"Password : {main_dictionary_json['Users'][username_verify.get()]['password']}",
          width='30').place(x=280, y=360)
    course_list_type = ''
    if main_dictionary_json['Users'][username_verify.get()]['is_student']:
        Label(profile_screen, text=f"Position : Student", width='30').place(x=280, y=390)
        course_list_type = 'register_course_list'
    else:
        Label(profile_screen, text=f"Position : Lecturer", width='30').place(x=280, y=390)
        course_list_type = 'teach_course_list'
    place_x = 10
    Label(profile_screen, fg='blue', text=f"My Courses:").place(x=10, y=420)
    for course in main_dictionary_json['Users'][username_verify.get()][course_list_type]:
        Label(profile_screen, text=f"{course}").place(x=place_x, y=440)
        place_x += 100
    place_x = 10
    Label(profile_screen, fg='blue', text=f"My Books:").place(x=10, y=470)
    for book in main_dictionary_json['Users'][username_verify.get()]['book_list']:
        Label(profile_screen,
              text=f"{book} : {main_dictionary_json['Users'][username_verify.get()]['book_list'][book]['name']} ").place(
            x=place_x, y=490)
        place_x += 150

    back_to_menu(profile_screen)
    profile_screen.mainloop()


def close_profile_window(window):
    window.destroy()


def main_screen():
    global welcome_screen
    global main_dictionary_json
    main_dictionary_path = open('main_dictionary.json')
    main_dictionary_json = json.load(main_dictionary_path)
    welcome_screen = Tk()
    init_screen_setting(welcome_screen, "500x300", "Menu")
    Label(text="Welcome To The Library Program").pack(pady=10)
    Label(text="", height='2', width='30')
    Button(text="Login ", height='2', width='30', bg="blue", command=login).pack()
    Label(text="", height='2', width='30').pack()
    Button(text="register", height='2', width='30', bg="green", command=register_user_screen).pack()
    welcome_screen.mainloop()

    global menu_screen
    menu_screen = Tk()
    init_screen_setting(menu_screen, "780x620", "Menu")
    img = (Image.open(".\images\librery_image.png"))
    resized_image = img.resize((800, 605), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    my_label = Label(menu_screen, image=new_image)
    my_label.pack()
    design_menu_screen()

    def my_time():
        time_string = strftime('%H:%M:%S\n%x')
        l1.config(text=time_string)
        l1.after(1000, my_time)  # time delay of 1000 milliseconds

    my_font = ('times', 14, 'bold')  # display size and style

    l1 = Label(menu_screen, font=my_font, bg='yellow')
    l1.place(x=10, y=10)

    my_time()

    menu_screen.mainloop()


def init_screen_setting(screen_name, size, title):
    screen_name.geometry("+{}+{}".format(int(screen_name.winfo_screenwidth() / 3 - screen_name.winfo_reqwidth() / 2),
                                         int(screen_name.winfo_screenheight() / 5 - screen_name.winfo_reqheight() / 2)))
    screen_name.geometry(size)
    screen_name.title(title)


def refref_db(self, screen_name):
    main_dictionary_json = json.load(open('main_dictionary.json'))
    screen_name.destroy()
    self.__init__()


main_screen()
