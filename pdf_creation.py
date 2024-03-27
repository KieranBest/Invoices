from fpdf import FPDF
import csv
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta


files_list = []
today = datetime.now() - relativedelta(days=+1)
last_day = today.strftime("%A %d %B %Y")
date = datetime.now().strftime("%d-%m-%Y")
last_month = datetime.now() - relativedelta(months=+1)
last_month = last_month.strftime("%A %d %B %Y")


class PDF(FPDF):
    def header(self):
        self.image('favicon.png', 155, 10, 40)
        self.set_font('Helvetica', 'B', 28)
        self.cell(80)
        self.cell(30, 30, 'INVOICE', 0, 1, 'C')
        self.ln(25)

    def footer(self):
        self.set_y(-20)
        self.set_font('Helvetica', '', 16)
        self.cell(0, 10, 'Best Web Dev', 0, 0, 'C')

def csvReader():
    with open('Invoices.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            file_name = row[1] + '_Invoice_' + date + '.pdf'
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
                pdf = PDF()
                pdf.add_page()
                pdf.set_font('Helvetica', '', 14)



                pdf.cell(0,10,row[0],0,1,'R')
                pdf.cell(0,10,date,0,1,'R')
                pdf.cell(0,10,'Name: ' + row[1],0,1,'L')
                pdf.cell(0,10,'Website: ' + row[2],0,1,'L')
                pdf.cell(0,10,'Email: ' + row[3],0,1,'L')
                pdf.cell(0,10,'Address: ' + row[4] + ", " + row[5] + ", " + row[6] + ", " + row[7],0,1,'L')
                pdf.cell(0,10,'Invoice Period: ' + last_month + ' - ' + last_day,0,1,'L')

                pdf.ln(15)

                pdf.cell(0,10,'Description',0,0,'L')
                pdf.cell(0,10,'Amount',0,1,'R')
                pdf.cell(0,10,'Monthly Fee',0,0,'L')
                pdf.cell(0,10,''.join(['£', format(float(row[8]), ',.2f')]),0,1,'R')
                if row[9] != f'0':
                    pdf.cell(0,10,'Additional Fee',0,0,'L')
                    pdf.cell(0,10,''.join(['£', format(float(row[9]), ',.2f')]),0,1,'R')
                pdf.cell(0,10,'Total Due',0,0,'L')
                pdf.cell(0,10,''.join(['£', format(float(row[10]), ',.2f')]),0,1,'R')

                pdf.output(file_name + '.pdf', 'F')

csvReader()