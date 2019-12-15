import os
import yaml


def get_model_path(name):
    with open(os.path.join(os.path.dirname(__file__), 'models.yml'), 'r') as stream:
        data = yaml.safe_load(stream)
        if name not in data.keys():
            raise ValueError("Model {} does not exist".format(name))
        else:
            return os.path.join(os.path.dirname(__file__), data[name])
