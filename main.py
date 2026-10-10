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

# Function to encode local images
def get_base64_image(image_path):
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
    except Exception:
        return None
    return None

banner_b64 = get_base64_image("banner.jpg")
logo_b64 = get_base64_image("logo.png")

bg_style = f"data:image/jpeg;base64,{banner_b64}" if banner_b64 else "https://images.alphacoders.com/131/1318498.jpeg"
logo_style = f"data:image/png;base64,{logo_b64}" if logo_b64 else "https://cdn-icons-png.flaticon.com/512/124/124010.png"

# Session State for Authentication / Entry
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 2. CSS Styles
st.markdown("""
<style>
#MainMenu, header, footer, div[data-testid="stDecoration"], div[data-testid="stToolbar"] {
    display: none !important;
}
.stApp {
    background-color: #0b0e14;
    color: #ffffff;
}
section[data-testid="stSidebar"] {
    background-color: #11151c !important;
    border-right: 1px solid #1e2430;
}
div[role="radiogroup"] label div[data-testid="stRadioButtonCustomIcon"],
div[role="radiogroup"] label input[type="radio"] {
    display: none !important;
}
div[role="radiogroup"] > label {
    background: #161b22;
    padding: 12px 18px;
    border-radius: 12px;
    margin-bottom: 8px;
    border: 1px solid #21262d;
    cursor: pointer;
}
div[role="radiogroup"] > label:hover {
    border-color: #0088ff;
    background: #1c212a;
}
div[role="radiogroup"] label p {
    color: #cbd5e1 !important;
    font-size: 15px !important;
    font-weight: 600;
}
.hero-title {
    font-size: 52px;
    font-weight: 900;
    color: #ffffff;
    margin: 5px 0;
}
.hero-tag {
    color: #0088ff;
    font-weight: bold;
    font-size: 13px;
}
.btn-action {
    display: inline-block;
    background: linear-gradient(90deg, #0066ff 0%, #00a2ff 100%);
    color: white !important;
    text-decoration: none !important;
    border-radius: 12px;
    padding: 12px 28px;
    font-weight: bold;
    margin-right: 15px;
    box-shadow: 0 4px 15px rgba(0, 102, 255, 0.4);
}
.btn-secondary-action {
    display: inline-block;
    background: #161b22;
    color: #ffffff !important;
    text-decoration: none !important;
    border: 1px solid #21262d;
    border-radius: 12px;
    padding: 12px 28px;
    font-weight: bold;
}
.card-box {
    background-color: #161b22;
    border: 1px solid #21262d;
    border-radius: 12px;
    padding: 15px 8px;
    text-align: center;
    margin-bottom: 15px;
    min-height: 110px;
}
.role-badge {
    color: #00a2ff;
    font-size: 11px;
    font-weight: bold;
}
.staff-title {
    color: #ffffff;
    font-size: 14px;
    font-weight: bold;
    margin-top: 6px;
    word-break: break-word;
}
.staff-sub {
    color: #64748b;
    font-size: 11px;
    margin-top: 2px;
    word-break: break-word;
}
</style>
""", unsafe_allow_html=True)

# --- LOGIN / WELCOME GATEWAY ---
if not st.session_state.logged_in:
    st.markdown(f"""
    <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: linear-gradient(180deg, rgba(11, 14, 20, 0.85) 0%, rgba(11, 14, 20, 0.95) 100%), url('{bg_style}'); background-size: cover; background-position: center; display: flex; justify-content: center; align-items: center; z-index: 99999;">
        <div style="background: #11151c; border: 1px solid #1e293b; border-radius: 24px; padding: 40px; width: 480px; text-align: center; box-shadow: 0 20px 50px rgba(0,0,0,0.8);">
            <img src="{logo_style}" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; margin-bottom: 15px; border: 2px solid #0088ff;">
            <div style="color: #0088ff; font-size: 12px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px;">VILLAGE RF COMMUNITY PORTAL</div>
            <h1 style="color: #ffffff; font-size: 32px; font-weight: 900; margin-bottom: 10px;">Enter the <span style="color: #0088ff;">VILLAGE</span> world.</h1>
            <p style="color: #64748b; font-size: 13px; line-height: 1.5; margin-bottom: 20px;">Connect your Discord account to access the official website and verify your community access.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st
