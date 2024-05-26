from flask import Flask, render_template, request
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from helper import *

app = Flask(__name__)

# sender_mail = "4tpurpose101@gmail.com"
# sende_password = "ajfd nsvb lztl ceev"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    sender_email = request.form['sender_email']
    sender_password = request.form['sender_password']
    receiver_email = request.form['receiver_email']
    subject = request.form['subject']
    body = request.form['body']
    times = int(request.form['times'])
    file_size = int(request.form['file_size'])  # Convert to integer

    # Create file with specified size
    file_path = create_file_with_size(file_size)
    with open(file_path, 'rb') as f:
        attachment = f.read()

    # Send Email
    try:
        for time in range(1, times + 1):
            if times > 1:
                current_subject = f"{subject} ({time}/{times})"
                current_body = f"{body} ({time}/{times})"
            else:
                current_subject = subject
                current_body = body
            
            send_email(sender_email, sender_password, receiver_email, current_subject, current_body, attachment)
            print(f"Email sent ({time}/{times})")
        
        os.remove(file_path)  # Clean up the created file after sending emails
        return f"Email sent successfully! {times} times. total file size: {file_size*times} MB"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
