from pathlib import Path
from processing_metadata.mata_data_processor import mata_data_processor
from processing_metadata.producer import producer


class Manager:
    def __init__(self):
        self.dir_path=r"C:\data_project_muezzin"
        self.processor = mata_data_processor.Mata_data_processor()
        self.pub = producer.Producer()


    #פןנקציה שעוברת על כל התייקיה ושולחת למעבד כל קובץ
    def get_files(self):
        #לולאה שעוברת על כל הקבצים שבתייקיה
        for file in Path(self.dir_path).iterdir():
            #בודק עם הקובץ קיים ותקין
            if file.is_file():
                #שולח את הקובץ לקבל ממנו את כל המאטאדאטא
                dict_data = self.processor.Building_dictionary_with_the_metadata(file)
                # שולחים את המילון להכנה להמרה לjson
                dict_data = self.processor._prepare_for_json_serialization(dict_data)

                #שולח את המילון שקיבלתי להמרה לjson שאני ישלח לקפקא
                json_data = self.processor.dict_to_json(dict_data)
                print(f"{file.name} sent to proses")
                #שולחים את הjson לkafka
                self.pub.send_to_kafka("metadata", dict_data)







a=Manager()
a.get_files()