## Knihovny

from time import sleep
from random import choice
from random import shuffle
from colorama import init, Fore, Style
import csv


## Proměnné

barvy_reset = Style.RESET_ALL
azur = Fore.CYAN
grn = Fore.GREEN
red = Fore.RED
ylo = Fore.YELLOW

vychozi_nazev_souboru = "vysledky.csv"
sire_rozhrani = 60

slovnik = {
    "program": "Sada instrukcí, které vykonává počítač.",
    "internet": "Celosvětová síť propojující počítače.",
    "python": "Populární programovací jazyk vhodný i pro začátečníky.",
    "algoritmus": "Postup řešení problému krok za krokem.",
    "data": "Informace uložené v digitální formě.",
    "knihovna": "Soubor funkcí a modulů, které rozšiřují schopnosti jazyka.",
    "cyklus": "Konstrukce umožňující opakované provádění části kódu.",
    "podmínka": "Konstrukce rozhodující, která část kódu se vykoná.",
    "proměnná": "Pojmenovaná oblast paměti pro uchování hodnoty.",
    "funkce": "Znovupoužitelný blok kódu pro konkrétní úkol."
}

jmeno = None
body = 0

## Funkce
init()          # Spuštění coloramy

def zobraz_uvod():
    # Zobrazí úvodní obrazovku.
    pozdrav = "\n" + "VÍTEJ VE HŘE SLOVNÍ DUEL".center(sire_rozhrani) + "\n"
    oddelovac = "-" * sire_rozhrani
    menu = f"""
1. {hry[0]}
2. {hry[1]}
3. {hry[2]}
4. Ukázat leaderboard
5. Ukončit aplikaci
"""
    hlavicka = azur + pozdrav + oddelovac + menu + oddelovac + barvy_reset
    print(hlavicka)

def ziskej_volbu():
    # Zjišťuje, jakou hru chce uživatel hrát.
    vyzva_uvod = azur + """Zadej styl hry (1 - 3), mrkni na tabulku vítězů (4),
nebo ukonči aplikaci (5), a potvrď klávesou Enter: """ + barvy_reset
    volba = input(vyzva_uvod)
    while volba not in pripustne_volby:         # Kontrola vstupu
        volba = input(red + "chybný vstup. ".upper() + azur + vyzva_uvod + barvy_reset)
    return volba

def specifikuj_hru(i, j):
    # Napíše, jakou hru si uživatel vybral a něco k ní. Vyžaduje 2x int (volbu a počet pokusů).
    hra = hry[i-1]
    pokusy = j
    uvod_hra = azur + f"Zvolil jsi hru {hra}. Myslím si slovo.\nUhodni ho. Zmýlit se můžeš maximálně {pokusy-1}krát.\nU hry č. 1 zadávej písmenka, u zbylých celá slova.\n" + barvy_reset
    print(uvod_hra)

def ziskej_pismena(pokusy, body):
    # Hra 1, uživatel zadává písmena. Vyžaduje 2x int (počet pokusů a počet bodů).
    slovo = choice(list(slovnik.keys()))            # Losování slova
    print(ylo + f"Slovo má {len(slovo)} písmen.\n" + barvy_reset)
    vyreseno = False            # Nastavení úvodních podmínek a proměnných
    slovo_hadani = ["-" for _ in range((len(slovo)))]
    reseni = []
    while pokusy > 0 and vyreseno is not True:          # Vlastní zadávání písmenek
        zadani = input(ylo + "Zadej pismeno: " + barvy_reset).lower()
        if zadani in reseni:            # Kontrola zadaných písmen
            print(azur + "Toto písmeno jsi již zadal.\n" + barvy_reset)
            sleep(1)
            continue
        while zadani.isalpha() is not True or len(zadani) != 1:         # Kontrola vstupu
            zadani = input(ylo + "Chybný vstup. Není písmeno, nebo více než jeden znak. Zadej pismeno: " + barvy_reset).lower()
        reseni.append(zadani)
        if zadani in slovo:         # Uhodnuté písmeno
            print(grn + "Uhodl jsi písmeno!" + barvy_reset)
            sleep(1)
            for i in range(len(slovo)):
                for j in reseni:
                    if j == slovo[i]:
                        slovo_hadani[i] = j
        if zadani not in slovo:         # Neuhodnuté písmeno + prohra
            pokusy -= 1
            if pokusy < 1:
                body = prohraj_hru(slovo, body)
                return body
            print(red + f"Ztrácíš pokus. Zbývá {pokusy} pokusů." + barvy_reset)
            sleep(1)
        if str("".join(slovo_hadani)) == slovo:         # Výhra
            vyreseno = True
        if vyreseno is True:
            body = vyhraj_hru(slovo, body)
            return body
        else:         
            print(azur + "\n" + " ".join(slovo_hadani) + barvy_reset, sep="")           # Tisk již uhodnutých písmenek

def vyhraj_hru(slovo, body):
    # Přičte body a vypíše oznámení o výhře a správném řešení. Vyžaduje str a int (slovo a počet bodů).
    body += 1
    print(grn + f"""Vyhrál jsi! Slovo bylo {slovo.upper()}.
Aktuální skóre: {body} bodů.""" + barvy_reset)
    sleep(2)
    return body

def prohraj_hru(slovo, body):
    # Odečte body a vypíše oznámení o prohře a správném řešení. Vyžaduje str a int (slovo a počet bodů).
    body -= 1
    print(red + f"""Prohrál jsi. Slovo bylo {slovo.upper()}.
Aktuální skóre: {body} bodů.""" + barvy_reset)
    sleep(2)
    return body

def vrat_se_do_menu():
    # Vrátí uživatele k volbě hry.    
    oznameni_navrat = azur + "Budeš vrácen na úvod..." + barvy_reset
    print("\n", oznameni_navrat, sep="")
    sleep(2)

def ziskej_slova(volba, pokusy, body):    
    # Hra 2 a 3, uživatel zadává slova. Vyžaduje 3x int (volbu, počet pokusů a počet bodů).
    slovo = choice(list(slovnik.keys()))            # Losování slova
    vyreseno = False            # Nastavení úvodních podmínek a proměnných
    if volba == 2:
        slovo_list = [pismeno for pismeno in slovo]
        shuffle(slovo_list)
    while pokusy > 0 and vyreseno is not True:          # Vlastní zadávání slov
        if volba == 3:
            print(ylo + f"""Slovo má {len(slovo)} písmen a vyskytují se v něm pouze písmena.\nJeho definice je:
{slovnik[slovo]}\n""" + barvy_reset)
        if volba == 2:
            print(ylo + f"""Slovo má {len(slovo)} písmen a vyskytují se v něm pouze písmena.\nTato písmena v přeházeném pořadí vypadají následovně:
{" ".join(slovo_list)}\n""" + barvy_reset)
        zadani = input(ylo + "Zadej slovo: " + barvy_reset).lower()
        while zadani.isalpha() is not True or len(zadani) != len(slovo):            # Kontrola vstupu
            zadani = input(ylo + "Chybný vstup. Neobsahuje pouze písmena, nebo má špatnou délku. Zadej slovo: " + barvy_reset).lower()
        if zadani == slovo:         # Uhodnuté slovo
            vyreseno = True
        if zadani != slovo:         # Neuhodnuté slovo + prohra
            pokusy -= 1
            if pokusy < 1:
                body = prohraj_hru(slovo, body)
                return body
            print(red + f"Ztrácíš pokus. Zbývá {pokusy} pokusů.\n" + barvy_reset)
            sleep(1)
        if vyreseno is True:         # Výhra
            body = vyhraj_hru(slovo, body)
            return body
        
def zapis_skore(jmeno, body):
    # Zapisuje body do tabulky. Vyžaduje str a int (jméno a počet bodů).
    with open("vysledky.csv", mode="a", newline="", encoding="utf-8") as f:
        zapis = csv.writer(f)
        zapis.writerow([f"{body}, {jmeno}"])

def vypis_skore():
    # Vypisuje skóre.
    try:
        leaderboard = []
        with open(vychozi_nazev_souboru, mode="r", encoding="utf-8") as f:          # Přepsání výsledků do proměnné
            vypis = csv.reader(f)
            for radek in vypis:
                leaderboard.append(str(radek).strip("'[]"))

        leaderboard.sort(key=serad_prvky_podle_poradi_KLIC, reverse=True)           # Jejich seřazení
        
        print(Fore.BLUE + "\n" + "Prvních pět příček tabulky vítězů:".center(int(sire_rozhrani)) + barvy_reset)         # Jejich zobrazení
        i = 0
        while i < 5:
            try:
                print(Fore.MAGENTA + f"{str(leaderboard[i]).split(", ")[1].upper().rjust(int(sire_rozhrani/3))}" + ("." * 20).center(int(sire_rozhrani/3)) + f"{str(leaderboard[i]).split(", ")[0].upper()} bodů".ljust(int(sire_rozhrani/3)) + barvy_reset)
                i += 1
            except IndexError: break           # Kdyby jich tam bylo méně než pět
    except FileNotFoundError:           # Kdyby žádný soubor s výsledky neexistoval
        print(red + "\nZatím žádný záznam v tabulce vítězů" + barvy_reset)

def serad_prvky_podle_poradi_KLIC(prvek: str):
    # Pomocná funkce. Jedná se o klíč k řazení výsledků od nejvyššího skóre.
    return int(prvek.split(", ")[0])




### Vlastní aplikace

while True:    
    hry = ["Hádání po písmenkách", "Rozsypaná písmena", "Hádání na základě definice"]
    zobraz_uvod()
    if jmeno is None:           # Zadání jména a kontrola vstupu
        jmeno = input(Fore.MAGENTA + "Zadej své jméno: " + barvy_reset)
        while jmeno.isalnum() is False or len(jmeno) > 20 :
            jmeno = input(Fore.MAGENTA + "Pouze písmena a čísla, maximálně 20 znaků. Zadej své jméno: " + barvy_reset)
    pripustne_volby = ["1", "2", "3", "4", "5", "/cheat"]
    volba = ziskej_volbu()

    # Hra 1
    if volba == pripustne_volby[0]:
        specifikuj_hru(int(volba), 7)
        body = ziskej_pismena(7, body)
        vrat_se_do_menu()

    # Hra 2
    elif volba == pripustne_volby[1]:
        specifikuj_hru(int(volba), 3)
        body = ziskej_slova(int(volba), 3, body)
        vrat_se_do_menu()

    # Hra 3
    elif volba == pripustne_volby[2]:
        specifikuj_hru(int(volba), 5)
        body = ziskej_slova(int(volba), 5, body)
        vrat_se_do_menu()

    # Funkce 4
    elif volba == pripustne_volby[3]:
        vypis_skore()
        input(azur + "\nPro návrat do menu stiskni ENTER" + barvy_reset)
        vrat_se_do_menu()

    # Test mod k vyplnění tabulky vítězů
    elif volba == pripustne_volby[5]:
        body = int(input("Zadej počet bodů: "))

    # Funkce 5
    else:
        if body > 0:            # Kontrola, jestli hráč nahrál alespoň jeden bod
            print(azur + "Zapisuji tvé skóre..." + barvy_reset)
            zapis_skore(jmeno, body)
            sleep(2)
        print(azur + "Ukončuji aplikaci..." + barvy_reset)
        sleep(2)
        exit()