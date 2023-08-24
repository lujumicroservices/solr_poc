import random
import nltk

# Download the nltk data (if not already downloaded)
nltk.download('reuters')

# Load the reuters corpus
from nltk.corpus import reuters

class WordGenerator:
    def __init__(self):
        self.sentences = reuters.sents()

    def generate_sentences(self, num_sentences=10, max_words=10):
        generated_sentences = []
        for _ in range(num_sentences):
            random_sentence = random.choice(self.sentences)
            random_sentence = random_sentence[:max_words]  # Limit to max_words
            generated_sentences.append(' '.join(random_sentence))
        return generated_sentences


