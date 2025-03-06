import streamlit as st # sreamlit
import re # Regular Expressions
import datetime # Datetime

if "old_passwords" not in st.session_state:
    st.session_state.old_passwords = {}

def check_strength(password):
    score = 0
    missing = []
    if len(password) > 8:
        score+=1
    else:
        st.error("❌ Password should be at least 8 characters long.")
        missing.append("More than 8 characters")
        
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score+=1
    else:
        st.error("❌ Password should be in lower case and upper case.")
        missing.append("Lower and Upper case")
        
    if re.search(r"\d", password):
        score+=1
    else:
        st.error("❌ Password should have one digit.")
        missing.append("digits")
        
    if re.search(r"[!@#$%^&*]", password):
        score+=1
    else:
        st.error("❌ Password should atleast have one special character.")
        missing.append("Special Characters")
    
    if score < 1:
        st.warning(f'❌ Weak Password - Try again!')
    elif score < 4:
        missing[-1] = f"and {missing[-1]}"if len(missing) > 1 else missing[-1]
        missing = ", ".join(missing)
        st.warning(f'⚠️ Weak Password - Try Adding {missing}!')
    else:
        missing = []
        if password in st.session_state.old_passwords:
            st.warning("⚠️ Password has been used before. Try a new one!")
        else:
            st.success('✔ Strong Password - Good to go!')
            st.session_state.old_passwords[password]= str(datetime.datetime.now().replace(microsecond=0))
st.set_page_config(page_title="", page_icon=":shark:", layout="centered")

st.title("Password Strength Meter 🔑")

tab1 , tab2 = st.tabs(["Check Password Strength", "Old Passwords"])

with tab1:
    password = st.text_input("Enter your password")
    st.info("ℹ️ Password should have atleast 8 characters, one digit, one special character and a mix of upper and lower case letters.")
    if st.button("Check Strength"):
        check_strength(password)
        
with tab2:
    if st.session_state.old_passwords:
        st.header("Old Passwords")
        for passwords,timestamp in st.session_state.old_passwords.items():
            st.subheader( '- ' + passwords)
            st.write('Created on ',timestamp)
    else:
        st.write("No old passwords found!")