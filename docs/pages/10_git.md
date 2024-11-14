---
tags: 
    - Git
    - komendy
---

# **Git - problemy i podstawowe komendy**

**Git** to narzędzie do zarządzania kodem źródłowym, które pozwala na śledzenie zmian w kodzie, a także na współpracę z innymi programistami. Git jest bardzo popularnym narzędziem wśród programistów i jest szeroko stosowany w branży IT.

## **Jak rozwiązać najczęstsze problemy związane z Gitem?**

### **Widzę błąd: `fatal: not a git repository (or any of the parent directories): .git`**

Jeżeli widzisz błąd `fatal: not a git repository (or any of the parent directories): .git`, oznacza to, że nie jesteś w folderze, który jest repozytorium Gita. Upewnij się, że znajdujesz się w odpowiednim folderze, w którym utworzyłeś repozytorium Gita.

### **Widzę błąd: `error: src refspec master does not match any`**

Jeżeli widzisz błąd `error: src refspec master does not match any`, oznacza to, że nie dodałeś żadnych plików do repozytorium. Upewnij się, że dodałeś pliki do repozytorium za pomocą polecenia `git add nazwa_pliku` lub `git add .`, a następnie zacommitowałeś zmiany za pomocą polecenia `git commit -m "Opis zmian"`.

### **Widzę błąd: `error: failed to push some refs to '...'`**

Jeżeli widzisz błąd `error: failed to push some refs to '...'`, oznacza to, że wystąpił problem podczas wysyłania zmian do repozytorium zdalnego. Sprawdź, czy masz dostęp do repozytorium zdalnego i czy masz uprawnienia do zapisu.


## **Podstawowe komendy w Git**

Poniżej znajdziesz listę podstawowych komend w Gicie, które pomogą Ci w zarządzaniu kodem źródłowym. Możesz również pobrać plik PDF z listą komend, aby mieć je zawsze pod ręką.

[Pobierz PDF](assets/GIT_commands.pdf)

### **Jak sprawdzić, czy mam zainstalowanego Gita?**

Aby sprawdzić, czy masz zainstalowanego Gita, otwórz terminal i wpisz poniższe polecenie:

```bash 
git --version
```

Jeżeli Git jest zainstalowany, zobaczysz informację o jego wersji.

### **Jak skonfigurować Gita?**

Aby skonfigurować Gita, wpisz w terminalu poniższe polecenia, podając swoje dane:

```bash
git config --global user.name "Twoje Imię i Nazwisko"
git config --global user.email "
```

### **Jak utworzyć nowe repozytorium Gita?**

Aby utworzyć nowe repozytorium Gita, przejdź do folderu, w którym chcesz utworzyć repozytorium, a następnie wpisz poniższe polecenie:

```bash
git init
```

Polecenie `git init` utworzy nowe repozytorium Gita w bieżącym folderze.

### **Jak sklonować istniejące repozytorium Gita na swój komputer?**

Aby sklonować istniejące repozytorium Gita na swój komputer, wpisz poniższe polecenie w terminalu:

```bash
git clone adres_repozytorium
```

Adres repozytorium możesz znaleźć na stronie repozytorium na platformie, na której jest hostowane (np. GitHub, GitLab). W tym celu skopiuj adres URL repozytorium i wklej go w powyższym poleceniu.

### **Jak sprawdzić status zmian w repozytorium Gita? (zmodyfikowane/nieśledzone pliki, aktualny branch)**

Aby sprawdzić status zmian w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git status
```

Polecenie `git status` pokaże listę zmodyfikowanych/nieśledzonych plików oraz aktualny branch.

### **Jak dodać pliki do repozytorium Gita?**

Aby dodać pliki do repozytorium Gita, wpisz poniższe polecenie w terminalu:

* Dodanie pojedynczego pliku:
```bash
git add nazwa_pliku
```

* Dodanie wszystkich plików:
```bash
git add .
```

### **Jak zacommitować zmiany w repozytorium Gita?**

Aby zacommitować zmiany w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git commit -m "Opis zmian"
```

W miejsce `Opis zmian` wpisz krótki opis zmian, które wprowadziłeś.

### **Jak edytować ostatni commit w repozytorium Gita?**

Aby edytować ostatni commit w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git commit --amend
```

### **Jak sprawdzić historię commitów w repozytorium Gita?**

Aby sprawdzić historię commitów w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git log
```

Polecenie `git log` pokaże listę commitów w repozytorium.

### **Jak wyświetlić wszystkie branch'e w repozytorium Gita?**

Aby wyświetlić wszystkie branch'e w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git branch
```

Polecenie `git branch` pokaże listę wszystkich branch'y w repozytorium.

### **Jak utworzyć nowy branch w repozytorium Gita?**

Aby utworzyć nowy branch w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git branch nazwa_brancha
```

W miejsce `nazwa_brancha` wpisz nazwę nowego brancha.

### **Jak przełączyć się na inny branch w repozytorium Gita?**

Aby przełączyć się na inny branch w repozytorium Gita, wpisz poniższe polecenie w terminalu:

* Przełączenie na istniejący branch:
```bash
git checkout nazwa_brancha
```

* Utworzenie nowego brancha i przełączenie się na niego:
```bash
git checkout -b nazwa_brancha
```

W miejsce `nazwa_brancha` wpisz nazwę brancha, na który chcesz się przełączyć.

### **Jak usunąć branch w repozytorium Gita?**

Aby usunąć branch w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git branch -d nazwa_brancha
```

W miejsce `nazwa_brancha` wpisz nazwę brancha, który chcesz usunąć.

### **Jak zmergować branch z innym branch'em w repozytorium Gita?**

Aby zmergować branch z innym branch'em w repozytorium Gita, przełącz się na branch, do którego chcesz zmergować inny branch, a następnie wpisz poniższe polecenie w terminalu:

```bash
git merge nazwa_brancha
```
W miejsce `nazwa_brancha` wpisz nazwę brancha, który chcesz zmergować z aktualnym branch'em. 

### **Jak zmienić nazwę brancha w repozytorium Gita?**

Aby zmienić nazwę brancha w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git branch -m nowa_nazwa_brancha
```

W miejsce `nowa_nazwa_brancha` wpisz nową nazwę brancha.

### **Jak dodać repozytorium zdalne w repozytorium Gita?**

Aby dodać repozytorium zdalne w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git remote add origin adres_repozytorium
```

Adres repozytorium zdalnego możesz znaleźć na stronie repozytorium na platformie, na której jest hostowane (np. GitHub, GitLab). W tym celu skopiuj adres URL repozytorium i wklej go w powyższym poleceniu.

### **Jak pobrać zmiany z repozytorium zdalnego do repozytorium lokalnego w Gicie?**

Aby pobrać zmiany z repozytorium zdalnego do repozytorium lokalnego w Gicie, wpisz poniższe polecenie w terminalu:

* 
```bash
git pull
```

* 
```bash
git pull --rebase
```

Różnica między `git pull` a `git pull --rebase` polega na tym, że `git pull` pobiera zmiany z repozytorium zdalnego i łączy je z lokalnym branch'em, tworząc nowy commit mergujący zmiany. Natomiast `git pull --rebase` pobiera zmiany z repozytorium zdalnego i nakłada je na lokalny branch, tworząc nowe commity na podstawie zmian z repozytorium zdalnego.

### **Jak wysłać zmiany z repozytorium lokalnego do repozytorium zdalnego w Gicie?**

Aby wysłać zmiany z repozytorium lokalnego do repozytorium zdalnego w Gicie, wpisz poniższe polecenie w terminalu:

* 
```bash
git push origin nazwa_brancha
```

* 
```bash
git push
```

Pierwsze polecenie wysyła zmiany z lokalnego brancha do zdalnego brancha o nazwie `nazwa_brancha`. Drugie polecenie wysyła zmiany z aktualnego brancha do zdalnego brancha o tej samej nazwie, czyli do domyślnego brancha zdalnego.

### **Jak zobaczyć różnice między plikami w repozytorium Gita?**

Aby zobaczyć różnice między plikami w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git diff
```

Polecenie `git diff` pokaże różnice między plikami w repozytorium.

### **Jak cofnąć zmiany w repozytorium Gita?**

Aby cofnąć zmiany w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git checkout -- nazwa_pliku
```

Polecenie `git checkout -- nazwa_pliku` cofnie zmiany w pliku i przywróci go do poprzedniego stanu.

### **Jak cofnąć ostatni commit w repozytorium Gita?**

Aby cofnąć ostatni commit w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git reset --soft HEAD~1
```

Polecenie `git reset --soft HEAD~1` cofnie ostatni commit, ale zachowa zmiany w plikach.

### **Jak cofnąć ostatni commit wraz z zmianami w repozytorium Gita?**

Aby cofnąć ostatni commit wraz z zmianami w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git reset --hard HEAD~1
```

Polecenie `git reset --hard HEAD~1` cofnie ostatni commit wraz z wprowadzonymi zmianami w plikach.

### **Jak zobaczyć listę zatwierdzonych zmian w repozytorium Gita?**

Aby zobaczyć listę zatwierdzonych zmian w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git stash list
```

Polecenie `git stash list` pokaże listę zatwierdzonych zmian w repozytorium.

### **Jak zatwierdzić zmiany w repozytorium Gita?**

Aby zatwierdzić zmiany w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git stash
```

Polecenie `git stash` zatwierdzi zmiany w repozytorium.

### **Jak przywrócić zatwierdzone zmiany w repozytorium Gita?**

Aby przywrócić zatwierdzone zmiany w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git stash apply
```

Polecenie `git stash apply` przywróci zatwierdzone zmiany w repozytorium.

### **Jak usunąć zatwierdzone zmiany w repozytorium Gita?**

Aby usunąć zatwierdzone zmiany w repozytorium Gita, wpisz poniższe polecenie w terminalu:

```bash
git stash drop
```

Polecenie `git stash drop` usunie zatwierdzone zmiany w repozytorium.
