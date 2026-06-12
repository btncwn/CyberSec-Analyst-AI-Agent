# Enterprise Ransomware Incident Response Workflow

## Identification

### Indicators

- Mass file encryption
- Ransom note creation
- Suspicious PowerShell activity
- Unusual SMB traffic
- Security tool tampering

### Initial Triage

Collect:

- Hostname
- Username
- Time detected
- Initial alert source
- Running processes
- Network connections

---

## Containment

### Immediate Actions

- Isolate affected endpoints
- Disable compromised accounts
- Block malicious IPs and domains
- Preserve volatile evidence

---

## Eradication

### Investigation

- Identify initial access vector
- Identify persistence mechanisms
- Identify lateral movement activity
- Identify impacted systems

---

## Recovery

### Recovery Actions

- Restore systems from backups
- Reset credentials
- Validate systems
- Monitor for reinfection

---

## MITRE ATT&CK Techniques

- T1059 Command and Scripting Interpreter
- T1105 Ingress Tool Transfer
- T1486 Data Encrypted for Impact
- T1021 Remote Services

---

## Evidence Collection

### Windows

- Security Logs
- Sysmon Logs
- PowerShell Logs

### Network

- Firewall Logs
- DNS Logs
- Proxy Logs

---

## Lessons Learned

- Timeline creation
- Detection improvements
- Sigma rule opportunities
- ATT&CK mapping updates
