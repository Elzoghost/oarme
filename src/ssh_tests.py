import paramiko

def check_ssh_weak_keys(hostname: str, port: int, username: str, password: str) -> bool:
    """
    Vérifie si une connexion SSH utilise des clés faibles.

    :param hostname: Adresse IP ou nom d'hôte du serveur SSH.
    :param port: Port SSH.
    :param username: Nom d'utilisateur pour la connexion.
    :param password: Mot de passe pour la connexion.
    :return: True si des clés faibles sont détectées, False sinon.
    """
    try:
        # Créer une instance SSHClient
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connexion au serveur SSH
        client.connect(hostname, port, username, password)

        # Vérifier les clés SSH (exemple simplifié)
        transport = client.get_transport()
        host_keys = transport.get_host_keys()

        # Exemple de vérification des clés faibles
        for key_type in host_keys.keys():
            if key_type in ['ssh-rsa', 'ssh-dss']:  # Exemple de clés faibles
                return True

        return False

    except Exception as e:
        print(f"Erreur lors de la connexion SSH : {e}")
        return False
    finally:
        client.close()

