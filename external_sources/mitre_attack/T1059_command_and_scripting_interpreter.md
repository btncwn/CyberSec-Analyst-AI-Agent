# T1059 - Command and Scripting Interpreter

## Description

Adversaries may abuse command and script interpreters to execute commands, run scripts, and perform malicious actions on systems.

## Common Examples

- PowerShell
- CMD
- Bash
- Python
- WScript
- CScript

## Detection Opportunities

- PowerShell with EncodedCommand
- Suspicious command-line arguments
- Script execution from temporary directories
- LOLBAS abuse

## Investigation Steps

- Review process creation logs
- Review parent-child process relationships
- Review command-line arguments
- Review network connections

## Related Techniques

- T1059.001 PowerShell
- T1059.003 Windows Command Shell
