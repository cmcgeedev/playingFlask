import json


class AppConfig:
    def __init__(self, args):
        self.Env = args["Env"]
        self.Port = args["Port"]
        self.Debug = args["Debug"]


instanceConfig = None


def get_config():
    return instanceConfig


def load_config(configFile):
    with open(configFile) as data_file:
        global instanceConfig
        instanceConfig = AppConfig(json.load(data_file))
    return