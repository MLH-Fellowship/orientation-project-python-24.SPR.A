# Orientation Project - Python

Refer to the Fellowship LMS for information!

## Setup
### Install Dependencies
Use `Pipenv` to manage virtual environment and install the dependencies. More details can be found in [Pipenv Documentation](https://pipenv.pypa.io/en/latest/).
```
python3 -m pip install pipenv
python3 -m pipenv install --dev
```
### Activate Virtual Environment
```
python3 -m pipenv shell
```

## Run
```
flask run
```

## Run tests
```
pytest test_pytest.py
```

## Run Linter
```
pylint *.py
```

## Setup Docker Based Development Environment
You can use  `docke-compose` to setup the development environment. Use following steps to setup the environment.

### Setup
1. Create `docker-compose.override.yml` file copying the given `docker-compose.override.yml.example` file. 
2. Change the port mapping in `docker-compose.override.yml` file if you want to use different port.

### Build
If you are running the environment for the first time, or you have made changes to the `Dockerfile` run following command.

```bash
docker-compose build
```
### Run
```bash
docker-compose up
```

### Stop
```bash
docker-compose down
```

### Install Dependencies
```bash
docker-compose exec app  pipenv install <package-name>
```
More information can be found in [Docker Compose Documentation](https://docs.docker.com/compose/).