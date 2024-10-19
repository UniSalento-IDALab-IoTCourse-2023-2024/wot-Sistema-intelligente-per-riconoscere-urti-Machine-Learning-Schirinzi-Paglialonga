import json
import re

# Nome del file sorgente e di destinazione
input_file = 'incident.txt'
output_file = 'incident.json'

# Lista per memorizzare i dati formattati
data_list = []

# Funzione per correggere la formattazione del dizionario
def correct_format(text):
    # Aggiunge parentesi mancanti se necessario e corregge il separatore
    if "'acc'" in text and "'gyr'" in text and '}' not in text:
        text = '{' + text.replace("} 'gyr'", "}, 'gyr'") + '}'  # Aggiungi parentesi graffe e virgola tra i blocchi
    # Sostituisci None con null e sistema le virgolette
    text = text.replace("None", "null").replace("'", '"')
    return text

# Lettura del file di testo
with open(input_file, 'r') as file:
    content = file.read()
    # Dividi il contenuto del file in righe
    lines = content.splitlines()

    for line in lines:
        # Correggi la formattazione
        formatted_line = correct_format(line)
        # Parsing della stringa come dizionario
        try:
            record = json.loads(formatted_line)
            formatted_record = {
                "acc_x": record['acc']['x'],
                "acc_y": record['acc']['y'],
                "acc_z": record['acc']['z'],
                "gyr_x": record['gyr']['x'],
                "gyr_y": record['gyr']['y'],
                "gyr_z": record['gyr']['z']
            }
            data_list.append(formatted_record)
        except Exception as e:
            print(f"Errore nel parsing della riga: {line}")
            print(e)

# Scrittura dei dati in formato JSON
with open(output_file, 'w') as json_file:
    json.dump(data_list, json_file, indent=4)

print(f"File JSON creato: {output_file}")
