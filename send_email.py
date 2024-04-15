import smtplib, ssl


def send_email(receiver, message):
    host = "smtp.gmail.com"
    port = 465
    username = "jrasgado01@gmail.com"
    password = "hith sqfn dbaj xpfu"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
