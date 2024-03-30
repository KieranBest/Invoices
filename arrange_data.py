import csv
import os
import datetime
from datetime import datetime
import shutil
import csv

def csv_Arrange():
    from_year = str(datetime.now().year)
    from_month = str(datetime.now().month)
    invoice_ID = 0

    os.chdir('Invoices/')

    if (from_month == '12'):
        to_month = '1'
        to_year = str(int(from_year) + 1)
        from_folder = from_year + '/' + from_month + '/Invoices.csv'
    else:
        to_month = str(int(from_month) + 1)
        to_year = from_year
        from_folder = from_year + '/' + from_month + '/Invoices.csv'
    
    copy_to = to_year + '/' + to_month + '/'

    if not os.path.exists(to_year):
        os.makedirs(to_year + '/')
    os.chdir(to_year)

    if not os.path.exists(to_month):
        os.makedirs(to_month + '/')
    os.chdir(to_month)

    os.chdir('../../')
    shutil.copy(from_folder, copy_to)

    os.chdir(copy_to)
    with open('Invoices.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                invoice_ID = row[1]
    
    op = open("Invoices.csv", "r") 

    dt = csv.DictReader(op) 
    up_dt = [] 
    for r in dt: 
        print(invoice_ID)
        new_invoice_ID = int(r['Invoice']) + int(invoice_ID)
        print(f'{new_invoice_ID:0>4}')
        row = {'ID': r['ID'], 
            'Invoice': f'{new_invoice_ID:0>4}', 
            'Name': r['Name'], 
            'Website': r['Website'], 
            'Email': r['Email'],
            'Address1': r['Address1'],
            'Address2': r['Address2'],
            'AddressTown': r['AddressTown'],
            'AddressPostcode': r['AddressPostcode'],
            'Monthly': r['Monthly'],
            'MonthlyAdditional': '0',
            'Total': r['Monthly']} 
        up_dt.append(row) 
    op.close() 
    op = open("Invoices.csv", "w", newline='') 
    headers = ['ID', 'Invoice', 'Name', 'Website', 'Email', 'Address1', 'Address2', 'AddressTown', 'AddressPostcode', 'Monthly', 'MonthlyAdditional', 'Total'] 
    data = csv.DictWriter(op, delimiter=',', fieldnames=headers) 
    data.writerow(dict((heads, heads) for heads in headers)) 
    data.writerows(up_dt) 
    op.close() 
csv_Arrange()