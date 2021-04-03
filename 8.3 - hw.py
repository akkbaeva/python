import time

class CatsWithWool:
    def __init__(self, name, tail, wool):
        self.name = name
        self.tail = tail
        self.wool = wool

    def __str__(self):
        return f'{self.name}, {self.tail}, {self.wool}'

class Regdoll(CatsWithWool):
    def cute(self):
        print('I am a very cute and obedient kitty 🐱')
    def obedient(self):
        print('______________________________________')

cute_regdoll = Regdoll(name='Maya', tail=10, wool='yes')
print(cute_regdoll)
time.sleep(1)

class Himalayan_cat(CatsWithWool):
    def fluffy(self):
        print('I have awesome eyes 🐱')
    def devotee(self):
        print('_______________________')

fluffy_himalayan_cat = Himalayan_cat(name='Bobi', tail=15, wool='very')
print(fluffy_himalayan_cat)
time.sleep(1)

class CatsWithoutWool:
    def __init__(self, name, tail, lifestyle):
        self.name = name
        self.tail = tail
        self.lifestyle = lifestyle

    def __str__(self):
        return f'{self.name}, {self.tail}, {self.lifestyle}'

class Sphinx(CatsWithoutWool):
    def bald(self):
        print('I am a kitty without hair 🐱')
    def horrible(self):
        print('_____________________________')

bald_sphinx = Sphinx(name='Richa', tail=10, lifestyle='active')
print(bald_sphinx)
time.sleep(1)

class Simona(CatsWithWool, CatsWithoutWool):
    def beauty(self):
        print('I have half of the body woolen, and half without wool 🐱')
    def amazing(self):
        print('_________________________________________________________')
    
beauty_simona = Simona(name='Simon', tail=15, wool='little')
print(beauty_simona)
time.sleep(1)


class Quest():
    def operation(self):
        print(f'Which kitty are you interested in? ')
        print('1. Maya')
        print('2. Bobi')
        print('3. Richa')
        print('4. Simon')
        print('5. None of them')
        choice = input('Choose a number: ')

        if choice == '1':
            cute_regdoll.cute()
        elif choice == '2':
            fluffy_himalayan_cat.fluffy()
        elif choice == '3':
            bald_sphinx.bald()
        elif choice == '4':
            beauty_simona.beauty()
        elif choice == '5':
            print('IT IS OVER!')


tipa = Quest()
tipa.operation()


