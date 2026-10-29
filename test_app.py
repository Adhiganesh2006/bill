from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Kubernetes CI/CD is working" in response.data

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_calculate_total_bill_success():
    client = app.test_client()
   
    payload = {"price": 25.50, "quantity": 4}
    response = client.post("/calculate", json=payload)
    
    assert response.status_code == 200
    assert response.json["total_bill"] == 102.0
    assert response.json["price"] == 25.50
    assert response.json["quantity"] == 4

def test_calculate_missing_fields():
    client = app.test_client()
  
    payload = {"price": 10.0}
    response = client.post("/calculate", json=payload)
    
    assert response.status_code == 400
    assert "error" in response.json

def test_calculate_invalid_data_types():
    client = app.test_client()
    
    payload = {"price": "ten dollars", "quantity": 5}
    response = client.post("/calculate", json=payload)
    
    assert response.status_code == 400
    assert "error" in response.json
