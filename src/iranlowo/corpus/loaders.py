import os

from iranlowo.corpus import Corpus, DirectoryCorpus
from iranlowo.corpus import get_corpus_path

import os

os.environ['YORUBA_TEXT_PATH'] = '/Users/Olamilekan/Desktop/Machine Learning/OpenSource/yoruba-text'


class YorubaCorpusLoader(object):
    def __init__(self, corpus_code):
        self.corpus_code = corpus_code

    def __call__(self, *args, **kwargs):
        yoruba_text_path = os.environ.get("YORUBA_TEXT_PATH", None)
        if not yoruba_text_path:
            raise NotADirectoryError(
                "YORUBA_TEXT_PATH environment variable not found. Please, clone the corpus repository from https://github.com/Niger-Volta-LTI/yoruba-text and set to YORUBA_TEXT_PATH to it's "
                "path")
        else:
            corpus_path = "{}/{}".format(yoruba_text_path, self.corpus_code)
            self.path = corpus_path


ne = YorubaCorpusLoader('yoruba_blog')

# class YorubaBlogCorpus(BaseLoader, Corpus):
#     def __init__(self, **kwargs):
#         """
#
#         Args:
#             path:
#         """
#         path = 'TheYorubaBlog/theyorubablog_dot_com.txt'
#         BaseLoader.__init__(self, corpus_path=path)
#         Corpus.__init__(self, path=BaseLoader.path, **kwargs)
#
#         # super(YorubaBlogCorpus, self).__init__(**kwargs)
#
#
# yor = YorubaBlogCorpus()
# print(yor.path)
#
#
# class BBCCorpus(Corpus):
#     def __init__(self, **kwargs):
#         """
#
#         Args:
#             path:
#         """
#         super(BBCCorpus, self).__init__(**kwargs)
#
#
# class BibeliCorpus(Corpus):
#     def __init__(self, **kwargs):
#         """
#
#         Args:
#             path:
#         """
#         super(BibeliCorpus, self).__init__(**kwargs)
#
#
# class en(BaseLoader, DirectoryCorpus):
#     def __init__(self):
#         BaseLoader.__init__(self, corpus_path="Owe/en")
#         DirectoryCorpus.__init__(self, path=self.path)
#
#
# class yo(BaseLoader, DirectoryCorpus):
#     def __init__(self):
#         BaseLoader.__init__(self, corpus_path="Owe/yo")
#         DirectoryCorpus.__init__(self, path=self.path)
#
#
# class OweLoader(object):
#     def __init__(self):
#         self.en = en()
#         self.yo = yo()
