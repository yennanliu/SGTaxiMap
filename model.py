from config import *

class TaxiData(db.Model):
    __tablename__ = 'taxi'

    def __init__(self
                 , lon
                 , lat
                 , timestamp
                 ):
        self.lon = lon
        self.lat = lat
        self.timestamp = timestamp

    def __repr__(self):
         return '<Taxi {}>'.format(self.timestamp)