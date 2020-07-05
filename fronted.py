#fronted
from tkinter import*
import tkinter.messagebox
import stdDatabase_Backend

class Student:
    def __init__(self,root):
        self.root =root
        self.root.title("Student Database Mangaement System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        #**********************************Function********************************
        def iExit():
            iExit =tkinter.messagebox.askyesno("Student Database Mangaement System","CONFIRM IF YOU WANT TO EXIT")
            if iExit > 0:
                root.destroy()
                return

        def ClearData():
            self.txtStdID.delete(0,END)
            self.txtfname.delete(0,END)
            self.txtsname.delete(0,END)
            self.txtdob.delete(0,END)
            self.txtage.delete(0,END)
            self.txtadd.delete(0,END)
            self.txtmno.delete(0,END)
            self.txtgen.delete(0,END)


        def addData():
            if(len(StdID.get())!=0):
                stdDatabase_Backend.addStdRec(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Address.get(),Mobile.get(),\
                                              Gender.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Address.get(),Mobile.get(),\
                                        Gender.get()))

        def DisplayData():
            studentlist.delete(0,END)
            for row in stdDatabase_Backend.viewData():
                studentlist.insert(END,row,str(""))


        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,sd[1])
            self.txtfname.delete(0,END)
            self.txtfname.insert(END,sd[2])
            self.txtsname.delete(0,END)
            self.txtsname.insert(END,sd[3])
            self.txtdob.delete(0,END)
            self.txtdob.insert(END,sd[4])
            self.txtage.delete(0,END)
            self.txtage.insert(END,sd[5])
            self.txtadd.delete(0,END)
            self.txtadd.insert(END,sd[6])
            self.txtmno.delete(0,END)
            self.txtmno.insert(END,sd[7])
            self.txtgen.delete(0,END)
            self.txtgen.insert(END,sd[8])
            


        def DeleteDate():
            if(len(StdID.get())!=0):
                stdDatabase_Backend.deleteRec(sd[0])
                ClearData()
                DisplayData()


        def searchData():
            studentlist.delete(0,END)
            for row in stdDatabase_Backend.searchData(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Address.get(),Mobile.get(),Gender.get()):
                studentlist.insert(END,row,str(""))



        def update():
            if(len(StdID.get())!=0):
                stdDatabase_Backend.deleteRec(sd[0])
            if(len(StdID.get())!=0):
                stdDatabase_Backend.addStdRec(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Address.get(),Mobile.get(),Gender.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Address.get(),Mobile.get(),Gender.get()))
                
            
            
                
                
                
            
        





        #**********************************Frames*******************

        MainFrame =Frame(self.root, bg="cadet blue")
        MainFrame.grid()
        
        TitFrame = Frame(MainFrame, bd=2, padx=54,pady=8, bg="Ghost White" , relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame ,font=('arial' ,47, 'bold'), text="Student Management Database System",bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350,height=70, padx=18,pady=10, bg="Ghost White" , relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300,height=400,padx=20,pady=10, bg="cadet blue" , relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000,height=600,padx=20, bg="Ghost White" , relief=RIDGE,font=('arial' ,20, 'bold'),text="STUDENT INFORMATION")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450,height=300,padx=31 ,pady=3, bg="Ghost White" , relief=RIDGE, font=('arial' ,20, 'bold'),text="STUDENT Details")
        DataFrameRIGHT.pack(side=RIGHT)

        #*****************************LABELS AND ENTRY WEIGHT**************
        self.lblStdID = Label(DataFrameLEFT ,font=('arial' ,20, 'bold'),text="Student Id",padx=2,pady=2, bg="Ghost White")
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID = Entry(DataFrameLEFT ,font=('arial' ,20, 'bold'),textvariable=StdID,width=39)
        self.txtStdID.grid(row=0,column=1)

        self.lblfname = Label(DataFrameLEFT ,font=('arial' ,20, 'bold'),text="Firstname",padx=2,pady=2, bg="Ghost White")
        self.lblfname.grid(row=1,column=0,sticky=W)
        self.txtfname = Entry(DataFrameLEFT ,font=('arial' ,20, 'bold'),textvariable=Firstname,width=39)
        self.txtfname.grid(row=1,column=1)

        self.lblsname = Label(DataFrameLEFT ,font=('arial' ,20, 'bold'),text="Surname",padx=2,pady=2, bg="Ghost White")
        self.lblsname.grid(row=2,column=0,sticky=W)
        self.txtsname = Entry(DataFrameLEFT ,font=('arial' ,20, 'bold'),textvariable=Surname,width=39)
        self.txtsname.grid(row=2,column=1)

        self.lbldob = Label(DataFrameLEFT ,font=('arial' ,20, 'bold'),text="DoB",padx=2,pady=2, bg="Ghost White")
        self.lbldob.grid(row=3,column=0,sticky=W)
        self.txtdob = Entry(DataFrameLEFT ,font=('arial' ,20, 'bold'),textvariable=DoB,width=39)
        self.txtdob.grid(row=3,column=1)

        self.lblgen = Label(DataFrameLEFT ,font=('arial' ,20, 'bold'),text="Gender",padx=2,pady=2, bg="Ghost White")
        self.lblgen.grid(row=7,column=0,sticky=W)
        self.txtgen = Entry(DataFrameLEFT ,font=('arial' ,20, 'bold'),textvariable=Gender,width=39)
        self.txtgen.grid(row=7,column=1)

        self.lblage = Label(DataFrameLEFT ,font=('arial' ,20, 'bold'),text="Age",padx=2,pady=2, bg="Ghost White")
        self.lblage.grid(row=4,column=0,sticky=W)
        self.txtage = Entry(DataFrameLEFT ,font=('arial' ,20, 'bold'),textvariable=Age,width=39)
        self.txtage.grid(row=4,column=1)

        self.lbladd = Label(DataFrameLEFT ,font=('arial' ,20, 'bold'),text="Address",padx=2,pady=2, bg="Ghost White")
        self.lbladd.grid(row=5,column=0,sticky=W)
        self.txtadd = Entry(DataFrameLEFT ,font=('arial' ,20, 'bold'),textvariable=Address,width=39)
        self.txtadd.grid(row=5,column=1)

        self.lblmno = Label(DataFrameLEFT ,font=('arial' ,20, 'bold'),text="Mobile",padx=2,pady=2, bg="Ghost White")
        self.lblmno.grid(row=6,column=0,sticky=W)
        self.txtmno = Entry(DataFrameLEFT ,font=('arial' ,20, 'bold'),textvariable=Mobile,width=39)
        self.txtmno.grid(row=6,column=1)


         #*****************************Scroll bars**************

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1, sticky = 'ns')

        studentlist = Listbox(DataFrameRIGHT ,width=41,height=16,font=('arial' ,12, 'bold'),yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=studentlist.yview)


        #*****************************Buttons**************
        self.btnAddData = Button(ButtonFrame ,text ="Add New",font=('arial' ,12, 'bold'),height=1,width=10,bd=4,
                                 command=addData)
        self.btnAddData.grid(row=0,column=0)
        
        self.btnDisplayData = Button(ButtonFrame ,text ="Display",font=('arial' ,12, 'bold'),height=1,width=10,bd=4,
                                     command=DisplayData)
        self.btnDisplayData.grid(row=0,column=1)
        
        self.btnClearData = Button(ButtonFrame ,text ="Clear",font=('arial' ,12, 'bold'),height=1,width=10,bd=4,command=ClearData)
        self.btnClearData.grid(row=0,column=2)
        
        self.btnDeleteData = Button(ButtonFrame ,text ="Delete",font=('arial' ,12, 'bold'),height=1,width=10,bd=4 ,command=DeleteDate)
        self.btnDeleteData.grid(row=0,column=3)
        
        self.btnSearchData = Button(ButtonFrame ,text ="Search",font=('arial' ,12, 'bold'),height=1,width=10,bd=4,command=searchData)
        self.btnSearchData.grid(row=0,column=4)
        
        self.btnUpdateData = Button(ButtonFrame ,text ="Update",font=('arial' ,12, 'bold'),height=1,width=10,bd=4,command=update)
        self.btnUpdateData.grid(row=0,column=5)

        
        self.btnExit = Button(ButtonFrame ,text ="Exit",font=('arial' ,12, 'bold'),height=1,width=10,bd=4 ,command=iExit)
        self.btnExit.grid(row=0,column=6)
        
        
        
if __name__=='__main__':
    root =Tk()
    application= Student(root)
    root.mainloop()
    
