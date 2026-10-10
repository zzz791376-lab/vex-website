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
                    return "data:" + mime + ";base64," + base64.b64encode(img_file.read()).decode()
            except Exception:
                pass
    return "https://cdn-icons-png.flaticon.com/512/808/808439.png"

logo_style = get_logo_base64()

# Check Login Status via Query Parameters
if "login" in st.query_params:
    st.session_state.logged_in = True

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"

# 2. Modern Ultra-Red Dark Theme CSS & FiveM Banner Styling
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
section[data-testid="stSidebar"] {
    background-color: rgba(11, 14, 20, 0.98) !important;
    border-right: 1px solid #1f293d;
    padding-top: 15px;
}

section[data-testid="stSidebar"] div.stButton > button {
    width: 100% !important;
    background: rgba(18, 22, 32, 0.9) !important;
    color: #e2e8f0 !important;
    border: 1px solid #1f293d !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    text-align: left !important;
    justify-content: flex-start !important;
    transition: all 0.3s ease !important;
    margin-bottom: 4px !important;
    box-shadow: none !important;
}

section[data-testid="stSidebar"] div.stButton > button:hover {
    border-color: #ff1e38 !important;
    background: rgba(255, 30, 56, 0.15) !important;
    color: #ffffff !important;
    transform: translateX(4px) !important;
}

/* شريط التنقل العلوي الفخم */
.top-navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(11, 14, 20, 0.95);
    border: 1px solid #1f293d;
    border-radius: 16px;
    padding: 12px 25px;
    margin-bottom: 25px;
    backdrop-filter: blur(10px);
}

.top-nav-links {
    display: flex;
    gap: 30px;
    align-items: center;
}

.top-user-box {
    display: flex;
    align-items: center;
    gap: 15px;
}

.user-pill {
    background: rgba(18, 22, 32, 0.9);
    border: 1px solid #1f293d;
    border-radius: 12px;
    padding: 8px 15px;
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 13px;
    font-weight: bold;
    color: #ffffff;
}

.logout-btn {
    background: rgba(230, 0, 35, 0.15);
    border: 1px solid #ff1e38;
    color: #ff1e38 !important;
    padding: 8px 18px;
    border-radius: 12px;
    font-weight: bold;
    font-size: 13px;
    text-decoration: none;
    transition: all 0.3s ease;
}

.logout-btn:hover {
    background: #ff1e38;
    color: #ffffff !important;
}

/* Hero Banner Card With FiveM / GTA V Car Background Image */
.hero-banner {
    background: linear-gradient(90deg, rgba(8, 10, 15, 0.96) 0%, rgba(8, 10, 15, 0.82) 55%, rgba(8, 10, 15, 0.4) 100%), 
                url('https://images.unsplash.com/photo-1552519507-da3b142c6e3d?q=80&w=1600&auto=format&fit=crop') center/cover no-repeat;
    border: 1px solid rgba(255, 30, 56, 0.4);
    border-radius: 24px;
    padding: 50px 45px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.8), inset 0 0 50px rgba(0,0,0,0.5);
    position: relative;
    overflow: hidden;
    margin-bottom: 25px;
}

.hero-portal-badge {
    display: inline-block;
    background: rgba(255, 30, 56, 0.15);
    border: 1px solid #ff1e38;
    color: #ff1e38;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 2px;
    padding: 6px 16px;
    border-radius: 30px;
    margin-bottom: 15px;
}

.hero-title {
    font-size: 48px;
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

.hero-stats-row {
    display: flex;
    gap: 40px;
    margin-top: 40px;
    padding-top: 25px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.stat-item {
    display: flex;
    flex-direction: column;
}
.stat-value {
    font-size: 22px;
    font-weight: 900;
    color: #ffffff;
}
.stat-label {
    font-size: 11px;
    color: #64748b;
    font-weight: 700;
    letter-spacing: 1px;
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
.glass-card {
    background: rgba(14, 17, 23, 0.85);
    backdrop-filter: blur(12px);
    border: 1px solid #1f293d;
    border-radius: 20px;
    padding: 35px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    margin-bottom: 25px;
    min-height: 280px;
}
.code-ip-box {
    background: #090c10;
    border: 1px solid #ff1e38;
    border-radius: 12px;
    padding: 15px 20px;
    font-family: monospace;
    font-size: 16px;
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
    border-color: #ff1e38 !important;
}
</style>
""", unsafe_allow_html=True)

# --- LOGIN / WELCOME GATEWAY ---
if not st.session_state.logged_in:
    login_html = (
        '<div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; display: flex; justify-content: center; align-items: center; z-index: 99999;">'
        '<div style="background: rgba(14, 17, 23, 0.90); backdrop-filter: blur(15px); border: 1px solid #1f293d; border-radius: 24px; padding: 40px; width: 460px; text-align: center; box-shadow: 0 25px 60px rgba(0,0,0,0.9);">'
        f'<img src="{logo_style}" style="max-width: 170px; max-height: 110px; object-fit: contain; margin-bottom: 15px; filter: drop-shadow(0 0 15px rgba(255, 30, 56, 0.6));">'
        '<div style="color: #ff1e38; font-size: 11px; font-weight: 900; letter-spacing: 3px; margin-bottom: 10px;">VILLAGE RF COMMUNITY PORTAL</div>'
        '<h1 style="color: #ffffff; font-size: 30px; font-weight: 900; margin-bottom: 10px;">Enter the <span style="color: #ff1e38;">VILLAGE</span> world.</h1>'
        '<p style="color: #64748b; font-size: 13px; line-height: 1.5; margin-bottom: 25px;">Connect your Discord account to access the official website and verify your community access.</p>'
        '<a href="?login=true" target="_self" class="btn-discord-login">🔗 Continue with Discord ➔</a>'
        '</div></div>'
    )
    st.markdown(login_html, unsafe_allow_html=True)
    st.stop()

# --- MAIN WEBSITE (After Login) ---

# 3. Sidebar Navigation
with st.sidebar:
    st.markdown(
        f'<div style="text-align: center; margin-bottom: 20px;">'
        f'<img src="{logo_style}" style="max-width: 110px; max-height: 75px; object-fit: contain; filter: drop-shadow(0 0 12px rgba(255, 30, 56, 0.6));">'
        f'</div>',
        unsafe_allow_html=True
    )
    st.markdown('<p style="color: #ff1e38; font-size: 11px; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 15px; padding-left: 5px;">MAIN MENU</p>', unsafe_allow_html=True)
    
    pages = {
        "Home": "🏠  Home",
        "Server": "🖥️  Server",
        "Staff Team": "👥  Staff Team",
        "Rules": "📜  Rules",
        "Events": "🎉  Events",
        "Staff Application": "📝  Staff Application",
        "Discord": "💬  Discord"
    }
    
    for key, label in pages.items():
        is_active = (st.session_state.active_page == key)
        btn_style = (
            "border: 1px solid #ff1e38 !important; "
            "background: linear-gradient(135deg, rgba(230, 0, 35, 0.35) 0%, rgba(255, 30, 56, 0.5) 100%) !important; "
            "box-shadow: 0 0 15px rgba(255, 30, 56, 0.3) !important;"
        ) if is_active else ""
        
        if is_active:
            st.markdown(f'<style>div[data-testid="stSidebar"] div.stButton > button[kind="secondary"][key*="{key}"] {{ {btn_style} }}</style>', unsafe_allow_html=True)

        if st.button(label, key=f"sidebar_btn_{key}"):
            st.session_state.active_page = key
            st.rerun()

    st.markdown("---")
    st.markdown(
        '<div style="background: rgba(18, 22, 32, 0.85); padding: 15px; border-radius: 14px; border: 1px solid #1f293d; text-align: center;">'
        '<div style="color: #ff1e38; font-weight: bold; font
