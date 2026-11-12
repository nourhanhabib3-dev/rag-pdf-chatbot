import chromadb 
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
from app import chunks 

ef = DefaultEmbeddingFunction()
client = chromadb.PersistentClient(path='./chroma_db')
collection = client.get_or_create_collection(name='docs' , embedding_function=ef)
collection.upsert(
    ids=[f'chunk-{i}' for i in range(len(chunks))],
    documents=[c.page_content for c in chunks],
    metadatas=[{'source': c.metadata['source'], 'page': c.metadata['page']} for c in chunks],
)
res = collection.query(query_texts=[' what is a large language model ? '], n_results= 1)
print(res['documents'][0][0])



