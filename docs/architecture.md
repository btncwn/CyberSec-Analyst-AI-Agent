# Personal Cyber Security Analyst AI Agent - Architecture

## Overview

The Personal Cyber Security Analyst AI Agent is a locally hosted AI-powered cyber security assistant designed to support defensive security operations, threat hunting, detection engineering, incident response, and threat intelligence workflows.

The solution uses a local Large Language Model (LLM) through Ollama and provides a web-based interface using Streamlit.

Authentication is not implemented in version 1 because the application is intended to run locally in a lab environment. If deployed on a shared network or server, authentication and access control should be added before use.

No cloud-based AI services are required.

---

## Architecture

```text
User
  │
  ▼
Streamlit Web Interface
  │
  ▼
Personal Cyber Security Analyst AI Agent
  │
  ▼
Ollama API
  │
  ▼
Llama 3.2 Local Model
  │
  ├── Incident Report Generator
  ├── Threat Hunting Assistant
  ├── Sigma Rule Generator
  ├── Splunk Query Generator
  ├── MITRE ATT&CK Mapper
  ├── Detection Engineering Assistant
  └── Threat Intelligence Assistant
```

---

## Core Components

### Streamlit Interface

Provides a simple web-based interface allowing analysts to submit investigation details, detection requirements, indicators of compromise, and threat hunting scenarios.

### Ollama

Hosts the local LLM and processes requests from the analyst interface.

### Llama 3.2

Generates cyber security analysis, detection logic, incident reports, and investigation workflows.

### Prompt Modules

Each module contains specialised instructions designed for a specific cyber security workflow.

---

## Supported Workflows

### Incident Response

* Incident reporting
* Investigation summaries
* Containment recommendations
* Recovery guidance

### Threat Hunting

* Hunting hypotheses
* Data source recommendations
* ATT&CK mapping
* Investigation workflows

### Detection Engineering

* Detection logic
* Sigma rules
* Splunk SPL generation
* Tuning recommendations

### Threat Intelligence

* IOC analysis
* Threat assessment
* Enrichment opportunities
* Investigation recommendations

---

## Security Considerations

* No cloud AI dependency
* Local processing of prompts and outputs
* Suitable for lab and educational environments
* AI-generated outputs require analyst validation before operational use

---

## Future Enhancements

* MISP integration
* Sigma rule export
* Incident report export
* IOC enrichment workflows
* Vector database integration
* Knowledge base support
* Multi-model support
- Authentication and user access control
