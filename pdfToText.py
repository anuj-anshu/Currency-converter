import PyPDF2
a = PyPDF2.PdfFileReader("Founder's Profile.pdf")
b = a.getNumPages()
str = ""
for i in range(0,b):
    str += a.getPage(i).extractText()

with open("text.txt",'w', encoding='utf-8') as f:
    f.write(str)