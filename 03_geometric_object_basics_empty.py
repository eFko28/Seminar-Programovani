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


print("Hey! Lets calculate the circumference and the are of a triangle!")
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


##############################################################
### Verze doplněná o klasifikaci trojúhelníku podle délek stran, podle úhlů, poloměry


##############################################################
### Verze s vykreslením, už nic nepočítám - výpočty viz předchozí

# je potřeba rozšíření: python extension pack
# !!! provést instalaci matplotlib příkazem v terminálu: pip install matplotlib




##############################################################
### Verze s jednoduchým menu - jednotlivé definice, bez hlubší kontroly (viz výše)

