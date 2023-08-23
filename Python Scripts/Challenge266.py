# Challenge Post : https://www.linkedin.com/feed/update/urn:li:activity:7092353320513601536/

import numpy as np
import pandas as pd


def read_excel_data(file_name, sheet_name, column_name, end_row):
    df = pd.read_excel(file_name, sheet_name=sheet_name, header=0, usecols=column_name,dtype=str)
    return df.loc[0:end_row - 2, :]


# write a function which takes two dataframes as input and returns True if they are equal else False. only consider values in the dataframe and not the index or the column names
def compare_dataframes(df1, df2):
    return np.array_equal(df1.values, df2.values)


def calculate_character_occurrences(input_string):
    # Dictionary to hold characters and their occurrences
    characters_occurrences = {}

    # Loop through each character in the string
    for current_character in input_string:
        # If the character is already in the dictionary, increment its count
        if current_character in characters_occurrences:
            characters_occurrences[current_character] += 1
        else:             # Otherwise, add the character to the dictionary with a count of 1
            characters_occurrences[current_character] = 1

    return characters_occurrences

def check_odd_even_occurrences(character_occurrences):
    # Loop through the dictionary and check the conditions
    for digit, occurrences in character_occurrences.items():
        current_digit = int(digit)

        # Check if odd digits occurred odd times
        if current_digit % 2 != 0 and occurrences % 2 == 0:
            return False

        # Check if even digits occurred even times
        if current_digit % 2 == 0 and occurrences % 2 != 0:
            return False

    return True


def analyze_digit_occurrences(input_string):
    # Calculate the occurrences of each digit in the input string
    character_occurrences = calculate_character_occurrences(input_string)

    # Check if odd digits occur an odd number of times and even digits occur an even number of times
    result = check_odd_even_occurrences(character_occurrences)

    return result

def main():
    file_name = "../Excel Files/Excel Challenges/Challenge 266 - Odd Odd Times Even Even Times.xlsx"
    sheet_name = "Sheet1"
    column_name = "A:A"
    end_row = 10
    df = read_excel_data(file_name, sheet_name, column_name, end_row)
    result_df = df[df.iloc[:, 0].apply(analyze_digit_occurrences)]
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
