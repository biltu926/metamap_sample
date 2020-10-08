from flask import Flask
from flask_smorest import Api, Blueprint

class Config:
    API_TITLE = '''Metamap APIs'''
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_URL = 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.32.5/'
    #OPENAPI_SWAGGER_UI_CONFIG = {'supportedSubmitMethods': []}

app = Flask(__name__)

app.config.from_object(Config)

api = Api(app, spec_kwargs={'info': {"description": '''A simple web app'''}})

blueprint = Blueprint('Metamap', 'Random', url_prefix='/web/teaching',
                               description=''' APIs''')