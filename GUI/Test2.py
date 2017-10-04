from Tkinter import *
from CsvReader import *
import ttk


class MyFirstGUI:

    def __init__(self, master, reader):
        #calling objects and classes
        self.feedbackinfo_list = {}
        self.master = master
        self.reader = reader

        self.container = Frame(master)
        self.container.pack()
        master.title("A simple GUI")
        self.label = Label(self.container, text="Welcome! Please select the CSV file which you would like to choose!")
        self.label.pack()

        #creating button
        self.greet_button = Button(self.container, text="OK", command=lambda: self.greet(self))
        self.greet_button.pack()

    def greet(self,button):
        self.feedbackinfo_list = self.reader.read_file()
        if self.feedbackinfo_list == "Invalid file":
            exit()
        else:
            self.createview()
            self.container.destroy()

    def search(self, button, desFrame, searchInput):
        self.createview(searchInput)
        desFrame.destroy()

    def createview(self, searchPara=""):
        #creating frame with parent, Tkinter
        masterFrame = Frame(self.master, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        #giving z-weight to frame, so that other child frame will resize with respect of this frame
        masterFrame.rowconfigure(0, weight=1)
        masterFrame.columnconfigure(0, weight=1)

        # create the elements for Search bar
        searchFrame = Frame(masterFrame, highlightbackground="green", highlightcolor="green", highlightthickness=1,width=300, height=300)
        searchLabel = Label(searchFrame, text="Search : \t")
        searchEntry = Entry(searchFrame, bd=10)
        #creating search button
        searchButton = Button(searchFrame, text="search",command=lambda: self.search(self,masterFrame,searchEntry.get()))

        # implement to grid
        searchLabel.grid(row=0, column=0)
        searchEntry.grid(row=0,column=1)
        searchButton.grid(row=0, column=2)

        #creating func frame with the frame
        funcFrame = Frame(masterFrame, highlightbackground="red", highlightcolor="red", highlightthickness=1, width=500,
                          height=300)
        #creating frame with parent being funcFrame
        w = Canvas(funcFrame, width=500, height=300)
        w.pack()

        #ignore
        '''funcButton1 = Button(funcFrame, text="search",command=lambda: self.search(self,masterFrame,searchEntry.get()))
        funcButton2 = Button(funcFrame, text="search",command=lambda: self.search(self,masterFrame,searchEntry.get()))
        funcButton3 = Button(funcFrame, text="search",command=lambda: self.search(self,masterFrame,searchEntry.get()))
        funcButton4 = Button(funcFrame, text="search",command=lambda: self.search(self,masterFrame,searchEntry.get()))

        funcButton1.grid(row=0, column=0, pady=5)
        funcButton2.grid(row=1, column=0, pady=5)
        funcButton3.grid(row=2, column=0, pady=5)
        funcButton4.grid(row=3, column=0, pady=5)'''

        #Create Tree
        treeFrame = Frame(masterFrame)
        tree = ttk.Treeview(treeFrame)
        treeFrame.rowconfigure(0, weight=1)
        treeFrame.columnconfigure(0, weight=1)

        #calling the columns and giving them an id
        tree["columns"]=("1", "2","3","4","5","6","7","8","9","10","11","12","13","14","15","16")
        tree.heading("#0", text="")
        tree.column("#0", minwidth=0, width=0)
        for x in range(1,16):
            tree.heading(str(x), text=str(x))
            tree.column(str(x), minwidth=0)
        for x in self.feedbackinfo_list:
            if searchPara == "":
                tree.insert("", "end", values=(x.report_date_time, x.company, x.requestor, x.property_name,
                            x.category, x.des_type, x.location, x.if_breakdown,
                            x.finding, x.start_date_time, x.acknowledge_date_time,
                            x.completed_date_time, x.status, x.customer_type))
                            #x.description.encode("utf-8"), x.action_taken.encode("utf=8")))
            elif x.company == searchPara:
                tree.insert("", "end", values=(x.report_date_time, x.company, x.requestor, x.property_name,
                            x.category, x.des_type, x.location, x.if_breakdown,
                            x.finding, x.start_date_time, x.acknowledge_date_time,
                            x.completed_date_time, x.status, x.customer_type))
                            #x.description.encode("utf-8"), x.action_taken.encode("utf=8")))

        #implementing the y-bar and x-bar of treeview
        treev = Scrollbar(treeFrame, orient=VERTICAL, command=tree.yview)
        treeh = Scrollbar(treeFrame, orient=HORIZONTAL, command=tree.xview)

        tree.configure(yscrollcommand=treev.set)
        tree.configure(xscrollcommand=treeh.set)

        tree.grid(row=0, column=0, sticky='nsw')
        treeh.grid(row=1,column=0, sticky='sew')
        treev.grid(row=0, column=1, sticky='nse')

        # add frames into grid
        #sticky='nsew' is being used to make it stick to which direction you prefer. North = n South =s and etc
        searchFrame.grid(row=0, column=0, pady=50, columnspan=2,sticky="nw")
        funcFrame.grid(row=0, column=1, pady=50, sticky="nsew")
        treeFrame.grid(row=1,column=0, columnspan=3, sticky="nsew")

        # pack masterFrame to TKinter
        masterFrame.pack(fill=None, expand=False)


reader = CsvReader()
root = Tk()
root.geometry("800x600")

my_gui = MyFirstGUI(root, reader)
root.mainloop()