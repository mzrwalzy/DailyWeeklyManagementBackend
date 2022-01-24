from requests import Response


def check_response_is_200(response: Response):
    assert response.status_code == 200


def check_response_is_application_json(response: Response):
    assert response.headers.get('content-type', '') == 'application/json'


def check_response_structure(response: Response):
    r = response.json()
    assert 'code' in r and ('data' in r or 'msg' in r)


def check_response_has_cors(response: Response):
    pass
