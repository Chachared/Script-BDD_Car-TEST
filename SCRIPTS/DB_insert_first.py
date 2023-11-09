import psycopg2
import pandas as pd

host = "localhost"
database = "Cat4Classic test"
user = "postgres"
password = "Splinter82"

excel_file = "./BDD_steps/Convert_types.xlsx"
try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    cursor = connection.cursor()

    table_name = "car"

    data = pd.read_excel(excel_file)

    # Initialisez un compteur pour suivre le nombre de lignes insérées en BDD
    num_inserted_rows = 0

    # Initialisez un dictionnaire pour suivre le nombre d'ajouts par colonne
    insert_counts = {col: 0 for col in data.columns}

    # Créez un dictionnaire de mappage entre les colonnes du fichier Excel et les champs de la base de données
    column_mapping = {
        'c4c_id': 'c4c_id',
        'td_id': 'td_id',
        'ebay_id':'ebay_id',
        'car_fuel': 'car_fuel',
        'car_nb_shift':'car_nb_shift',
        'car_desc':'car_desc',
        'car_trans':'car_trans',
        'car_trim':'car_trim',
        'car_version':'car_version',
        'car_plat':'car_plat',
        'car_y_from':'car_y_from',
        'car_y_to':'car_y_to',
        'car_d_from':'car_d_from',
        'car_d_to':'car_d_to',
        'car_ranking':'car_ranking',
        'car_mark':'car_mark',
        'car_name':'car_name',
        'car_doors':'car_doors',
        'car_chassis':'car_chassis',
        'car_model_y_from':'car_model_y_from',
        'car_model_y_to':'car_model_y_to',
        'car_code':'car_code',
        'car_engine_desc':'car_engine_desc',
        'car_aspi':'car_aspi',
        'car_alim':'car_alim',
        'car_name_cyl':'car_name_cyl',
        'car_valve':'car_valve',
        'car_kw':'car_kw',
        'car_cv':'car_cv',
        'car_disp':'car_disp',
        'car_cyl':'car_cyl',
        'car_nb_cyl':'car_nb_cyl',
        'car_type':'car_type',
        'car_url':'car_url',
        'car_user':'car_user',
        'car_method':'car_method',
        'car_comment':'car_comment',
        'car_valid': 'car_valid',
        'car_date_add': 'car_date_add',
        # Ajoutez d'autres colonnes et champs correspondants ici
    }

    # Utilisez ce dictionnaire pour mapper les colonnes du fichier Excel aux champs de la base de données
    for index, row in data.iterrows():
        values = {column_mapping[col]: row[col] for col in column_mapping}

        # Vérifiez si la colonne est "car_date_add" et traitez-la correctement
        if 'car_date_add' in values:
            values['car_date_add'] = values['car_date_add'].date()  # Supprimer l'information d'heure

        insert_query = f"INSERT INTO {table_name} ({', '.join(values.keys())}) VALUES ({', '.join(['%s'] * len(values))})"
        cursor.execute(insert_query, list(values.values()))

        # Mettez à jour le compteur pour chaque colonne insérée avec succès
        for col, value in zip(values.values(), data.columns):
            if pd.notna(col):
                insert_counts[value] += 1

    connection.commit()

except psycopg2.Error as db_error:
    print(f"Erreur de base de données: {db_error}")
except Exception as e:
    print(f"Erreur générale: {e}")
finally:
    if 'connection' in locals():
        connection.close()

print(f"Insertion réussie dans {table_name} de la BDD {database}.")

# Affichez le nombre d'ajouts par colonne (à l'exception des NULL)
for col, count in insert_counts.items():
    if count > 0:
        print(f"Nombre d'ajouts dans la colonne '{col}': {count}")