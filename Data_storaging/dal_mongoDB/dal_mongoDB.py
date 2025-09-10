from pymongo import MongoClient
from gridfs import GridFS
from logger.loger_manager import Logger
class DAL_MONGO:
    def __init__(self):
        self.logger = Logger.get_logger()

    #הפונקציה שמכניסה את הרובץ עצמו למונגו
    def store_audio_gridfs(self,file_path, db_name="the_muzzin", collection_name="audio"):
        try:
            client = MongoClient("mongodb://localhost:27017/")
            db = client[db_name]
            fs = GridFS(db, collection=collection_name)
            #פותחים את הקובץ ושולחים מחולק בביטים למונגו
            with open(file_path, "rb") as f:
                file_id = fs.put(f, filename=file_path.split("/")[-1])  # Store with original filename
                self.logger.debug(f"Audio file '{file_path}' stored in GridFS with ID: {file_id}")
            client.close()
        except Exception as e:
            self.logger.error(f"The file did not enter Mong because {e}")




