from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")
pages = loader.load()

print("Number of pages: " , len(pages))
print(pages[0].page_content[:300])
print(pages[0].metadata)