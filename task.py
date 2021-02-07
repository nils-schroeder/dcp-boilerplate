import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

smtp_port = "<SMTP_SERVER_PORT>"
smtp_server = "<SMTP_SERVER_ADRESS>"
sender_mail = "<EMAIL>"
sender_pw = "<PASSWORD>"
recipients = ["<EMAIL_1>", "<EMAIL_2>"]

def send_alert(title, message):
    message = MIMEMultipart("alternative")
    message["Subject"] = f"{title}"
    message["From"] = sender_mail
    message["To"] = ", ".join(recipients)
    body = f"{message}"
    message.attach(MIMEText(body, "html"))
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=context)
        server.login(sender_mail, sender_pw)
        server.sendmail(sender_mail, recipients, message.as_string())

if __name__ == "__main__":
    print(f"Running script at {datetime.now()}")
    send_alert("This message is sent every 30 minutes", "<h1>Hello World from a Docker container</h1>")