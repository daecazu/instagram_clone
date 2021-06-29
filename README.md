# Django Base service

This is a base repository for Django API, please replace the base folder and named it accordly.
the first step to use this repository is to replace "appname" in the compose image files an add the app to the Django settings/base.py

## Local Server commands (DEV)

**Adding Docker-compose File**

`export COMPOSE_FILe=compose-dev.yml` 

**Building project**

`docker-compose build`

**Running Tests**

`docker-compose run --rm django sh -c 'python manage.py test && flake8'`

**Create SuperUser**

`docker-compose run --rm django sh -c 'python manage.py createsuperuser'`

**Run Local Server**

`docker-compose up`

## Remote Server commands (Production)

**Adding Docker-compose File**
`export COMPOSE_FILe = compose-prod.yml` 

**Building project**

`docker-compose build`

**Create SuperUser**

`docker-compose run --rm django sh -c 'python manage.py createsuperuser'`

**Run Local Server**

`docker-compose up -d`

### Create a secret key

in python 3.6 we can use these 3 lines

```python
import secrets
import string 
print("".join(secrets.choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)))
```
is best practice to create a secret key for each project in the .envs/production/django file
