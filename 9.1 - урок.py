# class Discount:

#     def __init__(self, customer, price):
#         self.customer = customer
#         self.price = price

#     def give_discount(self):
#         if self.customer == 'normal':
#             return self.price * 0.2
#         elif self.customer == 'vip':
#             return self.price * 0.4
#         elif self.customer == 'supervip':
#             return self.price * 0.8



class Discount:

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
            return self.price * 0.2

    def __str__(self):
        return f'{self.customer}, {self.price}'

class VIPDiscount(Discount):
    def get_discount(self):
        return super().give_discount() * 2

class SuperVipDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 1.5


discount = Discount('normal', 89)
print(discount)
print(discount.give_discount())
vip_discount =  VIPDiscount('vip', 89)
print(vip_discount)
print(vip_discount.get_discount())
s = SuperVipDiscount('S', 89)
print(s)
print(s.get_discount())


        
