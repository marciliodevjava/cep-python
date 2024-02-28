from flask import Flask
from flask_restful import Api

from config.configuracao import db
from config.segredo import SQLALCHEMY_DATABASE_URI, DATABASE_URI
from resource.cep_resource import Cep

app = Flask(__name__)
app.config[DATABASE_URI] = SQLALCHEMY_DATABASE_URI

db.init_app(app)
api = Api(app)

api.add_resource(Cep, '/cep')

if __name__ == '__main__':
    app.run(debug=False)
