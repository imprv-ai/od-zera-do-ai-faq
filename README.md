
# FAQ dla kursu `od zera do AI`

## Jak uruchomić lokalnie

```bash
# zainstaluj mkdocs i inne zależności
poetry install

# aktywacja środowiska
poetry shell

# uruchom serwer z docsami - żeby mieć podgląd lokalnie
mkdocs serve
```

lub
```bash
# uruchamia bezpośrednio w środowisku aktywując po cichu poetry
poetry run mkdocs serve
```

## Jak publikować zmiany?

```bash
# Żeby zrobić nowy branch
git checkout -b nazwa_problemu_nad_ktorym_pracujesz
```

```bash
# Dodajemy nasze wszystkie zmiany do zatwierdzenia ( commita )
git add .
```

```bash
# Zatwierdzamy zmiany
git commit -m "krótka informacja co zostało zmienione"
```

```bash
# Wypychamy zatwierdzone zmiany
# Część `-u origin nazwa_problemu_nad_ktorym_pracujesz` dodajemy tylko przy pierwszym pushu

# Pierwsze wywołanie dla brancha
git push -u origin nazwa_problemu_nad_ktorym_pracujesz

# Każde kolejne
git push
```

Teraz należy ztworzyć Pull Request. Można to zrobić z poziomu strony GitHub
