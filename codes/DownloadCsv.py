import CsvReader
import csv
from dateutil import parser
import tkFileDialog

# Open Function - Allows user to download the csv files
# Each file contains information of complaints and feedback that have yet to be completed for a particular property
def get_files_by_property_name(feedbackinfo_list, filepath):
    for i in feedbackinfo_list:
        if not is_date(getattr(i, 'completed_date_time')):
            with open(filepath + getattr(i, 'property_name') + '.csv', 'wb') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(('Reported on', 'Co. Name', 'Ext. Requestor', 'Category', 'Order Group Description', 'Floor/unit or space', 'Breakdown?',
                                 'Description', 'Nature of feedback/complaints (& Finding)', 'Action', 'Start date & time', 'Acknowledged date', 'Status',
                                 'Customer/FED Internal'))

    for i in feedbackinfo_list:
        if not is_date(getattr(i, 'completed_date_time')):
            with open(filepath + getattr(i, 'property_name') + '.csv', 'ab') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow((getattr(i, 'report_date_time'), getattr(i, 'company'), getattr(i, 'requestor'), getattr(i, 'category'), getattr(i, 'des_type'),
                                 getattr(i, 'location'), getattr(i, 'if_breakdown'), getattr(i, 'description'), getattr(i, 'finding'), getattr(i, 'action_taken'),
                                 getattr(i, 'start_date_time'), getattr(i, 'acknowledge_date_time'), getattr(i, 'status'), getattr(i, 'customer_type')))

def is_date(string):
    try:
        parser.parse(string)
        return True
    except ValueError:
        return False

feedbackinfo_list = CsvReader.read_file()
directory = tkFileDialog.askdirectory() + '/'
get_files_by_property_name(feedbackinfo_list, directory)
