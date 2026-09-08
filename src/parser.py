import pdfplumber
from docx import Document
import pytesseract
import fitz


# Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text_from_pdf(file):
    """Extract text from normal or scanned PDF."""

    text = ""

    # First try normal PDF text extraction
    try:
        with pdfplumber.open(file) as pdf:

            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception:
        text = ""

    # If normal extraction gives no text,
    # use OCR
    if not text.strip():

        try:
            file.seek(0)

            pdf_data = file.read()

            pdf = fitz.open(
                stream=pdf_data,
                filetype="pdf"
            )

            for page in pdf:

                pix = page.get_pixmap(
                    matrix=fitz.Matrix(2, 2)
                )

                image = pix.tobytes("png")

                from PIL import Image
                import io

                img = Image.open(
                    io.BytesIO(image)
                )

                page_text = pytesseract.image_to_string(
                    img
                )

                text += page_text + "\n"

            pdf.close()

        except Exception as e:

            print("OCR Error:", e)
            return ""

    return text.strip()


def extract_text_from_docx(file):
    """Extract text from DOCX resume."""

    text = ""

    try:

        document = Document(file)

        for paragraph in document.paragraphs:

            if paragraph.text.strip():
                text += paragraph.text + "\n"

    except Exception as e:

        print("DOCX extraction error:", e)
        return ""

    return text.strip()


def extract_resume_text(file):
    """Detect file type and extract resume text."""

    file_name = file.name.lower()

    if file_name.endswith(".pdf"):

        return extract_text_from_pdf(file)

    elif file_name.endswith(".docx"):

        return extract_text_from_docx(file)

    return ""