from BDS_calculator import manager__BDS_calculator
from kafka import KafkaConsumer
from BDS_calculator.producer_BDS_calculator import pub_BDS_calculator
import json
from logger.loger_manager import Logger


#מחלקה שמקשיבה כל הזמן בקפקא לטופיק של המאטא דאטא
class lesener():
    def __init__(self):
        self.logger = Logger.get_logger()
        self.manager = manager__BDS_calculator. Manager_BDS_calculator()
        self.manager.clean_text()
        self.pub = pub_BDS_calculator.Producer()



    def listen_kafka(self):
        self.logger.info('Listening Kafka in topic "BDS_calculator"')
        consumer = KafkaConsumer(
            "BDS_calculator",  # הטופיק של של ישוב הסיכון
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='latest',
            enable_auto_commit=True,#שיקרא מהתחלה אם לא קראנו עדיין
            # group_id='gabis_metadata_good',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))

        )
        self.logger.info('Listening Kafka in topic "BDS_calculator"')
        try:
            for message in consumer:
                if(message.value):

                    Risk = self.manager.managemer(message.value["Transcribed"])
                    message.value["Risk"] = Risk
                    self.pub.send_to_kafka("Storaging_station",message.value)
                    self.logger.debug(f"sent message to kafka, 'Storaging_station' from 'BDS_calculator': {message.value} ")

                else:
                    self.logger.error(f"[{message.topic}] {message.value} dict is empty")


        except KeyboardInterrupt:
            self.logger.error('Stopping Kafka')

