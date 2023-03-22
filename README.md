# Ollivanders flask

Start statment that our teacher dfleta prepared to us: [statement](https://github.com/dfleta/ollivanders_shop). And his [solution](https://github.com/dfleta/ollivanders). All the documentation he gave to us [here](https://github.com/dfleta/flask-rest-ci-boilerplate)

Also there will be my solution of the [refactoring kata](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main/python) of Emily Bache. [My solution](https://github.com/ClearCB/gildedrose-kata/tree/main/python) of the previous kata without using an API REST.

The exercise that will be stored in this repository, will have the same statment but I wll create a "web" in which there will be an API REST additional at the solution.

## Domain

This application is a simulation of a magic store called "Gilded Rose" which have an specific inventory whose items have magicals behaviour. Each of them update their quality in a different way. The initial inventory stock was:

* Normal Items
* Sulfuras
* Aged Brie
* Backstage

And the kata is planned to create an application to keep SOLID principles, so we can add a new item category and keep working well (OCP principle). Since we have to add a new item called "conjured", the exercise consist in creating a logical architecture in which all the items correclty updates the quality.  

To understand the working application is important you to read the following documents: [application requierments](./doc/OriginalRequirements.txt) and [quality items behaviour](./doc/qualityBehaviour.txt)

## Install

This application is able to use in 2 ways. First you must have an mongo atlas cluster and its key to connect to it the key must look something like this:

"mongodb+srv://<database>:<password>@<urconnection>/?retryWrites=true&w=majority"

Then install it following these steps: 1 is posible to install it direcly cloning this repository and 2 [Dockerized](#dockerized): create a docker container with the application itself

* Create directory

```cmd
mkdir .\flask-app
cd flask-app
```

* Create virtual enviroment

```cmd
python -m venv venv
```

* Create enviroment variable called "MONGO_ATLAS_URI"

```cmd
windows_

set MONGO_ATLAS_URI="uri"

linux_

export MONGO_ATLAS_URI="uri"
```

* Clone repository

```cmd
git clone URL
```

* Install requirements

```cmd
pip install -r requirements.txt
```

## Use

Now that you have it in your local machine. Execute the "app.py" file with python and use postman or your cli to test the endpoints API.

Using commandline:

### CLI

```cmd
curl -X GET http://localhost:5000/items/find-one/4
```

![cli-find](./doc/img/cli_find.png)

```cmd
curl -X GET http://localhost:5000/inventory
```

```cmd
curl -X PUT http://localhost:5000/inventory/update
```

```cmd
curl -d "{\"_id\": 15, \"name\": \"sticky stick\", \"sell_in\": 80, \"quality\": 30, \"item_type\":\"Conjured\"}" -H "Content-Type: application/json" -X POST http://localhost:5000/items/create-one
```

![insert](./doc/img/cli_insert.png)

```cmd
curl -X DELETE http://localhost:5000/items/delete-one/15
```

![delete-one](./doc/img/cli_delete.png)

```cmd
curl -d "{\"name\": \"sticky stick\", \"sell_in\": 80, \"quality\": 10}" -H "Content-Type: application/json" -X PUT http://localhost:5000/items/update-one/4
```

To test it with postman

### POSTMAN

First is important to set up the headers with the following pair key-value.

* Headers: Content-type / application/json

GET:

```postman
http://localhost:5000/inventory/
```

![inventory](./doc/img/read-inventory.png)

```postman
http://localhost:5000/items/find-one/<id>
```

![readitem](./doc/img/read-item.png)

POST:

```postman
http://localhost:5000/items/create-one" + json item at request
```

![json sample](./doc/img/post-item.png)

PUT:

```postman
http://localhost:5000/inventory/update
```

![update-inventory](./doc/img/update-inventory.png)

```postman
http://localhost:5000/items/update-one/4 + json with update statment
```

![update-one](./doc/img/update-item.png)

DELETE

![delete-one](./doc/img/delete-item.png)

## Pre-req

* Mongo DB database: is necessary to have already created an atlas cluster in mongoDB.

## Database schema

The DBMS used is mongoDB, non-relation database, using a unique database ("ollivander_shop") with a unique collection ("items")

```python

{
    "_id":1,
    "name":"Sulfuras, item of god",
    "sell_in":5,
    "quality":10,
    "item_type":"Sulfuras
}
```

* _id = predefined id to unique identify an item
* name = the name of the item
* sell_in = the sell in date
* quality = the actual quality of the item
* item_type = the type of the item, used to catalog it

## Test

Development complete with TDD almost everytest. Used coverage to keep tracking of testing.

![tdd test](./doc/img/tdd.png)

![coverge](./doc/img/coverage.png)

### TOX

Tox is a tool which allow us to automate testing in different enviroments, also automate commands to keep track about testing

## CI/CD

Using github actions, tox and bandit keep track about the test and new features.

## Dockerized

To install the docker image of the application:

```cmd
docker pull docker push clearcb/flask-app:latest
```

Run a container

```cmd
docker run --name flask-local-app -e MONGO_ATLAS_URI="URI MONGO" -p 5000:5000 --rm clearcb/flask-app:latest
```

After running this command you will be able to use the application sending request to the same URL as above.
