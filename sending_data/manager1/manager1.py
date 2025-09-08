from sending_data.dal_elasticsearch import dal_elasticsearch
from sending_data.subsscriber import subsscriber
from sending_data.dal_mongoDB import dal_mongoDB

class Manager:
    def __init__(self):
        self.dal_elastic = dal_elasticsearch.DAL_Elasticsearch()
        self.dal_mongo = dal_mongoDB.DAL_MONGO()

    #פה אנחנו מדליקים את האזנה של הקפקה
    def get_sub(self):
        self.sub = subsscriber.lesener()
        self.sub.listen_kafka()



    #נותנים מוצאים מזהה יחודי לכל דבר שמגיע
    def find_uniq_id(self,size:str,Creation_time:str,Last_modification_time:str,Lastaccess_time:str):
        uniq_id=""
        uniq_id+=str(size)
        uniq_id+=str(Creation_time)
        uniq_id+=str(Last_modification_time)
        uniq_id+=str(Lastaccess_time)
        return uniq_id

    #מכניסים את המאטא דאטא לelasticsearch עH הDAL הרלוונטי
    def insert_to_elasticsearch(self,data):
        self.dal_elastic.insert_to_elasticsearch(data)

    #מכניסים את הקובץ אודיו עצמו לתוך המונגו ע"י הDAL הרלוונטי
    def insert_file_to_mongo(self,path):
        self.dal_mongo.store_audio_gridfs(path)


