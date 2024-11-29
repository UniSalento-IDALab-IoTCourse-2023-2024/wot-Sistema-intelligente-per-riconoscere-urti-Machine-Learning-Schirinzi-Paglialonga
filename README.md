# C.A.R.E. 
- - -

## Panoramica
- - -


Il progetto __C.A.R.E.__ si pone l'obiettivo di creare un'app Android per raccogliere dati dai sensori di accelerometro e giroscopio montati su uno smartphone; questi vengono inviati in tempo reale ad un algoritmo di Machine Learning che classifica i dati raccolti in una classe del tipo “incidente” o “altro”. Con il termine "altro" si raggruppano tutti gli eventi di accelerazione constante, accelerazione improvvisa, frenata constante, frenata improvvisa, svolta a destra e svolta a sinistra. Se l’evento rilevato è “incidente”, il fenomeno in questione viene memorizzato all’interno di un database MongoDB per essere analizzato meglio in seguito dall’admin dell’app (responsabile della compagnia assicurativa) mediante opportune dashboard.
L'interfaccia è facile ed intuitiva e permette agli utenti di registrarsi, fare il login, di visualizzare in tempo reale i dati di accelerometro e giroscopio e l’evento che è stato rilevato. 

## ARCHITETTURA DEL SISTEMA
- - -

<div align="center">
  <img src="https://i.ibb.co/0GdR93q/Immagine-Whats-App-2024-11-13-ore-18-59-09-a730b518.jpg" alt="Architettura" width="400"/>
</div>



Le componenti principali dell’architettura sono: 

-	__Front end:__ Realizzato con Flutter, prevede inizialmente un’interfaccia di login e registrazione e, una volta loggato, l’utente può navigare all’interno della sua area riservata visualizzando i dati di accelerometro e giroscopio raccolti in tempo reale, lo storico dei suoi incidenti e le sue informazioni personali, con l’opportunità di poterle modificare. 

-	__Android Studio:__ Grazie all’utilizzo di questo IDE si è creata un’app in grado si acquisire dati in tempo reale dai sensori (accelerometro e giroscopio) situati sullo smartphone su cui l’app viene eseguita.
	Una volta acquisiti vengono inviati, grazie al protocollo MQTT, all’algoritmo di ML che classifica i dati in eventi di incidenti ed altro;

-	__Python:__ Si è addestrato un modello di Random Forest che è in grado di classificare, in base ai dati ricevuti in input, un evento, distinguendolo in una di queste due classi: incidente e altro.
Inoltre, grazie al framework Flask, si sono sviluppate delle API che hanno permesso alle varie componenti dell'applicazione di comunicare con il database MongoDB.


## REPOSITORY DEI COMPONENTI:
- - -
- Machine Learning C.A.R.E.: [Link al repository][git-repo-url1]
- Back-end C.A.R.E.: [Link al repository][git-repo-url2]
- Front-end C.A.R.E.: [Link al repository][git-repo-url3]
- [Pagina web][link_pagina_web]

## MACHINE LEARNING C.A.R.E.
- - - 

## 1. Preparazione e pulizia dei dati

I dati sugli incidenti rappresentati mediante un file json sono stati trasformati in un DataFrame e sottoposti a pulizia: tutti i valori nulli sono stati sostituiti con la media della rispettiva colonna per evitare che eventuali mancanze influenzino negativamente il modello. Successivamente, le colonne sono state rinominate per rispecchiare le misurazioni dei sensori di accelerazione e giroscopio, facilitando la comprensione e la gestione delle variabili. Questo set di dati è stato poi esportato in formato CSV per l’addestramento del modello.

L'obiettivo è addestrare un modello capace di distinguere un incidente da un evento classificato come "altro" (accelerazione costante, accelerazione improvvisa, frenata costante, frenata improvvisa, svolta a destra e svolta a sinistra). Per includere anche questi eventi, sono stati cercati online dataset aggiuntivi rappresentativi della categoria "altro". In particolare, tramite la piattaforma [Kaggle][link_kaggle] è stato trovato un dataset adeguato ai nostri scopi.

Successivamente, il dataset è stato etichettato aggiungendo una colonna che distingue gli eventi di "incidente" rispetto a quelli di "altro", creando così un set di dati unificato per il training. Poiché i dati non erano bilanciati (con più esempi di una classe rispetto all’altra), è stata applicata la tecnica SMOTE, che genera esempi sintetici per la classe minoritaria, equilibrando così le classi ed evitando che il modello sviluppi un bias verso la classe maggioritaria.

Il dataset bilanciato è stato suddiviso in due parti: un set di addestramento (80%) e un set di test (20%), in modo da poter addestrare il modello e poi valutarne le prestazioni su dati nuovi, andandone cosi a testare la capacità di generalizzare.


## Addestramento modello

1. Installazione dipendenze
  ```
    pip install pandas
    pip install scikit-learn
    pip install imbalanced-learn
    pip install joblib
    pip install matplotlib
    pip install seaborn
   ```
2. Addestramento del modello Random Forest
 ```
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
 ```
3. Prestazioni ottenute

<div align="center">
  <img src="https://i.ibb.co/ccp5zSp/Immagine-Whats-App-2024-11-13-ore-18-58-19-b874d811.jpg" alt="Matrice_confusione" width="300"/>
  <img src="https://i.ibb.co/wLPjXMc/Immagine-Whats-App-2024-11-13-ore-18-58-07-6ca5a8a6.jpg" alt="Report" width="300"/>
</div>




  
   [git-repo-url1]: <https://github.com/UniSalento-IDALab-IoTCourse-2023-2024/wot-Sistema-intelligente-per-riconoscere-urti-Machine-Learning>
   
   [git-repo-url2]: <https://github.com/UniSalento-IDALab-IoTCourse-2023-2024/wot-Sistema-intelligente-per-riconoscere-urti-Backend>
    
   [git-repo-url3]: <https://github.com/UniSalento-IDALab-IoTCourse-2023-2024/wot-Sistema-intelligente-per-riconoscere-urti-Frontend>
   
   [link_pagina_web]: <https://unisalento-idalab-iotcourse-2023-2024.github.io/wot-project-presentation-Schirinzi-Paglialonga/>

   [link_kaggle]: <https://www.kaggle.com/datasets/saboorahmad47/harsh-driving-dataset?select=paved_sudden-right-line-chg_const-acc-at-40kmph_22-3-2023_20-2-54.csv.>
   
   
   
   
   
   
   
   
   
   
  
