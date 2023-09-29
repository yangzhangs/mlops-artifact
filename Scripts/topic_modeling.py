import gensim
import pandas as pd
import pymysql
from bs4 import BeautifulSoup
import re
import os
import joblib

from gensim import corpora
from gensim.models import CoherenceModel
from nltk.stem import PorterStemmer
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
from ldamallet import LdaMallet
#import matplotlib.pyplot as plt
#%matplotlib inline

os.environ.update({'MALLET_HOME': r'D:/research-related/mallet-2.0.8/mallet-2.0.8'})
mallet_path = 'D:\\research-related\\mallet-2.0.8\\mallet-2.0.8\\bin\\mallet'  # update this path
stop_words = stopwords.words('english')
print(len(stop_words))

f = open('mallet-stopwords-en.txt',encoding='utf-8')
mallet_stopwords = f.readlines()
f.close()
for word in mallet_stopwords:
    stop_words.extend([word])

stop_words.extend(['mlops','mlflow','dvc','tfx','amazon-sagemaker','kubeflow','azure-machine-learning-service',
                   'amazon','sagemaker','azure','azureml','google','aws',
                   'google-cloud-ml-engine','kubeflow-pipelines','azureml-python-sdk','amazon-sagemaker-studio'])
print(len(stop_words))


porter = PorterStemmer()
# Define functions for stopwords
def remove_stopwords(text):
    return [word for word in simple_preprocess(str(text)) if word not in stop_words]


def removeOneTag(text, tag):
    while (True):
        text = text[:text.find("<"+tag+">")] + text[text.find("</"+tag+">")+7:]
        #print(temp)
        if text.find("<"+tag+">")==-1:
            break
    return text

def preprocess(text):
    text = removeOneTag(text, "code")

    soup = BeautifulSoup(text,features="lxml").get_text()

    text1 = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', soup, flags=re.MULTILINE)

    text2 = remove_stopwords(text1)

    text4 = [porter.stem(word) for word in text2]

    return text4


def compute_coherence_values(dictionary, corpus, id2word, texts, limit, start=2, step=3):
    """
    Compute c_v coherence for various number of topics

    Parameters:
    ----------
    dictionary : Gensim dictionary
    corpus : Gensim corpus
    texts : List of input texts
    limit : Max num of topics

    Returns:
    -------
    model_list : List of LDA topic models
    coherence_values : Coherence values corresponding to the LDA model with respective number of topics
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        model = LdaMallet(mallet_path, corpus=corpus, num_topics=num_topics, id2word=id2word, alpha=50/num_topics, topic_threshold=0.01, iterations=500, random_seed=123)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())

    return model_list, coherence_values


def mallet_modeling(plt=None):
    clean_data = getCleanText()
    id2word = corpora.Dictionary(clean_data)
    # Create Corpus
    texts = clean_data
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]

    #ldamallet = LdaMallet(mallet_path, corpus=corpus, num_topics=20, id2word=id2word)
    #print(ldamallet.show_topics(formatted=False))
    #coherence_model_ldamallet = CoherenceModel(model=ldamallet, texts=clean_data, dictionary=id2word, coherence='c_v')
    #coherence_ldamallet = coherence_model_ldamallet.get_coherence()
    #print('\nCoherence Score: ', coherence_ldamallet)
    model_list, coherence_values = compute_coherence_values(dictionary=id2word, corpus=corpus, id2word=id2word, texts=clean_data,
                                                            start=5, limit=85, step=5)
    # Show graph
    #x = range(5, 80, 5)
    x = range(5, 85, 5)
    for m, cv in zip(x, coherence_values):
        print("Num Topics =", m, " has Coherence Value of", round(cv, 4))



if __name__ == '__main__':
    #mallet_modeling()
