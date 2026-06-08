import requests
import streamlit as st
from pathlib import Path

APP_TITLE = "Personal Cyber Security Analyst AI Agent"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"

BASE_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = BASE_DIR / "prompts"

MODULES = {
    "Incident Report Generator": "incident_report.md",
    "Threat Hunting Assistant": "threat_hunting.md",
    "Sigma Rule Generator": "sigma_rule.md",
    "Splunk Query Generator": "splunk_query.md",
    "MITRE ATT&CK Mapper": "mitre_mapper.md",
    "Detection Engineering Assistant": "detection_engineering.md",
    "Threat Intelligence Assistant": "threat_intelligence.md",
}


def load_prompt(filename):
    path = PROMPTS_DIR / filename
    return path.read_text(encoding="utf-8")


def call_ollama(system_prompt, user_prompt):
    full_prompt = f"""
SYSTEM ROLE:
{system_prompt}

USER REQUEST:
{user_prompt}

Return a structured cyber security analyst response.
"""

    payload = {
        "model": MODEL,
        "prompt": full_prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()
        return response.json().get("response", "No response returned.")
    except requests.exceptions.ConnectionError:
        return "Error: Ollama is not running. Start it with: ollama serve"
    except requests.exceptions.Timeout:
        return "Error: Ollama request timed out. Try a shorter prompt."
    except Exception as e:
        return f"Error: {e}"


st.set_page_config(page_title=APP_TITLE, layout="wide")

st.title(APP_TITLE)

st.markdown("""
This local AI assistant supports practical cyber security workflows including
incident response, threat hunting, detection engineering, Splunk search generation,
Sigma rule drafting, MITRE ATT&CK mapping, and threat intelligence analysis.

**Model:** llama3.2:3b via local Ollama
""")

module_name = st.sidebar.selectbox("Choose Analyst Module", list(MODULES.keys()))

st.subheader(module_name)

user_input = st.text_area(
    "Enter your alert details, logs, detection idea, IOC, or investigation notes:",
    height=280,
    placeholder="Example: PowerShell executed with an encoded command and connected to a suspicious external IP..."
)

if st.button("Run Cyber Security Analyst Agent"):
    if not user_input.strip():
        st.warning("Please enter investigation details first.")
    else:
        with st.spinner("Running local AI analyst..."):
            system_prompt = load_prompt(MODULES[module_name])
            result = call_ollama(system_prompt, user_input)

        st.markdown("## Analyst Output")
        st.markdown(result)

        st.download_button(
            label="Download Output as Markdown",
            data=result,
            file_name=f"{module_name.lower().replace(' ', '-')}.md",
            mime="text/markdown"
        )
