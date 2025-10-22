import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from app import app

def test_home():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert "Aplicación segura" in r.get_data(as_text=True)

def test_login_success():
    client = app.test_client()
    r = client.post("/login",
                    data=json.dumps({"username":"admin","password":"1234"}),
                    content_type='application/json')
    assert r.status_code == 200
    assert "Acceso concedido" in r.get_data(as_text=True)

def test_login_fail():
    client = app.test_client()
    r = client.post("/login",
                    data=json.dumps({"username":"admin","password":"mala"}),
                    content_type='application/json')
    assert r.status_code == 401
    assert "Credenciales inv" in r.get_data(as_text=True)
