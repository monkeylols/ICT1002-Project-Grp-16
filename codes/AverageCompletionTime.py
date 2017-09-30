import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

def average_completion_time():
    # Rounding of time taken
    def rounded_value():
        k = 0
        roundedvalue = []
        while k < len(value):
            for x in value:
                y = round(x, 0)
                roundedvalue.append(y)
                k += 1
        return roundedvalue

    #Reading CSV & Select the Cols needed
    df = pd.read_csv('Feedback and Complaints_Sample Dataset.csv', usecols=[5,12,13,14])
    #Remove any rows with any NaN
    df = df.dropna(axis=0,how='any')
    #Filter out rows with the "Status" being "Completed"
    df = df[df["Status"] == 'Completed']
    # Convert the col to datetime type
    df['Acknowledged date'] = pd.to_datetime(df['Acknowledged date'])
    df['Technically completed on'] = pd.to_datetime(df['Technically completed on'])
    # Convert the col to datetime type
    df['Acknowledged date'] = pd.to_datetime(df['Acknowledged date'])
    df['Technically completed on'] = pd.to_datetime(df['Technically completed on'])
    # Subtracting and getting the difference and storing it in a new col called "diff"
    df['diff'] = (df['Technically completed on'] - df['Acknowledged date']).dt.days
    # Find the unique values of "Order Group Description"
    type = df["Order Group Description"].unique()
    label = []
    value = []
    #number of elements inside the type
    for i in range(len(type)):
        # Labels the Type
        label.append(type[i])
        # Filtering the Dataset based on the Type e.g "Lift"
        temp = df[df["Order Group Description"] == type[i]]
        # Display only the average time by using the mean()
        value.append(temp["diff"].mean())

    # Defining the rounded value for use
    roundedvalue = rounded_value()
    # Uses default settings
    plt.rcdefaults()
    style.use('ggplot')
    fig, ax = plt.subplots()

    # Plots the range on the X-Axis
    y_pos = np.arange(len(value))
    # Formats the Chart
    ax.barh(y_pos, roundedvalue, align='center', color='green', ecolor='black')
    ax.set_yticks(y_pos)
    # Shows the labels for each respective bar
    for i, v in enumerate(roundedvalue):
        ax.text(v + 0.3, i + .25, str(v), color='blue', fontweight='bold')
    # Y-Axis label
    ax.set_yticklabels(label)
    ax.invert_yaxis()  # labels read top-to-bottom
    # X-Axis label
    ax.set_xlabel('Number of Days')
    # Title label
    ax.set_title('Average Completion Time')
    # Shows the chart
    plt.show()

average_completion_time()


