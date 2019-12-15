import unittest

from iranlowo import corpus


class TestCoprusLoader(unittest.TestCase):
    def setUp(self):
        self.yoruba_blog_path = ""
        self.owe_loader = corpus.OweLoader

    def test_load_owe(self):
        with self.assertRaises(NotADirectoryError):
            self.owe_loader()

    def test_load_yorubablog(self):
        yor = corpus.YorubaBlogCorpus(path=self.yoruba_blog_path)
        self.assertIsInstance(corpus.Corpus, yor)

    def load_yoruba_text_coprus(self):
        pass
