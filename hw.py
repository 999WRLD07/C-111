import plotly.figure_factory as ff
import pandas as pd
import statistics


df = pd.read_csv("111hw.csv")
data = df["claps"].to_list()
print(data)

fig = ff.create_distplot([data], ["amount of claps"], show_hist = False)
fig.show()

mean = statistics.mean(data)
std = statistics.stdev(data)
print("mean and std for data", mean, std)

z_score = (mean - mean)/std
print("The z score is = ",z_score)