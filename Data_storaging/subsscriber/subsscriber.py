from Data_storaging.manager_Data_storaging import manager_Data_storaging
from kafka import KafkaConsumer
import json
from logger.loger_manager import Logger


#מחלקה שמקשיבה כל הזמן בקפקא לטופיק של המאטא דאטא
class lesener():
    def __init__(self):
        self.logger = Logger.get_logger()
        self.manager = manager_Data_storaging.Manager()
        self.manager.connect_to_elastic()



    def listen_kafka(self):
        self.logger.info('Listening Kafka in topic "Storaging_station"')
        consumer = KafkaConsumer(
            "Storaging_station",  # הטופיק של של המאטאדאטא
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='latest',
            enable_auto_commit=True,#שיקרא מהתחלה אם לא קראנו עדיין
            # group_id='gabis_metadata_good',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))

        )

        try:
            for message in consumer:
                if(message.value):
                    self.manager.maneg_manager(message.value)
                    self.logger.debug(f"[{message.topic}] {message.value} sent to maneger")


                else:
                    self.logger.error(f"[{message.topic}] {message.value} dict is empty")


        except KeyboardInterrupt:
            self.logger.error('Stopping Kafka')

