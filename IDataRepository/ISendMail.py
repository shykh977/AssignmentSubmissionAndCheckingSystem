import abc


class ISendMail( abc.ABC ):
    @abc.abstractclassmethod
    def MailSend(self,subject, body, recipients):
        pass
