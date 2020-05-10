# django-polls-app
Working on a Polls app with the SIIT team

# Local setup
## System requirements
Please have [Docker](https://www.docker.com/products/docker-desktop)  and [docker-compose](https://docs.docker.com/compose/install/) (bundled with Docker for Mac/Windows) installed

## Initial setup
This is a first-time setup step
We first pull remote images, and build the local ones. After that 
On the first run of the application we need to run the migrations to populate the database structure.

```
docker-compose pull
docker-compose build
docker-compose run console django-admin migrate
```

## Startup the project

```
docker-compose up
```