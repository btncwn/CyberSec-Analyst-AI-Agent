# Sigma Rule - Encoded PowerShell Detection

## ATT&CK Mapping

- T1059.001 PowerShell
- T1027 Obfuscated Files or Information

## Detection Logic

Look for:

- EncodedCommand
- FromBase64String
- IEX
- DownloadString

## Investigation Steps

1. Extract command line.
2. Decode Base64 content.
3. Identify downloaded payload.
4. Review network activity.
5. Determine attacker objective.

## Sigma Concepts

selection:
  CommandLine|contains:
    - EncodedCommand
    - IEX
    - FromBase64String

condition:
  selection

## Analyst Notes

Frequently observed during malware execution and ransomware staging.
