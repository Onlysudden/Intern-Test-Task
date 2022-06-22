docker run --name elastic --net elastic -d -p 9200:9200 -p 9300:9300 --rm -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.2.3

docker run --name app --net elastic -d -p 5000:5000 --rm test:1