
# Błędy w Conda - Przyczyny i rozwiązania

'conda' to wszechstronne narzędzie do zarządzania środowiskami Python. Umożliwia ono łatwe instalowanie i zarządzanie pakietami, co znacząco ułatwia pracę z Pythonem. Niemniej jednak, podczas korzystania z conda można napotkać różne błędy. W tej sekcji znajdziesz przegląd najczęstszych problemów, ich możliwe przyczyny oraz sprawdzone sposoby na ich rozwiązanie.

## Widzę błąd: `Value type <class 'str'> must match with type plot`

Niektóre polecenia w Condzie działają poprawnie, ale gdy próbuję narysować wykres, pojawia się następujący błąd:

![](./assets/conda_errors_plot_error.png)

1. Sprawdź nazwę folderu, w którym znajduje się używany notebook. 
    * Domyślnie w kursie jest on zapisany pod nazwą modul_*, gdzie gwiazdka oznacza numer modułu. 
    * Upewnij się, że nazwa Twojego folderu nie zawiera spacji (zamiast spacji warto użyć podkreślnika)

    ![](./assets/conda_errors_plot_error_folder_name.png)

1. Zrestartuj kernel i uruchom ponownie wszystkie komórki, zaczynając od pierwszej.

    ![](./assets/conda_errors_plot_error_kernel_restart.png)

Dla zainteresowanych: przyczyną występowania błędu jest walidacja w bibliotece [pandasai](https://github.com/Sinaptik-AI/pandas-ai/blob/e011e8ffdc8a2cd88db07c4440f331540a175648/pandasai/helpers/output_validator.py#L99).

