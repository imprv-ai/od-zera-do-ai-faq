
# Problemy z jupyter lab / notebooki

Jupyter lab to interaktywne środowisko do pracy z notatnikami jupyter. Pozwala na pracę z wieloma notatnikami jednocześnie, a także na przeglądanie plików, terminal, konsolę pythona i wiele innych.


## Jupyter startuje ale nie działa. Widzę okno przeglądarki, ale Jupyter się nie odpala

Może to oznaczać, że masz zablokowane wyskakujące okna w przeglądarce. Spróbuj uruchomić Jupyter Notebook bezpośrednio z uprawnieniami administratora Następnie pojawi się konsola, w której będzie widać logi Jupyter Notebooka, które zawierają link do notebooka. Skopiuj ten link i wklej go do przeglądarki. Link powinien wyglądać mniej więcej tak:

`http://localhost:8888/tree?token=f7e5908823221f7bc83e0382337300e6bbe552e2013cc27f`

Twój token będzie inny!

![](assets/jupyter_lab__open.png)

## Śledzę kurs lub robię zadanie domowe i komórka się nie uruchamia a ja widzę ogromny błąd

Jeżeli widzisz błąd:

![](assets/notebook__file_not_found.png)

Zwróć uwagę na początek komunikatu o błędzie .
Jeśli jest tam informacja o braku pliku (np. `FileNotFoundError` jak na obrazku) to najprawdopodobniej masz błąd w ścieżce lub plik nie został pobrany we wskazane miejsce.

Sprawdź czy ścieżki są poprawne i czy plik istnieje.

Pliki z danymi znajdziesz w sekcji `Pliki do pobrania` pod filmami na platformie kursu.
