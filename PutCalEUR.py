import pandas as pd

# Load the Excel file
df = pd.read_excel("EURUSD-Mon.xls")

# Separate the call and put data, adjusting the rows and columns as needed
df = df.iloc[19:, :10]
df.columns = df.iloc[1]
df.index = df.Strike
df.drop("Strike", axis=1, inplace=True)
call = df.iloc[:45]
put = df.iloc[46:98]

# Filter the call data where the orders have changed
call_filtered = call.iloc[2:]
call_filtered['Globex'] = pd.to_numeric(call_filtered['Globex'], errors='coerce')
call_filtered = call_filtered.dropna(subset=['Globex'])
call_result = call_filtered[call_filtered['Globex'] >= 1]
print(call_result)

# Filter the put data where the orders have changed
put['Globex'] = pd.to_numeric(put['Globex'], errors='coerce')
put = put.dropna(subset=['Globex'])
put_result = put[put['Globex'] >= 1]
print(put_result)
