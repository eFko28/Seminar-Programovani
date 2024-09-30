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


# Získání vstupu od uživatele
print("ZÁKLADNÍ VERZE: Zadejte délky stran trojúhelníku:")
strana1 = float(input("Délka první strany: "))
strana2 = float(input("Délka druhé strany: "))
strana3 = float(input("Délka třetí strany: "))

# Výpočet obvodu
obvod = strana1 + strana2 + strana3

# Použití Heronova vzorce pro výpočet obsahu
s = (strana1 + strana2 + strana3) / 2
obsah = math.sqrt(s * (s - strana1) * (s - strana2) * (s - strana3))

# Zobrazení výsledků
print(f"Obvod trojúhelníku: {obvod:.2f}")
print(f"Obsah trojúhelníku: {obsah:.2f}")


##############################################################
### Verze s ověřením vstupu - obvod a obsah trojúhelníku
### + nově definice funkce


# Funkce pro ověření, že vstup je kladné číslo
def zadej_kladnou_stranu(cislo_strany):
    """Zadání délky strany včetně ošetření vstupu

    Input pro načtení čísla, ověření číselné hodnoty a smyslu - musí být větší než 0

    Returns:
        Vrací "hodnota" jako float
    """

    while True:
        try:
            hodnota = float(input(f"Délka {cislo_strany} strany: "))
            if hodnota > 0:
                return hodnota
            else:
                print("\nHodnota musí být kladné číslo větší než 0.")
        except ValueError:
            print("Neplatný vstup. Zadejte prosím číslo.\n")


# Získání vstupu od uživatele
print("VERZE S OVĚŘENÍM VSTUPŮ: Zadejte délky stran trojúhelníku:")
strana1 = zadej_kladnou_stranu("první")
strana2 = zadej_kladnou_stranu("druhé")
strana3 = zadej_kladnou_stranu("třetí")

# Ověření trojúhelníkové nerovnosti
if (
    (strana1 + strana2 > strana3)
    and (strana1 + strana3 > strana2)
    and (strana2 + strana3 > strana1)
):
    # OBVOD:
    obvod = strana1 + strana2 + strana3

    # OBSAH:
    s = obvod / 2
    obsah = math.sqrt(s * (s - strana1) * (s - strana2) * (s - strana3))

    # Zobrazení výsledků
    print(f"Obvod trojúhelníku: {obvod:.2f}")
    print(f"Obsah trojúhelníku: {obsah:.2f}")
else:
    print(
        "Zadané délky stran nesplňují podmínku trojúhelníkové nerovnosti a nelze z nich sestrojit trojúhelník."
    )


##############################################################
### Verze doplněná o klasifikaci trojúhelníku podle délek stran, podle úhlů, poloměry


# Funkce pro ověření, že vstup je kladné číslo
def zadej_kladnou_stranu(cislo_strany):
    """Zadání délky strany včetně ošetření vstupu

    Input pro načtení čísla, ověření číselné hodnoty a smyslu - musí být větší než 0

    Returns:
        Vrací "hodnota" jako float
    """

    while True:
        try:
            hodnota = float(input(f"Délka {cislo_strany} strany: "))
            if hodnota > 0:
                return hodnota
            else:
                print("\nHodnota musí být kladné číslo větší než 0.")
        except ValueError:
            print("Neplatný vstup. Zadejte prosím číslo.\n")


# Získání vstupu od uživatele
print(
    "VERZE S OVĚŘENÍM A KLASIFIKACÍ TROJÚHELNÍKU: Zadejte délky stran trojúhelníku:\n"
)
strana1 = zadej_kladnou_stranu("první")
strana2 = zadej_kladnou_stranu("druhé")
strana3 = zadej_kladnou_stranu("třetí")

# Ověření trojúhelníkové nerovnosti
if (
    (strana1 + strana2 > strana3)
    and (strana1 + strana3 > strana2)
    and (strana2 + strana3 > strana1)
):
    # OBVOD:
    obvod = strana1 + strana2 + strana3
    print(f"-----------------\nObvod trojúhelníku: {obvod:.2f}")

    # OBSAH:
    s = obvod / 2
    obsah = math.sqrt(s * (s - strana1) * (s - strana2) * (s - strana3))
    print(f"Obsah trojúhelníku: {obsah:.2f}")

    # KLASIFIKACE - podle DÉLKY STRAN:
    if strana1 == strana2 == strana3:
        print("Trojúhelník je rovnostranný.")
    elif strana1 == strana2 or strana1 == strana3 or strana2 == strana3:
        print("Trojúhelník je rovnoramenný.")
    else:
        print("Trojúhelník je různoramenný.")

    # ÚHLY (pomocí kosinové věty):
    uhel1 = math.degrees(
        math.acos((strana2**2 + strana3**2 - strana1**2) / (2 * strana2 * strana3))
    )
    uhel2 = math.degrees(
        math.acos((strana1**2 + strana3**2 - strana2**2) / (2 * strana1 * strana3))
    )
    uhel3 = 180 - uhel1 - uhel2  # Součet vnitřních úhlů je 180 stupňů
    print(f"Úhly trojúhelníku: {uhel1:.2f}°, {uhel2:.2f}°, {uhel3:.2f}°")

    # KLASIFIKACE - podle VELIKOSTI ÚHLŮ:
    if uhel1 == 90 or uhel2 == 90 or uhel3 == 90:
        print("Trojúhelník je pravoúhlý.")
    elif uhel1 > 90 or uhel2 > 90 or uhel3 > 90:
        print("Trojúhelník je tupoúhlý.")
    else:
        print("Trojúhelník je ostroúhlý.")

    # POLOMĚR - opsané:
    polomer_opsane_kruznice = (strana1 * strana2 * strana3) / (4 * obsah)
    print(f"Poloměr opsané kružnice: {polomer_opsane_kruznice:.2f}")

    # POLOMĚR - vepsané:
    polomer_vepsane_kruznice = obsah / s
    print(f"Poloměr vepsané kružnice: {polomer_vepsane_kruznice:.2f}")

else:
    print(
        "Zadané délky stran nesplňují podmínku trojúhelníkové nerovnosti a nelze z nich sestrojit trojúhelník."
    )

print("-----------------\n")


##############################################################
### Verze s vykreslením, už nic nepočítám - výpočty viz předchozí

# je potřeba rozšíření: python extension pack
# !!! provést instalaci matplotlib příkazem v terminálu: pip install matplotlib


import matplotlib.pyplot as plt


# Funkce pro ověření, že vstup je kladné číslo
def zadej_kladnou_stranu(cislo_strany):
    """Zadání délky strany včetně ošetření vstupu

    Input pro načtení čísla, ověření číselné hodnoty a smyslu - musí být větší než 0

    Returns:
        Vrací "hodnota" jako float
    """

    while True:
        try:
            hodnota = float(input(f"Délka {cislo_strany} strany: "))
            if hodnota > 0:
                return hodnota
            else:
                print("\nHodnota musí být kladné číslo větší než 0.")
        except ValueError:
            print("Neplatný vstup. Zadejte prosím číslo.\n")


# Získání vstupu od uživatele
print("VERZE S VYKRESLENÍM A OVĚŘENÍM VSTUPU: Zadejte délky stran trojúhelníku:\n")
strana1 = zadej_kladnou_stranu("první")
strana2 = zadej_kladnou_stranu("druhé")
strana3 = zadej_kladnou_stranu("třetí")

# Ověření trojúhelníkové nerovnosti
if (
    (strana1 + strana2 > strana3)
    and (strana1 + strana3 > strana2)
    and (strana2 + strana3 > strana1)
):
    # Souřadnice prvního bodu (0,0)
    x1, y1 = 0, 0

    # Souřadnice druhého bodu (a,0) - bod leží na ose x
    x2, y2 = strana1, 0

    # Souřadnice třetího bodu (x3, y3) - používáme kosinovou větu
    # Kosinová věta: cos(γ) = (a^2 + b^2 - c^2) / (2ab)
    cos_gamma = (strana1**2 + strana2**2 - strana3**2) / (2 * strana1 * strana2)
    gamma = math.acos(cos_gamma)  # úhel γ

    # Souřadnice třetího bodu (x3, y3)
    x3 = strana2 * math.cos(gamma)
    y3 = strana2 * math.sin(gamma)

    # Vykreslení trojúhelníku
    plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], marker="o")

    # Vyplnění trojúhelníku barvou
    plt.fill([x1, x2, x3], [y1, y2, y3], "b", alpha=0.3)

    # Nastavení poměru osy x a y na stejnou měřítko
    plt.gca().set_aspect("equal", adjustable="box")

    # Zobrazení grafu
    plt.title("Trojúhelník")
    plt.show()


##############################################################
### Verze s jednoduchým menu - jednotlivé definice, bez hlubší kontroly (viz výše)


def spocitat_ctverec():
    """Obvod a obsah čtverce

    Input pro načtení délky strany čtverce, BEZ OVĚŘENÍ VSTUPU

    Returns:
        Vrací "obsah" a "obvod" jako float
    """

    strana = float(input("Zadejte délku strany čtverce: "))
    obsah = strana**2
    obvod = 4 * strana
    return obsah, obvod


def spocitat_obdelnik():
    """Obvod a obsah obdélníku

    Input pro načtení délky a šířky obdélníku, BEZ OVĚŘENÍ VSTUPU

    Returns:
        Vrací "obsah" a "obvod" jako float
    """

    delka = float(input("Zadejte délku obdélníku: "))
    sirka = float(input("Zadejte šířku obdélníku: "))
    obsah = delka * sirka
    obvod = 2 * (delka + sirka)
    return obsah, obvod


def spocitat_trojuhelnik():
    """Obvod a obsah trojúhelníku

    Input pro načtení 3 stran trojúhelníku, Heronův vzorec pro obsah, BEZ OVĚŘENÍ VSTUPU

    Returns:
        Vrací "obsah" a "obvod" jako float
    """

    strana1 = float(input("Zadejte délku první strany trojúhelníku: "))
    strana2 = float(input("Zadejte délku druhé strany trojúhelníku: "))
    strana3 = float(input("Zadejte délku třetí strany trojúhelníku: "))
    # Použití Heronova vzorce pro výpočet obsahu
    s = (strana1 + strana2 + strana3) / 2
    obsah = math.sqrt(s * (s - strana1) * (s - strana2) * (s - strana3))
    obvod = strana1 + strana2 + strana3
    return obsah, obvod


def spocitat_kosoctverec():
    """Obvod a obsah kosočtverce

    Input pro načtení strany a 2 úhlopříček, BEZ OVĚŘENÍ VSTUPU

    Returns:
        Vrací "obsah" a "obvod" jako float
    """

    strana = float(input("Zadejte délku strany kosočtverce: "))
    uhlopricka1 = float(input("Zadejte délku první úhlopříčky: "))
    uhlopricka2 = float(input("Zadejte délku druhé úhlopříčky: "))
    obsah = (uhlopricka1 * uhlopricka2) / 2
    obvod = 4 * strana
    return obsah, obvod


def spocitat_kruh():
    """Obvod a obsah kruhu

    Input pro načtení poloměru, BEZ OVĚŘENÍ VSTUPU

    Returns:
        Vrací "obsah" a "obvod" jako float
    """

    polomer = float(input("Zadejte poloměr kruhu: "))
    obsah = math.pi * polomer**2
    obvod = 2 * math.pi * polomer
    return obsah, obvod


# Výběr tvaru
print("VERZE S VÝBĚREM OBJEKTU: Vyberte tvar (zadejte číslo):")
print("1 - Čtverec")
print("2 - Obdélník")
print("3 - Trojúhelník")
print("4 - Kosočtverec")
print("5 - Kruh")

volba = input("Vaše volba: ")

if volba == "1":
    obsah, obvod = spocitat_ctverec()
    tvar = "Čtverec"
elif volba == "2":
    obsah, obvod = spocitat_obdelnik()
    tvar = "Obdélník"
elif volba == "3":
    obsah, obvod = spocitat_trojuhelnik()
    tvar = "Trojúhelník"
elif volba == "4":
    obsah, obvod = spocitat_kosoctverec()
    tvar = "Kosočtverec"
elif volba == "5":
    obsah, obvod = spocitat_kruh()
    tvar = "Kruh"
else:
    print("Neplatná volba.")
    obsah, obvod = None, None
    tvar = None

if tvar:
    print(f"\n---------------\n{tvar} - výsledky:")
    print(f"Obsah: {obsah:.2f}")
    print(f"Obvod: {obvod:.2f}\n---------------\n")
