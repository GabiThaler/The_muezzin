
from sending_data.subsscriber import subsscriber

class Manager:
    def __init__(self):
        pass


    def get_sub(self):
        self.sub = subsscriber.lesener()
        self.sub.listen_kafka()


    def find_uniq_id(self):
        pass


    def insert_to_elasticsearch(self):
        pass


    def insert_file_to_mongo(self):
        pass


