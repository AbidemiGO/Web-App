import smtplib, ssl
from wsgiref.simple_server import server_version

username = "femigbenga3470@gmail.com"
password = "fqzd ittr hgwp dfvb"
receiver = "femigbenga3470@gmail.com"

host = "smtp.gmail.com"
post = 465
message = '''\
Subject: Hi! 
You are accepted
Bye!
'''
context = ssl.create_default_context()
with smtplib.SMTP_SSL(host, post, context = context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

