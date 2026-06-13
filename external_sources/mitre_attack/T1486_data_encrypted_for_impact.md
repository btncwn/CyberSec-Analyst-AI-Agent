Focus on:

Mass file encryption
Ransom note creation
Shadow copy deletion
Backup deletion
Encryption processes
Investigation workflow
Splunk hunting
# T1486 - Data Encrypted for Impact

## Description

Adversaries may encrypt data to interrupt availability and extort victims.

This technique is commonly associated with ransomware attacks.

## Common Indicators

- Mass file encryption
- Ransom note creation
- Shadow copy deletion
- Backup deletion
- High-volume file modifications
- Unusual process activity

## Common Commands

### Shadow Copy Deletion

```cmd
vssadmin delete shadows /all /quiet

Backup Deletion

wbadmin delete catalog -quiet

Detection Opportunities
Sysmon Event ID 1

Monitor:

vssadmin.exe
wbadmin.exe
powershell.exe
cmd.exe
Sysmon Event ID 11

Monitor:

Ransom note creation
Large numbers of file creation events
Investigation Steps
Identify affected systems.
Identify encryption process.
Review process creation logs.
Review PowerShell activity.
Review lateral movement activity.
Review backup deletion activity.
Determine initial access vector.
Related ATT&CK Techniques
T1059
T1021
T1105
T1003
Splunk Hunting Example

index=sysmon EventCode=1
(CommandLine="*vssadmin delete shadows*" OR CommandLine="*wbadmin delete catalog*")
| table _time Computer User Image CommandLine
