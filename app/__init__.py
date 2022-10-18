from flask import Flask

myapp_obj = Flask(__name__)

myapp_obj.config.update(
        SECRET_KEY = 'joao'
)

from app import routes
