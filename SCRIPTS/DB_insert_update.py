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

    # Initialisez les compteurs pour suivre le nombre de lignes modifiées et ajoutées
    num_updated_rows = 0
    num_added_rows = 0

    # Initialisez une liste pour stocker les erreurs
    errors = []

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

    for index, row in data.iterrows():
        values = {column_mapping[col]: row[col] for col in column_mapping}
        c4c_id = values['c4c_id']

        # Vérifiez si la ligne existe déjà en fonction de la clé primaire c4c_id
        cursor.execute(f"SELECT * FROM {table_name} WHERE c4c_id = %s", (c4c_id,))
        existing_row = cursor.fetchone()

        if existing_row is None:
            # La ligne n'existe pas, ajoutez-la
            insert_query = f"INSERT INTO {table_name} ({', '.join(values.keys())}) VALUES ({', '.join(['%s'] * len(values))})"
            cursor.execute(insert_query, list(values.values()))
            num_added_rows += 1
        else:
            # La ligne existe, vérifiez si les données sont identiques
            existing_values = dict(zip(data.columns, existing_row))
            if values == existing_values:
                # Les données sont identiques, ne faites rien
                pass
            else:
                # Les données sont différentes, mettez à jour la ligne
                update_query = f"UPDATE {table_name} SET {', '.join([f'{col} = %s' for col in values.keys()])} WHERE c4c_id = %s"
                cursor.execute(update_query, list(values.values()) + [c4c_id])
                num_updated_rows += 1

    connection.commit()

except psycopg2.Error as db_error:
    errors.append(f"Erreur de base de données: {db_error}")
except Exception as e:
    errors.append(f"Erreur générale: {e}")
finally:
    if 'connection' in locals():
        connection.close()

print(f"Nombre de lignes mises à jour : {num_updated_rows}")
print(f"Nombre de lignes ajoutées : {num_added_rows}")
for error in errors:
    print(error)