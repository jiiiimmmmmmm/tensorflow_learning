import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ign_data = pd.read_csv('./dataset/datasets_116573_334386_ign_scores.csv', index_col='Platform')

help(sns.barplot)

sns.barplot(x=ign_data['Racing'], y=ign_data.index)
plt.show()



sns.heatmap(ign_data, annot=True)
plt.show()

