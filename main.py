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
    st
