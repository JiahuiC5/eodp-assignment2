
import pandas as pd
import matplotlib.pyplot as plt

#data form 2016-2017
df = pd.read_csv('do not see GP.csv')
VIC = df.loc[df["State"] == 'VIC']
NSW = df.loc[df["State"] == 'NSW']
QLD = df.loc[df["State"] == 'QLD']
plt.figure(figsize=(10,8))
plt.bar(VIC["PHN area name"], VIC["Did not see a GP (%)"])
plt.bar(NSW["PHN area name"], NSW["Did not see a GP (%)"])
plt.bar(QLD["PHN area name"], QLD["Did not see a GP (%)"])
plt.yticks([10, 20, 30])
plt.xticks(rotation=45, ha="right")
plt.ylabel("Did not see a GP(%)")
plt.title("PHN area name with did not see a GP percentage")
plt.tight_layout()
plt.savefig("people do not see doctor percentage.jpg")
plt.show()