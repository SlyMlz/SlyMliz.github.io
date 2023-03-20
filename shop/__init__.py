import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask import render_template
# from werkzeug import UploadSet, IMAGES, configure_uploads, patch_request_class, flask_uploads
# from werkzeug.datastructures import  FileStorage


from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
 
# App = Blueprint("app", __name__)

###################################
##### * DataBase Setup ############
###################################
app.config["SECRET_KEY"] = "1234567890098765412345678"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] =  'sqlite:///'+ os.path.join(basedir, 'myshop.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()
###################################
##### * Handling Images ###########
###################################

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
# MAX_CONTENT_LENGTH(app) 

migrate = Migrate(app, db)
with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app,db, render_as_batch=True)
    else:
        migrate.init_app(app,db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'customerLogin'
login_manager.needs_refresh_message_category = 'danger'
login_manager.login_message = u"Please Login Sir/ Madam"

###################################
##### * Password Hashing ##########
###################################
bcrypt = Bcrypt(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(403)
def permisoDenegado(e):
    return render_template('403.html')

@app.errorhandler(500)
def serverError(e):
    #note that we set the 500 status explicitly
    return render_template('500.html')

@app.errorhandler(501)
def server_Error(e):
    #note that we set the 500 status explicitly
    return render_template('501.html')

###################################
##### * Routes ####################
###################################
from shop.admin import routes
from shop.products import routes
from shop.carts import carts
from shop.customers import routes

