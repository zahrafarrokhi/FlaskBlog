from flask import Flask
from mod_admin import admin
app=Flask(__name__)
app.register_blueprint(admin)

@app.route('/')
def index():
    return "hello world!"