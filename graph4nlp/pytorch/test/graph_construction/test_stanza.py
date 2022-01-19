import json
import stanza

corenlp_dir = './corenlp'
stanza.install_corenlp(dir=corenlp_dir)


# os.environ["CORENLP_HOME"] = "/home/shiina/software/stanford-corenlp-4.0.0"
import unittest

from stanfordcorenlp import StanfordCoreNLP


from stanza.server import CoreNLPClient



class TextStanzaWithStanfordCoreNLP(unittest.TestCase):
    text = "James went to the corner-shop. He want to buy some (eggs), <milk> and bread for breakfast."

    nlp_parser = StanfordCoreNLP("http://localhost", port=9000, timeout=300000)
    maxDiff = None
    def test_dependency(self):
        print("Test dependency parsing api.........")
        client = CoreNLPClient(
            annotators=[ "ssplit,tokenize,depparse"], 
            memory='4G', 
            endpoint='http://localhost:9001',
            be_quiet=True,
            output_format="json")
        client.start()

        output = client.annotate(
            text=self.text,
            properties={
            "tokenize.options": "splitHyphenated=false,normalizeParentheses=false,"
                            "normalizeOtherBrackets=false",
                            "tokenize.whitespace": True,
                            "ssplit.isOneSentence": True,
        })
        new_dict = output

        old_output = self.nlp_parser.annotate(text=self.text, properties={
                            "annotators": "ssplit,tokenize,depparse",
                            "tokenize.options": "splitHyphenated=false,normalizeParentheses=false,"
                            "normalizeOtherBrackets=false",
                            "tokenize.whitespace": True,
                            "ssplit.isOneSentence": True,
                            "outputFormat": "json",
                        })

        old_dict = json.loads(old_output)

        self.assertEqual(new_dict, old_dict)
        client.stop()

    def test_constituency(self):
        print("Test constituency parsing api.........")
        client = CoreNLPClient(
            annotators=[ "tokenize,ssplit,pos,parse"], 
            memory='4G', 
            endpoint='http://localhost:9001',
            be_quiet=True,
            output_format="json")
        client.start()

        output = client.annotate(
            text=self.text,
            properties={
            "tokenize.options": "splitHyphenated=false,normalizeParentheses=false,"
                    "normalizeOtherBrackets=false",
                    "tokenize.whitespace": True,
                    "ssplit.isOneSentence": False,
        })
        new_dict = output

        old_output = self.nlp_parser.annotate(text=self.text, properties={
                            "annotators": "tokenize,ssplit,pos,parse",
                    "tokenize.options": "splitHyphenated=false,normalizeParentheses=false,"
                    "normalizeOtherBrackets=false",
                    "tokenize.whitespace": True,
                    "ssplit.isOneSentence": False,
                    "outputFormat": "json",
                        })

        old_dict = json.loads(old_output)

        self.assertEqual(new_dict, old_dict)
        client.stop()

    def test_ie(self):
        print("Test ie parsing api: coref.........")
        client = CoreNLPClient(
            annotators=[ "tokenize, ssplit, pos, lemma, ner, parse, coref, openie"], 
            memory='4G', 
            endpoint='http://localhost:9001',
            be_quiet=True,
            output_format="json")
        client.start()

        output = client.annotate(
            text=self.text,
            properties={
                "annotators": "tokenize, ssplit, pos, lemma, ner, parse, coref",
           "tokenize.options": "splitHyphenated=true,normalizeParentheses=true,"
                    "normalizeOtherBrackets=true",
                    "tokenize.whitespace": False,
                    "ssplit.isOneSentence": False,
        })
        new_dict = output

        old_output = self.nlp_parser.annotate(text=self.text, properties={
                            "annotators": "tokenize, ssplit, pos, lemma, ner, parse, coref",
                    "tokenize.options": "splitHyphenated=true,normalizeParentheses=true,"
                    "normalizeOtherBrackets=true",
                    "tokenize.whitespace": False,
                    "ssplit.isOneSentence": False,
                    "outputFormat": "json",
                        })

        old_dict = json.loads(old_output)

        self.assertEqual(new_dict, old_dict)

        # client.stop()


        print("Test ie parsing: openie.............")

        # client = CoreNLPClient(
        #     annotators=[ "tokenize, ssplit, pos, ner, parse, openie"], 
        #     memory='4G', 
        #     endpoint='http://localhost:9001',
        #     be_quiet=True,
        #     output_format="json")


        output = client.annotate(
            text=self.text,
            properties={
                    "annotators": "tokenize, ssplit, pos, ner, parse, openie",
                    "tokenize.options": "splitHyphenated=true,normalizeParentheses=true,"
                    "normalizeOtherBrackets=true",
                    "tokenize.whitespace": False,
                    "ssplit.isOneSentence": False,
                    # "outputFormat": "json",
                    "openie.triple.strict": "true",
                })
        new_dict = output

        old_output = self.nlp_parser.annotate(text=self.text, properties={
                    "annotators": "tokenize, ssplit, pos, ner, parse, openie",
                    "tokenize.options": "splitHyphenated=true,normalizeParentheses=true,"
                    "normalizeOtherBrackets=true",
                    "tokenize.whitespace": False,
                    "ssplit.isOneSentence": False,
                    "outputFormat": "json",
                    "openie.triple.strict": "true",
                })

        old_dict = json.loads(old_output)
        # print(new_dict)
        # print("--------")
        # print(old_dict)
        # exit(0)

        self.assertEqual(new_dict, old_dict)

        client.stop()



if __name__ == "__main__":
    unittest.main()



