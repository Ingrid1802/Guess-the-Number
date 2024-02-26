## Adivina el Número - Guess the Number

### Descripción
Este proyecto implementa el juego "Adivina el Número" en Python, donde tanto el jugador como la computadora intentan adivinar el mismo número secreto generado aleatoriamente. Se ha integrado la mecánica de "frío o caliente", que proporciona pistas al jugador sobre la cercanía de su suposición al número secreto.

### Información sobre `main.py`

El archivo `main.py` contiene la lógica principal del juego y se compone de las siguientes funciones:

- `colorize(message, color)`: Aplica formato de color a un mensaje de texto para la salida en la consola.
- `cold_or_hot(secret_number, guess)`: Determina si la suposición del jugador está "fría" o "caliente" en relación al número secreto.
- `computer_guess(min_num, max_num, last_guess, feedback, computer_guesses, secret_number)`: Implementa la lógica de adivinanza de la computadora.
- `guess_the_number()`: Función principal que ejecuta el juego.

#### Lógica de "frío o caliente"

La función `cold_or_hot(secret_number, guess)` calcula la diferencia absoluta entre el número secreto y la suposición del jugador para determinar qué tan cerca está la suposición del número secreto. Según esta diferencia, se devuelve un mensaje indicando si la suposición está "fría" (lejos), "tibia" (cerca) o "caliente" (muy cerca) del número secreto.

#### Función `computer_guess`

La función `computer_guess(min_num, max_num, last_guess, feedback, computer_guesses, secret_number)` implementa la lógica de adivinanza de la computadora. Utiliza las suposiciones previas de la computadora y la retroalimentación recibida para calcular la siguiente suposición de la computadora.

### Ejecución de las pruebas

El archivo `test_main.py` contiene pruebas unitarias para las funciones en `main.py`. Estas pruebas aseguran el correcto funcionamiento de las funciones, incluyendo la lógica de "frío o caliente" y la lógica de adivinanza de la computadora.
