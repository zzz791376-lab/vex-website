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
    background: #0088ff;
    color: white !important;
    text-decoration: none !important;
    border-radius: 12px;
    padding: 12px 28px;
    font-weight: bold;
    margin-right: 15px;
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
    st.markdown("""
    <div style='background: #161b22; padding: 15px; border-radius: 12px; border: 1px solid #21262d;'>
        <div style='color: #00a2ff; font-weight: bold; font-size: 14px;'>🔵 VILLAGE RF</div>
        <div style='color: #64748b; font-size: 12px; margin-top: 2px;'>Server Online — LIVE</div>
    </div>
    """, unsafe_allow_html=True)

# 4. Main Content
if "Home" in page:
    st.markdown(f"""
    <div style="background: linear-gradient(180deg, rgba(11, 14, 20, 0.3) 0%, rgba(11, 14, 20, 1) 100%), url('{bg_style}'); background-size: cover; background-position: center; border-radius: 20px; padding: 55px 45px; border: 1px solid #1e293b; margin-bottom: 25px;">
        <span class="hero-tag">🔵 OFFICIAL COMMUNITY PORTAL • VILLAGE RF / 2026</span>
        <h1 class="hero-title">VILLAGE RF</h1>
        <p style="color: #00a2ff; font-weight: bold; font-size: 17px; margin-top: -5px;">MORE THAN JUST A SERVER.</p>
        <p style="color: #94a3b8; font-size: 15px; max-width: 650px; line-height: 1.6;">Welcome to the official VILLAGE RF community portal. Stay connected, check the latest events, meet the team and keep your Discord access verified.</p>
        <div style="margin-top: 25px;">
            <a href="https://discord.gg/WC9NFNVFS" target="_blank" class="btn-action">Join Community ➔</a>
            <a href="fivem://connect/217.160.240.61" class="btn-secondary-action">Connect Server 🚀</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
