from kafka import KafkaProducer
import json
from loger_manager import Logger


class Producer:
    def __init__(self):
        self.logger = Logger.get_logger()
        # מגדירים producer פעם אחת
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer = lambda v: json.dumps(v).encode('utf-8'))

    def send_to_kafka(self, topic, message):
        try:
            self.producer.send(topic,message)
            self.producer.flush()
        except Exception as e:
            self.logger.error(f"the kafka was not send {e}")