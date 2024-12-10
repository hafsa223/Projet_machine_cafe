from hardware.cupprovider import CupProviderInterface

class CupProviderSpy(CupProviderInterface):
    def __init__(self, cup_present: bool):
        self._cup_present = cup_present
        self._provide_cup_called = False

    def is_cup_present(self) -> bool:
        return self._cup_present

    def provide_cup(self):
        self._provide_cup_called = True

    def provide_cup_called(self) -> bool:
        return self._provide_cup_called

    def provide_stirrer(self):  
        pass
