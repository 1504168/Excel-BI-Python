# Challenge Post : https://www.linkedin.com/posts/excelbi_excel-excelchallenge-powerquerychallenge-activity-7090541381185675264-C1Uv/
import numpy as np
import pandas as pd


def read_excel_data(file_name, sheet_name, column_name, end_row):
    df = pd.read_excel(file_name, sheet_name=sheet_name, header=0, usecols=column_name,dtype=str)
    return df.loc[0:end_row - 2, :]

def compare_dataframes(df1, df2):
    return np.array_equal(df1.values, df2.values)

def binary_to_month_quarter(text):
    # convert text to character list
    text_list = list(text)

    # List to store the months and quarters
    month_quarter_list = []

    # Loop over the length of text_list
    for i in range(len(text_list)):
        # Check if the character is '1'
        if text_list[i] == '1':
            month = pd.to_datetime(str(i + 1), format='%m').strftime('%b')
            quarter = pd.to_datetime(str(i + 1), format='%m').quarter

            # Add the month and quarter to the list
            month_quarter_list.append(month + '-Q' + str(quarter))

    # Join the list into a string, with ', ' as the separator
    result = ', '.join(month_quarter_list)

    return result


def main():
    file_name = "../Excel Files/Month Quarter Printing.xlsx"
    sheet_name = "Sheet1"
    column_name = "A:A"
    end_row = 7

    df = read_excel_data(file_name, sheet_name, column_name, end_row)
    df['Month-Quarter'] = df['Strings'].apply(binary_to_month_quarter)
    # select only month-quarter column
    df = df.loc[:, ['Month-Quarter']]

    result_df = read_excel_data(file_name, sheet_name, "B:B", end_row)
    # fill Nan values with empty string
    result_df.fillna('', inplace=True)
    test_pass = compare_dataframes(df, result_df)
    print(f'Test Pass? : {test_pass}')

if __name__ == "__main__":
    main()
