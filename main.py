from tkinter import *

a = {}



def error_window(error_name):
    errno = Tk()
    polin = Label(errno, text=error_name, fg='red')
    polin.pack()
    errno.mainloop()

def main_jopa():
    tk_main = Tk()
    tk_main.geometry('100x100')
    tk_main.overrideredirect(True)
    tk_main.attributes('-topmost', True)
    tk_main.eval('tk::PlaceWindow . center')
    tk_main.resizable(False, False)


    log_btn = Button(tk_main, text='login', command=log_in_window)
    log_btn.pack()
    reg_btn = Button(tk_main, text='register', command=register_window)
    reg_btn.pack()
    reg_btn = Button(tk_main, text='INFO', command=info)
    reg_btn.pack()

    tk_main.mainloop()

def info():
    tk_info = Tk()
    tk_info.resizable(False, False)

    information = Label(tk_info, text='щоб вимкнути вірусну програму введіть \n Name admin\n і пароль адміня в полі Password ')
    information.pack()

    tk_info.mainloop()



class log_in_window():
    def __init__(self):
        self.tk_login_window = Tk()
        self.tk_login_window.geometry('185x65')
        self.tk_login_window.resizable(False, False)

        self.rem_name = StringVar()
        self.rem_password = StringVar()


        user_info = Frame(self.tk_login_window)
        user_info.pack(anchor='nw', fill=X)

        Name = Label(user_info, text="Name")
        Name.grid(row=1, column=1, padx=2)

        Password = Label(user_info, text="Password")
        Password.grid(row=2, column=1, padx=2)

        Name_inp = Entry(user_info, textvariable=self.rem_name)
        Name_inp.grid(row=1, column=2, padx=2)

        Password_inp = Entry(user_info, textvariable=self.rem_password)
        Password_inp.grid(row=2, column=2, padx=2)

        Submit_btn = Button(self.tk_login_window, text='Submit', command=self.log_password_check)
        Submit_btn.pack(anchor='se')

        self.tk_login_window.mainloop()

    def log_password_check(self):
        name = self.rem_name.get()
        p = self.rem_password.get()

        print(type(p))
        if name in a.keys():
            if p == a[name]:
                self.tk_login_window.quit()


class register_window():
    def __init__(self):
        self.tk_register_window = Tk()
        self.tk_register_window.geometry('185x105')
        self.tk_register_window.resizable(False, False)

        self.rem_name = StringVar()
        self.rem_password = StringVar()
        self.rem_password1 = StringVar()

        user_info = Frame(self.tk_register_window)
        user_info.pack(anchor='nw', fill=X)

        Name = Label(user_info, text="Name")
        Name.grid(row=1, column=1, padx=2)

        Password = Label(user_info, text="Password")
        Password.grid(row=2, column=1, padx=2)

        Password1 = Label(user_info, text="Password")
        Password1.grid(row=3, column=1, padx=2)

        Name_inp = Entry(user_info, textvariable=self.rem_name)
        Name_inp.grid(row=1, column=2, padx=2)

        Password_inp = Entry(user_info, textvariable=self.rem_password)
        Password_inp.grid(row=2, column=2, padx=2)

        Password1_inp = Entry(user_info, textvariable=self.rem_password1)
        Password1_inp.grid(row=3, column=2, padx=2)

        Submit_btn = Button(self.tk_register_window, text='Submit', command=self.reg_password_check)
        Submit_btn.pack(anchor='se')

        self.tk_register_window.mainloop()

    def reg_password_check(self):
        name = self.rem_name.get()
        p = self.rem_password.get()
        p1 = self.rem_password1.get()

        if name == '' or p == '' or p1 == '':
            error_window('ERROR_EMPTY_PLACE')
        elif p1 != p:
            error_window('ERROR_PASSWORD_DIFFERENT')
        else:
            a[name] = p
            self.tk_register_window.quit()

if __name__ == "__main__":
    main_jopa()




