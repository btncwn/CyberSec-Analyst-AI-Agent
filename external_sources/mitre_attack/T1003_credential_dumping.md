# T1003 - OS Credential Dumping

## Description

Adversaries may attempt to dump credentials from operating system memory, files, or security databases to obtain account credentials.

## Common Examples

- LSASS memory dumping
- SAM database extraction
- NTDS.dit extraction
- Credential theft tools
- Mimikatz-like behaviour

## Detection Opportunities

- Suspicious access to lsass.exe
- Dump files created from LSASS
- Use of procdump
- Suspicious rundll32 activity
- Access to SAM, SYSTEM, or SECURITY registry hives

## Investigation Steps

- Review process creation logs
- Review command-line arguments
- Review access to lsass.exe
- Review file creation events for dump files
- Review privileged account activity

## Related Techniques

- T1003.001 LSASS Memory
- T1059 Command and Scripting Interpreter
- T1021 Remote Services
