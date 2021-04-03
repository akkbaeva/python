class Horse:
    def __init__(self, name, tail, noisy):
        self.name = name
        self.tail = tail
        self.noisy = noisy

    def __str__(self):
        return f'{self.name}, {self.tail}, {self.noisy}'

class Pony(Horse):
    def cute(self):
        print('.......')
    def beauty(self):
        print('///////')

cute_pony = Pony(name='Pika', tail=20, noisy='normal')
print(cute_pony)

class Big_horse(Horse):
    def strong(self):
        print('-------')
    def glossy(self):
        print('=======')

beauty_horse = Big_horse(name='Pati', tail=40, noisy='no')
print(beauty_horse)

class Unicorn(Pony, Big_horse):
    def little(self):
        print('________')
    def smart(self):
        print('++++++++')

little_horse = Unicorn(name='Pikachu', tail=30, noisy='yes')
print(little_horse)
little_horse.cute()
little_horse.smart()
little_horse.beauty()
little_horse.glossy()


