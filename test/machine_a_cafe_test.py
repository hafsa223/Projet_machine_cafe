import unittest

from utilities.brewer_surveillant_les_appels import BrewerSpy
from utilities.carte_fake import CarteFake
from utilities.lecteur_cb_pour_les_tests import LecteurCbFake
from utilities.machine_a_cafe_builder import MachineACaféBuilder
from utilities.brewer_spy import BrewerSpy



class MyTestCase(unittest.TestCase):
    def test_cas_nominal(self):
        # ETANT DONNE une machine a café
        lecteur_cb = LecteurCbFake()
        brewer = BrewerSpy()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        # QUAND une carte approvisionnée est détectée
        carte = CarteFake.default()
        lecteur_cb.simuler_carte_détectée(carte)

        # ALORS un café est commandé au hardware
        self.assertTrue(brewer.make_a_coffee_appelé())

        # ET le prix d'un café est débité
        self.assertEqual(-50, carte.somme_operations_en_centimes())

    def test_sans_provision(self):
        # ETANT DONNE une machine a café
        lecteur_cb = LecteurCbFake()
        brewer = BrewerSpy()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        # ET une carte n'ayant de pas de provision
        carte = CarteFake(False)

        # QUAND cette carte est détectée
        lecteur_cb.simuler_carte_détectée(carte)

        # ALORS aucun café n'est commandé au hardware
        self.assertFalse(brewer.make_a_coffee_appelé())

    def test_defaillance(self):
        # ETANT DONNE une machine a café au brewer défaillant
        lecteur_cb = LecteurCbFake()
        machine_a_cafe = (MachineACaféBuilder()
                          .brewer_defaillant()
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        # QUAND une carte approvisionnée est détectée
        carte = CarteFake.default()
        lecteur_cb.simuler_carte_détectée(carte)

        # ALORS l'argent n'est pas débité
        self.assertEqual(0, carte.somme_operations_en_centimes())

    def test_sans_detection_cb(self):
        # ETANT DONNE une machine a café
        brewer = BrewerSpy()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .build())

        # QUAND aucune carte n'est détectée

        # ALORS aucun café n'est commandé au hardware
        self.assertFalse(brewer.make_a_coffee_appelé())

    def test_manque_d_eau(self):
        # ETANT DONNE une machine à café sans eau
        lecteur_cb = LecteurCbFake()
        brewer = BrewerSpy()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        brewer.simulate_no_water()  # Simuler le manque d'eau

        # QUAND une carte approvisionnée est détectée
        carte = CarteFake.default()
        lecteur_cb.simuler_carte_détectée(carte)

        # ALORS aucun café n'est commandé au hardware
        self.assertFalse(brewer.make_a_coffee_appelé())

    def test_manque_de_cafe(self):
        # ETANT DONNE une machine à café sans café
        lecteur_cb = LecteurCbFake()
        brewer = BrewerSpy()
        machine_a_cafe = (MachineACaféBuilder()
                          .ayant_pour_brewer(brewer)
                          .ayant_pour_lecteur_cb(lecteur_cb)
                          .build())

        brewer.simulate_no_coffee()  # Simuler le manque de café

        # QUAND une carte approvisionnée est détectée
        carte = CarteFake.default()
        lecteur_cb.simuler_carte_détectée(carte)

        # ALORS aucun café n'est commandé au hardware
        self.assertFalse(brewer.make_a_coffee_appelé())

if __name__ == '__main__':
    unittest.main()
