import pandas as pd
list = ('Carrot', 'Beans', 'Cauliflower')
# create data frame
titled_columns = {"name": list,
                 "height": [1.67, 1.9, 0.25],
                 "weight": [54, 100, 1]}
data = pd.DataFrame(titled_columns)
print(data)