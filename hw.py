hw - 1

# while True:
#     try:
#         number_1 = int(input('Введите первое число'))
#         number_2 = int(input('Введите второе число'))
#         operation = input('Введите операцию: ')

#         if operation == '+':
#             result = number_1 + number_2
#             print(number_1, '+', number_2, '=', result)
#         elif operation == '-':
#             result = number_1 - number_2
#             print(number_1, '-', number_2, '=', result)
#         elif operation == '*':
#             result = number_1 * number_2
#             print(number_1, '*', number_2, '=', result)
#         elif operation == '/':
#             result = number_1 / number_2
#             print(number_1, '/', number_2, '=', result)
#         elif operation == '//':
#             result = number_1 // number_2
#             print(number_1, '//', number_2, '=', result)
#         elif operation == '%':
#             result = number_1 % number_2
#             print(number_1, '%', number_2, '=', result)
#         restart = input('Restart or Quit')
#         if restart == 'no':
#                 break
#         else:
#             print('operation does not exist, please choose another one')
#     except ValueError:
#         print('type integer')


hw - 2


# import random

# def compare_results(player_list, computer_list, opens=False):
#     if sum(player_list) >= 21 and sum(computer_list) >= 21:
#         print('Draw')
#         return True
#     elif sum(player_list) <= 21 and sum(computer_list) <= 21:
#         print(f'You loose {sum(player_list)}! Computer score was {sum(computer_list)}')
#         return True
#     elif  sum(computer_list) > 21 and sum(player_list) <= 21:
#         print(f'You win {sum(player_list)}! Computer score was {sum(computer_list)}')
#         return True
#     else:
#         if opens:
#             if sum(player_list) > 21 and sum(computer_list) <= 21:
#                 print(f'You loose {sum(player_list)}! Computer score was {sum(computer_list)}')
#             elif sum(player_list) < 21 and sum(computer_list) > 21:
#                 print(f'You win {sum(player_list)}! Computer score was {sum(computer_list)}')
#         return False

# def black_jack():
#     cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#     die_or_win = [0, 100, 0, 0, 0]
#     computer = [random.choice(cards), random.choice(cards)]
#     player = [random.choice(cards), random.choice(cards)]

#     while True:
#         try:
#             print('Options')
#             print('1. Draw new card')
#             print('2. Open card')
#             print('4. Russian Roulette')
#             print('5. Only Computer playing roulette')
#             print('6. Reveal sum of computer cards')
#             print('3. End The Game')
#             print(f'your sum of cards --> {sum(player)}')
#             choice = int(input('choose your option'))

#             if choice == 1:
#                 player.append(random.choice(cards))
#                 computer.append(random.choice(cards))
#                 if compare_results(player, computer, opens=True):
#                     print(f'Your sum of cards --> {sum(player)}')
#                     print(f'Sum of computer cards --> {sum(computer)}')
#                     break
#                 else:
#                     print('No winner! Continue the game!')
#                     pass
#             if choice == 2:
#                 compare_results(player, computer, opens=True)
#                 break
#             else:
#                 pass
#             if choice == 3:
#                 print(f'Your sum of cards --> {sum(player)}')
#                 print(f'Sum of computer cards --> {sum(computer)}')
#                 break
#             if choice == 4:
#                 player.append(random.choice(die_or_win))
#                 computer.append(random.choice(die_or_win))
#                 if compare_results(player, computer, opens=True):
#                     break
#                 else:
#                     pass
#             if choice == 5:
#                 computer.append(random.choice(die_or_win))
#                 if compare_results(player, computer, opens=True):
#                     break
#                 else:
#                     pass
#             if choice == 6:
#                 print(f'Sum of computer cards --> {sum(computer)}')
#             else:
#                 print('choice does not exist, please choose another one')
#         except ValueError:
#             print('type integer')


# black_jack()


hw - 3



hw - 4


# def euro(num):
#     result = num * 89.26
#     print('euro: ', result)

# def dollar(num):
#     result = num * 28.06
#     print('dollar: ', result)

# def som(num):
#     result = num * 0.007221
#     print('som: ', result)

# def tenge(num):
#     result = num * 0.0062
#     print('tenge: ', result)

# def transition():
#     while True:
#         try:
#             print('1. transfer from rub to euro ')
#             print('2. transfer from rub to dollar ')
#             print('3. transfer from rub to som ')
#             print('4. transfer from rub to tenge')
#             operation = input('which operation will you choose? : ')
#             num = float(input('enter the amount: '))

#             if operation == '1':
#                 euro(num)
#             elif operation == '2':
#                 dollar(num)
#             elif operation == '3':
#                 som(num)
#             elif operation == '4':
#                 tenge(num)


#         except ValueError:
#             print('type integer')

#         restart = input('Restart or Quit: ')
#     if restart == 'no':


# transition()



hw - 5


# import random

# the_board = {
#     '1': '','2': '','3': '',
#     '4': '','5': '','6': '',
#     '7': '','8': '','9': '',
# }
# board_keys = []
# for key in the_board:
#     board_keys.append(key)

# def paint_board(board):
#     print('---------')
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])
#     print('---------')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('---------')
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])
#     print('---------')

# def game():
#     turn = 'X'
#     count = 0

#     for key in range(10):
#         paint_board(the_board)    
#         print('it is your turn' + turn  + 'to which position')
        
#         move = input('')
#         computer = input('')

#         if the_board[move] == '':
#             the_board[move] = turn 
#             count += 1
#         else:
#             print('that positision is filled , please choose another one')
#             continue
#         if the_board[computer] == '':
#             the_board[computer] = count
#             count += 1

#         if count >= 5:
#             if the_board['1'] == the_board['2'] == the_board['3'] != '':
#                 paint_board(the_board)
#                 print('Game over')
#                 print(turn, 'won')
#                 break
#             if the_board['4'] == the_board['5'] == the_board['6'] != '':
#                 paint_board(the_board)
#                 print('Game over')
#                 print(turn, 'won')
#                 break
#             if the_board['7'] == the_board['8'] == the_board['9'] != '':
#                 paint_board(the_board)
#                 print('Game over')
#                 print(turn, 'won')
#                 break
#             if the_board['1'] == the_board['4'] == the_board['7'] != '':
#                 paint_board(the_board)
#                 print('Game over')
#                 print(turn, 'won')
#                 break
#             if the_board['2'] == the_board['5'] == the_board['8'] != '':
#                 paint_board(the_board)
#                 print('Game over')
#                 print(turn, 'won')
#                 break
#             if the_board['3'] == the_board['6'] == the_board['9'] != '':
#                 paint_board(the_board)
#                 print('Game over')
#                 print(turn, 'won')
#                 break
#             if the_board['1'] == the_board['5'] == the_board['9'] != '':
#                 paint_board(the_board)
#                 print('Game over')
#                 print(turn, 'won')
#                 break
#             if the_board['3'] == the_board['5'] == the_board['7'] != '':
#                 paint_board(the_board)
#                 print('Game over')
#                 print(turn, 'won')
#                 break
#         if count == 9:
#             print('Game over')
#             print('No one wins')

#         if turn == 'X':
#             turn = 'O'
#         else:
#             turn = 'X'
#     restart = input('restart or stop? ')
#     if restart == 'yes' or restart == 'YES':
#         for key  in board_keys:
#             the_board[key] = ''
#         game()

# game()


hw - 6


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

# import time

# def say_family(func):
#     def wrapper():
#         print('What are your sisters names?')
#         func('Zhibek', 'Madina', 'Rayana', 'Regina')

#     return wrapper()

# @say_family
# def list(name1, name2, name3, name4):
#     time.sleep(1.5)
#     print(f'{name1}')
#     time.sleep(2)
#     print(f'{name2}')
#     time.sleep(2)
#     print(f'{name3}')
#     time.sleep(2)
#     print(f'{name4}')
#     time.sleep(2)



hw - 7


# import time

# class Animal:

#     def __init__(self, kind, name, age, color, habitat):
#         if isinstance(kind, str):
#             self.kind = kind
#         else:
#             raise ValueError('type integer')
#         if isinstance(name, str):
#             self.name = name
#         else:
#             raise ValueError('type integer')
#         if isinstance(age, int):
#             self.age = age
#         else:
#             raise ValueError('age can be only numeric')
#         if isinstance(color, str):
#             self.color = color
#         else:
#             raise ValueError('type integer')
#         if isinstance(habitat, str):
#             self.habitat = habitat
#         else:
#             raise ValueError('type integer')

#     def __str__(self):
#         return f'{self.kind}, {self.name}, {self.age}, {self.color}, {self.habitat}'
        
# class Assistant:
#     def care(self):
#         print('Dont give too hard food.')
#         time.sleep(3)

# class Chicken(Animal, Assistant):

#     def __init__(self, kind, name, age, color, habitat, size):

#         super(Chicken, self).__init__(kind, name, age, color, habitat)

#         if isinstance(size, str):
#             self.size = size
#         else:
#             raise ValueError('type integer')

#     def __str__(self):
#         return f'{self.kind}, {self.name}, {self.age}, {self.color}, {self.habitat}, {self.size}'

#     def details(self):
#         print('1. Learn more')
#         print('2. Go to another')
#         choice = int(input('choose your path ninja: '))

#         if choice == 1:
#             print('Chickens are very cute animals only when they are still small.')
#         elif choice == 2:
#             print('do you really want to know about cute chicks? ')
#         else:
#             print('IT IS OVER')
        
# chicken = Chicken(kind='Chicken', name='Normal', age=1, color='Yellow', habitat='Asia', size='S')
# print(chicken)

# class Dog(Animal, Assistant):

#     def __init__(self, kind, name, age, color, habitat, size, mood):

#         super(Dog, self).__init__(kind, name, age, color, habitat)

#         if isinstance(size, str):
#             self.size = size
#         else:
#             raise ValueError('type integer')
#         if isinstance(mood, str):
#             self.mood = mood
#         else:
#             raise ValueError('type integer')

#     def __str__(self):
#         return f'{self.kind}, {self.name}, {self.age}, {self.color}, {self.habitat}, {self.size}, {self.mood}'

#     def details(self):
#         print('1. Learn more')
#         print('2. Go to another')
#         choice = int(input('choose your path ninja: '))

#         if choice == 1:
#             print('Dogs are very intelligent and loyal animals.')
#         elif choice == 2:
#             print('Do you think this is the right choice?')
#         else:
#             print('IT IS OVER')

# dog = Dog(kind='Dog', name='Spitz', age=4, color='White', habitat='Europe', size='M', mood='Fine')
# print(dog)

# class Zoo_show:
#     def show(self):
#         time.sleep(1)
#         print('Start')
#         time.sleep(2)
#         print('p.s the show is on')
#         time.sleep(2)
#         print('End the show')


# class Ticket(Zoo_show):

#     def __init__(self, all_money):
#         self.all_money = all_money

#     def home(self):
#         print(f'You have ${self.all_money}, what will you spend on? ')
#         print('1. Chicken / 100$')
#         print('2. Dog / 100$')
#         print('3. Watch the show / 150$')
#         choice = input('Choose a number: ')

#         if choice == '1':
#             self.all_money -= 100
#             print(f'you have {self.all_money}$')
#             chicken.details()
#         elif choice == '2':
#             self.all_money -= 100
#             print(f'you have {self.all_money}$')
#             dog.details()
#         elif choice == '3':
#             self.all_money -= 150
#             print(f'you have {self.all_money}$')
#             zoo_show = Zoo_show()
#             zoo_show.show()

#         last = input('Do you want to choose another? ')
#         print('yes / no')

#         if last == 'yes':
#             self.home()

# ticket = Ticket(all_money=500)
# ticket.home()



hw - 8


