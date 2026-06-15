from pypdf import PdfReader, PdfWriter

pages = [1, 2, 3, 4, 5, 6, 7, 8]  # pages 5,12,27,80

reader = PdfReader("NASDAQ_TSLA_2022.pdf")
writer = PdfWriter()

for p in pages:
    writer.add_page(reader.pages[p])

with open("important_pages.pdf", "wb") as f:
    writer.write(f)