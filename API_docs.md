# Dokumentace API Klienta 

**Modul obsahuje hlavní třídu `BakapiUser`**

API klient komunikuje s API Bakalářů pouze při poskytnutí následujících parametrů:
- `username`: Uživatelské jméno pro přihlášení do Bakalářů.
- `password`: Heslo pro přihlášení do Bakalářů.
- `url`: URL adresa Bakalářů, která odkazuje na přihlašovací stránku.

## Funkce API klienta:
- [`get_student_info`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/user.md): vrací informace o uživateli.
- [`get_homework_count`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/homework_new.md): vrací počet domácích úkolů.
- [`get_timetable_perm`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/timetable.md): vrací stálý rozvrh.
- [`get_timetable_actual`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/timetable.md): vrací aktuální rozvrh, příjímá parametr `date` ve formátu `YYYY-MM-DD`.
- [`get_substitutions`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/substitutions.md): vrací seznam zastupování, funkce přijímá parametr `since` ve formátu `YYYY-MM-DD`, který je předán API jako parametr `from`.
- [`get_subjects_info`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/subjects.md): vrací seznam předmětů a informace o jejich učitelích.
- [`get_subject_themes`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/themes.md): vrací seznam hodin a jejich témata za celý školní rok v daném předmětu, přijímá parametr `subject_id`.
- [`get_api_info`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/API_info.md): vrací přehled všech dostupných API verzí.
- [`get_absence`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/absence.md): vrací absenci podle dní a předmětů.
- [`get_gdpr_info`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/gdpr.md): vrací informace o pověřenci pro ochranu osobních údajů.
- [`get_marks`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/marks.md): vrací předměty a jejich známky.
- [`get_marks_final`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/marks_final.md): vrací všechny vysvědčení od začátku studia.
- [`get_marks_measures`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/marks_measures.md): vrací kázeňské přestupky a pochvaly (třídního učitele, ředitele) za celou dobu studia.
- [`get_events`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/events.md): vrací seznam všech událostí, funkce přijímá parametr `since` ve formátu `YYYY-MM-DD`, který je předán API jako parametr `from`.
- [`get_my_events`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/events.md): vrací seznam událostí, které se týkají uživatele, funkce přijímá parametr `since` ve formátu `YYYY-MM-DD`, který je předán API jako parametr `from`.
- [`get_public_events`](https://github.com/bakalari-api/bakalari-api-v3/blob/master/moduly/events.md): vrací seznam veřejných událostí, funkce přijímá parametr `since` ve formátu `YYYY-MM-DD`, který je předán API jako parametr `from`.

