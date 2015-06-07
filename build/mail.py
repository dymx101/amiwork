import smtplib, base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mail(to, subject, message, file_to_send,filename=None):
	fromaddr = 'krishnancmf8@gmail.com'
	toaddrs  = to
	
	
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = 'krishnancmf8@gmail.com'
	msg['To'] = to
	
	if file_to_send is not None:
		f = file(file_to_send)
		attachment = MIMEText(f.read())
		if filename is None:
			filename = file_to_send
		attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
		msg.attach(attachment)
	
	server = smtplib.SMTP('localhost')
	server.sendmail(fromaddr, toaddrs, msg.as_string())#msg) #
	server.quit()
