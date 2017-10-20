# Done by: Foo Cher Zhi Adrian 1700550
class FeedbackInfo:
    def __init__(self, report_date_time, company, requestor, property_name, category, des_type, location, if_breakdown,
               description, finding, action_taken, start_date_time, acknowledge_date_time, completed_date_time, status,
               customer_type):
        self.report_date_time = report_date_time
        self.company = company
        self.requestor = requestor
        self.property_name = property_name
        self.category = category
        self.des_type = des_type
        self.location = location
        self.if_breakdown = if_breakdown
        self.description = description
        self.finding = finding
        self.action_taken = action_taken
        self.start_date_time = start_date_time
        self.acknowledge_date_time = acknowledge_date_time
        self.completed_date_time = completed_date_time
        self.status = status
        self.customer_type = customer_type

    def display_content(self):
        print self.report_date_time + ", " + self.company + ", " + self.requestor + ", " + self.property_name + ", " \
              + self.category + ", " + self.des_type + ", " + self.location + ", " + self.if_breakdown + ", " \
              + self.description + ", " + self.finding + ", " + self.action_taken + ", " + self.start_date_time \
              + ", " + self.acknowledge_date_time + ", " + self.completed_date_time + ", " + self.status + ", " \
              + self.customer_type

    def write_content(self):
        S = "ReportDateTime:\t%s\n"%self.report_date_time
        S+= "Company:\t%s\n"%self.company
        S+= "Requestor:\t%s\n"%self.requestor
        S+= "PropertyName:\t%s\n"%self.property_name
        S+= "Category:\t%s\n"%self.category
        S+= "Des_type:\t%s\n"%self.des_type
        S+= "Location:\t%s\n"%self.location
        S+= "Breakdown:\t%s\n"%self.if_breakdown
        S+= "Description:\t%s\n"%self.description
        S+= "Finding:\t%s\n"%self.finding
        S+= "ActionTaken:\t%s\n"%self.action_taken
        S+= "StartDateTime\t%s\n"%self.start_date_time
        S+= "AcknowledgeDateTime:\t%s\n"%self.acknowledge_date_time
        S+= "CompletedDateTime:\t%s\n"%self.completed_date_time
        S+= "Status:\t%s\n"%self.status
        S+= "CustomerType:\t%s"%self.customer_type
        return S

