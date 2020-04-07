import pytest, unittest
import sys
sys.path.append(".")   
from model import db, TaxiData
from run import app 
#from config import db 

# class SetupDB(unittest.TestCase):
#     def __init_(self):
#         self.app = app.test_client()
#         self.app.config['TESTING'] = True
#         self.app.config['WTF_CSRF_ENABLED'] = False
#         self.app.config['DEBUG'] = False
#         self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'database.db'
#
#     def setUp(self):
#         db.drop_all()
#         db.create_all()
#         self.assertEqual(app.debug, False)
#
#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()

@pytest.fixture(scope="function")
def db_cur():
    db.drop_all()
    db.create_all() 
    yield db 
    db.session.remove()
    db.drop_all()


def testInsert(db_cur):
    # insert test data : taxi 1 
    taxi1 = TaxiData(103, 1.23, '2019-01-01')
    db.session.add(taxi1)
    assert len(TaxiData.query.all()) == 1
    assert str(TaxiData.query.all()) == "[<Taxi 2019-01-01>]"

def testInsertDataCount(db_cur):
    # insert test data : taxi 1 
    taxi1 = TaxiData(103, 1.23, '2019-01-01')
    db.session.add(taxi1)
    # insert test data : taxi2 
    taxi2 = TaxiData(104, 1.24, '2019-01-02')
    db.session.add(taxi2)
    # insert test data : taxi 3 
    taxi3 = TaxiData(105, 1.25, '2019-01-03')
    db.session.add(taxi3)
    # commit change 
    db.session.commit()
    # validate the DB op
    assert len(TaxiData.query.all()) == 3

if __name__ == "__main__":
    unittest.main()