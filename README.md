# 🎮 Slovní duel (Terminálová hra v Pythonu)

**Autor:** rich95cz  
**Verze:** 1.0  
**Jazyk:** Python 3.13.3  
**Knihovny:** `colorama`, `csv`, `random`, `time`

## 🧠 O projektu

*Slovní duel* je terminálová hra, kde hráč soutěží proti náhodě – cílem je uhodnout slovo podle různých nápověd. Hra obsahuje tři režimy, skóruje správné a špatné odpovědi a zaznamenává výsledky do přehledné tabulky vítězů (`CSV`).

## 🎯 Herní režimy

1. **Hádání po písmenkách**  
   Uhodni slovo postupně, zadáváním jednotlivých písmen.

2. **Rozsypaná písmena**  
   Uhádni slovo, které máš zobrazeno v náhodném pořadí.

3. **Definice slova**  
   Uhádni slovo na základě jeho popisu.

## 🖥️ Ukázka spuštění

```bash
python main.py
```

Při spuštění hráč zadá své jméno a volí herní režim. Hra pracuje čistě v příkazové řádce.

Barevné výstupy jsou zajištěny pomocí knihovny colorama.
Výsledky jsou ukládány do vysledky.csv a hráč může zobrazit aktuální leaderboard.

## 📂 Soubory v projektu

    main.py – hlavní soubor s logikou hry

    vysledky.csv – automaticky generovaný soubor s výsledky

## 🔧 Instalace závislostí

Před spuštěním doporučujeme nainstalovat potřebné knihovny:

pip install colorama

## 💡 Možnosti rozšíření

    Uložení celého slovníku do .json souboru

    Více úrovní obtížnosti

    Počet výher/proher ve statistikách

    Možnost více kol v rámci jedné hry

## ✅ Ukázkové dovednosti

Projekt ukazuje:

    práci s uživatelským vstupem

    strukturování kódu pomocí funkcí

    zápis a čtení CSV souborů

    použití knihovny colorama pro zlepšení UI

    jednoduché třídění a výpis leaderboardu