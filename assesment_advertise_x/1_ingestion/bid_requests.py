import avro.schema
import avro.io
from kafka import KafkaProducer
from io import BytesIO

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_bid_requests(file_path):
    schema = avro.schema.Parse(open("bid_request_schema.avsc", "r").read())
    with open(file_path, "rb") as file:
        bytes_reader = BytesIO(file.read())
        decoder = avro.io.BinaryDecoder(bytes_reader)
        reader = avro.io.DatumReader(schema)
        while not bytes_reader.tell() == len(bytes_reader.getvalue()):
            bid_request = reader.read(decoder)
            producer.send('bid_requests_topic', bid_request)

# Example usage
send_bid_requests('bid_requests.avro')
