from ai_integration.ingestion.chunking import chunk_text
from ai_integration.ingestion.loader import load_documents
from ai_integration.ingestion.chunking import chunk_documents
import yaml
import pandas as pd
from collections import Counter
import textwrap


def print_section_divider(title):
    """Print a formatted section divider"""
    print(f"\n{'='*80}")
    print(f"  {title}")
    print(f"{'='*80}\n")


def analyze_chunks(chunks):
    """Comprehensive analysis of chunked data"""
    
    # Convert to DataFrame for easier analysis
    df = pd.DataFrame(chunks)
    
    print_section_divider("CHUNKING ANALYSIS REPORT")
    
    # 1. Overall Statistics
    print("OVERALL STATISTICS")
    print(f"  Total chunks: {len(df)}")
    print(f"  Unique documents: {df['source'].nunique()}")
    print(f"  Unique sections: {df['section_title'].nunique()}")
    
    # 2. Section Type Analysis
    print_section_divider("SECTION TYPE DISTRIBUTION")
    section_counts = df['section_type'].value_counts()
    for section_type, count in section_counts.items():
        percentage = (count / len(df)) * 100
        bar = "█" * int(percentage / 5)
        print(f"  {section_type:15} : {count:4} chunks ({percentage:5.1f}%) {bar}")
    
    # 3. Chunk Size Analysis
    print_section_divider("CHUNK SIZE STATISTICS")
    df['chunk_length'] = df['text'].str.len()
    
    print(f"  Average chunk size: {df['chunk_length'].mean():.0f} characters")
    print(f"  Median chunk size:  {df['chunk_length'].median():.0f} characters")
    print(f"  Min chunk size:     {df['chunk_length'].min():.0f} characters")
    print(f"  Max chunk size:     {df['chunk_length'].max():.0f} characters")
    print(f"  Std deviation:      {df['chunk_length'].std():.0f} characters")
    
    # 4. Chunk Size by Section Type
    print_section_divider("CHUNK SIZE BY SECTION TYPE")
    for section_type in df['section_type'].unique():
        section_data = df[df['section_type'] == section_type]['chunk_length']
        print(f"  {section_type}:")
        print(f"    Avg: {section_data.mean():7.0f} | Min: {section_data.min():5.0f} | "
              f"Max: {section_data.max():5.0f} | Count: {len(section_data)}")
    
    # 5. Per-Document Chunk Count
    print_section_divider("CHUNKS PER DOCUMENT")
    doc_chunks = df['source'].value_counts().sort_index()
    total_docs = len(doc_chunks)
    for idx, (source, count) in enumerate(doc_chunks.head(10).items(), 1):
        print(f"  {idx:2}. {source:40} : {count:4} chunks")
    if total_docs > 10:
        print(f"  ... and {total_docs - 10} more documents")
    
    # 6. Sample Chunks from Each Section Type
    print_section_divider("SAMPLE CHUNKS")
    for section_type in df['section_type'].unique():
        section_chunks = df[df['section_type'] == section_type]
        if len(section_chunks) > 0:
            sample = section_chunks.iloc[0]
            print(f"\n  [{section_type.upper()}]")
            print(f"  Source: {sample['source']}")
            print(f"  Section: {sample['section_title']}")
            print(f"  Chunk ID: {sample['chunk_id']}")
            print(f"  Length: {len(sample['text'])} characters\n")
            
            # Show first 200 chars of chunk
            preview = sample['text'][:200]
            wrapped = textwrap.fill(preview, width=76, initial_indent="  ", 
                                   subsequent_indent="  ")
            print(wrapped)
            if len(sample['text']) > 200:
                print("  ...")
    
    return df


if __name__ == "__main__":
    config = yaml.safe_load(open("ai_integration/config.yaml"))
    docs = load_documents("data/raw/")
    chunks = chunk_documents(
        docs,
        config["chunk_size"],
        config["chunk_overlap"]
    )
    
    print(f"\nLoaded {len(docs)} documents")
    print(f"Created {len(chunks)} chunks")
    print(f"Chunk size: {config['chunk_size']}, Overlap: {config['chunk_overlap']}")
    
    # Perform analysis
    df = analyze_chunks(chunks)
    
    print_section_divider("ANALYSIS COMPLETE")