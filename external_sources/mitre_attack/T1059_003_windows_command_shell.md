Focus on:

cmd.exe
whoami
net user
net localgroup
ipconfig
systeminfo
# T1059.003 - Windows Command Shell

## Description

Attackers may abuse cmd.exe to execute commands, perform discovery, and launch payloads.

## Common Commands

- whoami
- hostname
- ipconfig
- net user
- net localgroup
- systeminfo
- tasklist

## Detection Opportunities

### Sysmon Event ID 1

Monitor:

- cmd.exe execution
- Suspicious command arguments
- Unusual parent processes

## Investigation Steps

1. Review command lines.
2. Review parent process.
3. Review user context.
4. Review network activity.
5. Determine attacker objectives.

## Related ATT&CK

- T1059
- T1027
- T1105
