from flask_restful import Resource

class Users(Resource):
    def get(self):
        return {"Data":"Hurray!!"}