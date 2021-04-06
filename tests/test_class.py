import pytest

import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.sentiment import extract_sentiment, text_contain_word


class TestClass:

    def test_one(self):
        x = "this"
        assert "h" in x
        print(myPath)


    # Le retours des fonctions
    def test_extract_sentiment_positive(self):
        text = "Today I found a duck and I am happy"
        sentiment = extract_sentiment(text)
        assert sentiment >= 0

    def test_extract_sentiment_negative(self):
        text = "I do not think this will turn out well"
        sentiment = extract_sentiment(text)
        assert sentiment <= 0

    # Les paramètres des fonctions
    @pytest.mark.parametrize('texts', [
        'Python is a high-level, general-purpose programming language.',
        'I think today will be a great day',
        'Beautiful is better than ugly.'])
    def test_texts(self, texts):
        assert 0 <= extract_sentiment(texts)

    @pytest.fixture
    def example_data(self):
        return 'Today I found a duck and I am happy'

    def test_extract_sentiment(self, example_data):
        sentiment = extract_sentiment(example_data)
        assert sentiment > 0

    def test_text_contain_word(self, example_data):
        word = 'duck'
        assert text_contain_word(word, example_data) is True

    # La bonne gestion des erreurs
    def myfunc(self):
        raise ValueError("Exception 123 raised")

    def test_match(self):
        with pytest.raises(ValueError, match=r".* 123 .*"):
            self.myfunc()
