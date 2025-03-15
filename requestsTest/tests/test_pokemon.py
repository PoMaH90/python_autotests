import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '55a03d626d66efb206949ac499672cb9'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '22502'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_trainer():
    response_trainer = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_trainer.json()['data'][0]['trainer_name'] == 'спектор'