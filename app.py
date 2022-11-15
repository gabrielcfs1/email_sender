from email.message import EmailMessage
from password import password
import ssl 
import smtplib 

# COLOCAR EMAIL QUE IRA ENVIAR
email_sender = ''
email_password = password

# COLOCAR EMAIL QUE IRA RECEBER
email_receiver = ''

# ASSUNTO
subject = 'TESTE EMAIL SENDER PYTHON'
# CORPO DO EMAIL 
body = """
TESTANDO CORPO EMAIL SENDER PYTHON
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver  
em['Subject'] = subject
em.set_content(body)

# CREATE SSL CONTEXT
context = ssl.create_default_context()

# CONNECTION WITH SMTP SERVER 
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
