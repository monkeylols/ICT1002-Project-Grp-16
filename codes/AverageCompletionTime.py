import pandas as pd

#Reading CSV & Select the Cols needed
df = pd.read_csv('Feedback and Complaints_Sample Dataset.csv', usecols=[5,12,13,14])
#Remove any rows with any NaN
df = df.dropna(axis=0,how='any')
#Filter out rows with the "Status" being "Completed"
df = df[df["Status"] == 'Completed']
#Convert the col to datetime type
df['Acknowledged date'] = pd.to_datetime(df['Acknowledged date'])
df['Technically completed on'] = pd.to_datetime(df['Technically completed on'])

#Subtracting and getting the difference and storing it in a new col called "diff"
df['diff'] = df['Technically completed on'] - df['Acknowledged date']

#Find the unique values of "Order Group Description"
type = df["Order Group Description"].unique()


#As type is a DataSet, len(type) is to find the number of elements inside the dataset.
#Range is to limit the number of times the for-loop will run
#i is a variable name given for the counter in the for-loop
for i in range(len(type)):
    #Labels the Type
    print type[i]
    #Filtering the Dataset based on the Type e.g "Building"
    temp = df[df["Order Group Description"] == type[i]]
    #Display only the average time by using the mean()
    print temp["diff"].mean()