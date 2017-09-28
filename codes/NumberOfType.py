import CsvReader


feedbackinfo_list = CsvReader.read_file()
request_type = {}
for i in range(len(feedbackinfo_list)):
    request = getattr(feedbackinfo_list[i], 'des_type')
    if request:
        if request in request_type:
            request_type[request] += 1
        else:
            request_type[request] = 1