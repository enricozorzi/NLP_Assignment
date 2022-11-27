# Assignment 1 / Enrico Zorzi - VR495467
The assignment consists in the development, in NLTK of Naïve Bayes Classifier able to distinguishing ENGLISH against NON-ENGLISH




## [Repository on github.](https://github.com/enricozorzi/NLP_distinguishing_ENGLISH_es1)



## Corpus
I built the classifier using NLTK and I chose europarl corpus in different language, but i don't import all the raw but only few character for each language, Its size seems to be appropriate for the task.

| Language | # of char |
| ----------- | ----------- |
| English | 800000 |
| Italian | 200000 |
| French | 200000 |
| Spanish | 200000 |
| German | 200000 |

## Train/test split
The dataset has been split in a train and test, 80% for train and 20% for test.

## Performance indicators
I used the following performance indicators:
- Accuracy: from nltk.classify.accuracy, it measures the percentage of items correctly identified
- Precision: from nltk.metrics.scores, it measures the percentage of positive class predictions that actually belong to the positive class
- Recall: from nltk.metrics.scores, it measures the percentage of positive class predictions made out of all positive examples in the dataset

- F1: from nltk.metrics.scores, it provides a single score that balances both the concerns of precision and recall in one number.



## Usage as a Probabilistic Language Model
This Classifier is able to distinguishing only if a sentence  probably appartain to ENGLISH or NON-ENGLISH
