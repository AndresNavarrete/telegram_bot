import random 

def love_msg():
    with open('messages/love_messages.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return random.choice(lines)
