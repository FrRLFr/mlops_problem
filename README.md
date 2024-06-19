docker-compose build

docker-compose up -d

docker ps
docker exec -it <mycontainer> bash



python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip --version
python3 -m pip install -r requirements.txt



curl -X POST http://0.0.0.0:8080/queries/  -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"query_timestamp_start":"2024-06-17 14:52:00", "query_timestamp_end":"2024-06-17 18:54:00"}'


curl -X GET http://0.0.0.0:8080/queries/ -H 'accept: application/json' -H 'Content-Type: application/json' -d ' {"query_timestamp_start":"2024-06-17 14:52:00","query_timestamp_end":"2024-06-17 18:54:00"}'

curl -X POST http://0.0.0.0:8080/arxiv/8 -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"author":"sater"}'

curl -X GET http://0.0.0.0:8080/results/ 
curl -X GET http://0.0.0.0:8080/results/'?page=2&items_per_page=10'


Open:
- information in terminal -> got better with http
- arvix not avail -> fixed with http
- empty result with arvix -> got better with http 
- empty request with arvix -> fixed
- logs -> somewhat
- unit tests
- doku -> more detail in readme is enough?


- throughput/failure via load balancers?, but for docker compose would be process manager 

- clean up? try review with flo first and push to git


favorite references: 
https://github.com/KenMwaura1/Fast-Api-example/tree/main