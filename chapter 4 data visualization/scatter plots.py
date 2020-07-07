import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

candy_data = pd.read_csv('./dataset/datasets_116573_334386_candy.csv', index_col='id')

sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])
sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])
plt.show()


# sns.scatterplot(x=candy_data['pricepercent'], y=candy_data['winpercent'], hue=candy_data['chocolate'])
sns.lmplot(x='pricepercent', y='winpercent', hue='chocolate', data=candy_data)
plt.show()


sns.swarmplot(x=candy_data['chocolate'], y=candy_data['winpercent'])
plt.show()