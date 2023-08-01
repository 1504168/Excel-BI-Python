# Challenge Post : https://www.linkedin.com/posts/excelbi_excel-excelchallenge-powerquerychallenge-activity-7091990942710177792-LeBg/

import numpy as np
import pandas as pd


def read_excel_data(file_name, sheet_name, column_name, end_row):
    df = pd.read_excel(file_name, sheet_name=sheet_name, header=0, usecols=column_name)
    return df.loc[0:end_row - 2, :]


# write a function which takes two dataframes as input and returns True if they are equal else False. only consider values in the dataframe and not the index or the column names
def compare_dataframes(df1, df2):
    return np.array_equal(df1.values, df2.values)
def classify_password(password):
    types = set()
    for char in password:
        if char.isalpha():
            types.add("Alphabet")
        elif char.isdigit():
            types.add("Digit")
        else:
            types.add("Special character")
    if len(password) < 8:
        return "Invalid"
    elif len(password) >= 16 and len(types) == 3:
        return "Best"
    elif len(types) == 1:
        return "Weak"
    elif len(types) == 2:
        return "Strong"
    else:
        return "Very Strong"


def main():
    file_name = "../Excel Files/Password Classification.xlsx"
    sheet_name = "Sheet1"
    column_name = "A:A"
    end_row = 9
    df = read_excel_data(file_name, sheet_name, column_name, end_row)

    # apply classify_password function to each row of dataframe and store the results in a new df
    result_df = df.iloc[:, 0].apply(classify_password).to_frame()
    expected_df = read_excel_data(file_name, sheet_name, "B:B", end_row)
    # check equality of result_df and expected_df using compare_dataframes function
    # and store in a variable
    is_equal = compare_dataframes(result_df, expected_df)
    # print the variable
    print(f'Test Pass? : {is_equal}')


if __name__ == "__main__":
    main()
