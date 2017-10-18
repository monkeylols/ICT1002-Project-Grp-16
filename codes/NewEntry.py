import CsvReader
import csv
import datetime

def new_entry(feedbackinfo_list):
    new_fbi_list = CsvReader.read_file()
    feedbackinfo_list += new_fbi_list

    with open('../data/' + str(datetime.datetime.now().microsecond) + '.csv', 'wb') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(
            ['Reported on', 'Co. Name', 'Ext. Requestor', 'Property Name', 'Category', 'Order Group Description',
             'Floor/unit or space', 'Breakdown?\n(Yes/No)', 'Description', 'Nature of feedback/complants (& Finding)',
             'Action taken', 'Start date & time', 'Acknowledged date', 'Technically completed on', 'Status',
             'Customer/ FED Internal'])

        for item in feedbackinfo_list:
            wr.writerow(
                [item.report_date_time, item.company, item.requestor, item.property_name, item.category, item.des_type,
                 item.location, item.if_breakdown, item.description, item.finding, item.action_taken,
                 item.start_date_time, item.acknowledge_date_time, item.completed_date_time, item.status,
                 item.customer_type])

    return feedbackinfo_list