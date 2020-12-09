from tkinter import *
import pymysql
import tkinter.messagebox

conn=pymysql.connect(host='localhost',port=3306,user='root',password='yokesh',db='hospital')
c = conn.cursor()

class querypage:

    def __init__(self, master):
        self.master=master
        master.title('Food at Flood - FaF')

        self.left = Frame(master,width=800, height=720, bg='black')
        self.left.pack()

        self.heading = Label(self.left, text="#A_Ray_of_Hope", font=('arial 40 bold'), fg='black', bg='white')
        self.heading.place(x=200, y=0)

        self.name = Label(self.left, text="Name", font=('arial 18 italic'), fg='black', bg='lightgreen')
        self.name.place(x=0, y=150)

        self.phno = Label(self.left, text="Phone Number", font=('arial 18 italic'), fg='black', bg='lightgreen')
        self.phno.place(x=0, y=200)

        self.nop = Label(self.left, text="Number of persons", font=('arial 18 italic'), fg='black', bg='lightgreen')
        self.nop.place(x=0, y=300)

        self.place = Label(self.left, text="Place", font=('arial 18 italic'), fg='black', bg='lightgreen')
        self.place.place(x=0, y=400)

        self.need = Label(self.left, text="Needs", font=('arial 18 italic'), fg='black', bg='lightgreen')
        self.need.place(x=0, y=450)

        self.nameentry = Entry(self.left, width=50)
        self.nameentry.place(x=250, y=150)

        self.phentry = Entry(self.left, width=50)
        self.phentry.place(x=250, y=200)

        self.nopentry = Entry(self.left, width=50)
        self.nopentry.place(x=250, y=300)

        self.placeentry = Entry(self.left, width=50)
        self.placeentry.place(x=250, y=400)

        self.needs = Entry(self.left, width=50)
        self.needs.place(x=250, y=450)

        '''self.text=Text(master,width=50,height=5)
        self.text.place(x=200,y=450)'''

        self.saveme = Button(self.left, text="Save Me!!  :(", width=20, height=2, bg='steelblue',command=self.saveme)
        self.saveme.place(x=250, y=600)

    def saveme(self):
        self.val1 = self.nameentry.get()
        self.val2 = self.phentry.get()
        self.val3 = self.nopentry.get()
        self.val4 = self.placeentry.get()
        self.val5 = self.needs.get()


        if(self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == ''):
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

        sql = """insert into flood (name,phone,nop,place,needs) values(%s, %s, %s, %s, %s)"""
        c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5))
        conn.commit()
        tkinter.messagebox.showinfo("Sent")


root=Tk()
obj=querypage(root)
root.mainloop()
