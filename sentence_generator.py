import random
import nltk
import threading
from queue import Queue

# Download the nltk data (if not already downloaded)
nltk.download('reuters')
nltk.download('punkt')

# Load the reuters corpus
from nltk.corpus import reuters

class SentenceGenerator:
    sentences = reuters.sents()
    sentence_queue = Queue()
    sentence_queue_lock = threading.Lock()

    @staticmethod
    def generate_sentence(max_words=4):
        random_sentence = random.choice(SentenceGenerator.sentences)
        random_sentence = random_sentence[:max_words]  # Limit to max_words
        return ' '.join(random_sentence)

    @staticmethod
    def refill_queue(num_sentences=100000, max_words=4):
        print(f"fill queue request {num_sentences}")
        new_sentences = [SentenceGenerator.generate_sentence(max_words) for _ in range(num_sentences)]
        with SentenceGenerator.sentence_queue_lock:
            for sentence in new_sentences:
                SentenceGenerator.sentence_queue.put(sentence)
        print(f"fill queue request completed {num_sentences}")

    @staticmethod
    def get_next_sentence():
        if SentenceGenerator.sentence_queue.empty():
            SentenceGenerator.refill_queue(100000)
        return SentenceGenerator.sentence_queue.get()

