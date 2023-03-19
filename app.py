from flask import Flask, request
from flask_cors import CORS

from repository.Database import Database
from services.Services import Services

app = Flask(__name__)
CORS(app)
Database.drop_collection()
Database.init_db()

@app.route("/inventory", methods=["GET"])
def inventory():

    return Services.inventory()


if __name__ == "__main__":
    app.run()
