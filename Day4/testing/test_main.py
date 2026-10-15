from fastapi.testclient  import TestClient
#pip install httpx2
from main import app      # app= FastAPI()

#mocked call to endpoint
client= TestClient(app) #swagger

def test_eligibility():
    payload={
        'income' : 60000,
        'age' : 25,
        'type': 'employee'
    }
    response= client.post('/loan-eligibility', json=payload)
    assert response.status_code==200
    assert response.json() =={'eligbility':True}
    
def test_noneligibility():
    payload={
        'income' : 60000,
        'age' : 45,
        'type': 'employee'
    }
    response= client.post('/loan-eligibility', json=payload)
    assert response.status_code==200
    assert response.json() =={'eligbility':False}