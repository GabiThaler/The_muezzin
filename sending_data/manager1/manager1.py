from sending_data.dal_elasticsearch import dal_elasticsearch
from sending_data.subsscriber import subsscriber

class Manager:
    def __init__(self):
        self.dal_elastic=dal_elasticsearch.DAL_Elasticsearch()


    def get_sub(self):
        self.sub = subsscriber.lesener()
        self.sub.listen_kafka()




    def find_uniq_id(self,size:str,Creation_time:str,Last_modification_time:str,Lastaccess_time:str):
        uniq_id=""
        uniq_id+=str(size)
        uniq_id+=str(Creation_time)
        uniq_id+=str(Last_modification_time)
        uniq_id+=str(Lastaccess_time)
        return uniq_id


    def insert_to_elasticsearch(self,data):
        self.dal_elastic.insert_to_elasticsearch(data)


    def insert_file_to_mongo(self):
        pass


