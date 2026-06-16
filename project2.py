import pandas as pd 
from scipy.stats import ttest_ind
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv (url)

maile_tips = df[df['sex'] == 'Male']['tip']
female_tips = df[df['sex'] == 'Female']['tip']

t_static , p_value = ttest_ind(maile_tips,female_tips)   

print("T-static : ",t_static)
print("P-value : ",p_value)
alpha = 0.05
if p_value <=alpha:
    print("Reject the null Hypothesis")
else:
    print("Fail to reject the null Hypothesis")

sns.barplot(data=df, x='sex', y='tip')
plt.title('Average Tip by Sex')
plt.show()
