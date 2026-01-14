import smtplib
from config import *

def send_alert(ip):
    if not ENABLE_EMAIL_ALERTS:
        return

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    subject = "Honeypot Alert"
    body = f"Suspicious repeated intrusion attempts detected from {ip}"

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail(ADMIN_EMAIL, ALERT_TO, message)
    server.quit()
