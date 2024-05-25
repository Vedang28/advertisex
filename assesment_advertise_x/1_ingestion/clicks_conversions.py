import csv
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_clicks_conversions(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            producer.send('clicks_conversions_topic', row)

# Example usage
send_clicks_conversions('clicks_conversions.csv')
