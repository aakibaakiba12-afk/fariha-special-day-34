import streamlit as st
import time
from datetime import datetime

# Page Setup
st.set_page_config(page_title="HBD Fariha!", page_icon="🎂")

# Custom Design (Pure CSS Animations)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; } 
    .countdown-box {
        font-size: 25px; color: #d81b60; text-align: center;
        background: #f8f9fa; padding: 15px; border-radius: 15px;
        border: 2px dashed #d81b60; font-weight: bold;
    }
    .wish-title { font-size: 28px; color: #1e88e5; text-align: center; font-weight: bold; margin-top: 30px; }
    .pink-text { font-size: 20px; color: #ff4081; font-weight: bold; text-align: center; line-height: 1.8; }
    .blue-text { font-size: 20px; color: #1e88e5; font-weight: bold; text-align: center; line-height: 1.8; }
    
    /* Digital Cake & Fireworks Style */
    .cake { width: 200px; height: 150px; margin: 40px auto; position: relative; }
    .layer { width: 200px; height: 80px; background: #ff80ab; border-radius: 50% / 20%; position: absolute; bottom: 0; box-shadow: 0 10px #f06292; }
    .candle { width: 10px; height: 50px; background: #ffeb3b; position: absolute; bottom: 60px; left: 95px; border-radius: 5px; }
    .flame { width: 15px; height: 25px; background: orange; position: absolute; bottom: 110px; left: 92px; border-radius: 50% 50% 35% 35%; animation: flicker 0.1s infinite; }
    .fireworks { font-size: 50px; text-align: center; animation: burst 1.5s infinite; }
    @keyframes flicker { 0% { transform: scale(1); opacity: 1; } 100% { transform: scale(1.1); opacity: 0.8; } }
    @keyframes burst { 0% { transform: scale(0.1); opacity: 0; } 50% { opacity: 1; } 100% { transform: scale(1.5); opacity: 0; } }
    
    .special-wish {
        font-size: 22px; color: #1a237e; text-align: center; font-style: italic;
        background: #fce4ec; padding: 25px; border-radius: 15px; margin-top: 30px;
        border: 2px solid #ff4081;
    }
    .footer { text-align: center; color: #880e4f; font-weight: bold; margin-top: 50px; padding-bottom: 20px; }
    .stButton>button { background-color: #ff4081; color: white; font-size: 22px; font-weight: bold; border-radius: 15px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. COUNTDOWN ---
target_date = datetime(2026, 5, 3) 
now = datetime.now()
diff = target_date - now

if diff.total_seconds() > 0:
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    st.markdown(f'<div class="countdown-box">⏳ Time remaining for Fariha\'s Birthday: <br> {days} Days, {hours} Hours, {minutes} Minutes </div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="countdown-box">🎉 Today is Fariha\'s Special Day! 🎉</div>', unsafe_allow_html=True)

# --- 2. MAGIC BUTTON ---
if st.button("CLICK HEREEEEEEEEEE 🎈✨", use_container_width=True):
    with st.empty():
        for i in range(8): 
            st.balloons()
            time.sleep(2)

st.write("---")

# --- 3. 100 WISHES (Blue Title & Multi-color Text) ---
st.markdown('<p class="wish-title">✨ 100 Wishes For You ✨</p>', unsafe_allow_html=True)

for i in range(1, 101):
    if i % 2 != 0:
        st.markdown(f'<p class="pink-text">{i}. Happy Birthday to you Fariha 🎂💖</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p class="blue-text">{i}. Happy Birthday to you Fariha 🎂💖</p>', unsafe_allow_html=True)

st.write("---")

# --- 4. CAKE & PRANK ---
if "blown" not in st.session_state:
    st.session_state.blown = False
if "prank_step" not in st.session_state:
    st.session_state.prank_step = 0

if not st.session_state.blown:
    # ডিজিটাল জ্বলন্ত মোমবাতিওয়ালা কেক
    st.markdown('<div class="cake"><div class="flame"></div><div class="candle"></div><div class="layer"></div></div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size:24px; color:#d81b60; font-weight:bold;">🕯️ Blow the candle to start the magic!</p>', unsafe_allow_html=True)
    if st.button("Blow the Candle! 💨"):
        st.session_state.blown = True
        st.rerun()
else:
    # মোমবাতি নিভে যাওয়ার পর ডিজিটাল আতশবাজি
    st.markdown('<div class="cake"><div class="candle"></div><div class="layer"></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="fireworks">🎆✨🎊✨🎆</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align: center; color: #ff1493;">✨ Make a Wish! ✨</h1>', unsafe_allow_html=True)
    st.snow()
    
    # প্র্যাঙ্ক মেসেজ
    if st.session_state.prank_step == 0:
        if st.button("Click for the first truth! 😂"):
            st.session_state.prank_step = 1
            st.rerun()
    
    if st.session_state.prank_step >= 1:
        st.error("তুই একটা কুত্তা! 🐶")
        if st.session_state.prank_step == 1:
            if st.button("Next? 😜"):
                st.session_state.prank_step = 2
                st.rerun()
    
    if st.session_state.prank_step >= 2:
        st.warning("তুই একটা ছাগল! 🐐")
        if st.session_state.prank_step == 2:
            if st.button("Final? 🤪"):
                st.session_state.prank_step = 3
                st.rerun()
    
    if st.session_state.prank_step >= 3:
        st.info("পাগললললললললললললললললললললললললললললললললললললল! 🤪")
        st.success("Happy Birthday Fariha! ❤️")
        
        # আপনার সেই স্পেশাল ইংরেজি মেসেজটি এখন এখানে আসবে
        st.markdown("""
            <div class="special-wish">
            "To the person who knows all my secrets and still likes me—Happy Birthday! 
            I'm so lucky to have a best friend like you. Have the best day ever! 🎉"
            </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="footer">Made with ❤️ by your bestfriend</div>', unsafe_allow_html=True)
