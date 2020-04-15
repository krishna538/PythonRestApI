import json


def dictionary_to_json(dict1):
    try:
        if isinstance(dict1, dict):
            resultJson = json.dumps(dict1)
            return resultJson
        else:
            print("provided parameter is not a valid dictionary type")
            raise Exception()
    except:
        raise Exception("Unable to convert dictionary into Json string")


def json_to_dictionary(json_obj):
    try:
        if isinstance(json_obj, str):
            resultDict = json.loads(json_obj)
            return resultDict
        else:
            print("provided parameter is not a valid type of json string")
            raise Exception()
    except:
        raise Exception("Unable to convert json string into dictionary Object")