from kafka import KafkaProducer
import json


class Producer:
    def __init__(self):
        # מגדירים producer פעם אחת
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer = lambda v: json.dumps(v).encode('utf-8'))

    def send_to_kafka(self, topic, message):
        try:
            self.producer.send(topic,message)
            self.producer.flush()
            print(f"sent to {topic}: {message}")
        except Exception as e:
            print(f"the kafka was not send {e}")