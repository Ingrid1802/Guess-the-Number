from main import colorize, cold_or_hot, computer_guess, guess_the_number
from colorama import Style
import pytest
from unittest.mock import patch, MagicMock



###########    test para la funcion colorize    ###########

def test_colorize():
    # Mensaje de prueba y color ANSI para rojo
    mensaje = "Hola, mundo!"
    color = "\033[91m"  # Rojo
    resultado_esperado = f"\033[91mHola, mundo!{Style.RESET_ALL}"

    # Llamamos a la función colorize con el mensaje y el color de prueba
    resultado = colorize(mensaje, color)

    # Verificamos que el resultado sea el esperado
    assert resultado == resultado_esperado






###########    test para la funcion cold_or_hot    ###########

# Usamos parametrize para probar varios casos de prueba con una sola función de test
@pytest.mark.parametrize("secret_number, guess, expected_contains", [
    (50, 80, "¡Friooo, friooo! Te congelas."),  # Diferencia de 30, mensaje de muy frío
    (50, 70, "Ummm aun estas Friooo."),  # Diferencia de 20, mensaje de frío
    (50, 60, "Ya casiii, estas tibio."),  # Diferencia de 10, mensaje de tibio
    (50, 55, "Uyyy ya estas caliente, vamos tu puedessss."),  # Diferencia de 5, mensaje de caliente
    (50, 52, "¡Calienteee, calienteeee! ya te quemas."),  # Diferencia menor a 5, mensaje de muy caliente
])
def test_cold_or_hot(secret_number, guess, expected_contains):
    result = cold_or_hot(secret_number, guess)
    assert expected_contains in result




###########    test para la funcion computer_guess    ###########
    

    #Cobertura de Casos Extremos:
@pytest.mark.parametrize("last_guess, feedback, expected_range", [
    (1, 'low', (2, 100)),  # Caso extremo inferior
    (99, 'high', (1, 98)),  # Caso extremo superior
])
def test_computer_guess_extreme_cases(last_guess, feedback, expected_range):
    min_num = 1
    max_num = 100
    computer_guesses = []
    secret_number = 75  # No se utiliza directamente en la prueba

    with patch('main.random.choice') as mock_choice:
        mock_choice.side_effect = lambda x: x[0]  # Simula la selección del primer número válido
        guess = computer_guess(min_num, max_num, last_guess, feedback, computer_guesses, secret_number)
        
        assert expected_range[0] <= guess <= expected_range[1], "El número adivinado no está en el rango esperado para casos extremos."



    #Pruebas con computer_guesses No Vacío:
def test_computer_guess_with_non_empty_guesses():
    min_num = 1
    max_num = 100
    last_guess = 50
    feedback = 'low'
    computer_guesses = [51, 52, 53]  # Suposiciones previas que deben ser excluidas
    secret_number = 75  # No se utiliza directamente en la prueba

    with patch('main.random.choice') as mock_choice:
        mock_choice.return_value = 54  # Seleccionamos un número que no esté en `computer_guesses`
        guess = computer_guess(min_num, max_num, last_guess, feedback, computer_guesses, secret_number)
        
        assert guess not in computer_guesses, "El número adivinado no debería estar en las suposiciones previas."
    
    
    
    #Múltiples Rondas de Adivinanzas:
def test_computer_guess_multiple_rounds():
    min_num = 1
    max_num = 100
    secret_number = 75  # No se utiliza directamente en la prueba
    guesses_sequence = [
        (50, 'low'),  # Primera suposición, actualiza min_num a 51
        (60, 'low'),  # Segunda suposición, actualiza min_num a 61
        (70, 'low'),  # Tercera suposición, actualiza min_num a 71
    ]
    computer_guesses = []

    for last_guess, feedback in guesses_sequence:
        with patch('main.random.choice') as mock_choice:
            mock_choice.side_effect = lambda x: x[0]  # Simula la selección del primer número válido
            guess = computer_guess(min_num, max_num, last_guess, feedback, computer_guesses, secret_number)
            
            # Asegurar que la suposición está en el rango esperado después de cada actualización
            assert last_guess < guess <= max_num, "La suposición no se ajusta al rango esperado tras múltiples rondas."
            computer_guesses.append(guess)  # Añadir la suposición para la siguiente ronda







###########    test para la funcion guess_the_number   ###########



@pytest.fixture
def mock_inputs():
    # Simula las entradas del usuario: una adivinanza correcta y luego 'n' para no jugar de nuevo
    return iter(["50", "n"])

@pytest.fixture
def mock_randint():
    # Simula siempre devolver 50 como el número secreto
    return 50

def test_guess_the_number_correct_first_try(mock_inputs, mock_randint):
    with patch('builtins.input', lambda _: next(mock_inputs)):
        with patch('builtins.print') as mock_print:
            with patch('random.randint', return_value=mock_randint):
                guess_the_number()
                # Verifica que se imprima el mensaje de victoria
                mock_print.assert_any_call("🎉🎉🎉¡Correcto! El número era 50. ¡Has adivinado! 🎉🎉🎉")


def test_guess_the_number_invalid_input(mock_inputs, mock_randint):
    with patch('builtins.input', side_effect=["101", "50", "n"]):  # Primero un número inválido, luego la adivinanza correcta, y no jugar de nuevo
        with patch('builtins.print') as mock_print:
            with patch('random.randint', return_value=50):
                guess_the_number()
                mock_print.assert_any_call("Por favor, ingresa un número válido entre 1 y 100.")
