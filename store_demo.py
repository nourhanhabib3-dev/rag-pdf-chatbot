import chromadb 
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
from app import chunks 

# print('chunks' , len(chunks))

ef = DefaultEmbeddingFunction()
client = chromadb.PersistentClient(path='./chroma_db')
collection = client.get_or_create_collection(name='docs' , embedding_function=ef)
collection.upsert(
    ids=[f'chunk-{i}' for i in range(len(chunks))],
    documents=[c.page_content for c in chunks],
    metadatas=[{'source': c.metadata['source'], 'page': c.metadata['page']} for c in chunks],
)

print('store' , collection.count())