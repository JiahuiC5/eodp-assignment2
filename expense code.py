import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('expense2015-2016.csv')
VIC = df.loc[df["State"] == 'VIC']
NSW = df.loc[df["State"] == 'NSW']
QLD = df.loc[df["State"] == 'QLD']
plt.scatter(VIC["attendence per person"], VIC["expense per person"], label= 'VIC')
plt.scatter(NSW["attendence per person"], NSW["expense per person"], label= 'NSW')
plt.scatter(QLD["attendence per person"], QLD["expense per person"], label= 'QLD')
plt.xlabel("attendence per person")
plt.ylabel("expense per person")
plt.title("expense and attendence per person in 2015-2016")
plt.grid(True)
plt.savefig("expense2015-2016.jpg")
plt.legend()
plt.show()

#data form 2016-2017
df1 = pd.read_csv('expense2016-2017.csv')
VIC = df1.loc[df["State"] == 'VIC']
NSW = df1.loc[df["State"] == 'NSW']
QLD = df1.loc[df["State"] == 'QLD']
plt.scatter(VIC["attendence per person"], VIC["expense per person"], label= 'VIC')
plt.scatter(NSW["attendence per person"], NSW["expense per person"], label= 'NSW')
plt.scatter(QLD["attendence per person"], QLD["expense per person"], label= 'QLD')
plt.xlabel("attendence per person")
plt.ylabel("expense per person")
plt.title("expense and attendence per person in 2016-2017")
plt.grid(True)
plt.savefig("expense2016-2017.jpg")
plt.legend()
plt.show()