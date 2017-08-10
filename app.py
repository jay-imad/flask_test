from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from resources.user import UserRegister
from resources.item import Item, Itemlist
from resources.store import Store, StoreList

from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jay'
api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()

jwt = JWT(app,authenticate,identity) #/auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist,'/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister,'/register')

if __name__=='__main__':
	from db import db
	db.init_app(app)
	app.run(port=5002, debug=True)