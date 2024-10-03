
# **Problemy z jupyter lab / notebooki**

**Jupyter lab** to interaktywne środowisko do pracy z notatnikami jupyter. Pozwala na pracę z wieloma notatnikami jednocześnie, a także na przeglądanie plików, terminal, konsolę pythona i wiele innych.


## **Jupyter startuje, ale nie działa. Widzę okno przeglądarki, ale Jupyter się nie odpala**

Może to oznaczać, że masz zablokowane wyskakujące okna w przeglądarce. Spróbuj uruchomić Jupyter Notebook bezpośrednio z uprawnieniami administratora Następnie pojawi się konsola, w której będzie widać logi Jupyter Notebooka, które zawierają link do notebooka. Skopiuj ten link i wklej go do przeglądarki. Link powinien wyglądać mniej więcej tak:

`http://localhost:8888/tree?token=f7e5908823221f7bc83e0382337300e6bbe552e2013cc27f`

Twój token będzie inny!

![](assets/jupyter_lab__open.png)

## **Śledzę kurs lub robię zadanie domowe i komórka się nie uruchamia, a ja widzę ogromny błąd**

Jeżeli widzisz błąd:

![](assets/notebook__file_not_found.png)

Zwróć uwagę na początek komunikatu o błędzie .
Jeśli jest tam informacja o braku pliku (np. `FileNotFoundError` jak na obrazku) to najprawdopodobniej masz błąd w ścieżce lub plik nie został pobrany we wskazane miejsce.

Sprawdź czy ścieżki są poprawne i czy plik istnieje.

Pliki z danymi znajdziesz w sekcji `Pliki do pobrania` pod filmami na platformie kursu.

## **Kiedy uruchamiam *jupyter lab* przez terminal pojawia się nietypowy błąd**

![](./assets/jupyter_lab__second_opening_error.png)

Jeśli podczas uruchamiania *jupyter lab* w konsoli pojawia się taki błąd, oznacza to, że nie aktywowałeś swojego środowiska Conda. Aby to zrobić:

1. Najpierw aktywuj swoje środowisko, wpisując `conda activate od_zera_do_ai` (domyślnie według kursu). Zauważysz wtedy, że środowisko zostało zmienione z domyślnego 'base' na Twoje własne.

    ![](./assets/jupyter_lab__second_opening_activate_environment.png)

1. Następnie przejdź do folderu z Twoimi notebookami (domyślnie w kursie jest to folder na pulpicie o nazwie *od_zera_do_ai*) i skopiuj jego ścieżkę.

    ![](./assets/jupyter_lab__second_opening_folder_path.png)

1. Przejdź do tego folderu w konsoli, używając komendy `cd` i wklejając jego ścieżkę

    ![](./assets/jupyter_lab__second_opening_write_path_to_console.png)

1. Na koniec uruchom `jupyter lab`

    ![](./assets/jupyter_lab__second_opening_run_jupyter.png)

## **Nie działa eksportowanie notebooka do PDF na Windows**

Jeżeli próbujesz wyeksportować notebooka do PDF i dostajesz błąd:

![](./assets/notebook_to_pdf__step_1.png)

Wówczas będziemy musieli zainstalować dwie biblioteki: `pandoc` oraz `MikTeX`.

Aby zainstalować `pandoc`:

- Przechodzimy na stronę [https://pandoc.org/installing.html](https://pandoc.org/installing.html)
- I wykonujemy następujące kroki:

![](assets/notebook_to_pdf__step_2.png)
![](assets/notebook_to_pdf__step_3.png)
![](assets/notebook_to_pdf__step_4.png)
![](assets/notebook_to_pdf__step_5.png)
![](assets/notebook_to_pdf__step_6.png)

Aby zainstalować `MikTeX`:
- Przechodzimy na stronę [https://miktex.org/download](https://miktex.org/download)
- I wykonujemy następujące kroki:

![](assets/notebook_to_pdf__step_7.png)
![](assets/notebook_to_pdf__step_8.png)
![](assets/notebook_to_pdf__step_9.png)
![](assets/notebook_to_pdf__step_10.png)
![](assets/notebook_to_pdf__step_11.png)
![](assets/notebook_to_pdf__step_12.png)
![](assets/notebook_to_pdf__step_13.png)
![](assets/notebook_to_pdf__step_14.png)
![](assets/notebook_to_pdf__step_15.png)
![](assets/notebook_to_pdf__step_16.png)

- Uruchamiamy ponownie `Anaconda Prompt`, następnie `jupyter lab` i próbujemy ponownie wyeksportować notebooka do PDF. W tym momencie zostaniemy poproszeni o doinstalowanie dodatkowych pakietów, klikamy `Install`:

![](assets/notebook_to_pdf__step_17.png)
![](assets/notebook_to_pdf__step_18.png)
![](assets/notebook_to_pdf__step_19.png)
![](assets/notebook_to_pdf__step_20.png)
![](assets/notebook_to_pdf__step_21.png)
![](assets/notebook_to_pdf__step_22.png)
![](assets/notebook_to_pdf__step_23.png)
![](assets/notebook_to_pdf__step_24.png)
![](assets/notebook_to_pdf__step_25.png)
![](assets/notebook_to_pdf__step_26.png)
![](assets/notebook_to_pdf__step_27.png)
![](assets/notebook_to_pdf__step_28.png)
![](assets/notebook_to_pdf__step_29.png)
![](assets/notebook_to_pdf__step_30.png)
![](assets/notebook_to_pdf__step_31.png)
![](assets/notebook_to_pdf__step_32.png)
![](assets/notebook_to_pdf__step_33.png)
![](assets/notebook_to_pdf__step_34.png)
![](assets/notebook_to_pdf__step_35.png)
![](assets/notebook_to_pdf__step_36.png)
![](assets/notebook_to_pdf__step_37.png)
![](assets/notebook_to_pdf__step_38.png)
![](assets/notebook_to_pdf__step_39.png)
![](assets/notebook_to_pdf__step_40.png)
![](assets/notebook_to_pdf__step_41.png)
![](assets/notebook_to_pdf__step_42.png)
