# Voting Website

## Setup local dev env

- Change currently working dir to Project/website
- Install virtualenv if it is not already on the machine.
```shell
  pip install virtualenv
```
- Create a virtual environment, it should create a venv inside Project
```shell
  virtualenv ../venv 
```
- Activate the virtualenv
```shell
  source ../venv/bin/activate
```
- Install the dependencies from the requirement.txt file
```shell
  pip install -r requirements.txt 
```
> :warning: if pip doesn't work, try pip3 instead
- Export Flask env vars for developement (needs to be done for each new shell session)
```shell
  source flask_env.sh
```
> :warning: this step is not necessary if you are using Pycharm, you can setup these inside the project launch config. Setup your Pycharm to launch run.py and add the env variables from flask_env.sh to the env field, next to PYTHONBUFFERED=1, seperated by spaces.
- Run the dev server
```shell
  python run.py
```

## Accessing different routes
- The Client app is on the default route '/'
- The Admin app is on the route '/admin'
- The Ballot app is on the route '/ballot'
- The Counter app is on the route '/counter'