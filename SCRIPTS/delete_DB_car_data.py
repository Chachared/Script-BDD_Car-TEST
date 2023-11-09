import psycopg2
import pandas as pd

host = "localhost"
database = "Cat4Classic test"
user = "postgres"
password = "Splinter82"
excel_file = "./BDD_steps/ConvertTypes.xlsx"

try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    cursor = connection.cursor()
    table_name = "car"
    # Requête SQL pour supprimer toutes les lignes de la table
    delete_query = f"DELETE FROM {table_name}"
    cursor.execute(delete_query)

    # Validez (commit) la suppression
    connection.commit()

except psycopg2.Error as db_error:
    print(f"Erreur de base de données: {db_error}")
except Exception as e:
    print(f"Erreur générale: {e}")
finally:
    if 'connection' in locals():
        connection.close()
print(f"Suppression réussie des data dans la table {table_name} de la BDD {database}.")