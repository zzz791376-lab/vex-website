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

# 2. Modern Red Theme CSS & Full Animated Background Styles
st.markdown("""
<style>
#MainMenu, header, footer, div[data-testid="stDecoration"], div[data-testid="stToolbar"] {
    display: none !important;
}
/* خلفية متحركة شاملة لكل صفحات الموقع مع طبقة عتمة حمراء داكنة فخمة */
.stApp {
    background: linear-gradient(180deg, rgba(8, 10, 15, 0.85) 0%, rgba(8, 10, 15, 0.94) 100%), 
                url('https://i.gifer.com/76YS.gif') center/cover no-repeat fixed !important;
    color: #ffffff;
}
section[data-testid="stSidebar"] {
    background-color: rgba(14, 17, 23, 0.92) !important;
    border-right: 1px solid #1a202c;
}
div[role="radiogroup"] label div[data-testid="stRadioButtonCustomIcon"],
div[role="radiogroup"] label input[type="radio"] {
    display: none !important;
}
div[role="radiogroup"] > label {
    background: #121620;
    padding: 12px 18px;
    border-radius: 14px;
    margin-bottom: 8px;
    border: 1px solid #1f293d;
    cursor: pointer;
    transition: all 0.3s ease;
}
div[role="radiogroup"] > label:hover {
    border-color: #ff1e38;
    background: #1b1216;
}
div[role="radiogroup"] label p {
    color: #cbd5e1 !important;
    font-size: 15px !important;
    font-weight: 600;
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
    background-color: rgba(18, 22, 32, 0.85);
    backdrop-filter: blur(10px);
    border: 1px solid #1f293d;
    border-radius: 16px;
    padding: 18px 8px;
    text-align: center;
    margin-bottom: 15px;
    min-height: 120px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    transition: all 0.3s ease;
}
.card-box:hover {
    border-color: #ff1e38;
    transform: translateY(-3px);
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
    color: #64748b;
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
</style>
""", unsafe_allow_html=True)

# --- LOGIN / WELCOME GATEWAY ---
if not st.session_state.logged_in:
    login_html = (
        f'<div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; display: flex; justify-content: center; align-items: center; z-index: 99999;">'
        f'<div style="background: rgba(14, 17, 23, 0.90); backdrop-filter: blur(15px); border: 1px solid #1f293d; border-radius: 24px; padding: 40px; width: 460px; text-align: center; box-shadow: 0 25px 60px rgba(0,0,0,0.9);">'
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
    st.markdown("<h2 style='color: white; font-weight: 900;'>🎮 VILLAGE RF</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 12px; margin-bottom: 15px;'>MAIN MENU</p>", unsafe_allow_html=True)
    
    page = st.radio(
        "Navigation",
        ["🏠 Home", "🖥️ Server", "👥 Staff Team", "📜 Rules", "🎉 Events", "📝 Staff Application", "💬 Discord"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown(
        "<div style='background: rgba(18, 22, 32, 0.85); padding: 15px; border-radius: 14px; border: 1px solid #1f293d;'>"
        "<div style='color: #ff1e38; font-weight: bold; font-size: 14px;'>🔴 VILLAGE RF</div>"
        "<div style='color: #64748b; font-size: 12px; margin-top: 2px;'>Server Online — LIVE</div>"
        "</div>",
        unsafe_allow_html=True
    )

# 4. Main Content Pages
if "Home" in page:
    home_html = (
        '<div style="background: rgba(14, 17, 23, 0.80); backdrop-filter: blur(12px); border-radius: 20px; padding: 55px 45px; border: 1px solid #1f293d; margin-bottom: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">'
        '<span class="hero-tag">🔴 OFFICIAL COMMUNITY PORTAL • VILLAGE RF / 2026</span>'
        '<h1 class="hero-title">VILLAGE RF</h1>'
        '<p style="color: #ff1e38; font-weight: bold; font-size: 17px; margin-top: -5px;">MORE THAN JUST A SERVER.</p>'
        '<p style="color: #94a3b8; font-size: 15px; max-width: 650px; line-height: 1.6;">Welcome to the official VILLAGE RF community portal. Stay connected, check the latest events, meet the team and keep your Discord access verified.</p>'
        '<div style="margin-top: 25px;">'
        '<a href="https://discord.gg/WC9NFNVFS" target="_blank" class="btn-action">Join Community ➔</a>'
        '<a href="fivem://connect/217.160.240.61" class="btn-secondary-action">Connect Server 🚀</a>'
        '</div></div>'
    )
    st.markdown(home_html, unsafe_allow_html=True)

elif "Server" in page:
    st.header("🖥️ Server Direct Connect")
    st.info("Direct Connect IP: connect 217.160.240.61")
    st.code("connect 217.160.240.61", language="bash")
    st.markdown("<br><a href='fivem://connect/217.160.240.61' class='btn-action'>Connect Directly to FiveM 🚀</a>", unsafe_allow_html=True)

elif "Staff Team" in page:
    st.header("👥 Staff Team — VILLAGE RF")
    st.caption("Meet our official management and leadership team.")
    st.write("---")
    
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    
    with c1:
        st.markdown("<div class='card-box' style='border-color:#ff1e38;'><div class='role-badge'>👑 OWNER</div><div class='staff-title'>! Haroun.13K</div><div class='staff-sub'>@off_marseille</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card-box' style='border-color:#ff1e38;'><div class='role-badge'>👑 FOUNDER</div><div class='staff-title'>ADLANE HB</div><div class='staff-sub'>@adlanehb</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card-box'><div class='role-badge'>🟣 CO-OWNER</div><div class='staff-title'>SIDO</div><div class='staff-sub'>@sido_sido_18</div></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='card-box'><div class='role-badge'>⭐ MANAGER</div><div class='staff-title'>Johane</div><div class='staff-sub'>@yb.johane</div></div>", unsafe_allow_html=True)
    with c5:
        st.markdown("<div class='card-box'><div class='role-badge'>🔵 DEV</div><div class='staff-title'>ZR</div><div class='staff-sub'>@zr_rr011</div></div>", unsafe_allow_html=True)
    with c6:
        st.markdown("<div class='card-box'><div class='role-badge'>🔵 DEV</div><div class='staff-title'>PIROx99.</div><div class='staff-sub'>@piro.fps20.</div></div>", unsafe_allow_html=True)
    with c7:
        st.markdown("<div class='card-box'><div class='role-badge'>⭐ DEV DISCORD</div><div class='staff-title'>ZAKI VEX</div><div class='staff-sub'>@closedaccount1_</div></div>", unsafe_allow_html=True)

elif "Rules" in page:
    st.header("📜 Server Rules")
    st.markdown("1. **Respect All Members:** Toxic behavior is strictly prohibited.")
    st.markdown("2. **No RDM / VDM:** Follow Roleplay standards at all times.")
    st.markdown("3. **Value Your Life:** Fear RP is mandatory.")

elif "Staff Application" in page:
    st.header("📝 Staff Application")
    st.text_input("Discord Tag")
    st.text_area("Why do you want to join our staff?")
    st.button("Submit Application")

elif "Discord" in page:
    st.header("💬 Join Our Discord Server")
    st.markdown("<br><a href='https://discord.gg/WC9NFNVFS' target='_blank' class='btn-action'>Open Discord Invite ➔</a>", unsafe_allow_html=True)
