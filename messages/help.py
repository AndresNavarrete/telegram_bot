
import random 

def help_menu():
    msg = """

        Hola amorcito! ❤️ ❤️ ❤️

        Escribe el número de opción que quieres ver

        1. Mensajito de amor
        2. Dedicación de canciones
        3. Recomendación de película
        4. Recomendación de video de Youtube

    """
    return msg

def love_msg():
    with open('messages/love_messages.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return random.choice(lines)

