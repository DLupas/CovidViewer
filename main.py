from project import app

'''
from flask import Flask, render_template
#from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
import datetime
#import MySQLdb

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, default = datetime.datetime.now)
    province = db.Column(db.String(100))
    cases = db.Column(db.Integer)

    def __init__(self, date, province, cases):
        self.date = date
        self.province = province
        self.cases = cases
'''