# DevTestOps
* Python + FastAPI + PostgreSQL
* .NET 8 + PostgreSQL
* Java and SpringBoot
* API testing with Postman and newman
* UI Testing
    * [Selenium Grid](https://github.com/SeleniumHQ/docker-selenium)
    * [Robotframework](https://robotframework.org/)

## 1. REST API with Python and [FastAPI](https://fastapi.tiangolo.com/)

### Start PostgreSQL database
```
$docker compose up -d postgres
$docker compose ps
```

### Build and Run
```
$docker compose build python-api
$docker compose up -d python-api
$docker compose ps
```

URL of Swagger or OpenAPI documentation
* http://localhost:8000/docs

### API testing with Postman and [newman](https://www.npmjs.com/package/newman)
```
$docker compose up python-api-test --abort-on-container-exit
```
Report is generated in folder `postman/reports/`

## 2. REST API with .NET 8
* https://learn.microsoft.com/en-us/dotnet/core/docker/introduction

### Start PostgreSQL database
```
$docker compose up -d postgres
$docker compose ps
```

### Build and Run
```
$docker compose build dotnet-api
$docker compose up -d dotnet-api
$docker compose ps
```

URL of Swagger or OpenAPI documentation
* http://localhost:9000/swagger/index.html

### API testing with Postman and [newman](https://www.npmjs.com/package/newman)
```
$docker compose up dotnet-api-test --abort-on-container-exit
```
Report is generated in folder `postman/reports/`

## 3. REST API with Java and SpringBoot

### Start PostgreSQL database
```
$docker compose up -d postgres
$docker compose ps
```

### Build and Run
```
$docker compose build java-api
$docker compose up -d java-api
$docker compose ps
```

URL of Swagger or OpenAPI documentation
* http://localhost:7070/swagger-ui/index.html

## 4. Web UI Testing with Selenium and Robot framework

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