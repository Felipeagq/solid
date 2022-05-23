class Order:
    items = []
    quantities = []
    prices = []
    status = "open"


    def add_item(self,name,quantity,price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


    def pay(self, payment_type,security_code):
        if payment_type == "debit":
            print("Processing DEBIT payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing CREDIT payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknow payment type :{payment_type}")

if __name__ == "__main__":
    order = Order()
    order.add_item("a",1,50)
    order.add_item("b",2,50)
    order.add_item("c",3,50)

    print(order.total_price())
    order.pay("debit","123")