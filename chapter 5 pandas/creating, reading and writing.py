import pandas as pd
# creating
fruits = pd.DataFrame([[30,21]], columns=['Apples','Bananas'])
print(fruits)

fruit_sales = pd.DataFrame([[35,21],[41,34]], columns=['Apples','Bananas'], index=['2017 Sales', '2018 Sales'])
print(fruit_sales)

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
print(ingredients)
print(ingredients.shape)
# reading
# data = pd.read_csv(path, index_col='column')

# writing
# data.to_csv(path)
