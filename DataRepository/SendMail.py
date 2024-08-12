


from IDataRepository.ISendMail import ISendMail
import smtplib
from email.mime.text import MIMEText

class Mailing(ISendMail):
    def MailSend(self,subject, body, recipients):


        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "btgtechnologies2021@gmail.com"
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
         smtp_server.login("btgtechnologies2021@gmail.com", "qsokaccacxqnctsn")
         smtp_server.sendmail("btgtechnologies2021@gmail.com", recipients, msg.as_string())


         return "Mail Send"
    

