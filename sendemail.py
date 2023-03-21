class Send_Email():
    def __init__(self):
        self.faddress = "youngstarsairam@gmail.com"
        self.taddress = "sairambadiga@gmail.com"
        self.password = "vlcerbchfalneyav"
        self.message = "Hi this is a deafault mail body"

    def SendMail(self, fromusername, tousername, message):
        try:
            self.faddress = fromusername
            self.taddress = tousername
            self.message = message
            # message['Subject'] = 'your_subject'
            conn = SMTP_SSL("SMTP.gmail.com")
            conn.login(user=self.faddress, password=self.password)
            conn.sendmail(from_addr=self.faddress, to_addrs=self.taddress, msg=self.message)
        except Exception as e:
            print(e)
        finally:
            conn.close()

