from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
Migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Taxi(db.Model):
    __tablename__ = 'taxi'
    id = db.Column(db.Integer, primary_key=True)
    lon = db.Column(db.String(64))
    lat = db.Column(db.String(64))
    timestamp = db.Column(db.String(64))

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

if __name__ == '__main__':
	manager.run()
