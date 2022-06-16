import plotly.figure_factory as ff 
import plotly.graph_objects as go
import pandas as pd 
import statistics 
import csv 
import random 

df = pd.read_csv("blah.csv")
data = df["reading_time"].tolist()

fig = ff.create_distplot([data],["reading_time"] , show_hist=False)
fig.show()

std_deviation = statistics.stdev(data)
mean = statistics.mean(data)
print("mean :- ",mean)
print("Standard deviation :- ", std_deviation)

# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
     random_index=random.randint(0,len(data)-1)
     value=data[random_index]
     dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
  set_of_mean=random_set_of_mean(100)
  mean_list.append(set_of_mean)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)

fig = ff.create_distplot([mean_list],["student Marks"] , show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.show()




fstds,fstde= mean-std_deviation, mean+std_deviation
sstds,sstde= mean-(2*std_deviation), mean+(2*std_deviation)
tstds,tstde= mean-(3*std_deviation), mean+(3*std_deviation)

print("Std1",fstds,fstde)
print("Std2",sstds,sstde)
print("Std3",tstds,tstde)


df = pd.read_csv("s1.csv")
data = df["reading_time"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[fstde, fstde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[sstde, sstde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[tstds, tstds], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

# #finding the mean of the STUDENTS WHO USED MATH PRACTISE APP and plotting it on the plot.
df = pd.read_csv("s2.csv")
data = df["reading_time"].tolist()
mean_of_sample2 = statistics.mean(data)
print("mean of sample 2:- ",mean_of_sample2)
fig = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO USED THE APP"))
fig.add_trace(go.Scatter(x=[fstde, fstde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[sstde, sstde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[tstds, tstds], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


# finding the mean of the STUDENTS WHO WERE ENFORCED WITH REGISTERS and plotting it on the plot.
df = pd.read_csv("s3.csv")
data = df["reading_time"].tolist()
mean_of_sample3 = statistics.mean(data)
print("mean of sample3:- ",mean_of_sample3)
fig = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[fstde, fstde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[sstde, sstde], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[tstds, tstds], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()



z_score = (mean - mean_of_sample2)/std_deviation
print("The z score is = ",z_score)