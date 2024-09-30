# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
01) greetings_basics.py

Na inputu jméno, příjmení. Na výstupu jeden ze 3 možných pozdravů včetně vstupních informací.
* jak vyčistit terminál
* jak skutečně zajistit náhodnost
* pozdrav podle denní doby
"""

##############################################################
### Jak vymazat terminál před opětovným spuštěním - cls pro Win, clear pro Unix-like systémy

import os

# Vymazání obrazovky terminálu (Windows)
os.system("cls")


##############################################################
### Základní verze - vždy stejná odpověď

jmeno = input("Jméno uživatele: ")
prijmeni = input("Příjmení uživatele: ")

vystup = ("Ahoj " + jmeno + " " + prijmeni + "! Jak se dnes máš?")

print("Základní verze bez obměny pozdravu")
print(vystup)
print("________________")


##############################################################
### Rozšířená verze - pseudonáhodný výběr bez zamíchání

print("Rozšířená verze - pseudonáhodný výběr bez zamíchání")
























##############################################################
### Rozšířená verze - random seed()

# zamíchání, někdy se také používá s knihovnou time: inicializace seed pomocí time: random.seed(time.time())
# side effect provedení v této části kódu má za následek i zamíchání volby při opětovném volání
























##############################################################
### *verze - pozdrav podle denní doby























