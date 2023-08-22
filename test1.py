import pandas as pd
import matplotlib.pyplot as plot
from scipy import stats

targetFile = "Monthly_Sales.csv"
sales = pd.read_csv(targetFile)
print(sales)

X = sales["Month"]
y = sales["Sales per Month"]
slope, intercept, r, p, std_err = stats.linregress(X, y)

def getY(X):
    return slope * X + intercept

print(getY(20))

model = list(map(getY, X))
plot.scatter(X, y)
plot.plot(X, model)
plot.show()
