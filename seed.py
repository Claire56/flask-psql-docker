"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import Advertising
import pdb
from helper import load_json , Utilities , get_date


from model import connect_to_db, db
from app import app



def seed_db():
    """Load data into database."""
    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    Advertising.query.delete()
    #get data 
    data = load_json(Utilities.input_file)
    for record in data:
        str_date, slot_id = record['date'], record['slot_id']
        device, impressions = record['device'], record['impressions']
        date = get_date(str_date)

        # insert data
        advertising = Advertising(date = date, slot_id= slot_id,impressions =int(impressions)
        , device = device)

        # We need to add to the session or it won't ever be stored
        # pdb.set_trace()
        db.session.add(advertising)

    # Once we're done, we should commit our work
    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # seed database
    seed_db()
    
