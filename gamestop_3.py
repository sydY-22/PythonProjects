import matplotlib.pyplot as plt
import pandas as p
df = p.read_csv("C:\\Users\\sydne\\Documents\\CSV-files\\GME(2).csv")
print(df)
m = ["2020-12", "2021-01", "2021-02", "2021-03", "2021-04", "2021-05", "2021-06", "2021-07", "2021-08", "2021-09",
     "2021-10", "2021-11"]
vol_ls = []
for rows in m:
    v = df[(df["Date"].str[0:7] == rows)]
    print(rows)
    index = v.index
    number_of_rows = len(index)
    v["Volatility"] = (v["Close"].mean() - v["Close"])**2
    print(v["Volatility"])
    y = v["Volatility"].sum() / number_of_rows
    print(y)
    vol_ls.append(y)
y = vol_ls
plt.plot(["Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"], y)
plt.title("GME Volatility")
plt.show()

