# IOC Investigation Workflow

## IOC Types

- IP Address
- Domain
- URL
- File Hash
- Email Address

## Investigation Process

1. Identify IOC type.
2. Determine source of IOC.
3. Review internal telemetry.
4. Search SIEM.
5. Search EDR.
6. Search DNS logs.
7. Search Proxy logs.
8. Search Email logs.
9. Determine scope.
10. Determine impact.

## Analyst Questions

- Is the IOC malicious?
- Has it communicated internally?
- Which hosts are affected?
- Which users are affected?
- What ATT&CK techniques are involved?

## Containment Actions

- Block IP
- Block Domain
- Isolate Host
- Disable Account
- Create Detection Rule
