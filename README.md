# recipe-app-api
A recipe app API written django.

# How to

## Build docker image:

```
> docker build .
```

## Run docker-compose build

```
> docker-compose build
```

# Development notes:

## Start new project:

```
> docker-compose run app sh -c "django-admin.py startproject app ."
```

## Add dependency:

1. Install dependency with pipenv
```
> pipenv install <package_name>
OR:
> pipenv install "<package_name>>=<lowest_version,<<hightes_version"
example:  pipenv install "flake8>=3.6.0,<3.7.0"
```

2. Add dependency to requirements.txt.
```
> pipenv run pip freeze > requirements.txt
```

3. (Re-)Build docker container:

```
> docker build .
```

## Run Tests:

```
> docker-compose run app sh -c "python manage.py test && flake8"
```
