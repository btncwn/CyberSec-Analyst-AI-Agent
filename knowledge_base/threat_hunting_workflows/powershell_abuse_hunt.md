# Threat Hunt: PowerShell Abuse

## Hunt Objective

Identify potentially malicious PowerShell activity associated with malware delivery, credential access, persistence, lateral movement, or ransomware operations.

---

## Hunt Hypothesis

An attacker may be abusing PowerShell to execute malicious commands, download payloads, evade detection, or perform post-compromise actions.

---

## ATT&CK Mapping

### Execution

- T1059.001 PowerShell

### Defense Evasion

- T1027 Obfuscated Files or Information

### Command and Control

- T1105 Ingress Tool Transfer

---

## Data Sources

### Windows

- Sysmon Event ID 1
- PowerShell Operational Logs
- Windows Security Logs

### Network

- DNS Logs
- Proxy Logs
- Firewall Logs

---

## Indicators

Look for:

- EncodedCommand
- Invoke-WebRequest
- DownloadString
- IEX
- Base64 strings
- Hidden windows
- Unusual parent processes

---

## Splunk Search

```spl
index=sysmon EventCode=1 Image="*powershell.exe"
| table _time Computer User ParentImage CommandLine
```

---

## Investigation Questions

1. Who launched PowerShell?
2. What process spawned PowerShell?
3. Was a file downloaded?
4. Was PowerShell encoded?
5. Were credentials accessed?
6. Was persistence established?

---

## Evidence Collection

Collect:

- Full command line
- Parent process
- Child processes
- Related DNS activity
- Related network connections

---

## Potential Findings

### Benign

- Administrative scripting
- Software deployment
- IT automation

### Suspicious

- Encoded commands
- Download cradle activity
- Remote payload execution
- Credential dumping activity

---

## Analyst Notes

PowerShell is one of the most abused Windows utilities and should always be investigated in the context of surrounding process activity and network communications.
