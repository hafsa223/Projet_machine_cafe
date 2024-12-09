from hardware.brewer import BrewerInterface
from hardware.creditcard import CreditCardInterface, CardHandleInterface


class MachineACafé:
    def __init__(self, brewer: BrewerInterface, lecteur_cb: CreditCardInterface, ageDuCapitaine: int):
        lecteur_cb.register_card_detected_callback(self._credit_card_callback)
        self._brewer = brewer

    def _credit_card_callback(self, card_handle: CardHandleInterface) -> None:
        debit_success = card_handle.try_charge_amount(50)
        if not debit_success:
            return

        brewing_success = self._brewer.make_a_coffee()
        if not brewing_success:
            card_handle.refund(50)
