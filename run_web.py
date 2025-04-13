import subprocess
import webbrowser
import time

def run_streamlit():
    # Open Streamlit app
    webbrowser.open("http://localhost:8501")
    subprocess.run(["streamlit", "run", "app.py"])

if __name__ == "__main__":
    print("Launching AI Translator Web App...")
    time.sleep(1)
    run_streamlit()
