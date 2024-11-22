from hardware.brewer import BrewerInterface
from hardware.creditcard import CreditCardInterface, CardHandleInterface


class MachineACafé:
    def __init__(self, brewer: BrewerInterface, lecteur_cb: CreditCardInterface):
        lecteur_cb.register_card_detected_callback(self._credit_card_callback)
        self._brewer = brewer

    def _credit_card_callback(self, card_handle: CardHandleInterface) -> None:
        self._brewer.make_a_coffee()
