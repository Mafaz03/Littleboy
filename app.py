import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import threading
from helper import create_file_with_size, send_email  
import gradio as gr


def send_emails(sender_email, sender_password, receiver_email, subject, body, times, file_size, attachment, file_path):
    try:
        threads = []
        for time in range(1, times + 1):
            if times > 1:
                current_subject = f"{subject} ({time}/{times})"
                current_body = f"{body} ({time}/{times})"
            else:
                current_subject = subject
                current_body = body

            # Create a thread for each email sending task
            thread = threading.Thread(target=send_email, args=(sender_email, sender_password, receiver_email, current_subject, current_body, attachment))
            threads.append(thread)
            print(f"Starting {time}/{times}")
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        os.remove(file_path)  # Clean up the created file after sending emails
        print(f"All emails sent successfully! {times} times. Total file size: {file_size*times} MB")
    except Exception as e:
        print(f"Error: {str(e)}")


def sendit(sender_email, sender_password, receiver_email, subject, body, times, file_size_50_max):
    file_path = create_file_with_size(int(file_size_50_max))
    with open(file_path, 'rb') as f:
        attachment = f.read()
    
    thread = threading.Thread(target=send_emails, args=(sender_email, sender_password, receiver_email, subject, body, int(times),file_size_50_max, attachment, file_path))
    thread.start()

    return "Email sending in progress. You will be notified once completed."

demo = gr.Interface(
    fn=sendit,
    inputs=["text", "text", "text", "text", "text", "text", "slider"],
    outputs=["text"]
)

demo.launch(share=True)