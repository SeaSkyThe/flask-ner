import unittest
import json
from flask import request

from app import app

class TestApi(unittest.TestCase):
    def test_ner_endpoint_given_json_body_returns_200(self):
        with app.test_client() as client:
            response = client.post('/ner', json={'sentence': 'Steven Rodriguez is a latino guy.'})
            assert response._status_code == 200

    def test_ner_endpoint_given_json_body_with_known_entities_returns_entity_result_in_response(self):
        with app.test_client() as client:
            response = client.post('/ner', json={'sentence': 'Steven Rodriguez'})
            data = json.loads(response.get_data())
            assert data['entities'][0]['ent'] == 'Steven Rodriguez'
            assert data['entities'][0]['label'] == 'Person'