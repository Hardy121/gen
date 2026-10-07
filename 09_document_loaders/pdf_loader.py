from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    'jewellery_genai_phase_chart.pdf'
)

docs = loader.load()

print(docs[0].page_content)
print(len(docs))