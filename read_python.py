import pyttsx3
import PyPDF2
book = open('/home/husenbeg/Downloads/dsa_with_python.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages
print(pages)
speaker = pyttsx3.init()
#speaker.say("Hello I love you Muskan")
#speaker.runAndWait()
for num in range(21, pages):
    page = pdf_reader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
