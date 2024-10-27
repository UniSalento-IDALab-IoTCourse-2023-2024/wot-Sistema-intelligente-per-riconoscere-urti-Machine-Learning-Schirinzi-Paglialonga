import pandas as pd
import json

input_json_path = 'incident.json'

with open(input_json_path, 'r') as file:
    json_data = json.load(file)

df = pd.DataFrame(json_data)

# Vengono sostituiti i valori "null" con la media della feature corrispondente
df.fillna(df.mean(), inplace=True)

# Rinominiamo le colonne nel seguente modo
df.columns = ['acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z']

output_csv_path = 'dataset_addestramento.csv'

df.to_csv(output_csv_path, index=False)

print(f"File CSV creato: {output_csv_path}")
