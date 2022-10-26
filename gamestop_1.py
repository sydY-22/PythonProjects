import matplotlib.pyplot as plt
import pandas as p
df = p.read_csv("C:\\Users\\sydne\\Documents\\CSV-files\\GME.csv")
print(df)

plt.plot(df.Date, df.Close)
plt.xticks(["2020-12-01", "2021-01-04", "2021-02-01", "2021-03-01", "2021-04-01", "2021-05-03",
           "2021-06-01", "2021-07-01", "2021-08-02", "2021-09-01", "2021-10-01", "2021-11-01"], ['Dec',
           'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'])
plt.title("Closing Value of GME")
plt.show()






