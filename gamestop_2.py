import matplotlib.pyplot as plt
import pandas as p
df = p.read_csv("C:\\Users\\sydne\\Documents\\CSV-files\\GME.csv")
print(df)
plt.plot(df.Date[40:78], df.Volume[40:78])
plt.xticks(["2021-01-04", "2021-02-01"], ["Jan", "Feb"])
plt.title("Trading Volume")
plt.show()


