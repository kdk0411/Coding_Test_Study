from PyPDF2 import PdfReader
reader = PdfReader("전공영어1.pdf")
pages = reader.pages
text = ""
for page in pages:
    sub = page.extract_text()
    text += sub
print(text)