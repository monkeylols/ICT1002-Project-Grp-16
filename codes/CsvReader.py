import csv
from Tkinter import Tk
from tkFileDialog import askopenfilename
import FeedbackInfo


def read_file():
    # Open up a file selector window to let the user select the csv file
    Tk().withdraw()
    filename = askopenfilename()
    feedbackinfo_list = []
    global i
    i=[]
    # Reading the csv file and putting the data into a list
    try:
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            i = reader.next()
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
    except ValueError:
        return 'Invalid file'


'''#Adrian
# getting only the first row of the data (for example only)
reader = CsvReader()
feedbackinfo_list = reader.read_file()
if len(feedbackinfo_list) > 0:
    feedbackinfo_list[0].display_content()

    # example of getting specific info from each row
    print getattr(feedbackinfo_list[1], 'report_date_time')
'''


#Jun Hui
#temporary variables

# cName = "FMC/Walter Liong"
#
# # function 2
# def createFiles(feedbackinfo_list, coy):
#     count=1
#     for i in feedbackinfo_list:
#         if i.company == coy:
#             if not os.path.exists(coy):
#                 os.makedirs(coy)
#             f = open(os.path.join(coy) + "/%d.txt"%count,"w+")
#             f.write(feedbackinfo_list[i].write_content())
#             f.close
#             count +=1
#
# # YT - function 3
# def func3(feedbackinfo_list):
#     num_feedback = {}
#     num_complaints = {}
#     for i in feedbackinfo_list:
#         report_date_time = getattr(i, 'report_date_time')
#         category = getattr(i, 'category')
#
#         try:
#             date = parser.parse(report_date_time).strftime('%d/%m/%Y')
#         except ValueError:
#             try:
#                 date = datetime.datetime.strptime(report_date_time, '%d %b %Y %H%M hrs').strftime('%d/%m/%Y')
#             except ValueError:
#                 print "Unknown Date Format"
#
#         if category == 'Feedback':
#             if date in num_feedback:
#                 num_feedback[date] += 1
#             else:
#                 num_feedback[date] = 1
#         elif category == 'Complaints':
#             if date in num_complaints:
#                 num_complaints[date] += 1
#             else:
#                 num_complaints[date] = 1
#
# # YT - function 4
# def func4(feedbackinfo_list, searchPara):
#     request_type = {}
#     for i in feedbackinfo_list:
#         request = getattr(i, 'des_type')
#         if request:
#             if request in request_type:
#                 request_type[request] += 1
#             else:
#                 request_type[request] = 1
