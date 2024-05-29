import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os


def create_file_with_size(size_mb):
    file_path = 'attachment_file.txt'
    size_bytes = size_mb * 1024 * 1024  # Convert MB to bytes
    with open(file_path, 'wb') as f:
        f.write(os.urandom(size_bytes))
    return file_path

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    part = MIMEApplication(attachment, Name='attachment_file.txt')
    part['Content-Disposition'] = 'attachment; filename="attachment_file.txt"'
    msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
