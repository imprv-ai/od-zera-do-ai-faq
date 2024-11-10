---
tags:
    - KeyError
    - PDF
    - nbconvert
    - Pandoc
    - MikTeX
---

# **Różne - inne pytania i problemy**

## **Gdy próbuję wyciągnąć jakąś kolumnę z DataFrame dostaję błąd `KeyError`**


Podczas tworzenia kolumny z ilością mężczyzn w aplikacji prezentującej dane z półmaratonu wrocławskiego, otrzymuję błąd **`KeyError: Płeć`**:

![](./assets/streamlit__key_error_display_error.png)

W tym przypadku błąd `KeyError` wskazuje na brak kolumny `Płeć` w Twoim DataFrame.

* Błąd taki może wystąpić, gdy próbujesz odwołać się do kolumny, która nie istnieje w Twoim DataFrame. Upewnij się, że nazwa kolumny jest poprawna i zgodna z nazwą kolumny w Twoim DataFrame. Możesz sprawdzić nazwy kolumn w DataFrame, korzystając z metody `columns`:

    ```python
    df.columns
    ```

* Może to wynikać również z faktu, że dane zostały wczytane z pliku .csv z domyślnym separatorem - przecinkiem (`,`), podczas gdy plik ten używa separatorów w postaci średników (`;`). Upewnij się, że na końcu polecenia `pd.read_csv` dodałeś argument `sep=";"`, aby poprawnie określić separator danych:

    ![](./assets/streamlit__key_error_check_sep.png)

## **Gdy próbuję eksportować notebooka do PDF dostaję błąd `nbconvert failed: Pandoc wasn't found`**

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