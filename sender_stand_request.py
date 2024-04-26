import configuration
import requests
import data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
def post_new_kit(body):
    auth_token = post_new_user(data.user_body).json()
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body,
                         headers=headers)

def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = post_new_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name
def negative_assert (name):
    kit_body = get_kit_body(name)
    kit_response = post_new_kit(kit_body)
    assert kit_response.status_code == 400

def negative_assert_no_body():
    kit_body = { }
    kit_response = post_new_kit(kit_body)
    assert kit_response.status_code == 400
