# SINCE THE CHADGPT IS NOT WORKING IM USING GEMINI FOR QUES FOR THIS TOPIC 
# THIS IS THE QUESTION 
# 1.Define a base class PaymentMethod. This class should have an __init__ method (taking perhaps amount) and a method process_payment() that prints a generic message.
# 2.Create at least two subclasses: CreditCardPayment and PayPalPayment, inheriting from PaymentMethod.
# 3.Override process_payment() in CreditCardPayment to simulate processing a credit card (e.g., printing "Processing Credit Card payment for $X.XX").
# 4.Override process_payment() in PayPalPayment to simulate processing a PayPal transaction (e.g., printing "Initiating PayPal transaction for $X.XX").
# 5.Create a list of various payment method objects, each with a different amount.
# 6.Write a function execute_payments(payment_methods) that takes this list and calls process_payment() on each.


class PaymentMethod:
    def __init__(self, amount):
        self.amount = amount 

    def process_payment(self):
        print("Payment is in the progress !")

class CreditCardPayment(PaymentMethod):
    def __init__(self, amount):
        super().__init__(amount)

    def process_payment(self):
        print(f"Processing Credit Card payment for ${self.amount}.")

class PayPalPayment(PaymentMethod):
    def __init__(self, amount):
        super().__init__(amount)

    def process_payment(self):
        print(f"Initiating PayPal transaction for ${self.amount}")

pay1 = CreditCardPayment(100.50)
pay2 = PayPalPayment(45.75)
pay3 = CreditCardPayment(20.00)

total_payments = [pay1, pay2, pay3]

def execute_payments(payments):
    for pays in payments:
        pays.process_payment() 

execute_payments(total_payments)
        