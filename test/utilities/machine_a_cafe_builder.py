from hardware.brewer import BrewerInterface
from machine_a_cafe import MachineACafé
from utilities.brewer_surveillant_les_appels import BrewerSpy
from utilities.lecteur_cb_pour_les_tests import LecteurCbFake


class MachineACaféBuilder:
    def __init__(self):
        self.__brewer = BrewerSpy()
        self.__lecteur_cb = LecteurCbFake()

    def build(self) -> MachineACafé:
        return MachineACafé(self.__brewer, self.__lecteur_cb, 0)

    def ayant_pour_brewer(self, brewer: BrewerInterface):
        self.__brewer = brewer
        return self

    def ayant_pour_lecteur_cb(self, lecteur_cb: BrewerInterface):
        self.__lecteur_cb = lecteur_cb
        return self