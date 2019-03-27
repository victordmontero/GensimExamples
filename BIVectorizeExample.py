from gensim import corpora
from collections import defaultdict
from pprint import pprint
from sys import argv
from os import path
import tempfile

def readToEnd(texto):
    textFile = open(texto,"r")
    content = textFile.read()
    textFile.close()
    return content

documents = []
for doc in argv[1:]:
    documents.append(readToEnd(doc))

stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

pprint(texts)

print "Saving dict01.dict on:",tempfile.gettempdir()

dict = corpora.Dictionary(texts)
dict.save(path.join(tempfile.gettempdir(),'dict01.dict'))

print(dict.token2id)

corpus = [dict.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize(path.join(tempfile.gettempdir(),'dict01.mm'),corpus)

pprint(corpus)
