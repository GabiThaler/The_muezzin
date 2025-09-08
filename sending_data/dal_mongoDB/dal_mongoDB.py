from bson import ObjectId
from pymongo import MongoClient ,errors
import os
import gridfs



class DAL_MONGO:

    def __init__(self):
        self.client = None
        self.host = os.getenv("DB_HOST", "localhost")
        self.db_name = os.getenv("DB_NAME", "the_muzzin")
        self.db_coll = os.getenv("DB_COLL", "audio")
        self.db_port = os.getenv("BD_PORT", "27017")




    def connect(self):
        try:
            self.client = MongoClient(f"mongodb://{self.host}:{self.db_port}")
            self.client.admin.command("ping")
            print(f"Connected to {self.host}!")
        except errors.ServerSelectionTimeoutError as err:
            print(f"Server selection timeout: {err}")
            raise
        except errors.ConnectionFailure as err:
            print(f"Connection failed: {err}")
            raise
        except errors.ConfigurationError as err:
            print(f"Configuration error: {err}")
            raise
        except Exception as err:
            print(f"Unexpected error: {err}")
            raise


    def close_conn(self):
        self.client.close()

    def insert_audio(self):
        try:
            fs = gridfs.GridFS(self.client, self.db_coll)
            with open(r"'C:\\data_project_muezzin\\download (5).wav'", 'rb') as f:
                file_id = fs.put(f, filename='my_file.txt')
        except Exception as err:
            print(f"Unexpected error: {err}")


d=DAL_MONGO()
d.connect()
d.insert_audio()