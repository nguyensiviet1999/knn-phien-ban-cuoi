import pandas as pd
from math import sqrt
from random import randrange
import pickle

X_data = pickle.load(open('X_data.pkl', 'rb'))
y_data = pickle.load(open('y_data.pkl', 'rb'))

X_test = pickle.load(open('X_test.pkl', 'rb'))
y_test = pickle.load(open('y_test.pkl', 'rb'))
def getNumOfWords(X_data_):
    numOfWords=[]
    for bagOfWords in X_data_:
        numOfWordsTemp = dict.fromkeys(set(bagOfWords.split(' ')).union(), 0)
        for word in bagOfWords.split(' '):
            numOfWordsTemp[word] += 1
        numOfWords.append(numOfWordsTemp)
    return numOfWords
def tfTranform(X_data_):
    numOfWords = getNumOfWords(X_data_)
    tf=[]
    for index, bagOfWords in enumerate(X_data_, start=0):
        tfTemp = computeTF(numOfWords[index], bagOfWords.split(' '))
        tf.append(tfTemp)
    return tf
def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict
def tranform_to_build_model(X_data,X_test):
    X_data_tf = tfTranform(X_data)
    X_test_tf = tfTranform(X_test)
    pickle.dump(X_test_tf, open('X_data_tf.pkl', 'wb'))
    pickle.dump(X_test_tf, open('X_test_tf.pkl', 'wb'))