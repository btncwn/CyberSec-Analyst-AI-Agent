# T1027 - Obfuscated Files or Information

## Description

Adversaries may obfuscate files, commands, scripts, payloads, or other information to evade security controls, hinder analysis, and delay detection.

Obfuscation is commonly used during malware execution, ransomware deployment, PowerShell abuse, payload delivery, and command-and-control activity.

## Common Obfuscation Techniques

### PowerShell Obfuscation

* EncodedCommand
* Base64 encoded payloads
* String concatenation
* Character substitution
* Invoke-Expression (IEX)
* Hidden PowerShell windows

### Malware Obfuscation

* Packed executables
* Compressed payloads
* XOR encoding
* Encrypted payloads
* Obfuscated configuration files

### Script Obfuscation

* Variable renaming
* Character replacement
* String splitting
* Dynamic execution

## Common Indicators

* Long Base64 strings
* Encoded PowerShell commands
* Excessive use of special characters
* Suspicious use of IEX
* Hidden execution flags
* Downloads followed by execution
* Unusual parent-child process relationships

## Detection Opportunities

### PowerShell

Look for:

* EncodedCommand
* FromBase64String
* IEX
* DownloadString
* Invoke-WebRequest

### Sysmon

#### Event ID 1

Process Creation

Review:

* Image
* CommandLine
* ParentImage
* User

### Windows Security Logs

Review:

* PowerShell operational logs
* Process creation events
* Script block logging

## Investigation Steps

1. Extract the full command line.
2. Decode Base64 content when present.
3. Identify downloaded files or payloads.
4. Review parent-child process relationships.
5. Determine execution source.
6. Review network communications.
7. Review persistence mechanisms.
8. Determine attacker objectives.

## Related ATT&CK Techniques

* T1059 Command and Scripting Interpreter
* T1059.001 PowerShell
* T1105 Ingress Tool Transfer
* T1486 Data Encrypted for Impact
* T1003 Credential Dumping

## Splunk Hunting Example

```spl
index=sysmon EventCode=1
(CommandLine="*EncodedCommand*" OR
 CommandLine="*FromBase64String*" OR
 CommandLine="*IEX*" OR
 CommandLine="*DownloadString*")
| table _time Computer User Image ParentImage CommandLine
```

## Threat Hunting Questions

* Was PowerShell used?
* Was the command encoded?
* Did a download occur before execution?
* Was the payload executed?
* Were additional hosts affected?
* Was persistence established?
* Was credential access attempted?

## Analyst Notes

T1027 is frequently observed alongside PowerShell abuse, malware delivery, ransomware staging, credential theft, and post-exploitation activity. During investigations, decoding and understanding the original command or payload is often critical to identifying attacker objectives and determining incident scope.

