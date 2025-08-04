# DevTestOps
* [Selenium Grid](https://github.com/SeleniumHQ/docker-selenium)
* [Robotframework](https://robotframework.org/)

## REST API with Python and [FastAPI](https://fastapi.tiangolo.com/)

### Build and Run
```
$docker compose build python-api
$docker compose up -d python-api
$docker compose ps
```

URL of Swagger or OpenAPI documentation
* http://localhost:8000/docs


## Web UI Testing with Selenium and Robot framework

### Run Selenium Grid
```
$docker compose up -d selenium-hub
$docker compose up -d chrome
$docker compose ps
```

Access to selenium hub
* http://localhost:4444/ui/

### Run test
```
$docker compose build robot-runner
$docker compose up robot-runner
```

Report is generated in folder `report/results/`