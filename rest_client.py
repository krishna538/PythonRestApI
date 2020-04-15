import requests
import json


base_url = "https://reqres.in"


def get_request(resource):
    response = requests.get(base_url + resource)
    return response


def get_request_headers(resource, headers):
    response = requests.get(base_url+resource, headers=headers)
    return response


def get_request_with_parameters(resource, params):
    response = requests.get(base_url+resource, params=params)
    return response


def get_request_with_parameters_headers(resource, params, headers):
    response = requests.get(base_url+resource, params=params, headers=headers)
    return response


def post_request(resource, data):
    response = requests.post(base_url + resource, data= data)
    return response


def post_request_headers(resource, data, headers):
    response = requests.post(base_url + resource, data= data, headers=headers)
    return response


def delete_request(resource):
    response = requests.delete(base_url + resource)
    return response




# if you want to ignore the SSL certification error pass peramater as (verify = False)
# If you want to add authentication to the input requests add parameter as (auth = ('user', 'pass'))






