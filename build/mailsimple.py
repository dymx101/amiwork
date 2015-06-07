import smtplib, base64
from email.mime.text import MIMEText

def mail_text(to, subject, message):
	fromaddr = 'krishnancmf8@gmail.com'
	toaddrs  = to
	
	
	msg = MIMEText(message)
	msg['Subject'] = subject
	msg['From'] = 'krishnancmf8@gmail.com'
	msg['To'] = to
	
	server = smtplib.SMTP('localhost')
	server.sendmail(fromaddr, toaddrs, msg.as_string())#msg) #
	server.quit()




