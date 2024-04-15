import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "jrasgado01@gmail.com"
password = "hith sqfn dbaj xpfu"

receiver = "jrasgado01@hotmail.com"
context = ssl.create_default_context()

message = """\
Subject : Contact back
How are you?
Bye
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)