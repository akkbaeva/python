# def children():

#     def first_student():
#         print('My name is Seiyt')

#     def second_student():
#         print('My name is Fatima')

#     def third_student():
#         print('My name is Nurgul')

#     def fourth_student():
#         print('My name is Azamat')

#     if num == '1':
#         first_student()
#     elif num == '2':
#         second_student()
#     elif num == '3':
#         third_student()
#     elif num == '4':
#         fourth_student()
    

# children()

# ----------------------------------------------------------------

# def say_hello(func):
#     def wrapper():
#         print('Hello, what is your name?')
#         func('Fatima', 17)

#     return wrapper()

# @say_hello
# def names(name, age=None):
#     if age is None:
#         print(f'My name is {name}')
#     else:
#         print(f'My name is {name} and my age is {age}') 

# -----------------------------------------------------------------

# import time

# def say_hello(func):
#     def wrapper():
#         print('Hello, what is your name?')
#         func('Fatima', 'Azamat', 'Nurgul', 'Seyit')

#     return wrapper()

# @say_hello
# def greetings(name1, name2, name3, name4):
#     print(f'My name is {name1}')
#     time.sleep(2)
#     print(f'My name is {name2}')
#     time.sleep(2)
#     print(f'My name is {name3}')
#     time.sleep(2)
#     print(f'My name is {name4}')
#     time.sleep(2)



# ----------------------------------------------------------------

# def say_mood(other):
#     def cover():
#             print('How are you?')
#             other()

#     return cover()

# @say_mood
# def I():
#     print('I am fine.')



# ----------------------------------------------------------------

def calc_increase(calculator):
    def wrapper():
        calculator(1, 1)
        number1 = int(input(''))
        number2 = int(input(''))
        result = number1 - number2
        print(number1, '-', number2, '=', result)
        result = number1 * number2
        print(number1, '*', number2, '=', result)
        result = number1 / number2
        print(number1, '/', number2, '=', result)
        result = number1 // number2
        print(number1, '//', number2, '=', result)
        result = number1 % number2
        print(number1, '%', number2, '=', result)

    return wrapper()

@calc_increase
def calculator(number1, number2):
    print(number1 + number2)