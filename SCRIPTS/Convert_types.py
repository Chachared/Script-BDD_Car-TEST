import pandas as pd
import re
import unicodedata
import binascii
import numpy as np


# Spécifiez le chemin vers votre fichier Excel
input_file = "./BDD_steps/Convert_date_type.xlsx"

# Spécifiez le nom du fichier Excel de sortie
output_file = "./BDD_steps/Convert_types.xlsx"

# Spécifiez le nom du fichier CSV pour faciliter la lecture et le débogage
debug_file = "./BDD_steps/Convert_types.csv"


# Charger le fichier Excel en spécifiant le nom de la feuille
df = pd.read_excel(input_file)

# Créez un dictionnaire des types de données attendus
expected_data_types = {
    "c4c_id": "bigint",
    "td_id": "bigint",
    "ebay_id": "bigint",
    "car_fuel": "varchar(50)",
    "car_nb_shift": "varchar(50)",
    "car_desc": "varchar(100)",
    "car_trans": "varchar(50)",
    "car_trim": "varchar(100)",
    "car_version": "varchar(100)",
    "car_plat": "varchar(100)",
    "car_y_from": "int",
    "car_y_to": "int",
    # repasser en date au lieu de str quand on résoudra le traitement des Nan vers postgre
    "car_d_from": "varchar(50)",
    # repasser en date au lieu de str quand on résoudra le traitement des Nan vers postgre
    "car_d_to": "varchar(50)",
    "car_ranking": "varchar(50)",
    "car_mark": "varchar(50)",
    "car_name": "varchar(100)",
    "car_doors": "varchar(50)",
    "car_chassis": "varchar(50)",
    "car_model_y_from": "int",
    "car_model_y_to": "int",
    "car_code": "varchar(50)",
    "car_engine_desc": "varchar(50)",
    "car_aspi": "varchar(50)",
    "car_alim": "varchar(50)",
    "car_name_cyl": "varchar(50)",
    "car_valve": "varchar(50)",
    "car_kw": "varchar(50)",
    "car_cv": "varchar(50)",
    "car_disp": "varchar(50)",
    "car_cyl": "int",
    "car_nb_cyl": "int",
    "car_type":"varchar(50)",
    "car_date_add": "date",
    "car_url": "varchar(255)",
    "car_user": "varchar(100)",
    "car_method": "varchar(50)",
    "car_valid": "boolean",
    "car_comment": "varchar(255)",
    # repasser en bytea quand on résoudra le problème de l'envoi vers postgre
    "car_image":"varchar(255)"
}

# # Colonne que vous souhaitez traiter en tant que bytea
# column_name = "car_image"

# # Définissez une fonction pour convertir des bytes en une chaîne hexadécimale
# def bytes_to_hex(byte_data):
#     if pd.notna(byte_data):
#         return binascii.hexlify(byte_data).decode('utf-8')
#     return None

# # Convertissez les données en chaînes hexadécimales
# df[column_name] = df[column_name].apply(bytes_to_hex)

# # Assurez-vous que la colonne "car_image" est de type object (chaîne de caractères)
# df[column_name] = df[column_name].astype('object')

# Nettoyer les caractères spéciaux
def clean_string(text):
    if pd.notna(text):
        if isinstance(text, (int, float)):
            # Si la valeur est un entier ou un flottant, convertissez-la en chaîne de caractères
            text = str(text)
        # Nettoyer les caractères non valides
        cleaned_text = ''.join([c for c in text if unicodedata.category(c)[0] in {'L', 'N', 'P', 'Z'}])
        return cleaned_text
    elif expected_type.startswith("varchar"):
        return " "  # Remplacez par une chaîne vide pour les colonnes varchar vides
    else:
        return text

# Nettoyez d'abord les colonnes qui doivent rester des chaînes de caractères
for column, expected_type in expected_data_types.items():
    if "varchar" in expected_type:
        df[column] = df[column].apply(clean_string)
    

# Boucle pour convertir les colonnes en fonction des types attendus
for column, expected_type in expected_data_types.items():
    if column in df.columns:
        if expected_type == "bigint" or expected_type == "int":
            try:
                # Convertissez la colonne en un type numérique
                df[column] = pd.to_numeric(df[column], errors='coerce')
                # Remplacez les valeurs non valides par 0
                df[column].fillna(0, inplace=True)
                # Convertissez en Int64 ou Int32 selon le type attendu
                if expected_type == "bigint":
                    df[column] = df[column].astype('Int64')
                elif expected_type == "int":
                    df[column] = df[column].astype('Int32')
            except ValueError:
                print(f"La colonne '{column}' contient des valeurs non valides for la conversion en int.")       

        elif expected_type.startswith("varchar"):
            # Conserver les colonnes en tant que chaînes de caractères
            varchar_length = int(re.search(r'\d+', expected_type).group())
            df[column] = df[column].astype('string').str[:varchar_length]
            df[column] = df[column].where(df[column].notna(), " ")

        elif column in df.columns and expected_type == "boolean":
            df[column] = df[column].str.lower()  # Convertir en minuscules
            df[column] = df[column].map({'true': 'true', 'false': 'false','1': 'true', '0': 'false'})  # Normaliser en 'true' ou 'false'
            df[column] = df[column].astype('string')  # Convertir en chaîne de caractères
            invalid_values = ~df[column].isin(['true', 'false'])
            df.loc[invalid_values, column] = 'false'
# Vérifiez les types des colonnes après conversion
for column, expected_type in expected_data_types.items():
    if column in df.columns:
        print(f"Type de la colonne '{column}': {df[column].dtype}")

# Enregistrez le fichier modifié
df.to_excel(output_file, index=False)

# Comptez le nombre de lignes dans le fichier de sortie
num_output_rows = len(df)

# Écrire un fichier CSV pour faciliter la lecture et le débogage
df.to_csv(debug_file, index=False)

print(f"Un fichier CSV pour la lecture et le débogage a été créé : '{debug_file}'")
print(f"Le fichier '{input_file}' a été converti en '{output_file}'")
print(f"Nombre de lignes dans le fichier de sortie : {num_output_rows}")

