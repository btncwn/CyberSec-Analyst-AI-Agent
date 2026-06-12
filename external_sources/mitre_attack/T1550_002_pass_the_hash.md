# T1550.002 - Pass the Hash

## Description

Pass the Hash (PtH) is a technique where attackers authenticate using NTLM password hashes instead of plaintext passwords.

Attackers commonly use Pass the Hash after obtaining credentials through credential dumping techniques such as LSASS memory access.

## Common Tools

* Mimikatz
* CrackMapExec
* Impacket
* PsExec
* wmiexec.py
* smbexec.py

## Common Indicators

* Lateral movement between systems
* SMB authentication activity
* Administrative share access (ADMIN$, C$)
* Authentication without an interactive logon
* Repeated authentication attempts using privileged accounts

## Detection Opportunities

### Windows Event Logs

* Event ID 4624
* Event ID 4625
* Event ID 4672

### Indicators

* Logon Type 3 (Network Logon)
* NTLM authentication
* Administrative account usage
* Lateral movement patterns

## Investigation Steps

1. Identify the source host.
2. Identify the destination host.
3. Review NTLM authentication events.
4. Review administrative account activity.
5. Review process creation events.
6. Review SMB and remote service activity.
7. Determine whether credential dumping occurred before authentication activity.

## Related ATT&CK Techniques

* T1003 Credential Dumping
* T1021 Remote Services
* T1059 Command and Scripting Interpreter
* T1550 Use Alternate Authentication Material

## Splunk Hunting Example

```spl
index=wineventlog EventCode=4624 Logon_Type=3
| stats count by Account_Name Workstation_Name Source_Network_Address
| sort -count
```

