import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

fifa_data = pd.read_csv('dataset/datasets_116573_334386_fifa.csv', index_col='Date', parse_dates=True)
plt.figure(figsize=(16,6))

sns.lineplot(data=fifa_data)
plt.show()