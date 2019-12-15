import os
import yaml

from .corpus import Corpus, DirectoryCorpus
from .loaders import OweLoader, YorubaBlogCorpus, BBCCorpus, BibeliCorpus


def get_corpus(name, single=False):
    with open(os.path.join(os.path.dirname(__file__), 'corpus.yml'), 'r') as stream:
        data = yaml.safe_load(stream)
    if name not in data.keys():
        raise ValueError("Corpus {} does not exist".format(name))
    else:
        if not single:
            return Corpus(path=data[name]).data
        else:
            return DirectoryCorpus(path=data[name])


def get_corpus_path(name):
    with open(os.path.join(os.path.dirname(__file__), 'corpus.yml'), 'r') as stream:
        data = yaml.safe_load(stream)
        if name not in data.keys():
            raise ValueError("Corpus {} does not exist".format(name))
        else:
            return os.path.join(os.path.dirname(__file__), data[name])


def download_corpus(name, uri=None):
    pass

