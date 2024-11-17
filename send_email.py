import smtplib, ssl


def send_email(message):
    username = "femigbenga3470@gmail.com"
    password = "fqzd ittr hgwp dfvb"
    receiver = "femigbenga3470@gmail.com"

    host = "smtp.gmail.com"
    post = 465

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, post, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

