import nltk
import numpy as np
#nltk.download('punkt')
# 'punkt' is a tokenizer that divides the text into smaller elements by using an unsupervised algorithm
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    #working of bag of words
    # sentence = ['how', 'are', 'you']
    # words = ['hi','how','hello','you','ok']
    # bag = [0, 1, 0, 1, 0]
     
    #stemming of each word is performed
    sentence_words = [stem(w) for w in tokenized_sentence]

    #initialize the bag with zeroes for every word
    bag = np.zeros(len(all_words), dtype = np.float32)
    for idx,w in enumerate(all_words):
        if w in sentence_words:
            bag[idx] = 1.0

    return bag



