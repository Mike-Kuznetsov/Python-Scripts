#This script sends mail to your address

fromaddr = ""
toaddr = ""
mypass = ""
subject = ""
body = ""
server = "smtp.mail.ru" # I use mail.ru to send notifications to my address
port = 465

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject
 

msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP_SSL(server, port)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
