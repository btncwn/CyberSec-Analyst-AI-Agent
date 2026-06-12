# T1059.001 - PowerShell

## Description

PowerShell is frequently abused by attackers for execution, persistence, discovery, and lateral movement.

## Suspicious Indicators

- EncodedCommand
- Invoke-WebRequest
- DownloadString
- IEX
- Base64 strings
- HiddenWindow

## Detection

Sysmon Event ID 1

PowerShell process creation.

## Investigation

Review:

- User
- Parent Process
- Command Line
- Network Activity

## Related ATT&CK

- T1027 Obfuscated Files or Information
- T1105 Ingress Tool Transfer
