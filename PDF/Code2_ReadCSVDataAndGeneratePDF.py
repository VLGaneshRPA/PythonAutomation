# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/
  
import pandas
from fpdf import FPDF
  
df = pandas.read_excel('data.xlsx')
# print(df)
  
# This code snippet is iterating over each row in the DataFrame `df`.   Command + / to comment
# for index, row in df.iterrows():
#     txt  = row['kingdom']
#     print(f'{index} - {txt}')
#     for col in df.columns[1:]:
#         print(col.title())
    
for index, row in df.iterrows():
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=1)

    for column in df.columns[1:]:
        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt=f"{column.title()}:")

        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=row[column], ln=1)


    pdf.output(f"{row['name']}.pdf")