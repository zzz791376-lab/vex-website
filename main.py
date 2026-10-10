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

# Check Login Status via Query Parameters
if "login" in st.query_params:
    st.session_state.logged_in = True

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 2. CSS Styles (Safe lines)
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
.btn-discord-login {
    display: block;
    width: 100%;
    background: linear-gradient(90deg, #0066ff 0%, #00a2ff 100%);
    color: #ffffff !important;
    text-decoration: none !important;
    font-weight: bold;
    font-size: 15px;
    padding: 14px 20px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0, 136, 255, 0.4);
    text-align: center;
    border: none;
    cursor: pointer;
}
.btn-discord-login:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(0, 136, 255, 0.6);
}
</style>
""", unsafe_allow_html=True)

# --- LOGIN / WELCOME GATEWAY ---
if not st.session_state.logged_in:
    login_html = (
        f'<div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: linear-gradient(180deg, rgba(11, 14, 20, 0.85) 0%, rgba(11, 14, 20, 0.95) 100%), url(\'{bg_style}\'); background-size: cover; background-position: center; display: flex; justify-content: center; align-items: center; z-index: 99999;">'
        f'<div style="background: #11151c; border: 1px solid #1e293b; border-radius: 24px; padding: 40px; width: 460px; text-align: center; box-shadow: 0 20px 50px rgba(0,0,0,0.8);">'
        f'<img src="{logo_style}" style="width: 85px; height: 85px; border-radius: 50%; object-fit: cover; margin-bottom: 15px; border: 2px solid #0088ff;">'
        '<div style="color: #0088ff; font-size: 11px; font-weight: bold; letter-spacing: 2px; margin-bottom: 10px;">VILLAGE RF COMMUNITY PORTAL</div>'
        '<h1 style="color: #ffffff; font-size: 30px; font-weight: 900; margin-bottom: 10px;">Enter the <span style="color: #0088ff;">VILLAGE</span> world.</h1>'
        '<p style="color: #64748b; font-size: 13px; line-height: 1.5; margin-bottom: 25px;">Connect your Discord account to access the official website and verify your community access.</p>'
        '<a href="?login=true" target="_self" class="btn-discord-login">🔗 Continue with Discord ➔</a>'
        '</div></div>'
    )
    st.markdown(login_html, unsafe_allow_html=True)
    st.stop()

# --- MAIN WEBSITE (After Login) ---

# 3. Sidebar Navigation
with st.sidebar:
    st.markdown("<h2 style='color: white;'>🎮 VILLAGE RF</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 12px; margin-bottom: 15px;'>MAIN MENU</p>", unsafe_allow_html=True)
    
    page = st.radio(
        "Navigation",
        ["🏠 Home", "🖥️ Server", "👥 Staff Team", "📜 Rules", "🎉 Events", "📝 Staff Application", "💬 Discord"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown(
        "<div style='background: #161b22; padding: 15px; border-radius: 12px; border: 1px solid #21262d;'>"
        "<div style='color: #00a2ff; font-weight: bold; font-size: 14px;'>🔵 VILLAGE RF</div>"
        "<div style='color: #64748b; font-size: 12px; margin-top: 2px;'>Server Online — LIVE</div>"
        "</div>",
        unsafe_allow_html=True
    )

# 4. Main Content Pages
if "Home" in page:
    home_html = (
        f'<div style="background: linear-gradient(180deg, rgba(11, 14, 20, 0.3) 0%, rgba(11, 14, 20, 1) 100%), url(\'{bg_style}\'); background-size: cover; background-position: center; border-radius: 20px; padding: 55px 45px; border: 1px solid #1e293b; margin-bottom: 25px;">'
        '<span class="hero-tag">🔵 OFFICIAL COMMUNITY PORTAL • VILLAGE RF / 2026</span>'
        '<h1 class="hero-title">VILLAGE RF</h1>'
        '<p style="color: #0088ff; font-weight: bold; font-size: 17px; margin-top: -5px;">MORE THAN JUST A SERVER.</p>'
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
        st.markdown("<div class='card-box' style='border-color:#0088ff;'><div class='role-badge'>👑 OWNER</div><div class='staff-title'>! Haroun.13K</div><div class='staff-sub'>@off_marseille</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card-box' style='border-color:#0088ff;'><div class='role-badge'>👑 FOUNDER</div><div class='staff-title'>ADLANE HB</div><div class='staff-sub'>@adlanehb</div></div>", unsafe_allow_html=True)
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
