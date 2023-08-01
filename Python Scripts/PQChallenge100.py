# # Challenge Post : https://www.linkedin.com/feed/update/urn:li:activity:7091266157277515776/
import pandas as pd

file_name = "../Excel Files/PQ_Challenge_100.xlsx"
sheet_name = "Sheet1"
column_name = "A:D"
end_row =7
df = pd.read_excel(file_name, sheet_name=sheet_name, header=0, usecols=column_name)
df = df.loc[0:end_row-2, :]

def generate_date_map(row):
    from_date = row['From Date']
    to_date = row['To Date']
    rate = row['Rate']
    name = row['Name']
    if pd.isnull(to_date):
        to_date = pd.to_datetime(str(from_date.year) + '-12-31')
    # generate all the date from from_date to to_date including both
    date_range = pd.date_range(from_date, to_date)
    # filter date_range for holidays
    date_range = date_range[date_range.dayofweek < 5]
    # create a dataframe from date_range
    df = pd.DataFrame(date_range, columns=['Date'])
    df['Rate'] = rate
    df['Name'] = name
    return df

# apply generate_date_map function to each row of dataframe and store the results in a list
df_list = df.apply(generate_date_map, axis=1).tolist()
# convert df_list to a dataframe
new_df = pd.concat(df_list)
# add a quarter column to new_df which we will calculate from Date column
new_df['Quarter'] = new_df['Date'].dt.quarter
# group new_df by Quarter and Name and calculate sum of Rate
new_df = new_df.groupby(['Name','Quarter'],sort=False)['Rate'].sum().reset_index()

# Store the original order of 'Name' column
name_order = new_df['Name'].unique()

# pivot new_df to get desired output
new_df = new_df.pivot(index='Name', columns='Quarter', values='Rate')

# Reindex to maintain the original order
new_df = new_df.reindex(name_order)
print(new_df)
