import smtplib
import os
import mimetypes
from email.message import EmailMessage

Mail = EmailMessage()
Mail["To"] = r'receiver@email.com'
Mail["From"] = r'sender@email.com'
Mail["Subject"] = r'Python'

Body = r'Its working yesssssssssss !!!!!!!'
Mail.set_content(Body)
Path = r'C:\Users\admin\Desktop\test13.jpg' #full Absolute Path To Attachment

File = open(Path, "rb")
data = File.read()
Mail.add_attachment(data, maintype = "Image", subtype = "jpg" , filename="test13.jpg")
mail_server = smtplib.SMTP("smtp.gmail.com:587")

mail_server.starttls()
mail_server.login("email","password")
mail_server.sendmail("sender_email", "receiver_email", Mail.as_string())
mail_server.quit()

