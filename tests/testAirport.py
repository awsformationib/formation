from datetime import datetime
from unittest import TestCase

from vols import Vol
from avions import Avion


# TestRunner (environnement)
#   -> TestSuite (groupby / sequentiel)   modele, restapi, db,
#        -> TestCase (un theme/obj)  tous les fonctions de ...
#
# Vol(**param)
    #tous les params
class TestVol(TestCase):

    def setUp(self):
        """Initialisation avant chaque test."""
        now = datetime.now()
        a = Avion('XYZ',"Airbus A310")
        self.v = Vol('X1Y2Z',"Cannes",a)

    def tearDown(self):
        self.v = None

    def testContenu(self):
        timestamp = datetime.now()
        self.assertEqual(self.v.destination, "Cannes")
        self.assertEqual(self.v.numero, "X1Y2Z")
        self.assertLess(self.v.heure_creation, timestamp)
        self.assertIsNone(self.v.heure_arrivee)
        self.assertIsNot(self.v.heure_arrivee, self.v.heure_creation)

    def testAvion(self):
        self.assertIsNotNone(self.v.avion)
        self.assertIsNotNone(self.v.avion.id)




