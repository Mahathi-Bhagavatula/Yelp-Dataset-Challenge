import pandas as pd
import json
import cPickle
from nltk import sent_tokenize
from nltk.corpus import stopwords
from gensim import corpora, models

stop_words = stopwords.words()
vector_sentences=[]

subset = cPickle.load(open("/Users/mahathi/Downloads/yelp_data_subset.pkl"))
all_sentences =[]
for each_data in subset:
    text = each_data["text"]
    text = text.lower()
    sentences = sent_tokenize(text)
    all_sentences.extend(sentences)
    
 for each_sent in all_sentences:
    vector_sentences.append(each_sent.split())
    
texts = [[word for word in sentence.lower().split() if word not in stop_words] for sentence in all_sentences]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
lda = models.LdaModel(corpus, num_topics=3, id2word=dictionary)
lda.print_topics(num_topics=3, num_words=50)

model = models.Word2Vec(vector_sentences, size=100, window=5, min_count=2, workers=4)
model.most_similar("chicken", topn=20)
