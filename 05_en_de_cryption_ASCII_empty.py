# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
05_en_de_cryption_ASCII.py

* Příprava - napište funkci, která zobrazí tabulku ASCII jakkoliv
* Doplňte tabulku o hodnotu znaků BIN, OCT, HEX
* Doplňte možnost omezení od-do
* Napište funkci, která vám dle charu a typu vstupu vrátí hodnotu bin/hex/oct
** Pokuste se zobrazit výstup ve formě tabulky, nejde o ohraničení, ale o strukturu více sloupců
"""

import os
os.system("cls")


##############################################################
### Vypiš ASCII kódy DEC / CHAR od 1 do 127
# funkce ascii_table
def ascii_table():
    print("ASCII PŘEVODNÍK - DEC/CHAR")       #uvod
    print("Dec -- Char")       

    for i in range(1, 128):    #loop, ktery vypise hodnotu char pro i a i jako takove (i = decimal)
        char = chr(i)
        print(f"{i:4}  {char:5}")   #:4 a :5 dela prostor -> zabere tolik mist, pokud ma min, napise se co nejvic v pravo




##############################################################
### Vypiš ASCII kódy - rozšířený výpis, bin/oct/hex doplněný o omezení rozsahu
# funkce ascii_table_with_range:



def ascii_table_with_range(start=32, end=127):
    print("ASCII CONVERTER - DEC/CHAR/BIN/OCT/HEX")
    print(f"Characters from {start} to {end}:")
    print(f"{'Dec':<5}{'Char':<5}{'Bin':<10}{'Oct':<5}{'Hex':<5}")
    
    for i in range(start, end + 1):       #vypise vsechny korespondujici hodnoty pro decimal od 32 do 127
        print(f"{i:<5}{chr(i):<5}{bin(i)[2:]:<10}{oct(i)[2:]:<5}{hex(i)[2:].upper():<5}")




##############################################################
### Preveď znak na ASCII=DEC hodnotu a poté vrať hodnotu znaku v BIN/OCT/HEX podle base
# funkce char_to_base
# využito v main
def ascii_convert_char_to_base(char: str, return_type: str) -> str:
    if len(char) != 1:    #osetreni vstupu na pouze 1-mistny
        raise ValueError()

    numerical_value = ord(char) #prevede jakykoliv vstup na ASCII decimal
    
    if return_type.upper() == "BIN":     #podle usr specifikovaneho return_type vraci hodnoty korespondujici druhum zapisu
        return bin(numerical_value)
    elif return_type.upper() == "OCT":
        return oct(numerical_value)    
    elif return_type.upper() == "HEX":
        return hex(numerical_value)
    
    else:
        raise ValueError("Invalid return type. Use 'oct', 'bin', or 'hex'.")     #ostreni vstupu



##############################################################
### Vypiš ASCII kódy - zformátovaná tabulka, DEC/CHAR/BIN/OCT/HEX = 1 sloupeček
# Možnost zvolit více sloupečků, default 1
# funkce ascii_table_multicolumn

def ascii_table_multicolumn(start: int, end: int, columns: int = 1) -> None:     #definujeme 3 promenne - start, end, columns(pro zatim konstanta)
    if start < 1 or start > 126:   #osetreni vstupu
        raise ValueError("Invalid start value. Must be 1-126.")
    if end < 2 or end > 127:
        raise ValueError("Invalid end value. Must be 2-127.")
    output = []    #vytvoreni listu output
    for i in range(start, end):    #pokud je hodnota 1-32, ulozi char jako "nevytisknutelny charakter"; pokud je 32-127, ulozi char jako korespondujici charakter
        if i >= 32:
            char = chr(i)
        elif i <= 31:
            char = "Non-printable character"
        output.append(f"Char: {char} -- Dec: {i} -- Bin: {bin(i)[2:]} -- Oct: {oct(i)[2:]} -- Hex: {hex(i)[2:]}") #prida k listu spravne hodnoty i-krat

    print(f"{'Char':<5}{'Dec':<5}{'Bin':<5}{'Oct':<5}{'Hex':<5}  " * columns)   #vytiskne columns-krat (zatim 1) zahlavi k outputu
    for i in range(start, end + 1, columns):   #venkovni loop: definuje vychozi bod pro kazdy radek
        for index in range(i, min(i + columns, end + 1)):   #vnitrni loop: vypisuje hodnoty korespondujici s i z venkovniho loopu
            print(f"{chr(index):<5}{index:<5}{bin(index)[2:]:<5}{oct(index)[2:]:<5}{hex(index)[2:].upper():<5}")
    print("\n")    #pokazde napise novy radek - pekny zapis

print("Hey! I will output you an ASCII codes for a specific range of ASCII codes you wish to have output.")   #uziti fce nakonec
start = int(input("Range from: (Decimal input) "))
end = int(input("Range to: (Decimal input) "))
ascii_table_multicolumn(start, end)




##############################################################
### Spuštění programu - MAIN
"""
if __name__ == "__main__":
    os.system("cls")

#    ascii_table()
#    print("------------------------------------------------\n")

    char = "#"
    print(f"Znak '{char}' -> ASCII: ", ord(char))
    print(f"Znak '{char}' -> BIN: ", char_to_base(char, 'bin'))
    print(f"Znak '{char}' -> OCT: ", char_to_base(char, 'oct'))
    print(f"Znak '{char}' -> HEX: ", char_to_base(char, 'hex'))
    print(f"Znak '{char}' -> HIPIIII: ", char_to_base(char, 'hip'))
    print("------------------------------------------------\n")

    ascii_table_multicolumn(35,62,4)
"""