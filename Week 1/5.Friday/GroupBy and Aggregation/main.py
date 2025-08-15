#https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html

import pandas as pd
import numpy as np

speeds = pd.DataFrame(
    [
        ("bird", "Falconiformes", 389.0),
        ("bird", "Psittaciformes", 24.0),
        ("mammal", "Carnivora", 80.2),
        ("mammal", "Primates", np.nan),
        ("mammal", "Carnivora", 58),
    ],
    index=["falcon", "parrot", "lion", "monkey", "leopard"],
    columns=("class", "order", "max_speed"),

)
print("Original DataFrame:")
print(speeds)

# Grouping by 'class' and calculating the mean of 'max_speed'
groupedByClass = speeds.groupby("class")
print("\nGrouped DataFrame by 'class':")
print(groupedByClass)
mean_speed_by_class = groupedByClass["max_speed"].mean()
print("\nMean max speed by class:")
print(mean_speed_by_class)