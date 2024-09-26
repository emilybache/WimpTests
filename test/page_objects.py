class PaymentPage:
    def payment_options(self):
        return []


class OrderPage:

    def proceed_to_payment(self):
        return PaymentPage()
