import pandas as pd
import sympy as primechecker

file_path = "Reversed Primes.xlsx"
COL_COUNT = 1
df = pd.read_excel(file_path, sheet_name="Sheet1")
df = df.iloc[:, :COL_COUNT]

def is_reverse_prime(number):
    reverse_number = str(number)[::-1]
    return primechecker.isprime(int(reverse_number))

new_df = df[df.apply(lambda x: is_reverse_prime(x["Number"]), axis=1)]
print(new_df)
