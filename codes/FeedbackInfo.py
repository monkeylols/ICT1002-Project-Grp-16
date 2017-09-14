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
        return self.report_date_time + ", " + self.company + ", " + self.requestor + ", " + self.property_name + ", " \
              + self.category + ", " + self.des_type + ", " + self.location + ", " + self.if_breakdown + ", " \
              + self.description + ", " + self.finding + ", " + self.action_taken + ", " + self.start_date_time \
              + ", " + self.acknowledge_date_time + ", " + self.completed_date_time + ", " + self.status + ", " \
              + self.customer_type
