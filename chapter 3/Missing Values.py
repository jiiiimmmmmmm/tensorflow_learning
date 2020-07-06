import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
X_full = pd.read_csv('home_data/train.csv', index_col='Id')
X_test_full = pd.read_csv('home_data/test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X_full.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X_full.SalePrice
X_full.drop(['SalePrice'], axis=1, inplace=True)

# To keep things simple, we'll use only numerical predictors
X = X_full.select_dtypes(exclude=['object'])
X_test = X_test_full.select_dtypes(exclude=['object'])

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8,
                                                      test_size=0.2, random_state=0)


# Number of missing values in each column of training data
missing_val_count_by_column = (X_train.isnull().sum())
print("Number of missing values in each column of training data:\n",
      missing_val_count_by_column[missing_val_count_by_column > 0])

# Fill in the line below: How many rows are in the training data?
num_rows,num_cols = X_train.shape
print("How many rows are in the training data?",num_rows)

# Fill in the line below: How many columns in the training data
# have missing values?
num_cols_with_missing = sum(missing_val_count_by_column>0)
print("How many columns in the training data"
      "have missing values?", num_cols_with_missing)
# Fill in the line below: How many missing entries are contained in
# all of the training data?
tot_missing = sum(missing_val_count_by_column)
print("How many missing entries are contained in"
      "all of the training data?",tot_missing)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Function for comparing different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# Fill in the line below: get names of columns with missing values
drop_features = [col
                 for col in X_train.columns
                if X_train[col].isnull().any()] # Your code here

# Fill in the lines below: drop columns in training and validation data

reduced_X_train = X_train.drop(drop_features, axis = 1)
reduced_X_valid = X_valid.drop(drop_features, axis = 1)
print("MAE (Drop columns with missing values):",
      score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))

from sklearn.impute import SimpleImputer

# Fill in the lines below: imputation
my_imputer = SimpleImputer() # Your code here
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

# Fill in the lines below: imputation removed column names; put them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns
print("MAE (Imputation):",
      score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))


# Preprocessed training and validation features
myimputer = SimpleImputer(strategy = "median")
final_X_train = pd.DataFrame(myimputer.fit_transform(X_train))
final_X_valid = pd.DataFrame(myimputer.transform(X_valid))
# Define and fit model
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(final_X_train, y_train)

# Get validation predictions and MAE
preds_valid = model.predict(final_X_valid)
print("MAE (use median strategy):",
      mean_absolute_error(y_valid, preds_valid))


# Fill in the line below: preprocess test data
final_X_test = pd.DataFrame(myimputer.fit_transform(X_test))

# Fill in the line below: get test predictions
preds_test = model.predict(final_X_test)


print("""
Given that thre are so few missing values in the dataset, we'd expect imputation to perform better than dropping columns entirely. However, we see that dropping columns performs slightly better! While this can probably partially be attributed to noise in the dataset, another potential explanation is that the imputation method is not a great match to this dataset. That is, maybe instead of filling in the mean value, it makes more sense to set every missing value to a value of 0, to fill in the most frequently encountered value, or to use some other method. For instance, consider the GarageYrBlt column (which indicates the year that the garage was built). It's likely that in some cases, a missing value could indicate a house that does not have a garage. Does it make more sense to fill in the median value along each column in this case? Or could we get better results by filling in the minimum value along each column? It's not quite clear what's best in this case, but perhaps we can rule out some options immediately - for instance, setting missing values in this column to 0 is likely to yield horrible results!
""")