import csv
import datetime

# Done by: Lim Yan Tian 1702261
# Open Function - Allows user to download the csv files
# Each file contains information of complaints and feedback for a particular property
def get_files_by_property_name(feedbackinfo_list, filepath):
    now = datetime.datetime.now()
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

