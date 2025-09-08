from sending_data.manager1 import manager1
from kafka import KafkaConsumer
import json


#מחלקה שמקשיבה כל הזמן בקפקא לטופיק של המאטא דאטא
class lesener():
    def __init__(self):
        self.manager = manager1.Manager()
        # pass


    def listen_kafka(self):
        consumer = KafkaConsumer(
            "metadata",  # הטופיק של של המאטאדאטא
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',  # שיקרא מהתחלה אם לא קראנו עדיין
            enable_auto_commit=True,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )

        print("listening")

        try:
            for message in consumer:
                print(f"[{message.topic}] {message.value}")
                if message.value:
                    # self.manager.find_uniq_id(message.value)
                    pass

        except KeyboardInterrupt:
            print("stopt thre lesenir ")

