Focus on:

Failed logons
Password spraying
Event IDs 4625
Account lockouts
# T1110 - Brute Force

## Description

Attackers may attempt to gain access by repeatedly trying passwords.

## Common Variants

- Password guessing
- Password spraying
- Credential stuffing

## Detection Opportunities

### Windows Event IDs

- 4625 Failed Logon
- 4624 Successful Logon
- 4740 Account Lockout

## Investigation Steps

1. Review failed logons.
2. Identify source IP.
3. Identify targeted accounts.
4. Review successful authentication events.
5. Determine attack scope.

## Splunk Hunting Example

```spl
index=wineventlog EventCode=4625
| stats count by Account_Name Source_Network_Address
| sort -count

Related ATT&CK
T1078
T1550
