import CsvReader
import datetime

reader = CsvReader.CsvReader()
feedbackinfo_list = reader.read_file()

statusDict = {}
for item in range(len(feedbackinfo_list)):
    status = feedbackinfo_list[item].status

    if status in statusDict:
        statusDict[status] = statusDict[status] + 1
    else:
        statusDict[status] = 1
print statusDict
