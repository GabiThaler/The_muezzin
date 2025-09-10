from elasticsearch import Elasticsearch
from logger.loger_manager import Logger

class DAL_Elasticsearch:
    def __init__(self):
        self.logger = Logger.get_logger()
        try:
            #מגדירים את האינדקס של האלסטיק
            self.es = Elasticsearch('http://localhost:9200')
            self.client_info = self.es.info()
            self.logger.info(f"Connected to Elasticsearch! Info: {self.client_info}")
            self.es.indices.delete(index='metadata_test', ignore_unavailable=True)
            self.es.indices.create(index='metadata_test')
        except Exception as e:
            self.logger.error(f"Failed to connect to Elasticsearch! Error: {e}")

    #מכניס את המאטאדאטא לאינדקס
    def insert_to_elasticsearch(self, data):
        try:
            response = self.es.index(index='metadata_test', body=data)
            self.logger.debug(f"Response from Elasticsearch: {response}")
        except Exception as e:
            self.logger.error(f"Failed to connect to Elasticsearch! Error: {e}")



