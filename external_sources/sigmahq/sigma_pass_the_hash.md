# Sigma Rule - Pass the Hash Detection

## Rule Title

Potential Pass the Hash Activity

## ATT&CK Mapping

- T1550.002 Pass the Hash

## Log Source

Windows Security

## Detection Logic

Monitor:

- Event ID 4624
- Logon Type 3
- NTLM Authentication
- Privileged Accounts

## Investigation Steps

1. Review source host.
2. Review destination host.
3. Review account used.
4. Review lateral movement activity.
5. Review credential dumping activity.

## Sigma Concepts

selection:
  EventID: 4624
  LogonType: 3

condition:
  selection

## Analyst Notes

Pass the Hash is often observed after credential dumping and before lateral movement.
