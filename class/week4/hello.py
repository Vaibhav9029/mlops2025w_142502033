import pandas as pd

d = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
# creating a Dataframe object 
df = pd.DataFrame(d)
print(df)
