import pandas as pd

input_file_1 = 'frenate.csv'
input_file_2 = 'altro.csv'

combined_file_path = 'altro.csv'

df1 = pd.read_csv(input_file_1)
df2 = pd.read_csv(input_file_2)

# Concateniamo i 2 DataFrame
combined_df = pd.concat([df1, df2], ignore_index=True)

# Salviamo il data frame combinato in un nuovo file csv
combined_df.to_csv(combined_file_path, index=False)

print(f"I file CSV sono stati uniti e salvati in {combined_file_path}.")
