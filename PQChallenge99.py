# Challenge Post : https://www.linkedin.com/feed/update/urn:li:activity:7090903773715267584/

import pandas as pd
def read_excel_data(file_name, sheet_name, column_name, end_row):
    df = pd.read_excel(file_name, sheet_name=sheet_name, header=0, usecols=column_name)
    return df.loc[0:end_row - 2, :]


def add_month_column(df):
    df['Month'] = df['Date'].dt.month_name().str[:3]
    return df


def concat_dates(date_series):
    return ', '.join(date_series.astype(str).tolist())


def group_summary(group):
    min_val = group['Amount'].min()
    min_date = concat_dates(group[group['Amount'] == min_val]['Date'])

    max_val = group['Amount'].max()
    max_date = concat_dates(group[group['Amount'] == max_val]['Date'])

    # create series with required values
    return pd.Series({'Min': min_val, 'Min Date': min_date, 'Max': max_val, 'Max Date': max_date})


def perform_groupby(df):
    return df.groupby('Month', sort=False).apply(group_summary).reset_index()


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
