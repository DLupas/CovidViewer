import unittest
from covidviewer import app, db, daily_parser, PastData, Hospitals

class TestDatabase(unittest.TestCase):

    def setUp(self):
        #creates a fake database for testing that does not interfere with the normal one
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.session.commit()

    def test_database_empty(self):
        #should be nothing in the database right nwo
        self.assertEqual(PastData.query.all(), [])
    
    def test_adding_entries(self):
        #dummy data
        entry1 = PastData(name="New York", region="New York", date="01-01-2020", cases_today=0, cumulative_cases=0, deaths_today=0, cumulative_deaths=0)
        entry2 = PastData(name="Alberta", region="Vancouver", date="02-02-2020", cases_today=1, cumulative_cases=1, deaths_today=1, cumulative_deaths=1)
        db.session.add(entry1)
        db.session.add(entry2)
        db.session.commit()
        data1 = PastData.query.filter_by(region="New York")
        self.assertEqual([i for i in data1][0].region, "New York")
        data2 = PastData.query.filter_by(region="Alberta")
        self.assertEqual([i for i in data2], [])

    def test_parser_returns_values(self):
        #checks that parser returns something
        data = daily_parser.extract()
        self.assertFalse(data == [])


if __name__ == '__main__':
    unittest.main()
    