import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os


def send_email(sender_email, sender_password, receiver_email, subject, body, attachment=None):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment:
        part = MIMEApplication(attachment, Name=os.path.basename("example.txt"))
        part['Content-Disposition'] = f'attachment; filename="example.txt"'
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

def create_file_with_size(size_in_megabytes):
    file_name = 'example.txt'
    size_in_bytes = size_in_megabytes * 1_000_000  # in megabytes
    chunk_size = 1024 * 1024
    with open(file_name, 'wb') as f:
        for _ in range(size_in_bytes // chunk_size):
            f.write(b'\0' * chunk_size)
        remaining_bytes = size_in_bytes % chunk_size
        if remaining_bytes:
            f.write(b'\0' * remaining_bytes)
    print(f"File '{file_name}' created with size {size_in_bytes / 1_000_000} megabytes.")
    return file_name
