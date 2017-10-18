from Tkinter import *
import CsvReader, Classifier, matplotlib, ttk, CatFrequency,NumberofType,NumberOfFeedback, typefreq, tkFileDialog, \
    DownloadCsv,tkMessageBox,cloud, NewEntry
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import AverageCompletionTime

class GUI:

    def __init__(self, master):
        #calling objects and classes
        self.feedbackinfo_list = []
        self.cloudstr = ""
        self.master = master

        self.container = Frame(master)
        self.container.pack(fill="both", expand=True, pady=300)
        master.title("Feedback")
        self.label = Label(self.container, text="Welcome! Please select the CSV file which you would like to choose!")
        self.label.pack()

        #creating button
        self.greet_button = Button(self.container, text="OK", command=lambda: self.greet(self))
        self.greet_button.pack()

        self.colnames = ["Reported On", "Co. Name", "Requestor", "Property Name", "Category",
                           "Order Group Description", "Floor/unit or space", "Breakdown? (Yes/No)", "Description",
                           "Nature of feedback/complants (& Finding)", "Action Taken", "Start date & time",
                           "Acknowledged date", "Technically completed on", "Status", "Customer / FED Internal"]


    def greet(self,button):
        self.feedbackinfo_list = CsvReader.read_file()
        if self.feedbackinfo_list == "Invalid file":
            exit()
        else:
            self.createview()
            self.container.destroy()

    def search(self, button, desFrame, searchInput):
        self.treeview(searchInput)

    def deletechild(self,funcFrame):
        for child in funcFrame.winfo_children():
            child.destroy()
        plt.cla()
        plt.clf()
        plt.close('all')

    def classify(self, button):
        self.deletechild(self.rightFrame)
        plt = Classifier.get_com_feedback_prob(self.feedbackinfo_list, self.uniqueCoy[self.coybox.current()], self.uniquecat[self.catbox.current()])
        if type(plt) is str:
            tkMessageBox.showinfo("Error", plt)
            return
        self.fig1 = plt.figure(1)
        canvas = FigureCanvasTkAgg(self.fig1, master=self.rightFrame)
        canvas.show()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def classifier(self,button):
        self.funcFrame.destroy()
        self.funcFrame = Frame(self.leftFrame, highlightbackground="blue", highlightcolor="black", highlightthickness=1)
        backButton = Button(self.funcFrame, text="Back", command=lambda: self.basicfuncFrame())
        coyLabel = Label(self.funcFrame, text="Company : \t")
        catLabel = Label(self.funcFrame, text="Category : \t")
        analyseButton = Button(self.funcFrame, text="Analyse", command=lambda: self.classify(self))

        self.uniqueCoy = list(self.getuniquecoy())
        variable = StringVar(self.master)
        self.coybox = ttk.Combobox(self.funcFrame, textvariable=variable, state='readonly')
        self.coybox['values'] = (self.uniqueCoy)

        self.uniquecat = list(self.getuniquecat())
        variable = StringVar(self.master)
        self.catbox = ttk.Combobox(self.funcFrame, textvariable=variable, state='readonly')
        self.catbox['values'] = (self.uniquecat)

        backButton.grid(row=0,column=0,sticky="nw")
        coyLabel.grid(row=1, column=0)
        self.coybox.grid(row=1, column=1)
        catLabel.grid(row=2, column=0)
        self.catbox.grid(row=2,column=1)
        analyseButton.grid(row=3, column=1)

        self.funcFrame.grid(row=1,column=0)

    def catFrequency(self,button):
        self.getfreq()
        self.funcFrame.destroy()
        self.funcFrame = Frame(self.leftFrame, highlightbackground="blue", highlightcolor="black", highlightthickness=1)
        backButton = Button(self.funcFrame, text="Back", command=lambda: self.basicfuncFrame())
        catLabel = Label(self.funcFrame, text="Category : \t")
        goButton = Button(self.funcFrame, text="Go", command=lambda: self.specificfreq())

        variable = StringVar(self.master)
        self.combox = ttk.Combobox(self.funcFrame, textvariable=variable, state='readonly')
        self.combox['values'] = ("Completed","Acknowledged")

        self.uniquecat = list(self.getuniquecat())
        variable = StringVar(self.master)
        self.catbox = ttk.Combobox(self.funcFrame, textvariable=variable, state='readonly')
        self.catbox['values'] = (self.uniquecat)

        backButton.grid(row=0,column=0,sticky="nw")
        catLabel.grid(row=1, column=0)
        self.catbox.grid(row=1, column=1)
        self.combox.grid(row=2,column=1)
        goButton.grid(row=3, column=1)

        self.funcFrame.grid(row=1,column=0)

    def avgComplete (self,button):
        self.deletechild(self.rightFrame)
        plt = AverageCompletionTime.average_completion_time()
        fig = plt.figure(1)
        canvas = FigureCanvasTkAgg(fig, master=self.rightFrame)
        canvas.show()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def numoftype(self,button):
        self.deletechild(self.rightFrame)
        plt = NumberofType.get_request_type(self.feedbackinfo_list)
        fig = plt.figure(1)
        canvas = FigureCanvasTkAgg(fig, master=self.rightFrame)
        canvas.show()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def getfreq(self):
        self.deletechild(self.rightFrame)
        plt = CatFrequency.getFrequency(self.feedbackinfo_list)
        fig = plt.figure(1)
        canvas = FigureCanvasTkAgg(fig, master=self.rightFrame)
        canvas.show()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def specificfreq(self):
        self.deletechild(self.rightFrame)
        s = ["Completed","Acknowledged"]
        plt = CatFrequency.GenerateHistograph(self.uniquecat[self.catbox.current()],s[self.combox.current()],
                                              self.feedbackinfo_list)
        fig = plt.figure(1)
        canvas = FigureCanvasTkAgg(fig, master=self.rightFrame)
        canvas.show()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def getuniquecoy(self):
        output =set()
        for x in self.feedbackinfo_list:
            output.add(x.company)
        return list(output)

    def getuniquecat(self):
        output = set()
        for x in self.feedbackinfo_list:
            output.add(x.category)
        return list(output)

    def numfb(self, button):
        self.deletechild(self.rightFrame)
        s = NumberOfFeedback.get_feedback(self.feedbackinfo_list)
        sFrame = Text(self.rightFrame)
        sFrame.pack(expand=YES, fill=BOTH)
        sFrame.insert(END, s)
        sFrame.config(state=DISABLED)

    def typefreq(self, button):
        self.deletechild(self.rightFrame)
        s = typefreq.requestfreq(self.feedbackinfo_list)
        sFrame = Text(self.rightFrame)
        sFrame.pack(expand=YES, fill=BOTH)
        sFrame.insert(END, s)
        sFrame.config(state=DISABLED)

    def downloadcsv(self, button):
        directory = tkFileDialog.askdirectory() + '/'
        x=[]
        if directory =="/":
            return
        for i in self.resultcount:
            x.append(self.feedbackinfo_list[i])
        DownloadCsv.get_files_by_property_name(x, directory)

    def downloadtxt(self, button):
        directory = tkFileDialog.askdirectory() + '/'
        x=[]
        if directory =="/":
            return
        for i in self.resultcount:
            x.append(self.feedbackinfo_list[i])
        DownloadCsv.downloadtxt(x, directory)

    def dlframe(self,button):
        self.funcFrame.destroy()
        self.funcFrame = Frame(self.leftFrame)
        backButton = Button(self.funcFrame, text="Back", command=lambda: self.basicfuncFrame())
        dlLabel = Label(self.funcFrame, text="Download as : \t")
        csvButton = Button(self.funcFrame, text="Csv file", command=lambda: self.downloadcsv(self))
        txtButton = Button(self.funcFrame, text="Txt file", command=lambda: self.downloadtxt(self))

        backButton.grid(row=0,column=0,sticky="nw")
        dlLabel.grid(row=1, column=0)
        csvButton.grid(row=2, column=0, sticky="w")
        txtButton.grid(row=2, column=1, sticky="e")

        self.funcFrame.grid(row=1,column=0, sticky="w")

    def newentry (self,button):
        self.feedbackinfo_list = NewEntry.new_entry(self.feedbackinfo_list)

    def basicfuncFrame(self):
        if hasattr(self, 'funcFrame'):
            self.funcFrame.destroy()

        self.deletechild(self.rightFrame)
        self.funcFrame = Frame(self.leftFrame)

        for i in self.feedbackinfo_list:
            self.cloudstr += i.company + i.property_name + i.location

        plt = cloud.gencloud(self.cloudstr)
        fig = plt.figure(1)
        canvas = FigureCanvasTkAgg(fig, master=self.rightFrame)
        canvas.show()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        # creating claasify button
        classifyButton = Button(self.funcFrame, text="Predictive Analysis", command=lambda: self.classifier(self),
                                width =25)
        # creating avgComplete Button
        avgComButton = Button(self.funcFrame, text="Avg Completion Time", command=lambda: self.avgComplete(self),
                                width =25)
        # creating numFB Button
        getfreqButton = Button(self.funcFrame, text="Category Frequency", command=lambda: self.catFrequency(self),
                                width =25)
        # creating numoftype Button
        numoftypeButton = Button(self.funcFrame, text="Number Of Requests", command=lambda: self.numoftype(self),
                                width =25)
        # creating numoffb Button
        numoffbButton = Button(self.funcFrame, text="Number Of Feedback", command=lambda: self.numfb(self),
                                width =25)
        #creating of typefreq Button
        typefreqButton = Button(self.funcFrame, text="Types Of Frequency", command=lambda: self.typefreq(self),
                                width =25)
        #creating downnload Button
        printButton = Button(self.funcFrame, text="Download", command=lambda: self.dlframe(self),
                                width =25)
        # creating Merge Button
        mergeButton = Button(self.funcFrame, text="Merge", command=lambda: self.newentry(self), width=25)

        classifyButton.grid(row=0, column=0, sticky="nw")
        avgComButton.grid(row=1, column=0, sticky="nw")
        getfreqButton.grid(row=2, column=0, sticky="nw")
        numoftypeButton.grid(row=3,column=0, sticky="nw")
        numoffbButton.grid(row=4,column=0, sticky="nw")
        typefreqButton.grid(row=5,column=0, sticky="nw")
        printButton.grid(row=6,column=0, sticky="sw")
        mergeButton.grid(row=7,column=0, sticky="sw")

        self.funcFrame.grid(row=1, column=0, sticky="w")

    def treeview(self, searchPara):
        if hasattr(self, 'treeFrame'):
            self.treeFrame.destroy
        self.treeFrame = Frame(self.masterFrame)
        tree = ttk.Treeview(self.treeFrame)
        self.treeFrame.rowconfigure(0, weight=1)
        self.treeFrame.columnconfigure(0, weight=1)

        # calling the columns and giving them an id
        tree["columns"] = (self.colnames)
        tree.heading("#0", text="")
        tree.column("#0", minwidth=0, width=0)
        for x in range(1, 16):
            tree.heading(str(x), text=self.colnames[x])
            tree.column(str(x), minwidth=0)

        counter = 0
        self.resultcount=[]
        if searchPara != "":
            for x in self.feedbackinfo_list:
                try:
                    if searchPara in x.company or searchPara in x.category or searchPara in x.property_name :
                        tree.insert("", "end", values=(x.report_date_time, x.company, x.requestor, x.property_name,
                                               x.category, x.des_type, x.location, x.if_breakdown,x.description,
                                               x.finding, x.action_taken,x.start_date_time, x.acknowledge_date_time,
                                               x.completed_date_time, x.status, x.customer_type))
                        self.resultcount.append(counter)
                except:
                    pass
                counter += 1
        else:
            try:
                for x in self.feedbackinfo_list:
                    tree.insert("", "end", values=(x.report_date_time, x.company, x.requestor, x.property_name,
                                                x.category, x.des_type, x.location, x.if_breakdown,
                                                x.finding, x.start_date_time, x.acknowledge_date_time,
                                                x.completed_date_time, x.status, x.customer_type))
            except:
                pass

        # implementing the y-bar and x-bar of treeview
        treev = Scrollbar(self.treeFrame, orient=VERTICAL, command=tree.yview)
        treeh = Scrollbar(self.treeFrame, orient=HORIZONTAL, command=tree.xview)

        tree.configure(yscrollcommand=treev.set)
        tree.configure(xscrollcommand=treeh.set)

        tree.grid(row=0, column=0, sticky='nsw')
        treeh.grid(row=1, column=0, sticky='sew')
        treev.grid(row=0, column=1, sticky='nse')
        self.treeFrame.grid(row=1,column=0, columnspan=3, sticky="nsew")

    def createview(self, searchPara=""):
        #creating frame with parent, Tkinter
        self.masterFrame = Frame(self.master)
        #giving z-weight to frame, so that other child frame will resize with respect of this frame
        self.masterFrame.rowconfigure(0, weight=1)
        self.masterFrame.columnconfigure(0, weight=1)

        # create the elements for Search bar
        self.leftFrame = Frame(self.masterFrame)
        searchFrame = Frame(self.leftFrame)

        # creating search button
        searchButton = Button(searchFrame, text="search",
                              command=lambda: self.search(self, self.masterFrame, searchEntry.get()))

        searchLabel = Label(searchFrame, text="Search : \t")
        searchEntry = Entry(searchFrame, bd=10)


        # implement to searchframe
        searchLabel.grid(row=0, column=0)
        searchEntry.grid(row=0,column=1)
        searchButton.grid(row=0, column=2)

        #reqtypeButton.grid(row=4, column=2)
        searchFrame.grid(row=0,column=0)

        # creating func frame with the frame
        self.rightFrame = Frame(self.masterFrame)

        #Create Tree
        self.treeview(searchPara)

        #Create function fram + word cloud
        self.basicfuncFrame()

        # add frames into grid
        #sticky='nsew' is being used to make it stick to which direction you prefer. North = n South =s and etc
        self.leftFrame.grid(row=0, column=0, pady=50, columnspan=2,sticky="nw")
        self.rightFrame.grid(row=0, column=1, pady=50, sticky="ne")

        # pack masterFrame to TKinter
        self.masterFrame.pack(fill=None, expand=False)

root = Tk()
root.geometry("1200x700")
my_gui = GUI(root)
root.mainloop()