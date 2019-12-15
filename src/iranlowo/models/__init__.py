from pathlib import Path

from ruamel.yaml import YAML


def get_model_path(name):
    yaml = YAML(typ='safe')
    data = yaml.load(Path('/Users/Olamilekan/Desktop/Machine Learning/OpenSource/iranlowo/src/iranlowo/models/models.yml'))
    if name not in data.keys():
        raise ValueError("Model {} does not exist".format(name))
    else:
        print(data)
        return data[name]
