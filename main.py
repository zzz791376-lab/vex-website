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

if img_b64:
    bg_style = "data:image/jpeg;base64," + img_b64
else:
    bg_style = "https://images.alphacoders.com/131/1318498.jpeg"

# 2. Advanced Premium CSS
css_style = """
<style>
.stApp {
    background-color: #0b0e14;
    color: #ffffff;
}

header[data-testid="stHeader"] {
    background: transparent;
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
    transition: all 0.3s ease;
    cursor: pointer;
}

div[role="radiogroup"] > label:hover {
    border-color: #0088ff;
    background: #1c212a;
    transform: translateX(4px);
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
    letter-spacing: 2px;
    text-shadow: 0 4px 20px rgba(0,0,0,0.9);
}

.hero-tag {
    color: #0088ff;
    font-weight: bold;
    font-size: 13px;
    letter-spacing: 2px;
    text-shadow: 0 2px 10px rgba(0,136,255,0.4);
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
    transition: all 0.3s ease;
}

.btn-action:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(0, 136, 255, 0.7);
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
    transition: all 0.3s ease;
}

.btn-secondary-action:hover {
    border-color: #0088ff;
    background: #1c212a;
    transform: translateY(-2px);
}

.staff-card {
    background: linear-gradient(145deg, #11151c 0%, #161b22 100%);
    border: 1px solid #1e293b;
    border-radius: 18px;
    padding: 25px 15px;
    text-align: center;
    margin-bottom: 20px;
    transition: all 0.3s ease;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
}

.staff-card:hover {
    border-color: #0088ff;
    transform: translateY(-6px);
    box-shadow: 0 12px 28px rgba(0, 136, 255, 0.3);
}

.staff-card-owner {
    border: 1px solid rgba(0, 136, 255, 0.4);
    background: linear-gradient(145deg, #131b2e 0%, #11151c 100%);
}

.staff-role {
    display: inline-block;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    background: rgba(0, 136, 255, 0.12);
    color: #00a2ff;
    padding: 6px 14px;
    border-radius: 20px;
    border: 1px solid rgba(0, 136, 255, 0.3);
}

.staff-name {
    color: #ffffff;
    font-size: 20px;
    font-weight: 900;
    margin: 15px 0 5px 0;
    letter-spacing: 0.5px;
}

.staff-tag {
    color: #64748b;
    font-size: 13px;
    font-family: monospace;
}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 3. Sidebar Navigation
with st.sidebar:
    st.markdown("<h2 style='color: white;'>🎮 VILLAGE RF</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 12px; margin-bottom: 15px;'>MAIN MENU</p>", unsafe_allow_html=True)
    
    page = st.radio(
        "Navigation",
        ["🏠 Home", "🖥️ Server", "👥 Staff Team", "📜 Rules", "🎉 Events", "📝 Staff Application", "💬 Discord"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("""
        <div style="background: #161b22; padding: 15px; border-radius: 12px; border: 1px solid #21262d;">
            <div style="color: #00a2ff; font-weight: bold; font-size: 14px;">🔵 VILLAGE RF</div>
            <div style="color: #64748b; font-size: 12px; margin-top: 2px;">Server Online — LIVE</div>
        </div>
    """, unsafe_allow_html=True)

# 4. Main Content
if "Home" in page:
    banner_html = "<div style=\"background: linear-gradient(180deg, rgba(11, 14, 20, 0.3) 0%, rgba(11, 14, 20, 1) 100%), url('" + bg_style + "'); background-size: cover; background-position: center; border-radius: 20px; padding: 55px 45px; border: 1px solid #1e293b; margin-bottom: 25px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);\"><span class=\"hero-tag\">🔵 OFFICIAL COMMUNITY PORTAL • VILLAGE RF / 2026</span><h1 class=\"hero-title\">VILLAGE RF</h1><p style=\"color: #00a2ff; font-weight: bold; font-size: 17px; margin-top: -5px;\">MORE THAN JUST A SERVER.</p><p style=\"color: #94a3b8; font-size: 15px; max-width: 650px; line-height: 1.6;\">Welcome to the official VILLAGE RF community portal. Stay connected, check the latest events, meet the team and keep your Discord access verified.</p><div style=\"margin-top: 25px;\"><a href=\"https://discord.gg/WC9NFNVFS\" target=\"_blank\" class=\"btn-action\">Join Community ➔</a><a href=\"fivem://connect/217.160.240.61\" class=\"btn-secondary-action\">Connect Server 🚀</a></div></div>"
    st.markdown(banner_html, unsafe_allow_html=True)

elif "Server" in page:
    st.header("🖥️ Server Direct Connect")
    st.info("Direct Connect IP: connect 217.160.240.61")
    st.code("connect 217.160.240.61", language="bash")
    st.markdown("<br><a href='fivem://connect/217.160.240.61' class='btn-action'>Connect Directly to FiveM 🚀</a>", unsafe_allow_html=True)

elif "Staff Team" in page:
    st.header("👥 Staff Team — VILLAGE RF")
    st.caption("Meet our official management and leadership team.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("👑 Leadership & Founders")
    f1, f2, f3, f4 = st.columns(4)
    
    with f1:
        st.markdown('<div class="staff-card staff-card-owner"><span class="staff-role">👑 FOUNDER</span><div class="staff-name">VL · Johane</div><div class="staff-tag">@yb.johane</div></div>', unsafe_allow_html=True)

    with f2:
        st.markdown('<div class="staff-card staff-card-owner"><span class="staff-role">👑 OWNER</span><div class="staff-name">! Haroun.13K</div><div class="staff-tag">@off_marseille</div></div>', unsafe_allow_html=True)

    with f3:
        st.markdown('<div class="staff-card staff-card-owner"><span class="staff-role">👑 FOUNDER</span><div class="staff-name">VL · ADLANE HB</div><div class="staff-tag">@adlanehb</div></div>', unsafe_allow_html=True)
        
    with f4:
        st.markdown('<div class="staff-card"><span class="staff-role">🟣 CO-OWNER</span><div class="staff-name">VL · SIDO</div><div class="staff-tag">@sido_sido_18</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("⚙️ Management & Development")
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.markdown('<div class="staff-card"><span class="staff-role">🔵 SERVER DEVELOPER</span><div class="staff-name">VL · ZR</div><div class="staff-tag">@zr_rr011</div></div>', unsafe_allow_html=True)
        
    with m2:
        st.markdown('<div class="staff-card"><span class="staff-role">🔵 SERVER DEV / HIGH STAFF</span><div class="staff-name">VL · PIROx99.</div><div class="staff-tag">@piro.fps20.</div></div>', unsafe_allow_html=True)

    with m3:
        st.markdown('<div class="staff-card"><span class="staff-role">⭐ DEV DISCORD</span><div class="staff-name">VL · ZAKI VEX</div><div class="staff-tag">@closedaccount1_</div></div>', unsafe_allow_html=True)

    with m4:
        st.markdown('<div class="staff-card"><span class="staff-role">⭐ STAFF MANAGER</span><div class="staff-name">VL · Radixx</div><div class="staff-tag">@radix009</div></div>', unsafe_allow_html=True)

elif "Rules" in page:
    st.header("📜 Server Rules")
    st.markdown("""
    1. **Respect All Members:** Toxic behavior is strictly prohibited.
    2. **No RDM / VDM:** Follow Roleplay standards at all times.
    3. **Value Your Life:** Fear RP is mandatory.
    """)

elif "Staff Application" in page:
    st.header("📝 Staff Application")
    st.text_input("Discord Tag")
    st.text_area("Why do you want to join our staff?")
    st.button("Submit Application")

elif "Discord" in page:
    st.header("💬 Join Our Discord Server")
    st.markdown("<br><a href='https://discord.gg/WC9NFNVFS' target='_blank' class='btn-action'>Open Discord Invite ➔</a>", unsafe_allow_html=True)
