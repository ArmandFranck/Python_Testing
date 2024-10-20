import sys
import os
import pytest
from server import app # Remplacer par le chemin correct si nécessaire

# 1. Ajouter le répertoire racine au chemin d'import pour que pytest trouve server.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 2. Fixture pour initialiser un client Flask pour tous les tests
@pytest.fixture
def client():
    # Activer le mode test dans Flask
    app.config['TESTING'] = True
    # Fournir un client de test pour simuler des requêtes
    with app.test_client() as client:
        yield client

# 3. (Optionnel) Si tu veux charger des données de test ou initialiser certaines choses avant les tests
@pytest.fixture(scope='module')
def init_data():
    # Par exemple, charger les données de clubs ou de compétitions
    # Cette fixture sera appelée avant les tests si nécessaire
    clubs = {"clubs": [{"name": "Simply Lift", "email": "john@simplylift.co", "points": "13", "total_reserved": 0}, {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4", "total_reserved": 0}, {"name": "New Club", "email": "new@club.com", "points": "10", "total_reserved": 0}]}  # Remplis cela avec des données réelles si nécessaire
    competitions = {"competitions": [{"name": "Fall Classic", "numberOfPlaces": "10", "date": "2024-10-20 00:00:00"}, {"name": "New Competition", "date": "2024-10-30 00:00:00", "numberOfPlaces": "20"}]}
    return clubs, competitions
