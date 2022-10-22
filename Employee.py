from Draws import *
class Employee(Draw):
    name = ''
    email = ''
    password = ''
    date = datetime.date.today()

    def __init__(self):
        super().__init__()


    def connection(self):
        try:
            con = pm.connect(host="localhost", database='crudemp', user='root', password='')
            cursor = con.cursor()
            return cursor, con
        except:
            raise ValueError('Connection Failed')


    def create(self):
        con = self.connection()[1]
        cursor = con.cursor()
        if self.email == '' or self.name == '' or self.password == '':
            pass
        else:
            query_insert = "insert into employee(firstname,email,password,date) values('%s','%s','%s','%s')" % (
            self.name, self.email, self.password, self.date)
            print( self.name, self.email, self.password, self.date)

            cursor.execute(query_insert)
            print(con.commit())
            messagebox.showinfo("Successfully", "Inserted successful")
            self.clearform()

    def searchall(self):
        con = self.connection()[1]
        cursor = con.cursor()
        searchquery = "select * from employee "
        cursor.execute(searchquery)

        data = cursor.fetchall()
        for x in data:
            self.r.insert(END, x)
        con.commit()

    def search(self):
        self.r.delete(0, tk.END)
        con = self.connection()[1]
        cursor = con.cursor()
        try:
            searchquery = "select * from employee where id={}".format(int(self.s1.get()))
            cursor.execute(searchquery)
            data = cursor.fetchall()
            for x in data:
                self.r.insert(END, x)
            con.commit()
        except ValueError:
                self.searchall()


    def delete(self):
        con = self.connection()[1]
        cursor = con.cursor()
        for i in self.r.curselection():
            delete = "delete from employee where id={}".format(self.r.get(i)[0])
            cursor.execute(delete)
            con.commit()
            x=self.r.delete(i)[0]

    def update(self):
        con = self.connection()[1]
        cursor = con.cursor()
        if self.email == '' or self.name == '' or self.password == '':
            pass
        else:
            for i in self.r.curselection():
                cursor.execute("""
                   UPDATE employee
                   SET firstname=%s, email=%s, password=%s
                   WHERE id=%s
                """, (self.name_entry.get(),self.email_entry.get(), self.password_entry.get(), self.r.get(i)[0]))
                con.commit()

            self.clearform()












