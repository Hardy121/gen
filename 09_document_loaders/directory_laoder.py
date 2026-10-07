from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="dct",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)
# docs = loader.lazy_load()
docs = loader.load()

for documents in docs:
    print(documents)