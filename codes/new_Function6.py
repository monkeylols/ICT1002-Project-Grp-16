import CsvReader
from datetime import datetime
from dateutil import parser


def tryParsingDate(text):
    newText = text.replace("hrs", "")
    return parser.parse(newText).strftime("%d/%m/%Y")


feedbackinfo_list = CsvReader.read_file()

countTypeDict = {}  # A dictionary that store {des_type:[desTypeCount, firstReportDate, lastReportDate]}
for item in range(len(feedbackinfo_list)):  # For loop count the number of desType for each desType in data set

    des_type = feedbackinfo_list[item].des_type

    # Convert string into date using tryParsingDate function
    reportedDate = tryParsingDate(feedbackinfo_list[item].report_date_time)

    if des_type not in countTypeDict:  # If des_type not in dict, add it into the dict
        countTypeDict[des_type] = [1, reportedDate, reportedDate]
    else:  # If des_type in dict, increase the count by 1
        countTypeDict[des_type][0] = countTypeDict[des_type][0] + 1

for item in range(len(feedbackinfo_list)):  # For loop to update the firstReportDate in countTypeDict

    des_type = feedbackinfo_list[item].des_type
    reportedDate = datetime.strptime(tryParsingDate(feedbackinfo_list[item].report_date_time), "%d/%m/%Y")  # Date from feedbackinfot_list
    reportedDateDict = datetime.strptime(countTypeDict[des_type][1], "%d/%m/%Y")  # Date from the dict

    if reportedDate < reportedDateDict:  # Check if date from feedbackinfo_list is earlier than the date in the dict
        countTypeDict[des_type][1] = reportedDate.strftime("%d/%m/%Y")  # If the date is earlier, set it to the dict

for item in range(len(feedbackinfo_list)):  # For loop to update the lastReportDate in countTypeDict

    des_type = feedbackinfo_list[item].des_type
    reportedDate = datetime.strptime(tryParsingDate(feedbackinfo_list[item].report_date_time), "%d/%m/%Y")  # Date from feedbackinfot_list
    reportedDateDict = datetime.strptime(countTypeDict[des_type][1], "%d/%m/%Y")  # Date from the dict

    if reportedDate > reportedDateDict:  # Check if date from feedbackinfo_list is later than the date in the dict
        countTypeDict[des_type][2] = reportedDate.strftime("%d/%m/%Y")  # If the date is later, set it to the dict

newCountDict = {}  # A new dict to store the data with no duplicate of words
for keys in countTypeDict.keys():

    # Format the desType
    formatKeys = keys.lower()
    formatKeys = formatKeys.replace("-", " ")

    if formatKeys not in newCountDict:  # If the formated keys is not in the new dict, copy everything from old dict over
        newCountDict[formatKeys] = countTypeDict[keys]
    elif formatKeys in newCountDict:  # If formated keys is in the new dict, total the count values
        newCountDict[formatKeys][0] = newCountDict[formatKeys][0] + countTypeDict[keys][0]
        if datetime.strptime(newCountDict[formatKeys][1], "%d/%m/%Y") < datetime.strptime(countTypeDict[keys][1], "%d/%m/%Y"):  # At the same time check for the earlier date
            newCountDict[formatKeys][1] = newCountDict[formatKeys][1]
        else:  # This means that the date in the old dict is earlier than the one in the new dict
            newCountDict[formatKeys][1] = countTypeDict[keys][1]

for keys in countTypeDict.keys():

    # Format the desType
    formatKeys = keys.lower()
    formatKeys = formatKeys.replace("-", " ")

    if formatKeys in newCountDict:
        if datetime.strptime(newCountDict[formatKeys][2], "%d/%m/%Y") > datetime.strptime(countTypeDict[keys][2], "%d/%m/%Y"):  # At the same time check for the later date
            newCountDict[formatKeys][2] = newCountDict[formatKeys][2]
        else:  # This means that the date in the old dict is later than the one in the new dict
            newCountDict[formatKeys][2] = countTypeDict[keys][2]

for keys in newCountDict.keys():

    desType = keys
    frequency = newCountDict[keys][0]
    firstReportDate = datetime.strptime(newCountDict[keys][1], "%d/%m/%Y")
    lastReportDate = datetime.strptime(newCountDict[keys][2], "%d/%m/%Y")
    difference = (lastReportDate - firstReportDate).days

    if difference != 0:
        reportFrequency = float(frequency)/float(difference)
    else:
        reportFrequency = float(frequency)/1.0
        difference = 1

    print "There is about %.3f requests on %s in the span of %d days" % (reportFrequency, keys, difference)

