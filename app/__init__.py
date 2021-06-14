import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
	load_dotenv()
	app = Flask(__name__)
	
	app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
	app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

	db.init_app(app)

	from .views import views
	from .auth import auth

	from .models import Todo

	# create_database(app)

	app.register_blueprint(views, url_prefix='/')
	app.register_blueprint(auth, url_prefix='/auth')

	return app
	

def create_database(app):
	db.create_all(app=app)
	print('Created database')