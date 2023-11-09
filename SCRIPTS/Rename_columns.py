import pandas as pd

# Spécifiez le chemin vers votre fichier Excel
input_file = "./BDD_steps/Select_columns.xlsx"

# Spécifiez le nom du fichier CSV de sortie
output_file = "./BDD_steps/Rename_columns.xlsx"

# Spécifiez le nom du fichier CSV pour faciliter la lecture et le débogage
debug_file = "./BDD_steps/Rename_columns.csv"

# Charger le fichier Excel en spécifiant le nom de la feuille
df = pd.read_excel(input_file)

# Renommer les colonnes de l'excel comme dans la BDD
if 'car_ebayID' in df.columns:
    df.rename(columns={'car_ebayID': 'ebay_id'}, inplace=True)

if 'car_tdID' in df.columns:
    df.rename(columns={'car_tdID': 'td_id'}, inplace=True)

if 'car_c4cID' in df.columns:
    df.rename(columns={'car_c4cID': 'c4c_id'}, inplace=True)

if 'car_nbShift' in df.columns:
    df.rename(columns={'car_nbShift': 'car_nb_shift'}, inplace=True)

if 'ABC_ranking' in df.columns:
    df.rename(columns={'ABC_ranking': 'car_ranking'}, inplace=True)

if 'model_mark' in df.columns:
    df.rename(columns={'model_mark': 'car_mark'}, inplace=True)

if 'model_name' in df.columns:
    df.rename(columns={'model_name': 'car_name'}, inplace=True)

if 'model_doors' in df.columns:
    df.rename(columns={'model_doors': 'car_doors'}, inplace=True)

if 'model_chassis' in df.columns:
    df.rename(columns={'model_chassis': 'car_chassis'}, inplace=True)

if 'model_YFrom' in df.columns:
    df.rename(columns={'model_YFrom': 'car_model_y_from'}, inplace=True)

if 'model_YTo' in df.columns:
    df.rename(columns={'model_YTo': 'car_model_y_to'}, inplace=True)

if 'engine_code' in df.columns:
    df.rename(columns={'engine_code': 'car_code'}, inplace=True)

if 'engine_desc' in df.columns:
    df.rename(columns={'engine_desc': 'car_engine_desc'}, inplace=True)

if 'engine_aspi' in df.columns:
    df.rename(columns={'engine_aspi': 'car_aspi'}, inplace=True)

if 'engine_alim' in df.columns:
    df.rename(columns={'engine_alim': 'car_alim'}, inplace=True)

if 'engine_nameCyl' in df.columns:
    df.rename(columns={'engine_nameCyl': 'car_name_cyl'}, inplace=True)

if 'engine_valve' in df.columns:
    df.rename(columns={'engine_valve': 'car_valve'}, inplace=True)

if 'engine_KW' in df.columns:
    df.rename(columns={'engine_KW': 'car_kw'}, inplace=True)

if 'engine_CV' in df.columns:
    df.rename(columns={'engine_CV': 'car_cv'}, inplace=True)

if 'engine_disp' in df.columns:
    df.rename(columns={'engine_disp': 'car_disp'}, inplace=True)

if 'engine_Cyl' in df.columns:
    df.rename(columns={'engine_Cyl': 'car_cyl'}, inplace=True)

if 'engine_nbCyl' in df.columns:
    df.rename(columns={'engine_nbCyl': 'car_nb_cyl'}, inplace=True)

if 'engine_type' in df.columns:
    df.rename(columns={'engine_type': 'car_type'}, inplace=True)

if 'info_dateAdd' in df.columns:
    df.rename(columns={'info_dateAdd': 'car_date_add'}, inplace=True)

if 'info_URL' in df.columns:
    df.rename(columns={'info_URL': 'car_url'}, inplace=True)

if 'info_user' in df.columns:
    df.rename(columns={'info_user': 'car_user'}, inplace=True)

if 'info_method' in df.columns:
    df.rename(columns={'info_method': 'car_method'}, inplace=True)

if 'info_valid' in df.columns:
    df.rename(columns={'info_valid': 'car_valid'}, inplace=True)

if 'info_comment' in df.columns:
    df.rename(columns={'info_comment': 'car_comment'}, inplace=True)

# Enregistrez le fichier modifié
df.to_excel(output_file, index=False)

# Comptez le nombre de lignes dans le fichier de sortie
num_output_rows = len(df)

# Écrire un fichier CSV pour faciliter la lecture et le débogage
df.to_csv(debug_file, index=False)

print(f"Un fichier CSV pour la lecture et le débogage a été créé : '{debug_file}'")
print(f"Le fichier '{input_file}' a été converti en '{output_file}'")
print(f"Nombre de lignes dans le fichier de sortie : {num_output_rows}")