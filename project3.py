import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv (url)
# df.drop("index",axis=1,inplace=True)

x = df["total_bill"].values.reshape(-1, 1)
y = df["tip"].values

model = LinearRegression()
model.fit(x, y)

print("slope : ",model.coef_[0])
print("intercept : ",model.intercept_)
print("R^2 Score : ",r2_score(y,model.predict(x)))
sns.scatterplot(x=x.flatten(),y=y)
sns.lineplot(x=x.flatten(),y=model.predict(x))
plt.show()