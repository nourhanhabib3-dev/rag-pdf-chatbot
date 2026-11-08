import numpy as np 
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

ef = DefaultEmbeddingFunction()
text = ['i love cats '  , 'i adore kittens' , 'the stock market']

vectors = ef(text)

def cosine(a,b): 
    a, b = np.array(a) , np.array(b) 
    return float(np.dot(a , b) /(np.linalg.norm(a)*(np.linalg.norm(b))))

print(cosine(vectors[0] , vectors[1]))
print(cosine(vectors[0] , vectors[2]))
