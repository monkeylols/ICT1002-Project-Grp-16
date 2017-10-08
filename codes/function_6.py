import CsvReader
import datetime
from dateutil import parser
import re


feedbackinfo_list = CsvReader.read_file()

# Counting the request type
counterDict = {}
for i in range(len(feedbackinfo_list)):
    des_type = re.sub('[^A-Za-z0-9]+', '', feedbackinfo_list[i].des_type).lower()
    if des_type[-1:] == " ":  # Remove the last character if it is a space
        des_type = des_type.replace(" ", "")

    if des_type in counterDict:
        counterDict[des_type][2] = counterDict[des_type][2] + 1
    else:
        for aKey in counterDict.keys():
            if des_type in aKey:
                counterDict[aKey][2] = counterDict[aKey][2] + 1

        counterDict[des_type] = [None, None, 1]

# Adding last reported date
for i in range(len(feedbackinfo_list)):
    report_date_time = feedbackinfo_list[i].report_date_time
    des_type = re.sub('[^A-Za-z0-9]+', '', feedbackinfo_list[i].des_type).lower()
    if des_type[-1:] == " ":  # Remove the last character if it is a space
        des_type = des_type.replace(" ", "")

    try:
        date = parser.parse(report_date_time).strftime('%d/%m/%Y')
    except ValueError:
        try:
            date = datetime.datetime.strptime(report_date_time, '%d %b %Y %H%M hrs').strftime('%d/%m/%Y')
        except ValueError:
            print "Unknown Date Format"

    if counterDict[des_type][0] == None:
        counterDict[des_type][0] = date
    elif datetime.datetime.strptime(counterDict[des_type][0], "%d/%m/%Y") < datetime.datetime.strptime(date, "%d/%m/%Y"):
        counterDict[des_type][0] = date

# Adding first reported date
for i in range(len(feedbackinfo_list)):
    report_date_time = feedbackinfo_list[i].report_date_time
    des_type = re.sub('[^A-Za-z0-9]+', '', feedbackinfo_list[i].des_type).lower()
    if des_type[-1:] == " ":  # Remove the last character if it is a space
        des_type = des_type.replace(" ", "")

    try:
        date = parser.parse(report_date_time).strftime('%d/%m/%Y')
    except ValueError:
        try:
            date = datetime.datetime.strptime(report_date_time, '%d %b %Y %H%M hrs').strftime('%d/%m/%Y')
        except ValueError:
            print "Unknown Date Format"

    if counterDict[des_type][1] == None:
        counterDict[des_type][1] = date
    elif datetime.datetime.strptime(counterDict[des_type][1], "%d/%m/%Y") > datetime.datetime.strptime(date, "%d/%m/%Y"):
        counterDict[des_type][1] = date

# [lastdate, firstdate, count]
# Calculating frequency
for aKey in counterDict:
    lastDate = datetime.datetime.strptime(counterDict[aKey][0], "%d/%m/%Y")
    firstDate = datetime.datetime.strptime(counterDict[aKey][1], "%d/%m/%Y")
    count = counterDict[aKey][2]

    differenceDay = lastDate - firstDate
    frequency = differenceDay.days/count
    outputStr = "There is about %s request on %s in the span of %s days" % (frequency, aKey, differenceDay)
    if str(differenceDay) == "0:00:00":
        print "There is about %s request on %s in the span of 0 days." % (frequency, aKey)
    else:
        print outputStr[:-12].replace(",", ".")