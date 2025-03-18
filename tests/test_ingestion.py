import unittest
import os
from src.ingestion import load_data, save_data
from src.utils import generate_key

# Créer le répertoire s'il n'existe pas
os.makedirs('data', exist_ok=True)


class TestIngestion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Générer une clé de chiffrement pour les tests
        cls.encryption_key = generate_key()
        # Chemin vers un fichier CSV d'exemple
        cls.sample_data_path = 'data/sample_data.csv'
        # Données d'exemple pour les tests
        cls.sample_data = [
            {'name': 'Alice', 'age': '30', 'city': 'Paris'},
            {'name': 'Bob', 'age': '25', 'city': 'Lyon'}
        ]
        # Sauvegarder les données d'exemple dans un fichier temporaire
        save_data(cls.sample_data_path, cls.sample_data)

    def test_load_data(self):
        # Charger les données à partir du fichier temporaire
        data = load_data(self.sample_data_path)
        # Vérifier que les données chargées correspondent aux données d'exemple
        self.assertEqual(data, self.sample_data)

    def test_save_data(self):
        # Chemin vers un fichier temporaire pour tester la sauvegarde
        temp_file_path = 'data/temp_test_data.csv'
        # Sauvegarder les données d'exemple dans le fichier temporaire
        save_data(temp_file_path, self.sample_data)
        # Charger les données à partir du fichier temporaire
        data = load_data(temp_file_path)
        # Vérifier que les données sauvegardées correspondent aux données d'exemple
        self.assertEqual(data, self.sample_data)
        # Supprimer le fichier temporaire après le test
        os.remove(temp_file_path)

    @classmethod
    def tearDownClass(cls):
        # Supprimer le fichier d'exemple après les tests
        if os.path.exists(cls.sample_data_path):
            os.remove(cls.sample_data_path)

if __name__ == '__main__':
    unittest.main()
