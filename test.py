'''
Created on Sep 12, 2017

@author: admin
'''
# importing required modules
import PyPDF2
import os
import csv
os.chdir("C:/Users/admin/Desktop")
# creating a pdf file object
pdfFileObj = open('example.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
print(pdfReader.numPages)
download_dir = "exampleCsv3.csv" #where you want the file to be downloaded to 

csv = open(download_dir, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "PNR, Roll, Name, mother, Sgpa, Credit,\n"
csv.write(columnTitleRow)

for x in range(0,112):
    pageObj = pdfReader.getPage(x)
    S=pageObj.extractText()
    
    
    
    Name1=S[441:471]
    Roll1=S[429:439] 
    Sgpa1=S[1729:1733]
    Mother1=S[490:500]
    Credit1=S[1751:1754]
    Pnr1=S[521:530]
    
    name = Name1
    roll = Roll1
    sgpa = Sgpa1
    mother =Mother1
    PNR=Pnr1
    Credit=Credit1
    row = PNR + "," + roll +","+name+","+mother+","+sgpa+","+Credit+","+"\n"
    csv.write(row)
    
    Name2=S[1875:1904] 
    Roll2=S[1863:1873]
    Sgpa2=S[3163:3167]
    Mother2=S[1924:1934]
    Credit2=S[3185:3188]
    Pnr2=S[1955:1964]
    
   
    
    name = Name2
    roll = Roll2
    sgpa = Sgpa2
    mother=Mother2
    PNR=Pnr2
    Credit=Credit2
    row = PNR + "," + roll +","+name+","+mother+","+sgpa+","+Credit+","+"\n"
    csv.write(row)


pdfFileObj.close()


