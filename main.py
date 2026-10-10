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

# 2. Modern Ultra-Red Dark Theme CSS & Clean Sidebar Buttons
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

/* القضاء النهائي على الخلفيات البيضاء وجعل الأزرار داكنة وفخمة 100% */
div[data-testid="stSidebar"] div.stButton > button {
    width: 100% !important;
    background: rgba(18, 22, 32, 0.85) !important;
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

div[data-testid="stSidebar"] div.stButton > button:hover {
    border-color: #ff1e38 !important;
    background: rgba(255, 30, 56, 0.15) !important;
    color: #ffffff !important;
    transform: translateX(4px) !important;
}

div[data-testid="stSidebar"] div.stButton > button:focus,
div[data-testid="stSidebar"] div.stButton > button:active {
    border-color: #ff1e38 !important;
    background: linear-gradient(135deg, rgba(230, 0, 35, 0.35) 0%, rgba(255, 30, 56, 0.45) 100%) !important;
    color: #ffffff !important;
    box-shadow: 0 4px 15px rgba(255, 30, 56, 0.3) !important;
}

.hero-title {
    font-size: 46px;
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

# 3. Sidebar Navigation (Pure Clean Buttons - NO Circles)
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
        if st.button(label, key=f"menu_btn_{key}"):
            st.session_state.active_page = key

    st.markdown("---")
    st.markdown(
        '<div style="background: rgba(18, 22, 32, 0.85); padding: 15px; border-radius: 14px; border: 1px solid #1f293d; text-align: center;">'
        '<div style="color: #ff1e38; font-weight: bold; font-size: 13px;">🔴 VILLAGE RF</div>'
        '<div style="color: #00ff88; font-size: 11px; font-weight: bold; margin-top: 4px;">● Server online — LIVE</div>'
        '</div>',
        unsafe_allow_html=True
    )

# 4. Main Content Pages
page = st.session_state.active_page

if page == "Home":
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            '<div class="glass-card">'
            '<span class="hero-tag">🔴 OFFICIAL COMMUNITY PORTAL • VILLAGE RF / 2026</span>'
            '<h1 class="hero-title">VILLAGE RF</h1>'
            '<p style="color: #ff1e38; font-weight: bold; font-size: 16px; margin-top: -5px;">MORE THAN JUST A SERVER.</p>'
            '<p style="color: #94a3b8; font-size: 14px; line-height: 1.6;">Welcome to the official VILLAGE RF community portal. Stay connected, check the latest events, meet the team and keep your Discord access verified.</p>'
            '<div style="margin-top: 25px;">'
            '<a href="https://discord.gg/WC9NFNVFS" target="_blank" class="btn-action">Join Community ➔</a>'
            '</div></div>',
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            '<div class="glass-card">'
            '<h2 style="color: white; margin-bottom: 5px; font-size: 24px;">🖥️ Direct Connect IP</h2>'
            '<p style="color: #64748b; font-size: 14px;">Quick launch directly via FiveM application.</p>'
            '<div class="code-ip-box">'
            '<span>connect 217.160.240.61</span>'
            '<span style="color: #ff1e38; font-size: 12px; font-weight: bold;">[ONLINE]</span>'
            '</div>'
            '<a href="fivem://connect/217.160.240.61" class="btn-action">Connect Server 🚀</a>'
            '</div>',
            unsafe_allow_html=True
        )

elif page == "Server":
    st.markdown(
        '<div class="glass-card">'
        '<h2 style="color: white; margin-bottom: 5px;">🖥️ Direct Connect IP</h2>'
        '<p style="color: #64748b; font-size: 14px;">Copy the IP below or launch directly via FiveM application.</p>'
        '<div class="code-ip-box">'
        '<span>connect 217.160.240.61</span>'
        '<span style="color: #ff1e38; font-size: 12px; font-weight: bold;">[LIVE ONLINE]</span>'
        '</div>'
        '<a href="fivem://connect/217.160.240.61" class="btn-action">Connect Directly to FiveM 🚀</a>'
        '</div>',
        unsafe_allow_html=True
    )

elif page == "Staff Team":
    st.header("👥 Staff Team — VILLAGE RF")
    st.caption("Meet our official management and leadership team.")
    st.write("---")
    
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    
    with c1:
        st.markdown("""<div class="card-box"><div class="role-badge">👑 OWNER</div><div class="staff-title">! Haroun.13K</div><div class="staff-sub">@off_marseille</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card-box"><div class="role-badge">👑 FOUNDER</div><div class="staff-title">ADLANE HB</div><div class="staff-sub">@adlanehb</div></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="card-box"><div class="role-badge">🟣 CO-OWNER</div><div class="staff-title">SIDO</div><div class="staff-sub">@sido_sido_18</div></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""<div class="card-box"><div class="role-badge">⭐ MANAGER</div><div class="staff-title">Johane</div><div class="staff-sub">@yb.johane</div></div>""", unsafe_allow_html=True)
    with c5:
        st.markdown("""<div class="card-box"><div class="role-badge">🔵 DEV</div><div class="staff-title">ZR</div><div class="staff-sub">@zr_rr011</div></div>""", unsafe_allow_html=True)
    with c6:
        st.markdown("""<div class="card-box"><div class="role-badge">🔵 DEV</div><div class="staff-title">PIROx99.</div><div class="staff-sub">@piro.fps20.</div></div>""", unsafe_allow_html=True)
    with c7:
        st.markdown("""<div class="card-box"><div class="role-badge">⭐ DEV DISCORD</div><div class="staff-title">ZAKI VEX</div><div class="staff-sub">@closedaccount1_</div></div>""", unsafe_allow_html=True)

elif page == "Rules":
    st.markdown(
        '<div class="glass-card">'
        '<h2 style="color: white; margin-bottom: 20px;">📜 Server Guidelines & Rules</h2>'
        '<div class="rule-card"><b>1. Respect All Members:</b> Toxic behavior, racism, and harassment are strictly prohibited.</div>'
        '<div class="rule-card"><b>2. No RDM / VDM:</b> Random Killing or using vehicles as weapons is strictly forbidden.</div>'
        '<div class="rule-card"><b>3. Value Your Life (Fear RP):</b> You must value your character\'s life at all times during Roleplay scenarios.</div>'
        '</div>',
        unsafe_allow_html=True
    )

elif page == "Events":
    st.markdown(
        '<div class="glass-card">'
        '<h2 style="color: white; margin-bottom: 10px;">🎉 Upcoming Events</h2>'
        '<p style="color: #94a3b8;">Stay tuned for the official VILLAGE RF launch and community events!</p>'
        '</div>',
        unsafe_allow_html=True
    )

elif page == "Staff Application":
    st.markdown('<div class="glass-card"><h2 style="color: white; margin-bottom: 15px;">📝 Staff Application</h2>', unsafe_allow_html=True)
    st.text_input("Discord Tag (e.g. zaki_vex)")
    st.text_area("Why do you want to join VILLAGE RF Staff Team?")
    if st.button("Submit Application ➔"):
        st.success("Your application has been submitted successfully!")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Discord":
    st.markdown(
        '<div class="glass-card" style="text-align: center;">'
        '<h2 style="color: white; margin-bottom: 10px;">💬 VILLAGE RF Discord Server</h2>'
        '<p style="color: #64748b; margin-bottom: 25px;">Click below to join our official active Discord server and stay up to date!</p>'
        '<a href="https://discord.gg/WC9NFNVFS" target="_blank" class="btn-action">Open Discord Invite ➔</a>'
        '</div>',
        unsafe_allow_html=True
    )
