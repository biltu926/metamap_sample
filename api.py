from flask import Flask
from flask_marshmallow import Marshmallow

from models import Employee, Department, Project, Base
from db import session
from db import engine

app = Flask(__name__)
ma = Marshmallow(app)

def create_tables():
    ''' Creates all the tables '''
    Base.metadata.create_all(engine)

'''book = Books(
    bname = "India's ancient past",
    author = "R.S Sharma",
    bid = 101
)
'''

session.add(book)
session.commit()
session.close()