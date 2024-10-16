# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
01_review_Jypyter_1-7.py
Vypracujte bez použití AI a připojení k netu. 12 úkolů.

VYPRACOVAL/A: JOSEF KOVář
-----------------------------------------------------------------
"""

import os

os.system("cls")


##############################################################
# 1. Úkol: Základní aritmetické operace
# Napište kód, který bude načítat 2 čísla od uživatele (number1 a number2) a bude:
    # a) sčítat dvě načtená čísla (suma)
    # b) používat dělení a vracet jak běžné, tak celočíselné dělení (quotient, integer_division)
print("1:")
# Načtení čísel
number1 = float(input("Number 1:"))
number2 = float(input("Number 2:"))


# a) Sčítání
output = number1 + number2
print(f"The sum of your numbers is: {output}")

# b) Dělení a celočíselné dělení
output = number1 / number2
print(f"The quotient of your numbers is {output}")
output = number1 // number2
print(f"For integer division, the result is: {output}")


##############################################################
# 2. Úkol: Exponenty
# Doplňte kód, který načte číslo od uživatele a:
# a) spočítá třetí odmocninu čísla
# b) spočítá druhou odmocninu čísla
print("2:")
# Načtení čísla
number = float(input("Number to make a square and a cube root out of:"))


# a) Třetí odmocnina

output = number ** (1/3)
print(f"The cubed number you inputed is: {output}")

# b) Druhá odmocnina
output = number ** (1/2)
print(f"The squared number you inputed is: {output}")


##############################################################
# 3. Úkol: Práce s proměnnými
# Zadejte proměnnou 'my_savings' a přiřaďte jí hodnotu od uživatele (např. 200)
# Poté vypočítejte, kolik budete mít peněz po přidání 10% úroků, které si uložíte do proměnné 'my_interest'.
print("3:")
my_savings = float(input("How much money you got? "))
my_interest = my_savings * 1.1

print(f"With 10% interest youll have {my_interest}")


##############################################################
# 4. Úkol: Operace s řetězci
# Napište kód, který:
    # a) načte dva řetězce od uživatele (string1 a string2)
    # b) zkontroluje, zda jsou oba řetězce stejné délky
    # c) spojí oba řetězce do jednoho a vypíše výsledek
print("4:")
# a) Načtení řetězců
print("Think of an input and divide it into 2 of the same length")
# b) Zkontrolujte délku řetězců + C)     :))
while True:
    
    string1 = input("First piece of your input:")
    string2 = input("Second piece of your input:")
    if len(string1) == len(string2):
        break
    else:
        print("Your pieces are not of the same length.")



# c) Spojení řetězců

print(F"This is the two pieces conjuncted: {string1 + string2}")



##############################################################
# 5. Úkol: Práce s cykly
# Napište kód, který:
    # a) načte číslo od uživatele (např. 16)
    # b) vypíše všechna čísla od 1 do tohoto čísla
    # c) na každém pátém čísle vypíše text "Pátý krok!"
print("5:")
# Načtení čísla
number = int(input("Type a number:"))



# b) Výpis čísel
for a in range(1, number + 1):
    print(a)
    if a % 5 == 0:
        print("That was the fifth step!")






##############################################################
# 6. Úkol: Slovníky v Pythonu
# Napište kód, který:
    # a) vytvoří prázdný slovník "person"
    # b) přidá do slovníku tři položky, které načte od uživatele (např. name, age, city)
    # c) vypíše všechny klíče a hodnoty slovníku v cyklu
print("6:")
# a) Vytvoření slovníku
person = {}

# b) Načtení údajů od uživatele
name = input("enter your name: " )
age = input("enter your age: ")
city = input("enter city: ")
# Přidání údajů do slovníku
person["name"] = name
person["age"] = age
person["city"] = city

# c) Výpis slovníku
print(f"Your name is {person["name"]}, you are {person["age"]} years old and live in {person["city"]}")


##############################################################
# 7. Úkol: Použití f-string
# Napište kód, který načte dva číselné údaje (např. result, score) a poté:
    # a) použije f-string pro vložení těchto hodnot do textu
    # b) použije f-string pro zobrazení těchto hodnot s přesností na 2 desetinná místa
print("7:")
# Načtení čísel
result = float(input("your result: "))
score = float(input("your score: "))

# a) Použití f-string
print(f"Your result is: {result} and youre score is: {score}")

# b) Použití f-string s přesností na 2 desetinná místa
print(f"Your result is: {round(result, 2)} and your score is: {round(score, 2)}")


##############################################################
# 8. Úkol: Vytváření seznamů a indexování
# Napište kód, který:
    # a) vytvoří seznam my_list o pěti prvcích na základě vstupu od uživatele
    # b) vypíše třetí prvek seznamu
    # c) vypíše poslední dva prvky seznamu
print("8:")
# a) Vytvoření seznamu
a = input("Prvek 1: ")
b = input("Prvek 2: ")
c = input("Prvek 3: ")
d = input("Prvek 4: ")
e = input("Prvek 5: ")

my_list = [a, b, c, d, e]


# b) Třetí prvek
print(f"Treti prvek je: {my_list[2]}")

# c) Poslední dva prvky
print(f"Posledni dva prvky seznamu jsou: {my_list[-2:]}")

##############################################################
# 9. Úkol: Základní metody seznamu
# Napište kód, který:
    # a) vytvoří seznam my_list o třech prvcích od uživatele a přidá nový prvek pomocí metody append() + zobrazí
    # b) odstraní prvek z určeného indexu od uživatele, pomocí metody pop() + zobrazí
    # c) seřadí seznam abecedně pomocí metody sort() + zobrazí
print("9:")
# a) Vytvoření seznamu a přidání nového prvku
a = input("Prvek 1: ")
b = input("Prvek 2: ")
c = input("Prvek 3: ")

my_list = [a, b, c]
d = input("Prvek 4: ")
my_list.append(d)

# b) Odstranění prvku na zvoleném indexu
delete = int(input("Ktery z techto 4 prvku chcete odstranit? "))
if 1 <= delete <= 4:  
    my_list.pop(delete - 1)  
else:
    print("Neplatný výběr, zadejte číslo od 1 do 4.")

print(my_list)


# c) Seřazení seznamu
my_list.sort()
print(my_list)

##############################################################
# 10. Úkol: Vytvoření tuple a indexování
# Napište kód, který:
    # a) vytvoří tuple my_tuple se třemi prvky na základě vstupu od uživatele
    # b) vypíše první prvek tohoto tuple
    # c) vypíše poslední prvek tohoto tuple
print("10:")
# a) Vytvoření tuple
a = input("Prvek 1:")
b = input("Prvek 2:")
c = input("Prvek 3:")
my_tuple = (a, b, c)

# b) První prvek
print(my_tuple[0])

# c) Poslední prvek

print(my_tuple[2])

##############################################################
# 11. Úkol: Základní metody pro tuple
# Napište kód, který:
    # a) vytvoří tuple my_tuple, který bude obsahovat následující prvky: 1, 2, 3, 2, 4, 2, 5
    #    a spočítá počet výskytů uživatelem zadaného prvku pomocí metody count()
    # b) zjistí index uživatelem zadaného prvku element_to_find v tuplu my_tuple pomocí metody index()
print("11:")
# a) Vytvoření tuple a použití metody count()
my_tuple = (1, 2, 3, 2, 4, 2, 5)
print(my_tuple)
user_input = int(input("Zadejte číslo, o kterém se chcete dozvědět, kolikrát se v seznamu na předešlém řádku vyskytuje: "))
print(f"V seznamu se číslo vyskytuje tolikrát: {my_tuple.count(user_input)}")
# b) Použití metody index()

element_to_find = int(input("U kterého z čísel by vás zajímalo pořadí, které v seznamu zaujímá? "))
if 1 <= element_to_find <=5:
    output = my_tuple.index(element_to_find)
    print(f"Vámi zvolené číslo v seznamu zaujímá {output + 1}. pozici.")
else:
    print("Vámi zvolené číslo se v seznamu nevyskytuje.")


##############################################################
# 12. Úkol: Neměnnost tuple
# Napište kód, který:
    # a) vytvoří tuple a pokusí se změnit jeden z jeho prvků (tím demonstruje chybu)
    # b) dokáže zachytit tuto chybu a informovat uživatele o chybě
print("12:")
# a) Vytvoření tuple
my_tuple = (1, 2, 3, 4, 5, 6, 7, 7, 4, 3, 1, 2, 3)
print(my_tuple)
# b) Pokus o změnu prvku
try:
    my_tuple[1] = 99  
except TypeError as error:
    print(f"Error: {error}")
    print("Tuple proměnné nejsou po jejich vytvoření možné změnit. ")

##############################################################

## NEZAPOMEŇTE ZMĚNIT JMÉNO SOUBORU! ##