
# **Jak zainstalować i skonfigurować conda**

`conda` to narzędzie do zarządzania środowiskami w Pythonie. Dzięki niemu możemy łatwo instalować i zarządzać pakietami w Pythonie.

## **Jak zainstalować conda**

- [Instrukcja instalacji conda pod Macos](assets/conda__installation_for_macos.pdf)
- [Instrukcja instalacji conda pod Windows](assets/conda__installation_for_windows.pdf)

## **Jak skonfigurować conda**

- [Instrukcja konfiguracji conda](assets/conda__configuration.pdf)


## **Zainstalowałem i skonfigurowałem condę, jednak folder `modul_3` jest pusty**

![](./assets/jupyter_lab_no_notebooks_main.png)

Na początku folder modul_3 jest pusty, ale z każdą kolejną lekcją stopniowo go zapełnisz.
Docelowo na końcu modułu Twój folder będzie wyglądał tak:

![](./assets/jupyter_lab_no_notebooks_already_with_notebooks.png)

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