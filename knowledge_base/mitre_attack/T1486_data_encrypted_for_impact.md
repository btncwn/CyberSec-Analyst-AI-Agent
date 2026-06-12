# T1486 - Data Encrypted for Impact

## Summary

Data Encrypted for Impact is a MITRE ATT&CK technique where an attacker encrypts files or systems to disrupt availability and pressure the victim into paying a ransom.

## Common Ransomware Behaviours

- Rapid file modification
- Large numbers of renamed files
- Ransom note creation
- Backup deletion
- Shadow copy deletion
- Security tool tampering

## Detection Ideas

Look for:

- High-volume file writes
- Suspicious encryption processes
- Unexpected use of vssadmin
- Unexpected use of wbadmin
- Suspicious PowerShell execution
- Ransom note file creation

## Splunk Investigation Ideas

```spl
index=sysmon EventCode=1
(CommandLine="*vssadmin delete shadows*" OR CommandLine="*wbadmin delete catalog*")
