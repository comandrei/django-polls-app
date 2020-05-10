# django-polls-app
Working on a Polls app with the SIIT team

# Local setup
## System requirements
Please have [Docker](https://www.docker.com/products/docker-desktop)  and [docker-compose](https://docs.docker.com/compose/install/) (bundled with Docker for Mac/Windows) installed

## Initial setup
This is a first-time setup step.

On the first run of the application we need to run the migrations to populate the database structure.

```
docker-compose run console django-admin migrate
```

As the other containers are missing they will be built/downloaded prior to running the command.

So this basically also calls docker-compose pull and docker-compose build prior to building.


## Startup the project

```
docker-compose up
```

Go to [http://localhost:8000](http://localhost:8000) to view the newly created Django application