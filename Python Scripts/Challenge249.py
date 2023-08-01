# Challenge Post : https://www.linkedin.com/feed/update/urn:li:activity:7091628544677560321/

import numpy as np
import pandas as pd

file_name = "../Excel Files/Mulitply Till a Single Digit.xlsx"
sheet_name = "Sheet1"
column_name = "A:A"
df = pd.read_excel(file_name, sheet_name=sheet_name, header=0, usecols=column_name)
df.dropna(inplace=True)

def multiply_till_single_digit(num):
    if len(str(num)) < 2:
        return num
    else:
        num_list = [int(i) for i in str(num)]
        product = num_list[0]
        for i in range(1, len(num_list)):
            product = int(product) * num_list[i]
            product = str(product).replace('0', '1')
        return multiply_till_single_digit(product)

# Apply operations to a slice of 'df' and store the results in a new column 'Result'
df.loc[:, 'Result'] = df.loc[:, 'Number'].astype(str).apply(lambda x: x.split('.')[0]).apply(multiply_till_single_digit)
print(df)
