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

# Získání jména a příjmení od uživatele
jmeno = input("Zadejte své jméno: ")
prijmeni = input("Zadejte své příjmení: ")

# Generování pozdravu bez náhodného prvku
pozdrav = f"Ahoj, {jmeno} {prijmeni}! Těší mě, že tě poznávám."

# Zobrazení pozdravu
print("\nZákladní verze - vždy stejná odpověď:")
print(pozdrav)
print("-----------------------")


##############################################################
### Rozšířená verze - pseudonáhodný výběr bez zamíchání

import random

print("\nRozšířená verze - pseudonáhodný výběr bez zamíchání:")
# Definování různých možností pozdravu
pozdravy = [
    f"01 Ahoj, {jmeno} {prijmeni}! Těší mě, že tě poznávám.",
    f"02 Ahoj {jmeno}! Jak se máš, {prijmeni}?",
    f"03 Zdravím tě, {jmeno} {prijmeni}! Doufám, že máš skvělý den.",
    f"04 Tě pic {prijmeni}! Jde to, {jmeno}?",
    f"05 Čúúúz, bambus, {jmeno}! Máš se, {prijmeni}?",
    f"06 Hola hoj {jmeno}! Jsem rád, že tě znám, {prijmeni}?",
]

# Výběr náhodného pozdravu
vybrany_pozdrav = random.choice(pozdravy)

# Zobrazení pozdravu
print(vybrany_pozdrav)
print("-----------------------")


##############################################################
### Rozšířená verze - random seed()

# zamíchání, někdy se také používá s knihovnou time: inicializace seed pomocí time: random.seed(time.time())
# side effect provedení v této části kódu má za následek i zamíchání volby při opětovném volání

random.seed()

# Výběr náhodného pozdravu
vybrany_pozdrav_seed = random.choice(pozdravy)

# Zobrazení pozdravu
print("\nRozšířená verze se zamícháním:")
print(vybrany_pozdrav_seed)
print("-----------------------")


##############################################################
### *verze - pozdrav podle denní doby

import datetime

# Získání aktuálního času
aktualni_cas = datetime.datetime.now()
hodina = aktualni_cas.hour

# Definování pozdravu podle denní doby
if 5 <= hodina < 11:
    pozdrav_dle_casu = f"Dobré ráno, {jmeno} {prijmeni}! Ať se ti daří na prográmku! Je asik {hodina} hodin."
elif 11 <= hodina < 17:
    pozdrav_dle_casu = f"Krásný den přeji, {jmeno} {prijmeni}! Dnes bude sluníčko svítit jako o prázdninách. Je asik {hodina} hodin."
else:
    pozdrav_dle_casu = f"Pěkný večer nebo noc, {jmeno} {prijmeni}! Raději už odpočívej. Je asik {hodina} hodin."

# Zobrazení pozdravu
print("\nVerze dle denní doby:")
print(pozdrav_dle_casu)
print("-----------------------")
