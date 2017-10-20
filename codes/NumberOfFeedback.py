# Done by: Lim Yan Tian 1702261
import CsvReader
import datetime
from dateutil import parser
from collections import OrderedDict

# Function 3
def get_feedback(feedbackinfo_list):
    feedback = {}
    complaints = {}

    for i in feedbackinfo_list:
        report_date_time = getattr(i, 'report_date_time')
        category = getattr(i, 'category')

        try:
            date = parser.parse(report_date_time).strftime('%Y/%m/%d')
        except ValueError:
            try:
                date = datetime.datetime.strptime(report_date_time, '%d %b %Y %H%M hrs').strftime('%Y/%m/%d')
            except ValueError:
                print "Unknown Date Format"

        if category == 'Feedback':
            if date in feedback:
                feedback[date] += 1
            else:
                feedback[date] = 1
        elif category == 'Complaints':
            if date in complaints:
                complaints[date] += 1
            else:
                complaints[date] = 1

    s= "Feedback:\n"
    ordered = OrderedDict(sorted(feedback.items(), key=lambda t: t[0]))
    for k,v in ordered.items():
        s+= "%s: %d\n" %(k, v)

    s+= "\nComplaints:\n"
    ordered = OrderedDict(sorted(complaints.items(), key=lambda t: t[0]))
    for k, v in ordered.items():
        s+= "%s: %d\n" % (k, v)
    return s


