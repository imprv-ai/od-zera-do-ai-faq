---
tags:
    - Streamlit Community Cloud
    - Moduł 6
    - wdrożenie
    - repozytorium
    - deploy
---

# **Streamlit Community Cloud - problemy**

**Streamlit Community Cloud** to platforma, która pozwala na wdrożenie aplikacji stworzonych w Streamlit. Poniżej znajdziesz rozwiązania na najczęściej pojawiające się problemy związane z tą platformą.

## **Podczas wdrażania aplikacji nie widzę mojego repozytorium**

Przy próbie wdrożenia aplikacji, kiedy klikam `Create App` i klikam w pole `Repository` nic mi się nie wyświetla, a później
inne pola świecą się na czerwono

![](./assets/streamlit_community_cloud__cant_select_repository.png)


1. **Kliknij w swoją nazwę w lewym górnym rogu**
![](./assets/streamlit_community_cloud__cant_select_repository__solution_step_1.png)

1. **Z menu wybierz `Settings`**
![](./assets/streamlit_community_cloud__cant_select_repository__solution_step_2.png)

1. **W niebieskiej ramce w sekcji `Private access` kliknij `Connect here`**
![](./assets/streamlit_community_cloud__cant_select_repository__solution_step_3.png)

1. **Następnie kliknij zielony przycisk `Authorize streamlit`**
![](./assets/streamlit_community_cloud__cant_select_repository__solution_step_4.png)

1. **Potwierdź wpisując hasło do konta GitHub i kliknij zielony przycisk `Confirm`**
![](./assets/streamlit_community_cloud__cant_select_repository__solution_step_5.png)

1. Po wykonaniu tych operacji kiedy **odświeżymy stronę** i klikniemy w pole tekstowe `Repository`, wyświetli się nam link do naszego repozytorium ( lub repozytoriów jeśli jest
ich więcej)
![](./assets/streamlit_community_cloud__cant_select_repository__solution_step_6.png)