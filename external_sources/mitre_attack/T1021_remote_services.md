# T1021 - Remote Services

## Description

Adversaries may use valid accounts and remote services to move laterally across a network.

This is commonly seen during ransomware intrusions after credential access or privilege escalation.

## Common Remote Services

- RDP
- SMB
- WinRM
- SSH
- PsExec
- WMI

## Common Indicators

- Logons from unusual source hosts
- Administrative account usage
- Lateral movement between endpoints
- Remote command execution
- Access to administrative shares
- New services created remotely

## Detection Opportunities

- Windows Event ID 4624
- Windows Event ID 4625
- Windows Event ID 4672
- Sysmon Event ID 1
- Sysmon Event ID 3
- Service creation events

## Investigation Steps

1. Identify source and destination hosts.
2. Review authentication logs.
3. Review account used for remote access.
4. Check for administrative share access.
5. Review remote process creation.
6. Review newly created services.
7. Determine whether credential dumping occurred before lateral movement.

## Related ATT&CK Techniques

- T1003 Credential Dumping
- T1550.002 Pass the Hash
- T1059 Command and Scripting Interpreter
- T1486 Data Encrypted for Impact

## Splunk Hunting Example

```spl
index=wineventlog (EventCode=4624 OR EventCode=4672)
| stats count by Account_Name Workstation_Name Source_Network_Address Logon_Type
| sort -count
