# Challenge Post : https://www.linkedin.com/posts/excelbi_excel-excelchallenge-powerquerychallenge-activity-7100688247596494848-cGfE

import pandas as pd
import numpy as np


def read_excel_data(file_name, sheet_name, column_name, end_row):
    df = pd.read_excel(file_name, sheet_name=sheet_name, header=0, usecols=column_name)
    return df.loc[0:end_row - 2, :]

# write a function which takes two dataframes as input and returns True if they are equal else False. only consider values in the dataframe and not the index or the column names
def compare_dataframes(df1, df2):
    return np.array_equal(df1.values, df2.values)


def decrypt_baconian(text):
    chunks = [text[i:i + 5] for i in range(0, len(text), 5)]
    powers = [2 ** i for i in range(0, 5)][::-1]
    #     for each chunk replace b with 1 and a with 0
    binary_chunks = [chunk.replace('b', '1').replace('a', '0') for chunk in chunks]
    #     multiply each letter of each chunk with the corresponding power
    binary_chunks = [[int(binary_chunks[i][j]) * powers[j] for j in range(0, 5)] for i in range(0, len(binary_chunks))]
    #     sum the values in each chunk
    binary_chunks = [sum(chunk) for chunk in binary_chunks]
    #     convert the sum to ascii after adding 97
    binary_chunks = [chr(chunk + 97) for chunk in binary_chunks]
    #     join the chunks and make to proper case
    result = ''.join(binary_chunks).title()
    return result


def main():
    print(decrypt_baconian("aaaabaaaaabaabbbaabbababbaabaa"))
    file_name = "../../Excel Files/Excel Challenges/Challenge 268 - Baconian Decrypter.xlsx"
    sheet_name = "Sheet1"
    column_name = "A:A"
    end_row = 7
    df = read_excel_data(file_name, sheet_name, column_name, end_row)
    # apply the function to the dataframe first column
    result_df = df.iloc[:, 0].apply(decrypt_baconian)
    result_df = pd.DataFrame(result_df)
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
