import streamlit as st
import re

st.title("🔍 SEO Keyword Density Checker")

text = st.text_area("Paste your article here:")

keywords = st.text_input("Enter comma-separated keywords:", "hris, hris software, payroll")

if text and keywords:
    text_clean = re.sub(r'[^\w\s]', '', text.lower())
    word_list = text_clean.split()
    total_words = len(word_list)

    st.write(f"Total word count: {total_words}")

    st.subheader("📊 Keyword Stats")
    for kw in [k.strip().lower() for k in keywords.split(",")]:
        pattern = r'\b' + re.escape(kw) + r'\b'
        count = len(re.findall(pattern, text_clean))
        density = (count / total_words) * 100 if total_words else 0
        st.write(f"**{kw}** — Count: {count} | Density: {density:.2f}%")
