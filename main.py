import random
import emoji
from colorama import Fore, Style

def colorize(message, color):
    return f"{color}{message}{Style.RESET_ALL}"


def cold_or_hot(secret_number, guess):
    diff = abs(secret_number - guess)
    if diff >= 30:
        return colorize("¡Friooo, friooo! Te congelas.", "\033[38;2;0;0;255m")  # Azul intenso
    elif diff >= 20:
        return colorize("Ummm aun estas Friooo.", "\033[38;2;51;186;248m")  # Azul claro
    elif diff >= 10:
        return colorize("Ya casiii, estas tibio.", "\033[38;2;229;189;57m")  # Amarillo
    elif diff >= 5:
        return colorize("Uyyy ya estas caliente, vamos tu puedessss.", "\033[38;2;255;127;80m")  # Naranja
    else:
        return colorize("¡Calienteee, calienteeee! ya te quemas.", "\033[38;2;255;0;0m")  # Rojo




def computer_guess(min_num, max_num, last_guess, feedback, computer_guesses, secret_number):
    if feedback == 'low':
        min_num = max(min_num, last_guess + 1)  # Actualizar min_num correctamente
    elif feedback == 'high':
        max_num = min(max_num, last_guess)

    valid_guesses = [x for x in range(min_num, max_num + 1) if x not in computer_guesses]

    if not valid_guesses:
        min_num = 1
        max_num = 100
        valid_guesses = [x for x in range(min_num, max_num + 1) if x not in computer_guesses]

    computer_guess_num = random.choice(valid_guesses)
    amarillo_verde = "\033[38;2;154;205;50m"
    print(f"{amarillo_verde}La computadora supone que el número es {computer_guess_num}.{Fore.RESET}")
    print(colorize(cold_or_hot(secret_number, computer_guess_num), Fore.CYAN))
    return computer_guess_num




def guess_the_number():
   while True:
        secret_number = random.randint(1, 100)
        jugador_suposiciones = []
        computer_guesses = []
        welcome_message = "¡Bienvenido a Adivina el Número!"
        console_width = 80  # Ancho de la consola
        welcome_message_centered = welcome_message.center(console_width - 6)  # Dejamos 2 espacios menos en cada lado
        asterisks_line = "*" * (console_width - 2)
        print(colorize("*" * console_width, Fore.MAGENTA))
        print(colorize(f"*  {welcome_message_centered}  *", Fore.MAGENTA))
        print(colorize(f"*{asterisks_line}*", Fore.MAGENTA))
        print("Estoy pensando en un número entre 1 y 100. Adivina cuál es.".center(console_width))
        
        while True:
            try:
                rosa = "\033[38;2;255;192;203m"  # Código de color para #FFC0CB
                guess = int(input(f"{rosa}Tu suposición: {Fore.RESET}"))
                if guess < 1 or guess > 100:
                    raise ValueError("El número debe estar entre 1 y 100.")
            except ValueError:
                print("Por favor, ingresa un número válido entre 1 y 100.")
                continue

            jugador_suposiciones.append(guess)
            
            if guess < secret_number:
                print(colorize(cold_or_hot(secret_number, guess), Fore.BLUE))
                print("¡Muy bajo! Intenta de nuevo.")
            elif guess > secret_number:
                print(colorize(cold_or_hot(secret_number, guess), Fore.BLUE))
                print("¡Muy alto! Intenta de nuevo.")
            else:
                print(f"🎉🎉🎉¡Correcto! El número era {secret_number}. ¡Has adivinado! 🎉🎉🎉")
                break

            computer_guess_num = computer_guess(guess, 100, guess, 'low' if guess < secret_number else 'high', computer_guesses, secret_number)
            
            if computer_guess_num is None:
                print("La computadora no puede hacer una suposición válida.")
                break

            if computer_guess_num < secret_number:
                print("La suposición de la computadora es muy baja.")
            elif computer_guess_num > secret_number:
                print("La suposición de la computadora es muy alta.")
            else:
                print(f"🎉🎉🎉 ¡La computadora ha adivinado! El número era {secret_number}. 🎉🎉🎉")
                break

            computer_guesses.append(computer_guess_num)
        
        print(f"Suposiciones de la jugadora: {jugador_suposiciones}")
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_de_nuevo.lower() != 's':
            print("¡Gracias por jugar! ¡Hasta luego!")
            break

# Llama a la función para comenzar el juego
if __name__ == "__main__":
    guess_the_number()