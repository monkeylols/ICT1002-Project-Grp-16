import csv
import datetime
import os

# Open Function - Allows user to download the csv files
# Each file contains information of complaints and feedback that have yet to be completed for a particular property
def get_files_by_property_name(feedbackinfo_list, filepath):
    now = datetime.datetime.now()
        #if not is_date(getattr(i, 'completed_date_time')):
    with open(filepath + str(now.microsecond) + '.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ['Reported on', 'Co. Name', 'Ext. Requestor', 'Property Name', 'Category', 'Order Group Description',
             'Floor/unit or space', 'Breakdown?\n(Yes/No)', 'Description', 'Nature of feedback/complants (& Finding)',
             'Action taken', 'Start date & time', 'Acknowledged date', 'Technically completed on', 'Status',
             'Customer/ FED Internal'])
        for item in feedbackinfo_list:
            writer.writerow(
                [item.report_date_time, item.company, item.requestor, item.property_name, item.category, item.des_type,
                 item.location, item.if_breakdown, item.description, item.finding, item.action_taken,
                 item.start_date_time, item.acknowledge_date_time, item.completed_date_time, item.status,
                 item.customer_type])

    return

def downloadtxt(feedbackinfo_list, filepath):
    count=1
    for i in feedbackinfo_list:
            f = open(filepath + "/%d.txt"%(count),"w+")
            f.write(i.write_content())
            f.close
            count +=1

    #for i in feedbackinfo_list:
        #if not is_date(getattr(i, 'completed_date_time')):
        #with open(filepath + date + '.csv', 'wb') as csvfile:
                #writer = csv.writer(csvfile)
                # writer.writerow((getattr(i, 'report_date_time'), getattr(i, 'company'), getattr(i, 'requestor'), getattr(i, 'category'), getattr(i, 'des_type'),
                #                  getattr(i, 'location'), getattr(i, 'if_breakdown'), getattr(i, 'description'), getattr(i, 'finding'), getattr(i, 'action_taken'),
                #                  getattr(i, 'start_date_time'), getattr(i, 'acknowledge_date_time'), getattr(i, 'status'), getattr(i, 'customer_type')))

# def is_date(string):
#     try:
#         parser.parse(string)
#         return True
#     except ValueError:
#         return False

# feedbackinfo_list = CsvReader.read_file()
# directory = tkFileDialog.askdirectory() + '/'
# get_files_by_property_name(feedbackinfo_list, directory)
