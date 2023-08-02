# Challenge Post : https://www.linkedin.com/feed/update/urn:li:activity:7092353320513601536/

import numpy as np
import pandas as pd


def read_excel_data(file_name, sheet_name, column_name, end_row):
    df = pd.read_excel(file_name, sheet_name=sheet_name, header=0, usecols=column_name)
    return df.loc[0:end_row - 2, :]


# write a function which takes two dataframes as input and returns True if they are equal else False. only consider values in the dataframe and not the index or the column names
def compare_dataframes(df1, df2):
    return np.array_equal(df1.values, df2.values)


# write a function which takes a number as input and returns True if we multiply the number by 2,3,4..till length of the number and if any of the multiplication output contains all the digits of the original number else False
def is_cyclic_number(number):
    number_str = str(number)
    for i in range(2, len(number_str) + 1):
        if sorted(number_str) == sorted(str(number * i)):
            return True
    return False


def main():
    file_name = "../Excel Files/Cyclic Type of Number.xlsx"
    sheet_name = "Sheet1"
    column_name = "A:A"
    end_row = 11
    df = read_excel_data(file_name, sheet_name, column_name, end_row)
    result_df = df[df.iloc[:, 0].apply(is_cyclic_number)]
    expected_df = read_excel_data(file_name, sheet_name, "B:B", end_row).dropna()
    print("Input Dataframe: \n", df)
    print('\n')
    print("Result Dataframe: \n", result_df)
    print('\n')
    print("Expected Result: \n", expected_df)
    print('\n')
    print("Test Pass: ", compare_dataframes(result_df, expected_df))


if __name__ == "__main__":
    main()
