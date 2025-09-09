from transcriber.manager import manager_transcriber
from kafka import KafkaConsumer
import json
from logger.loger_manager import Logger


#מחלקה שמקשיבה כל הזמן בקפקא לטופיק של המאטא דאטא
class lesener():
    def __init__(self):
        self.logger = Logger.get_logger()
        self.manager = manager_transcriber.Manager_transcriber()



    def listen_kafka(self):

        consumer = KafkaConsumer(
            "Transcription_station",  # הטופיק של של המאטאדאטא
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='latest',
            enable_auto_commit=True,#שיקרא מהתחלה אם לא קראנו עדיין
            group_id='muezzin_metadata',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))

        )
        self.logger.info('Listening Kafka in topic "Transcription station"')
        try:
            for message in consumer:

                if (message.value):
                    self.logger.debug(f"{message.value} is sent to trenscrib")
                    self.manager.send_to_add_transcriber(message.value)
                    print(message.value)


                else:
                    self.logger.error(f"[{message.topic}] {message.value} dict is empty")


        except KeyboardInterrupt:
            self.logger.info('Stopping Kafka')

