import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from imblearn.over_sampling import SMOTE
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

incidenti_df = pd.read_csv('incidenti.csv')
altro_df = pd.read_csv('altro.csv')

# Aggiungi una label "evento" per indicare il tipo di evento
incidenti_df['evento'] = 'incidenti'
altro_df['evento'] = 'altro'

# Concatenazione dataset
combined_df = pd.concat([incidenti_df, altro_df], ignore_index=True)


X = combined_df[['acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z']]
y = combined_df['evento']

# Applichiamo lo SMOTE per bilanciare le classi (altrimenti si sviluppa un bias verso le classi che hanno più dati)
smote = SMOTE(random_state=42)
X_smote, y_smote = smote.fit_resample(X, y)

# Divide il dataset bilanciato in training (80%) e test set (20%)
X_train, X_test, y_train, y_test = train_test_split(X_smote, y_smote, test_size=0.2, random_state=42)

# Addestriamo il modello
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Analisi quantitativa del modello:
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Matrice di confusione associata:
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=model.classes_, yticklabels=model.classes_)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

# Salviamo il modello
joblib.dump(model, 'model.joblib')
