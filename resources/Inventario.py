from flask_restful import Resource
from services.Services import Services
class Inventario(Resource):

    def get(self):

        return Services.inventory(),200
    
    def post(self):

        # Avoiding future problems
        pass
