import csv
from Tkinter import Tk
from tkFileDialog import askopenfilename
import FeedbackInfo
import matplotlib.pyplot as plot
from matplotlib.backends.backend_pdf import PdfPages
import datetime
import calendar
from dateutil.parser import parse
import numpy as np


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


################## function 7 -Identify the frequency of each request from each category###############################
# Ivan

class CategoryFrequency():
    def get_category_total(datadict, category):
        """Method to return total items of a category regardless of date"""
        print category
        total = 0
        if category not in datadict:
            print "Category absent in datadict"
            return total
        cat_dict = datadict[category]

        for day in cat_dict['ack'].keys():
            total = total + int(cat_dict['ack'][day])
            # print(total)
        return total
    #Method to get acknowledgement/completion request of a specific day
    def get_category_total_by_day_and_querytype(datadict, category, querytype, day):
        print category
        total = 0
        if category not in datadict:
            print "Category absent in datadict"
            return total
        if querytype != 'ack' and querytype != 'comp':
            print "Invalid type"
            return total

        cat_dict = datadict[category][querytype]

        if day not in cat_dict:
            print "No date found for {}:{}".format(category, querytype)
            return total
        else:
            return datadict[category][querytype][day]

    # Method to get acknowledgement/completion request of a specific month
    def get_category_total_by_month(datadict, category, querytype, month, year):

        cat_dic=datadict[category][querytype]
        # print int(month)
        # since 2nd object in returned tuple is the last day of the month
        days_in_month = calendar.monthrange(year, int(month))[1]
        # print days_in_month
        total = 0
        for day in range (1, int(days_in_month) + 1):
            datestring = ""
            if day < 10:
                day = "0{}".format(day)
            if month < 10:
                month = "0{}".format(month)

            datestring = "{day}/{month}/{year}".format(day=day, month=month, year=year)
            total = total + cat_dic.get(datestring, 0)
        return total

    global feedbackinfo_list
    reader = CsvReader()
    feedbackinfo_list = reader.read_file()  # assuming if user wants to use a different file to analyse user request
    numberofrows = 1

    freqofFeedback = float(0)
    freqofComplaints = float(0)
    freqofcompliments = float(0)
    freqofOthers = float(0)

    #This is a global dictionary to store accumulated data for the frequency and average request analysis
    global datadict
    datadict = {
        'Feedback': {},
        'Complaints': {},
        'Others/Request for Information': {},
        'Compliment': {},
        'total': len(feedbackinfo_list),
        'total_feedback': 0,
        'total_compliments': 0,
        'total_complaints': 0,
        'total_others': 0,
        'average_request_time': 0
    }

    total_report_time = datetime.datetime.now() - datetime.datetime.now()
    # Loop thru csv rows
    for row in range(0, len(feedbackinfo_list)):
        # storeddata.append(feedbackinfo_list[row].write_content())  # get the entire csv data

        # 1)Obtain category, ack datetime, comp datetime from each row
        category = feedbackinfo_list[row].category
        ack_date = feedbackinfo_list[row].acknowledge_date_time
        comp_date = feedbackinfo_list[row].completed_date_time
        report_date = feedbackinfo_list[row].report_date_time
        ack_dt = None
        comp_dt = None
        report_dt = None
        print("Before {}: {} | {} | {}".format(row, category, ack_date, comp_date))

        # 2) check if ack date is not None
        if len(ack_date) != 0 and not (ack_date == 'NA' or ack_date == 'in progress'):
            # if not None or not NA
            # convert datetime to date
            ack_dt = parse(ack_date)
            # print ack_dt
            ack_date = ack_dt.strftime("%d/%m/%Y")

        # print len(ack_date)
        # print(ack_date=='in progress')

        if len(ack_date) == 0:
            ack_date = 'blank'
        elif (ack_date == 'in progress'):
            ack_date = 'progress'
        elif len(ack_date) == 2:
            ack_date = 'not_applicable'

        if 'ack' not in datadict[category]:
            datadict[category]['ack'] = {
                'blank': 0,
                'progress': 0,
                'not_applicable': 0
            }
        # print(ack_date)
        # check if date is alrd in datadict
        if ack_date not in datadict[category]['ack']:
            # if not yet added, initialize entry
            datadict[category]['ack'][ack_date] = 1
        else:
            # else increment counter
            datadict[category]['ack'][ack_date] = datadict[category]['ack'][ack_date] + 1

        # 3 check if comp date is not None
        if len(comp_date) != 0 and not (comp_date == 'NA' or comp_date == 'in progress'):
            # if not None
            # convert
            comp_dt = parse(comp_date)
            # print comp_dt
            comp_date = comp_dt.strftime("%d/%m/%Y")

            # print(comp_date=='in progress')
        # check if comp is alrd in datadict
        if 'comp' not in datadict[category]:
            datadict[category]['comp'] = {
                'blank': 0,
                'progress': 0,
                'not_applicable': 0
            }

        if len(comp_date) == 0:
            # if date is None, set it to 'blank'
            comp_date = 'blank'
        elif comp_date == 'in progress':
            comp_date = 'progress'
        elif len(comp_date) == 2:
            comp_date = 'not_applicable'

        if comp_date not in datadict[category]['comp']:
            # if not yet added, initialize entry
            datadict[category]['comp'][comp_date] = 1
        else:
            # else increment counter
            datadict[category]['comp'][comp_date] = datadict[category]['comp'][comp_date] + 1

        # 4 compare ack_dt and comp_dt to find avg time against report_dt
        if not ack_dt and not comp_dt:
            continue
        else:
            report_dt = parse(report_date)
            if not ack_dt:
                total_report_time = total_report_time + (comp_dt - report_dt)
            elif not comp_dt:
                total_report_time = total_report_time + (ack_dt - report_dt)
            else:
                dt_list = []
                dt_list.append(comp_dt)
                dt_list.append(ack_dt)
                min_dt = min(dt_list)
                total_report_time = total_report_time + (min_dt - report_dt)
    #set the reporting total time in seconds
    total_time_in_sec = total_report_time.total_seconds()

    datadict['average_request_time'] = total_time_in_sec / datadict.get('total')

    avgreqtime=str(datetime.timedelta(seconds=datadict.get('average_request_time')))

    #print "Result:{}".format(get_category_total_by_month(datadict,category,'comp','05/2017'))
    #print "Result: {}".format(get_category_total_by_day_and_querytype(datadict, "Feedback", 'ack', '03/08/2017'))

    datadict['total_feedback'] = get_category_total(datadict, 'Feedback')
    datadict['total_compliments'] = get_category_total(datadict, "Compliment")
    datadict['total_complaints'] = get_category_total(datadict, "Complaints")
    datadict['total_others'] = get_category_total(datadict, "Others/Request for Information")
    print("Total request time taken in seconds: {}, Total: {}".format(total_time_in_sec, datadict.get('total')))
    print "The average time of receiving request is:{}".format(avgreqtime)
    #print datadict['Feedback']['comp']

    #print "The total amount of request in the enquired month is:{}".format(get_category_total_by_month(datadict, "Feedback", "comp", 3, 2017))
def getFrequency():
    """Plots a frequency graph for up to 4 labelled values"""
    def plot_graph(title, labels, values):
        def create_autopct(totalreq):
            def req_autopct(percent):
                total = sum(totalreq)
                percentile = int(round(percent * total / 100.0))
                return '{p:.2f}%  ({v:d})'.format(p=percent, v=percentile)

            return req_autopct

        explode = (0.1, 0.1, 0.1, 0.1)
        plot.figure("Frequency of each different category",figsize = (9, 9)).add_axes(([0.1, 0.1, 0.8, 0.8]))
        totalreq = values
        plot.pie(totalreq, labels=labels, autopct=create_autopct(totalreq), explode=explode, startangle=90)
        plot.title(title, bbox={'facecolor': '0.8', 'pad': 2})
        plot.legend(labels, loc="best")
        chartoPDF = PdfPages('Request_Analysis_by_Category.pdf')
        plot.savefig(chartoPDF, format='pdf')
        plot.show()
    # Get Category Feedback Frequency Result
    feedbackcounter = datadict['total_feedback']
    complaincounter = datadict['total_complaints']
    otherreqcounter = datadict['total_others']
    complimentcounter = datadict['total_compliments']
    print "Total number of Request in CSV:{0}".format(datadict['total'])
    print "Total number of feedback request: {0}".format(feedbackcounter)
    print "Total number of complaints:{0}".format(complaincounter)
    print "Total number of compliment request: {0}".format(complimentcounter)
    print "Total number of Others/Request or Information:{0}".format(otherreqcounter)
    totalfeedback = float(feedbackcounter)
    totalcomplaints = float(complaincounter)
    totalcompliments = float(complimentcounter)
    totalothers = float(otherreqcounter)
    FreqofComplaints = (totalcomplaints / float(datadict['total'])) * 100
    Freqofcompliments = (totalcompliments / float(datadict['total'])) * 100
    FreqofFeedback = (totalfeedback / float(datadict['total'])) * 100
    FreqofOthers = (totalothers / float(datadict['total'])) * 100

    print "Frequency Percentage of Complaints:{0:.2f}%".format(FreqofComplaints)
    print "Frequency Percentage of Feedback:{0:.2f}%".format(FreqofFeedback)
    print "Frequency Percentage of Compliment:{0:.2f}%".format(Freqofcompliments)
    print "Frequency Percentage of Others/Request or Information:{0:.2f}%".format(FreqofOthers)


    labels = ["Complaints", "Feedback", "Compliment", "Others"]
    title = 'Frequency of Each Request from All Categories'
    values = [totalcomplaints, totalfeedback, totalcompliments, totalothers]
    #Set Pie Chart data and generate pie chart of Frequency for each request
    plot_graph(title=title, values=values, labels=labels)


# Function to call  when generating Histograph of specific request
# Requires users to select a string called itemselect and status

def GenerateHistograph(itemselect,status):
    avgreqtime = str(datetime.timedelta(seconds=datadict.get('average_request_time')))
    #Method to Create Histogram for Data Retrieval
    def CreateHisto(data,label,title):
        plot.figure('Request_Analysis_Histogram')
        plot.bar(range(len(data)), data.values())
        plot.xticks(range(len(data)), data.keys(), rotation=50)
        plot.legend(label,loc='upper left', shadow=True, ncol=1)
        plot.tight_layout()
        plot.title(title, bbox={'facecolor': '0.8', 'pad': 2})
        chartoPDF = PdfPages('Date_Request_Analysis_by_Category.pdf')
        plot.savefig(chartoPDF, format='pdf')
        plot.show()
        plot.close()

#1) Validate the itemselected before generating the histogram
    try:
        if itemselect=="Feedback":
            if status == "Completed":
                hislab="Feedback"
                histit="Average Request Response Time:{}".format(avgreqtime)
    # Generate Histogram for all completed request
                CreateHisto(datadict['Feedback']['comp'],label=hislab,title=histit)
            elif status == "Acknowledged":
                hislab = "Feedback"
                histit = "Average Request Response Time:{}".format(avgreqtime)
                # Generate Histogram for all acknowledge request
                CreateHisto(datadict['Feedback']['ack'], label=hislab, title=histit)
        elif itemselect=="Complaint":
            if status == "Completed":
                    hislab="Complaint"
                    histit="Average Request Response Time:{}".format(avgreqtime)
                    # Generate Histogram for all completed request
                    CreateHisto(datadict['Complaints']['comp'],label=hislab,title=histit)
            elif status == "Acknowledged":
                    hislab = "Complaints"
                    histit = "Average Request Response Time:{}".format(avgreqtime)
                    # Generate Histogram for all acknowledge request
                    CreateHisto(datadict['Complaints']['ack'], label=hislab, title=histit)
        elif itemselect=="Compliment":
            if status=="Completed":
                    hislab="Compliment"
                    histit="Average Request Response Time:{}".format(avgreqtime)
                     # Generate Histogram for all completed request
                    CreateHisto(datadict['Compliment']['comp'], label=hislab, title=histit)
            elif status=="Acknowledged":
                    hislab = "Compliment"
                    histit = "Average Request Response Time:{}".format(avgreqtime)
                     # Generate Histogram for all acknowledge request
                    CreateHisto(datadict['Compliment']['ack'], label=hislab, title=histit)
        elif itemselect=="Others":
            if status == "Completed":
                hislab = "Others"
                histit = "Average Request Response Time:{}".format(avgreqtime)
                 # Generate Histogram for all completed request
                CreateHisto(datadict['Others/Request for Information']['comp'], label=hislab, title=histit)
            elif status == "Acknowledged":
                hislab = "Others"
                histit = "Average Request Response Time:{}".format(avgreqtime)
                # Generate Histogram for all acknowledge request
                CreateHisto(datadict['Compliment']['ack'], label=hislab, title=histit)

    except ValueError:
        print "Invalid input please try again"

