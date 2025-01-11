from pdf2image import convert_from_path
import pytesseract
import pypdf

def ocr_pdf_to_text(pdf_path):
    images = convert_from_path(pdf_path,poppler_path='/path/to/poppler/bin')
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    return text

# pdf_path = "/Users/vasudevan/Downloads/II PUC Eng TB.pdf"
# text = ocr_pdf_to_text(pdf_path)
# print(text)

def read_pdf(path,max_pages=20):
    if path is None:
        return None
    reader = pypdf.PdfReader(path)
    data=[]
    for i in range(len(reader.pages)):
        if max_pages<=i:
            break
        data.append(reader.pages[i].extract_text())
    text = "\n".join(data)
    text = split_text_by_word_count(text)
    return text
    

def split_text_by_word_count(text, word_limit=300):
    words = text.split()
    sections = [' '.join(words[i:i + word_limit]) for i in range(0, len(words), word_limit)]
    return sections
