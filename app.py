from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Development


app=Flask(__name__)
app.config.from_object(Development)

# db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from views import index


# blueprint
from mod_admin import admin
from mod_users import users

app.register_blueprint(admin)
app.register_blueprint(users)
