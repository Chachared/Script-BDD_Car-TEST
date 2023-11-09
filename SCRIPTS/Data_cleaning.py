import pandas as pd

# Spécifiez le chemin vers votre fichier Excel
input_file = "./BDD_steps/Clean_duplicates.xlsx"

# Spécifiez le nom du fichier Excel de sortie
output_file = "./BDD_steps/Data_cleaning.xlsx"

# Spécifiez le nom du fichier CSV pour faciliter la lecture et le débogage
debug_file = "./BDD_steps/Data_cleaning.csv"

# Charger le fichier Excel en spécifiant le nom de la feuille
df = pd.read_excel(input_file)


# Traiter les colonnes spécifiques
df['engine_Cyl'] = df['engine_Cyl'].str.replace(' ccm', '')
df['engine_Cyl'] = pd.to_numeric(df['engine_Cyl'], errors='coerce')

# Étape 1 : Supprimer les espaces des noms de colonnes
df.columns = [col.strip() for col in df.columns]

# Étape 2 : Supprimer les espaces dans les cellules
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Enregistrez le fichier modifié
df.to_excel(output_file, index=False)

# Comptez le nombre de lignes dans le fichier de sortie
num_output_rows = len(df)

# Écrire un fichier CSV pour faciliter la lecture et le débogage
df.to_csv(debug_file, index=False)

print(f"Le fichier '{input_file}' a été converti en '{output_file}'")
print(f"Un fichier CSV pour la lecture et le débogage a été créé : '{debug_file}'")
print(f"Nombre de lignes dans le fichier de sortie : {num_output_rows}")