from transcriber.producer import pub_transcriber
from pathlib import WindowsPath
from transcriber.actual_converter import actual_converter

class Manager_transcriber:

    def __init__(self):
        self.trenscrib= actual_converter.Transcriber()
        self.pub= pub_transcriber.Producer()

    def send_to_add_transcriber(self,messege):
        path = messege["path"]
        Transcribed = self.trenscrib.Transcriber_activator(path)
        messege["Transcribed"] = Transcribed
        print(messege)
        a=self._prepare_for_json_serialization(messege)
        self.pub.send_to_kafka("gabis_metadata", a)

    def send_to_kafka(self,messege):
        self.pub.send_to_kafka("gabis_metadata",messege)

    def _prepare_for_json_serialization(self, obj):
            if isinstance(obj, dict):
                return {k: self._prepare_for_json_serialization(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [self._prepare_for_json_serialization(elem) for elem in obj]
            elif isinstance(obj, WindowsPath):
                return str(obj)  # Convert WindowsPath to string
            else:
                return obj