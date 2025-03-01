import streamlit as st
from google.generativeai import GenerativeModel

# Show title and description.
st.title("💬 AmanWisata Chatbot")
st.write(
    "AmanWisata adalah chatbot yang membantu Anda berwisata dengan aman dengan mengetahui lokasi wisata yang aman dari bencana. "
    "Chatbot ini menggunakan model Google Gemini untuk memberikan informasi yang akurat."
)

# Ask user for their Google API key
api_key = st.text_input("Google API Key", type="password")
if not api_key:
    st.info("Silakan masukkan Google API key Anda untuk melanjutkan.", icon="🗝️")
else:
    # Create a Gemini client
    model = GenerativeModel(api_key=api_key, model_name="gemini-pro")

    # Create a session state variable to store the chat messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display existing chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field
    if prompt := st.chat_input("Tanyakan tentang lokasi wisata aman!"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate a response using Google Gemini
        response = model.generate_content(
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )
        
        # Display and store response
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
