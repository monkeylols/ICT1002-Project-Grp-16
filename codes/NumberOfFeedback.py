import CsvReader
from dateutil import parser
import datetime


feedbackinfo_list = CsvReader.read_file()
num_feedback = {}
num_complaints = {}
for i in range(len(feedbackinfo_list)):
    report_date_time = getattr(feedbackinfo_list[i], 'report_date_time')
    category = getattr(feedbackinfo_list[i], 'category')

    try:
        date = parser.parse(report_date_time).strftime('%d/%m/%Y')
    except ValueError:
        try:
            date = datetime.datetime.strptime(report_date_time, '%d %b %Y %H%M hrs').strftime('%d/%m/%Y')
        except ValueError:
            print "Unknown Date Format"

    if category == 'Feedback':
        if date in num_feedback:
            num_feedback[date] += 1
        else:
            num_feedback[date] = 1
    elif category == 'Complaints':
        if date in num_complaints:
            num_complaints[date] += 1
        else:
            num_complaints[date] = 1