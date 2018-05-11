Requirements
============

* [Docker](https://docs.docker.com/install/)

### Start Containers ###
Run command from root directory
```
    docker-compose up
```

Then you should be able to access the application at http://localhost:9000/harvest

disclaimer: this app is currently configured as a REST api and the url will return a JSON response


### Running commands on the server ###
```
    docker exec -it <server name> <cmd>
    # i.e. docker-compose run server manage.py migrate
```
