# Suspicious Certutil Download Detection

## Purpose

Detect potential abuse of certutil.exe to download files from remote locations.

## ATT&CK Mapping

- T1105 Ingress Tool Transfer
- T1218 Signed Binary Proxy Execution

## Sigma Rule

```yaml
title: Suspicious Certutil Download

logsource:
  product: windows

detection:
  selection:
    Image|endswith:
      - '\certutil.exe'
    CommandLine|contains:
      - 'http'
      - 'https'
      - '-urlcache'

  condition: selection

level: high
```

## Investigation Steps

1. Review command line arguments
2. Identify source URL
3. Determine downloaded file
4. Check file hash
5. Review parent process
6. Review network activity

## False Positives

- Administrative software deployment
- Internal certificate management

## Analyst Notes

Certutil is a common LOLBAS utility frequently abused by threat actors to download malware while bypassing application controls.
