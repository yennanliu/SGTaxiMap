import pytest, unittest
import sys
sys.path.append(".")   
from model import db, TaxiData
from run import app 
#from config import db 

class TestDB(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'database.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        #pass 

    def testModel(self):
        # taxi 1 
        taxi1 = TaxiData(103, 1.23, '2019-01-01')
        db.session.add(taxi1)
        # taxi2 
        taxi2 = TaxiData(104, 1.24, '2019-01-02')
        db.session.add(taxi2)
        #taxi 3 
        taxi3 = TaxiData(105, 1.25, '2019-01-03')
        db.session.add(taxi3)

        db.session.commit()
        assert len(TaxiData.query.all()) == 3 

 
if __name__ == "__main__":
    unittest.main()