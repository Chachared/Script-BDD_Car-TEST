import pandas as pd

# Spécifiez le chemin vers votre fichier Excel
input_file = "./BDD_steps/Convert_to_UTF8.xlsx"

# Spécifiez le nom du fichier CSV de sortie
output_file = "./BDD_steps/Select_columns.xlsx"

# Spécifiez le nom du fichier CSV pour faciliter la lecture et le débogage
debug_file = "./BDD_steps/Select_columns.csv"

# Charger le fichier en spécifiant le nom de la feuille
df = pd.read_excel(input_file)

# Etape 1: Supprimer les colonnes qui ne sont pas dans la BDD

if 'car_odooID' in df.columns:
    df.drop('car_odooID', axis=1, inplace=True)

if 'car_info_ID' in df.columns:
    df.drop('car_info_ID', axis=1, inplace=True)

if 'car_mod_ID' in df.columns:
    df.drop('car_mod_ID', axis=1, inplace=True)

if 'car_eng_ID' in df.columns:
    df.drop('car_eng_ID', axis=1, inplace=True)

if 'car_restriction_ID' in df.columns:
    df.drop('car_restriction_ID', axis=1, inplace=True)

if 'model_ID' in df.columns:
    df.drop('model_ID', axis=1, inplace=True)

if 'engine_ID' in df.columns:
    df.drop('engine_ID', axis=1, inplace=True)

if 'info_ID' in df.columns:
    df.drop('info_ID', axis=1, inplace=True)

if 'info_ABC' in df.columns:
    df.drop('info_ABC', axis=1, inplace=True)

if 'info_state' in df.columns:
    df.drop('info_state', axis=1, inplace=True)

if 'Doublon' in df.columns:
    df.drop('Doublon', axis=1, inplace=True)

# Sélectionner les colonnes dont le nom commence par "Unnamed:" et Supprimer ces colonnes du DataFrame
unnamed_columns = df.filter(like='Unnamed:', axis=1)
df = df.drop(columns=unnamed_columns)

# Etape 2: Ajouter les colonnes qui manquent dans la BDD
# Ajout de la nouvelle colonne "img_car" après la colonne "engine_type"
cols = list(df.columns)
idx_engine_type = cols.index('engine_type')
df.insert(idx_engine_type + 1, 'car_image', None)

# Enregistrez le fichier modifié
df.to_excel(output_file, index=False)

# Comptez le nombre de lignes dans le fichier de sortie
num_output_rows = len(df)

# Écrire un fichier CSV pour faciliter la lecture et le débogage
df.to_csv(debug_file, index=False)

print(f"Un fichier CSV pour la lecture et le débogage a été créé : '{debug_file}'")
print(f"Le fichier '{input_file}' a été converti en '{output_file}'")
print(f"Nombre de lignes dans le fichier de sortie : {num_output_rows}")