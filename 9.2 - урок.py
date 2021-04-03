class Pizza:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def appetite(self):
        return self.size / 0.2

    def __str__(self):
        return f'{self.size} {self.name}'

class LittlePiesePizza(Pizza):

    def share(self):
        return super().appetite() / 4

class BigPiesePizza(Pizza):

    def share(self):
        return super().appetite() / 2

class NormalPiesePizza(LittlePiesePizza, BigPiesePizza):

    def share(self):
        return super().appetite() / 3
    

pizza = Pizza('Chicken_cheese', 9)
print(pizza)
print(pizza.appetite())
little_piese = LittlePiesePizza('LittlePizza', 6)
print(little_piese)
print(little_piese.appetite())
big_piese = BigPiesePizza('BigPizza', 12)
print(big_piese)
print(big_piese.appetite())
normal_piese = NormalPiesePizza('NormalPizza', 10)
print(normal_piese)
print(normal_piese.appetite())