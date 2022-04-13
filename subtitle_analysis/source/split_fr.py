import spacy
import re

nlp = spacy.load("fr_core_news_sm")

def split_into_words(text):
	words = []
	doc = nlp(text)
	for sent in doc.sents:
		words.extend(token.text for token in sent)
	return words


# def remove_empty_words(words):

# def split_into_words(text):
#     words = re.split("\W", text)
#     return words