import smtplib


def send_email(sender_email, receiver_email, password, subject, body):
    port = 465 # For SSL
    smtp_server = "smtp.gmail.com"

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


sender_email = input("Type your email: ")
password = input("Type your password: ")
receiver_email = input("Type receiver's email: ")
subject = input("Type subject: ")
body = input("Type message: ")
send_email(sender_email, receiver_email, password, subject, body)
