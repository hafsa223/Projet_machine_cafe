import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_cas_nominal(self):
        # ETANT DONNE une machine a café
        lecteur_cb = LecteurCbPourLesTests()
        brewer = BrewerSurveillantLesAppels()
        machine_a_cafe = MachineACafé()

        # QUAND une carte est détectée
        lecteur_cb.simuler_carte_détectée()

        # ALORS un café est commandé au hardware
        self.assertTrue(brewer.make_a_coffee_appelé())


if __name__ == '__main__':
    unittest.main()
