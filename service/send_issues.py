import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText


def send_email_with_attachment(smtp_server,
                               port,
                               sender_email,
                               password,
                               recipient_email,
                               subject,
                               body,
                               file_path,
                               sender,
                               receiver):
    # Setup multipart email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach file
    attachment = open(file_path, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + file_path)

    msg.attach(part)

    # Start SMTP session
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()

    # Authentication
    server.login(sender_email, password)

    # Sending the email
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()
