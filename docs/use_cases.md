# Use Cases

## Overview

The Personal Cyber Security Analyst AI Agent is designed to support defensive cyber security workflows by assisting analysts with investigation, detection engineering, threat hunting, threat intelligence, and incident response activities.

---

# Use Case 1 – Incident Response

## Scenario

A suspicious PowerShell execution alert is detected by Splunk.

## Analyst Input

* Alert details
* Hostname
* User account
* Sysmon logs
* Windows Event Logs

## Agent Output

* Executive Summary
* Timeline of Events
* Technical Analysis
* MITRE ATT&CK Mapping
* Containment Recommendations
* Recovery Recommendations

---

# Use Case 2 – Threat Hunting

## Scenario

An analyst suspects malicious PowerShell activity within the environment.

## Analyst Input

* Hunting hypothesis
* Initial indicators
* Observed behaviours

## Agent Output

* Threat Hunting Plan
* ATT&CK Techniques
* Data Sources
* Splunk Searches
* Investigation Workflow
* Escalation Criteria

---

# Use Case 3 – Sigma Rule Generation

## Scenario

A detection engineer needs a Sigma rule for suspicious PowerShell activity.

## Analyst Input

* Detection requirement
* Threat behaviour

## Agent Output

* Sigma Rule YAML
* Detection Logic
* ATT&CK Mapping
* False Positives
* Tuning Guidance

---

# Use Case 4 – Splunk Query Generation

## Scenario

An analyst requires a Splunk SPL query to identify suspicious activity.

## Analyst Input

* Detection objective
* Available log sources

## Agent Output

* SPL Query
* Query Explanation
* ATT&CK Mapping
* Tuning Recommendations

---

# Use Case 5 – MITRE ATT&CK Mapping

## Scenario

An analyst needs to understand which ATT&CK techniques are associated with observed activity.

## Analyst Input

* Observed behaviours
* Alert details
* Investigation findings

## Agent Output

* ATT&CK Tactics
* ATT&CK Techniques
* Confidence Assessment
* Detection Opportunities

---

# Use Case 6 – Detection Engineering

## Scenario

A detection engineer wants to build a detection for suspicious process execution.

## Analyst Input

* Threat scenario
* Detection requirement

## Agent Output

* Detection Logic
* Sigma Rule
* Splunk Query
* ATT&CK Mapping
* Validation Steps

---

# Use Case 7 – Threat Intelligence

## Scenario

An analyst investigates a suspicious IP address, domain, or file hash.

## Analyst Input

* IOC
* Context
* Investigation findings

## Agent Output

* Threat Assessment
* ATT&CK Mapping
* Investigation Workflow
* Detection Opportunities
* Intelligence Gaps
* Recommended Actions

---

# Intended Audience

* SOC Analysts
* Cyber Security Analysts
* Threat Hunters
* Detection Engineers
* Incident Responders
* Students and Home Lab Practitioners

---

# Limitations

* AI-generated content must be validated by a human analyst.
* Outputs should not be considered evidence without verification.
* The application is intended for educational, research, and defensive security purposes.

