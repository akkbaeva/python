import time

class Animal:

    def __init__(self, kind, name, age, color, habitat):
        if isinstance(kind, str):
            self.kind = kind
        else:
            raise ValueError('type integer')
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('type integer')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('age can be only numeric')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('type integer')
        if isinstance(habitat, str):
            self.habitat = habitat
        else:
            raise ValueError('type integer')

    def __str__(self):
        return f'{self.kind}, {self.name}, {self.age}, {self.color}, {self.habitat}'
        
class Assistant:
    def care(self):
        print('Dont give too hard food.')
        time.sleep(3)

class Chicken(Animal, Assistant):

    def __init__(self, kind, name, age, color, habitat, size):

        super(Chicken, self).__init__(kind, name, age, color, habitat)

        if isinstance(size, str):
            self.size = size
        else:
            raise ValueError('type integer')

    def __str__(self):
        return f'{self.kind}, {self.name}, {self.age}, {self.color}, {self.habitat}, {self.size}'

    def details(self):
        print('1. Learn more')
        print('2. Go to another')
        choice = int(input('choose your path ninja: '))

        if choice == 1:
            print('Chickens are very cute animals only when they are still small.')
        elif choice == 2:
            print('do you really want to know about cute chicks? ')
        else:
            print('IT IS OVER')
        
chicken = Chicken(kind='Chicken', name='Normal', age=1, color='Yellow', habitat='Asia', size='S')
print(chicken)

class Dog(Animal, Assistant):

    def __init__(self, kind, name, age, color, habitat, size, mood):

        super(Dog, self).__init__(kind, name, age, color, habitat)

        if isinstance(size, str):
            self.size = size
        else:
            raise ValueError('type integer')
        if isinstance(mood, str):
            self.mood = mood
        else:
            raise ValueError('type integer')

    def __str__(self):
        return f'{self.kind}, {self.name}, {self.age}, {self.color}, {self.habitat}, {self.size}, {self.mood}'

    def details(self):
        print('1. Learn more')
        print('2. Go to another')
        choice = int(input('choose your path ninja: '))

        if choice == 1:
            print('Dogs are very intelligent and loyal animals.')
        elif choice == 2:
            print('Do you think this is the right choice?')
        else:
            print('IT IS OVER')

dog = Dog(kind='Dog', name='Spitz', age=4, color='White', habitat='Europe', size='M', mood='Fine')
print(dog)

class Zoo_show:
    def show(self):
        time.sleep(1)
        print('Start')
        time.sleep(2)
        print('p.s the show is on')
        time.sleep(2)
        print('End the show')


class Ticket(Zoo_show):

    def __init__(self, all_money):
        self.all_money = all_money

    def home(self):
        print(f'You have ${self.all_money}, what will you spend on? ')
        print('1. Chicken / 100$')
        print('2. Dog / 100$')
        print('3. Watch the show / 150$')
        choice = input('Choose a number: ')

        if choice == '1':
            self.all_money -= 100
            print(f'you have {self.all_money}$')
            chicken.details()
        elif choice == '2':
            self.all_money -= 100
            print(f'you have {self.all_money}$')
            dog.details()
        elif choice == '3':
            self.all_money -= 150
            print(f'you have {self.all_money}$')
            zoo_show = Zoo_show()
            zoo_show.show()

        last = input('Do you want to choose another? ')
        print('yes / no')

        if last == 'yes':
            self.home()

ticket = Ticket(all_money=500)
ticket.home()








