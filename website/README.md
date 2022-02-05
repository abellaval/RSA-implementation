# Private Voting Website

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
> :warning: this step is not necessary if you are using Pycharm Pro, you can setup these inside the project launch config. Specify the path to the app.py file in Target, Application is **app**, FLASK_ENV is **development** and thick the FLASK_DEBUG option.
- Run the server
```shell
  python -m flask run
```
