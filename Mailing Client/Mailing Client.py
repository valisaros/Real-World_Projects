import smtplib
from email import encoders
from email.mine.text import MIMEText
from email.mime.text import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('email', password)

msg = MIMEMultipart()
msg['From'] = 'Vali'
msg['To'] = 'testmails@spam1.de'
msg['Subject'] = 'Just A Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'image.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition, f'attachment; filename={filename})

text = msg.as_string()
server.sendmail('mailtesting@vali.com', 'testmail@spam1.de', text)