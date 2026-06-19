import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Fxeyu AI", page_icon="🚀")
st.title("Fxeyu AI 🚀")
st.write("እንኳን ወደ ማህበረሰቡ AI ረዳት በሰላም መጡ!")

# API Keyን ከ Streamlit Secrets ያነባል
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # የሞዴል ስም ትክክለኛ አጻጻፍ
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("ምን ልርዳዎት?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"ስህተት ተፈጠረ: {e}")
else:
    st.error("API Key አልተገኘም! እባክዎ በ Streamlit Secrets ውስጥ በትክክል ማስገባቱን ያረጋግጡ።")
