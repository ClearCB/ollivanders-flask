from flask_restful import Resource, reqparse
from services.Services import Services


class Items(Resource):

    def get(self,id):

        return Services.get_one(int(id)), 200

    def post(self):

        pass
    # def parse_request():

    #     parser = reqparse.RequestParser(bundle_errors=True)
    #     parser.add_argument('_id', type=int, required=True,
    #                         help='id required')
    #     parser.add_argument('sell_in', type=int, required=True,
    #                         help='sell_in required')
    #     parser.add_argument('quality', type=int, required=True,
    #                         help='quality required')
    #     parser.add_argument('item_type', type=str, required=True,
    #                         help='quality required')
    #     # args = parser.parse_args()
    #     # es un diccionario con los argumentos
    #     # especificados como keys
    #     return parser.parse_args()