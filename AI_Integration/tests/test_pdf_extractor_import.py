import importlib


def test_pdf_extractor_imports_without_fitz_tools_error():
    module = importlib.import_module("ai_integration.ingestion.pdf_extractor")
    assert hasattr(module, "extract_documents")
