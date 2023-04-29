''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

import smtplib
import os
import schedule
import logging
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

sender_email = "juanjosecreusramos@hotmail.com"
sender_password = "3w8JiHDEueUiHd"
recipient_emails = ["juanjocr00@gmail.com", "creusjuan9@gmail.com"]
subject = "Daily Report"
body = "Please find attached the daily report."
attachment_path = "./JuanJoseCreus_automate_email_sending/test_report.txt"

logging.basicConfig(filename='./JuanJoseCreus_automate_email_sending/email_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email():
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ", ".join(recipient_emails)
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    with open(attachment_path, "rb") as file:
        part = MIMEApplication(file.read(), Name=os.path.basename(attachment_path))
    part["Content-Disposition"] = f"attachment; filename={os.path.basename(attachment_path)}"
    message.attach(part)
    
    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:    #This is for Outlook servers, for gmail is smtp.gmail.com
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            print("Email sent successfully")
            logging.info(f"Email sent to {recipient_emails} successfully")
    except Exception as e:
        logging.error(f"An error occurred while sending the email: {str(e)}")
        print(f"An error occurred while sending the email: {str(e)}")

schedule.every().day.at("12:00").do(send_email)
while True:
    schedule.run_pending()
    time.sleep(60) 
