# import random

# door = ['auto', 'empty']

# def choose_doors():
#     try:
#         choice = random.choice(door)
#         print('you did your choice')
#         judje = input('one of the doors is revealed, and it is not prize door: '
#                     'do you want to change your mind?')
        
#         if judje == 'yes':
#             print('your original choice was ', choice)
#             if choice == 'auto':
#                 choice = 'empty'
#                 print('your  new choice is', choice)
#                 print('you loose')
#             else:
#                 choice = 'auto'
#                 print('your  new choice is', choice)
#                 print('you win')
#         if judje == 'no':
#             print('your choice is', choice)
#             if choice == 'auto':
#                 print('You win the auto!')
#             else:
#                 print('you loose')
#         else:
#             print('choice does not exist, please choose another one')
#     except ValueError:
#             print('type integer')


# choose_doors()


# ---------------------------------------------------------------------------------------------


# cash = [500,
#         200,
#         100,
#         50,
#         20,
#         10,
#         1]
# def bankomat(pika):
#     for pati in cash:
#         bankomat, residue = divmod(pika, pati)
#         pika = residue
#         if bankomat != 0:
#             for p in range(bankomat):
#                 print(pati)
#             if residue == 0:
#                 break

# bankomat(int(input('сколько денег ты хочешь получить: ')))


# ---------------------------------------------------------------------------------------------


text = """
The Zen of Python , by Tim Peters. 
Beautiful is better than ugly.  
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested.     
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambiguity, refuse dan the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those! 
"""
def note(word):
    return 'd' in word.lower()


# -------------------------------------------------------------- 

    
result = filter(note, text.split(' '))
print([i.replace('\n', '') for i in list(result)])

# cash = [5000,
#         2000,
#         1000,
#         500,
#         200,
#         100,
#         50,
#         20,
#         10,
#         5,
#         3,
#         1]
# def banknote(amout):
#     for money in cash:
#         banknotes, remainder = divmod(amout, money)
#         amout = remainder
#         if banknotes != 0:
#             for k in range(banknotes):
#                 print(money)
#             if remainder == 0:
#                 break

# banknote(int(input('how much money do you want to get: ')))

