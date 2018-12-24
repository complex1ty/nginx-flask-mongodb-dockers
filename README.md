# nginx-flask-mongodb-dockers
An starter project for running a web server backend using flask, nginx and mongodb with docker technology.

## Geting started
Move to the project and simply run `docker-compose up --build` to start the dockers.

To run all the dockers in background, use `docker-compose up -d`.

To change the initial username and password for building mongodb on the first time(when there is no files in `mongodb/db`), edit `.env` to pass in environment variables.

To restore from existing mongodb, put backup file in `mongo/db`, after dockers run, run `docker exec -it mongodb sh` to enter interactive shell inside of the mongodb docker container and use mongo shell command to retore your backup file under `/data/db`.

## Test
After runing the project, use `curl 0.0.0.0` to access the static resources in nginx, and `curl 0.0.0.0/api` to route to flask that handles mongodb data manipulation.
