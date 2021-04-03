class Dog:
    def __init__(self, name, tail, size, noisy):
        self.name = name
        self.tail = tail
        self.size = size
        self.noisy = noisy

    def __str__(self):
        return f'{self.name}, {self.tail}, {self.size}, {self.noisy}'

    def can_bark(self):
        print('woooof')

class Samoyed(Dog):

    def obedient(self):
        print('this dog is easy to teach')

    def strong(self):
        print('really strong and powerful')

samoyed = Samoyed(name='Bobi', tail=15, size=30, noisy='NORMAL')

class Pomerian_Spitz(Dog):

    def cute(self):
        print('this dog is really cute')
spitz = Pomerian_Spitz(name='Boba', tail=5, size=10, noisy='normal')

class Japanese_Spitz(Samoyed, Pomerian_Spitz):

    def energy(self):
        print('got a lot of energy')

jap_spitz = Japanese_Spitz(name='Jackie', tail=5, size=20, noisy='nope')

for i in (samoyed, spitz, jap_spitz):
    print(samoyed)
    samoyed.strong()
    print(spitz)
    spitz.can_bark()
    spitz.cute()
    print(jap_spitz)
    jap_spitz.can_bark()
    jap_spitz.cute()
    jap_spitz.energy()
    jap_spitz.strong()
