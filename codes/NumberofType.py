import CsvReader
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style


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
    typerequest = [0]
    typefreq = [0]
    for k, v in request_type.items():
        typerequest.append(k)
        typefreq.append(v)
        complaintdict = dict(zip(typerequest, typefreq))
        s+= "%s: %d\n" %(k, v)
        # Done by: Marcus Goh 1700277
        def plot_graph():
            # uses default settings
            plt.rcdefaults()
            style.use('ggplot')
            fig, ax = plt.subplots()

            # plots the range on the X-Axis
            y_pos = np.arange(len(typerequest))
            # formats the Chart
            ax.barh(y_pos, typefreq, align='center', color='green', ecolor='black')
            ax.set_yticks(y_pos)
            # shows the labels for each respective bar
            for i, v in enumerate(typefreq):
                ax.text(v + 0.3, i + .25, str(v), color='blue', fontweight='bold')
            # y-axis label
            ax.set_yticklabels(typerequest)
            # labels read top-to-bottom
            ax.invert_yaxis()
            # x-axis label
            ax.set_xlabel('Number of requests')
            # title label
            ax.set_title('Total number of requests by type')
            # fits chart to the window size
            plt.tight_layout()
            # Shows the chart
            return plt
    return plot_graph()



# feedbackinfo_list = CsvReader.read_file()
#
# print get_request_type(feedbackinfo_list)
