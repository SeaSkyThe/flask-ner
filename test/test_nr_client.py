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

    def test_get_ents_returns_dictionery_given_nonempty_string_causes_empty_spacy_doc_ents (self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Oklahoma City is the capital of Oklahoma State")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Pharrell Williams', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Pharrell Williams', 'label': 'Person'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Brazilian', 'label_': 'NORP'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Brazilian', 'label': 'Group'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Brazil', 'label_': 'LOC'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Brazil', 'label': 'Location'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Brazilian', 'label_': 'NORP'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Brazilian', 'label': 'Group'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])
    
    def test_get_ents_given_spacy_LANGUAGE_is_returned_serializes_to_Language(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Portuguese', 'label_': 'LANGUAGE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Portuguese', 'label': 'Language'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_GPE_is_returned_serializes_to_Location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Australia', 'label_': 'GPE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Australia', 'label': 'Location'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_multiple_ents_serializes_all(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Australia', 'label_': 'GPE'}, {'text': 'Judith Polgar', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = { 'ents': 
                        [{'ent': 'Australia', 'label': 'Location'}, {'ent': 'Judith Polgar', 'label': 'Person'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])