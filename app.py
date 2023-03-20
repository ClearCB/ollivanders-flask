from flask import Flask
from flask_cors import CORS

from resources.inventory import inventory_bp
from resources.items import items_bp

from repository.Database import Database

app = Flask(__name__)

CORS(app)
Database.drop_collection()
Database.init_db()

app.register_blueprint(inventory_bp)
app.register_blueprint(items_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
