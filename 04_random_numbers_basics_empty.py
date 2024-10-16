# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
04) random_numbers_basics.py

Vygeneruj 2 náhodná čísla od 1 do 10, zvol náhodou operaci, zobraz, zeptej se na výsledek, zkontroluj.
* Přidej opakování, dokud nebude stiknuto "q" nebo "Q"
* Přidej statistiku - počet správných odpovědí / celkem příkladů
** Rozděl hlavní funkci na části tak, aby bylo možno generovat příklady i s více čísly (př.: 5+6-4), stačí operace + a -,
   volbu počtu čísel v příkladu ponech na uživateli

"""

import random
import os


# Globální konstanty a proměnné
CORRECT_ANSWERS = 0          # využito ve funkci statistika() ve 2. části
WRONG_ANSWERS = 0           # využito ve funkci statistika() ve 2. části


os.system("cls")


##############################################################
### Generátor příkladu - 2 čísla a operace, ověření výsledku, zodpovězení, opakování dokud q
# fce generate_example, exercise_generator_simple, celková funkce example_generator_2numbers
print("Ver1: Exercise generator")

def generate_example() -> int:
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)

    operation = random.randint(1, 4)

    if operation == 1:
        result = number1 * number2
    elif operation == 2:
        result = number1 / number2
    elif operation == 3:
        result = number1 + number2
    else:
        result = number1 - number2
    return number1, number2, operation, result




def exercise_generator_simple_2numbers():
    while True:
        try:
            number1, number2, operation, result = generate_example()
            operation = str(operation)
            if operation == "1":
                operation = "*"
            elif operation == "2":
                operation = "/"
            elif operation == "3":
                operation = "+"
            elif operation == "4":
                operation = "-"

            print(f"Exercise: {number1} {operation} {number2}")
            user_result = input("Your answer: (or enter Q to end the programm)")
            if user_result == "Q":
                print("Quitting the exercise generator")
            elif user_result == "q":
                print("Quitting the exercise generator")
                break
            user_result = float(user_result)
            if user_result == result:
                print("Thats right, generating another exercise")
            elif user_result != result:
                print(f"That wasnt right! The correct result was: {result}")
                print("Generating another exercise.")
        except ValueError:
            print("Non-numerical input. Generating a new exercise.")


print("The programm will generate a random exercise. You can either answer it or enter Q to quit.")
exercise_generator_simple_2numbers()

    

##############################################################
### Generátor příkladů - n čísel a operace mezi nimi (+, -), přidána funkce statistika
# funkce numbers_generator, example_generator_advance, user_statistics, celková fce example_generator_processor
print("Ver2: stats, n numbers")

def create_variables() -> list:
    while True:
        try:
            term_count = int(input("How many terms would you like to have to exercise with? (2-10)"))
            if 2 <= term_count <= 10:
                variables = []
                for i in range(1, term_count + 1):
                    variables.append(random.randint(1, 10))
                return variables
            elif term_count < 2 or term_count > 10:
                print("Incorrect input. Must input whole numbers 2-10.")
              
        except ValueError:
            print("Incorrect input. Must input whole numbers 2-10.")       
        
def create_operations(term_count) -> dict:
    while True:
        try:
            if 2 <= term_count <= 10:
                variables = {}
                for i in range(term_count):
                    operation = f'operation{i + 1}'
                    
                    
                return variables
            elif term_count < 2 or term_count > 10:
                print("Incorrect input. Must input whole numbers 2-10.")
              
        except ValueError:
            print("Incorrect input. Must input whole numbers 2-10.")     







def generate_example() -> int:
    numbers = create_variables()

    operation = random.randint(1, 4)

    if operation == 1:
        result = 
    elif operation == 2:
        result = number1 / number2
    elif operation == 3:
        result = number1 + number2
    else:
        result = number1 - number2
    return numbers, operation, result




def exercise_generator_simple_2numbers():
    while True:
        try:
            numbers, operation, result = generate_example()
            operation = str(operation)
            if operation == "1":
                operation = "*"
            elif operation == "2":
                operation = "/"
            elif operation == "3":
                operation = "+"
            elif operation == "4":
                operation = "-"
                
            print(f"Exercise: {number1} {operation} {number2}")
            user_result = input("Your answer: (or enter Q to end the programm)")
            if user_result == "Q":
                print("Quitting the exercise generator")
            elif user_result == "q":
                print("Quitting the exercise generator")
                break
            user_result = float(user_result)
            if user_result == result:
                print("Thats right, generating another exercise")
            elif user_result != result:
                print(f"That wasnt right! The correct result was: {result}")
                print("Generating another exercise.")
        except ValueError:
            print("Non-numerical input. Generating a new exercise.")


print("The programm will generate a random exercise. You can either answer it or enter Q to quit.")
exercise_generator_simple_2numbers()




##############################################################
### Spuštění programu - MAIN
"""
Následující podmínka (if __name__ == "__main__":) zajistí, že se kód v bloku pod touto podmínkou spustí pouze tehdy, 
když je skript spuštěn přímo. Pokud je soubor importován do jiného skriptu, kód v tomto bloku se nespustí.
Jinými slovy lze celý tento soubor v případě potřeby importovat do jiného, hlavního souboru.

__name__ je speciální proměnná, kterou Python automaticky nastaví, až když se skript spouští.
Pokud skript spouštíte přímo jako hlavní program/soubor (např. python muj_skript.py), proměnná __name__ bude mít hodnotu "main".
vs.
pokud skript importujete do jiného skriptu (např. import 04_random_numbers_basics.py), __name__ bude mít hodnotu název souboru 
(zde "04_random_numbers_basics").
"""

if __name__ == "__main__":
    random.seed()
    print("\nPRVNÍ ČÁST PROGRAMU")
    example_generator_2numbers()
    print("------------------------------------------------")
    print("DRUHÁ ČÁST PROGRAMU")
    example_generator_processor()
    print(f"Odpovědi: ve druhé části programu bylo zodpovězeno {CORRECT_ANSWERS} správně a {WRONG_ANSWERS} špatně.\n")
