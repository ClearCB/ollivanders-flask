from flask_restful import Resource
from services.Services import Services


class Items(Resource):

    def get(self,id):

        return Services.get_one(int(id)), 200

    def post(self):

        # Avoiding future problems
        pass

    