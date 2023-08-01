# Challenge Post : https://www.linkedin.com/posts/excelbi_excel-excelchallenge-powerquerychallenge-activity-7090541381185675264-C1Uv/

import pandas as pd
import numpy as np

def read_excel_data(file_name, sheet_name, column_name, end_row):
    df = pd.read_excel(file_name, sheet_name=sheet_name, header=0, usecols=column_name)
    return df.loc[0:end_row - 2, :]

# write a function which takes two dataframes as input and returns True if they are equal else False. only consider values in the dataframe and not the index or the column names
def compare_dataframes(df1, df2):
    return np.array_equal(df1.values, df2.values)

def main():
    file_name = "../Excel Files/Month Quarter Printing.xlsx"
    sheet_name = "Sheet1"
    column_name = "A:A"
    end_row = 7
    df = read_excel_data(file_name, sheet_name, column_name, end_row)
    print(df)

if __name__ == "__main__":
    main()
