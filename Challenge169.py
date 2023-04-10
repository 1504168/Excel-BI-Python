import pandas as pd
file_path = "Order Cities.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")
df = df.iloc[:,0:5]
non_nan_count =  df.count().to_frame(name="Non NaN count").reset_index()
correct_column_order = non_nan_count.sort_values(["Non NaN count","index"],ascending=[False,False])["index"].tolist()
final_df = df[correct_column_order]
print(final_df)