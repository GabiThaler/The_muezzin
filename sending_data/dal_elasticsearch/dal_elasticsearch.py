from elasticsearch import Elasticsearch


class DAL_Elasticsearch:
    def __init__(self):
        try:
            self.es = Elasticsearch('http://localhost:9200')
            self.client_info = self.es.info()
            print('Connected to Elasticsearch!')
            print(self.client_info.body)
            self.es.indices.delete(index='metadata_test', ignore_unavailable=True)
            self.es.indices.create(index='metadata_test')
        except Exception as e:
            print(f"the was no conniction the elasticsearch {e}")


    def insert_to_elasticsearch(self, data):
        try:
            response = self.es.index(index='metadata_test', body=data)
            print(response["result"])
        except Exception as e:
            print(f"we didnt insert the data {e}")


