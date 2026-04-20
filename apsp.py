import streamlit as st
import time
from datetime import datetime
import random

# Page Setup
st.set_page_config(page_title="HBD Fariha!", page_icon="🎂", layout="wide")

# Custom Design for Centering and Full-Screen Rain
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; } 
    
    .countdown-box {
        font-size: 25px; color: #d81b60; text-align: center;
        background: #f8f9fa; padding: 15px; border-radius: 15px;
        border: 2px dashed #d81b60; font-weight: bold; margin: 0 auto; width: 60%;
    }
    
    .age-fact { font-size: 22px; color: #d81b60; text-align: center; margin-top: 15px; font-weight: bold; }
    .wish-title { font-size: 28px; color: #1e88e5; text-align: center; font-weight: bold; margin-top: 30px; }
    .pink-text { font-size: 20px; color: #ff4081; font-weight: bold; text-align: center; line-height: 1.8; }
    .blue-text { font-size: 20px; color: #1e88e5; font-weight: bold; text-align: center; line-height: 1.8; }
    
    /* 2-Pound Cake Centering */
    .cake-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        margin-top: 50px;
    }
    .cake { position: relative; width: 300px; height: 180px; }
    .layer { width: 300px; height: 100px; background: #ff80ab; border-radius: 50% / 20%; position: absolute; bottom: 0; box-shadow: 0 12px #f06292; }
    .candle { width: 12px; height: 60px; background: #ffeb3b; position: absolute; bottom: 75px; left: 144px; border-radius: 6px; }
    .flame { width: 18px; height: 30px; background: orange; position: absolute; bottom: 135px; left: 141px; border-radius: 50% 50% 35% 35%; animation: flicker 0.15s infinite; }
    @keyframes flicker { 0% { transform: scale(1); opacity: 1; } 100% { transform: scale(1.1); opacity: 0.8; } }
    
    /* Full Screen Food Rain */
    .food-rain {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
    }

    .special-wish { font-size: 22px; color: #1a237e; text-align: center; font-style: italic; background: #fce4ec; padding: 25px; border-radius: 15px; margin-top: 30px; border: 2px solid #ff4081; }
    .footer { text-align: center; color: #880e4f; font-weight: bold; margin-top: 50px; padding-bottom: 20px; }
    .stButton>button { background-color: #ff4081; color: white; font-size: 25px; font-weight: bold; border-radius: 15px; width: 100%; height: 3em; }
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

# --- 2. AGE FUN FACT ---
birth_date = datetime(2011, 5, 3) 
days_alive = (now - birth_date).days
st.markdown(f'<div class="age-fact">🌟 Fariha, you have been awesome for {days_alive:,} days! 🌟</div>', unsafe_allow_html=True)

# --- 3. BALLOON BUTTON (Top Section) ---
st.write("")
if st.button("CLICK HEREEEEEEEEEE 🎈✨", use_container_width=True):
    with st.empty():
        for i in range(12): 
            st.balloons()
            time.sleep(2.5)

st.write("---")

# --- 4. 100 WISHES (Colorful Scroll) ---
st.markdown('<p class="wish-title">✨ 100 Wishes For You ✨</p>', unsafe_allow_html=True)
for i in range(1, 101):
    color_class = "pink-text" if i % 2 != 0 else "blue-text"
    st.markdown(f'<p class="{color_class}">{i}. Happy Birthday to you Fariha 🎂💖</p>', unsafe_allow_html=True)

st.write("---")

# --- 5. 2-POUND CAKE & FOOD RAIN ---
if "blown" not in st.session_state:
    st.session_state.blown = False
if "prank_step" not in st.session_state:
    st.session_state.prank_step = 0

# Center container
st.markdown('<div class="cake-container">', unsafe_allow_html=True)

if not st.session_state.blown:
    st.markdown('<div class="cake"><div class="flame"></div><div class="candle"></div><div class="layer"></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size:24px; color:#d81b60; font-weight:bold; margin-top:20px;">🕯️ Blow the candle to start the magic!</p>', unsafe_allow_html=True)
    if st.button("Blow the Candle! 💨"):
        st.session_state.blown = True
        st.rerun()
else:
    # After blowing the candle
    st.markdown('<div class="cake"><div class="candle"></div><div class="layer"></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Full Screen Food Rain
    food_emojis = ["🍫", "🍦", "🍕", "🍔", "🍟", "🍩", "🍰", "🍓", "🍗", "🍭"]
    rain_items = "".join([f'<div style="left:{random.randint(0,95)}%; animation: fall {random.randint(3,7)}s linear infinite; position:fixed; top:-50px; font-size:35px; z-index:9999;">{random.choice(food_emojis)}</div>' for _ in range(50)])
    
    st.markdown(f"""
        <div class="food-rain">{rain_items}</div>
        <style>
        @keyframes fall {{ 0% {{ top: -50px; }} 100% {{ top: 100vh; }} }}
        </style>
    """, unsafe_allow_html=True)

    # Sound effect
    st.components.v1.html("""<iframe width="0" height="0" src="https://youtube.com" frameborder="0" allow="autoplay"></iframe>""", height=0)
    
    st.snow()
    st.markdown('<h1 style="text-align: center; color: #ff1493; margin-top:20px;">✨ Make a Wish! ✨</h1>', unsafe_allow_html=True)
    
    # Prank Messages (In Bengali)
    st.write("---")
    if st.session_state.prank_step == 0:
        if st.button("Click for the first truth! 😂"):
            st.session_state.prank_step = 1
            st.rerun()
    
    if st.session_state.prank_step >= 1:
        st.error("তুই একটা কুত্তা! 🐶")
        if st.session_state.prank_step == 1:
            if st.button("Next? 😜"): st.session_state.prank_step = 2; st.rerun()
    
    if st.session_state.prank_step >= 2:
        st.warning("তুই একটা ছাগল! 🐐")
        if st.session_state.prank_step == 2:
            if st.button("Final? 🤪"): st.session_state.prank_step = 3; st.rerun()
    
    if st.session_state.prank_step >= 3:
        st.info("পাগললললললললললললললললললললললললললললললললললললল! 🤪")
        st.success("Happy Birthday Fariha! ❤️")
        st.markdown('<div class="special-wish">"To the person who knows all my secrets and still likes me—Happy Birthday! I\'m so lucky to have a best friend like you. Have the best day ever! 🎉"</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Made with ❤️ by your bestfriend</div>', unsafe_allow_html=True)
