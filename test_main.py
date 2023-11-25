import unittest
from flask_testing import TestCase
from main import get_all_user_hobbies_customer, get_user_hobbies_per_year_customer, get_all_count_user_hobbies_per_year
from schemas.analytics_db import UserHobby, db
from flask import Flask


class TestFlaskApi(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)

        app.add_url_rule('/', 'get_all_user_hobbies', get_all_user_hobbies_customer, methods=['GET'])
        app.add_url_rule('/<int:join_year>', 'get_user_hobbies_per_year', get_user_hobbies_per_year_customer,
                         methods=['GET'])
        app.add_url_rule('/count/<int:join_year>', 'get_all_count_user_hobbies_per_year',
                         get_all_count_user_hobbies_per_year, methods=['GET'])

        return app

    def setUp(self):
        with self.app.app_context():
            db.create_all()
            db.session.add(UserHobby(hobby_name='Painting', join_year=2018))
            db.session.add(UserHobby(hobby_name='Dancing', join_year=2018))
            db.session.add(UserHobby(hobby_name='Cooking', join_year=2019))
            db.session.commit()

    def test_get_all_user_hobbies(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)

    def test_get_user_hobbies_per_year(self):
        response = self.client.get('/2018')
        self.assertEqual(response.status_code, 200)
        hobbies = response.json
        self.assertIn('Cooking', hobbies)

    def test_get_all_count_user_hobbies_per_year(self):
        response = self.client.get('/count/2018')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['year'], 2018)
        self.assertEqual(data['distinct_hobby_count'], 2)


if __name__ == '__main__':
    unittest.main()
