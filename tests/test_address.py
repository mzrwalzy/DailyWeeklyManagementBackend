from tests._base import client
from tests import common_checks as checks

def test_address_create():
    response = client.post('/addresses/', json={})
    checks.check_response_is_200(response)
    checks.check_response_is_application_json(response)
    checks.check_response_structure(response)
    checks.check_response_has_cors(response)

    r = response.json()
    assert 400 == r['code']