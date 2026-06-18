from ai_integration.ingestion.pdf_extractor import extract_documents
from ai_integration.ingestion.loader import load_documents
import time
path = "data/raw/FY25_Q4_Consolidated_Financial_Statements.pdf"
parent_folder = "data/raw"
# print(extract_documents(path))
start_time = time.time()
print(extract_documents(path))
load_documents(parent_folder)

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")