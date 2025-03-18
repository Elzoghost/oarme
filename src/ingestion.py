import csv
from typing import List, Dict
from src.utils import encrypt_data, decrypt_data, load_key

# Charger la clé de chiffrement à partir d'un fichier
encryption_key = load_key('data/secret.key')

def load_data(file_path: str) -> List[Dict[str, str]]:
    """
    Charge les données à partir d'un fichier CSV et les déchiffre.

    :param file_path: Chemin du fichier CSV à charger.
    :return: Liste de dictionnaires contenant les données déchiffrées.
    """
    data = []
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                decrypted_row = {k: decrypt_data(encryption_key, v.encode()) for k, v in row.items()}
                data.append(decrypted_row)
        print("Données chargées et déchiffrées avec succès.")
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
    return data

def save_data(file_path: str, data: List[Dict[str, str]]) -> None:
    """
    Chiffre et sauvegarde les données dans un fichier CSV.

    :param file_path: Chemin du fichier CSV où sauvegarder les données.
    :param data: Liste de dictionnaires contenant les données à chiffrer et sauvegarder.
    """
    try:
        with open(file_path, mode='w', newline='') as file:
            if data:
                encrypted_data = [{k: encrypt_data(encryption_key, v).decode() for k, v in row.items()} for row in data]
                writer = csv.DictWriter(file, fieldnames=encrypted_data[0].keys())
                writer.writeheader()
                writer.writerows(encrypted_data)
        print("Données chiffrées et sauvegardées avec succès.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des données : {e}")
