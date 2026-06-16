import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency  

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv (url)
contingency =pd.crosstab(df['smoker'],df['time'])
chi2,p,dofexpected,expected = chi2_contingency(contingency)
print("Chi-Squared Statistic:",chi2)
print("p-value:",p)
print("Degrees of Freedom:",dofexpected)
print("Expected Frequencies:",expected) 
if p < 0.05:
    print("Reject the null hypothesis: ")
else:
    print("Fail to reject the null hypothesis:")
sns.countplot(data=df,x="smoker",hue='time')
plt.title('Smoker Distribution')
plt.show()