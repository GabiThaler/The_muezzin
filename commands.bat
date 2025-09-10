#פקודה להרצת הסייפריה שיקבל את כל הmetadata

pip install pathlib

#פקודה שיריץ קונטיינר של קאפקה

docker run -d -p 9092:9092 --name broker apache/kafka:latest

#הפקודה להוריד את התיקייה של הקפקאע

pip install kafka

# פקודה להרצאת הדוקר של ה elasticsearch

docker run -p 127.0.0.1:9200:9200 -d --name elasticsearch -e "discovery.type=single-node" -e "xpack.security.enabled=false" -e "xpack.license.self_generated.type=trial" -v "elasticsearch-data:/usr/share/elasticsearch/data"  docker.elastic.co/elasticsearch/elasticsearch:8.15.0

# פקודה להתקנת הסיפרייה של elasticsearch וממודאים שיש לנו את הגירסא הנכינה שזה 8

 pip install "elasticsearch>=8,<9"

#פקודות להאריץ את הדוקרים של המונגו דיבי
docker pull mongodb/mongodb-community-server:latest
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest


#פקודה להרצהת הספרייה של התמלול אודיו

pip install faster_whisper