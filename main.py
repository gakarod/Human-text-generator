import PyPDF2
from fpdf import FPDF

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(3)
text = pageObj.extractText()
pdfWriter = PyPDF2.PdfFileWriter()
pdf = FPDF(format='a4')

pdf.add_page()
pdf.add_font('cedar', '', 'Cedarville-Cursive.ttf', uni=True)
pdf.set_font('cedar')
pdf.set_text_color(65,105,225)
pdf.set_xy(0, 0)
for i in str(text):
    pdf.write(5,i)

pdf.output('test.pdf', 'F')
