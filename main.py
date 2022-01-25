from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class FlaskAPI(Resource):

    def get(self):
        return 200


api.add_resource(FlaskAPI, "/")

if __name__ == "__main__":
    app.run(debug=True)
