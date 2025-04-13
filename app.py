import streamlit as st
from translator_model import LanguageTranslator

st.set_page_config(page_title="🌐 AI Translator", layout="centered")

st.title("🌐 AI Language Translator")
st.write("Translate text between different languages using AI (HuggingFace Transformers).")

# Language codes mapping
lang_codes = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

# Select languages
source_lang = st.selectbox("Select source language:", list(lang_codes.keys()))
target_lang = st.selectbox("Select target language:", list(lang_codes.keys()))

# Prevent same language selection
if source_lang == target_lang:
    st.warning("Source and target languages must be different.")

text_input = st.text_area("Enter text to translate:", height=150)

if st.button("Translate"):
    if source_lang != target_lang:
        with st.spinner("Translating..."):
            try:
                translator = LanguageTranslator(lang_codes[source_lang], lang_codes[target_lang])
                result = translator.translate(text_input)
                st.success("Translation:")
                st.text_area("Translated Text:", result, height=150)
            except ValueError as ve:
                st.error(str(ve))
