---
tags:
    - Moduł Bonusowy
    - St-paywall
---

# **St-paywall - problemy**

## Problemy z biblioteką `st-paywall`

Streamlit i St-paywall zostały zaktualizowane i w tej chwili nie współpracują ze sobą.
Tymczasowo można użyć zamiast biblioteki `st-paywall` przygotowanego przez nas pliku `bmc_auth.py`, który będzie zachowywał się jak ta biblioteka. 


### Potrzebne zmiany

1. Należy pobrać pliki <a href="../assets/modul-bonusowy.zip" download>>>>Pobierz archiwum ZIP<<<</a> i zapisać je w tym samym folderze, co plik przykładowej aplikacji **Opowiadacz**.

1. W powyższym archiwum są również pozostałe zaktualizowane pliki do odpowiednich lekcji z **Modułu Bonusowego**: 
```bash
app_v2.py
app_v3.py
app_v4.py
bmc_auth.py
```
W każdym z tych plików zostały wprowadzone konieczne zmiany, aby dostować aplikację do nowego sposobu obsługiwania logowania Google przez Streamlita.

    Np. w tej chwili dane użytkownika pobieramy:
```Python
st.user.email
```
    Zamiast wcześniejszego:
```Python
st.session_state['email']
```

1. Jeśli za jakiś czas biblioteka `st_paywall` zostanie poprawiona, to będzie można do niej łatwo wrócić. <br>
Należy wtedy ponownie użyć importu: 
```Python
from st_paywall import add_auth
```
Oraz zamiast obecnej funkcji `add_bmc_auth()` ponownie użyć funkcji `add_auth()`, z tymi samymi parametrami co w załączonych plikach aplikacji.

### Poprawny format pliku `secrets.toml`
```Python
payment_provider = "bmac" 
bmac_api_key = "..."
bmac_link = "..."
OPENAI_API_KEY = "..."
# Data Base
dialect = "postgresql"
username = "..."
password = "..."
host = "..."
port = ...
database = "..."
sslmode = "require"

[auth]
redirect_uri = "http://localhost:8501/oauth2callback" # Lub "https://twoja-domena.com/oauth2callback" - ważna jest ta końcówka
cookie_secret = "...." # Dowolny długi ciąg znaków
client_id = "..."
client_secret = '...'
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```
