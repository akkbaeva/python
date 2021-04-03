class Human:

    def __init__(self, name, gender, age, nationality):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('type integer')
        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError('type integer')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('age can be only numeric')
        if isinstance(nationality, str):
            self.nationality = nationality
        else:
            raise ValueError('type integer')



    def __str__(self):
        return f'{self.name}, {self.gender}, {self.age}, {self.nationality}'

    def can_breathe(self):
        print('can breathe')


human1 = Human('Fatima', 'Female', 17, 'Kyrgyz')
print(human1)
human1.can_breathe()
samurai = Human('LinSong', 'Male', 29, 'Chinese')
print(samurai)

class Developer(Human):
    def __init__(self, name, gender, age, nationality, laptop, smart):
        super(Developer, self).__init__(name, gender, age, nationality)
        if isinstance(laptop, str):
            self.laptop = laptop
        else:
            raise ValueError('laptop should be str')
        if isinstance(smart, str):
            self.smart = smart
        else:
            raise ValueError('smart should be str')

    def can_code(self):
        print('I can code')


    def __str__(self):
        return f'{super(Developer, self).__str__()}, {self.laptop}, {self.smart}'
programmer = Developer(name = 'Fatima', 
                    gender='Female', 
                    age=17, 
                    nationality='Kyrgyz', 
                    laptop='Xiaomi Mi Notebook Pro 15,6',
                    smart='right')
programmer.__str__()
print(programmer)
programmer.can_code()

