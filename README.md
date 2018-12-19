# nginx-flask-mongodb-dockers
An starter project for running a web server backend using flask, nginx and mongodb with docker technology.

## Geting started
Move to the project and simply run `docker-compose up --build` to start the dockers.

To run all the dockers in background, use `docker-compose up -d`.

## Test
After runing the project, use `curl 0.0.0.0` to access the static resources in nginx, and `curl 0.0.0.0/api` to route to flask that handles mongodb data manipulation.
