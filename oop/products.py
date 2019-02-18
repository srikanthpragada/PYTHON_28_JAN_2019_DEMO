class Product:
    # class attribute
    TAX = 18

    def __init__(self, name, price, qoh=0):
        self.name = name
        self.price = price
        self.qoh = qoh

    def print_details(self):
        print(self.name)
        print(self.price)
        print(self.qoh)

    def get_net_price(self):
        return self.price + (self.price * Product.TAX / 100)


class DiscountProduct(Product):
    def __init__(self, name, price, disrate, qoh=0):
        super().__init__(name, price, qoh)
        self.disrate = disrate

    # Overriding
    def print_details(self):
        super().print_details()
        print(self.disrate)

    # Overriding
    def get_net_price(self):
        grossprice = self.price - (self.price * self.disrate / 100)
        netprice = grossprice + (grossprice * Product.TAX / 100)
        return netprice


p = Product("Abc", 10000, 2)
print(p.get_net_price())
dp = DiscountProduct("Xyz", 15000, 20, 5)
print(dp.get_net_price())

p.print_details()
dp.print_details()
