# **Problemy ze Streamlit**

## **Halfmarathon - gdy próbuję wyciągnąć liczbę mężczyzn z DataFrame dostaję błąd `KeyError`**

Podczas tworzenia kolumny z ilością mężczyzn w aplikacji prezentującej dane z półmaratonu wrocławskiego, otrzymuję błąd **`KeyError: Płeć`**:

![](./assets/streamlit__key_error_display_error.png)

Błąd `KeyError` wskazuje na brak kolumny `Płeć` w Twoim DataFrame. Może to wynikać z faktu, że dane zostały wczytane z pliku .csv z domyślnym separatorem - przecinkiem (`,`), podczas gdy plik ten używa separatorów w postaci średników (`;`). Upewnij się, że na końcu polecenia `pd.read_csv` dodałeś argument `sep=";"`, aby poprawnie określić separator danych:

![](./assets/streamlit__key_error_check_sep.png)