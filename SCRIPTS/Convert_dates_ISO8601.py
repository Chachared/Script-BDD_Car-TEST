import pandas as pd

# Spécifiez le chemin vers votre fichier Excel
input_file = "./BDD_steps/Rename_columns.xlsx"

# Spécifiez le nom du fichier CSV de sortie
output_file = "./BDD_steps/Convert_dates_ISO8601.xlsx"

# Spécifiez le nom du fichier CSV pour faciliter la lecture et le débogage
debug_file = "./BDD_steps/Convert_dates_ISO8601.csv"

# Charger le fichier Excel en spécifiant le nom de la feuille
df = pd.read_excel(input_file)

# Étape 1: Renommer et formater "car_YFrom"
if 'car_YFrom' in df.columns:
    # df['car_YFrom'] = pd.to_datetime(df['car_YFrom'], format='%d/%m/%Y', errors='coerce')
    # df['car_YFrom'] = df['car_YFrom'].dt.strftime('%Y-%m-%d')
    df.rename(columns={'car_YFrom': 'car_d_from'}, inplace=True)

# Étape 2: Renommer et formater "car_YTo"
if 'car_YTo' in df.columns:
    # df['car_YTo'] = pd.to_datetime(df['car_YTo'], format='%d/%m/%Y', errors='coerce')
    # df['car_YTo'] = df['car_YTo'].dt.strftime('%Y-%m-%d')
    df.rename(columns={'car_YTo': 'car_d_to'}, inplace=True)

# Étape 3: Créer une colonne "car_y_from" et y écrire la première année de la colonne "car_year"
if 'car_year' in df.columns:
    df['car_y_from'] = df['car_year'].str.split('-').str[0]

# Étape 4: Créer une colonne "car_y_to" et y écrire la deuxième année de la colonne "car_year"
if 'car_year' in df.columns:
    df['car_y_to'] = df['car_year'].str.split('-').str[1]

# Étape 5: Vérifier que toutes les données de "car_year" ont bien été réécrites dans les colonnes "car_y_from" et "car_y_to"
if 'car_year' in df.columns:
    df.drop('car_year', axis=1, inplace=True)

# Étape 6: Réorganiser les colonnes
if 'car_d_to' in df.columns and 'car_y_from' in df.columns and 'car_y_to' in df.columns:
    cols = list(df.columns)
    cols.remove('car_y_from')
    cols.remove('car_y_to')
    idx_d_to = cols.index('car_d_to')
    cols.insert(idx_d_to + 1, 'car_y_from')
    cols.insert(idx_d_to + 2, 'car_y_to')
    df = df[cols]

# Étape 7: Formater ISO8601 la colonne "car_date_add"
if 'car_date_add' in df.columns:
    df['car_date_add'] = pd.to_datetime(df['car_date_add'], format='%d/%m/%Y', errors='coerce')
    df['car_date_add'] = df['car_date_add'].dt.strftime('%Y-%m-%d')

# Enregistrez le fichier modifié
df.to_excel(output_file, index=False)

# Comptez le nombre de lignes dans le fichier de sortie
num_output_rows = len(df)

# Écrire un fichier CSV pour faciliter la lecture et le débogage
df.to_csv(debug_file, index=False)

print(f"Un fichier CSV pour la lecture et le débogage a été créé : '{debug_file}'")
print(f"Le fichier '{input_file}' a été converti en '{output_file}'")
print(f"Nombre de lignes dans le fichier de sortie : {num_output_rows}")