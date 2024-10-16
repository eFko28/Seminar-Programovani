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
import random
import datetime

# Vymazání obrazovky terminálu (Windows)
os.system("cls")


##############################################################
### Základní verze - vždy stejná odpověď

#ziskani inputu
jmeno = input("Jméno uživatele: ")
prijmeni = input("Příjmení uživatele: ")           

#prvni verze
print("Základní verze bez obměny pozdravu:")
vystup = ("Ahoj " + jmeno.title() + " " + prijmeni.title() + "! Jak se dnes máš?")
print(vystup)
print("----------")


##############################################################
### Rozšířená verze - pseudonáhodný výběr bez zamíchání

print("Rozšířená verze - pseudonáhodný výběr bez zamíchání:")

#vytvoreni promenne s listem pozdravu
pozdravy = [
    f"Ahoj {jmeno.title()} {prijmeni.title()}! Jak se dnes máš?",
    f"Ahojky! Jak se dnes {jmeno.title()} {prijmeni.title()} má?",
    f"{jmeno.title()} {prijmeni.title()}! Těší mně!",
    f"Přeji hezký den {jmeno.title()} {prijmeni.title()}",
    f"Ahoj {prijmeni.title()}, jsi dnes {prijmeni.title()}",
]

#vyber nahodneho pozdravu do promenne random_greeting
random_greeting = random.choice(pozdravy)
print(random_greeting)

print("----------")

##############################################################
### Rozšířená verze - random seed()

# zamíchání, někdy se také používá s knihovnou time: inicializace seed pomocí time: random.seed(time.time())
# side effect provedení v této části kódu má za následek i zamíchání volby při opětovném volání


print("Rozšířená verze - random seed()")

#vytvoreni seedu
random.seed(50)

#promenna pro nahodny pozdrav se seedem
random_greeting_with_seed = random.choice(pozdravy)


print(random_greeting_with_seed)
print("----------")


##############################################################
### *verze - pozdrav podle denní doby

print("Verze - pozdrav podle denní doby")

#ziskani casu, vytvoreni promenne s presnosti na minuty
current_daytime = datetime.datetime.now()
minutes = current_daytime.hour * 60 + current_daytime.minute


#podminky pro output 
if 0 <= minutes < 360:
    output_time = "Tak brzo? Makej ještě spát!"
elif 360 <= minutes < 690:
    output_time = "Dobré ráno! Co budeš dneska programovat?"
elif 690 <= minutes < 810:
    output_time = "Už jsi byl na oběd? Nezapomínej, že musíš krom programování i jíst!"
elif 810 <= minutes < 1260:
    output_time = "Myslím, že by jsi měl ještě něco naprogramovat..."
else:
    output_time = "Padej spát! Ať máš zítra sílu na programování!"


print(output_time)
print("----------")
