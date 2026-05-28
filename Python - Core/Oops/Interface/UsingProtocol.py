from typing import Protocol

class PaymentMethod(Protocol):

    def isAuthorizedPayment(self, amount:float)->bool:
        pass
    def isPaymentProcess(self, amount:float)->bool:
        pass

class CreditCardPayment:

    def isAuthorizedPayment(self, amount:float)->bool:
        #print("Authorizing credit card payment")
        return True
    
    def isPaymentProcess(self, amount:float)->bool:
        print("Processing payment")
        return True
 
def processOrder(payment : PaymentMethod,amount : float):
    if(payment.isAuthorizedPayment(amount)):
        payment.isPaymentProcess(amount)
        print("Payment success")
    else:
        print("Payment failed")

payment=CreditCardPayment()

processOrder(payment,1000)