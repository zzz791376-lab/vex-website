import streamlit as st
import base64
import os

# 1. Page Config
st.set_page_config(
    page_title="VILLAGE RF — Official Portal",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to encode local banner
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

# 2. Premium Dark CSS Injection
css_lines = [
    "<style>",
    "#MainMenu, header, footer, div[data-testid='stDecoration'], div[data-testid='stToolbar'] { display: none !important; }",
    ".stApp { background-color: #0b0e14; color: #ffffff; }",
    "section[data-testid='stSidebar'] { background-color: #11151c !important; border-right: 1px solid #1e2430; }",
    "div[role='radiogroup'] label div[data-testid='stRadioButtonCustomIcon'], div[role='radiogroup'] label input[type='radio'] { display: none !important; }",
    "div[role='radiogroup'] > label { background: #161b22; padding: 12px 18px; border-radius: 12px; margin-bottom: 8px; border: 1px solid #21262d; transition: all 0.3s ease; cursor: pointer; }",
    "div[role='radiogroup'] > label:hover { border-color: #0088ff; background: #1c212a; transform: translateX(4px); }",
    "div[role='radiogroup'] label p { color: #cbd5e1 !important; font-size: 15px !important; font-weight: 600; }",
    ".hero-title { font-size: 52px; font-weight: 900; color: #ffffff; margin: 5px 0; letter-spacing: 2px; text-shadow: 0 4px 20px rgba(0,0,0,0.9); }",
    ".hero-tag { color: #0088ff; font-weight: bold; font-size: 13px; letter-spacing: 2px; text-shadow: 0 2px 10px rgba(0,136,255,0.4); }",
    ".btn-action { display: inline-block; background: linear-gradient(90deg, #0066ff 0%, #00a2ff 100%); color: white !important; text-decoration: none !important; border-radius: 12px; padding: 12px 28px; font-weight: bold; margin-right: 15px; box-shadow: 0 4px 15px rgba(0, 102, 255, 0.4); transition: all 0.3s ease; }",
    ".btn-action:hover { transform: translateY(-2px); box-shadow: 0 6px 25px rgba(0, 136, 255, 0.7); }",
    ".btn-secondary-action { display: inline-block; background: #161b22; color: #ffffff !important; text-decoration: none !important; border: 1px solid #21262d; border-radius: 12px; padding: 12px 28px; font-weight: bold; transition: all 0.3s ease; }",
    ".btn-secondary-action:hover { border-color: #0088ff; background: #1c212a; transform: translateY(-2px); }",
    ".staff-card { background: linear-gradient(145deg, #11151c 0%, #161b22 100%); border: 1px solid #1e293b; border-radius: 18px; padding: 25px 15px; text-align: center; margin-bottom: 20px; transition: all 0.3s ease; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4); }",
    ".staff-card:hover { border-color: #0088ff; transform: translateY(-6px); box-shadow: 0 12px 28px rgba(0, 136, 255, 0.3); }",
    ".staff-card-owner { border: 1px solid rgba(0, 136, 255, 0.4); background: linear-gradient(145deg, #131b2e 0%, #11151c 100%); }",
    ".staff-role { display: inline-block; font-size: 11px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; background: rgba(0, 136, 255, 0.12); color: #00a2ff; padding: 6
