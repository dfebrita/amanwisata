import streamlit as st
import google.generativeai as genai

# Show title and description.
st.title("💬 Aman Wisata Chatbot")
st.write(
    "Aman Wisata adalah chatbot yang membantu Anda berwisata dengan aman dengan mengetahui lokasi wisata yang aman dari bencana. "
    "Chatbot ini menggunakan model Google Gemini untuk memberikan informasi yang akurat."
)

# Ask user for their Google API key
api_key = st.text_input("Google API Key", type="password")
if not api_key:
    st.info("Silakan masukkan Google API key Anda untuk melanjutkan.", icon="🗝️")
else:
    # Create a Gemini client
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

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
        try:
            response = model.generate_content(m["content"] for m in st.session_state.messages
            )

            # Display and store response
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error generating response: {e}")
