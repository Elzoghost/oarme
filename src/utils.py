from cryptography.fernet import Fernet
import os

def load_key(key_file: str) -> bytes:
    """
    Charge la clé de chiffrement à partir d'un fichier.

    :param key_file: Chemin du fichier contenant la clé.
    :return: Clé de chiffrement.
    """
    try:
        with open(key_file, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print("Fichier de clé non trouvé. Génération d'une nouvelle clé.")
        key = generate_key()
        with open(key_file, 'wb') as file:
            file.write(key)
        return key

def generate_key() -> bytes:
    """
    Génère une clé de chiffrement.

    :return: Clé de chiffrement.
    """
    return Fernet.generate_key()

def encrypt_data(key: bytes, data: str) -> bytes:
    """
    Chiffre les données avec la clé fournie.

    :param key: Clé de chiffrement.
    :param data: Données à chiffrer.
    :return: Données chiffrées.
    """
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(key: bytes, token: bytes) -> str:
    """
    Déchiffre les données avec la clé fournie.

    :param key: Clé de chiffrement.
    :param token: Données chiffrées.
    :return: Données déchiffrées.
    """
    fernet = Fernet(key)
    return fernet.decrypt(token).decode()
