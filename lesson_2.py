import random

def compare_results(player_list, computer_list, opens=False):
    if sum(player_list) >= 21 and sum(computer_list) >= 21:
        print('Draw')
        return True
    elif sum(player_list) <= 21 and sum(computer_list) <= 21:
        print(f'You loose {sum(player_list)}! Computer score was {sum(computer_list)}')
        return True
    elif  sum(computer_list) > 21 and sum(player_list) <= 21:
        print(f'You win {sum(player_list)}! Computer score was {sum(computer_list)}')
        return True
    else:
        if opens:
            if sum(player_list) > 21 and sum(computer_list) <= 21:
                print(f'You loose {sum(player_list)}! Computer score was {sum(computer_list)}')
            elif sum(player_list) < 21 and sum(computer_list) > 21:
                print(f'You win {sum(player_list)}! Computer score was {sum(computer_list)}')
        return False

def black_jack():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    die_or_win = [0, 100, 0, 0, 0]
    computer = [random.choice(cards), random.choice(cards)]
    player = [random.choice(cards), random.choice(cards)]

    while True:
        try:
            print('Options')
            print('1. Draw new card')
            print('2. Open card')
            print('4. Russian Roulette')
            print('5. Only Computer playing roulette')
            print('6. Reveal sum of computer cards')
            print('3. End The Game')
            print(f'your sum of cards --> {sum(player)}')
            choice = int(input('choose your option'))

            if choice == 1:
                player.append(random.choice(cards))
                computer.append(random.choice(cards))
                if compare_results(player, computer, opens=True):
                    print(f'Your sum of cards --> {sum(player)}')
                    print(f'Sum of computer cards --> {sum(computer)}')
                    break
                else:
                    print('No winner! Continue the game!')
                    pass
            if choice == 2:
                compare_results(player, computer, opens=True)
                break
            else:
                pass
            if choice == 3:
                print(f'Your sum of cards --> {sum(player)}')
                print(f'Sum of computer cards --> {sum(computer)}')
                break
            if choice == 4:
                player.append(random.choice(die_or_win))
                computer.append(random.choice(die_or_win))
                if compare_results(player, computer, opens=True):
                    break
                else:
                    pass
            if choice == 5:
                computer.append(random.choice(die_or_win))
                if compare_results(player, computer, opens=True):
                    break
                else:
                    pass
            if choice == 6:
                print(f'Sum of computer cards --> {sum(computer)}')
            else:
                print('choice does not exist, please choose another one')
        except ValueError:
            print('type integer')


black_jack()

