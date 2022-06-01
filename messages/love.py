''' love messages manager'''

import random


def love_msg():
    ''' get random love message'''

    with open("data/love_messages.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return random.choice(lines)
