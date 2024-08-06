import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Carica i dataset
frenate_df = pd.read_csv('fr.csv')
incidenti_df = pd.read_csv('dataset_addestramento.csv')
altro_df = pd.read_csv('oth.csv')

# Aggiungi una colonna "evento" per indicare il tipo di evento
frenate_df['evento'] = 'frenate'
incidenti_df['evento'] = 'incidenti'
altro_df['evento'] = 'altro'

# Divide ciascun dataset in training e test set
frenate_train, frenate_test = train_test_split(frenate_df, test_size=0.2, random_state=42)
incidenti_train, incidenti_test = train_test_split(incidenti_df, test_size=0.2, random_state=42)
altro_train, altro_test = train_test_split(altro_df, test_size=0.2, random_state=42)

# Combina i dati di training
train_data = pd.concat([frenate_train, incidenti_train, altro_train], ignore_index=True)

# Combina i dati di test
test_data = pd.concat([frenate_test, incidenti_test, altro_test], ignore_index=True)

# Prepara le feature e le etichette per il training set
X_train = train_data[['acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z']]
y_train = train_data['evento']

# Prepara le feature e le etichette per il test set
X_test = test_data[['acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z']]
y_test = test_data['evento']

# Crea e addestra il modello
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Valuta il modello
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Esempio di predizione
esempio = pd.DataFrame({
    'acc_x': [0.1],
    'acc_y': [0.2],
    'acc_z': [0.3],
    'gyro_x': [0.0],
    'gyro_y': [0.0],
    'gyro_z': [0.0]
})
predizione = model.predict(esempio)
print("Predizione per l'esempio:", predizione[0])
