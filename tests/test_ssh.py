import unittest
from unittest.mock import patch, MagicMock
from src.ssh_tests import check_ssh_weak_keys

class TestSSH(unittest.TestCase):

    @patch('paramiko.SSHClient')
    def test_check_ssh_weak_keys_detected(self, MockSSHClient):
        # Configurer le mock pour simuler une connexion SSH réussie
        mock_ssh = MockSSHClient.return_value
        mock_transport = MagicMock()
        mock_transport.get_host_keys.return_value = {
            'ssh-rsa': b'key_data'  # Simuler une clé faible
        }
        mock_ssh.get_transport.return_value = mock_transport

        # Appeler la fonction avec des informations de connexion fictives
        result = check_ssh_weak_keys('hostname', 22, 'username', 'password')

        # Vérifier que la fonction détecte les clés faibles
        self.assertTrue(result)

    @patch('paramiko.SSHClient')
    def test_check_ssh_weak_keys_not_detected(self, MockSSHClient):
        # Configurer le mock pour simuler une connexion SSH réussie
        mock_ssh = MockSSHClient.return_value
        mock_transport = MagicMock()
        mock_transport.get_host_keys.return_value = {
            'ssh-ed25519': b'key_data'  # Simuler une clé forte
        }
        mock_ssh.get_transport.return_value = mock_transport

        # Appeler la fonction avec des informations de connexion fictives
        result = check_ssh_weak_keys('hostname', 22, 'username', 'password')

        # Vérifier que la fonction ne détecte pas de clés faibles
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
