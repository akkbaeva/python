# name = "Adilet"
# age = 17

# if age > 18:
#     print('Ты совершеннолетний')
# elif age < 18:
#     print('Ты не совершеннолетний')


while True:
    try:
        number_1 = int(input('Введите первое число'))
        number_2 = int(input('Введите второе число'))
        operation = input('Введите операцию: ')

        if operation == '+':
            result = number_1 + number_2
            print(number_1, '+', number_2, '=', result)
        elif operation == '-':
            result = number_1 - number_2
            print(number_1, '-', number_2, '=', result)
        elif operation == '*':
            result = number_1 * number_2
            print(number_1, '*', number_2, '=', result)
        elif operation == '/':
            result = number_1 / number_2
            print(number_1, '/', number_2, '=', result)
        elif operation == '//':
            result = number_1 // number_2
            print(number_1, '//', number_2, '=', result)
        elif operation == '%':
            result = number_1 % number_2
            print(number_1, '%', number_2, '=', result)
        restart = input('Restart or Quit')
        if restart == 'no':
                break
        else:
            print('operation does not exist, please choose another one')
    except ValueError:
        print('type integer')




# weekday = False
# vacation = True
# if weekday and not vacation:
#     print("we are not sleeping")
# if not weekday and vacation:
#     print("we are sleeping")


# a_smile = True
# b_smile = True
# if a_smile and b_smile:
#     print('we are in trouble')
# elif not a_smile and not b_smile:
#     print('we are in trouble')
# else:
#     print('we are not in trouble')


