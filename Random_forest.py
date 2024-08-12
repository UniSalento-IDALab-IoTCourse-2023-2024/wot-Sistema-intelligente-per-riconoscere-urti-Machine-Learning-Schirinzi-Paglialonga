import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from imblearn.over_sampling import SMOTE
import joblib

# Carica i dataset
frenate_df = pd.read_csv('fr.csv')
incidenti_df = pd.read_csv('dataset_addestramento.csv')
altro_df = pd.read_csv('oth.csv')

# Aggiungi una colonna "evento" per indicare il tipo di evento
frenate_df['evento'] = 'frenate'
incidenti_df['evento'] = 'incidenti'
altro_df['evento'] = 'altro'

# Combina i dataset
combined_df = pd.concat([frenate_df, incidenti_df, altro_df], ignore_index=True)

# Prepara le feature e le etichette
X = combined_df[['acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z']]
y = combined_df['evento']

# Applica SMOTE per bilanciare le classi
smote = SMOTE(random_state=42)
X_smote, y_smote = smote.fit_resample(X, y)

# Divide il dataset bilanciato in training e test set
X_train, X_test, y_train, y_test = train_test_split(X_smote, y_smote, test_size=0.2, random_state=42)

# Crea e addestra il modello
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Valuta il modello
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Salva il modello
joblib.dump(model, 'model.joblib')
