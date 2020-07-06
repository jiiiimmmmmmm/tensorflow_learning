import pandas as pd

# melbourne_data = pd.read_csv('melb_data.csv')
#
# y = melbourne_data.Price
# print(y.describe())
#
# melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
# x = melbourne_data[melbourne_features]
# print(x.describe())
# print(x.head())
#
# from sklearn.tree import *
# decition_tree_model = DecisionTreeRegressor(random_state=1)
#
# decition_tree_model.fit(x,y)
# preds = decition_tree_model.predict(x.head())
#
# print(preds)


home_data = pd.read_csv('home_data_train.csv')
pd.set_option('display.max_columns',None)
y = home_data.SalePrice
print(y.head())
print(y.describe())
# Create the list of features below
feature_names = ["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF","FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]
# Select data corresponding to features in feature_names
X = home_data[feature_names]
print(X.head())
print(X.describe())

from sklearn.tree import DecisionTreeRegressor
decision_tree_model = DecisionTreeRegressor(random_state=1)
decision_tree_model.fit(X,y)
preds = decision_tree_model.predict(X)
print(preds)
