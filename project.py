import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv (url)
print (df.info())
print(df.describe())
del df["sex"]
del df["smoker"]
del df["day"]
del df["time"]
# sns.histplot(df['total_bill'],kde =True)
# plt.title('Distribution of Total Bill')
# plt.xlabel('Total Bill')
# plt.ylabel('Frequency')
# plt.show()
sns.heatmap(df.corr(),annot=True,cmap="coolwarm")
plt.title('Correlation Matrix')
plt.show()