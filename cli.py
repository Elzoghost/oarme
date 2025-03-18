import argparse
from src.ingestion import load_data, save_data
from src.vulnerability import check_sql_injection, check_xss
from tests.ssh_tests import check_ssh_weak_keys

def main():
    parser = argparse.ArgumentParser(description="Outil de tests de sécurité.")
    subparsers = parser.add_subparsers(dest="command")

    # Sous-commande pour charger des données
    parser_load = subparsers.add_parser('load', help="Charger des données à partir d'un fichier CSV.")
    parser_load.add_argument('file_path', type=str, help="Chemin du fichier CSV à charger.")

    # Sous-commande pour sauvegarder des données
    parser_save = subparsers.add_parser('save', help="Sauvegarder des données dans un fichier CSV.")
    parser_save.add_argument('file_path', type=str, help="Chemin du fichier CSV où sauvegarder les données.")

    # Sous-commande pour vérifier l'injection SQL
    parser_sql = subparsers.add_parser('check-sql', help="Vérifier l'injection SQL dans une chaîne.")
    parser_sql.add_argument('input_string', type=str, help="Chaîne à vérifier pour l'injection SQL.")

    # Sous-commande pour vérifier les attaques XSS
    parser_xss = subparsers.add_parser('check-xss', help="Vérifier les attaques XSS dans une chaîne.")
    parser_xss.add_argument('input_string', type=str, help="Chaîne à vérifier pour les attaques XSS.")

    # Sous-commande pour vérifier les clés SSH faibles
    parser_ssh = subparsers.add_parser('check-ssh', help="Vérifier les clés SSH faibles sur un serveur.")
    parser_ssh.add_argument('hostname', type=str, help="Adresse IP ou nom d'hôte du serveur SSH.")
    parser_ssh.add_argument('port', type=int, help="Port SSH.")
    parser_ssh.add_argument('username', type=str, help="Nom d'utilisateur pour la connexion SSH.")
    parser_ssh.add_argument('password', type=str, help="Mot de passe pour la connexion SSH.")

    args = parser.parse_args()

    if args.command == 'load':
        data = load_data(args.file_path)
        print("Données chargées :", data)

    elif args.command == 'save':
        sample_data = [
            {'name': 'Alice', 'age': '30', 'city': 'Paris'},
            {'name': 'Bob', 'age': '25', 'city': 'Lyon'}
        ]
        save_data(args.file_path, sample_data)
        print("Données sauvegardées.")

    elif args.command == 'check-sql':
        if check_sql_injection(args.input_string):
            print("Injection SQL détectée !")
        else:
            print("Aucune injection SQL détectée.")

    elif args.command == 'check-xss':
        if check_xss(args.input_string):
            print("Attaque XSS détectée !")
        else:
            print("Aucune attaque XSS détectée.")

    elif args.command == 'check-ssh':
        if check_ssh_weak_keys(args.hostname, args.port, args.username, args.password):
            print("Clés SSH faibles détectées !")
        else:
            print("Aucune clé SSH faible détectée.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
