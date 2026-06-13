# Splunk Detection - Ransomware Activity

## ATT&CK Mapping

- T1486 Data Encrypted for Impact
- T1059 Command and Scripting Interpreter
- T1105 Ingress Tool Transfer
- T1021 Remote Services

## Detection Objective

Identify ransomware behaviours such as backup deletion, shadow copy deletion, ransom note creation, suspicious PowerShell, and high-impact file activity.

## Key Data Sources

- Sysmon Event ID 1 - Process Creation
- Sysmon Event ID 11 - File Creation
- Windows Security Logs
- DNS Logs
- Proxy/Web Logs

## Suspicious Indicators

- vssadmin delete shadows
- wbadmin delete catalog
- bcdedit recovery changes
- ransom note creation
- suspicious PowerShell execution
- unusual file modification activity
- lateral movement before encryption

## Splunk Searches

### Shadow Copy Deletion

```spl
index=sysmon EventCode=1
CommandLine="*vssadmin delete shadows*"
| table _time Computer User Image CommandLine ParentImage



Backup Deletion
index=sysmon EventCode=1
CommandLine="*wbadmin delete catalog*"
| table _time Computer User Image CommandLine ParentImage



Ransom Note Creation

index=sysmon EventCode=11
(TargetFilename="*README*" OR TargetFilename="*RECOVER*" OR TargetFilename="*DECRYPT*" OR TargetFilename="*HELP*")
| table _time Computer User Image TargetFilename

Suspicious PowerShell Before Encryption

index=sysmon EventCode=1 Image="*powershell.exe"
(CommandLine="*EncodedCommand*" OR CommandLine="*IEX*" OR CommandLine="*DownloadString*" OR CommandLine="*Invoke-WebRequest*")
| table _time Computer User CommandLine ParentImage


Investigation Steps
Identify affected systems.
Identify the encryption process.
Review process creation before encryption.
Review PowerShell and command shell activity.
Check for backup or shadow copy deletion.
Identify ransom note files.
Review lateral movement activity.
Determine initial access vector.
Preserve evidence before recovery.
Analyst Notes

Ransomware investigations should focus on identifying the initial access vector, staging activity, credential access, lateral movement, encryption activity, and recovery impact.
