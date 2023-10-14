import fitz
path = "./data/sample.pdf"
doc = fitz.open(path)
for page in doc:
    text = page.get_text()
    print(text)