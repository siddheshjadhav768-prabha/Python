class Payment:
    def pay(self):
        pass


class CreditCardPayment(Payment):
    def pay(self):
        print("Payment done using Credit Card")


class UPIPayment(Payment):
    def pay(self):
        print("Payment done using UPI")


class NetBankingPayment(Payment):
    def pay(self):
        print("Payment done using Net Banking")


payments = [
    CreditCardPayment(),
    UPIPayment(),
    NetBankingPayment()
]

for payment in payments:
    payment.pay()