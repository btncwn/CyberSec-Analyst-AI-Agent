Focus on:

ADMIN$
C$
IPC$
PsExec
Lateral movement
Remote execution
# T1021.002 - SMB / Windows Admin Shares

## Description

Attackers may use SMB administrative shares to move laterally across systems.

## Common Shares

- ADMIN$
- C$
- IPC$

## Common Tools

- PsExec
- CrackMapExec
- Impacket
- smbexec.py

## Indicators

- Access to ADMIN$
- Service creation
- Remote execution
- New executable deployment

## Investigation Steps

1. Review SMB authentication.
2. Review administrative share access.
3. Review service creation.
4. Review process execution.
5. Review lateral movement timeline.

## Related ATT&CK

- T1021
- T1550.002
- T1003
