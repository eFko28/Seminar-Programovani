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

def generate_example() -> int:      #vytvoreni prikladu
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
    return number1, number2, operation, result #vrati vsechny hodnoty, se kteryma budu potom pracovat




def exercise_generator_simple_2numbers(): #tato fce bezi az do konce(Q input od usr)
    while True:
        try:   
            number1, number2, operation, result = generate_example()
            operation = str(operation)
            if operation == "1":
                operation = "*"
            elif operation == "2":
                operation = "/"
            elif operation == "3":         #prevedeni hodnot pod var opration na stringy
                operation = "+"
            elif operation == "4":
                operation = "-"

            print(f"Exercise: {number1} {operation} {number2}")    #vypsani prikladu usr
            user_result = input("Your answer: (or enter Q to end the program) ")  #input vysledku
            if user_result == "Q":   #pokud Q, rozbije loop a ukonci tedy program
                print("Quitting the exercise generator")
                break
            elif user_result == "q":
                print("Quitting the exercise generator")
                break
            user_result = float(user_result)
            if user_result == result:   #porovnani spravneho vysledku
                print("Thats right, generating another exercise")
            elif user_result != result:
                print(f"That wasnt right! The correct result was: {result}")
                print("Generating another exercise.")
        except ValueError:    #osetreni vstupu
            print("Non-numerical input. Generating a new exercise.")


print("The program will generate a random exercise. You can either answer it or enter Q to quit.")
exercise_generator_simple_2numbers()

    

##############################################################
### Generátor příkladů - n čísel a operace mezi nimi (+, -), přidána funkce statistika
# funkce numbers_generator, example_generator_advance, user_statistics, celková fce example_generator_processor
print("\nVer2: stats, n numbers")

def create_variables() -> list:    #vytvoreni listu x hodnot (dle usr inputu) pro priklady
    while True:
        try:
            term_count = int(input("How many terms would you like to have to exercise with? (2-10) "))
            if 2 <= term_count <= 10:
                variables = []
                for i in range(term_count):      #vytvoreni listu, delka dle poskytnuteho inputu
                    variables.append(random.randint(1, 10))
                return variables

            elif term_count < 2 or term_count > 10:
                print("Incorrect input. Must input whole numbers 2-10.")  #ostreni vstupu, jen cisla ktera davaji smysl
              
        except ValueError:     #osetreni vstupu, pouze cisla
            print("Incorrect input. Must input whole numbers 2-10.")


def create_operations(term_count: int) -> list:  #vytvoreni listu operaci, uz potrebujeme zadat do funkce promennou -> delka listu
    operations_list_random = []
    operations_list = ["+", "-", "*", "/"]
    for i in range(1, term_count + 1):   #kvuli generalizaci davame +1
        operations_list_random.append(random.choice(operations_list))
    return operations_list_random  #vrati hodnoty

def generate_example() -> str:   #vytvoreni prikladu
    variables = create_variables()    #uziti definiovanych funkci
    operations = create_operations(len(variables) - 1)    # -1, protoze potrebujeme o 1 vice cisel nez operaci
    example = ""    #vytvoreni str example
    for i in range(len(variables) - 1):    #prida do str example vzdy 1. variables, 1. operations, 2. 2., 3. 3. atd, dle delky variables
        example += str(variables[i]) + " " + operations[i] + " "
    example += str(variables[-1])    #dodani posledni ciselne promenne (cisel o 1 vic nez operaci)
    return example #vrati str pro fci eval()

def evaluate_example(example: str) -> float:   #vyhodnoti priklad, str -> float
    try:
        return round(eval(example), 4)
    except ZeroDivisionError:       #pokud neexistuje reseni kvuli deleni 0, nevrati nic
        return None
    

def exercise_generator_n_numbers():   #finalni fce - vsecky predtim definovane spoji do finalniho programu
    correct_answers = 0      #definice promennych pro statistiky
    wrong_answers = 0
    total_answers = 0
    while True:
        example = generate_example()   #vytvori hodnoty, vyhodnoti je a pokud nebude existovat hodnota z fce evaluate_example (deleni nulou)
        result = evaluate_example(example)          #provede continue -> bude donekonecna vytvaret hodnoty, dokud jedna nebude existovat
        if result is None:
            continue
        print(f"Expression to solve: {example} (or Q to quit the program.)")     #podnet pro usr
        while True:
            try:
                user_result = input("")   #input vysledku od usr
                total_answers += 1
                if user_result.lower() == "q":  #pokud Q, rozbije program
                    print("Quitting the exercise generator. Hope you liked it!")
                    print(f"\nStatistics: Correct answers: {correct_answers}, Wrong answers: {wrong_answers}, Total answers: {total_answers}")
                    return    #zde return, protoze tehdy ukonci python celou fci (pokud neco vrati, nemuze dal probihat)
                user_result = float(user_result) #prevedeni na float
                if round(user_result, 4) == result:  #porovnani usr inputu s presnosti na 4 desetinne mista
                    print("Thats right! Generating another exercise:")
                    correct_answers += 1
                    break
                elif round(user_result, 4) != result:
                    print(f"That wasnt right! The correct result was: {result}")
                    wrong_answers += 1
                    break

            except ValueError:  #osetreni vstupu
                print("Incorrect input. Must be numbers (or Q for quitting).")

print("The program will now also ask with how many terms you wish to practice with. You can either answer or input Q to quit like before.")
exercise_generator_n_numbers()



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
