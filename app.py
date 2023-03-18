from flask import Flask
from flask_restful import Api


from resources.Inventario import Inventario


app = Flask(__name__)

api = Api(app, catch_all_404s=True)

api.add_resource(Inventario, "/inventory")


if __name__ == "__main__":
    app.run()
