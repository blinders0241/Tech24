from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file, docx_file):
    # Create a Converter object
    cv = Converter(pdf_file)

    # Convert the PDF to a DOCX file
    cv.convert(docx_file, start=0, end=None)

    # Close the PDF file
    cv.close()

# Usage
filePath = r"C:\SIMPLY_Official\2024\TechHome241\drfcore\home\mylibs\FileConvert\\"
convert_pdf_to_docx(filePath + 'asiddique_20240311T144835Z.pdf', 'output.docx')
