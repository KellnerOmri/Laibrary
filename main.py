# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    from tkinter import *

    window = Tk()
    # add widgets here
    window.title('Welcome To The Best Library!')
    window.geometry("700x700+500+500")
    student_button = Button(window, text="sign as student", fg='blue')
    student_button.place(x=100, y=250)
    lecture_button = Button(window, text="sign as lecture", fg='red')
    lecture_button.place(x=250, y=250)
    window.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
