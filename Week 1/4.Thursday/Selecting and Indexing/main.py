# Assign a new column 'E' to the DataFrame based on columns 'A' and 'B'
df_with_E = df_from_dict.assign(E=df_from_dict['A'] + df_from_dict['B'])
print("\nDataFrame after assigning new column 'E':")
print(df_with_E)

#Indexing / Selection
print("\nSelecting column 'A' from DataFrame:")
print(df_with_E['A'])
# Selecting multiple columns
print("\nSelecting columns 'A' and 'B' from DataFrame:")
print(df_with_E[['A', 'B']])
# Selecting rows by index
print("\nSelecting first two rows of DataFrame:")
print(df_with_E.iloc[:2])
# Selecting rows based on a condition
print("\nSelecting rows where column 'A' is greater than 19:")
print(df_with_E[df_with_E['A'] > 19])