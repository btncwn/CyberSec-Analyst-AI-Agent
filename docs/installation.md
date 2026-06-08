# Installation Guide

## Prerequisites

* macOS, Linux, or Windows
* Python 3.10+
* Ollama
* Git

---

## Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/CyberSec-Analyst-AI-Agent.git
cd CyberSec-Analyst-AI-Agent
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

## Download Model

```bash
ollama pull llama3.2:3b
```

Verify:

```bash
ollama list
```

---

## Start Ollama

```bash
ollama serve
```

---

## Launch Application

```bash
streamlit run app.py
```

---

## Access Application

Open:

```text
http://localhost:8501
```

---

## Available Modules

1. Incident Report Generator
2. Threat Hunting Assistant
3. Sigma Rule Generator
4. Splunk Query Generator
5. MITRE ATT&CK Mapper
6. Detection Engineering Assistant
7. Threat Intelligence Assistant

---

## Troubleshooting

### Ollama Not Running

```bash
ollama serve
```

### Verify Installed Models

```bash
ollama list
```

### Verify Python Packages

```bash
pip list
```

