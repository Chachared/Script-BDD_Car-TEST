import pandas as pd

# Spécifiez le chemin vers votre fichier Excel
input_file = "./BDD_steps/Data_cleaning.xlsx"

# Spécifiez le nom du fichier CSV de sortie
output_file = "./BDD_steps/Convert_to_UTF8.xlsx"

# Spécifiez le nom du fichier CSV pour faciliter la lecture et le débogage
debug_file = "./BDD_steps/Convert_to_UTF8.csv"

# Charger le fichier Excel en spécifiant le nom de la feuille
df = pd.read_excel(input_file)

def encode_cell(cell):
    if isinstance(cell, str):
        return cell.encode('utf-8').decode('utf-8')
    return cell

df_encoded = df.applymap(encode_cell)

# Enregistrez le fichier modifié
df.to_excel(output_file, index=False)

# Comptez le nombre de lignes dans le fichier de sortie
num_output_rows = len(df)

# Écrire un fichier CSV pour faciliter la lecture et le débogage
df.to_csv(debug_file, index=False)

print(f"Un fichier CSV pour la lecture et le débogage a été créé : '{debug_file}'")
print(f"Le fichier '{input_file}' a été converti en '{output_file}'")
print(f"Nombre de lignes dans le fichier de sortie : {num_output_rows}")
