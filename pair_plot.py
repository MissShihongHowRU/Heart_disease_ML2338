import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



data = pd.read_csv("heart.csv")
sns.pairplot(data, hue = "target")
plt.savefig("pairplot.png")