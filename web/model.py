"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy
from helper import Utilities
from decimal import Decimal
import json, os
from config import DEV_DB,PROD_DB

db = SQLAlchemy()


##############################################################################
# Model definitions
# col_names = Utilities.column_names
# print(len(col_names))

class Advert(db.Model):
    """table holding date related to advert compaigns."""

    __tablename__ = "adverts"


    advert_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    advert_date = db.Column(db.String(14), nullable=True)
    slot_id = db.Column(db.Integer, nullable=True)
    device = db.Column(db.String(14), nullable=True)
    impressions = db.Column(db.Integer, nullable=True)

    # def __repr__(self):
    #     """Provide helpful representation when printed."""

    #     return f'device: {self.device} date: {self.date} impressions: {self.impressions}'



##############################################################################
# Helper functions

class DecimalEncoder(json.JSONEncoder):
    ''' this class is used to help serialize numbers with decimal (json cant serialize numbers with Decimal'''
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)  

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our  database
    if os.environ.get('DEBUG')=="1":
        app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = PROD_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from app import app
    connect_to_db(app)
    print("Connected to DB.") 