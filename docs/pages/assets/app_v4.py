
import streamlit as st
import pandas as pd  # type: ignore
import psycopg2  # type: ignore
from datetime import datetime, timezone
from openai import OpenAI
from st_paywall import add_auth  # type: ignore

openai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


FREE_USER_MAX_INPUT_TOKENS = 1000
FREE_USER_MAX_OUTPUT_TOKENS = 10000
PREMIUM_USER_MAX_INPUT_TOKENS = 10000
PREMIUM_USER_MAX_OUTPUT_TOKENS = 100000

#
# database & openai
#
def get_connection():
    return psycopg2.connect(
        dbname=st.secrets["database"],
        user=st.secrets["username"],
        password=st.secrets["password"],
        host=st.secrets["host"],
        port=st.secrets["port"],
        sslmode=st.secrets["sslmode"]
    )


def insert_usage(email, output_tokens, input_tokens, input_text):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO usages2 (google_user_email, output_tokens, input_tokens, input_text) VALUES (%s, %s, %s, %s)
            """, (email, output_tokens, input_tokens, input_text))
            conn.commit()


def get_current_month_usage_df(email):
    with get_connection() as conn:
        now = datetime.now(timezone.utc)
        start_date = datetime(now.year, now.month, 1)
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM usages2 WHERE google_user_email = %s AND created_at >= %s", (email, start_date))
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            df_usage = pd.DataFrame(rows, columns=columns)

    return df_usage


def create_story(story_prompt):
    if not st.user.is_logged_in:
        raise Exception("User is not logged in")

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """
                    Jesteś opowiadaczem historii.
                    Twórz krótkie opowiadania na podstawie podanego tekstu.
                    Opowiadania powinny być wciągające i zaskakujące.
                    Mają być zbudowane wokół struktury:
                    - wstęp
                    - rozwinięcie
                    - zakończenie

                    Opowiadanie nie powinno być krótsze niż 100 słów.
                """
            },
            {"role": "user", "content": story_prompt}
        ]
    )
    usage = {}
    if response.usage:
        usage = {
            "completion_tokens": response.usage.completion_tokens,
            "prompt_tokens": response.usage.prompt_tokens,
            "total_tokens": response.usage.total_tokens,
        }

    insert_usage(
        email=st.user.email,
        output_tokens=usage['completion_tokens'],
        input_tokens=usage['prompt_tokens'],
        input_text=story_prompt,
    )

    return {
        "role": "assistant",
        "content": response.choices[0].message.content,
        "usage": usage,
    }


def allow_usage():
    is_free_user = not st.session_state.get("user_subscribed")
    email = st.user.email

    if not email:
        raise Exception("User is not logged in")

    usage_df = get_current_month_usage_df(email)
    used_input_tokens = usage_df['input_tokens'].sum()
    used_output_tokens = usage_df['output_tokens'].sum()

    if is_free_user:
        if used_input_tokens >= FREE_USER_MAX_INPUT_TOKENS or used_output_tokens >= FREE_USER_MAX_OUTPUT_TOKENS:
            return False, "Przekroczono limit tokenów, subskrybuj naszą usługę, aby móc generować więcej opowiadań."

    else:
        if used_input_tokens >= PREMIUM_USER_MAX_INPUT_TOKENS or used_output_tokens >= PREMIUM_USER_MAX_OUTPUT_TOKENS:
            return False, "Przekroczono limit tokenów, poczekaj do końca miesiąca."

    return True, ""


#
# MAIN
#
_, c, _ = st.columns([2, 2, 2])
with c:
    st.image("logo.png")

st.title("Generator krótkich opowiadań 📖")
st.write("""
Użyj tej aplikacji, aby wygenerować krótkie opowiadania. Wprowadź swój tekst w poniższym polu tekstowym,
a następnie kliknij przycisk 'Generuj'. ✨
""")

# Handle Streamlit's native authentication
with st.sidebar:
    if not st.user.is_logged_in:
        st.button("Zaloguj się", on_click=st.login, use_container_width=True)
    else:
        st.button("Wyloguj się", on_click=st.logout, use_container_width=True)

if st.user.is_logged_in:
    try:
        add_auth(
            required=False,
            use_sidebar=True,
            subscription_button_text="Zostań PREMIUM",
        )
    except KeyError:
        pass

# Sprawdź czy użytkownik jest zalogowany
if st.user.is_logged_in:
    allow, msg = allow_usage()
    if not allow:
        st.error(msg)

    else:
        st.session_state['user_input'] = st.text_area("Wprowadź swój tekst:", max_chars=1000)
        if st.button("Generuj 🚀", disabled=not st.session_state['user_input'].strip(), use_container_width=True):
            st.session_state['story'] = create_story(st.session_state['user_input'])

        if st.session_state.get('story'):
            st.write("### Twoje wygenerowane opowiadanie:")
            st.write(st.session_state['story']['content'])

            st.download_button(
                label="Pobierz wygenerowane opowiadanie",
                data=st.session_state['story']['content'],
                file_name="wygenerowane_opowiadanie.txt",
                mime="text/plain",
                use_container_width=True,
            )

with st.sidebar:
    st.image("logo.png", width=150)
    st.title("Generator krótkich opowiadań 📖")
    st.link_button("Polityka prywatności", "https://od-zera-do-ai-assets.fra1.cdn.digitaloceanspaces.com/privacy_policy.pdf")
    st.link_button("Regulamin", "https://od-zera-do-ai-assets.fra1.cdn.digitaloceanspaces.com/regulations.pdf")

    if st.user.is_logged_in:
        account, stats = st.tabs(["Konto", "Statystyki"])

        with account:
            st.write(f"Jesteś zalogowano jako: {st.user.email}")
            st.write(f"Aktywna subskrypcja: {'**PREMIUM**' if st.session_state.get('user_subscribed') else '**FREE**'}")

        with stats:
            usage_df = get_current_month_usage_df(st.user.email)
            st.write(f"W tym miesiącu użyłeś")

            max_input_tokens = FREE_USER_MAX_INPUT_TOKENS if not st.session_state.get("user_subscribed") else PREMIUM_USER_MAX_INPUT_TOKENS
            st.metric("Input tokenów", f"{usage_df['input_tokens'].sum()} / {max_input_tokens}")

            max_output_tokens = FREE_USER_MAX_OUTPUT_TOKENS if not st.session_state.get("user_subscribed") else PREMIUM_USER_MAX_OUTPUT_TOKENS
            st.metric("Output tokenów", f"{usage_df['output_tokens'].sum()} / {max_output_tokens}")
            