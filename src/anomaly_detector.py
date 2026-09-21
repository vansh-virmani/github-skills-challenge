class AnomalyDetector:
    """Detects basic anomalies in service telemetry."""

    def __init__(
        self,
        response_time_threshold=1000,
        cpu_threshold=85,
        memory_threshold=85
    ):
        self.response_time_threshold = response_time_threshold
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold

    def detect(self, record):
        reasons = []
        response_time = float(record.get("response_time_ms", 0))
        cpu_percent = float(record.get("cpu_percent", 0))
        memory_percent = float(record.get("memory_percent", 0))
        log_level = str(record.get("log_level", "")).upper()


        if response_time > self.response_time_threshold:
            reasons.append(
                f"High response time ({response_time}ms > {self.response_time_threshold}ms)"
            )

        if cpu_percent > self.cpu_threshold:
            reasons.append(
                f"High CPU utilization ({cpu_percent}% > {self.cpu_threshold}%)"
            )

        if memory_percent > self.memory_threshold:
            reasons.append(
                f"High memory utilization ({memory_percent}% > {self.memory_threshold}%)"
            )

      
        if log_level in {"WARN", "WARNING"}:
            reasons.append("Warning log detected")
        elif log_level == "ERROR":
            reasons.append("Error log detected")

        if not reasons:
            return None

        return {
            "timestamp": record["timestamp"],
            "service": record["service"],
            "type": "ANOMALY",
            "reasons": reasons,
            "source": record
        }
