# Programowanie w języku Python

Krótki opis projektu: repo zawiera materiały i przykłady do nauki programowania w Pythonie.

## Jak uruchomić
1. Utwórz i aktywuj wirtualne środowisko:
   - Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
2. Zainstaluj zależności (jeśli jest requirements.txt):
   ```bash
   pip install -r requirements.txt
   ```

## Struktura repo
- foldery z przykładami i zadaniami
- pliki .py z ćwiczeniami

## Zadania
- [zadanie1.py](zadanie1.py) — krótki opis zadania 1
- [zadanie2.py](zadanie2.py) — krótki opis zadania 2
- (Jeśli pliki są w podfolderze, użyj np. [zadanie3.py](folder/zadanie3.py))

## Jak dodać zadania i wypchnąć na GitHub
1. Umieść pliki .py w katalogu repo (np. zadanie1.py, zadanie2.py).
2. W terminalu w katalogu projektu:
   ```bash
   git add .
   git commit -m "Dodaj zadania"
   ```
3. Jeśli repo nie ma zdalnego origin, dodaj je (zamień URL):
   ```bash
   git remote add origin https://github.com/TWOJ_USER/TWOJ_REPO.git
   git branch -M main
   git push -u origin main
   ```
   Lub użyj SSH:
   ```bash
   git remote add origin git@github.com:TWOJ_USER/TWOJ_REPO.git
   git push -u origin main
   ```
4. Alternatywa — utworzenie i wypchnięcie repo jednym poleceniem (gh CLI):
   ```bash
   gh repo create NAZWA_REPO --public --source=. --remote=origin --push
   ```
5. Jeśli GitHub poprosi o uwierzytelnienie przez HTTPS, użyj tokenu PAT jako hasła lub skonfiguruj klucze SSH.

### Przykład — dodanie i wypchnięcie konkretnych plików (szybko)
- Jeśli chcesz dodać konkretne pliki (np. zadanie1.py i zadanie2.py) i wypchnąć:
```bash
# sprawdź status
git status

# dodaj konkretne pliki
git add zadanie1.py zadanie2.py

# commit z opisem
git commit -m "Dodaj zadania: zadanie1.py, zadanie2.py"

# przed push najlepiej pobrać aktualizacje i zrebase'ować, aby uniknąć konfliktów
git pull --rebase origin main

# wypchnij zmiany
git push origin main
```

- Jeśli nie masz remote lub go nie pamiętasz:
```bash
git remote -v
# jeśli brak remote:
git remote add origin https://github.com/TWOJ_USER/TWOJ_REPO.git
git push -u origin main
```

- Gdy napotkasz konflikt przy pull:
```bash
# rozwiąż konflikt w plikach ręcznie, potem:
git add <rozwiązane_pliki>
git rebase --continue   # jeśli używałeś --rebase
# lub
git commit              # jeśli merge
git push origin main
```

## Podstawowe polecenia git — szybki cheat-sheet
- Sklonowanie repo:
  ```bash
  git clone https://github.com/TWOJ_USER/TWOJ_REPO.git
  cd TWOJ_REPO
  ```
- Sprawdzenie stanu i zmian:
  ```bash
  git status
  git diff
  ```
- Dodanie zmian i commit:
  ```bash
  git add <plik_lub_folder>    # np. git add zadanie1.py
  git commit -m "Krótki opis zmian"
  ```
- Praca na gałęziach:
  ```bash
  git branch                # lista gałęzi
  git checkout main         # przełącz na main
  git checkout -b nowa-gałąź  # utwórz i przełącz się na nową gałąź
  ```
- Aktualizacja zdalnego repo i wysyłanie zmian:
  ```bash
  git pull origin main      # pobierz i zmerguj zmiany z main
  git push -u origin nowa-gałąź  # wypchnij nową gałąź i ustaw śledzenie
  git push origin main      # wypchnij zmiany na main
  ```
- Jeśli chcesz zaktualizować README lokalnie i wypchnąć:
  ```bash
  # w katalogu projektu
  git pull origin main
  git add README.md
  git commit -m "Update README"
  git push origin main
  ```
- Szybkie tworzenie i wysłanie repo (gh CLI):
  ```bash
  gh repo create NAZWA_REPO --public --source=. --remote=origin --push
  ```

Uwagi:
- Zamiast hasła przy HTTPS użyj PAT (Personal Access Token) — GitHub wymaga tokenów.  
- Jeśli coś się nie zgadza (konflikty), napisz, pomogę krok po kroku.  

## Wkład
Zgłaszaj issue lub wysyłaj pull requesty.

## Licencja
(Dopisz licencję, np. MIT)
