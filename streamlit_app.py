import streamlit as st
from ai_agent import AI_Agent

# Instantiate AI agent
ai_agent = AI_Agent()

# Define Streamlit app
def app():
    # Set app title
    st.title("AI-Driven Plugin Testing")

    # Add input fields for required information
    name = st.text_input("Customer name")
    email = st.text_input("Customer email")
    phone = st.text_input("Customer phone number")
    message = st.text_area("Message")

    # Add button to trigger communication automation
    if st.button("Send Message"):
        ai_agent.send_message(name, email, phone, message)

# Run Streamlit app
if __name__ == "__main__":
    app()
