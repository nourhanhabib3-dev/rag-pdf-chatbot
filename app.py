from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")
pages = loader.load()

# print("Number of pages: " , len(pages))
# print(pages[0].page_content[:300])
# print(pages[0].metadata)

from langchain_text_splitters import RecursiveCharacterTextSplitter 

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 50,
    add_start_index = True
)

chunks = splitter.split_documents(pages)

