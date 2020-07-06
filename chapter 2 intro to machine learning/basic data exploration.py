import pandas as pd

# melbourne_data = pd.read_csv('melb_data.csv')
#
# print(melbourne_data.columns)
# print(melbourne_data.describe())
# print(melbourne_data.head())




home_data = pd.read_csv('home_data_train.csv')
print(home_data.columns)

print(home_data.LotArea.describe())

print(home_data.YearBuilt.describe())




