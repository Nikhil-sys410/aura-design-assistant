import streamlit as st
import time
import random

# --- 1. CONFIGURATION & SETUP ---
st.set_page_config(
    page_title="AURA | GenAI Design Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- 2. HIGH-CONTRAST CSS ---
st.markdown("""
    <style>
        /* IMPORT FONTS */
        @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Inter:wght@400;600&display=swap');

        /* ANIMATED BACKGROUND */
        @keyframes gradient-animation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        :root {
            --primary-glow: #00F0FF;
            --secondary-glow: #FF003C;
            --bg-dark: #050505;
            --glass-border: rgba(255, 255, 255, 0.2);
            --text-main: #FFFFFF;
            --text-dim: #CCCCCC;
        }

        /* GLOBAL STYLES */
        .stApp {
            background-color: var(--bg-dark);
            background-image: 
                radial-gradient(circle at 15% 50%, rgba(0, 240, 255, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 85% 30%, rgba(255, 0, 60, 0.08) 0%, transparent 50%);
            color: var(--text-main);
            font-family: 'Inter', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Syncopate', sans-serif !important;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: white !important;
        }
        
        p, div, label, span {
            color: var(--text-main); 
        }

        /* --- CRITICAL FONT VISIBILITY FIXES --- */
        
        /* Force all widget labels (Category, Keywords) to be bright Cyan */
        .stTextInput label, .stSelectbox label {
            color: #00F0FF !important;
            font-family: 'Syncopate', sans-serif !important;
            font-size: 0.8rem !important;
            letter-spacing: 1px;
            font-weight: 700 !important;
            text-transform: uppercase;
        }
        
        /* Input Fields Background & Text */
        .stTextInput > div > div > input {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 8px;
        }
        
        /* Selectbox (Dropdown) Specifics */
        .stSelectbox div[data-baseweb="select"] > div {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 8px;
        }
        
        /* Dropdown Menu Items */
        div[data-baseweb="menu"] {
            background-color: #111 !important;
            border: 1px solid #333 !important;
        }
        div[data-baseweb="option"] {
            color: white !important;
        }

        /* Sidebar Visibility */
        section[data-testid="stSidebar"] {
            background-color: #0a0a0a;
            border-right: 1px solid #333;
        }
        
        section[data-testid="stSidebar"] .stRadio label {
            color: #DDDDDD !important;
            font-weight: 500 !important;
            font-size: 1rem !important;
        }
        
        /* NEON GRADIENT TEXT */
        .neon-text {
            background: linear-gradient(90deg, #00F0FF, #FFFFFF, #FF003C);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
            text-shadow: 0 0 30px rgba(0, 240, 255, 0.3);
        }

        /* CYBER BUTTON */
        .stButton > button {
            background: linear-gradient(90deg, #00F0FF 0%, #0088FF 100%);
            color: #000 !important; /* Black text on bright button */
            border: none;
            font-weight: 900 !important;
            text-transform: uppercase;
            padding: 18px 30px;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            box-shadow: 0 0 30px rgba(0, 240, 255, 0.6);
            color: #000 !important;
            transform: scale(1.02);
        }
        
        /* GLASS CARDS */
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 20px;
            backdrop-filter: blur(10px);
        }

    </style>
""", unsafe_allow_html=True)

# --- 3. HELPER FUNCTIONS ---
def generate_prompt(category, keywords):
    styles = [
        "Unreal Engine 5 render", "Vogue Italia Editorial", 
        "Cyberpunk 2077 Aesthetic", "Neo-Tokyo Street Style"
    ]
    style = random.choice(styles)
    return f"Full body shot of {category} fashion, featuring {keywords}. {style}, volumetric lighting, 8k resolution, octane render, hyper-detailed textures."

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: white;'>AURA <span style='color:#00F0FF'>v3</span></h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color: #333;'>", unsafe_allow_html=True)
    
    # Using st.radio with custom styling applied via CSS above
    st.radio("SYSTEM MODULES", ["Inspiration Generator", "Trend Radar", "Saved Archives", "Global Settings"])
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='background: rgba(0,240,255,0.1); border: 1px solid #00F0FF; padding: 10px; border-radius: 5px; text-align: center;'>
            <span style='color: #00F0FF; font-weight: bold; font-size: 0.8rem;'>● SYSTEM ONLINE</span>
        </div>
    """, unsafe_allow_html=True)

# --- 5. MAIN UI ---

# Hero Section
st.markdown("<h1 style='font-size: 3.5rem; margin-bottom: 0;'>DESIGN <span class='neon-text'>INSPIRATION</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='font-family: Inter; font-weight: 400; font-size: 1.1rem; color: #CCCCCC; max-width: 700px;'>AI-Orchestrated Merchandising & Ideation Engine. Generate high-fidelity prompts instantly.</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Input Box Container
st.markdown("""
    <div style="padding: 25px; border: 1px solid rgba(255, 255, 255, 0.15); background: rgba(0,0,0,0.6); border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1.5, 3, 1])

with c1:
    # The label color is forced to Cyan via CSS
    category = st.selectbox("Design Category", ["Streetwear", "Haute Couture", "Techwear", "Sustainable", "Avant-Garde"])

with c2:
    # The label color is forced to Cyan via CSS
    keywords = st.text_input("Trend Keywords", placeholder="e.g. Liquid Metal, Bioluminescence, Y2K Glitch")

with c3:
    st.markdown("<br>", unsafe_allow_html=True) # Spacer to align button
    generate_btn = st.button("INITIALIZE")

st.markdown("</div>", unsafe_allow_html=True)

# Logic
if generate_btn:
    if not keywords:
        st.error("⚠️ INPUT REQUIRED: Please define trend keywords.")
    else:
        # Progress Bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            time.sleep(0.005)
            progress_bar.progress(i + 1)
            
        status_text.empty()
        progress_bar.empty()
        
        st.session_state.generated = True
        st.session_state.prompt = generate_prompt(category, keywords)
        st.session_state.keywords = keywords

# --- 6. RESULTS DISPLAY ---
if st.session_state.get('generated', False):
    st.markdown("<br><h3 style='color: white;'>/// GENERATION OUTPUT</h3>", unsafe_allow_html=True)
    
    # Bento Grid Layout
    col_main, col_stat = st.columns([2, 1])
    
    with col_main:
        st.markdown(f"""
            <div class="glass-card">
                <h4 style="color: #00F0FF; margin-bottom: 10px; font-size: 0.9rem; letter-spacing: 1px;">AI PROMPT SEQUENCE</h4>
                <p style="font-family: 'Courier New', monospace; font-size: 1.1rem; color: #FFF; line-height: 1.6; font-weight: 500;">
                    {st.session_state.prompt}
                </p>
                <div style="margin-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px;">
                    <span style="color: #666; font-size: 0.8rem;">OPTIMIZED FOR: </span>
                    <span style="color: #FFF; font-weight: bold; font-size: 0.8rem; margin-left: 5px;">MIDJOURNEY v6</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_stat:
        st.markdown(f"""
            <div class="glass-card" style="text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: center;">
                <h4 style="color: #888; font-size: 0.8rem;">TREND CONFIDENCE</h4>
                <div class="neon-text" style="font-size: 3.5rem; line-height: 1.1; margin: 10px 0;">98%</div>
                <p style="color: #AAA; font-size: 0.8rem;">Based on Q3 2026 Metrics</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Mood Board Assets
    r1, r2, r3, r4 = st.columns(4)
    
    assets = [
        ("TEXTURE", "Graphene", "🕸️"),
        ("PALETTE", "Acid Neon", "🎨"),
        ("LIGHT", "Volumetric", "🌫️"),
        ("STYLE", "Post-Digital", "💾")
    ]
    
    for idx, col in enumerate([r1, r2, r3, r4]):
        with col:
            st.markdown(f"""
                <div class="glass-card" style="text-align: center; padding: 20px;">
                    <div style="font-size: 2.5rem; margin-bottom: 10px;">{assets[idx][2]}</div>
                    <div style="color: #00F0FF; font-weight: bold; font-size: 0.8rem; letter-spacing: 1px;">{assets[idx][0]}</div>
                    <div style="color: #EEE; font-size: 0.9rem;">{assets[idx][1]}</div>
                </div>
            """, unsafe_allow_html=True)

elif not st.session_state.get('generated', False):
    # Empty State
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; opacity: 0.3;">
            <h1 style="font-family: 'Syncopate'; font-size: 5rem; color: #222; margin: 0;">AURA</h1>
            <p style="color: #555;">WAITING FOR INPUT STREAM...</p>
        </div>
    """, unsafe_allow_html=True)