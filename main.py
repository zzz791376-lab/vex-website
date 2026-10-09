import streamlit as st
import base64
import os

# 1. Konfiguracja strony
st.set_page_config(
    page_title="VILLAGE RF — Official Portal",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Funkcja kodowania banera
def get_base64_image(image_path):
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
    except Exception:
        return None
    return None

img_b64 = get_base64_image("banner.jpg")
bg_style = f"data:image/jpeg;base64,{img_b64}" if img_b64 else "https://images.alphacoders.com/131/1318498.jpeg"

# 2. Styl Ciemny CSS (Jednolinijkowe, bezpieczne reguły)
css_code = (
    "<style>"
    "#MainMenu, header, footer, div[data-testid='stDecoration'], div[data-testid='stToolbar'] { display: none !important; }"
    ".stApp { background-color: #0b0e14; color: #ffffff; }"
    "section[data-testid='stSidebar'] { background-color: #11151c !important; border-right: 1px solid #1e2430; }"
    "div[role='radiogroup'] label div[data-testid='stRadioButtonCustomIcon'], div[role='radiogroup'] label input[type='radio'] { display: none !important; }"
    "div[role='radiogroup'] > label { background: #161b22; padding: 12px 18px; border-radius: 12px; margin-bottom: 8px; border: 1px solid #21262d; transition: all 0.3s ease; cursor: pointer; }"
    "div[role='radiogroup'] > label:hover { border-color: #0088ff; background: #1c212a; }"
    "div[role='radiogroup'] label p { color: #cbd5e1 !important; font-size: 15px !important; font-weight: 600; }"
    ".hero-title { font-size: 52px; font-weight: 900; color: #ffffff; margin: 5px 0; letter-spacing: 2px; }"
    ".hero-tag { color: #0088ff; font-weight: bold; font-size: 13px; letter-spacing: 2px; }"
    ".btn-action { display: inline-block; background: linear-gradient(90deg, #0066ff 0%, #00a2ff 100%); color: white !important; text-decoration: none !important; border-radius: 12px; padding: 12px 28px; font-weight: bold; margin-right: 15px; }"
    ".btn-secondary-action { display: inline-block; background: #161b22; color: #ffffff !important; text-decoration: none !important; border: 1px solid #21262d; border-radius: 12px; padding: 12px 28px; font-weight: bold; }"
    ".staff-card {
