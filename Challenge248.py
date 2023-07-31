# Challenge Post : https://www.linkedin.com/posts/excelbi_excel-excelchallenge-powerquerychallenge-activity-7090541381185675264-C1Uv/

import pandas as pd
def read_excel_data(file_name, sheet_name, column_name, end_row):
    df = pd.read_excel(file_name, sheet_name=sheet_name, header=0, usecols=column_name)
    return df.loc[0:end_row - 2, :]

def main():
    file_name = "PQ_Challenge_99.xlsx"
    sheet_name = "Sheet1"
    column_name = "A:B"
    end_row = 366

    df = read_excel_data(file_name, sheet_name, column_name, end_row)
    df = add_month_column(df)

    df_summary = perform_groupby(df)
    print(df_summary)

if __name__ == "__main__":
    main()
