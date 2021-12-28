import PyPDF2
file=open('Good Programmers.pdf','rb')
reader=PyPDF2.PdfFileReader(file)
page2=reader.getPage(1)
print(page2.extractText())

