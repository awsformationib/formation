import json
import unittest
from unittest import TestCase

import requests



#serveur repond
#   statuscode 200
    # contenu message

# serveur list_vols n'est pas vide
#   statuscode 200

# serveur vol "XYZA" est bien recupere

class TestRestApi(TestCase):
    """
    def setUpClass(cls): # methode de classe

        # 1 fois au debut (charge db, calcul , init fichiers
        pass

    def tearDownClass(cls): # methode de classe
        # 1 fois à la fin (menage ; vide la base, les fichiers)
        pass
    """

    def setUp(self):
        #'test' fois
        self.numvol = "179H2J"

    def tearDown(self):
        #'test' fois
        pass

    def testRacine(self):
        url = "http://localhost:8000/"
        response = requests.get(url)
        self.assertEqual(response.status_code,200)

    def testVol(self):
        url = "http://localhost:8000/vol/{}".format(self.numvol)
        response = requests.get(url)
        self.assertEqual(response.status_code,200)
        self.assertIsNotNone(response.text)
        data_dico = json.loads(response.text)
        self.assertIn("numero",data_dico)
        self.assertNotIn("modele", data_dico)

    @unittest.skip("Test pas implementé")
    def testEncoreDeRealisation(self):
        pass
