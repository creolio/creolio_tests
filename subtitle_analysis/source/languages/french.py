import spacy

class French:
    def get_file_ending(self):
        return "_fr.srt"

    def split_into_words(self, text):
        nlp = spacy.load("fr_core_news_sm")

        words = []
        doc = nlp(text)
        for sent in doc.sents:
            words.extend(token.text for token in sent)
        return words


