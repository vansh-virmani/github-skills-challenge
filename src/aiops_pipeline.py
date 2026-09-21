import json

from anomaly_detector import AnomalyDetector
from event_consumer import EventConsumer
from event_producer import EventProducer
from event_topic import EventTopic


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def run_pipeline(file_path):
    data = load_data(file_path)

    # INTENTIONAL ASSESSMENT ISSUE #2
    topic = EventTopic("anomaly-events")

    detector = AnomalyDetector()
    producer = EventProducer(topic)

    # INTENTIONAL ASSESSMENT ISSUE #3
    consumer = EventConsumer(topic)

    detected_events = []

    print("=" * 50)
    print("Data -> Anomaly -> Producer -> Topic -> Consumer -> AIOps Processing")
    print(f"[Data] Loading telemetry from: {file_path}")
    print(f"[Data] Records loaded: {len(data)}")

    for record in data:
        print(f"\n[Data] Processing record: {record['service']} @ {record['timestamp']}")
        event = detector.detect(record)

        if event:
            print(f"[Anomaly] Detected: {event['reasons']}")
            producer.publish(event)
            detected_events.append(event)
            print(f"[Producer] Published to topic: {topic.name}")
        else:
            print("[Anomaly] No anomaly found")

    print(f"\n[Topic] Messages in queue: {len(topic.get_messages())}")
    consumed_events = consumer.consume()
    print(f"[Consumer] Consumed events: {len(consumed_events)}")
    print("[AIOps Processing] Final downstream processing complete")

    return {
        "records_processed": len(data),
        "anomalies_detected": detected_events,
        "events_consumed": consumed_events
    }


if __name__ == "__main__":
    result = run_pipeline("data/service_data.json")

    print("=" * 50)
    print("AIOps Pipeline Result")
    print("=" * 50)

    print(f"Records processed: {result['records_processed']}")
    print(f"Anomalies detected: {len(result['anomalies_detected'])}")
    print(f"Events consumed: {len(result['events_consumed'])}")

    print("\nDetected Events:")

    for event in result["events_consumed"]:
        print(f"\nService: {event['service']}")
        print(f"Timestamp: {event['timestamp']}")
        print(f"Type: {event['type']}")
        print(f"Reasons: {', '.join(event['reasons'])}")