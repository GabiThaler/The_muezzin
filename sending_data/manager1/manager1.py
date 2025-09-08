from sending_data.dal_elasticsearch import dal_elasticsearch
from sending_data.subsscriber import subsscriber
from sending_data.dal_mongoDB import dal_mongoDB
#הספריות שמקודדת את המזהה יחודי
import uuid
import hashlib

class Manager:
    def __init__(self):
        self.dal_elastic = dal_elasticsearch.DAL_Elasticsearch()
        self.dal_mongo = dal_mongoDB.DAL_MONGO()

    #פה אנחנו מדליקים את האזנה של הקפקה
    def get_sub(self):
        self.sub = subsscriber.lesener()
        self.sub.listen_kafka()



    #מוצאים מזהה יחודי לכל דבר שמגיע
    def find_uniq_id(self,my_string):
        # Generate a UUID based on the MD5 hash of the string
        unique_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, my_string)
        print(f"The UUID generated from '{my_string}' is: {unique_uuid}")

    #מכניסים את המאטא דאטא לelasticsearch עH הDAL הרלוונטי
    def insert_to_elasticsearch(self,data):
        self.dal_elastic.insert_to_elasticsearch(data)

    #מכניסים את הקובץ אודיו עצמו לתוך המונגו ע"י הDAL הרלוונטי
    def insert_file_to_mongo(self,path):
        self.dal_mongo.store_audio_gridfs(path)
    #פונקציה שמנהלת את כל התהליך
    def maneg_manager(self,messege):
        #יוצרים id יחודי
        id=self.find_uniq_id(messege["path"]+messege["name"])
        #מכניסים את הid לתוך המילון
        messege["unique_id"]=id
        #מכניסים את המילון לתוך האלסטיק
        self.insert_to_elasticsearch(messege)
        #מכניסים את הקובץ עצמו לתוך המונגו
        self.insert_file_to_mongo(messege["path"])



