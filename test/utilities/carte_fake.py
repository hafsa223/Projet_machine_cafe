from hardware.creditcard import CardHandleInterface


class CarteFake(CardHandleInterface):
    def try_charge_amount(self, amount_in_cents: int) -> bool:
        return self.__approvisionnee

    def refund(self, amount_in_cents: int) -> None:
        raise NotImplementedError()

    def __init__(self, approvisionnee):
        self.__approvisionnee = approvisionnee