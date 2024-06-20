
# core tasks

the required apis are given in their respective api python files. to run, one should ensure to have a working docker installation. in case of troubleshooting, maybe some of the notes in notes.txt could help. 
to run the application, one can apply in the terminal in the base directory  

    docker-compose build
    docker-compose up -d

-d leaves the container running in the background, ommit if desired otherwise. 
to log into the container, you can use 

    docker ps
to get the id of the container and then run: 

    docker exec -it <mycontainer> bash

when the container is running, you interact with the three apis acording to these example commands: 

## arvix:
    curl -X POST http://0.0.0.0:8080/arxiv/8 -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"author":"sater"}'


## queries:
    curl -X POST http://0.0.0.0:8080/queries/  -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"query_timestamp_start":"2024-06-17 14:52:00", "query_timestamp_end":"2024-06-17 18:54:00"}'


    curl -X GET http://0.0.0.0:8080/queries/ -H 'accept: application/json' -H 'Content-Type: application/json' -d ' {"query_timestamp_start":"2024-06-17 14:52:00","query_timestamp_end":"2024-06-17 18:54:00"}'

The json file is found in the main directory. 

## resuls with or without page statement: 
    curl -X GET http://0.0.0.0:8080/results/ 
    curl -X GET http://0.0.0.0:8080/results/'?page=2&items_per_page=10'


# About the remarks ot keep in mind:   

### 1. Operations & 2. Orchestration
Are done according to Dockerfile and docker-compose.yml

### 3. Reproducibilty
Request to arxiv should give the same results, as long as their database is the same (e.g. new paper by other -> additional entry in request to arxiv). Similar, as long as the postgres db is the same, the results and queries APIs are reproducable. Reproducability is limited by the query timestamp.   

### 4. Throughput performance bottlenecks
Is covered by using async in the implementation. 

### 5. Failure Redundancy
In the Docker implementation, one can implement the usage of redundant containers. 

### 6. Testing. Unit testing.
The app solution is structured and split up to allow for possible implementation of unit testing. 

### 7. Logging in code
A log file is found in the main container directory and Http exceptions are risen upon errors. 



### Messy process notes

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip --version
    python3 -m pip install -r requirements.txt


- Use Python as the programming language
- Use FastAPI to build the API
- Use SQLAlchemy to interact with a PostgreSQL database
- Use docker-compose to run FastAPI and the PostgreSQL database



References: 
	https://info.arxiv.org/help/api/user-manual.html#query_details
	https://fastapi.tiangolo.com/advanced/testing-database/
	https://medium.com/@agusmahari/docker-how-to-install-postgresql-using-docker-compose-d646c793f216
	https://github.com/KenMwaura1/Fast-Api-example/tree/main
	
run 
conda 
fastapi dev main.py


    docker install
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo docker run hello-world


docker compose install already included above...
sudo apt install docker-compose 

wants sudo...
sudo groupadd docker
sudo usermod -aG docker $USER

might need reboot :|


sudo chown root:docker /var/run/docker.sock

sudo ln -s /usr/bin/docker-compose /usr/local/bin/docker-compose

orm - object relational mapper
https://github.com/grillazz/fastapi-sqlalchemy-asyncpg/blob/main/app/main.py
https://github.com/DarkbordermanTemplate/fastapi-sqlalchemy/blob/master/api/config.py



Open:
- information in terminal -> got better with http
- arvix not avail -> fixed with http
- empty result with arvix -> got better with http 
- empty request with arvix -> fixed
- logs -> somewhat
- unit tests -> structure allows for that
- doku -> more detail in readme is enough?

