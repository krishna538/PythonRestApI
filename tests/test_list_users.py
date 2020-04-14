import rest_client
import pytest
import json

def test_list_users_get_request():

    response = rest_client.get_request('/api/users/?page=2')
    # printing the response
    print(response.json()) # printing json response without pretty format
    print(json.dumps(response.json(), indent=4)) # printing the json response with pretty format
    print(response.headers) # printing the response headers
    # checking the status code
    assert response.status_code == 200
    # checking the total number of data objects in the response
    assert len(response.json()['data']) == 6
    # checking the list of first_names from the response
    expected_first_name = ['George', 'Janet', 'Emma', 'Charles', 'Eve', 'Tracey']
    actual_first_names = [d['first_name'] for d in response.json()['data']]
    assert expected_first_name.sort() == actual_first_names.sort()


def test_single_user():
    id = 2
    response = rest_client.get_request('/api/users/'+str(id))
    print(response.json())

    # validating the length of the data object
    assert len(response.json()['data']) == 5
    # validating the id, email, first_name, last_name and avatar data
    assert response.json()["data"]['id'] == 2
    expected_user_data = {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg"
    }
    actual_user_data = response.json()["data"]
    assert expected_user_data == actual_user_data


def test_create_user():

    # creating the payload for the request
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = rest_client.post_request('/api/users', data=data)
    print(response.json())
    # validating the name and job in the response
    assert response.json()['name'] == data['name']
    assert response.json()['job'] == data['job']


def test_delete_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = rest_client.post_request('/api/users', data=data)
    print(response.json())

    id = response.json()['id']
    print(id)
    response = rest_client.delete_request('/api/users/' + str(id))

    # validating the response code
    assert response.status_code == 204
    # validating the response
    assert response.text == ""
