from tkinter import *
from student import Student
from book import Book
from PIL import ImageTk, Image
import json


def register_user():
    username_info = username.get()
    password_info = password.get()
    if username_info in main_dictionary_json['Users']:
        Label(register_screen, text="User already exist", font="green", height='2', width='30').pack()
        return False
    Student.add_student_to_list(username_info, username_info, username_info, password_info, id=1234, student_id=4,
                                date="03.03.1994")
    Button(register_screen, text=f"registration success!", font="green", height='2', width='30').pack()


def register_user_screen():
    global register_screen
    register_screen = Toplevel(welcome_screen)
    register_screen.geometry("350x250")
    register_screen.title("Register")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="please enter the given given information", height="2", width="30")
    Label(register_screen, text="", height='2', width='30').pack()
    Label(register_screen, text="username * ", height='2', width='30').pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen, text="password *", height='2', width='30').pack()
    password_entry = Entry(register_screen, textvariable=password)
    password_entry.pack()
    Label(register_screen, text="", height='2', width='30').pack()
    Button(register_screen, text="submit", height='2', width='30', command=register_user).pack()


def add_book(serial_num, book_name, author_name, inventory_quantity, useful_courses_list):
    Book.add_book_to_list(serial_num, book_name, author_name, inventory_quantity, useful_courses_list)
    Label(add_books_screen, text=f"registration success!", width=30, height='2').place(x=210,y=360)


def add_book_screen():
    global add_books_screen
    add_books_screen = Toplevel(menu_screen)
    add_books_screen.geometry("600x400")
    add_books_screen.title("Add Book To Library")
    book_name = StringVar()
    serial_num = StringVar()
    author_name = StringVar()
    inventory_quantity = IntVar()

    # row 0
    Label(add_books_screen, text="", height='2', width='30').grid(row=0, column=0)
    Label(add_books_screen, text="Please enter book's details", height="2").grid(row=0, column=1)
    Label(add_books_screen, text="", height='2', width='30').grid(row=0, column=2)

    # row 1
    empty_row(1)
    # row 2
    Label(add_books_screen, text="book name :", height='2').grid(row=2, column=0)
    Entry(add_books_screen, textvariable=book_name).grid(row=2, column=1)
    Label(add_books_screen, text="", height='2', width='30').grid(row=2, column=2)
    # row4
    Label(add_books_screen, text="  Serial Number :", height='2').grid(row=4, column=0)
    Entry(add_books_screen, textvariable=serial_num).grid(row=4, column=1)

    # row 6
    Label(add_books_screen, text="Author :", height='2').grid(row=6, column=0)
    Entry(add_books_screen, textvariable=author_name).grid(row=6, column=1)

    # row 8
    Label(add_books_screen, text="Inventory quantity:", height='2').grid(row=8, column=0)
    Entry(add_books_screen, textvariable=inventory_quantity).grid(row=8, column=1)

    # checkbox
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()
    Checkbutton(add_books_screen, text="Algorithm", variable=v1).place(x=100, y=200)
    Checkbutton(add_books_screen, text="Physics", variable=v2).place(x=190, y=200)
    Checkbutton(add_books_screen, text="Math", variable=v3).place(x=280, y=200)
    Checkbutton(add_books_screen, text="English", variable=v4).place(x=370, y=200)

    Button(add_books_screen, text="submit", height='2', width='30',
           command=lambda: add_book(serial_num.get(), book_name.get(), author_name.get(),
                                    inventory_quantity.get(),
                                    get_useful_courses_list(v1.get(), v2.get(), v3.get(), v4.get()))).place(x=200,
                                                                                                            y=300)
    Button(add_books_screen, text=f"Back to Menu", height='2',
           command=lambda: close_profile_window(add_books_screen)).place(x=500, y=350)


def get_useful_courses_list(v1, v2, v3, v4):
    useful_courses_list = []
    set_useful_courses_list_by_value(useful_courses_list, v1, "Algorithm")
    set_useful_courses_list_by_value(useful_courses_list, v2, "Physics")
    set_useful_courses_list_by_value(useful_courses_list, v3, "Math")
    set_useful_courses_list_by_value(useful_courses_list, v4, "English")
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
    # dictionary_users_path = open('main_dictionary.json')
    # dictionary_users = json.load(dictionary_users_path)
    # row 0
    Label(text="", height='2', width='30').grid(row=0, column=0)
    Label(text=f"Welcome {username_verify.get()} To Our Library Program", background='yellow',
          font=("Helvetica", 14)).grid(row=0, column=1)
    Label(text="", height='2', width='30').grid(row=0, column=2)
    # row 1
    Label(text="", height='2', width='30').grid(row=1, column=0)
    Label(text="Lets have fun! ", font=("Helvetica", 11), height='2', width='30').grid(row=1, column=1)
    Label(text=f"ID: {main_dictionary_json['Users'][username_verify.get()]['id']}", height='2', width='30').grid(row=1,
                                                                                                                 column=2)
    # row 2
    Button(text="Order Book", font=("Helvetica", 14), height='2', width=17, bg="orange", command=login).grid(row=2,
                                                                                                             column=0)
    Button(text="Search For Book", font=("Helvetica", 14), height='2', width=17, bg="green").grid(
        row=2, column=1)
    Button(text="My Profile", font=("Helvetica", 14), height='2', width=17, bg="blue", command=my_profile_screen).grid(
        row=2, column=2)
    # row 3
    empty_row(3)
    # row 4
    empty_row(4)
    # row 5
    Button(text="Return Book", font=("Helvetica", 14), height='2', width='17', bg="green").grid(
        row=5, column=0)
    Button(text="Pay Fee", font=("Helvetica", 14), height='2', width='17', bg="green").grid(
        row=5, column=1)
    Button(text="Register to Course", font=("Helvetica", 14), height='2', width='17', bg="green").grid(row=5, column=2)
    # row 6
    empty_row(6)
    # row 7
    empty_row(7)
    # row 8
    Button(text="Add Book", font=("Helvetica", 14), height='2', width='17', bg="green", command=add_book_screen).grid(
        row=8, column=0)
    Button(text="Add Course", font=("Helvetica", 14), height='2', width='17', bg="green").grid(
        row=8, column=1)
    Button(text="Extending book loan", font=("Helvetica", 14), height='2', width='17', bg="green").grid(row=8, column=2)
    # row 9
    empty_row(9)
    # row 10
    empty_row(10)
    # row 11
    Label(text="", height='2', width='30').grid(row=11, column=0)
    Label(text="", height='2', width='30').grid(row=11, column=1)
    Button(text="Exit", font=("Helvetica", 14), height='2', width='17', bg="red",
           command=exit).grid(row=12, column=2)


def empty_row(row):
    Label(text="", height='2', width='30').grid(row=row, column=0)
    Label(text="", height='2', width='30').grid(row=row, column=1)
    Label(text="", height='2', width='30').grid(row=row, column=2)


def my_profile_screen():
    global profile_screen
    profile_screen = Toplevel(menu_screen)
    profile_screen.geometry("500x600")
    profile_screen.title("Profile")
    photo = PhotoImage(file="C:\omri\year D\pythonProject\profile_image.png")
    photoimage = photo.subsample(3, 3)
    my_label = Label(profile_screen, image=photoimage)
    my_label.pack(pady=10)

    Label(profile_screen, text=f"Hi {username_verify.get()}! ", height='2', width='30').pack()
    Label(profile_screen, text=f"ID: {main_dictionary_json['Users'][username_verify.get()]['id']}", height='2',
          width='30').pack()
    Label(profile_screen, text=f"First Name: {main_dictionary_json['Users'][username_verify.get()]['first_name']}",
          height='2',
          width='30').pack()
    Label(profile_screen, text=f"Last Name: {main_dictionary_json['Users'][username_verify.get()]['last_name']}",
          height='2',
          width='30').pack()
    Label(profile_screen, text=f"Date of birth : {main_dictionary_json['Users'][username_verify.get()]['date']}",
          height='2',
          width='30').pack()
    Label(profile_screen, text=f"Password {main_dictionary_json['Users'][username_verify.get()]['password']}",
          height='2',
          width='30').pack()
    if main_dictionary_json['Users'][username_verify.get()]['is_student']:
        Label(profile_screen, text=f"Student at Ruppin", height='2', width='30').pack()
        Label(profile_screen, fg='blue', text=f"My Courses:", height='2', width='30').pack()
        for course in main_dictionary_json['Users'][username_verify.get()]['register_course_list']:
            Label(profile_screen, text=f"{course}", height='2', width='30').pack()

    else:
        Label(profile_screen, text=f"lecturer at Ruppin", height='2', width='30').pack()
    Label(profile_screen, text="", height='2', width='30').pack()
    Label(profile_screen, text="", height='2', width='30').pack()
    Button(profile_screen, text="Back to menu", height="2", bg='blue', width="30",
           command=lambda: close_profile_window(profile_screen)).pack()
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
    welcome_screen.geometry("300x250")
    Label(text="Welcome To The Library Program").pack(pady=10)
    Label(text="", height='2', width='30')
    Button(text="Login ", height='2', width='30', bg="blue", command=login).pack()
    Label(text="", height='2', width='30').pack()
    Button(text="register", height='2', width='30', bg="green", command=register_user_screen).pack()
    welcome_screen.mainloop()
    global menu_screen
    menu_screen = Tk()
    menu_screen.title("Menu")
    menu_screen.geometry("780x590")
    design_menu_screen()
    menu_screen.mainloop()


main_screen()
