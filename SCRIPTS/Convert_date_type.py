import pandas as pd
from datetime import datetime

# Spécifiez le chemin vers votre fichier Excel
input_file = "./BDD_steps/Convert_dates_ISO8601.xlsx"

# Spécifiez le nom du fichier CSV de sortie
output_file = "./BDD_steps/Convert_date_type.xlsx"

# Spécifiez le nom du fichier CSV pour les données invalides
invalid_data_file = "./BDD_steps/Invalid_car_date_add.csv"

# Charger le fichier Excel en spécifiant le nom de la feuille
df = pd.read_excel(input_file)

# # Liste des colonnes 'object' à convertir en datetime
columns_to_convert = ['car_d_from', 'car_d_to']
for column in columns_to_convert:
    df[column] = df[column].astype(str)

# for column in columns_to_convert:
#     df[column] = pd.to_datetime(df[column], format='%Y-%m-%d', errors='coerce')
#     df[column] = df[column].apply(lambda x: x.date() if pd.notna(x) else None)  # Remplacez NaT par None
#     df[column].replace({pd.NaT: None}, inplace=True)  # Remplacez NaT par None

# for column in columns_to_convert:
    # df[column] = pd.to_datetime(df[column], format='%Y-%m-%d', errors='coerce')
    # df[column] = df[column].apply(lambda x: x.date() if pd.notna(x) else None)  # Remplacez NaT par None
    # df[column] = df[column].fillna(None, inplace=True)

# Vérification des types de la colonne avec le nombre
# type_counts = df[column].apply(type).value_counts()
# print(f"Types de données dans la colonne '{column}':\n{type_counts}")
# print(f"Type de la colonne '{column}': {df[column].dtype}")

# Filtrer les lignes avec des données invalides ou non remplies dans la colonne 'car_date_add'
invalid_data = df[pd.isna(df['car_date_add']) | (df['car_date_add'] == pd.NaT)]

# Maintenant, traitons la colonne 'car_date_add'
car_date_add_column = 'car_date_add'
df[car_date_add_column] = pd.to_datetime(df[car_date_add_column], format='%Y-%m-%d', errors='coerce')
df[car_date_add_column] = df[car_date_add_column].apply(lambda x: x.date() if pd.notna(x) else datetime.today().date())

# Enregistrez les données invalides dans un fichier CSV
invalid_data.to_csv(invalid_data_file, index=False)

# Enregistrez le DataFrame modifié dans un fichier Excel
df.to_excel(output_file, index=False)

# Comptez le nombre de lignes dans le fichier de sortie
num_output_rows = len(df)

print(f"Un fichier CSV pour les données invalides a été créé : '{invalid_data_file}'")
print(f"Le fichier '{input_file}' a été converti en '{output_file}'")
print(f"Nombre de lignes dans le fichier de sortie : {num_output_rows}")