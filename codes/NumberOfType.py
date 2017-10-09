import CsvReader

# Function 4
def get_request_type(feedbackinfo_list):
    request_type = {}
    types = {'Air Conditioning': ['Air', 'Acmv'], 'Building': ['Building', 'Floor'], 'Carpark & Driveway': ['Carpark', 'Driveway', 'Pothole'],
             'Cleanliness': ['Cleaning', 'Cleanliness'], 'Electrical': ['Electrical'], 'Fire': ['Fire'], 'Lift': ['Lift'], 'Lighting': ['Lighting'],
             'Others': ['Other'], 'Pest Control': ['Pest'], 'Maintenance': ['Drainage', 'Plumbing', 'Pump', 'Toilet', 'Water', 'Tree', 'Waste', 'Mechanical'],
             'Security & Services': ['Security', 'Safety', 'Service', 'Equipment']}
    s=""
    for i in feedbackinfo_list:
        request = getattr(i, 'des_type').title()
        if request:
            for key, value in types.items():
                for val in value:
                    if val in request.title():
                        if key in request_type:
                            request_type[key] += 1
                        else:
                            request_type[key] = 1
    for k, v in request_type.items():
        s+= "%s: %d\n" %(k, v)
    return s

#feedbackinfo_list = CsvReader.read_file()
#get_request_type(feedbackinfo_list)
