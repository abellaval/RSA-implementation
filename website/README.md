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
  source flask_env_debug.sh
```
> :warning: this step is not necessary if you are using Pycharm, you can setup these inside the project launch config.
- Run the dev server
```shell
  python3 app.py
```