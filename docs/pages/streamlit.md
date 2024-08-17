# **Problemy ze Streamlit**

## **Podczas wyciągania danych z pliku .csv dostaję błąd `KeyError`**

Podczas tworzenia kolumny z ilością mężczyzn w aplikacji prezentującej dane z półmaratonu wrocławskiego, otrzymuję błąd `KeyError`.

![](./assets/streamlit__key_error_display_error.png)

Upewnij się, że na końcu polecenia `pd.read_csv` dodałeś argument `sep=";"`, aby poprawnie określić separator danych:

![](./assets/streamlit__key_error_check_sep.png)