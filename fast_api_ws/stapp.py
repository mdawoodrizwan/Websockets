import streamlit as st
from websocket import create_connection

# URL of the WebSocket
ws_url = "ws://localhost:8000/ws"

# Create a Streamlit interface
st.title('WebSocket Client')

# Maintain the WebSocket connection in session state
if 'ws' not in st.session_state:
    st.session_state.ws = create_connection(ws_url)

# Input for sending a message
user_input = st.text_input("Send a message to the WebSocket:")

if st.button('Send'):
    if user_input:  # Ensure the input is not empty
        # Send the message
        st.session_state.ws.send(user_input)

        # Receive and print the response
        response = st.session_state.ws.recv()
        st.write("Received:", response)
    else:
        st.write("Please enter a message to send.")

# Optionally close the connection
if st.button('Close Connection'):
    st.session_state.ws.close()
    del st.session_state.ws
    st.write("Connection closed.")
