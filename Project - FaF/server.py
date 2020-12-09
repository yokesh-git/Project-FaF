from tkinter import *
import pymysql

conn=pymysql.connect(host='localhost',port=3306,user='root',password='yokesh',db='hospital')
c = conn.cursor()

class server:
    def __init__(self,master):
        self.master=master
        master.title("Display")

        self.left = Frame(master,width=800, height=720, bg='black')
        self.left.pack()

        self.txt=Text(master,width=80,height=20)
        self.txt.place(x=75,y=100)

        '''self.txt = Text(self.left, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)


        scrollb = Scrollbar(self.left, command=self.txt.yview)
        scrollb.place(x=50,y=100)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set'''

        self.heading = Label(self.left, text="FaF Centre", font=('arial 40 bold'), fg='black', bg='white')
        self.heading.place(x=250, y=0)

        self.displayAppointments = Button(self.left, text="display", width=20, height=2, bg='steelblue',command=self.buttonclick)
        self.displayAppointments.place(x=300,y=450)

        
        self.count=0
        self.tuple=()

    def retrive(self):

        try:
            sql="""select * from flood"""
            B_cur=conn.cursor()
            B_cur.execute(sql)

            for B in B_cur:
                self.table=B
                self.txt.insert(END,'\n')
                
            #tuple=(self.table)
                self.txt.insert(END,self.table,'\n')
        except:
            
            print('Exception')
    def buttonclick(self):
        self.retrive()
        
root=Tk()
obj=server(root)
