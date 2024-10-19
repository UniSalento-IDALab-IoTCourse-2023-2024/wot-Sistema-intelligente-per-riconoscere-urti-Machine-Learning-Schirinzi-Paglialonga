import pandas as pd

# Percorsi dei due file CSV di input
input_file_1 = 'frenate.csv'  # Primo file CSV
input_file_2 = 'altro.csv'  # Secondo file CSV

# Percorso del file CSV di output
combined_file_path = 'altro.csv'

# Leggere i due file CSV in DataFrame separati
df1 = pd.read_csv(input_file_1)
df2 = pd.read_csv(input_file_2)

# Unire i due DataFrame
combined_df = pd.concat([df1, df2], ignore_index=True)

# Salvare il DataFrame combinato in un nuovo file CSV
combined_df.to_csv(combined_file_path, index=False)

print(f"I file CSV sono stati uniti e salvati in {combined_file_path}.")
