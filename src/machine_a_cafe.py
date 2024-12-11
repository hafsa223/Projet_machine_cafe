from hardware.brewer import BrewerInterface
from hardware.creditcard import CreditCardInterface, CardHandleInterface
from hardware.buttonpanel import ButtonPanelInterface
from hardware.buttoncode import ButtonCode

class MachineACafé:
    def __init__(self, brewer: BrewerInterface, lecteur_cb: CreditCardInterface, button_panel: ButtonPanelInterface, ageDuCapitaine: int) -> None:
        lecteur_cb.register_card_detected_callback(self._credit_card_callback)
        button_panel.register_button_pressed_callback(self._button_pressed_callback)
        self._brewer = brewer
        self._button_panel = button_panel
        self._button_pressed = False

    def _credit_card_callback(self, card_handle: CardHandleInterface) -> None:
        debit_success = card_handle.try_charge_amount(50)
        if not debit_success:
            return

        if not self._button_pressed:
            brewing_success = self._brewer.make_a_coffee()  # Make an espresso if no button was pressed
        else:
            brewing_success = True  # Assume the button press logic handles brewing

        if not brewing_success:
            card_handle.refund(50)

        self._button_pressed = False  # Reset button pressed state after handling

    def _button_pressed_callback(self, button_code: ButtonCode) -> None:
        self._button_pressed = True

        if button_code == ButtonCode.BTN_LUNGO:
            self._button_panel.set_lungo_warning_state(True)
            self._brewer.try_pull_water()
            self._brewer.try_pull_water()
            self._brewer.make_a_coffee()
     
        elif button_code == ButtonCode.BTN_LATTE:
            self._brewer.pour_milk()
            self._brewer.make_a_coffee()
        elif button_code == ButtonCode.BTN_CHOCOLATE_WATER:
            self._brewer.pour_chocolate()
            self._brewer.pour_milk()

        elif button_code == ButtonCode.BTN_CAPUCCINO:
            self._brewer.pour_milk()
            self._brewer.make_a_coffee()
      
        else:
            self._button_panel.set_lungo_warning_state(False)

