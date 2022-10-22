import datetime
import pymysql as pm
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import *
import re

class Draw():
    root = Tk()
    root.title("Employee Crud App")
    p = Label(root, text='List Of Employee', height="20", width="40", bg='#145660', fg='white',
              font=('Helvetica', '18', 'bold', 'italic'))
    p.place(x=470, y=90)
    root.configure(bg='#145660')
    root.geometry('1920x1080')
    r = Listbox(root, width='73', height='13', font=('Helvetica', '15'))
    r.place(x=370, y=400)
    s1 = Entry(root, bd=5, width='52', font=('Helvetica', '19'))
    s1.place(x=400, y=250)

    def __init__(self):
        self.searchall()
        q = Label(self.root, text='Enter Emp ID :', bg='#145660', fg='white', font=('Helvetica', '15', 'bold'))
        q.place(x=400, y=220)

        butt3 = Button(self.root, text="Search>>", bg="red",command=self.search, padx=25, pady=5, bd=5, fg='white',
                       font=('Helvetica', '10', 'bold'))
        butt3.place(x=610, y=305)
        but = Button(self.root, text="Edit Employee>>", bg="red",command=self.updated, padx=55, pady=10, bd=7, fg='white',
                     font=('Helvetica', 12, 'bold'))
        but.place(x=950, y=20)
        butt1 = Button(self.root, text="Add New Employee>>", bg="red",command=self.insert, padx=40, pady=10, bd=7, fg='white',
                       font=('Helvetica', 12, 'bold'))
        butt1.place(x=370, y=20)
        butt4 = Button(self.root, text="Delete>>", bg="red", padx=25, pady=5, bd=5, fg='white',
                       font=('Helvetica', '10', 'bold'), command=self.delete)
        butt4.place(x=790, y=305)
        self.root.mainloop()



    def insert(self):
            # root = Tk()
            # root.title("2")
            #
            # label1 = Label(root,text='Name:').grid(row=0, column=0, padx=5, pady=5)
            # label2 = Label(root,text='Email:').grid(row=2, column=0, padx=5, pady=5)
            # label3 = Label(root,text='Password:').grid(row=5, column=0, padx=5, pady=5)
            # label4 = Label(root,text='Confirm Password:').grid(row=6, column=0, padx=5, pady=5)
            #
            # self.email_entry = Entry(root, width=50)
            # self.name_entry = Entry(root, width=50)
            # self.password_entry = Entry(root, show="*", width=50)
            # self.confirmpassword = Entry(root, show="*", width=50)
            #
            # self.name_entry.grid(row=0, column=1, columnspan=2, padx=50, pady=20)
            # self.email_entry.grid(row=2, column=1, columnspan=2, padx=50, pady=20)
            # self.password_entry.grid(row=5, column=1, columnspan=2, padx=50, pady=30)
            # self.confirmpassword.grid(row=6, column=1, columnspan=2, padx=50, pady=20)
            #
            # emailvalid = (root.register(self.validate), '%P')
            # emailinvalid = (root.register(self.on_invalid),)
            # namevalid = (root.register(self.containsNumber), '%P')
            # nameinvalid = (root.register(self.name_invalid),)
            # passvalid = (root.register(self.validatepassword), '%P')
            # passinvalid = (root.register(self.password_invalid),)
            #
            # self.email_entry.config(validate='focusout', validatecommand=emailvalid, invalidcommand=emailinvalid)
            # self.name_entry.config(validate='focusout', validatecommand=namevalid, invalidcommand=nameinvalid)
            # self.password_entry.config(validate='focusout', validatecommand=passvalid, invalidcommand=passinvalid)
            #
            # self.label_error = Label(root, foreground='red')
            # self.label_error3 = Label(root, foreground='red')
            # self.label_error4 = Label(root, foreground='red')
            #
            # self.label_error.grid(row=1, column=1, sticky=tk.W, padx=15)
            # self.label_error3.grid(row=3, column=1, sticky=tk.W, padx=15)
            # self.label_error4.grid(row=7, column=1, sticky=tk.W, padx=5)
            #
            # self.send_button = Button(root, text='Insert',command=self.create).grid(row=1, column=5, padx=5)
            # # self.send_button = Button(root, text='Search'.grid(row=2, column=5, padx=5)
            # self.send_button = Button(root,text='Clear', command=self.clearform).grid(row=3, column=5, padx=5)
            #
            # root.mainloop()
            root = Tk()
            root.title("update Employee")
            root.geometry("1530x1080")
            p = Label(root, height='22', width="100", bg='#636466', font=('Helvetica', '20', 'italic'))
            p.pack()

            q = Label(root, height="2", width="12", bg='#636466', fg="white", text="Email:",
                      font=('Helvetica', '18', 'italic'))
            q.place(x=400, y=38)
            self.email_entry = Entry(root, bd=5, width='45', font=('Helvetica', '19'))
            self.email_entry.place(x=611, y=50)
            #########
            q1 = Label(root, height="2", width="12", bg='#636466', fg="white", text="Password:",
                       font=('Helvetica', '18', 'italic'))
            q1.place(x=400, y=138)
            self.password_entry = Entry(root, bd=5, width='45', font=('Helvetica', '19'))
            self.password_entry.place(x=611, y=150)

            ####
            q2 = Label(root, height="2", width="12", bg='#636466', fg="white", text="ConfirmPass:",
                       font=('Helvetica', '17', 'italic'))
            q2.place(x=400, y=238)
            self.confirmpassword = Entry(root, bd=5, width='45', font=('Helvetica', '19'))
            self.confirmpassword.place(x=611, y=250)
            ##
            q3 = Label(root, height="2", width="12", bg='#636466', fg="white", text="Name :",
                       font=('Helvetica', '18', 'italic'))
            q3.place(x=400, y=338)
            self.name_entry = Entry(root, bd=5, width='45', font=('Helvetica', '19'))
            self.name_entry.place(x=611, y=350)

            ##
            butto2 = Button(root, text="Save>>", command=self.create, bg="red", padx=50, pady=10, fg='white',
                            font=('Helvetica', '8', 'bold'))
            butto2.place(x=1080, y=580)
            butto3 = Button(root, text="Quit", command=root.destroy, bg="red", padx=50, pady=10, fg='white',
                            font=('Helvetica', '8', 'bold'))
            butto3.pack(pady=25)
            root.configure(bg="black")
            emailvalid = (root.register(self.validate), '%P')
            emailinvalid = (root.register(self.on_invalid),)
            namevalid = (root.register(self.containsNumber), '%P')
            nameinvalid = (root.register(self.name_invalid),)
            passvalid = (root.register(self.validatepassword), '%P')
            passinvalid = (root.register(self.password_invalid),)
            cpassvalid = (root.register(self.cvalidatepassword), '%P')
            cpassinvalid = (root.register(self.cpassword_invalid),)

            self.email_entry.config(validate='focusout', validatecommand=emailvalid, invalidcommand=emailinvalid)
            self.name_entry.config(validate='focusout', validatecommand=namevalid, invalidcommand=nameinvalid)
            self.password_entry.config(validate='focusout', validatecommand=passvalid, invalidcommand=passinvalid)
            self.confirmpassword.config(validate='focusout', validatecommand=cpassvalid, invalidcommand=cpassinvalid)

            self.label_error = Label(root, foreground='red')
            self.label_error3 = Label(root, foreground='red')
            self.label_error4 = Label(root, foreground='red')
            self.label_error5 = Label(root, foreground='red')

            self.label_error.place(x=611, y=400)

            self.label_error3.place(x=611, y=100)
            self.label_error5.place(x=611, y=300)

            #########
            self.label_error4.place(x=611, y=200)
            #########
            root.mainloop()

    def updated(self):
            root = Tk()
            root.title("update Employee")
            root.geometry("1530x1080")
            p = Label(root, height='22', width="100", bg='#636466', font=('Helvetica', '20', 'italic'))
            p.pack()

            q = Label(root, height="2", width="12", bg='#636466', fg="white", text="Email:",
                      font=('Helvetica', '18', 'italic'))
            q.place(x=400, y=38)
            self.email_entry = Entry(root, bd=5, width='45', font=('Helvetica', '19'))
            self.email_entry.place(x=611, y=50)
            #########
            q1 = Label(root, height="2", width="12", bg='#636466', fg="white", text="Password:",
                       font=('Helvetica', '18', 'italic'))
            q1.place(x=400, y=138)
            self.password_entry = Entry(root, bd=5, width='45', font=('Helvetica', '19'))
            self.password_entry.place(x=611, y=150)

            ####
            q2 = Label(root, height="2", width="12", bg='#636466', fg="white", text="ConfirmPass:",
                       font=('Helvetica', '17', 'italic'))
            q2.place(x=400, y=238)
            self.confirmpassword = Entry(root, bd=5, width='45', font=('Helvetica', '19'))
            self.confirmpassword.place(x=611, y=250)
            ##
            q3 = Label(root, height="2", width="12", bg='#636466', fg="white", text="Name :",
                       font=('Helvetica', '18', 'italic'))
            q3.place(x=400, y=338)
            self.name_entry = Entry(root, bd=5, width='45', font=('Helvetica', '19'))
            self.name_entry.place(x=611, y=350)

            ##
            butto2 = Button(root, text="Save>>",command=self.update, bg="red", padx=50, pady=10, fg='white',
                            font=('Helvetica', '8', 'bold'))
            butto2.place(x=1080, y=580)
            butto3 = Button(root, text="Quit", command=root.destroy, bg="red", padx=50, pady=10, fg='white',
                            font=('Helvetica', '8', 'bold'))
            butto3.pack(pady=25)
            root.configure(bg="black")
            emailvalid = (root.register(self.validate), '%P')
            emailinvalid = (root.register(self.on_invalid),)
            namevalid = (root.register(self.containsNumber), '%P')
            nameinvalid = (root.register(self.name_invalid),)
            passvalid = (root.register(self.validatepassword), '%P')
            passinvalid = (root.register(self.password_invalid),)
            cpassvalid = (root.register(self.cvalidatepassword), '%P')
            cpassinvalid = (root.register(self.cpassword_invalid),)


            self.email_entry.config(validate='focusout', validatecommand=emailvalid, invalidcommand=emailinvalid)
            self.name_entry.config(validate='focusout', validatecommand=namevalid, invalidcommand=nameinvalid)
            self.password_entry.config(validate='focusout', validatecommand=passvalid, invalidcommand=passinvalid)
            self.confirmpassword.config(validate='focusout', validatecommand=cpassvalid, invalidcommand=cpassinvalid)

            self.label_error = Label(root, foreground='red')
            self.label_error3 = Label(root, foreground='red')
            self.label_error4 = Label(root, foreground='red')
            self.label_error5 = Label(root, foreground='red')

            self.label_error.place(x=611, y=400)

            self.label_error3.place(x=611, y=100)
            self.label_error5.place(x=611, y=300)

            #########
            self.label_error4.place(x=611, y=200)
            #########

            for i in self.r.curselection():
                self.email_entry.insert(0, self.r.get(i)[3])
                self.email=self.r.get(i)[3]
                self.name_entry.insert(0, self.r.get(i)[1])
                self.name = self.r.get(i)[1]
                self.password_entry.insert(0, self.r.get(i)[4])
                self.password = self.r.get(i)[4]
                self.confirmpassword.insert(0, self.r.get(i)[4])
            root.mainloop()


    def clearform(self):
        self.label_error4['text'] = ''
        self.label_error3['text'] = ''
        self.label_error['text'] = ''
        self.email = ''
        self.name = ''
        self.password = ''
        self.email_entry['foreground'] = 'black'
        self.name_entry['foreground'] = 'black'
        self.password_entry['foreground'] = 'black'
        self.password_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')

    def validatepassword(self, value):

        pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        if re.fullmatch(pattern, value) is None:
            return False

        self.show_message()
        self.label_error4['text'] = ''
        self.password_entry['foreground'] = 'black'
        self.password = self.password_entry.get()
        return True

    def password_invalid(self):
        self.show_message('Minimum eight characters, at least one letter and one number', 'red')

    def cvalidatepassword(self, value):

        if self.password!=value:
            return False

        self.show_message()
        self.label_error5['text'] = ''
        self.confirmpassword['foreground'] = 'black'
        return True

    def cpassword_invalid(self):
        self.show_message('Identical Password', 'red')






    def containsNumber(self, value):
        pattern = r'^[A-Za-z -]*$'
        if re.fullmatch(pattern, value) is None :
            return False
        else:
            self.show_message()
            self.label_error['text'] = ''
            self.name_entry['foreground'] = 'black'
            self.name = self.name_entry.get()
            return True

    def name_invalid(self):
        self.show_message('Can,t add Number in Name', 'red')

    def validate(self, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value) is None or len(value) < 1:
            return False

        self.show_message()
        self.label_error3['text'] = ''
        self.email_entry['foreground'] = 'black'
        self.email = self.email_entry.get()
        return True

    def on_invalid(self):
        self.show_message('Please enter a valid email', 'red')

    def show_message(self, error='', color='black'):
        if error == 'Please enter a valid email':
            self.label_error3['text'] = error
            self.email_entry['foreground'] = color
        elif error == 'Can,t add Number in Name':
            self.label_error['text'] = error
            self.name_entry['foreground'] = color
        elif error == 'Identical Password':
            self.label_error5['text'] = error
            self.confirmpassword['foreground'] = color
        elif error == 'Minimum eight characters, at least one letter and one number':
            self.label_error4['text'] = error
            self.password_entry['foreground'] = color


