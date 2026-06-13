# Splunk Detection - Credential Dumping

## ATT&CK Mapping

- T1003 Credential Dumping

## Detection Objective

Identify suspicious credential dumping behaviour, especially LSASS access, dump file creation, and tools commonly used to extract credentials.

## Key Data Sources

- Sysmon Event ID 1 - Process Creation
- Sysmon Event ID 10 - Process Access
- Windows Security Logs
- Endpoint Detection logs

## Suspicious Indicators

- procdump.exe targeting lsass.exe
- rundll32.exe loading comsvcs.dll
- lsass.exe memory access
- dump files created on disk
- suspicious PowerShell around credential access
- privileged account activity after suspected dumping

## Splunk Searches

### Suspicious Process Creation

```spl
index=sysmon EventCode=1
(Image="*procdump.exe*" OR Image="*rundll32.exe*" OR CommandLine="*comsvcs.dll*")
| table _time Computer User Image CommandLine ParentImage


LSASS Access:

index=sysmon EventCode=10 TargetImage="*lsass.exe"
| table _time Computer SourceImage TargetImage GrantedAccess CallTrace

Dump File Creation:

index=sysmon EventCode=11
(TargetFilename="*.dmp" OR TargetFilename="*lsass*")
| table _time Computer User TargetFilename Image

Investigation Steps
Identify the affected host.
Identify the user account involved.
Review process lineage.
Check whether lsass.exe was accessed.
Look for dump files.
Review nearby PowerShell or command shell activity.
Check for lateral movement after the suspected dump.
Review privileged account logons.
Analyst Notes

Credential dumping is often followed by lateral movement, Pass the Hash, remote services abuse, and ransomware deployment.
