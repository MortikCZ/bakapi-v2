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
pip install bakapi-v2
py -m pip install bakapi-v2
```
## Changelog
### 0.4
- Přidána funkce `get_timetable`, `get_timetable_actual`, `get_substitutions`, `get_subjects_info`, `get_subject_themes`, `get_marks_final`, `get_marks_measures` a `get_marks`.
- Oprava chyb v dokumentaci
- Oprava chyb v kódu
- Dokumentace API klienta je dostupná v souboru [`API_docs.md`](https://github.com/MortikCZ/bakapi-v2/blob/main/API_docs.md).
### 0.3 
- Oprava PyPi balíčku
### 0.2
- Přidána funkce `get_api_info`, `get_absence`, `get_gdpr_info`, `get_marks`, `get_events`, `get_my_events` a `get_public_events`.
- Nově je možné instalovat balíček pomocí `pip` příkazu.
### 0.1
- První release 

## Dokumentace
Dokumentace k tomuto projektu je dostupná v souboru [`API_docs.md`](https://github.com/MortikCZ/bakapi-v2/blob/main/API_docs.md) v kořenovém adresáři tohoto repozitáře.
