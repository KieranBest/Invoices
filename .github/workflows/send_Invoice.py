import js2py

year = str(datetime.now().year)
month = str(datetime.now().month)
date = datetime.now().strftime("%d-%m-%Y")

if (month == '1'):
    invoice_month = '12'
    invoice_year = str(int(year) - 1)
else:
    invoice_month = month
    invoice_year = year
from_folder = invoice_year + '/' + invoice_month + '/Invoices.csv'

def send_Invoice():

    os.chdir('Invoices/' + invoice_year + '/' + invoice_month + '/')


    with open('Invoices.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
                email_params = {
                    'name': row[2],
                    'email': row[4],
                    'attachment': row[1] + 'Invoice_' + date + '.pdf',
                }

            send_email = """
            emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', email_params).then(
            (response) => {
                console.log('SUCCESS!', response.status, response.text);
            },
            (error) => {
                console.log('FAILED...', error);
            },
            );
            """

            js2py.eval_js(send_email)

send_Invoice()