import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./housing.csv")
x = df[0:100].median_income
y = df[0:100].median_house_value

plt.scatter(x, y)

plt.show()