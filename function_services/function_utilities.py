import json


def GetConfiguration(file):
    with open(file, "r") as config_file:
        return json.load(config_file)