class payment:
    bankname = None
    accounttype = None
    paymentmethod = None

    def paymentmode_razorpay(self):
        print("pay by razorpay")

    def paymentmode_stripe(self):
        print("pay by stripe")

    def paymentmode_instanojo(self):
        print("pay by instanojo")


pay = payment()
pay.paymentmode_razorpay()
pay.paymentmethod = "UPI razorpay"
print(pay.paymentmethod)
