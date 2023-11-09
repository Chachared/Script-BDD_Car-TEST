import subprocess
import time

# Liste des scripts à exécuter dans l'ordre souhaité
scripts_to_run = [
    "SCRIPTS/Clean_duplicates.py", 
    "SCRIPTS/Data_cleaning.py", 
    "SCRIPTS/Convert_to_UTF8.py", 
    "SCRIPTS/Select_columns.py", 
    "SCRIPTS/Rename_columns.py", 
    "SCRIPTS/Convert_dates_ISO8601.py", 
    "SCRIPTS/Convert_date_type.py", 
    "SCRIPTS/Convert_types.py", 
    # "SCRIPTS/DB_insert_first.py",
    # "SCRIPTS/DB_insert_MAJ.py",

]

delay = 60

# Parcourez la liste des scripts et exécutez-les un par un
for script in scripts_to_run:
    try:
        subprocess.run(["python", script], check=True)
        print(f"Le script {script} a été exécuté avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du script {script}: {e}")
    except FileNotFoundError:
        print(f"Le fichier {script} n'a pas été trouvé. Veuillez vérifier le chemin ou le nom du fichier.")

    # Ajoutez un délai entre les exécutions
    time.sleep(delay)