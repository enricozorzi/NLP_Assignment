from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, words
from nltk.corpus import gutenberg
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk
import re
from nltk.metrics import *
from gensim.models import Word2Vec
from nltk.corpus import brown


import numpy as np
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')
# nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('omw-1.4')
nltk.download('movie_reviews')


def find_features(word_features):
   
    features = {}
    for w in word_features:
        features[w] = "eng"
    return features

def create_dataset(s):
    dataset = nltk.sent_tokenize(s)
    for i in range(len(dataset)):
        dataset[i] = dataset[i].lower()
        dataset[i] = re.sub(r'\W', ' ', dataset[i])
        dataset[i] = re.sub(r'\s+', ' ', dataset[i])
    return dataset

def list_100(dataset):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    word2count = {}
    for data in dataset:
        words_t = nltk.word_tokenize(data)
        # filtered_sentence = [w for w in words_t if not w.lower() in stop_words]
        words = []
        for w in words_t:
            words.append(lemmatizer.lemmatize(w))
        for word in words:
            if word not in word2count.keys():
                word2count[word] = 1
            else:
                word2count[word] += 1
    import heapq
    return heapq.nlargest(3000, word2count, key=word2count.get)

s= nltk.corpus.gutenberg.raw('bryant-stories.txt')



dataset = create_dataset(s)
np.random.shuffle(dataset)

#reference = dataset[:len(dataset)//2]
#test = dataset[len(dataset)//2:]

#reference = list_100(reference)
#test = list_100((test))

bow = list_100(dataset)
word_list= find_features(bow)


# set that we'll train our classifier with
training_set = word_list[:1900]

# set that we'll test against.
testing_set = word_list[1900:]


classifier = nltk.NaiveBayesClassifier.train(training_set)

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
