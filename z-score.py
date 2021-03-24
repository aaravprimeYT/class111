import plotly.figure_factory as ff
import csv
import pandas as pd
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("School3.csv")
data = df["Math_score"].tolist()

def random_set_of_mean(counter):
    dataSet = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return(mean)

mean_list = []

for i in range(0,100):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("mean of sampling distribution: ",mean)
print("Standard deviation of sampling distribution: ",deviation)

fsds,fsde = mean-deviation,mean+deviation
ssds,ssde = mean-(2*deviation),mean+(2*deviation)
tsds,tsde = mean-(3*deviation),mean+(3*deviation)

df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[fsde, fsde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[ssde, ssde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[tsde, tsde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

df = pd.read_csv("School_2_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)
print("mean of sample 2:- ",mean_of_sample2)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO USED THE APP"))
fig.add_trace(go.Scatter(x=[fsde, fsde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[ssde, ssde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[tsde, tsde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)
print("mean of sample 3:- ",mean_of_sample2)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO USED THE APP"))
fig.add_trace(go.Scatter(x=[fsde, fsde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[ssde, ssde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[tsde, tsde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (mean - mean_of_sample2)/deviation
print("The z score is = ",z_score)