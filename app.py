from flask import Flask
from flask_restful import Api


from repository.Database import Database
from resources.Inventario import Inventario
from resources.Items import Items


app = Flask(__name__)

api = Api(app, catch_all_404s=True)

Database.init_db()

api.add_resource(Inventario, "/inventory")
api.add_resource(Items, "/items/<id>","/items")


if __name__ == "__main__":
    app.run()
