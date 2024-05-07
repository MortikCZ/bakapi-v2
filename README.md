# bakapi-v2
Klient k API Bakalářů v jazyce Python.

Tento projekt je API klient pro Bakaláře, který umožňuje získávat data z API Bakalářů a manipulovat s nimi pomocí jazyka Python. Funkce budou postupně rozšiřovány až do kompletního pokrytí API Bakalářů.

## Licence
Tento projekt obsahuje kód, který je licencován pod MIT licencí. Podrobnosti o této licenci naleznete v souboru `LICENSE` v kořenovém adresáři tohoto repozitáře. 

Přispěvatelé k tomuto projektu jsou vyzváni k dodržování podmínek MIT licence pro jakýkoliv kód, který přidají nebo upraví v tomto repozitáři.

Tento projekt používá kód z nasledujícího repozitáře:
[bakapi](https://github.com/mvolfik/bakapi), autor: [mvolfik](https://github.com/mvolfik)

## Instalace
Instalace je možná pomocí `pip` příkazu:
```bash
pip install bakapiv2
py -m pip install bakapiv2
```
## Changelog

### 0.2
- Přidána funkce `get_api_info`, `get_absence`, `get_gdpr_info`, `get_marks`, `get_events`, `get_my_events` a `get_public_events`.
- Nově je možné instalovat balíček pomocí `pip` příkazu.
### 0.1
- První release 

## Dokumentace
API klient je navržen pro komunikaci s API Bakalářů pomocí jazyka Python. Poskytuje sadu funkcí pro získávání dat z API a jejich manipulaci.

### Funkce API klienta:
- `get_student_info`: Tato funkce slouží k získání informací o studentovi.
- `get_subjects`: Tato funkce vrátí seznam předmětů a informace o nich..
- `get_timetable_actual`: Tato funkce vrátí rozvrh studenta.
- `get_homework`: Tato funkce vrátí seznam domácích úkolů.
- `get_absence`: Tato funkce vrátí seznam absencí studenta.
- `get_marks`: Tato funkce vrátí seznam známek studenta.
- `get_events`: Tato funkce vrátí seznam událostí.
- `get_my_events`: Tato funkce vrátí seznam událostí studenta.
- `get_public_events`: Tato funkce vrátí seznam veřejných událostí.
- `get_gdpr_info`: Tato funkce vrátí informace o GDPR.
- `get_api_info`: Tato funkce vrátí informace o API.

Pro použití API klienta je nejprve nutné provést inicializaci objektu klienta a přihlášení pomocí přihlašovacích údajů studenta. Poté je možné volat jednotlivé funkce pro získání a manipulaci s daty z API.

Proměnné potřebné pro přihlášení:
- `username`: Uživatelské jméno
- `password`: Heslo
- `url`: URL adresa Bakalářů (musí odkazovat na přihlašovací stránku).

##
Kompletní dokumentaci k API Bakalářů a seznam Endpointů naleznete [zde](https://github.com/bakalari-api/bakalari-api-v3).
