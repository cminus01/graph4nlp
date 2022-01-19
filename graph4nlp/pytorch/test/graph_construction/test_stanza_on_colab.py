import json
import os
import stanza

corenlp_dir = './corenlp'
stanza.install_corenlp(dir=corenlp_dir)


from stanza.server import CoreNLPClient



class TestStanzaWithStanfordCoreNLP:
    text = "James went to the corner-shop. He want to buy some (eggs), <milk> and bread for breakfast."
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
        print(new_dict)
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

        print(new_dict)
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
        print(new_dict)



        print("Test ie parsing: openie.............")

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
        print(new_dict)

        client.stop()



if __name__ == "__main__":
    test_obj = TestStanzaWithStanfordCoreNLP()
    test_obj.test_dependency()
    test_obj.test_constituency()
    test_obj.test_ie()



