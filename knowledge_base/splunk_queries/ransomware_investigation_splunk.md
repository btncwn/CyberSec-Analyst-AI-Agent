# Ransomware Investigation Splunk Searches

## Process Creation Investigation

### Sysmon Event ID 1

```spl
index=sysmon EventCode=1
| stats count by Image CommandLine ParentImage User
| sort -count
```

Purpose:

- Identify suspicious processes
- Review parent-child relationships
- Detect attacker tooling

---

## PowerShell Investigation

```spl
index=sysmon EventCode=1 Image="*powershell.exe"
| table _time Computer User CommandLine ParentImage
```

Purpose:

- Detect encoded commands
- Detect malicious scripts
- Detect ransomware staging activity

---

## Certutil Investigation

```spl
index=sysmon EventCode=1 Image="*certutil.exe"
| table _time Computer User CommandLine ParentImage
```

Purpose:

- Detect payload downloads
- Identify LOLBAS abuse

---

## DNS Investigation

```spl
index=dns
| stats count by query
| sort -count
```

Purpose:

- Identify suspicious domains
- Identify command and control traffic

---

## Ransom Note Detection

```spl
index=sysmon EventCode=11
(TargetFilename="*README*" OR TargetFilename="*RECOVER*" OR TargetFilename="*DECRYPT*")
```

Purpose:

- Detect ransomware note creation
- Identify affected systems

---

## Analyst Notes

Always build a timeline:

1. Initial access
2. Execution
3. Persistence
4. Lateral movement
5. Impact
