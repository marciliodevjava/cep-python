from flask import Flask
from flask_restful import Api

from resource.cep_resource import Cep

app = Flask(__name__)
api = Api(app)

api.add_resource(Cep, '/cep')

if __name__ == '__main__':
    app.run(debug=False)
