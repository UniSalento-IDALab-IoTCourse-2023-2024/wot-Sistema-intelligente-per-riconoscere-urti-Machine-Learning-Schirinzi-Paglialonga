import pandas as pd

# Elenco dei percorsi dei file CSV di input
file_paths = [
    'oth1.csv',
    'oth2.csv',
    'oth3.csv',
    'oth4.csv',
    'oth5.csv',
    'oth6.csv',
    'oth7.csv',
    'oth8.csv'
]

# Percorso del file CSV di output
combined_file_path = 'oth.csv'

# Lista per memorizzare i DataFrame
dataframes = []

# Leggere ogni file CSV e aggiungerlo alla lista
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Unire tutti i DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Salvare il DataFrame combinato in un nuovo file CSV
combined_df.to_csv(combined_file_path, index=False)

print(f"I file CSV sono stati uniti e salvati in {combined_file_path}.")
