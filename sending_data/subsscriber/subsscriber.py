from sending_data.manager1 import manager1
from kafka import KafkaConsumer
import json


#מחלקה שמקשיבה כל הזמן בקפקא לטופיק של המאטא דאטא
class lesener():
    def __init__(self):
        self.manager = manager1.Manager()
        self.count =0


    def listen_kafka(self):
        print("listening")
        consumer = KafkaConsumer(
            "Gabis_metadata",  # הטופיק של של המאטאדאטא
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',  # שיקרא מהתחלה אם לא קראנו עדיין
            enable_auto_commit=True,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )


        try:
            for message in consumer:

                if(message.value):
                    self.manager.maneg_manager(message.value)
                    print(f"[{message.topic}] {message.value} sent to maneger")


                else:
                    print("json is empty")


        except KeyboardInterrupt:
            print("stopt thre lesenir ")

