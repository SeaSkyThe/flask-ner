import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble

class TestNerClient(unittest.TestCase):
    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        # ents = { ents: [{...}],
        #          html: "<span>..."}

        # Our object from the class 'NamedEntityClient'
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        # Will have a 'get_ents' method, that will receive a string and return a dict
        # In this case, we are testing with a empty string
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionery_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Oklahoma City is the capital of Oklahoma State")
        self.assertIsInstance(ents, dict)

    