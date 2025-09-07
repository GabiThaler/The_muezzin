from pathlib import Path
from mata_data_processor import mata_data_processor

class Manager:
    def __init__(self):
        self.dir_path=r"C:\data_project_muezzin"
        self.processor = mata_data_processor.Mata_data_processor()

    #פןנקציה שעוברת על כל התייקיה ושולחת למעבד כל קובץ
    def get_files(self):
        #לולאה שעוברת על כל הקבצים שבתייקיה
        for file in Path(self.dir_path).iterdir():
            #בודק עם הקובץ קיים ותקין
            if file.is_file():
                #שולח את הקובץ לקבל ממנו את כל המאטאדאטא
                dict_data = self.processor.Building_dictionary_with_the_metadata(file)
                #שולח את המילון שקיבלתי להמרה לjson שאני ישלח לקפקא
                json_data = self.processor.dict_to_json(dict_data)
                print(f"{file.name} sent to proses")




a=Manager()
a.get_files()