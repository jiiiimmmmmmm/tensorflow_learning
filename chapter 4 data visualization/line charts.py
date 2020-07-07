import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
museum_data = pd.read_csv('./dataset/datasets_116573_334386_museum_visitors.csv'
                          ,index_col='Date',parse_dates=True)

plt.figure(figsize=(16,6))
sns.lineplot(data=museum_data)
plt.show()