# SOC Analyst Lab

A practical Security Operations Center (SOC) home lab built with Wazuh, TheHive, Velociraptor, Volatility, and more.

## Tools Included

| Tool              | Purpose                          | Status     |
|-------------------|----------------------------------|----------|
| **Wazuh**         | SIEM / XDR / Threat Detection    | ✅ Running |
| **TheHive**       | Incident Response & Case Management | ⚠️ Running |
| **Velociraptor**  | Live Response & Digital Forensics| Partial |
| **Volatility 3**  | Memory Forensics                 | ✅ Ready |
| **Ansible**       | Automation                       | Ready |

## Architecture

- **Detection Layer**: Wazuh + Zeek (planned)
- **Response Layer**: TheHive + Velociraptor
- **Forensics Layer**: Volatility + Autopsy

## Setup Instructions

### 1. Wazuh
```bash
cd wazuh-docker/single-node
docker compose up -d
