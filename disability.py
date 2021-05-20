import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('disability2012.csv')
plt.figure(figsize=(10,8))
expl=[0,0,0.1,0]
plt.pie(df["Total"], explode=expl, labels=df["Type of health care assistance received"], autopct='%1.1f%%', shadow=True, pctdistance=0.8)
plt.title("diability health care assistance received in 2012")
plt.savefig("diability health care assistance received in 2012.jpg")
plt.show()

df1 = pd.read_csv('disability2015.csv')
plt.figure(figsize=(10,8))
expl=[0,0,0.1,0]
plt.pie(df1["Total"], explode=expl, labels=df1["Type of health care assistance received"], autopct='%1.1f%%', shadow=True, pctdistance=0.8)
plt.title("diability health care assistance received in 2015")
plt.savefig("diability health care assistance received in 2015.jpg")
plt.show()