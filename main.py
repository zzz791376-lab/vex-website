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

# Function to search and encode logo dynamically
def get_logo_base64():
    for ext in ["vilag2.png", "logo.png", "logo.jpg", "logo.jpeg", "vilag3.png"]:
        if os.path.exists(ext):
            try:
                with open(ext, "rb") as img_file:
                    mime = "image/png" if ext.endswith(".png") else "image/jpeg"
                    return f"data:{mime};base64," + base64.b64encode(img_file.read()).decode()
            except Exception:
                pass
    return "https://cdn-icons-png.flaticon.com/512/808/808439.png"

logo_style = get_logo_base64()

# Check Login Status via Query Parameters
if "login" in st.query_params:
    st.session_state.logged_in = True

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 2. Modern Ultra-Red Theme CSS & Styles
st.markdown("""
<style>
#MainMenu, header, footer, div[data-testid="stDecoration"], div[data-testid="stToolbar"] {
    display: none !important;
}
.stApp {
    background: linear-gradient(180deg, rgba(8, 10, 15, 0.88) 0%, rgba(8, 10, 15, 0.96) 100%), 
                url('https://i.gifer.com/76YS.gif') center/cover no-repeat fixed !important;
    color: #ffffff;
}
/* Enhanced Modern Sidebar & Hide Radio Circles Completely */
section[data-testid="stSidebar"] {
    background-color: rgba(11, 14, 20, 0.95) !important;
    border-right: 1px solid #1f293d;
    padding-top: 10px;
}
div[role="radiogroup"] {
    gap: 8px;
}
/* إخفاء الأيقونات الدائرية والدوائر البيضاء نهائياً */
div[role="radiogroup"] label div[data-testid="stRadioButtonCustomIcon"],
div[role="radiogroup"] label input[type="radio"],
div[role="radiogroup"] label span[class*="st-"] {
    display: none !important;
    width: 0px !important;
    height: 0px !important;
    visibility: hidden !important;
}
div[role="radiogroup"] > label {
    background: rgba(18, 22, 32, 0.7);
    padding: 12px 18px !important;
    border-radius: 12px;
    border: 1px solid #1f293d;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex !important;
    align-items: center !important;
}
div[role="radiogroup"] > label:hover {
    border-color: #ff1e38;
    background: rgba(255, 30, 56, 0.1);
    transform: translateX(4px);
}
div[role="radiogroup"] > label[data-checked="true"] {
    border-color: #ff1e38;
    background: linear-gradient(135deg, rgba(230, 0, 35, 0.25) 0%, rgba(255, 30, 56, 0.35) 100%);
    box-shadow: 0 4px 15px rgba(255, 30, 56, 0.25);
}
div[role="radiogroup"] label p {
    color: #e2e8f0 !important;
    font-size: 15px !important;
    font-weight: 700;
    margin: 0 !important;
}
.hero-title {
    font-size: 56px;
    font-weight: 900;
    color: #ffffff;
    margin: 5px 0;
    text-shadow: 0 5px 25px rgba(255, 30, 56, 0.4);
}
.hero-tag {
    color: #ff1e38;
    font-weight: 800;
    font-size: 13px;
    letter-spacing: 1px;
}
.btn-action {
    display: inline-block;
    background: linear-gradient(135deg, #e60023 0%, #ff1e38 100%);
    color: white !important;
    text-decoration: none !important;
    border-radius: 12px;
    padding: 12px 28px;
    font-weight: bold;
    margin-right: 15px;
    box-shadow: 0 4px 20px rgba(230, 0, 35, 0.5);
    transition: all 0.3s ease;
}
.btn-action:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(255, 30, 56, 0.7);
}
.btn-secondary-action {
    display: inline-block;
    background: #121620;
    color: #ffffff !important;
    text-decoration: none !important;
    border: 1px solid #1f293d;
    border-radius: 12px;
    padding: 12px 28px;
    font-weight: bold;
    transition: all 0.3s ease;
}
.btn-secondary-action:hover {
    border-color: #ff1e38;
    background: #1b1216;
}
.card-box {
    background-color: rgba(18, 22, 32, 0.9);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 30, 56, 0.3);
    border-radius: 16px;
    padding: 18px 8px;
    text-align: center;
    margin-bottom: 15px;
    min-height: 120px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    transition: all 0.3s ease;
}
.card-box:hover {
    border-color: #ff1e38;
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(255, 30, 56, 0.3);
}
.role-badge {
    color: #ff1e38;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 0.5px;
}
.staff-title {
    color: #ffffff;
    font-size: 14px;
    font-weight: bold;
    margin-top: 6px;
    word-break: break-word;
}
.staff-sub {
    color: #94a3b8;
    font-size: 11px;
    margin-top: 2px;
    word-break: break-word;
}
.btn-discord-login {
    display: block;
    width: 100%;
    background: linear-gradient(135deg, #e60023 0%, #ff1e38 100%);
    color: #ffffff !important;
    text-decoration: none !important;
    font-weight: bold;
    font-size: 15px;
    padding: 14px 20px;
    border-radius: 14px;
    box-shadow: 0 4px 25px rgba(230, 0, 35, 0.5);
    text-align: center;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
}
.btn-discord-login:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 30px rgba(255, 30, 56, 0.8);
}
.glass-card {
    background: rgba(14, 17, 23, 0.85);
    backdrop-filter: blur(12px);
    border: 1px solid #1f293d;
    border-radius: 20px;
    padding: 35px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    margin-bottom: 25px;
}
.code-ip-box {
    background: #090c10;
    border: 1px solid #ff1e38;
    border-radius: 12px;
    padding: 15px 20px;
    font-family: monospace;
    font-size: 18px;
    color: #00ff88;
    margin: 15px 0 25px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 0 15px rgba(255, 30, 56, 0.2);
}
.rule-card {
    background: rgba(18, 22, 32, 0.85);
    border-left: 4px solid #ff1e38;
    border-radius: 10px;
    padding: 15px 20px;
    margin-bottom: 12px;
    font-size: 15px;
}
div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > div {
    background-color: #090c10 !important;
    border: 1px solid #1f293d !important;
    color: white !important;
    border-radius: 10px !important;
}
div[data-baseweb="input"] > div:focus-within, div[data-baseweb="textarea"] > div:focus-within {
    border-color:
