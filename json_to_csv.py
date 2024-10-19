import pandas as pd
import json

# Percorso del file JSON di input
input_json_path = 'incident.json'

# Leggere i dati dal file JSON
with open(input_json_path, 'r') as file:
    json_data = json.load(file)

# Creare il DataFrame dai dati JSON
df = pd.DataFrame(json_data)

# Sostituire i valori null con la media della feature in esame
df.fillna(df.mean(), inplace=True)

# Aggiungere la colonna crash
df['crash'] = "yes"

# Rinomina le colonne come richiesto
df.columns = ['acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z', 'crash']

# Percorso del file CSV di output
output_csv_path = 'dataset_addestramento.csv'

# Salvare il DataFrame in un file CSV
df.to_csv(output_csv_path, index=False)

print(f"File CSV creato: {output_csv_path}")
