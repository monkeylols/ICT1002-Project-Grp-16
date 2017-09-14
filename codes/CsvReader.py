import csv
from Tkinter import Tk
from tkFileDialog import askopenfilename

import FeedbackInfo


class CsvReader:
    def read_file(self):
        # Open up a file selector window to let the user select the csv file
        Tk().withdraw()
        filename = askopenfilename()
        feedbackinfo_list = []

        # Reading the csv file and putting the data into a list
        try:
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    feedbackinfo = FeedbackInfo.FeedbackInfo(row['Reported on'], row['Co. Name'], row['Ext. Requestor'],
                                                             row['Property Name'], row['Category'],
                                                             row['Order Group Description'],
                                                             row['Floor/unit or space'], row['Breakdown?\n(Yes/No)'],
                                                             row['Description'],
                                                             row['Nature of feedback/complants (& Finding)'],
                                                             row['Action taken'],
                                                             row['Start date & time'], row['Acknowledged date'],
                                                             row['Technically completed on'], row['Status'],
                                                             row['Customer/ FED Internal'])

                    feedbackinfo_list.append(feedbackinfo)
            return feedbackinfo_list
        except:
            print 'Invalid file'
            return feedbackinfo_list


# getting only the first row of the data (for example only)
reader = CsvReader()
feedbackinfo_list = reader.read_file()
if len(feedbackinfo_list) > 0:
    feedbackinfo_list[0].display_content()

    # example of getting specific info from each row
    print getattr(feedbackinfo_list[1], 'report_date_time')

# function 2
a=1
for i in range(len(feedbackinfo_list)):
    if feedbackinfo_list[i].company == "FMC/Walter Liong":
        f = open("%d.txt"%a,"w+")
        f.write(feedbackinfo_list[i].write_content())
        f.close
        a +=1