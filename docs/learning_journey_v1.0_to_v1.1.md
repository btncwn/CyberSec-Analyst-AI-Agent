# Personal Cyber Security Analyst AI Agent

## Learning Journey Report (v1.0 → v1.1)

---

# Introduction

This project began with a simple question:

**"Can I build my own local AI cyber security analyst?"**

At the beginning, I had limited Python development experience and no previous experience building AI-powered applications.

The goal was not to replace security analysts.

Instead, the goal was to build an AI assistant capable of supporting common Security Operations Centre (SOC) activities such as:

* Incident Response
* Threat Hunting
* Threat Intelligence
* Detection Engineering
* Sigma Rule Development
* Splunk Query Generation
* MITRE ATT&CK Mapping

A secondary goal was to learn how modern AI systems actually work and understand their strengths and weaknesses when applied to cyber security investigations.

---

# Understanding the Technology Stack

Before building the application, it was important to understand the purpose of each component.

Think of the application as a team of workers.

Each worker has a specific responsibility.

---

# Python

Python is the foundation of the application.

Think of Python as the project manager.

Python controls everything:

* Reads uploaded files
* Processes data
* Displays information
* Sends requests to the AI model
* Receives responses
* Generates reports

Without Python:

Nothing happens.

Python coordinates every part of the application.

---

# Streamlit

Streamlit converts Python code into a web application.

Without Streamlit:

```text
Python Script
↓
Terminal Output
```

With Streamlit:

```text
Python Script
↓
Interactive Web Application
```

This is why the application can be opened in a browser at:

```text
http://localhost:8501
```

instead of running entirely inside a terminal.

Streamlit provided:

* Text boxes
* Upload buttons
* Download buttons
* Dropdown menus
* Interactive results

---

# Ollama

Ollama allows Large Language Models to run locally.

Normally AI applications work like this:

```text
User
↓
Internet
↓
OpenAI / Cloud Provider
↓
AI Response
```

Our application works differently:

```text
User
↓
Laptop
↓
Local AI Model
↓
AI Response
```

Benefits:

* Privacy
* No API costs
* Offline operation
* Complete control

This is extremely useful when analysing security logs because sensitive data never leaves the machine.

---

# Llama 3.2 3B

Llama 3.2 is the AI model itself.

Think of the AI model as the analyst.

The model receives:

* Instructions
* Investigation notes
* Log data

and produces:

* Reports
* Assessments
* Recommendations

The model does not understand cyber security automatically.

It must be guided.

This is where Prompt Engineering becomes important.

---

# Prompt Engineering

Prompt Engineering means teaching the AI how to think.

Example:

Without instructions:

```text
Analyse these logs.
```

The AI may produce generic output.

With instructions:

```text
You are a SOC Threat Intelligence Analyst.

Focus on:

- Suspicious IPs
- Exploitation attempts
- Web shells
- MITRE ATT&CK

Ignore:

- SEO metrics
- Marketing statistics
- Browser popularity
```

The quality of output improves dramatically.

This was one of the biggest lessons of the project.

AI performance depends heavily on instructions.

---

# Version 1.0

The first version created seven analyst modules.

## Incident Report Generator

Creates incident reports.

---

## Threat Hunting Assistant

Assists with threat hunting investigations.

---

## Sigma Rule Generator

Generates Sigma detection rules.

---

## Splunk Query Generator

Generates Splunk SPL searches.

---

## MITRE ATT&CK Mapper

Maps activity to ATT&CK techniques.

---

## Detection Engineering Assistant

Assists with creating detection logic.

---

## Threat Intelligence Assistant

Performs threat intelligence investigations.

---

# First Major Problem

Initially the application only accepted text.

Example:

```text
Paste logs manually.
```

Problem:

Real analysts rarely work this way.

They usually investigate:

* CSV exports
* Sysmon logs
* SIEM exports
* Endpoint telemetry

The application was unrealistic.

---

# Version 1.1

## File Upload Capability

We introduced:

```python
uploaded_file = st.file_uploader(...)
```

For a beginner Python learner:

This line creates an upload button.

Before:

```text
Copy
↓
Paste
↓
Analyse
```

After:

```text
Upload File
↓
Analyse
```

This small feature made the application much more practical.

---

# The Second Major Problem

After CSV uploads were added, another issue appeared.

The AI started making poor decisions.

Example output:

```text
DDoS Attack
SEO Statistics
Browser Analytics
```

Why?

Because the AI was attempting to analyse hundreds of raw log entries at once.

The model became distracted by irrelevant information.

---

# Understanding AI Hallucinations

This was one of the most important lessons.

A hallucination occurs when AI produces information that is not supported by evidence.

Example:

Observed:

```text
54 requests from an IP
```

AI conclusion:

```text
DDoS Attack
```

Problem:

54 requests is not evidence of a DDoS attack.

The AI guessed.

This taught a critical SOC lesson:

Evidence and conclusions are not the same thing.

Analysts must verify claims.

---

# The Intelligence Layer

This became the biggest improvement in the entire project.

We introduced Pandas.

---

# What Is Pandas?

Pandas is a Python data analysis library.

Think of it as:

```text
Excel
+
Python
```

Pandas allows Python to:

* Read CSV files
* Count events
* Identify top IPs
* Identify top URLs
* Summarise large datasets

---

# The Most Important Code Change

Before:

```text
CSV
↓
AI
↓
Poor Analysis
```

After:

```text
CSV
↓
Pandas
↓
Summary
↓
AI
↓
Better Analysis
```

---

# What This Code Does

```python
df = pd.read_csv(uploaded_file)
```

Meaning:

```text
Read CSV file
↓
Convert to table
↓
Store in memory
```

The variable:

```python
df
```

stands for:

DataFrame

A DataFrame is essentially a spreadsheet inside Python.

---

# Counting Source IPs

```python
df['src_ip'].value_counts()
```

Meaning:

```text
Look at source IP column
↓
Count occurrences
↓
Sort highest to lowest
```

Result:

```text
61.75.35.114 54
45.7.231.174 40
```

Now the AI receives useful intelligence.

---

# Why The AI Improved

Before:

The model saw:

```text
164 raw rows
```

After:

The model saw:

```text
Top Source IPs
Top URI Paths
HTTP Status Codes
```

The AI was no longer searching for patterns.

Python had already found them.

This significantly reduced hallucinations.

---

# BOTS v3 Investigation

The application was tested using Splunk BOTS v3 HTTP telemetry.

Query used:

index=botsv3 sourcetype=stream:http http_method=POST
| search uri_path="*.php"
| table _time src_ip dest_ip uri_path status http_user_agent

Purpose:

Identify suspicious PHP activity.

Examples observed:

* cmd.php
* ak47.php
* qq.php
* qaq.php

These names are commonly investigated because attackers frequently use similar filenames when deploying web shells.

---

# MITRE ATT&CK

MITRE ATT&CK is a framework used by defenders.

Think of it as:

A catalogue of attacker behaviour.

Example:

T1190

Exploit Public-Facing Application

T1505.003

Web Shell

Instead of saying:

"Hacker Activity"

we can say:

"This behaviour resembles ATT&CK technique T1190."

This creates professional, structured investigations.

---

# Most Important Lessons Learned

Technical Skills:

* Python fundamentals
* Streamlit development
* Local AI deployment
* CSV processing
* Pandas
* Git
* GitHub
* Prompt Engineering

Cyber Security Skills:

* Splunk investigations
* Threat hunting
* Threat intelligence
* IOC analysis
* MITRE ATT&CK mapping
* Evidence-based analysis

AI Skills:

* Prompt engineering
* Hallucination reduction
* Data preprocessing
* Local LLM operation
* AI-assisted investigations

---

# Final Reflection

The most valuable lesson was not learning Python.

The most valuable lesson was learning that:

AI is not intelligence.

AI is pattern prediction.

Good cyber security analysis still requires:

* Evidence
* Validation
* Analyst judgement

The purpose of AI is not to replace analysts.

The purpose of AI is to help analysts investigate faster and focus on higher-value decision making.

This project evolved from:

"An AI chatbot"

into

"An AI-Assisted SOC Investigation Platform."

More importantly, it provided practical experience in combining Python, AI, threat hunting and security operations into a real-world security workflow.

