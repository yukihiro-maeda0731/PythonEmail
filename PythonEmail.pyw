import smtplib, ssl

def read_creds():
    user = passw = ""
    with open("credentials.txt", "r", encoding="utf-8") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw


port = 465

sender, password = read_creds()

receiver = sender

message = """\
Subject: Pythonmailtest

sending email via python

"""

context = ssl.create_default_context()

print("Starting to send")
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)

print("sent email!")