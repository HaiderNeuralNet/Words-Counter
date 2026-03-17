import streamlit as st

# Page config
st.set_page_config(page_title="Word Counter", page_icon="📝")

# Simple dark theme
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
    }
</style>
""", unsafe_allow_html=True)

# Title with emoji
st.title("📝 Word Counter")

# Text input
text = st.text_area("Paste your text here:", height=200)

# Analyze button
if st.button("🔍 Count Words"):
    if text:
        # Simple calculations
        words = len(text.split())
        characters = len(text)
        lines = len(text.splitlines())
        
        # Display results
        st.markdown("---")
        st.subheader("📊 Results")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Words", words)
        col2.metric("Characters", characters)
        col3.metric("Lines", lines)
        
        st.success(f"✅ Found {words} words and {characters} characters in {lines} Lines !")
    else:
        st.warning("⚠️ Please enter some text first")