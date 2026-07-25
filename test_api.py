import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_get_single_user():
    headers = {
        "x-api-key": os.getenv("REQRES_API_KEY")
    }
    response = requests.get("https://reqres.in/api/users/2", headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2

def test_create_user():
    headers = {"x-api-key": os.getenv("REQRES_API_KEY")}
    payload = {
        "name": "John Doe",
        "job": "QA Automation Engineer"
    }
    response = requests.post("https://reqres.in/api/users", json=payload, headers=headers)
    
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["job"] == "QA Automation Engineer"


def test_update_user():
    headers = {"x-api-key": os.getenv("REQRES_API_KEY")}
    payload = {
        "name": "John Doe",
        "job": "Senior QA Engineer"
    }
    response = requests.put("https://reqres.in/api/users/2", json=payload, headers=headers)
    
    assert response.status_code == 200
    
    data = response.json()
    assert data["job"] == "Senior QA Engineer"


def test_delete_user():
    headers = {"x-api-key": os.getenv("REQRES_API_KEY")}
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)
    
    assert response.status_code == 204

def test_get_nonexistent_user():
    headers = {"x-api-key": os.getenv("REQRES_API_KEY")}
    response = requests.get("https://reqres.in/api/users/999", headers=headers)
    
    assert response.status_code == 404        