# GitHub Challenge

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey there!

Your challenge is ready.
Follow the instructions provided for this challenge and complete the required tasks in this repository.

Make sure your work is committed and pushed to your repository before submission.

Good luck!


---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

## Overview

### Service Being Monitored
The system monitors an internal microservice environment processing operational telemetry data, including response latency, host CPU/memory utilization metrics, and system log levels (`INFO`, `WARN`, `ERROR`).

### Operational Problem Being Addressed
Manual monitoring and static alerting often fail to catch complex service degradation or result in alert fatigue. Uncoordinated telemetry makes it difficult to quickly isolate performance bottlenecks (e.g., CPU spikes, elevated latencies) and critical log errors in real-time across disparate system components.

### Purpose of AIOps in this Assessment
The goal of implementing AIOps in this challenge is to demonstrate automated telemetry processing and anomaly detection. By routing detected anomalies through an event-driven architecture (Producer → Topic → Consumer), the system automates fault identification and streamlines incident analysis without human intervention.

