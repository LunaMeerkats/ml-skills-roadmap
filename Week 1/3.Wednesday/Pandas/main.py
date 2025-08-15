# Many operations can be performed on pandas DataFrames and Series.
# https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html

import numpy as np
import pandas as pd

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print("Original DataFrame:")
print(df)

# Adding a new column 'D' with values
df['D'] = [10, 11, 12]
print("\nDataFrame after adding new column 'D':")
print(df)

# New series with index
new_index = pd.Series([13, 14, 15], index=['A', 'B', 'C'])
print("\nNew Series with index:")
print(new_index)

# Series from dicts
dict_data = {'A': 16, 'B': 17, 'C': 18}
new_series = pd.Series(dict_data)
print("\nNew Series from dictionary:")
print(new_series)

#If an index is passed,series will be created with that index
new_series_with_index = pd.Series(dict_data, index=['A', 'B', 'C', 'D'])
print("\nNew Series with specified index:")
print(new_series_with_index)

# DataFrame from a dictionary of Series
dict_of_series = {
    'A': pd.Series([19, 20, 21]),
    'B': pd.Series([22, 23, 24]),
    'C': pd.Series([25, 26, 27])}

df_from_dict = pd.DataFrame(dict_of_series)
print("\nDataFrame from a dictionary of Series:")
print(df_from_dict)

