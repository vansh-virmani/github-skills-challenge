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

## TASK2: Data Analysis & Observations

### 1. Metrics Fields
* `response_time_ms`: Service latency in milliseconds.
* `cpu_percent`: Host CPU utilization percentage.
* `memory_percent`: Host RAM/memory usage percentage.

### 2. Log Fields
* `log_level`: Severity level of the log message (`INFO`, `WARN`, `ERROR`).
* `message`: Text description of the logged event or system status.

### 3. Timestamp Usage
* `timestamp`: ISO 8601 formatted string (e.g., `2026-03-30T10:00:00Z`).
* **Usage:** Timestamps provide chronological ordering of operational telemetry, allowing the system to track performance trends over time, correlate metric anomalies with concurrent log events, and trace incident progression.

### 4. Normal Observations
Observations representing healthy service conditions exhibit:
* Low response latency (~120ms – 150ms)
* Moderate host resource usage (`cpu_percent` ~ 40%–55%, `memory_percent` ~ 50%–60%)
* `log_level` set to `INFO` with successful execution logs (e.g., `"Payment request processed successfully"`)

### 5. Unusual / Anomalous Observations
Observations representing performance degradation or failure exhibit:
* **Latency Spikes:** `response_time_ms` exceeding threshold limits (e.g., spiking over 1000ms / 2500ms).
* **Resource Exhaustion:** Extreme CPU utilization (`cpu_percent` > 85%–90%) or RAM saturation (`memory_percent` > 85%–90%).
* **Elevated Log Errors:** Records with `WARN` or `ERROR` log levels indicating failed backend requests, database connection timeouts, or unhandled exceptions.


### task3

## Part 3: Anomaly Detection Findings

### Detection Analysis
* **Anomalies Detected:** Successfully isolated records with response times over 1000ms, CPU/memory usage above 85%, and log levels flagged as `WARN` or `ERROR`.
* **Accuracy:**
  * **Missed Anomalies:** None observed; all breached conditions were flagged.
  * **False Positives:** None; baseline healthy observations returned `None`.

### Limitations & Improvements
* **Limitation:** Static thresholding does not dynamically adjust to scheduled high-traffic spikes or seasonal baseline changes.
* **Possible Improvement:** Replace fixed thresholds with statistical anomaly detection (e.g., rolling standard deviation / Z-score) or dynamic baseline monitoring.

### task 5

Identify the Affected Component
The issue was identified by running the pipeline and test suite to observe the failing behavior. The affected component was the anomaly detection and event-processing flow in the repository, specifically the modules responsible for telemetry analysis and event publication/consumption.

Determine the Cause
The root cause was a combination of:
threshold logic that did not align with the assessment requirements
incorrect handling of warning/error log levels
an event flow that needed to be verified from data ingestion through anomaly detection, publishing, topic storage, and consumer retrieval
The investigation confirmed that the telemetry data in service_data.json contained abnormal records requiring detection based on:

response time greater than 1000 ms
CPU utilization above 85%
memory utilization above 85%
WARN / ERROR log levels being flagged with correct reason strings
Apply Corrections
A minimal fix was applied within the existing architecture:

updated anomaly thresholds in anomaly_detector.py
corrected warning/error reason labeling
kept the event-driven producer/topic/consumer structure intact
added clear runtime output to confirm the event lifecycle
Execute and Verify
The pipeline and tests were re-run to verify that the issue was resolved.

Verified result:

Records processed: 10
Anomalies detected: 2
Events consumed: 2
This confirms that data successfully moved through:

Data ingestion
Anomaly detection
Producer publishing
Topic queue
Consumer consumption
Downstream AIOps processing