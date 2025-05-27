import streamlit as st
import re

st.title("🔍 SEO Keyword Density Checker")

# 1. Input fields
text = st.text_area("Paste your article here:")
keywords = st.text_input("Enter comma-separated keywords:", "hris, hris software, payroll")

# 2. Process when input is available
if text and keywords:
    # Clean and prepare the text
    text_clean = re.sub(r'[^\w\s]', '', text.lower())  # remove punctuation
    word_list = text_clean.split()                    # turn into list of words
    total_words = len(word_list)                      # count total words

    # 3. Display word count
    st.subheader("🧮 Total Word Count")
    st.write(f"Your article contains **{total_words} words**.")

    # 4. Show keyword stats
    st.subheader("📊 Keyword Stats")
    for kw in [k.strip().lower() for k in keywords.split(",")]:
        pattern = r'\b' + re.escape(kw) + r'\b'
        count = len(re.findall(pattern, text_clean))
        density = (count / total_words) * 100 if total_words else 0
        st.write(f"**{kw}** — Count: `{count}` | Density: `{density:.2f}%`")
