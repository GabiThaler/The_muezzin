from pymongo import MongoClient
from gridfs import GridFS

class DAL_MONGO:

    def store_audio_gridfs(self,file_path, db_name="the_muzzin", collection_name="audio"):
        try:
            client = MongoClient("mongodb://localhost:27017/")
            db = client[db_name]
            fs = GridFS(db, collection=collection_name)

            with open(file_path, "rb") as f:
                file_id = fs.put(f, filename=file_path.split("/")[-1])  # Store with original filename

            print(f"Audio file '{file_path}' stored in GridFS with ID: {file_id}")
            client.close()
        except Exception as e:
            print(f"The file did not enter Mong because {e}")




