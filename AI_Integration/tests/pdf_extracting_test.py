from ai_integration.ingestion.pdf_extractor import extract_documents
from ai_integration.ingestion.loader import load_documents
import time
path = "ai_integration/tests/FY25_Q4_Consolidated_Financial_Statements.pdf"
parent_folder = "data/raw"
# print(extract_documents(path))
start_time = time.time()
sections = extract_documents(path)
for section in sections:
    if section["section_type"] == "table":
        print(f"Section Title: {section['section_title']}")
        print(f"Page Number: {section['page']}")
        print(f"Source: {section['source']}")
        print("Table Text:")
        print(section["text"])
        print("\n" + "="*50 + "\n")
# load_documents(parent_folder)

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")