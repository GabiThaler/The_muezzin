from sending_data.manager1 import manager1
from kafka import KafkaConsumer
import json
from logger.loger_manager import Logger


#מחלקה שמקשיבה כל הזמן בקפקא לטופיק של המאטא דאטא
class lesener():
    def __init__(self):
        self.logger = Logger.get_logger()
        self.manager = manager1.Manager()



    def listen_kafka(self):
        self.logger.info('Listening Kafka in topic "Gabis_metadata"')
        consumer = KafkaConsumer(
            "Gabis_metadata",  # הטופיק של של המאטאדאטא
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='latest',  # שיקרא מהתחלה אם לא קראנו עדיין
            # group_id='gabis_metadata',
            enable_auto_commit=True,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))

        )


        try:
            for message in consumer:

                if(message.value):
                    self.manager.maneg_manager(message.value)
                    self.logger.debug(f"[{message.topic}] {message.value} sent to maneger")


                else:
                    self.logger.info(f"[{message.topic}] {message.value} dict is empty")


        except KeyboardInterrupt:
            self.logger.info('Stopping Kafka')

