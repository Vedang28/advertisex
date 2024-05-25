import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_ad_impressions(data):
    producer.send('ad_impressions_topic', data)

# Example usage
ad_impression = {
    "ad_creative_id": "abc123",
    "user_id": "user456",
    "timestamp": "2024-05-25T12:34:56",
    "website": "example.com"
}
send_ad_impressions(ad_impression)
