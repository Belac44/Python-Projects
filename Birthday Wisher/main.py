import smtplib

my_email = "cale@gmail.com"
password="abcd123.."

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addr="caleb.bosire1")
connection.close()