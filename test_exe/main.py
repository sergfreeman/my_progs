# from email.message import EmailMessage
# import webbrowser
# import smtplib
# url = 'http://sergfreeman.zzz.com.ua/index.html/'
#
#
#
#
# message = EmailMessage()
# message.set_content('Message content here')
# # message['Password'] = 'banca.bank21'
# message['Subject'] = 'Your subject here'
# message['From'] = 'banca.bank@meta.ua'
# message['To'] = 'sergandd@gmail.com'
#
# smtp_server = smtplib.SMTP('smtp.meta.ua:465')
# smtp_server.login('banca.bank@meta.ua', 'banca.bank21')
# smtp_server.sendmail('banca.bank@meta.ua','sergandd@gmail.com','test')
#
# # smtp_server.password = 'banca.bank21'
# smtp_server.send_message(message)
# smtp_server.quit()
#
# webbrowser.open(url)
import time
import smtplib
import ssl
from email.mime.text import MIMEText

sender = 'banca.bank@meta.ua'
receivers = ['sergandd@gmail.com']

port = 465
user = 'banca.bank@meta.ua'
password = 'banca.bank21'

msg = MIMEText("""
    Hello, dear client. 
We have sent your password. Thank you for your cooperation. 
If you don't enter in our base, forget this letter.
""")

msg['Subject'] = 'Remember a password'
msg['From'] = 'banca.bank@meta.ua'
msg['To'] = 'sergandd@gmail.com'

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.meta.ua", port, context=context) as server:

    server.login(user, password)

    server.sendmail(sender, receivers, msg.as_string())

    print('mail successfully sent')
