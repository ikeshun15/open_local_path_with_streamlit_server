import streamlit as st
import requests
from streamlit import runtime
from streamlit.runtime.scriptrunner import get_script_run_ctx
import os
from dotenv import load_dotenv
load_dotenv()

# 環境変数を取得
FLASK_CLIENT_SERVER_PORT = os.getenv('FLASK_CLIENT_SERVER_PORT')

def get_remote_ip() -> str:
    """Get remote IP, including localhost."""
    try:
        ctx = get_script_run_ctx()
        if ctx is None:
            return None

        session_info = runtime.get_instance().get_client(ctx.session_id)
        if session_info is None:
            return None
        
        remote_ip = session_info.request.remote_ip
        
        # Handle localhost scenarios
        if remote_ip in ['127.0.0.1', '::1']:
            return 'localhost'
        
        return remote_ip
    except Exception as e:
        return None

client_server = f"http://{get_remote_ip()}:{FLASK_CLIENT_SERVER_PORT}/open_file"

st.set_page_config(page_title="Open Local Path with Streamlit", page_icon="📁", layout="centered")

st.title(body="Open Local path with Streamlit")
st.markdown(body="This application can open local path. Please use with a client server that open path.")

with st.form(key="file_path_form"):
    file_path = st.text_input(label="Enter path:", placeholder="ex) D:\Documents or D:\sample.txt")
    submit_button = st.form_submit_button(label="Send and Open Path", type="primary")

if submit_button and client_server:
    try:
        response = requests.post(client_server, json={"file_path": file_path})

        if response.status_code == 200:
            st.success(icon="🙆", body="Path sent to client server successfully!")
        else:
            st.error(icon="🙅", body=f"Failed to send path to client server. Status code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(icon="🙅", body=f"Failed to send path to client server. Error: {e}")
elif submit_button:
    st.error("No client server selected.")
