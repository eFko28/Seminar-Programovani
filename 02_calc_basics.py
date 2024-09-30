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

##############################################################
### Jednoduchá verze bez kontroly


print("Jednoduchá verze bez kontroly")
# Získání dvou čísel od uživatele
cislo1 = float(input("Zadejte první číslo: "))
cislo2 = float(input("Zadejte druhé číslo: "))

# Provedení aritmetických operací
soucet = cislo1 + cislo2
rozdil = cislo1 - cislo2
soucin = cislo1 * cislo2
podil = cislo1 / cislo2

# Zobrazení výsledků
print(f"Sčítání: {cislo1} + {cislo2} = {soucet}")
print(f"Odčítání: {cislo1} - {cislo2} = {rozdil}")
print(f"Násobení: {cislo1} * {cislo2} = {soucin}")
print(f"Dělení: {cislo1} / {cislo2} = {podil}")
print("-----------------------")


##############################################################
### Rozšířená verze - dělení nulou (ZeroDivisionError: float division by zero)


print("\nRozšířená verze - kontrola dělení nulou:")
# Získání dvou čísel od uživatele
cislo1 = float(input("Zadejte první číslo: "))
cislo2 = float(input("Zadejte druhé číslo: "))

# Provedení aritmetických operací
soucet = cislo1 + cislo2
rozdil = cislo1 - cislo2
soucin = cislo1 * cislo2

# Kontrola, zda se nedělí nulou
if cislo2 != 0:
    podil = cislo1 / cislo2
else:
    podil = " nedefinováno (dělení nulou)"

# Zobrazení výsledků
print(f"Sčítání: {cislo1} + {cislo2} = {soucet}")
print(f"Odčítání: {cislo1} - {cislo2} = {rozdil}")
print(f"Násobení: {cislo1} * {cislo2} = {soucin}")
print(f"Dělení: {cislo1} / {cislo2} = {podil}")
print("-----------------------")



##############################################################
### * verze - ověření číselného vstupu od uživatele


# Získání dvou čísel od uživatele
print("\nRozšířená verze - kontrola dělení nulo, kontrola číselného vstupu:")
while True:
    try:
        cislo1 = float(input("Zadejte první číslo: "))
        cislo2 = float(input("Zadejte druhé číslo: "))
        break
    except ValueError:
        print("\nNeplatný vstup. Zadejte hodnoty, prosím, znovu.\n\n")

# Provedení aritmetických operací
soucet = cislo1 + cislo2
rozdil = cislo1 - cislo2
soucin = cislo1 * cislo2

# Kontrola, zda se nedělí nulou
if cislo2 != 0:
    podil = cislo1 / cislo2
else:
    podil = " nedefinováno (dělení nulou)"

# Zobrazení výsledků
print(f"Sčítání: {cislo1} + {cislo2} = {soucet}")
print(f"Odčítání: {cislo1} - {cislo2} = {rozdil}")
print(f"Násobení: {cislo1} * {cislo2} = {soucin}")
print(f"Dělení: {cislo1} / {cislo2} = {podil}")
print("-----------------------")


##############################################################
### ** verze - uložení do csv


print("\nRozšířená verze - uložení do csv calc_basics_vysledky.csv:")

# Získání dvou čísel od uživatele
while True:
    try:
        cislo1 = float(input("Zadejte první číslo: "))
        cislo2 = float(input("Zadejte druhé číslo: "))
        break
    except ValueError:
        print("\nNeplatný vstup. Zadejte hodnoty, prosím, znovu.\n\n")

# Provedení aritmetických operací
soucet = cislo1 + cislo2
rozdil = cislo1 - cislo2
soucin = cislo1 * cislo2

# Kontrola, zda se nedělí nulou
if cislo2 != 0:
    podil = cislo1 / cislo2
else:
    podil = " nedefinováno (dělení nulou)"

# Získání výsledků jako seznam
vysledky = [
    f"Sčítání: {cislo1} + {cislo2} = {soucet}",
    f"Odčítání: {cislo1} - {cislo2} = {rozdil}",
    f"Násobení: {cislo1} * {cislo2} = {soucin}",
    f"Dělení: {cislo1} / {cislo2} = {podil}"
]

# Uložení výsledků do CSV souboru - vždy jako nový soubor, smaže a zapíš
with open('calc_basics_vysledky.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Operace", "Výsledek"])
    for vysledek in vysledky:
        writer.writerow([vysledek.split(':')[0], vysledek.split('=')[1].strip()])


# Čtení CSV souboru
with open('calc_basics_vysledky.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    
    # Zobrazení dat
    print("Operace a jejich výsledky - načteno z csv souboru:")
    for radek in reader:
        operace = radek['Operace']
        vysledek = radek['Výsledek']
        print(f"{operace}: {vysledek}")


##############################################################
### *** verze s GUI - tkinter s výběrem operace
### !!! je potřeba zakomentovat předcházející kód

print("\nRozšířená verze - grafické rozhraní - otevřelo se okno!")

def vypocitat():
    """Zpracování 2 čísel a operace ze vstupu - kalkulačka, voláno objektem button

    Pro 2 vstupní čísla ("entry_cislo1", "entry_cislo2") provede zvolenou operaci, vrací "vysledek"
    
    Args:
        entry_cislo1: Nevstupují jako parametr, ale musí být definovány dříve
        entry_cislo1: Nevstupují jako parametr, ale musí být definovány dříve

    Returns:
        Vrací "vysledek" jako float, který zobrazí v messageboxu
    """

    try:
        cislo1 = float(entry_cislo1.get())
        cislo2 = float(entry_cislo2.get())
        operace = var_operace.get()

        if operace == '+':
            vysledek = cislo1 + cislo2
        elif operace == '-':
            vysledek = cislo1 - cislo2
        elif operace == '*':
            vysledek = cislo1 * cislo2
        elif operace == '/':
            if cislo2 != 0:
                vysledek = cislo1 / cislo2
            else:
                messagebox.showerror("Chyba", "Dělení nulou není povoleno")
                return
        else:
            messagebox.showerror("Chyba", "Neplatná operace")
            return

        messagebox.showinfo("Výsledek", f"Výsledek {operace} je: {vysledek}")
    except ValueError:
        messagebox.showerror("Chyba", "Zadejte platná čísla")

# Nastavení GUI
root = tk.Tk()
root.title("Kalkulačka")

tk.Label(root, text="První číslo:").pack()
entry_cislo1 = tk.Entry(root)
entry_cislo1.pack()

tk.Label(root, text="Druhé číslo:").pack()
entry_cislo2 = tk.Entry(root)
entry_cislo2.pack()

var_operace = tk.StringVar(value='+')
tk.Label(root, text="Vyberte operaci:").pack()
tk.Radiobutton(root, text="+", variable=var_operace, value='+').pack()
tk.Radiobutton(root, text="-", variable=var_operace, value='-').pack()
tk.Radiobutton(root, text="*", variable=var_operace, value='*').pack()
tk.Radiobutton(root, text="/", variable=var_operace, value='/').pack()

# volání funkce vypocitat()
tk.Button(root, text="Vypočítat", command=vypocitat).pack()

root.mainloop()
