from pathlib import Path
from mata_data_processor import mata_data_processor

class Manager:
    def __init__(self):
        self.dir_path=r"C:\data_project_muezzin"
        self.processor = mata_data_processor.Mata_data_processor()

    #פןנקציה שעוברת על כל התייקיה ושולחת למעבד כל קובץ
    def get_files(self):
        for file in Path(self.dir_path).iterdir():
            if file.is_file():
                print(f"{file.name} sent to proses")
                self.processor.Process(file)


a=Manager()
a.get_files()