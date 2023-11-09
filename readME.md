# Documentation de Traitement-Conversion

Cette documentation fournit un guide pour le processus de traitement et de conversion des données à l'aide de plusieurs scripts Python. Ces scripts permettent de préparer un fichier Excel pour l'importation dans une base de données.

## Étapes du Traitement

Le processus de traitement et de conversion des données comprend les étapes suivantes :

1. **Nettoyage des Doublons** : Le script `Clean_duplicates.py` supprime les doublons dans les colonnes CAR_C4C_ID et CAR_TDID, corrige les valeurs non numériques et ajoute des identifiants manquants.

2. **Nettoyage des Données** : Le script `Data_cleaning.py` effectue diverses opérations de nettoyage, telles que la suppression des espaces inutiles dans les colonnes.

3. **Conversion en UTF-8** : Le script `Convert_to_UTF8.py` convertit le fichier en UTF-8 pour assurer la compatibilité.

4. **Sélection de Colonnes** : Le script `Select_columns.py` permet de sélectionner des colonnes spécifiques à conserver dans le fichier final.

5. **Renommage des Colonnes** : Le script `Rename_columns.py` renomme les colonnes avec des noms plus significatifs.

6. **Conversion des Dates au Format ISO8601** : Le script `Convert_dates_ISO8601.py` convertit les dates au format ISO8601 pour une meilleure gestion des dates.

7. **Conversion des Types de Données** : Le script `Convert_date_type.py` assure que les types de données sont corrects.

8. **Conversion de Types** : Le script `Convert_types.py` convertit les types de données selon les besoins.

9. **Insertion dans la BDD la première fois** : Le script `DB_insert_first.py` permet d'insérer les données depuis un fichier Excel dans la base de données PostgreSQL la première fois.

10. **Mise à jour de la BDD** : Le script `DB_insert_update.py` est utilisé pour effectuer des mises à jour de la base de données après la première insertion.

Chaque étape est réalisée à l'aide d'un script Python dédié. Vous pouvez exécuter ces scripts dans l'ordre spécifié pour préparer vos données en vue de leur importation dans une base de données. Il faut simplement choisir l'exécution du script d'insertion en BDD approprié.

## Instructions d'Exécution

Pour exécuter les scripts, vous pouvez utiliser la ligne de commande Python. Par exemple, pour exécuter le script `Clean_duplicates.py`, utilisez la commande suivante :

```bash
python SCRIPTS/Clean_duplicates.py
```

## Script 1: Clean_duplicates.py

### Résumé

Ce script nettoie un fichier Excel en supprimant les doublons dans les colonnes CAR_C4C_ID et CAR_TDID, en ajoutant des identifiants manquants et en corrigeant les valeurs non numériques.

### Prérequis

- Python installé.
- Bibliothèque Pandas installée (vous pouvez l'installer avec `pip install pandas`).

### Étapes

1. **Chargement du Fichier :** Charge le fichier Excel cible. Veiller à bien indiquer le fichier utile à traiter.

2. **Gestion des Doublons :** Identifie et gère les doublons dans CAR_C4C_ID.

3. **Traitement des CAR_C4C_ID :** Nettoie et numérise les valeurs.

4. **Ajout d'Identifiants :** Ajoute des identifiants manquants.

5. **Gestion des Doublons de CAR_TDID :** Identifie et gère les doublons dans CAR_TDID.

6. **Traitement des CAR_TDID :** Corrige les valeurs non numériques.

7. **Enregistrement du Fichier Modifié :** Enregistre le fichier Excel sans doublons.

8. **Enregistrement d'un Fichier CSV :** Enregistre un fichier CSV pour la lecture et le débogage.

9. **Affichage des Statistiques :** Affiche des statistiques.

### Utilisation

Pour exécuter le script, utilisez la commande suivante :

```bash
python Clean_duplicates.py
```

## Script 2: Data_cleaning.py

### Résumé

Ce script effectue des opérations de nettoyage sur un fichier Excel en supprimant les espaces inutiles dans les noms de colonnes et les cellules. Il traite également la colonne 'engine_Cyl' en remplaçant les occurrences de ' ccm' et en convertissant les valeurs en numériques.

### Prérequis

- Python installé.
- Bibliothèque Pandas installée (vous pouvez l'installer avec `pip install pandas`).

### Étapes

1. **Chargement du Fichier :** Charge le fichier Excel de sortie du script précédent.

2. **Suppression des Espaces dans les Noms de Colonnes :** Élimine les espaces inutiles dans les noms de colonnes.

3. **Suppression des Espaces dans les Cellules :** Supprime les espaces inutiles dans les cellules, en conservant les autres valeurs intactes.

4. **Traitement de la Colonne 'engine_Cyl' :** Remplace les occurrences de ' ccm' dans la colonne 'engine_Cyl'.

5. **Conversion des Valeurs en Numériques :** Convertit les valeurs de la colonne 'engine_Cyl' en numériques.

6. **Enregistrement du Fichier Modifié :** Enregistre le fichier Excel après le nettoyage.

7. **Enregistrement d'un Fichier CSV :** Enregistre un fichier CSV pour la lecture et le débogage.

8. **Affichage des Statistiques :** Affiche des statistiques, y compris le nombre de lignes dans le fichier de sortie.

### Utilisation

Pour exécuter le script, utilisez la commande suivante :

```bash
python Data_cleaning.py
```

## Script 3: Convert_to_UTF8.py

### Résumé

Ce script convertit un fichier Excel en UTF-8 pour garantir la compatibilité. Il encodera les valeurs des cellules en UTF-8.

### Prérequis

- Python installé.
- Bibliothèque Pandas installée (vous pouvez l'installer avec `pip install pandas`).

### Étapes

1. **Chargement du Fichier :** Charge le fichier Excel de sortie du script précédent après le nettoyage des données.

2. **Conversion en UTF-8 :** Encode les valeurs de chaque cellule du DataFrame en UTF-8.

3. **Enregistrement du Fichier Modifié :** Enregistre le fichier Excel converti en UTF-8.

4. **Enregistrement d'un Fichier CSV :** Enregistre un fichier CSV pour la lecture et le débogage.

5. **Affichage des Statistiques :** Affiche des statistiques, y compris le nombre de lignes dans le fichier de sortie.

### Utilisation

Pour exécuter le script, utilisez la commande suivante :

```bash
python Convert_to_UTF8.py
```

## Script 4: Select_columns.py

### Résumé

Ce script permet de sélectionner les colonnes spécifiques à conserver dans le fichier Excel. Il supprime les colonnes non requises et ajoute de nouvelles colonnes au besoin.

### Prérequis

- Python installé.
- Bibliothèque Pandas installée (vous pouvez l'installer avec `pip install pandas`).

### Étapes

1. **Chargement du Fichier :** Charge le fichier Excel de sortie du script précédent converti en UTF-8.

2. **Suppression des Colonnes Non Requises :** Supprime les colonnes non nécessaires dans le DataFrame. Les colonnes supprimées sont spécifiées et incluent "car_odooID," "car_info_ID," "car_mod_ID," "car_eng_ID," "car_restriction_ID," "model_ID," "engine_ID," "info_ID," "info_ABC," "info_state," et "Doublon."

3. **Suppression des Colonnes "Unnamed:" :** Supprime les colonnes dont le nom commence par "Unnamed:".

4. **Ajout de Nouvelles Colonnes :** Ajoute une nouvelle colonne "car_image" après la colonne "engine_type."

5. **Enregistrement du Fichier Modifié :** Enregistre le fichier Excel modifié.

6. **Enregistrement d'un Fichier CSV :** Enregistre un fichier CSV pour la lecture et le débogage.

7. **Affichage des Statistiques :** Affiche des statistiques, y compris le nombre de lignes dans le fichier de sortie.

### Utilisation

Pour exécuter le script, utilisez la commande suivante :

```bash
python Select_columns.py
```

## Script 5: Rename_columns.py

### Résumé

Ce script renomme les colonnes d'un fichier Excel conformément à la structure de la base de données.

### Prérequis

- Python installé.
- Bibliothèque Pandas installée (vous pouvez l'installer avec `pip install pandas`).

### Étapes

1. **Chargement du Fichier :** Charge le fichier Excel de sortie du script précédent après sélection des colonnes.

2. **Renommage des Colonnes :** Renomme les colonnes de l'Excel pour qu'elles correspondent à la structure de la base de données. Les colonnes renommées incluent "car_ebayID," "car_tdID," "car_c4cID," "car_nbShift," "ABC_ranking," "model_mark," "model_name," "model_doors," "model_chassis," "model_YFrom," "model_YTo," "engine_code," "engine_desc," "engine_aspi," "engine_alim," "engine_nameCyl," "engine_valve," "engine_KW," "engine_CV," "engine_disp," "engine_Cyl," "engine_nbCyl," "engine_type," "info_dateAdd," "info_URL," "info_user," "info_method," "info_valid," et "info_comment."

3. **Enregistrement du Fichier Modifié :** Enregistre le fichier Excel avec les colonnes renommées.

4. **Enregistrement d'un Fichier CSV :** Enregistre un fichier CSV pour la lecture et le débogage.

5. **Affichage des Statistiques :** Affiche des statistiques, y compris le nombre de lignes dans le fichier de sortie.

### Utilisation

Pour exécuter le script, utilisez la commande suivante :

```bash
python Rename_columns.py
```

## Script 6: Convert_dates_ISO8601.py

### Résumé

Ce script renomme et formate les dates dans un fichier Excel au format ISO8601, modifie le format de la date d'une colonne et réorganise les colonnes du fichier.

### Prérequis

- Python installé.
- Bibliothèque Pandas installée (vous pouvez l'installer avec `pip install pandas`).

### Étapes

1. **Chargement du Fichier :** Charge le fichier Excel après le renommage des colonnes.

2. **Renommer et Formater "car_YFrom" :** Renomme la colonne "car_YFrom" en "car_d_from."

3. **Renommer et Formater "car_YTo" :** Renomme la colonne "car_YTo" en "car_d_to."

4. **Créer une Colonne "car_y_from" :** Crée une colonne "car_y_from" et y écrit la première année de la colonne "car_year."

5. **Créer une Colonne "car_y_to" :** Crée une colonne "car_y_to" et y écrit la deuxième année de la colonne "car_year."

6. **Vérifier et Supprimer "car_year" :** Vérifie que toutes les données de "car_year" ont bien été réécrites dans les colonnes "car_y_from" et "car_y_to." Supprime la colonne "car_year."

7. **Réorganiser les Colonnes :** Réorganise les colonnes pour placer "car_y_from" et "car_y_to" après "car_d_to."

8. **Formater ISO8601 la Colonne "car_date_add" :** Formate la colonne "car_date_add" au format ISO8601.

9. **Enregistrement du Fichier Modifié :** Enregistre le fichier Excel avec les dates au format ISO8601 et les colonnes réorganisées.

10. **Enregistrement d'un Fichier CSV :** Enregistre un fichier CSV pour la lecture et le débogage.

11. **Affichage des Statistiques :** Affiche des statistiques, y compris le nombre de lignes dans le fichier de sortie.

### Utilisation

Pour exécuter le script, utilisez la commande suivante :

```bash
python Convert_dates_ISO8601.py
```

## Script 7: Convert_date_type.py

### Résumé

Ce script convertit les colonnes de dates au format ISO8601 en types de données appropriés, traite les données invalides et enregistre les données invalides dans un fichier CSV.

### Prérequis

- Python installé.
- Bibliothèque Pandas installée (vous pouvez l'installer avec `pip install pandas`).
- Module `datetime` pour manipuler les dates.

### Étapes

1. **Chargement du Fichier :** Charge le fichier Excel avec les dates au format ISO8601.

2. **Conversion des Colonnes en Chaînes de Caractères :** Convertit les colonnes de dates en chaînes de caractères.

3. **Conversion en Types de Données Appropriés :** Convertit les chaînes de caractères en types de données appropriés, traite les données invalides et remplace les valeurs manquantes.

4. **Filtrage des Données Invalides :** Filtrage des lignes avec des données invalides ou non remplies dans la colonne 'car_date_add'.

5. **Enregistrement des Données Invalides :** Enregistre les données invalides dans un fichier CSV.

6. **Enregistrement du Fichier Modifié :** Enregistre le fichier Excel avec les dates converties en types de données appropriés.

7. **Affichage des Statistiques :** Affiche des statistiques, y compris le nombre de lignes dans le fichier de sortie.

### Utilisation

Pour exécuter le script, utilisez la commande suivante :

```bash
python Convert_date_type.py
```

## Script 8: Convert_types.py

### Résumé

Ce script convertit les types de données des colonnes dans un fichier Excel en utilisant un dictionnaire de types de données attendus. Il traite également les caractères spéciaux, convertit les valeurs en hexadécimal et nettoie les colonnes pour respecter les types attendus.

### Prérequis

- Python installé.
- Bibliothèque Pandas installée (vous pouvez l'installer avec `pip install pandas`).
- Module `re` pour les expressions régulières.
- Module `unicodedata` pour nettoyer les caractères spéciaux.
- Module `binascii` pour convertir des bytes en hexadécimal.
- Module `numpy` pour manipuler les données.

### Étapes

1. **Chargement du Fichier :** Charge le fichier Excel avec les données.

2. **Création d'un Dictionnaire des Types Attendus :** Crée un dictionnaire des types de données attendus pour chaque colonne.

3. **Conversion des Colonnes en Chaînes Hexadécimales :** Convertit les données de la colonne spécifiée en hexadécimal.

4. **Conversion des Colonnes en Types de Données Attendus :** Convertit les colonnes en fonction des types de données attendus. Les valeurs non valides sont traitées et les colonnes sont nettoyées pour respecter les types attendus.

5. **Enregistrement du Fichier Modifié :** Enregistre le fichier Excel avec les types de données convertis.

6. **Affichage des Statistiques :** Affiche des statistiques, y compris le nombre de lignes dans le fichier de sortie.

### Utilisation

Pour exécuter le script, utilisez la commande suivante :

```bash
python Convert_types.py
```

## Script 9: DB_insert.py

### Résumé

Ce script insère les données d'un fichier Excel dans une base de données PostgreSQL en utilisant la bibliothèque `psycopg2`. Il effectue également le mappage des colonnes du fichier Excel avec les champs de la base de données et traite spécifiquement la colonne "car_date_add".

### Prérequis

- PostgreSQL installé.
- Bibliothèque psycopg2 installée (vous pouvez l'installer avec `pip install psycopg2`).
- Bibliothèque Pandas installée (vous pouvez l'installer avec `pip install pandas`).
- Fichier Excel avec les données à insérer.

### Étapes

1. **Établissement de la Connexion à la Base de Données :** Établit une connexion à la base de données PostgreSQL en utilisant les informations de connexion spécifiées.

2. **Initialisation des Variables :** Initialise un compteur pour suivre le nombre de lignes insérées en BDD, un dictionnaire pour suivre le nombre d'ajouts par colonne et un dictionnaire de mappage entre les colonnes du fichier Excel et les champs de la base de données.

3. **Chargement des Données depuis le Fichier Excel :** Charge les données depuis le fichier Excel.

4. **Boucle d'Insertion :** Parcourt les lignes du fichier Excel, effectue le mappage des colonnes et des champs, traite spécifiquement la colonne "car_date_add" et exécute les requêtes d'insertion dans la base de données.

5. **Validation et Fermeture de la Connexion :** Valide les insertions, effectue la commit et ferme la connexion à la base de données.

6. **Affichage des Statistiques :** Affiche un message de réussite d'insertion dans la base de données ainsi que le nombre d'ajouts par colonne (à l'exception des NULL).

### Utilisation

Pour exécuter le script, utilisez la commande suivante :

```bash
python DB_insert.py
```

## Script 10: DB_insert_first.py

### Résumé

Le script `DB_insert_first.py` est utilisé pour peupler la base de données PostgreSQL la première fois, en insérant les données depuis un fichier Excel. Il effectue le mappage des colonnes du fichier Excel avec les champs de la base de données et traite spécifiquement la colonne "car_date_add".

### Prérequis

- PostgreSQL installé.
- Bibliothèque psycopg2 installée (vous pouvez l'installer avec `pip install psycopg2`).
- Bibliothèque Pandas installée (vous pouvez l'installer avec `pip install pandas`).
- Fichier Excel avec les données à insérer.

### Étapes

1. **Établissement de la Connexion à la Base de Données :** Établit une connexion à la base de données PostgreSQL en utilisant les informations de connexion spécifiées.

2. **Initialisation des Variables :** Initialise un compteur pour suivre le nombre de lignes insérées en BDD, un dictionnaire pour suivre le nombre d'ajouts par colonne et un dictionnaire de mappage entre les colonnes du fichier Excel et les champs de la base de données.

3. **Chargement des Données depuis le Fichier Excel :** Charge les données depuis le fichier Excel.

4. **Boucle d'Insertion :** Parcourt les lignes du fichier Excel, effectue le mappage des colonnes et des champs, traite spécifiquement la colonne "car_date_add" et exécute les requêtes d'insertion dans la base de données.

5. **Validation et Fermeture de la Connexion :** Valide les insertions, effectue la commit et ferme la connexion à la base de données.

6. **Affichage des Statistiques :** Affiche un message de réussite d'insertion dans la base de données ainsi que le nombre d'ajouts par colonne (à l'exception des NULL).

### Utilisation

Pour exécuter le script, utilisez la commande suivante :

```bash
python DB_insert_first.py
```

