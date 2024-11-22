from hardware.brewer import BrewerInterface


class MachineACafé:
    def __init__(self, brewer: BrewerInterface):
        brewer.make_a_coffee()