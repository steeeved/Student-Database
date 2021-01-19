#frontend
import tkinter
from tkinter import *
import tkinter.messagebox
import stdDatabase

class Student:

    def __init__(self, root): 
        self.root = root
        self.root.title("Kanjogu Primary School Database")
        self.root.geometry("1350x750+0+0")
        self.root.configure(bg="cadet blue")

        stdAd = StringVar()
        firstname = StringVar()
        surname = StringVar() 
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Parents_Contact= StringVar()
        Address= StringVar()
        
        #FUCTIONS
        def iExit():
            iExit = tkinter.messagebox.askyesno("Kanjogu Primary School Database", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtstdAd.delete(0, END)
            self.txtfirstname.delete(0, END)
            self.txtsurname.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtParents_Contact.delete(0, END)
            self.txtAddress.delete(0, END)

        def addData():
            if(len(stdAd.get())!=0):
                stdDatabase.addStudentRecord(stdAd.get(), firstname.get(), surname.get(), DoB.get(), Age.get(), Gender.get(), \
                            Parents_Contact.get(), Address.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (stdAd.get(), firstname.get(), surname.get(), DoB.get(), Age.get(), Gender.get(), \
                            Parents_Contact.get(), Address.get()))
 
        def DispalyData():
            studentlist.delete(0, END)
            for row in stdDatabase.viewData():
                studentlist.insert(END,row, str(""))

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtstdAd.delete(0, END)
            self.txtstdAd.insert(END,sd[1])
            self.txtfirstname.delete(0, END)
            self.txtfirstname.insert(END,sd[2])
            self.txtsurname.delete(0, END)
            self.txtsurname.insert(END,sd[3])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END,sd[4])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END,sd[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END,sd[6])
            self.txtParents_Contact.delete(0, END)
            self.txtParents_Contact.insert(END,sd[7])
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END,sd[8])


        def DeleteData():
            if(len(stdAd.get())!=0):
                stdDatabase.deleteRec(sd[0])
                clearData()
                DispalyData()

        def searchData():
            studentlist.delete(0, END)
            for row in stdDatabase.searchData(stdAd.get(), firstname.get(), surname.get(), DoB.get(), Age.get(), Gender.get(), Parents_Contact.get(), Address.get()):           
                            studentlist.insert(END, row, str(""))

        def updateData():
            if(len(stdAd.get())!=0):
                stdDatabase.deleteRec(sd[0])
            if(len(stdAd.get())!=0):
                stdDatabase.addStudentRecord(stdAd.get(), firstname.get(), surname.get(), DoB.get(), Age.get(), Gender.get(), \
                            Parents_Contact.get(), Address.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (stdAd.get(), firstname.get(), surname.get(), DoB.get(), Age.get(), Gender.get(), \
                            Parents_Contact.get(), Address.get()))
        #frames
        MainFrame = Frame(self.root,  bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost white")
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=("aerial", 30,"bold"), text="Kanjogu Primary School", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1550, height=70, padx=18, pady=10, bg="Ghost white", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1500, height=400, padx=20, pady=20, bg="cadet blue", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=50, height=40, padx=31, bg="Ghost white", relief=RIDGE,
        font=("aerial", 18,"bold"), text="Student Information\n") 
        DataFrameLeft.pack(side=LEFT)
 
        DataFrameRight = LabelFrame(DataFrame, bd=1, width=50, height=300, padx=31, pady=3, bg="Ghost white", relief=RIDGE,
        font=("aerial", 18,"bold"), text="Student Details\n")
        DataFrameRight.pack(side=RIGHT)

        #Entry Widgets
        self.lblstdAd = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Student Adm No:",padx=2, pady=2, bg="Ghost White")
        self.lblstdAd.grid(row=0, column=0, sticky=W)
        self.txtstdAd = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"), textvariable=stdAd, width=39)
        self.txtstdAd.grid(row=0, column=1, sticky=W)

        self.lblfirstname = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="First Name:",padx=2, pady=2, bg="Ghost White")
        self.lblfirstname.grid(row=1, column=0, sticky=W)
        self.txtfirstname = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"), textvariable=firstname, width=39)
        self.txtfirstname.grid(row=1, column=1, sticky=W)

        self.lblsurname= Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Surname :",padx=2, pady=2, bg="Ghost White")
        self.lblsurname.grid(row=2, column=0, sticky=W)
        self.txtsurname = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"), textvariable=surname, width=39)
        self.txtsurname.grid(row=2, column=1, sticky=W)

        self.lblDoB = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Date of Birth:",padx=2, pady=2, bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1, sticky=W)

        self.lblAge = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Age:",padx=2, pady=2, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1, sticky=W)

        self.lblGender = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Gender:",padx=2, pady=2, bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1, sticky=W)

        self.txtParents_Contact = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Parents Contact:",padx=2, pady=2, bg="Ghost White")
        self.txtParents_Contact.grid(row=6, column=0, sticky=W)
        self.txtParents_Contact = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"), textvariable=Parents_Contact, width=39)
        self.txtParents_Contact.grid(row=6, column=1, sticky=W)

        self.txtAddress = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Adress:",padx=2, pady=2, bg="Ghost White")
        self.txtAddress.grid(row=7, column=0, sticky=W)
        self.txtAddress = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"), textvariable=Address, width=39)
        self.txtAddress.grid(row=7, column=1, sticky=W)

        #LISTBOX and SCROLLBAR WIDGET
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky="ns")

        studentlist = Listbox(DataFrameRight, width=40, height=8, font=("Comfortaa Light", 15 ,"bold"),yscrollcommand=scrollbar.set) 
        studentlist.bind("<<ListboxSelect>>", StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = studentlist.yview)

        #BUTTON WIDGTES
        self.btnAddData = Button(ButtonFrame, text="Add New", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=DispalyData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=searchData)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=updateData)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)
    
if __name__ == "__main__":
    root = Tk()
    application = Student(root)
    root.mainloop()