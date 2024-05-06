# bakapi-v2
Klient k API Bakalářů v jazyce Python.

Tento projekt je API klient pro Bakaláře, který umožňuje získávat data z API Bakalářů a manipulovat s nimi pomocí jazyka Python. Funkce budou postupně rozšiřovány až do kompletního pokrytí API Bakalářů.

## Licence
Tento projekt obsahuje kód, který je licencován pod MIT licencí. Podrobnosti o této licenci naleznete v souboru `LICENSE` v kořenovém adresáři tohoto repozitáře. 

Přispěvatelé k tomuto projektu jsou vyzváni k dodržování podmínek MIT licence pro jakýkoliv kód, který přidají nebo upraví v tomto repozitáři.

Tento projekt používá kód z nasledujícího repozitáře:
[bakapi](https://github.com/mvolfik/bakapi), autor: [mvolfik](https://github.com/mvolfik)

## Instalace
Instalace je zatím možná pouze pomocí stažení zdrojových kódů z tohoto repozitáře.

V budoucnu bude možné instalovat balíček pomocí `pip` příkazu.

## Changelog
### 0.1
- První release 

## Dokumentace
API klient je navržen pro komunikaci s API Bakalářů pomocí jazyka Python. Poskytuje sadu funkcí pro získávání dat z API a jejich manipulaci.

### Funkce API klienta:
- `get_student_info()`: Tato funkce slouží k získání informací o studentovi.
- `get_subjects()`: Tato funkce vrátí seznam předmětů a informace o nich..
- `get_timetable()`: Tato funkce vrátí rozvrh studenta.
- `get_homework()`: Tato funkce vrátí seznam domácích úkolů.

Pro použití API klienta je nejprve nutné provést inicializaci objektu klienta a přihlášení pomocí přihlašovacích údajů studenta. Poté je možné volat jednotlivé funkce pro získání a manipulaci s daty z API.

Proměnné potřebné pro přihlášení:
- `username`: Uživatelské jméno
- `password`: Heslo
- `url`: URL adresa Bakalářů (musí odkazovat na přihlašovací stránku).

##
Kompletní dokumentaci k API Bakalářů a seznamu Endpointů naleznete zde: [bakalari-api-v3](https://github.com/bakalari-api/bakalari-api-v3)
