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

# 2. Load External CSS File safely
if os.path.exists("style.css"):
    with open("style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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
    st.markdown("<div class='sidebar-status'><div class='status-title'>🔵 VILLAGE RF</div><div class='status-sub'>Server Online — LIVE</div></div>", unsafe_allow_html=True)

# 4. Main Content
if "Home" in page:
    st.markdown(f"""
    <div style="background: linear-gradient(180deg, rgba(11, 14, 20, 0.3) 0%, rgba(11, 14, 20, 1) 100%), url('{bg_style}'); background-size: cover; background-position: center; border-radius: 20px; padding: 55px 45px; border: 1px solid #1e293b; margin-bottom: 25px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);">
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
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("👑 Owner")
    o1, _ = st.columns([1, 2])
    with o1:
        st.markdown('<div class="staff-card staff-card-owner"><span class="staff-role">👑 OWNER</span><div class="staff-name">! Haroun.13K</div><div class="staff-tag">@off_marseille</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("👑 Founders")
    f1, _ = st.columns([1, 2])
    with f1:
        st.markdown('<div class="staff-card staff-card-owner"><span class="staff-role">👑 FOUNDER</span><div class="staff-name">VL · ADLANE HB</div><div class="staff-tag">@adlanehb</div></div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("🟣 Co-Owners")
    c1, _ = st.columns([1, 2])
    with c1:
        st.markdown('<div class="staff-card"><span class="staff-role">🟣 CO-OWNER</span><div class="staff-name">VL · SIDO</div><div class="staff-tag">@sido_sido_18</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("⚙️ Server Management & Development")
    m1, m2, m3 = st.columns(3)
    
    with m1:
        st.markdown('<div class="staff-card"><span class="staff-role">⭐ SERVER MANAGER</span><div class="staff-name">VL · Johane</div><div class="staff-tag">@yb.johane</div></div>', unsafe_allow_html=True)

    with m2:
        st.markdown('<div class="staff-card"><span class="staff-role">🔵 SERVER DEVELOPER</span><div class="staff-name">VL · ZR</div><div class="staff-tag">@zr_rr011</div></div>', unsafe_allow_html=True)
        
    with m3:
        st.markdown('<div class="staff-card"><span class="staff-role">🔵 SERVER DEV / HIGH STAFF</span><div class="staff-name">VL · PIROx99.</div><div class="staff-tag">@piro.fps20.</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("🤖 Discord Development")
    d1, _ = st.columns([1, 2])
    with d1:
        st.markdown('<div class="staff-card"><span class="staff-role">⭐ DEV DISCORD</span><div class="staff-name">VL · ZAKI VEX</div><div class="staff-tag">@closedaccount1_</div></div>', unsafe_allow_html=True)

elif "Rules" in page:
    st.header("📜 Server Rules")
    st.markdown("1. **
