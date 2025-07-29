import pyPDF2
import re
import string

file_handle = open("Sense_and_Sensibility.txt", "rb")
readr = pyPDF2.PdfFileReader(file_handle)
page_number = len(readr.pages)
freq_table = {}
for i in range(page_number):
    page_object = reader.pages[i]
    page_text = page_object.extract_text()
    lines = page_text.split('\n')