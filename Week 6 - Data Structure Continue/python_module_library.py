import os
from datetime import date

def clear_screen():
    # 'nt' means Windows, others are usually Unix-based
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_for_action():
    input('Hit any key to continue ...')

def sum_value(*args):
    return sum(args)

def exp_value(number, power):
    return number ** power

def displayWelcomeMessage(nb):
    print('-' * nb)
    print('Welcome to the guesting number game.\nYou have 10 chances trying to guest the number.')
    print(f"Today is {date.today().strftime('%d %b %Y')}")
    print('-' * nb)