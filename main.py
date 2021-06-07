import csv, smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
context = ssl.create_default_context()

message = """Subject: Type Subject
To: {recipient}
From: {sender}

Hello {name}

Type Your Message
"""
sender = "Youremail@gmail.com"

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("Youremail@gmail.com", "Pasword")
    with open("test.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for name, email in csv_reader:
            server.sendmail(
                sender,
                email,
                message.format(name=name, recipient=email, sender=sender)      
            )
            print(f'Sent to {name}')