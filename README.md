# Steps
 ## If you want to run the game, follow the next steps:
 - Run in the terminal this: 
```sh
python3 06_Game.py
```

## If you want to run the chart graph, go to the chart folder and run de next command:
```sh
python3 main.py
```

## If you want to run the AppFinal34:

```sh
git clone https://github.com/jsalegria16/pip_env_py.git # Or even a fork

cd AppFinal34_GlobalPopulation # Go to the project folder

python3 -m venv env_AppFinal34 # Create the virtual environment

source env_AppFinal34/bin/activate # Activate the environment

pip3 install -r requirements.txt # Install all the modules you need.

python3 final33.py # Run the project
```

## 

## If you want to run the Apweb-server app :

```sh
git clone https://github.com/jsalegria16/pip_env_py.git # Or even a fork

cd web-server # Go to the project folder

python3 -m venv env_webServer # Create the virtual environment

source env_webServer/bin/activate # Activate the environment

pip3 install -r requirements.txt # Install all the modules you need.

python3 main.py # Run the project
```

### Web server with fast api (Store.py file):

```sh
git clone https://github.com/jsalegria16/pip_env_py.git # Or even a fork

cd web-server # Go to the project folder

python3 -m venv env_webServer # Create the virtual environment

source env_webServer/bin/activate # Activate the environment

pip3 install -r requirements.txt # Install all the modules you need.

python3 main.py # Run the project

uvicorn main:app --reload # Run the server in your PC.

http://127.0.0.1:8000 # In browser go there. 

```
## Docker to AppFinal34

install docker:
- [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
-  [https://docs.docker.com/desktop/windows/wsl/](https://docs.docker.com/desktop/windows/wsl/)


```sh

git clone https://github.com/jsalegria16/pip_env_py.git # Or even a fork

cd AppFinal34_GlobalPopulation # Go to AppFinal34 project

# Run docker on your PC 

docker-compose build # Create the container,

docker-compose up -d # Turn on the container (**docker-compose down** if you want stop it)

docker-compose exec app_final bash # Acces to the container with in a bash mode.

# you will be in /Docker_AppFinal. This is the proyect. Run it with **python3 final33.py**

exit # get out from docker container.


```


