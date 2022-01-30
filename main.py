from tkinter import *

import person
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
        Student.add_student_to_list(register_person, get_useful_courses_list(register_course_list))

    Button(register_screen, text=f"registration success!", font="green", height='2', width='30').pack()


def register_user_screen():
    global register_screen
    register_screen = Toplevel(welcome_screen)
    register_screen.geometry("350x450")
    register_screen.title("Register")
    global username
    global password
    global username_entry
    global password_entry
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
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.place(x=160, y=50)
    Label(register_screen, text="Password : ", width='30').place(x=10, y=80)
    password_entry = Entry(register_screen, textvariable=password)
    password_entry.place(x=160, y=80)

    Label(register_screen, text="ID : ", width='30').place(x=10, y=110)
    id_entry = Entry(register_screen, textvariable=register_person.id)
    id_entry.place(x=160, y=110)

    Label(register_screen, text="First Name : ", width='30').place(x=10, y=140)
    first_name_entry = Entry(register_screen, textvariable=register_person.first_name)
    first_name_entry.place(x=160, y=140)

    Label(register_screen, text="Last Name : ", width='30').place(x=10, y=170)
    last_name_entry = Entry(register_screen, textvariable=register_person.last_name)
    last_name_entry.place(x=160, y=170)

    Label(register_screen, text="Date of birth : ", width='30').place(x=10, y=170)
    date_entry = Entry(register_screen, textvariable=register_person.date)
    date_entry.place(x=160, y=170)

    r1 = Radiobutton(register_screen, text='Student', value=True, variable=is_student)
    r1.place(x=30, y=200)
    r2 = Radiobutton(register_screen, text='Lecturer', value=False, variable=is_student)
    r2.place(x=160, y=200)

    Label(register_screen, text="Select witch courses would you like to register : ").place(x=30, y=240)
    place_y = 240
    register_course_list = dict()
    for course in main_dictionary_json["Courses"]:
        place_y += 30
        register_course_list[course] = IntVar()
        chk = Checkbutton(register_screen, text=f'{course}', variable=register_course_list[course])
        chk.place(x=30, y=place_y)

    Button(register_screen, text="submit", width='30',
           command=lambda: register_user(register_person, register_course_list, is_student)).place(x=60,
                                                                                                   y=place_y + 50)


def add_book(serial_num, book_name, author_name, inventory_quantity, useful_courses_list):
    Book.add_book_to_list(serial_num, book_name, author_name, inventory_quantity, useful_courses_list)
    Label(add_books_screen, text=f"registration success!", width=30, height='2').place(x=210, y=360)


def add_book_screen():
    global add_books_screen
    add_books_screen = Toplevel(menu_screen)
    add_books_screen.geometry("600x400")
    add_books_screen.title("Add Book To Library")
    book_name = StringVar()
    serial_num = StringVar()
    author_name = StringVar()
    inventory_quantity = IntVar()

    Label(add_books_screen, text="Please enter book's details", height="2").place(x=20, y=5)

    Label(add_books_screen, text="book name :").place(x=20, y=40)
    Entry(add_books_screen, textvariable=book_name).place(x=160, y=40)

    Label(add_books_screen, text="  Serial Number :").place(x=20, y=70)
    Entry(add_books_screen, textvariable=serial_num).place(x=160, y=70)

    Label(add_books_screen, text="Author :").place(x=20, y=100)
    Entry(add_books_screen, textvariable=author_name).place(x=160, y=100)

    Label(add_books_screen, text="Inventory quantity:").place(x=20, y=130)
    Entry(add_books_screen, textvariable=inventory_quantity).place(x=160, y=130)

    # checkbox
    Label(add_books_screen, text="Select courses that will use this book from the list:").place(x=20, y=180)
    place_x = 20
    course_list = dict()
    for course in main_dictionary_json["Courses"]:
        course_list[course] = IntVar()
        chk = Checkbutton(add_books_screen, text=f'{course}', variable=course_list[course])
        chk.place(x=place_x, y=200)
        place_x += 90

    Button(add_books_screen, text="submit", height='2', width='30',
           command=lambda: add_book(serial_num.get(), book_name.get(), author_name.get(),
                                    inventory_quantity.get(),
                                    get_useful_courses_list(course_list))).place(x=200,
                                                                                 y=300)
    Button(add_books_screen, text=f"Back to Menu", height='2',
           command=lambda: close_profile_window(add_books_screen)).place(x=500, y=350)


def get_useful_courses_list(course_list):
    useful_courses_list = []
    for course in course_list:
        if course_list[course].get() == 1:
            useful_courses_list.append(course)
    return useful_courses_list


def set_useful_courses_list_by_value(useful_courses_list, v, course):
    if (v == 1):
        useful_courses_list.append(course)
    return useful_courses_list


def login_verify():
    user_name = username_verify.get()
    if user_name in main_dictionary_json['Users']:
        if main_dictionary_json['Users'][user_name]["password"] == password_verify.get():
            welcome_screen.destroy()
        else:
            Label(login_screen, text=f"wrong password", height="2", width="30").pack()
            print("wrong password")
    else:
        Label(login_screen, text=f"User {user_name} not found,please try again", height="2", width="30").pack()
        print("user not found")


def login():
    global login_screen
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    login_screen = Toplevel(welcome_screen)
    login_screen.geometry("500x300")
    login_screen.title("Login")
    Label(login_screen, text="Please enter the information for login ", height='2', width='30').pack()
    Label(login_screen, text="", height='2', width='30').pack()
    Label(login_screen, text="username : ", height='2', width='30').pack()
    username_entry1 = Entry(login_screen, textvariable=username_verify)
    username_entry1.pack()
    Label(login_screen, text="password : ", height='2', width='30').pack()
    password_entry1 = Entry(login_screen, textvariable=password_verify)
    password_entry1.pack()
    Label(login_screen, text="", height='2', width='30').pack()
    Button(login_screen, text="login", height="2", width="30", command=login_verify).pack()


def design_menu_screen():
    Label(text=f"Welcome {username_verify.get()} To Our Library Program", background='yellow',
          font=("Helvetica", 14)).place(x=250, y=20)
    Button(text="Order Book", font=("Helvetica", 14), height='2', width='17', bg="orange",
           command=search_for_book).place(x=120, y=70)

    Button(text="Add Book", font=("Helvetica", 14), height='2', width='17', bg="green", command=add_book_screen).place(
        x=460, y=70)
    Button(text="Return Book", font=("Helvetica", 14), height='2', width='17', bg="green").place(x=120, y=150)
    Button(text="Add Course", font=("Helvetica", 14), height='2', width='17', bg="green").place(x=460, y=150)

    Button(text="Pay Fee", font=("Helvetica", 14), height='2', width='17', bg="green").place(x=120, y=230)

    Button(text="Register to Course", font=("Helvetica", 14), height='2', width='17', bg="green").place(x=460, y=230)
    Button(text="Extending book loan", font=("Helvetica", 14), height='2', width='17', bg="green").place(x=120, y=310)

    Button(text="My Profile", font=("Helvetica", 14), height='2', width='17', bg="blue",
           command=my_profile_screen).place(x=40, y=520)

    Button(text="Exit", font=("Helvetica", 14), height='2', width='17', bg="red",
           command=exit).place(x=540, y=520)


def search_for_book():
    global search_book_screen
    search_book_screen = Toplevel(menu_screen)
    search_book_screen.geometry("500x600")
    search_book_screen.title("Search Book")
    Label(search_book_screen, text=f"Hi {username_verify.get()}! , Enter witch book whould you like to get ").place(
        x=10, y=20)
    search_by_name = Entry(search_book_screen, width=70, textvariable=username_verify)
    search_by_name.place(x=10, y=50)

    Label(search_book_screen, text="Choose course for filter").place(x=10, y=90)
    place_x = 20
    selected_course = StringVar()
    for course in main_dictionary_json["Courses"]:
        rb = Radiobutton(search_book_screen, text=f"{course}", value=f"{course}", variable=selected_course)
        rb.place(x=place_x, y=110)
        place_x += 90

    Button(search_book_screen, text="Search ", height='2', width='30', bg="blue",
           command=lambda: get_books_list_by_course_filter(selected_course.get())).place(x=20, y=400)


def get_books_list_by_course_filter(selected_course):
    book_list_filter = Book.get_books_list_by_course_filter(selected_course)
    place_y = 160
    for book in book_list_filter:
        Button(search_book_screen,
               text=f"Serial Number : {book} ,Book Name: {book_list_filter[book]['name']} "
                    f",Author: {book_list_filter[book]['author']}, "
                    f"Inventory: {book_list_filter[book]['inventory_quantity']}",
               command=lambda: Book.get_book(username_verify.get(), book)).place(x=10, y=place_y)
        place_y += 30


def my_profile_screen():
    global profile_screen
    profile_screen = Toplevel(menu_screen)
    profile_screen.geometry("500x600")
    profile_screen.title("Profile")
    photo = PhotoImage(file=".\images\profile_image.png")
    photoimage = photo.subsample(3, 3)
    my_label = Label(profile_screen, image=photoimage)
    my_label.pack(pady=10)

    Label(profile_screen, text=f"Hi {username_verify.get()}! ", width='30').pack()
    Label(profile_screen, text=f"ID: {main_dictionary_json['Users'][username_verify.get()]['id']}",
          width='30').place(x=140, y=240)
    Label(profile_screen, text=f"First Name: {main_dictionary_json['Users'][username_verify.get()]['first_name']}",
          height='2',
          width='30').place(x=140, y=270)
    Label(profile_screen, text=f"Last Name: {main_dictionary_json['Users'][username_verify.get()]['last_name']}",
          width='30').place(x=140, y=300)
    Label(profile_screen, text=f"Date of birth : {main_dictionary_json['Users'][username_verify.get()]['date']}",
          width='30').place(x=140, y=330)
    Label(profile_screen, text=f"Password {main_dictionary_json['Users'][username_verify.get()]['password']}",
          width='30').place(x=140, y=360)

    if main_dictionary_json['Users'][username_verify.get()]['is_student']:
        Label(profile_screen, text=f"Student at Ruppin", width='30').place(x=140, y=390)
    else:
        Label(profile_screen, text=f"lecturer at Ruppin", width='30').place(x=140, y=390)

    place_x = 10
    Label(profile_screen, fg='blue', text=f"My Courses:").place(x=10, y=420)
    for course in main_dictionary_json['Users'][username_verify.get()]['register_course_list']:
        Label(profile_screen, text=f"{course}").place(x=place_x, y=440)
        place_x += 100
    place_x = 10
    Label(profile_screen, fg='blue', text=f"My Books:").place(x=10, y=470)
    for book in main_dictionary_json['Users'][username_verify.get()]['book_list']:
        Label(profile_screen,
              text=f"{book} : {main_dictionary_json['Users'][username_verify.get()]['book_list'][book]['name']} ").place(
            x=place_x, y=490)
        place_x += 150

    Button(profile_screen, text="Back to menu", bg='blue', width="30",
           command=lambda: close_profile_window(profile_screen)).place(x=140, y=530)
    profile_screen.mainloop()


def close_profile_window(window):
    window.destroy()


def main_screen():
    global welcome_screen
    global main_dictionary_json
    main_dictionary_path = open('main_dictionary.json')
    main_dictionary_json = json.load(main_dictionary_path)
    welcome_screen = Tk()
    welcome_screen.title("Menu")
    welcome_screen.geometry("400x250")
    Label(text="Welcome To The Library Program").pack(pady=10)
    Label(text="", height='2', width='30')
    Button(text="Login ", height='2', width='30', bg="blue", command=login).pack()
    Label(text="", height='2', width='30').pack()
    Button(text="register", height='2', width='30', bg="green", command=register_user_screen).pack()
    welcome_screen.mainloop()
    global menu_screen
    menu_screen = Tk()
    menu_screen.title("Menu")
    menu_screen.geometry("780x620")
    img = (Image.open(".\images\librery_image.png"))
    resized_image = img.resize((800, 605), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    my_label = Label(menu_screen, image=new_image)
    my_label.pack()
    design_menu_screen()
    menu_screen.mainloop()


main_screen()
