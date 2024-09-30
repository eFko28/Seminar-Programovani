# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
02) calc_basics.py

Vyžádej si na vstupu 2 čísla, proveď s nima základní operace, na výstupu vždy zobraz operaci a výsledek.
* ošetři dělení nulou
* ošetři číselný vstup
** ukládání výstupů do souboru
*** GUI tkinter
"""

# import knihoven je zvykem definovat na začátku
import os
import csv

import tkinter as tk
from tkinter import messagebox


os.system('cls')
"""
##############################################################
### Jednoduchá verze bez kontroly
print("Jednoduchá verze bez kontroly")
print("----------")

print("Ahoj! Vítám tě ve své kalkulačce.")
input1 = float(input("Zadej první číslo:"))
input2 = float(input("Zadej druhé číslo:"))

soucet = input1 + input2
rozdil = input1 - input2
soucin = input1 * input2
podil = input1 / input2

print("Výsledky:")
print(f"Součet: {soucet}")
print(f"Rozdíl: {rozdil}")
print(f"Součin: {soucin}")
print(f"Podíl: {podil}")

print("----------")

##############################################################
### Rozšířená verze - dělení nulou (ZeroDivisionError: float division by zero)

print("Rozšířená verze - dělění nulou")
print("----------")

print("Ahoj! Vítám tě ve své kalkulačce.")
input1 = float(input("Zadej první číslo:"))
input2 = float(input("Zadej druhé číslo:"))

soucet = input1 + input2
rozdil = input1 - input2
soucin = input1 * input2
if input2 != 0:
    podil = input1 / input2
else:
    podil = "Nedefinovaná operace(dělění nulou)."


print("Výsledky:")
print(f"Součet: {soucet}")
print(f"Rozdíl: {rozdil}")
print(f"Součin: {soucin}")
print(f"Podíl: {podil}")

print("----------")


##############################################################
### * verze - ověření číselného vstupu od uživatele


print("Verze s ošetřením vstupu")
print("----------")

print("Ahoj! Vítám tě ve své kalkulačce.")
while True:
    try:

        input1 = float(input("Zadej první číslo:"))
        input2 = float(input("Zadej druhé číslo:"))
        break
    except ValueError:
        print("Vstup není číselný, prosím znovu.")



soucet = input1 + input2
rozdil = input1 - input2
soucin = input1 * input2
if input2 != 0:
    podil = input1 / input2
else:
    podil = "Nedefinovaná operace(dělění nulou)."


print("Výsledky:")
print(f"Součet: {soucet}")
print(f"Rozdíl: {rozdil}")
print(f"Součin: {soucin}")
print(f"Podíl: {podil}")

print("----------")

##############################################################
### ** verze - uložení do csv

"""
print("Verze - uložení do csv")
print("----------")

print("Ahoj! Vítám tě ve své kalkulačce.")
while True:
    try:

        input1 = float(input("Zadej první číslo:"))
        input2 = float(input("Zadej druhé číslo:"))
        break
    except ValueError:
        print("Vstup není číselný, prosím znovu.")



soucet = input1 + input2
rozdil = input1 - input2
soucin = input1 * input2
if input2 != 0:
    podil = input1 / input2
else:
    podil = "Nedefinovaná operace(dělění nulou)."



vysledky = [
    f"Sčítaní: {soucet}"
    f"Odčítání: {rozdil}"
    f"Násobení: {soucin}"
    f"Dělení: {podil}"
]



with open('calc_basics_vysledky.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Operace", "Výsledek"])
    for vysledek in vysledky:
        writer.writerow(vysledek)



with open('calc_basics_vysledky.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    
 
    print("Operace a jejich výsledky - načteno z csv souboru:")
    for radek in reader:
        operace = radek['Operace']
        vysledek = radek['Výsledek']
        print(f"{operace}: {vysledek}")



##############################################################
### *** verze s GUI - tkinter s výběrem operace
### !!! je potřeba zakomentovat předcházející kód


