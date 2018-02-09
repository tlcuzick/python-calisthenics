import copy
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = '../book1-exercises-master/chp11/practice_files'

outputPDF = PdfFileWriter()

cover_file_name = os.path.join(path, 'Emperor cover sheet.pdf')
cover_file = PdfFileReader(open(cover_file_name, 'rb'))

cover_page = cover_file.getPage(0)
outputPDF.addPage(cover_page)

main_file_name = os.path.join(path, 'The Emperor.pdf')
main_file = PdfFileReader(open(main_file_name, 'rb'))

num_pages = main_file.getNumPages()

for page_num in range(0, num_pages):
    page = main_file.getPage(page_num)
    outputPDF.addPage(page)
    
output_file_path = os.path.join(path, 'output/The Covered Emperor.pdf')
output_file = open(output_file_path, "wb")
outputPDF.write(output_file)
output_file.close()


            
            
                
    
