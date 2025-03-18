from src.ingestion import load_data, save_data
from src.vulnerability import check_sql_injection, check_xss
from tests.ssh_tests import check_ssh_weak_keys

def main():
    # Exemple d'utilisation du module d'ingestion
    file_path = 'data/sample_data.csv'
    print("Chargement des données...")
    data = load_data(file_path)
    print("Données chargées :", data)

    # Exemple d'utilisation du module de vulnérabilité
    test_input = "SELECT * FROM users;"
    print("Vérification de l'injection SQL...")
    if check_sql_injection(test_input):
        print("Injection SQL détectée !")
    else:
        print("Aucune injection SQL détectée.")

    test_input_xss = '<script>alert("XSS")</script>'
    print("Vérification de l'attaque XSS...")
    if check_xss(test_input_xss):
        print("Attaque XSS détectée !")
    else:
        print("Aucune attaque XSS détectée.")

    # Exemple d'utilisation du module de tests SSH
    hostname = 'example.com'
    port = 22
    username = 'user'
    password = 'pass'
    print("Vérification des clés SSH faibles...")
    if check_ssh_weak_keys(hostname, port, username, password):
        print("Clés SSH faibles détectées !")
    else:
        print("Aucune clé SSH faible détectée.")

if __name__ == "__main__":
    main()
