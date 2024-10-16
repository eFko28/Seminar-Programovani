# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
03) geometric_object_basics.py

Obvod a obsah trojúhelníku - na vstupu budou délky 3 stran
* Doplňte o podmínky řešitelnosti - vstupní hodnoty (využij definici funkce), trojúhelníková nerovnost
* Podle délek stran urči, zda se jedná o některý ze speciálních případů trojúhelníku.
* Dopočítejte úhly v trojúhelníku, upřesněte popis trojúhelníku i podle vypočítaných úhlů.
* Doplňte poloměr kružnice vepsané i opsané.
** Vytvoř "menu" pro volbu úkolu nebo objektu - jde spíše o princip tvorby volby
** Vykresli trojúhelník.
+ Jak by se daná úloha dala rozšířit na další obrazce? Zamysli se na vhodností, efektivitou, smyslem....
"""


import math
import os

##############################################################
### Jak vymazat terminál před opětovným spuštěním - cls pro Win, clear pro Unix-like systémy
os.system("cls")


##############################################################
### Základní verze - obvod a obsah trojúhelníku

print("Ver: basic")

print("Hey! Lets calculate the circumference and the area of a triangle!")
while True:
    try:
        a = float(input("What should be the length of the first side?"))
        b = float(input("And what about the second?"))
        c= float(input("The third and last one?"))
        break
    except ValueError:
        print("Non-numerical input. Try again.")


circumference = a + b + c
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))



print(f"The cicumference of your triangle is {circumference} and the area should be {area}")






##############################################################
### Verze s ověřením vstupu - obvod a obsah trojúhelníku
### + nově definice funkce

print("Ver: is valid?")
a = float(input("What should be the length of the first side?"))
b = float(input("And what about the second?"))
c= float(input("The third and last one?"))

def is_valid_triangle(a, b, c) -> bool:
    if a + b <= c:
        return False
    elif a + c <= b:
        return False
    elif b + c <= a:
        return False

    return True

is_valid = is_valid_triangle(a, b, c)
if (is_valid is not True):
    print("Yoh have inputed non-defined side lengths.")
else:
    circumference = a + b + c
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"The cicumference of your triangle is {circumference} and the area should be {area}")

##############################################################
### Verze doplněná o klasifikaci trojúhelníku podle délek stran, podle úhlů, poloměry
print("Ver: type?")
a = float(input("What should be the length of the first side?"))
b = float(input("And what about the second?"))
c= float(input("The third and last one?"))

def is_valid_triangle(a, b, c) -> bool:
    if a + b <= c:
        return False
    elif a + c <= b:
        return False
    elif b + c <= a:
        return False
    return True

is_valid = is_valid_triangle(a, b, c)
if (is_valid is not True):
    print("Yoh have inputed non-defined side lengths.")
else:
    circumference = a + b + c
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"The cicumference of your triangle is {circumference} and the area should be {area}")


def triangle_type_by_sides(a, b, c) -> str:
    if a == b == c:
        return "Equilateral"
    elif a == b:
        return "Isosceles"
    elif a == c:
        return "Isosceles"
    elif c == b:
        return "Isosceles"
    else:
        return "Scalene"



def triangle_type_by_angle(a, b, c) -> str:
    if  a == 90 or b == 90 or c == 90:
        return "Right-angled"
    elif a > 90 or b > 90 or c > 90:
        return "Obtuse-angled"
    else:
        return "Acute-angled"
    
A_angle = math.acos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * b * c))
B_angle = math.acos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * a * c))
C_angle = math.acos(((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b))


type_side = triangle_type_by_sides(a, b, c)
type_angle = triangle_type_by_angle(A_angle, B_angle, C_angle)

print(f"The triangle was also {type_side} and {type_angle}")



##############################################################
### Verze s vykreslením, už nic nepočítám - výpočty viz předchozí

# je potřeba rozšíření: python extension pack
# !!! provést instalaci matplotlib příkazem v terminálu: pip install matplotlib




##############################################################
### Verze s jednoduchým menu - jednotlivé definice, bez hlubší kontroly (viz výše)

