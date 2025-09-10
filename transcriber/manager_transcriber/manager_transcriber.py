from transcriber.producer import pub_transcriber
from pathlib import WindowsPath
from transcriber.actual_converter import actual_converter
from transcriber.subsscriber_transcriber import sub_transcriber



class Manager_transcriber:

    def __init__(self):
        self.trenscrib= actual_converter.Transcriber()
        self.pub= pub_transcriber.Producer()


    def get_sub(self):
        sub = sub_transcriber.lesener()
        sub.listen_kafka()



    #פונקציה שמנהלתמוסיפה את התמלול לjson ושולחת לקפקה
    def handler(self, message):
        path = message["path"]
        #שולח את הנתיב לפונקציה שמתממלת והתמלול חוזר במשתנה
        Transcribed = self.trenscrib.Transcriber_activator(path)
        #מוסיפים את התמלול לjson
        message["Transcribed"] = Transcribed
        self.send_to_kafka(message)



    def send_to_kafka(self,messege):
        self.pub.send_to_kafka("Storaging_station",messege)


