from elasticsearch import Elasticsearch


class DAL_Elasticsearch:
    def __init__(self):
        try:
            #מגדירים את האינדקס של האלסטיק
            self.es = Elasticsearch('http://localhost:9200')
            self.client_info = self.es.info()
            print('Connected to Elasticsearch!')
            print(self.client_info.body)
            self.es.indices.delete(index='metadata_test', ignore_unavailable=True)
            self.es.indices.create(index='metadata_test')
        except Exception as e:
            print(f"the was no conniction the elasticsearch {e}")

    #מכניס את המאטאדאטא לאינדקס
    def insert_to_elasticsearch(self, data):
        try:
            response = self.es.index(index='metadata_test', body=data)
            print(f"{response["result"]} wes inserted to elasticsearch")
        except Exception as e:
           raise f"we didnt insert the data {e}"



